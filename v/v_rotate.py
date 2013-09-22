

from myhdl import *
from interface import *

import logging

# req
# ack
# rw
# addr
# data
# command bus handle cpu command
# data bus handle raw data

(ADDR_WIDTH) = (23)
(DATA_WIDTH) = (23)
(INT_WIDTH)  = (32)
(IDLE, WRITE_START, WRITE_LOOP, WRITE_DONE, READ_START, READ_LOOP, READ_DONE) = (0,1,2,3,4,5,6)
(FIFO_DEEP) = (10)


def task_dec_addr (i_base, i_addr, o_h, o_w, i_w_size):
    """ dec addr which is aligned to memory width """

    # declare
#    i_base = Signal(intbv(0, min=0, max=ADDR_WIDTH))
#    i_addr = Signal(intbv(0, min=0, max=ADDR_WIDTH))
#    o_h    = Signal(intbv(0, min=0, max=INT_WIDTH))
#    o_w    = Signal(intbv(0, min=0, max=INT_WIDTH))
#    i_w_size = Signal(intbv(0, min=0, max=INT_WIDTH))

    offset = i_addr - i_base

    @alays_comb
    def task_dec_addr_aligment():
        o_h.next = offset / i_w_size
        o_w.next = offset % i_w_size

    return task_dec_addr_aligment


def task_enc_addr (i_base, o_addr, i_h, i_w, i_w_size):
    """ encode addr which is aligned to memory width """

    # declare
#    i_base = Signal(intbv(0, min=0, max=ADDR_WIDTH))
#    o_addr = Signal(intbv(0, min=0, max=ADDR_WIDTH))
#    i_h    = Signal(intbv(0, min=0, max=INT_WIDTH))
#    i_w    = Signal(intbv(0, min=0, max=INT_WIDTH))
#    i_w_size = Signal(intbv(0, min=0, max=INT_WIDTH))

    @always_comb
    def task_enc_addr_alignment():
        o_addr.next = i_base + i_h * i_w_size + i_w

    return task_enc_addr_alignment


def task_rotate_90(i_h, i_w, o_h, o_w):
    """ rotate 90 degree """
    i_h
    i_w


def task_rotate_90(c_deep, i_clk, i_rst, r_en, r_addr, r_data, w_en, w_addr, w_data, o_empty, o_full):
    """ rotate 90 degree, sync data fifo """

    # declare
#    c_deep = Signal(intbv(0, min=0, max=INT_WIDTH))
#    i_clk  = Signal(intbv(0, min=0, max=0))
#    i_rst  = Signal(intbv(0, min=0, max=0))
#    r_en   = Signal(intbv(0, min=0, max=0))
#    r_data = Signal(intbv(0, min=0, max=data_WIDTH))
#    w_en   = Signal(intbv(0, min=0, max=0))
#    w_data = Signal(intbv(0, min=0, max=data_WIDTH))

    cur_status = Signal(intbv(0, min=0, max=3))
    nxt_status = Signal(intbv(0, min=0, max=3))

    indx = Signal(intbv(0, min=0, max=INT_WIDTH))
    mem_addr_data  = [Signal(intbv(0, min=0, max=ADDR_WIDTH+DATA_WIDTH+1)) for i in xrange(c_deep)]


    @always(indx):
    def task_run_status():
        if indx == c_deep:
            o_full.next = 1
        elif index == 0:
            o_empty.next = 1
        else:
            o_full.next  = 0
            o_empty.next = 0


    @always(clk.posedge)
    def task_run_init():
        """ init FSM """
        if i_rst:
            cur_status.next = IDLE
        else:
            cur_status.next = nxt_status


    @always(cur_status, r_en, o_empty, o_full)
    def task_run_fsm():
        """ run FSM read > write priority """
        if cur_status == IDLE:
            if r_en and !o_empty:
                nxt_status.next = READ_START
            elif w_en and !o_full:
                nxt_status.next = WRITE_START
            else:
                nxt_status.next = IDLE

        elif cur_status == READ_START:
            nxt_status.next = READ_DONE

        elif cur_status == WRITE_START:
            nxt_status.next = WRITE_DONE

        elif cur_status == READ_DONE:
            nxt_status.next = IDLE

        elif cur_status == WRITE_DONE:
            nxt_status.next = IDLE


    @always(cur_status)
    def task_run_func():
        if cur_status == IDLE:
            indx.next = 0

        elif cur_status == READ_START:
            r_data.next = mem[0]
            indx.next = indx - 1

            for i in xrange(c_deep-1):
                mem[i].next = mem[i+1]

        elif cur_status == WRITE_START:
            mem[indx].next = w_data
            indx.next = indx + 1


    return task_run_status, task_run_init, task_run_fsm, task_run_func

