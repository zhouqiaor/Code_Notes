clc
clear
tic
frienddata = csvread('Example_0420.csv');
[clan_a_all,clan_b_all] = size(frienddata);
dirfrienddata = zeros(clan_a_all+clan_b_all,10);
%% ����˼·��һ��
for clan_a = 1:1:clan_a_all
    i = 1;
    for clan_b = 1:1:clan_b_all
        if frienddata(clan_a,clan_b) == 1
            dirfrienddata(clan_a,i) = clan_a_all + clan_b;  
            %δ���ֲ��䣬��b������Ա���ͳһ����a������棬����a��������
            i = i + 1;
        end
    end
end
for clan_b = 1:1:clan_b_all
    i = 1;
    for clan_a = 1:1:clan_a_all
        if frienddata(clan_a,clan_b) == 1
            dirfrienddata(clan_a_all+clan_b,i) = clan_a;
            i = i + 1;
        end
    end
end
%% ����˼·�ڶ���
i = 1;
p = zeros(20000,9);
for r = 1:1:(clan_a+clan_b)
    for c = 1:1:10   %�״��߸�ֵ
        p(i,1) = r; % pǰ��λΪ�״��ߵ����� �Լ����
        p(i,2) = c;
        p(i,3) = r;
        if c ~= 1 && p(i,4) == 0
            for c_i = 1:1:3
                p(i,c_i) =  p(i-1,c_i);
            end
        end 
        if dirfrienddata(r,c) == 0
            p(i,4) = 0;
            break;
        end        
        if c == 1
        p(i,4) = dirfrienddata(r,c);
        end  
        p(i,4) = dirfrienddata(r,c);
    for c1 = 1:1:10  %�����߸�ֵ
        if c1 ~= 1 && p(i,5) == 0
            for c1_i = 1:1:4
                p(i,c1_i) =  p(i-1,c1_i);
            end
        end
        if dirfrienddata(p(i,4),c1) == 0 
            p(i,5) = 0;
            break;
        end     
        if c1 == 1 
          p(i,5) = dirfrienddata(p(i,4),c1);
        end  
        p(i,5) = dirfrienddata(p(i,4),c1);
 %% �Ż�˼·һ
        if   (length(p(i,3:4)) - length(unique(p(i,3:4))))
            p(i,5) = 0;
            break
        end      
     for c2 = 1:1:10  %�����߸�ֵ
        if c2 ~= 1 && p(i,6) == 0
            for c2_i = 1:1:5
                p(i,c2_i) =  p(i-1,c2_i);
            end
        end         
        if dirfrienddata(p(i,5),c2) == 0 
            p(i,6) = 0;
            break;
        end
        if c2 == 1 
          p(i,6) = dirfrienddata(p(i,5),c2);   
        end
        p(i,6) = dirfrienddata(p(i,5),c2);        
        if   (length(p(i,3:5)) - length(unique(p(i,3:5))))
            p(i,6) = 0;
            break
        end 
      for c3 = 1:1:10  %�Ĵ��߸�ֵ
        if c3 ~= 1 && (p(i,7) == 0)
            for c3_i = 1:1:6
                p(i,c3_i) =  p(i-1,c3_i);
            end
        end  
        if dirfrienddata(p(i,6),c3) == 0 
            p(i,7) = 0;
            break;
        end   
        if c3 == 1 
          p(i,7) = dirfrienddata(p(i,6),c3);   
        end       
        p(i,7) = dirfrienddata(p(i,6),c3);

        if   (length(p(i,3:6)) - length(unique(p(i,3:6))))
            p(i,7) = 0;
            break
        end
      for c4 = 1:1:10  %�崫�߸�ֵ
        if c4 ~= 1 && (p(i,8) == 0)
            for c4_i = 1:1:7
                p(i,c4_i) =  p(i-1,c4_i);
            end
        end
        if dirfrienddata(p(i,7),c4) == 0 
            p(i,8) = 0;
            break;
        end
        if c4 == 1 
          p(i,8) = dirfrienddata(p(i,7),c4);   
        end       
        p(i,8) = dirfrienddata(p(i,7),c4);

        if   (length(p(i,3:7)) - length(unique(p(i,3:7))))
            p(i,8) = 0;
            break
        end 
      for c5 = 1:1:10  %�����߸�ֵ
        if c5 ~= 1 && (p(i,9) == 0)
            for c5_i = 1:1:8
                p(i,c5_i) =  p(i-1,c5_i);
            end
        end
        if dirfrienddata(p(i,8),c5) == 0 
            p(i,9) = 0;
            break;
        end  
        if c5 == 1 
          p(i,9) = dirfrienddata(p(i,8),c5);   
        end       
        p(i,9) = dirfrienddata(p(i,8),c5);
%% ����˼·������
        if   p(i,9) == p(i,3) && ((length(p(i,4:9)) - length(unique(p(i,4:9)))) == 0)      
            i = i+1;
        end    
      end %������
      end %�崫��
      end %�Ĵ���
     end %������
    end %������
    end %�״���               
end
%% �Ż�˼·��
result = (i-1)/12
toc