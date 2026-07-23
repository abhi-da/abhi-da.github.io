---
layout: single
title: "Introduction to Propositional Logic"
date: 2026-07-21
subject: "Mathematics for Economists"
toc: true
---
You might have seen MEMES like: ![Math Meme]({{ '/assets/images/useless_math_meme.jpg' | relative_url }})

But is it really the case?

See, you may not use the exact same problems in your daily life, but it teaches you how to use a that particular tool. It controls the world. We use it to put man in the moon. Yet, it is considered useless by most of the people.

The graduate mathematics is very different then higher secondary schools mathematics, at least in India. There's a lot of rigour in graduate texts. By rigor, I mean doing the same maths with great precision. In senior secondary school, continuity is often taught intuitively: "a function is continuous if you can draw its graph in a single, free-flowing pen stroke without lifting your paper."At the graduate level, however, math demands absolute precision. Intuitive rules are replaced with formal, rigorous definitions (like the $\epsilon$-$\delta$ criterion) which we will study later in limits and continuity.We need this level of rigour because human visual intuition breaks down when dealing with complex functions. For example, $x \cdot \sin\left(\frac{1}{x}\right)$ cannot be hand-drawn. Also, computers cannot read or draw such images on their own. To make them draw such graphs, we need to feed exact definitions to them.

Imagine senior secondary as knowing how to use Python libraries, while in graduation, you are actually building them.

When you know where a particular formula or theorem comes from, the result becomes very interesting.

For example, what does the idiom "Chhattis ka aakda" mean, and how do you think it originated?

Let me ask a simple question. Take a solid ball in 3D space. Is it possible to cut it into 5 pieces, rotate those pieces around, reassemble them without stretching anything, and end up with two identical solid balls of the exact same size as the original? The intuition would say - No. That is not possible. Cause the volume then doubles.

However, [Banach–Tarski paradox](https://en.wikipedia.org/wiki/Banach%E2%80%93Tarski_paradox) says, we can.

And No. I have got no idea about how the proof is done. These were just to stimulate the curiosity in the mind that intuition is not always correct and hence we need to define things precisely.

For example, How many months have 28 days? Some would say February. But that is wrong, All 12 months have 28 days.
Precision would mean, How many months have only 28 days. And that again cannot be February, cause we don't know if we are talking about leap or not a leap year.

Now, the above texts were to generate a bit of curiosity in the mind. I hope math sounds interesting now.

With that, let me tell you how to approach math. You cannot just read it like a novel. You can skip things which are not useful. You can move backward and forward between texts. Every author has written books on the basis of their understanding; the same doesn't apply to you.

But you will need to practice and understand how things are working. The more you practice, the better you get. By practicing, I don't mean by-hearting.

The above paragraph were some written by me, and some ideas were borrowed from [How to think like a Mathematician-2009](https://blngcc.wordpress.com/wp-content/uploads/2008/11/2-kevin-houston-how-to-think-like-a-mathematician.pdf)

With that, Let us begin with our topic: **Logic**

It is advisable to give a read to chapter 0 of [Mathematical Proofs: A Transition to Advanced Mathematics - Chartrand et al](https://www.amazon.in/Mathematical-Proofs-Transition-Advanced-Mathematics/dp/0321797094).

## Logic

### Statements

A sentence which can be either _true_ or _false_ but not _both_ is a statement. For example,

1. 2 is an even number. This statement is true.
2. 6 is a prime number. This statement is false.

Now sometimes, a sentence can be true or false, but you cannot declare immediately.
