from django.shortcuts import render
from room.models import Room  # Import your Room model
from django.contrib.auth.decorators import login_required  # Import login_required

# Create your views here.
def get_home(request):
    rooms = Room.objects.all()  # Fetch all room instances
    context = {
        'rooms': rooms,  # Pass the rooms data to the template
    }
    return render(request, "content.html", context)

<<<<<<< HEAD
@login_required(login_url='/login')  # Nếu chưa đăng nhập, chuyển hướng đến trang login
def home(request):
    rooms = Room.objects.all()  # Lấy tất cả dữ liệu phòng từ database
    
    # Thông tin người dùng (in ra để kiểm tra)
    print(f"User is logged in: {request.user.username}")
    
    context = {
        'rooms': rooms,  # Truyền dữ liệu phòng vào template
        'user': request.user  # Truyền thông tin người dùng vào template
    }
    return render(request, 'content.html', context)
=======

>>>>>>> edit_by_huong
