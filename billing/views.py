# billing/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HostelMember, Attendance

def mark_attendance(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        member = HostelMember.objects.get(id=member_id)
        Attendance.objects.create(member=member)
        messages.success(request, 'Attendance marked successfully.')
        return redirect('mark_attendance')
    else:
        hostel_members = HostelMember.objects.all()
        return render(request, 'billing/mark_attendance.html', {'hostel_members': hostel_members})
