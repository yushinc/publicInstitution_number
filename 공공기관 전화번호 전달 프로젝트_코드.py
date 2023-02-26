from tkinter import *
import tkinter.font as font

#상담-------------------------------------------------------------------------
def counseling():
    #아동
    def Child():
        #실종
        def Missing():
            Child.destroy()
            Missing = Tk()
            Missing.title("실종")
            Missing.geometry('300x200')

            #실종
            label1 = Label(Missing, text='경찰청 실종아동찾기센터', font=30)
            label2 = Label(Missing, text='182', font=30)
            label3 = Label(Missing, text='실종아동전문기관', font=30)
            label4 = Label(Missing, text='02-777-0182', font=30)

            label1.pack()
            label2.pack()
            label3.pack()
            label4.pack()

            Missing.mainloop()

        #보호
        def ChildProtect():
            #학대아동 보호 및 예방
            def ChildProtect2():
                ChildProtect.destroy()
                ChildProtect2 = Tk()
                ChildProtect2.title("학대아동 보호 및 예방")
                ChildProtect2.geometry('300x200')

                label1 = Label(ChildProtect2, text = "중앙아동보호전문기관", font=30)
                label2 = Label(ChildProtect2, text = "112", font=30)
                
                label1.pack()
                label2.pack()
                
                ChildProtect2.mainloop()

            #아동 성폭력 피해자 상담, 치료, 신고, 지원
            def ChildProtect3():
                ChildProtect.destroy()
                ChildProtect3 = Tk()
                ChildProtect3.title("아동 성폭력 피해자 상담, 치료, 신고, 지원")
                ChildProtect3.geometry('300x200')

                label1 = Label(ChildProtect3, text='해바라기아동센터', font=30)
                label2 = Label(ChildProtect3, text='02-3274-1375', font=30)
                
                label1.pack()
                label2.pack()
                
                ChildProtect3.mainloop()

            #보호
            Child.destroy()
            ChildProtect = Tk()
            ChildProtect.title("보호")
            ChildProtect.geometry('300x200')

            hbtn1 = Button(ChildProtect, text='학대아동 보호 및 예방', command=ChildProtect2)
            hbtn2 = Button(ChildProtect, text='아동 성폭력 피해자 \n상담, 치료, 신고, 지원', command=ChildProtect3)

            hbtn1['font'] = myFont
            hbtn2['font'] = myFont

            
            hbtn1.pack(side=TOP, fill=X, ipadx=33, ipady=33)
            hbtn2.pack(side=TOP, fill=X, ipadx=33, ipady=33)

            ChildProtect.mainloop()

        #상담, 치료, 심리검사
        def Psychology():
            Child.destroy()
            Psychology = Tk()
            Psychology.title("상담, 치료, 심리검사")
            Psychology.geometry('300x200')

            label1 = Label(Psychology, text = "한국아동청소년 심리상담센터", font=30)
            label2 = Label(Psychology, text = "02-511-5080", font=30)

            label1.pack()
            label2.pack()

            Psychology.mainloop()
            
        #아동
        counseling.destroy()
        Child = Tk()
        Child.title("아동")
        Child.geometry('300x200')

        fbtn1 = Button(Child, text='실종', command=Missing)
        fbtn2 = Button(Child, text='보호', command=ChildProtect)
        fbtn3 = Button(Child, text='상담, 치료, 심리검사', command=Psychology)

        fbtn1['font'] = myFont
        fbtn2['font'] = myFont
        fbtn3['font'] = myFont

        fbtn1.pack(side=TOP, fill=X, ipadx=16, ipady=16)
        fbtn2.pack(side=TOP, fill=X, ipadx=16, ipady=16)
        fbtn3.pack(side=TOP, fill=X, ipadx=16, ipady=16)


        Child.mainloop()
        #아동 끝

    #청소년
    def teenager():
        #학교폭력
        def schoolViolence():
            #예방교육 및 상담
            def schoolViolence2():
                schoolViolence.destroy()
                schoolViolence2 = Tk()
                schoolViolence2.title("예방교육 및 상담")
                schoolViolence2.geometry('300x200')

                #예방교육 및 상담
                label1 = Label(schoolViolence2, text='교육부,여성가족부,경찰청', font=30)
                label2 = Label(schoolViolence2, text='117', font=30)
                
                label1.pack()
                label2.pack()
                
                schoolViolence2.mainloop()

            #개인 및 집단 상담
            def schoolViolence3():
                schoolViolence.destroy()
                schoolViolence3 = Tk()
                schoolViolence3.title("개인 및 집단 상담")
                schoolViolence3.geometry('300x200')

                #개인 및 집단 상담
                label1 = Label(schoolViolence3, text='푸른나무재단 \n(청소년폭력예방재단)', font=30)
                label2 = Label(schoolViolence3, text='1588-9128', font=30)
                
                label1.pack()
                label2.pack()
                
                schoolViolence3.mainloop()

            #학교폭력
            teenager.destroy()
            schoolViolence = Tk()
            schoolViolence.title("학교폭력")
            schoolViolence.geometry('300x200')

            hbtn1 = Button(schoolViolence, text='예방교육 및 상담', font=30, command=schoolViolence2)
            hbtn2 = Button(schoolViolence, text='개인 및 집단 상담', font=30, command=schoolViolence3)

            hbtn1.pack(side=TOP, fill=X, ipadx=33, ipady=33)
            hbtn2.pack(side=TOP, fill=X, ipadx=33, ipady=33)

            schoolViolence.mainloop()

        #가출, 중독, 고민
        def concern():
            teenager.destroy()
            concern = Tk()
            concern.title("가출, 중독, 고민")
            concern.geometry('300x200')

            #가출, 중독, 고민
            label1 = Label(concern, text = "청소년 사이버상담센터", font=30)
            label2 = Label(concern, text = "1388", font=30)
            
            label1.pack()
            label2.pack()

            concern.mainloop()
            
        #학교, 가정생활, 특수교육
        def school():
            teenager.destroy()
            school = Tk()
            school.title("학교, 가정생활, 특수교육")
            school.geometry('300x200')

            #학교, 가정생활, 특수교육
            label1 = Label(school, text = "서울시청소년상담복지센터", font=30)
            label2 = Label(school, text = "02-2285-1318", font=30)
            
            label1.pack()
            label2.pack()

            school.mainloop()

        #성범죄 피해
        def sexCrimes():
            teenager.destroy()
            school = Tk()
            school.title("성범죄 피해")
            school.geometry('300x200')

            #성범죄 피해
            label1 = Label(school, text = "탁틴내일 \n(아동,청소년성폭력상담소)", font=30)
            label2 = Label(school, text = "02-3141-6191", font=30)

            label1.pack()
            label2.pack()

            school.mainloop()

        #청소년
        counseling.destroy()
        teenager = Tk()
        teenager.title("청소년")
        teenager.geometry('300x200')

        fbtn1 = Button(teenager, text='학교폭력', command=schoolViolence)
        fbtn2 = Button(teenager, text='가출, 중독, 고민', command=concern)
        fbtn3 = Button(teenager, text='학교, 가정생활, 특수교육', command=school)
        fbtn4 = Button(teenager, text='성범죄 피해', command=sexCrimes)

        fbtn1['font'] = myFont
        fbtn2['font'] = myFont
        fbtn3['font'] = myFont
        fbtn4['font'] = myFont

        fbtn1.pack(side=TOP, fill=X, ipadx=8, ipady=8)
        fbtn2.pack(side=TOP, fill=X, ipadx=8, ipady=8)
        fbtn3.pack(side=TOP, fill=X, ipadx=8, ipady=8)
        fbtn4.pack(side=TOP, fill=X, ipadx=8, ipady=8)

        teenager.mainloop()
        #청소년 끝

    #노인
    def old():
        #보호
        def oldProtect():
            #노인 학대 신고 및 상담
            def oldProtect2():
                oldProtect.destroy()
                oldProtect2 = Tk()
                oldProtect2.title("노인 학대 신고 및 상담")
                oldProtect2.geometry('300x200')
                
            #노인 학대 신고 및 상담
                label1 = Label(oldProtect2, text='중앙노인보호전문기관', font=30)
                label2 = Label(oldProtect2, text='1577-1389', font=30)
                
                label1.pack()
                label2.pack()
                
                oldProtect2.mainloop()

            #노인 주거 및 복지시설 안내
            def oldProtect3():
                oldProtect.destroy()
                oldProtect3 = Tk()
                oldProtect3.title("노인 주거 및 복지시설 안내")
                oldProtect3.geometry('300x200')

                #노인 주거 및 복지시설 안내
                label1 = Label(oldProtect3, text='한국노인복지중앙회', font=30)
                label2 = Label(oldProtect3, text='02-712-9763', font=30)
                
                label1.pack()
                label2.pack()
                
                oldProtect3.mainloop()

            #보호
            old.destroy()
            oldProtect = Tk()
            oldProtect.title("보호")
            oldProtect.geometry('300x200')

            hbtn1 = Button(oldProtect, text='노인 학대 신고 및 상담', command=oldProtect2)
            hbtn2 = Button(oldProtect, text='노인 주거 및 복지시설 안내', command=oldProtect3)

            hbtn1['font'] = myFont
            hbtn2['font'] = myFont

            hbtn1.pack(side=TOP, fill=X, ipadx=33, ipady=33)
            hbtn2.pack(side=TOP, fill=X, ipadx=33, ipady=33)

            oldProtect.mainloop()

        #취업, 법률 상담
        def EmploymentCounseling():
            old.destroy()
            EmploymentCounseling = Tk()
            EmploymentCounseling.title("취업, 법률 상담")
            EmploymentCounseling.geometry('300x200')

            #취업, 법률 상담
            label1 = Label(EmploymentCounseling, text = "한국노인의전화", font=30)
            label2 = Label(EmploymentCounseling, text = "062-351-5070", font=30)
            
            label1.pack()
            label2.pack()

            EmploymentCounseling.mainloop()

        #노인
        counseling.destroy()
        old = Tk()
        old.title("노인")
        old.geometry('300x200')

        fbtn1 = Button(old, text='보호', command=oldProtect)
        fbtn2 = Button(old, text='취업, 법률 상담', command=EmploymentCounseling)

        fbtn1['font'] = myFont
        fbtn2['font'] = myFont

        fbtn1.pack(side=TOP, fill=X, ipadx=33, ipady=33)
        fbtn2.pack(side=TOP, fill=X, ipadx=33, ipady=33)

        old.mainloop()
        #노인 끝

    #장애인
    def disabled():
        #학대
        def abuse():
            disabled.destroy()
            abuse = Tk()
            abuse.title("학대")
            abuse.geometry('300x200')

            #학대
            label1 = Label(abuse, text='중앙장애인권익옹호기관원', font=30)
            label2 = Label(abuse, text='1644-8295', font=30)

            label1.pack()
            label2.pack()

            abuse.mainloop()

        #지원
        def support():
            #장애인 재활, 장애가정 청소년 지원
            def d_reh():
                support.destroy()
                d_reh = Tk()
                d_reh.title("장애인 재활, 장애가정 청소년 지원")
                d_reh.geometry('300x200')

                #장애인 재활, 장애가정 청소년 지원
                label1 = Label(d_reh, text='한국장애인재활협회', font=30)
                label2 = Label(d_reh, text='02-3675-4465', font=30)

                label1.pack()
                label2.pack()

                d_reh.mainloop()

            #장애인 무료 정보화교육
            def d_informEducate():
                support.destroy()
                d_informEducate = Tk()
                d_informEducate.title("장애인 무료 정보화 교육")
                d_informEducate.geometry('300x200')

                #장애인 무료 정보화교육
                label1 = Label(d_informEducate, text='배움나라', font=30)
                label2 = Label(d_informEducate, text='1588-0814', font=30)

                label1.pack()
                label2.pack()

                d_informEducate.mainloop()

            #지원
            disabled.destroy()
            support = Tk()
            support.title("지원")
            support.geometry('300x200')
                
            btn1 = Button(support, text='장애인 재활,\n장애가정 청소년 지원', command=d_reh)
            btn2 = Button(support, text='장애인 무료 정보화교육', command=d_informEducate)

            btn1.pack(side=TOP, fill=X, ipadx=33, ipady=33)
            btn2.pack(side=TOP, fill=X, ipadx=33, ipady=33)

            btn1['font'] = myFont
            btn2['font'] = myFont

            support.mainloop()
            
        #여성장애인 복지 및 상담
        def f_disabled():
            disabled.destroy()
            f_disabled = Tk()
            f_disabled.title("여성장애인 복지 및 상담")
            f_disabled.geometry('300x200')

            #여성장애인 복지 및 상담
            label1 = Label(f_disabled, text='한국여성장애인연합', font=30)
            label2 = Label(f_disabled, text='02-3675-4465', font=30)

            label1.pack()
            label2.pack()

            f_disabled.mainloop()

        #장애인
        counseling.destroy()
        disabled = Tk()
        disabled.title("장애인")
        disabled.geometry('300x200')

        btn1 = Button(disabled, text='학대', command=abuse)
        btn2 = Button(disabled, text='지원', command=support)
        btn3 = Button(disabled, text='여성장애인 복지 및 상담', command=f_disabled)

        btn1['font'] = myFont
        btn2['font'] = myFont
        btn3['font'] = myFont

        btn1.pack(side=TOP, fill=X, ipadx=16, ipady=16)
        btn2.pack(side=TOP, fill=X, ipadx=16, ipady=16)
        btn3.pack(side=TOP, fill=X, ipadx=16, ipady=16)

        disabled.mainloop()
        #장애인

    #여성
    def Women():
        #보호
        def Protection():
            #가정폭력, 성폭력, 성매매
            def Protection2():
                Protection.destroy()
                Protection2 = Tk()
                Protection2.title("가정폭력, 성폭력, 성매매")
                Protection2.geometry('300x200')

                #가정폭력, 성폭력, 성매매
                label1 = Label(Protection2, text='한국여성인권진흥원', font=30)
                label2 = Label(Protection2, text='1366', font=30)

                label1.pack()
                label2.pack()

                Protection2.mainloop()
        
            #폭력피해 이주여성
            def Protection3():
                Protection.destroy()
                Protection3 = Tk()
                Protection3.title("폭력피해 이주여성")
                Protection3.geometry('300x200')

                #폭력피해 이주여성
                label1 = Label(Protection3, text='다누리콜센터', font=30)
                label2 = Label(Protection3, text='1577-1366', font=30)
                
                label1.pack()
                label2.pack()

                Protection3.mainloop()
        
            #보호
            Women.destroy()
            Protection = Tk()
            Protection.title("보호")
            Protection.geometry('300x200')

            hbtn1 = Button(Protection, text='가정폭력, 성폭력, 성매매', command=Protection2)
            hbtn2 = Button(Protection, text='폭력피해 이주여성', command=Protection3)

            hbtn1['font'] = myFont
            hbtn2['font'] = myFont

            hbtn1.pack(side=TOP, fill=X, ipadx=33, ipady=33)
            hbtn2.pack(side=TOP, fill=X, ipadx=33, ipady=33)

            Protection.mainloop()

        #부부갈등
        def Conflict():
            Women.destroy()
            Conflict = Tk()
            Conflict.title("부부갈등")
            Conflict.geometry('300x200')

            #부부갈등
            label1 = Label(Conflict, text = "한국여성상담센터", font=30)
            label2 = Label(Conflict, text = "02-953-2017", font=30)

            label1.pack()
            label2.pack()

            Conflict.mainloop()

        #여성인권
        def Rights():
            Women.destroy()
            Rights = Tk()
            Rights.title("여성인권")
            Rights.geometry('300x200')

            #여성인권
            Rights1 = Label(Rights, text = "한국여성의전화", font=30)
            Rights2 = Label(Rights, text = "02-2263-6464", font=30)
            
            Rights1.pack()
            Rights2.pack()
        
            Rights.mainloop()
        
        #성상담,자녀 성교육
        def SexCounseling():
            Women.destroy()
            SexCounseling = Tk()
            SexCounseling.title("성상담, 자녀 성교육")
            SexCounseling.geometry('300x200')

            #성상담, 자녀 성교육
            SexCounseling1 = Label(SexCounseling, text = "푸른아우성", font=30)
            SexCounseling2 = Label(SexCounseling, text = "02-332-9978", font=30)
            
            SexCounseling1.pack()
            SexCounseling2.pack()

            SexCounseling.mainloop()

        #일자리, 사업 지원
        def Employment():
            Women.destroy()
            Employment = Tk()
            Employment.title("일자리, 사업 지원")
            Employment.geometry('300x200')

            #취업 상담 및 교육
            def Employment2():
                Employment.destroy()
                Employment2 = Tk()
                Employment2.title("취업 상담 및 교육")
                Employment2.geometry('300x200')

                #취업 상담 및 교육
                label1 = Label(Employment2, text='여성인력개발센터', font=30)
                label2 = Label(Employment2, text='02-318-5880', font=30)
                
                label1.pack()
                label2.pack()
                
                Employment2.mainloop()

            #일자리 상담
            def Employment3():
                Employment.destroy()
                Employment3 = Tk()
                Employment3.title("일자리 상담")
                Employment3.geometry('300x200')

                #일자리 상담
                label1 = Label(Employment3, text='여성가족부', font=30)
                label2 = Label(Employment3, text='1544-1199', font=30)
                
                label1.pack()
                label2.pack()
                
                Employment3.mainloop()
                
            #일자리, 사업 지원
            hbtn1 = Button(Employment, text='취업 상담 및 교육', command=Employment2)
            hbtn2 = Button(Employment, text='일자리 상담', command=Employment3)

            hbtn1['font'] = myFont
            hbtn2['font'] = myFont

            hbtn1.pack(side=TOP, fill=X, ipadx=33, ipady=33)
            hbtn2.pack(side=TOP, fill=X, ipadx=33, ipady=33)

            Employment.mainloop()
        
        counseling.destroy()      
        Women = Tk()
        Women.title("여성")
        Women.geometry('300x200')

        fbtn1 = Button(Women, text='보호', command=Protection)
        fbtn2 = Button(Women, text='부부갈등', command=Conflict)
        fbtn3 = Button(Women, text='여성인권', command=Rights)
        fbtn4 = Button(Women, text='성상담, 자녀 성교육 ', command=SexCounseling)
        fbtn5 = Button(Women, text='일자리, 사업 지원', command=Employment)

        fbtn1['font'] = myFont
        fbtn2['font'] = myFont
        fbtn3['font'] = myFont
        fbtn4['font'] = myFont
        fbtn5['font'] = myFont

        fbtn1.pack(side=TOP, fill=X, ipadx=3, ipady=3)
        fbtn2.pack(side=TOP, fill=X, ipadx=3, ipady=3)
        fbtn3.pack(side=TOP, fill=X, ipadx=3, ipady=3)
        fbtn4.pack(side=TOP, fill=X, ipadx=3, ipady=3)
        fbtn5.pack(side=TOP, fill=X, ipadx=3, ipady=3)

        Women.mainloop()
        #여성 끝

    #상담
    counseling = Tk()
    counseling.title("상담")
    counseling.geometry('300x200')

    btn1 = Button(counseling, text='아동', command=Child)
    btn2 = Button(counseling, text='청소년', command=teenager)
    btn3 = Button(counseling, text='여성', command=Women)
    btn4 = Button(counseling, text='노인', command=old)
    btn5 = Button(counseling, text='장애인', command=disabled)

    btn1['font'] = myFont
    btn2['font'] = myFont
    btn3['font'] = myFont
    btn4['font'] = myFont
    btn5['font'] = myFont

    btn1.pack(side=TOP, fill=X, ipadx=3, ipady=3)
    btn2.pack(side=TOP, fill=X, ipadx=3, ipady=3)
    btn3.pack(side=TOP, fill=X, ipadx=3, ipady=3)
    btn4.pack(side=TOP, fill=X, ipadx=3, ipady=3)
    btn5.pack(side=TOP, fill=X, ipadx=3, ipady=3)


    counseling.mainloop()
