import poa


def main():
    fasta = (
        ('0-145', 'TCCCGGTCATCATAACCCCGATCGTACCCTCTGTCATAATAGTCTCGGCGGCGAGAACTGCCACTGTAAATCTGATCCCTGTCTTGAGCTGCTCTCCATCCACCTCCCTCCACCACCTCCTCCTCTGTATGATCTGCTGTAATAG'),
        ('145-289', 'TCCCGGTCATCATAACCCCGATCATTGCCACCTGTCATAGTCTCGGCGGCGAGAACTGCCACTGTAAATCCCCTGATCCCTGTCTTGAGCTGCTCTCCATCCCCTCCTCCACCACCTCCTCCTCTGTATGATCTGCTGTAATAG'),
        ('289-433', 'TCCCGGTCATCATAACCCCGATCGTACCCTCTGTCATAATGGTCTCGGCGGCGAGAACTGCCACTGTAAATCTGATCCCTGTCTTGAGCTGCTCTCCATCCACCTCCTCCACCACCTCCTCCTCTGTATGATCTGCTGTAATAG'),
        ('433-579', 'TCCCGGTCATCATAACCCCGATCGTACCCTCTGTCATAATAGTCTCGGCGGCGAGAGGCGCCACTGTAAATCTGATCCCTGTCTTGAGCTGCTCTCCATCCACCTCCTCCACCACCTCCTCCCCTCTGTATGATCTGCTGTAATAG'),
        ('579-721', 'TCCCGGTCATCATAACCCCGATCGTACCCTCTGTCATAATAGTCTCGGCGAGAACTGCCACTGTAAATCCTGATCCCTGTCTTGAGCTGCTCTCCATCCACCTCCTCCACCACCTCCTCCTCTGTATGATCTGCTGTAATAG'),
        # ('721-742', 'TCCGGTCATCATAACCCCGAT'),
    )
    print(poa.consensus(fasta))


if __name__ == '__main__':
    main()
