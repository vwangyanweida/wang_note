/*************************************************************************
    > File Name: test.sh
    > Author: wangyanwei
    > Mail:  
    > Created Time: 日 12/ 6 14:36:29 2015
 ************************************************************************/
#! /bin/sh

num=123
func1()
{
    num=321
    echo $num
}

func2()
{
    local num=456
    echo $num
}
echo $num
func1
echo $num
func2
echo $num