#상담 끝 ---------------------------------------------------------------------


#가정/생활-------------------------------------------------------------------------
def home_life():
    #건강
    def health():
        #금연
        def noSmoking():
            health.destroy()
            noSmoking = Tk()
            noSmoking.title("금연")
            noSmoking.geometry('300x200')
            
            nlabel1 = Label(noSmoking, text='금연길라잡이', font=30)
            nlabel2 = Label(noSmoking, text='1544-9030', font=30)

            nlabel1.pack()
            nlabel2.pack()

            noSmoking.mainloop()

        #암
        def cancer():
            health.destroy()
            cancer = Tk()
            cancer.title("암")
            cancer.geometry('300x200')

            clabel1 = Label(cancer, text='국가암정보센터', font=30)
            clabel2 = Label(cancer, text='1577-8899', font=30)

            clabel1.pack()
            clabel2.pack()

            cancer.mainloop()

        #에이즈
        def aids():
            health.destroy()
            aids = Tk()
            aids.title("에이즈")
            aids.geometry('300x200')

            alabel1 = Label(aids, text='대한에이즈예방협회', font=30)
            alabel2 = Label(aids, text='1599-8105', font=30)

            alabel1.pack()
            alabel2.pack()

            aids.mainloop()

        #건강
        familyLife.destroy()
        health = Tk()
        health.title("건강")
        health.geometry('300x200')

        myFont = font.Font(size=30)

        hbtn1 = Button(health, text='금연', command=noSmoking)
        hbtn2 = Button(health, text='암', command=cancer)
        hbtn3 = Button(health, text='에이즈', command=aids)

        hbtn1['font'] = myFont
        hbtn2['font'] = myFont
        hbtn3['font'] = myFont

        hbtn1.pack(ipadx=120, ipady=15)
        hbtn2.pack(ipadx=130, ipady=15)
        hbtn3.pack(ipadx=110, ipady=15)

        health.mainloop()
    #건강 끝

    #가족
    def family():
        #자녀
        def children():
            #아이돌봄
            def takeChild():
                children.destroy()
                takeChild = Tk()
                takeChild.title("아이돌봄, 돌보미 지원")
                takeChild.geometry('300x200')
                
                tlabel1 = Label(takeChild, text='아이돌봄서비스', font=30)
                tlabel2 = Label(takeChild, text='1577-2514', font=30)

                tlabel1.pack()
                tlabel2.pack()

                takeChild.mainloop()
                
            #자녀 양육비 청구 및 소송 지원
            def claim():
                children.destroy()
                claim = Tk()
                claim.title("자녀 양육비 청구 및 소송 지원")
                claim.geometry('300x200')

                label1 = Label(claim, text='양육비이행관리원', font=30)
                label2 = Label(claim, text='1644-6621', font=30)

                label1.pack()
                label2.pack()

                claim.mainloop()

            #자녀
            family.destroy()
            children = Tk()
            children.title("자녀")
            children.geometry('300x200')

            myFont = font.Font(size=16)
            
            cbtn1 = Button(children, text='아이돌봄, 돌보미 지원', command=takeChild)
            cbtn2 = Button(children, text='자녀 양육비 청구 및 소송 지원', command=claim)

            cbtn1['font'] = myFont
            cbtn2['font'] = myFont

            cbtn1.pack(ipadx=40, ipady=33)
            cbtn2.pack(ipadx=5, ipady=33)

            children.mainloop()

        #한부모 가족
        def singleParent():
            family.destroy()
            singleParent = Tk()
            singleParent.title("한부모 가족")
            singleParent.geometry('300x200')

            slabel1 = Label(singleParent, text='한부모상담전화', font=30)
            slabel2 = Label(singleParent, text='1644-6621', font=30)

            slabel1.pack()
            slabel2.pack()

            singleParent.mainloop()

        #취약/위기 가족
        def vunerableFam():
            family.destroy()
            vunerableFam = Tk()
            vunerableFam.title("취약/위기 가족")
            vunerableFam.geometry('300x200')

            vlabel1 = Label(vunerableFam, text='건강가정지원센터', font=30)
            vlabel2 = Label(vunerableFam, text='1577-9337', font=30)

            vlabel1.pack()
            vlabel2.pack()

            vunerableFam.mainloop()

        #가족
        familyLife.destroy()
        family = Tk()
        family.title("가족")
        family.geometry('300x200')

        myFont = font.Font(size=30)

        fbtn1 = Button(family, text='자녀', command=children)
        fbtn2 = Button(family, text='한부모 가족', command=singleParent)
        fbtn3 = Button(family, text='취약/위기 가족', command=vunerableFam)

        fbtn1['font'] = myFont
        fbtn2['font'] = myFont
        fbtn3['font'] = myFont

        fbtn1.pack(ipadx=120, ipady=15)
        fbtn2.pack(ipadx=87, ipady=15)
        fbtn3.pack(ipadx=73, ipady=15)

        family.mainloop()
    #가족 끝

    #생활
    def life():
        #정부 민원 안내
        def govern():
            life.destroy()
            govern = Tk()
            govern.title("정부 민원 안내")
            govern.geometry('300x200')

            glabel1 = Label(govern, text='국민권익위원회', font=30)
            glabel2 = Label(govern, text='110', font=30)
            
            glabel1.pack()
            glabel2.pack()
            
            govern.mainloop()

        #수도
        def waterSupply():
            #서울
            def SU():
                waterSupply.destroy()
                SU = Tk()
                SU.title("서울")
                SU.geometry('300x200')
            
                label1 = Label(SU, text='서울 상수도사업본부', font=30)
                label2 = Label(SU, text='02-121', font=30)

                label1.pack()
                label2.pack()

                SU.mainloop()

            #대전
            def DJ():
                waterSupply.destroy()
                DJ = Tk()
                DJ.title("대전")
                DJ.geometry('300x200')
            
                label1 = Label(DJ, text='대전 상수도사업본부', font=30)
                label2 = Label(DJ, text='042-121', font=30)

                label1.pack()
                label2.pack()

                DJ.mainloop()

            #부산
            def BS():
                waterSupply.destroy()
                BS = Tk()
                BS.title("부산")
                BS.geometry('300x200')
            
                label1 = Label(BS, text='부산 상수도사업본부', font=30)
                label2 = Label(BS, text='051-120', font=30)

                label1.pack()
                label2.pack()

                BS.mainloop()

            #울산
            def US():
                waterSupply.destroy()
                US = Tk()
                US.title("울산")
                US.geometry('300x200')
            
                label1 = Label(US, text='울산 상수도사업본부', font=30)
                label2 = Label(US, text='052-120', font=30)

                label1.pack()
                label2.pack()

                US.mainloop()

            #광주
            def GJ():
                waterSupply.destroy()
                GJ = Tk()
                GJ.title("광주")
                GJ.geometry('300x200')
            
                label1 = Label(GJ, text='광주 상수도사업본부', font=30)
                label2 = Label(GJ, text='062-121', font=30)

                label1.pack()
                label2.pack()

                GJ.mainloop()

            #대구
            def DG():
                waterSupply.destroy()
                DG = Tk()
                DG.title("대구")
                DG.geometry('300x200')
            
                label1 = Label(DG, text='대구 상수도사업본부', font=30)
                label2 = Label(DG, text='053-121', font=30)

                label1.pack()
                label2.pack()

                DG.mainloop()

            #인천
            def IC():
                waterSupply.destroy()
                IC = Tk()
                IC.title("인천")
                IC.geometry('300x200')
                
                label1 = Label(IC, text='인천 상수도사업본부', font=30)
                label2 = Label(IC, text='032-120', font=30)

                label1.pack()
                label2.pack()

                IC.mainloop()

            #수도
            life.destroy()
            waterSupply = Tk()
            waterSupply.title("수도")
            waterSupply.geometry('300x250')

            myFont = font.Font(size=10)
            
            wbtn1 = Button(waterSupply, text='서울', command=SU)
            wbtn2 = Button(waterSupply, text='대전', command=DJ)
            wbtn3 = Button(waterSupply, text='부산', command=BS)
            wbtn4 = Button(waterSupply, text='울산', command=US)
            wbtn5 = Button(waterSupply, text='광주', command=GJ)
            wbtn6 = Button(waterSupply, text='대구', command=DG)
            wbtn7 = Button(waterSupply, text='인천', command=IC)

            wbtn1['font'] = myFont
            wbtn2['font'] = myFont
            wbtn3['font'] = myFont
            wbtn4['font'] = myFont
            wbtn5['font'] = myFont
            wbtn6['font'] = myFont
            wbtn7['font'] = myFont


            wbtn1.pack(ipadx=130)
            wbtn2.pack(ipadx=130)
            wbtn3.pack(ipadx=130)
            wbtn4.pack(ipadx=130)
            wbtn5.pack(ipadx=130)
            wbtn6.pack(ipadx=130)
            wbtn7.pack(ipadx=130)

            waterSupply.mainloop()

        #전기
        def elec():
            #고장
            def breakDown():
                elec.destroy()
                breakDown = Tk()
                breakDown.title("고장")
                breakDown.geometry('300x200')

                blabel1 = Label(breakDown, text='한국전력공사', font=30)
                blabel2 = Label(breakDown, text='123', font=30)

                blabel1.pack()
                blabel2.pack()

                breakDown.mainloop()

            #점검 신청
            def check():
                elec.destroy()
                check = Tk()
                check.title("점검 신청")
                check.geometry('300x200')

                clabel1 = Label(check, text='한국전기안전공사', font=30)
                clabel2 = Label(check, text='1588-7500', font=30)

                clabel1.pack()
                clabel2.pack()

                check.mainloop()

            #전기
            life.destroy()
            elec = Tk()
            elec.title("전기")
            elec.geometry('300x200')

            myFont = font.Font(size=43)

            ebtn1 = Button(elec, text='고장', command=breakDown)
            ebtn2 = Button(elec, text='점검 신청', command=check)

            ebtn1['font'] = myFont
            ebtn2['font'] = myFont

            ebtn1.pack(ipadx=120, ipady=33)
            ebtn2.pack(ipadx=96, ipady=33)
        
            elec.mainloop()

        #가스
        def gas():
            life.destroy()
            gas = Tk()
            gas.title("가스")
            gas.geometry('300x200')

            glabel1 = Label(gas, text='한국가스안전공사', font=30)
            glabel2 = Label(gas, text='1544-4500', font=30)

            glabel1.pack()
            glabel2.pack()
        
            gas.mainloop()

        #생활
        familyLife.destroy()
        life = Tk()
        life.title("생활")
        life.geometry('300x200')

        myFont = font.Font(size=20)

        lbtn1 = Button(life, text='정부 민원 안내', command=govern)
        lbtn2 = Button(life, text='수도', command=waterSupply)
        lbtn3 = Button(life, text='전기', command=elec)
        lbtn4 = Button(life, text='가스', command=gas)

        lbtn1['font'] = myFont
        lbtn2['font'] = myFont
        lbtn3['font'] = myFont
        lbtn4['font'] = myFont

        lbtn1.pack(ipadx=73, ipady=8)
        lbtn2.pack(ipadx=120, ipady=8)
        lbtn3.pack(ipadx=120, ipady=8)
        lbtn4.pack(ipadx=120, ipady=8)

        life.mainloop()
        #생활  끝

    #가정/생활
    familyLife = Tk()
    familyLife.title("가정/생활")
    familyLife.geometry('300x200')

    myFont = font.Font(size=30)

    fbtn1 = Button(familyLife, text='건강', command=health)
    fbtn2 = Button(familyLife, text='가족', command=family)
    fbtn3 = Button(familyLife, text='생활', command=life)

    fbtn1['font'] = myFont
    fbtn2['font'] = myFont
    fbtn3['font'] = myFont

    fbtn1.pack(ipadx=120, ipady=15)
    fbtn2.pack(ipadx=120, ipady=15)
    fbtn3.pack(ipadx=120, ipady=15)

    familyLife.mainloop()
