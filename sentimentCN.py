def judgeodd(num):
    if (num/2)*2 == num:
        return 'even'
    else:
        return 'odd'

5. ��з�ֵ����������
def sentiment_score_list(dataset):
    cuted_data = []
    for cell in dataset:
        cuted_data.append(tp.cut_sentence(cell))

    count1 = []
    count2 = []
    for sents in cuted_data: #ѭ������ÿһ������
        for sent in sents:  #ѭ�����������е�ÿһ���־�
            segtmp = tp.segmentation(sent, 'list')  #�Ѿ��ӽ��зִʣ����б����ʽ����
            i = 0 #��¼ɨ�赽�Ĵʵ�λ��
            a = 0 #��¼��дʵ�λ��
            poscount = 0 #�����ʵĵ�һ�η�ֵ
            poscount2 = 0 #�����ʷ�ת��ķ�ֵ
            poscount3 = 0 #�����ʵ�����ֵ������̾�ŵķ�ֵ��
            negcount = 0
            negcount2 = 0
            negcount3 = 0
            for word in segtmp:
                if word in posdict: #�жϴ����Ƿ�����д�
                    poscount += 1                
                    c = 0 # ��¼�񶨴�����
                    for w in segtmp[a:i]:  #ɨ����д�ǰ�ĳ̶ȴ�
                        if w in mostdict:
                            poscount *= 4.0
                        elif w in verydict:
                            poscount *= 3.0
                        elif w in moredict:
                            poscount *= 2.0
                        elif w in ishdict:
                            poscount /= 2.0
                        elif w in insufficientdict:
                            poscount /= 4.0
                        elif w in inversedict:
                            c += 1
                    if judgeodd(c) == 'odd': #ɨ����д�ǰ�ķ񶨴���
                        poscount *= -1.0
                        poscount2 += poscount
                        poscount = 0
                        poscount3 = poscount + poscount2 + poscount3
                        poscount2 = 0
                    else:
                        poscount3 = poscount + poscount2 + poscount3
                        poscount = 0
                    a = i + 1 #��дʵ�λ�ñ仯
                elif word in negdict: #������еķ�����������һ��
                    negcount += 1
                    d = 0
                    for w in segtmp[a:i]:
                        if w in mostdict:
                            negcount *= 4.0
                        elif w in verydict:
                            negcount *= 3.0
                        elif w in moredict:
                            negcount *= 2.0
                        elif w in ishdict:
                            negcount /= 2.0
                        elif w in insufficientdict:
                            negcount /= 4.0
                        elif w in inversedict:
                            d += 1
                    if judgeodd(d) == 'odd':
                        negcount *= -1.0
                        negcount2 += negcount
                        negcount = 0
                        negcount3 = negcount + negcount2 + negcount3
                        negcount2 = 0
                    else:
                        negcount3 = negcount + negcount2 + negcount3
                        negcount = 0
                    a = i + 1
                elif word == '��'.decode('utf8') or word == '!'.decode('utf8'): ##�жϾ����Ƿ��и�̾��
                    for w2 in segtmp[::-1]: #ɨ���̾��ǰ����дʣ����ֺ�Ȩֵ+2��Ȼ���˳�ѭ��
                        if w2 in posdict or negdict:
                            poscount3 += 2
                            negcount3 += 2
                            break                    
                i += 1 #ɨ���λ��ǰ��


			#�����Ƿ�ֹ���ָ��������
            pos_count = 0
            neg_count = 0
            if poscount3 < 0 and negcount3 > 0:
                neg_count += negcount3 - poscount3
                pos_count = 0
            elif negcount3 < 0 and poscount3 > 0:
                pos_count = poscount3 - negcount3
                neg_count = 0
            elif poscount3 < 0 and negcount3 < 0:
                neg_count = -poscount3
                pos_count = -negcount3
            else:
                pos_count = poscount3
                neg_count = negcount3
                
            count1.append([pos_count, neg_count])
        count2.append(count1)
        count1 = []    

    return count2