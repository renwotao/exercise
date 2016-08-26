#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	Coroutine
		协程，又称微线程，纤程。
'''

'''
	子程序，或者函数，都是层级调用，子程序调用是通过栈实现，一个线程就是执行一个子程序。
	子程序调用总是一个入口，一次返回，调用顺序是明确的。

	协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的饿时候再返回来接着执行。

	注意，在一个子程序中中断去执行其他子程序，不是函数调用，类似于CPU的中断
'''

'''
	协程的执行像多线程，但协程的特点是在于是一个线程执行，和多线程比，协程的有哪些优势？
	1 最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，
	因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就月明显。
	2 另一个优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，
	在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
'''

'''
	因为协程是一个线程执行，怎么利用多核 CPU 呢？
	最简单的方法是多进程 + 协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
'''

'''
	Python 对协程的支持是通过 generator 实现的。
	在 generator中，不但可以通过 for 循环来迭代，还可以不断调用 next() 函数获取由 yield 语句返回的下一个值。
	但 Python 的 yield 不但可以返回一个值，还可以接收调用者发出的参数。
'''

'''
	例子：
		生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但不一小心就可能死锁。
		
		如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高。
'''
def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('[CONSUMER] Consuming %s...' % n)
		r = '200 OK'

def produce(c):
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCER] Producing %s...' % n)
		r = c.send(n)
		print('[PRODUCER] Consumer return: %s' % r)
	c.close()

c = consumer()
produce(c)


'''
	注意到 consumer 函数是一个 generator， 把一个 consumer 传入 produce 后：
	1 首先调用 c.send(None) 启动生成器
	2 然后，一旦生产了东西，通过 c.send(n) 切换到 consumer 执行
	3 consumer 通过 yield 拿到消息，处理，又通过 yield 把结果传回
	4 produce 拿到 consumer 处理的结果，继续生产下一条消息
	5 produce 决定不生产，通过 c.close() 关闭 consumer，整个过程结束

	整个流程无锁，有一个线程执行， produce 和 consumer 协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

	协程的特点：
		子程序就是协程的一种特例。
'''