#가정/생활 끝-----------------------------------------------------------------

#긴급-------------------------------------------------------------------------
def emergency():
    def crime():
        #범죄
        def crime2():
            crime.destroy()
            crime2 = Tk()
            crime2.title("철도범죄")
            crime2.geometry("300x200")

            #철도범죄
            label1 = Label(crime2, text = "철도 특별 사법 경찰대", font = 30)
            label2 = Label(crime2, text = "1588-7722", font = 30)
            
            label1.pack()
            label2.pack()
            
            crime2.mainloop()

        #범죄
        emergency.destroy()
        crime = Tk()
        crime.title("범죄")
        crime.geometry("300x200")
        myFont = font.Font(size=10)

        btn1 = Button(crime, text = "철도범죄", command = crime2)
        label1 = Label(crime, text = "경찰청 112", font = 30)

        btn1['font'] = myFont
        
        btn1.pack(side=TOP, fill=X, ipadx=33, ipady=33)
        label1.pack()

        crime.mainloop()

    #화재, 구조/구급, 응급의료
    def rescue():
        emergency.destroy()
        rescue = Tk()
        rescue.title("화재, 구조/구급, 응급의료")
        rescue.geometry("300x200")

        #화재,구조/구급, 응급의료
        label1 = Label(rescue, text = "119안전신고센터", font = 30)
        label2 = Label(rescue, text = "119", font = 30)
        
        label1.pack()
        label2.pack()
        
        rescue.mainloop()

    #해양긴급신고 
    def sea_rescue():
        emergency.destroy()
        sea_rescue = Tk()
        sea_rescue.title("해양긴급신고")
        sea_rescue.geometry("300x200")

        #해양긴급신고
        label1 = Label(sea_rescue, text = "해양경찰청", font = 30)
        label2 = Label(sea_rescue, text = "119", font = 30)
        
        label1.pack()
        label2.pack()
        
        sea_rescue.mainloop()

    #긴급
    emergency = Tk()
    emergency.title("긴급")
    emergency.geometry("300x200")
    myFont = font.Font(size=30)

    ebtn1 = Button(emergency, text = "범죄", command=crime)
    ebtn2 = Button(emergency, text = "화재, 구조/구급, 응급의료", command=rescue)
    ebtn3 = Button(emergency, text = "해양긴급신고", command=sea_rescue)

    ebtn1['font'] = myFont
    ebtn2['font'] = myFont
    ebtn3['font'] = myFont

    ebtn1.pack(side=TOP, fill=X, ipadx=16, ipady=16)
    ebtn2.pack(side=TOP, fill=X, ipadx=16, ipady=16)
    ebtn3.pack(side=TOP, fill=X, ipadx=16, ipady=16)

    emergency.mainloop()
