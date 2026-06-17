# 📦 其他研究 | 2026年06月18日

> 本类共 **205** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-205**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-205**

---

### 201. [EvolveNav: Proactive Preflection and Self-Evolving Memory for Zero-Shot Object Goal Navigation](https://arxiv.org/abs/2606.18235)

**<font color=#1a73e8>作者：</font>** Qi Chai, Wenhao Shen, Nanjie Yao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Zero-Shot Object-Goal Navigation (ZS-OGN) requires embodied agents to explore and locate target objects without any prior training. To this end, recent methods leverage foundation models. But they typically rely on static priors and lack adaptation, which leads to repeated errors and costly trial and error. In this paper, we propose a self-evolving ZS-OGN framework that enables continuous test-time improvement. Specifically, we build an agentic rule memory by extracting actionable knowledge from past trajectories. Then, we propose a retrieval strategy based on upper confidence bound, selecting effective rules by balancing semantic relevance and historical success. In addition, we introduce a memory-guided preflection module that forecasts potential outcomes before action, reducing inefficient exploration. Extensive experiments show that our method outperforms existing zero-shot baselines, achieving a 10.1\% improvement in success rate with fewer unnecessary steps.

---


### 202. [Sign-Rank, Index, and List Replicability: Connections and Separations](https://arxiv.org/abs/2606.18236)

**<font color=#1a73e8>作者：</font>** Ari Blondal, Hamed Hatami, Pooya Hatami 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In learning theory, the sign rank of a binary concept class captures the smallest dimension in which it can be represented by points and halfspaces. Despite tremendous interest, lower bounds on sign rank are notoriously difficult to come by. Two recent approaches to the problem establish lower bounds on sign rank by measures that are easier to analyze: the $\mathbb{Z}_2$-index and the list replicability number.
We order these measures, showing that the $\mathbb{Z}_2$-index is upper-bounded by a linear function of the list replicability number. As a main consequence, we obtain a strong separation between sign rank and $\mathbb{Z}_2$-index, thereby resolving a question of Frick, Hosseini, and Vasileuski.
This motivates a thorough study of list replicability, the stronger of the two lower-bounding measures. We establish upper bounds on the list replicability number by two combinatorial measures: height and minimum star number. We also prove a fundamental composition result, showing that the product of two concept classes has list replicability number bounded by the sum of the list replicability numbers of the two classes.

---


### 203. [EventDrive: Event Cameras for Vision-Language Driving Intelligence](https://arxiv.org/abs/2606.18242)

**<font color=#1a73e8>作者：</font>** Dongyue Lu, Rong Li, Ao Liang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras sense the world through asynchronous brightness changes with microsecond latency and high dynamic range, offering motion fidelity far beyond frame-based sensors and capturing temporal structure that conventional exposures often miss. These properties make events a powerful complement to RGB in autonomous driving, especially under blur, glare, and rapid motion, where frame-based perception can become unreliable. However, existing event-aware vision-language models remain limited to generic perception and do not reveal how event sensing contributes to reasoning and decision-making across the full driving loop. We present EventDrive, a large-scale benchmark and model suite that unifies event streams, RGB frames, and language supervision across four core dimensions: Perception, Understanding, Prediction, and Planning, covering captions, structured QA, grounding, motion-state recognition, trajectory forecasting, and planning tasks. Building on this foundation, EventDrive-VLM introduces a multi-horizon event pyramid and a temporal-horizon mixture-of-experts module to adaptively encode and fuse asynchronous and frame-based information for downstream reasoning. Comprehensive evaluation across diverse tasks shows that event streams provide substantial gains in temporal precision, motion awareness, and robustness, bringing event sensing into the center of driving intelligence.

---


### 204. [MOCHI: Motion Enhancement of Collaborative Human-object Interactions](https://arxiv.org/abs/2606.18243)

**<font color=#1a73e8>作者：</font>** Jiye Lee, Yonghun Choi, Jungdam Won  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collaborative human-object interaction shows dynamic and complex movements that require mutual anticipation and continuous adjustment between participants and the shared object. Modeling such collaborative multi-human object interaction (MHOI) scenarios requires high-quality data acquisition as a foundational step; however, this is challenging due to the inherent complexity of MHOI where human-human and human-object interactions occur simultaneously. Such complexity leads to noisy MHOI captures characterized by several artifacts: contact misalignment between hands and objects, motion jitter and temporal inconsistencies in the captured sequences, and missing or incomplete finger-level articulation details. To address these challenges, we present MOCHI (MOtion Enhancement of Collaborative Human-object Interactions), a two-stage framework for enhancing noisy MHOI data. Our approach first generates physically plausible hand grasps through optimization from noisy body input, producing grasps that are both physically plausible and semantically consistent with the body pose, where these optimized grasps are extended into complete hand-object interaction sequences. Consequently, the full-body motion for all participants are refined through a diffusion-based noise optimization framework that uses single-person motion priors. During the optimization process, we introduce optimization objectives to encode human-object and human-human interaction information within these single-person priors. Experimental results demonstrate the effectiveness of our pipeline across diverse MHOI data, either acquired by existing capture methods or synthesized by generative models. We further show robustness of our system across varying numbers of participants and types of interactions, and demonstrate various applications including keyframe-based MHOI creation and data augmentation through varying object geometries.

---


### 205. [Variable-Width Transformers](https://arxiv.org/abs/2606.18246)

**<font color=#1a73e8>作者：</font>** Zhaofeng Wu, Oliver Sieberling, Shawn Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scaling model size, specifically depth and width, has driven significant progress in transformer-based language models. However, most architectures maintain a constant width across all layers, allocating a fixed parameter and computation budget evenly despite different layers potentially playing distinct computational roles. In this work, we empirically investigate nonuniform capacity allocation across network depth by proposing a $\times$-shaped > <former architecture. This design maintains wider early and late layers while narrowing the middle layers, utilizing a parameter-free residual resizing mechanism. Across decoder-only language models ranging from 200M to 2B parameters (dense) and 3B parameters (MoE), our > <former consistently outperforms parameter-matched uniform baselines on language modeling loss. By reducing the average layer width, this architecture also requires fewer overall FLOPs (22% reduction under fitted loss-matched scaling curves) and smaller KV cache memory and I/O cost (15% reduction). In analysis, we show that this bottleneck structure results in qualitatively different representations in residual streams. Overall, our results demonstrate that nonuniform width allocation can result in more resource-optimal scaling of language models.

---


> [!TIP]
> 当前位于：**201-205**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-205**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
