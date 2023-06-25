def main():

    total_males = int(input('How many males are registered?\n'))
    total_females = int(input('How many females are registered?\n'))

    total_students = total_males + total_females

    m_perc = (total_males / total_students) * 100
    f_perc = (total_females / total_students) * 100

    print(f'The total number of students: \t {total_students}')
    print(f'The number of males and females: \t {total_males} \t {total_females}')
    print(f'The percentage of males and females: \t {m_perc:.2f}% \t {f_perc:.2f}%')

    return m_perc, f_perc


if __name__ == '__main__':
    main()
