for i in 10 100 1000 10000 100000
do  
    echo "$i" > query_count.txt
    echo "Handling Database with size of $i:"
    for j in 1 2 3 4 5 6 7
    do
        python3 create_gunreg_input.py < query_count.txt
        time python3 test/test_sse_schemes/gunreg_model.py < input.txt > output.txt
    done
    echo ""
done