def main():

    total_males = int(input('How many males are registered?\n'))
    total_females = int(input('How many females are registered?\n'))

    total_students = total_males + total_females

    m_perc = total_males / total_students
    f_perc = total_females / total_students
    
    return m_perc, f_perc


if __name__ == '__main__':
    main()
