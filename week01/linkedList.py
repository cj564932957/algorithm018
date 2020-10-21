#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   linkedList.py
@Time    :   2020/10/20 14:27:34
@Author  :   chen
@Version :   1.0
@Contact :   cj564932957@outlook.com
@License :   (C)Copyright 2020-2021,
@Desc    :   None
'''

# here put the import lib


class SingleNode:
    """单链表的结点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None


class DoubleNode:
    """双链表的结点"""

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class CycleNode:
    """循环链表的结点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None


class SingleLinkList:

    """单链表"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        # 初始指针指向head
        cur = self._head
        count = 0
        # 指针指向None 表示到达尾部
        while cur is not None:
            count += 1
            # 指针下移
            cur = cur.next
        return count

    def items(self):
        """遍历链表"""
        # 获取head指针
        cur = self._head
        # 循环遍历
        while cur is not None:
            # 返回生成器
            yield cur.item
            # 指针下移
            cur = cur.next

    def add(self, item):
        """向链表头部添加元素"""
        node = SingleNode(item)
        # 新结点指针指向原头部结点
        node.next = self._head
        # 头部结点指针修改为新结点
        self._head = node

    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 先判断是否为空链表
        if self.is_empty():
            # 空链表，_head 指向新结点
            self._head = node
        else:
            # 不是空链表，则找到尾部，将尾部next结点指向新结点
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        """指定位置插入元素"""
        # 指定位置在第一个元素之前，在头部插入
        if index <= 0:
            self.add(item)
        # 指定位置超过尾部，在尾部插入
        elif index > (self.length() - 1):
            self.append(item)
        else:
            # 创建元素结点
            node = SingleNode(item)
            cur = self._head
            # 循环到需要插入的位置
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur is not None:
            # 找到指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                return True
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    def search(self, item):
        """
        查找数据

        Args:
            item ([type]): [description]

        Returns:
            [bool]: [判断是否查到数据]
        """
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def init(self, l: list):
        """
        列表数据转单链表

        Args:
            l (list): [description]
        """
        for item in l:
            self.append(item)
    def reverse(self):
        pass

class DoubleLinkList:
    """
    双链表，其判空，求长，遍历方法和单链表一致，

    重写： 插入，删除，头插，尾查

    Args:
        SingleLinkList ([type]): [description]
    """

    def __init__(self):
        self._head = None

    def is_empty(self):
        """
        判断链表是否为空

        Returns:
            [bool]: [description]
        """
        return self._head is None

    def length(self):
        """
        链表长度

        Returns:
            [type]: [description]
        """
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        """
        遍历链表

        Yields:
            [Node.item]: 
        """
        cur = self._head
        while cur is not None:
            yield cur.item
            cur = cur.next

    def add(self, item):
        """
        在头添加数据

        Args:
            item ([type]): [description]
        """
        node = DoubleNode(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self, item):
        """
        尾部追加

        Args:
            item ([type]): [description]
        """
        node = DoubleNode(item)
        if self.is_empty():
            # 如果是空链表，将 node 赋值给 _head
            self._head = node
        else:
            # 循环移动到链表尾部结点的位置
            cur = self._head
            while cur.next != None:
                cur = cur.next
            # 将尾结点 cur 的 next 属性指向 node
            cur.next = node
            # 将 node 的 prev 属性指向 cur
            node.prev = cur

    def insert(self, pos, item):
        """
        指定位置插入数据

        Args:
            pos ([type]): [description]
            item ([type]): [description]
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = DoubleNode(item)
            cur = self._head
            count = 0
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node

    def remove(self, item):
        """
        删除数据

        Args:
            item ([type]): [description]
        """
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                if cur.next == None:
                    self._head = None
                else:
                    cur.next.prev = None
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    break
                cur = cur.next

    def reverse(self):
        """
        翻转链表
        """
        prev = None
        # 将头节点保存在current中
        current = self._head
        # 当链表为非空的时候，需要执行相应反转的操作
        # 分别将相邻的两个节点的前驱后继关系进行反转
        while current:
            # 将下一个节点保存在next_node中
            next_node = current.next
            # 由于反转链表，因此头节点反转后，成为尾节点，应该指向None
            current.next = prev
            # 尾节点的前驱应指向原本的后继
            current.prev = next_node
            # 更新prev，向后移动
            prev = current
            # 更新current，向后移动
            current = next_node
        # 到达链表尾部时，需要特殊处理
        self._head = prev


class CycleLinkList:
    def __init__(self):
        pass


if __name__ == '__main__':
    s_list = SingleLinkList()
    s_list.init([1, 2, 3, 4, 5])
    s_list.insert(2, 33)
    s_list.remove(4)
    for i in s_list.items():
        print(i)
