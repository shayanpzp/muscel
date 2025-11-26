# workout/views.py
from django.shortcuts import render, redirect
from .forms import QuestionnaireForm

# قیمت نمونه — می‌تونی تغییر بدی
PRICES = {
    "beginner": 200000,  # تومان
    "pro": 500000,
}

WORKOUT_TYPES = [
    ("bodybuilding", "بادی بیلدینگ"),
    ("crossfit", "کراس فیت"),
    ("powerlifting", "پاور لیفتینگ"),
    ("trx", "TRX"),
    ("cardio", "هوازی (cardio)"),
    ("pilates", "پیلاتس"),
    ("yoga", "یوگا"),
]

def home(request):
    return render(request, "workout/home.html", {"workout_name": "Muscle Factory"})

def questionnaire(request):
    if request.method == "POST":
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # ذخیره در سشن برای استفاده در صفحات بعدی
            request.session["user_data"] = data
            return redirect("workout:bmi_result")
    else:
        form = QuestionnaireForm()
    return render(request, "workout/questionnaire.html", {"form": form})

def bmi_result(request):
    data = request.session.get("user_data")
    if not data:
        return redirect("workout:questionnaire")

    # محاسبه BMI
    weight = float(data.get("weight") or 0)
    height_cm = float(data.get("height") or 0)
    height_m = height_cm / 100 if height_cm else 0
    bmi = None
    ideal_weight = None
    status = ""
    if height_m > 0:
        bmi = weight / (height_m ** 2)
        # وزن ایده‌آل بر اساس BMI هدف 22
        ideal_weight = 22 * (height_m ** 2)
        # وضعیت عمومی BMI
        if bmi < 18.5:
            status = "کمبود وزن"
        elif 18.5 <= bmi < 25:
            status = "وزن نرمال"
        elif 25 <= bmi < 30:
            status = "اضافه وزن"
        else:
            status = "چاقی"

    # ذخیره چند مقدار برای ادامه
    request.session["bmi_info"] = {
        "bmi": round(bmi, 2) if bmi else None,
        "ideal_weight": round(ideal_weight, 1) if ideal_weight else None,
        "status": status,
    }
    return render(request, "workout/bmi_result.html", {"bmi_info": request.session["bmi_info"], "user": data})

def choose_program(request):
    if not request.session.get("user_data"):
        return redirect("workout:questionnaire")

    if request.method == "POST":
        chosen = request.POST.get("workout_type")
        request.session["chosen_workout"] = chosen
        return redirect("workout:price")

    return render(request, "workout/choose_program.html", {"workouts": WORKOUT_TYPES})

def price(request):
    user = request.session.get("user_data")
    bmi_info = request.session.get("bmi_info")
    chosen = request.session.get("chosen_workout")
    if not user or not chosen:
        return redirect("workout:choose_program")

    # مثال: قیمت‌ها میتونه وابسته به نوع ورزش هم باشه؛ برای ساده‌سازی همشون برابر
    price_beginner = PRICES["beginner"]
    price_pro = PRICES["pro"]

    workout_display = dict(WORKOUT_TYPES).get(chosen, "نامشخص")

    return render(request, "workout/price.html", {
        "user": user,
        "bmi_info": bmi_info,
        "workout": workout_display,
        "price_beginner": price_beginner,
        "price_pro": price_pro,
    })