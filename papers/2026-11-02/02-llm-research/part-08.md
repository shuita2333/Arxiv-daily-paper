# 🧠 大模型相关研究 | 2026年11月02日

> 本类共 **353** 篇论文：已确认 **335** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-353**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-353**

---

### 351. [Your LR Schedule May Not Be Principled: Effective Learning Rate Scheduling in Weight-Normalized Training](https://arxiv.org/abs/2610.40362)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qifan Yu, Xinyu Ma, Xingyan Bin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight-normalized (WN) training is emerging as a compelling alternative to conventional weight decay (WD), with recent studies reporting substantial pretraining loss gains. We show that these gains are driven primarily by the induced effective learning rate (ELR) trajectory rather than by normalization alone. Matching ELR trajectories largely collapses the training loss dynamics of WN and WD. Schedule design should therefore target ELR rather than the nominal learning rate (LR) alone. Building on this principle, we propose AIR (Affine Inverse-square-Root decay), which combines a theoretically derived $1/\sqrt{t}$ decay with an affine adjustment to satisfy prescribed peak and terminal LRs over a finite training horizon. We further identify late-stage ELR scheduling as a key source of its gains, because a shared late schedule attenuates the effect of earlier LR choices. Experiments on 128 B-token Mixture-of-Experts pretraining demonstrate that AIR outperforms cosine and other candidate schedules in training loss, downstream performance, and hyperparameter robustness, reducing terminal training loss by approximately 0.01 relative to cosine at matched cumulative LR. Applying the same ELR trajectory to WD reproduces the corresponding training dynamics, showing that the benefits extend beyond fixed-norm training and establishing ELR as the principled scheduling object.

---


### 352. [Training Foundation Models with a Single Algorithm](https://arxiv.org/abs/2610.40564)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuda Song, Alvin Zhang, Fahim Tajwar 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are typically trained in stages: pretraining, midtraining, supervised fine-tuning (SFT), and reinforcement learning (RL), with changes in both data and learning algorithms. We show that this algorithmic separation is not fundamental. By deriving suitable RL objectives as maximum-likelihood fitting to model-generated target distributions, we place all of these stages under a single likelihood-based training algorithm, unified training. This perspective turns the foundation-model training lifecycle into a problem of choosing which data to train on, in what proportions, and when, with conventional staged training as a special case. We instantiate this framework in a unified training system that mixes static data and RL generations within a single trainer. Across controlled and real-world experiments, unified training improves the accuracy-compute tradeoff and task coverage while preserving broader capabilities, and provides a stronger starting point for continual learning. This work lays the groundwork for a unified science of foundation-model training, connecting mathematical principles, training infrastructure, and the development of model capabilities.

---


### 353. [Probing Spatial State Representations in Visual Foundation Models](https://arxiv.org/abs/2610.40636)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Baiqiao Yin, Zhongang Cai, Ruisi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An observer sees only part of the surrounding world, yet must keep track of what lies beyond the current view. Spatial perception therefore involves more than recognizing individual images: it calls for a persistent spatial state that is updated under self-motion and used to guide action. Do visual foundation models provide representations that support such a state? We study this question through four levels of spatial capability---spatial structure, object persistence, predictive spatial update, and actionability---using frozen-feature probes on ten representations under streaming egocentric observations of static indoor environments. The resulting capability profiles vary across tasks, network layers, and prefix lengths: strong readout of the visible scene does not ensure accurate object persistence or future-feature retrieval. Matched controls separate readout accuracy from reliance on visual history and motion. Native future prediction retains recoverable spatial structure, but a spatial reader trained on real features does not transfer to predicted features unchanged. Finally, goal-dependent candidate selection does not establish reliable continuous action utility: predicted actions respond to goal changes, yet supplying the correct goal does not reliably improve progress. Across the four levels, object persistence and actionability build on camera-pose readout, whereas feature prediction builds on visible-scene readout. Together, these findings motivate evaluating spatial representations not only by what can be decoded from them, but by whether that information is maintained beyond observation, updated predictively, and used for goal-directed action.

---


> [!TIP]
> 当前位于：**351-353**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-353**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