#긴급 끝----------------------------------------------------------------------

#재난/안전
def disaster_safety():
    #국가관련
    def country():
        #간첩
        def country2():
            country.destroy()
            country2 = Tk()
            country2.title("간첩")
            country2.geometry("300x200")
            
            #간첩
            label1 = Label(country2, text = '국가정보원', font = 30)
            label2 = Label(country2, text = '111', font = 30)
            
            label1.pack()
            label2.pack()

            country2.mainloop()

        #국방헬프콜, 군범죄
        def country3():
            country.destroy()
            country3 = Tk()
            country3.title("국방헬프콜, 군범죄")
            country3.geometry("300x200")

            #국방헬프콜, 군범죄
            label1 = Label(country3, text = '국방부', font = 30)
            label2 = Label(country3, text = '1303', font = 30)
            
            label1.pack()
            label2.pack()

            country3.mainloop()

        #군사 기밀, 간첩
        def country4():
            country.destroy()
            country4 = Tk()
            country4.title("군사 기밀, 간첩")
            country4.geometry("300x200")

            #군사 기밀, 간첩
            label1 = Label(country4, text = '국사안보지원사령부', font = 30)
            label2 = Label(country4, text = '1337', font = 30)
            
            label1.pack()
            label2.pack()

            country4.mainloop()

        #국가관련
        disaster.destroy()
        country = Tk()
        country.title("국가관련")
        country.geometry("300x200")
        myFont = font.Font(size=30)

        btn1 = Button(country, text = "간첩", command = country2)
        btn2 = Button(country, text = "국방헬프콜, 군범죄", command = country3)
        btn3 = Button(country, text = "군사기밀", command = country4)

        btn1['font'] = myFont
        btn2['font'] = myFont
        btn3['font'] = myFont
        
        btn1.pack(side=TOP, fill=X, ipadx=16, ipady=16)
        btn2.pack(side=TOP, fill=X, ipadx=16, ipady=16)
        btn3.pack(side=TOP, fill=X, ipadx=16, ipady=16)
        
        country.mainloop()

    #불법행위
    def illegal():
        #마약
        def drug():
            #마약범죄
            def illegal2():
                drug.destroy()
                illegal2 = Tk()
                illegal2.title("마약범죄")
                illegal2.geometry("300x200")

                label1 = Label(illegal2, text = '검찰청', font = 30)
                label2 = Label(illegal2, text = '1301', font = 30)
                
                label1.pack()
                label2.pack()
                
                illegal2.mainloop()

            #상담, 치료 및 재활
            def illegal3():
                drug.destroy()
                illegal3 = Tk()
                illegal3.title("상담, 치료 및 재활")
                illegal3.geometry("300x200")

                label1 = Label(illegal3, text = '한국 마약 퇴치 운동본부', font = 30)
                label2 = Label(illegal3, text = '1899-0893', font = 30)
                
                label1.pack()
                label2.pack()
                
                illegal3.mainloop()

            #마약
            illegal.destroy()
            drug = Tk()
            drug.title("마약")
            drug.geometry('300x200')
            myFont = font.Font(size=30)

            btn1 = Button(drug, text = "마약범죄", command = illegal2)
            btn2 = Button(drug, text = "상담, 치료 및 재활", command = illegal3)

            btn1['font'] = myFont
            btn2['font'] = myFont

            btn1.pack(side=TOP, fill=X, ipadx=33, ipady=33)
            btn2.pack(side=TOP, fill=X, ipadx=33, ipady=33)

            drug.mainloop()

        #밀수
        def illegal4():
            illegal.destroy()
            illegal4 = Tk()
            illegal4.title("밀수")
            illegal4.geometry("300x200")

            label1 = Label(illegal4, text = '관세청', font = 30)
            label2 = Label(illegal4, text = '125', font = 30)
            
            label1.pack()
            label2.pack()
            
            illegal4.mainloop()

        #도박
        def gambling():
            #도박범죄
            def illegal5():
                gambling.destroy()
                illegal5 = Tk()
                illegal5.title("도박범죄")
                illegal5.geometry("300x200")
        
                label1 = Label(illegal5, text = '불법사행산업감시신고센터', font = 30)
                label2 = Label(illegal5, text = '1855-0112', font = 30)

                label1.pack()
                label2.pack()
                
                illegal5.mainloop()

            #예방, 치유 및 재활
            def illegal6():
                gambling.destroy()
                illegal6 = Tk()
                illegal6.title("예방, 치유 및 재활")
                illegal6.geometry("300x200")

                label1 = Label(illegal6, text = '한국 도박 문제 관리센터', font = 30)
                label2 = Label(illegal6, text = '1336', font = 30)
                
                label1.pack()
                label2.pack()
                
                illegal6.mainloop()
                
            #도박
            illegal.destroy()
            gambling = Tk()
            gambling.title("도박")
            gambling.geometry("300x200")
            myFont = font.Font(size=30)

            btn1 = Button(gambling, text = "도박범죄", command = illegal5)
            btn2 = Button(gambling, text = "예방, 치유 및 재활", command = illegal6)

            btn1['font'] = myFont
            btn2['font'] = myFont

            btn1.pack(side=TOP, fill=X, ipadx=33, ipady=33)
            btn2.pack(side=TOP, fill=X, ipadx=33, ipady=33)

            gambling.mainloop()
            
        #불법행위 
        disaster.destroy()
        illegal = Tk()
        illegal.title("불법행위")
        illegal.geometry('300x200')
        myFont = font.Font(size=30)

        btn1 = Button(illegal, text = "마약", command = drug)
        btn2 = Button(illegal, text = "밀수", command = illegal4)
        btn3 = Button(illegal, text = "도박", command = gambling)

        btn1['font'] = myFont
        btn2['font'] = myFont
        btn3['font'] = myFont
        
        btn1.pack(side=TOP, fill=X, ipadx=16, ipady=16)
        btn2.pack(side=TOP, fill=X, ipadx=16, ipady=16)
        btn3.pack(side=TOP, fill=X, ipadx=16, ipady=16)
        
        illegal.mainloop()
        
    #건강
    def fitness():
        #감염병, 질병
        def fitness2():
            fitness.destroy()
            fitness2 = Tk()
            fitness2.title("감염병, 질병")
            fitness2.geometry("300x200")

            label1 = Label(fitness2, text = "질병관리청", font = 30)
            label2 = Label(fitness2, text = "1339", font = 30)
            
            label1.pack()
            label2.pack()
            
            fitness2.mainloop()

        #부정, 불량식품
        def fitness3():
            fitness.destroy()
            fitness3 = Tk()
            fitness3.title("부정, 불량식품")
            fitness3.geometry("300x200")

            label1 = Label(fitness3, text = "식품 의약품 안전처", font = 30)
            label2 = Label(fitness3, text = "1399", font = 30)
            
            label1.pack()
            label2.pack()
            
            fitness3.mainloop()
            
        #건강
        disaster.destroy()
        fitness = Tk()
        fitness.title("건강")
        fitness.geometry("300x200")
        myFont = font.Font(size=30)

        btn1 = Button(fitness, text = "감염병, 질병", command = fitness2)
        btn2 = Button(fitness, text = "부정, 불량식품", command = fitness3)

        btn1['font'] = myFont
        btn2['font'] = myFont
        
        btn1.pack(side=TOP, fill=X, ipadx=33, ipady=33)
        btn2.pack(side=TOP, fill=X, ipadx=33, ipady=33)
        
        fitness.mainloop()
        
    #사이버
    def cyber():
        #개인정보 침해, 사이버 테러
        def cyber2():
            cyber.destroy()
            cyber2 = Tk()
            cyber2.title("개인정보 침해, 사이버 테러")
            cyber2.geometry("300x200")

            #개인정보 침해, 사이버 테러
            label1 = Label(cyber2, text = "한국 인터넷 진흥원", font = 30)
            label2 = Label(cyber2, text = "118", font = 30)
            
            label1.pack()
            label2.pack()
            
            cyber2.mainloop()

        #중독
        def cyber3():
            cyber.destroy()
            cyber3 = Tk()
            cyber3.title("중독")
            cyber3.geometry("300x200")

            #중독
            label1 = Label(cyber3, text = "스마트쉼 센터", font = 30)
            label2 = Label(cyber3, text = "1599-0075", font = 30)
            
            label1.pack()
            label2.pack()
            
            cyber3.mainloop()
            
        #사이버
        disaster.destroy()
        cyber = Tk()
        cyber.title("사이버")
        cyber.geometry("300x200")
        myFont = font.Font(size=30)

        btn1 = Button(cyber, text = "개인정보 침해, 사이버테러", command = cyber2)
        btn2 = Button(cyber, text = "중독", command = cyber3)

        btn1['font'] = myFont
        btn2['font'] = myFont

        btn1.pack(side=TOP, fill=X, ipadx=33, ipady=33)
        btn2.pack(side=TOP, fill=X, ipadx=33, ipady=33)
        
        cyber.mainloop()

    #환경오염
    def pollution():
        disaster.destroy()
        pollution = Tk()
        pollution.title("환경오염")
        pollution.geometry("300x200")

        #환경오염
        label1 = Label(pollution, text = "환경부", font = 30)
        label2 = Label(pollution, text = "128", font = 30)
        
        label1.pack()
        label2.pack()
        
        pollution.mainloop()

    #재난/안전
    disaster = Tk()
    disaster.title("재난/안전")
    disaster.geometry("300x200")
    myFont = font.Font(size=30)

    dbtn1 = Button(disaster, text = "국가관련", command=country)
    dbtn2 = Button(disaster, text = "불법행위", command=illegal)
    dbtn3 = Button(disaster, text = "건강", command=fitness)
    dbtn4 = Button(disaster, text = "사이버", command=cyber)
    dbtn5 = Button(disaster, text = "환경오염", command=pollution)

    dbtn1['font'] = myFont
    dbtn2['font'] = myFont
    dbtn3['font'] = myFont
    dbtn4['font'] = myFont
    dbtn5['font'] = myFont

    dbtn1.pack(side=TOP, fill=X, ipadx=3, ipady=3)
    dbtn2.pack(side=TOP, fill=X, ipadx=3, ipady=3)
    dbtn3.pack(side=TOP, fill=X, ipadx=3, ipady=3)
    dbtn4.pack(side=TOP, fill=X, ipadx=3, ipady=3)
    dbtn5.pack(side=TOP, fill=X, ipadx=3, ipady=3)

    disaster.mainloop()
#재난/안전 끝-----------------------------------------------------------------

public = Tk()
public.title('공공기관 전화번호')
public.geometry('300x200')

myFont = font.Font(size = 20)

pbtn1 = Button(public, text='상담', width = 9, height = 3, compound = 'c', command=counseling)
pbtn2 = Button(public, text='가정/생활', width = 9, height = 3, compound = 'c', command=home_life)
pbtn3 = Button(public, text='긴급',  width = 9, height = 3, compound = 'c',command=emergency)
pbtn4 = Button(public, text='안전/재난',  width = 9, height = 3, compound = 'c',command=disaster_safety)

pbtn1['font'] = myFont
pbtn2['font'] = myFont
pbtn3['font'] = myFont
pbtn4['font'] = myFont

pbtn1.place(x = 0, y = 0)
pbtn2.place(x = 150, y = 0)
pbtn3.place(x = 0, y = 100)
pbtn4.place(x = 150, y = 100)

public.mainloop()

