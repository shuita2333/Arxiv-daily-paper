# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**801-810**（第 17/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | **801-810**

---

### 801. [H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression](https://arxiv.org/abs/2610.18125)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Or Ronai, Vladimir Kulikov, Tomer Michaeli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free diffusion-based compression methods repurpose the generative priors of a diffusion or a flow model to compress data without retraining them as task-specific codecs. Recent codebook-based approaches such as Turbo-DDCM achieve strong perceptual quality at ultra-low bitrates, but their reliance on dense Gaussian codebooks remains costly in both memory and computation, and scales poorly with the large latent dimensions of modern image and video generators. Their combinatorial bitstream encoding further becomes computationally heavy at this scale. We introduce H-DDCM, a scalable generative compression framework that replaces Gaussian codebooks with implicit randomized Hadamard dictionaries. The fast Walsh-Hadamard transform allows for implicitly synthesizing full-dimensional dictionaries with $O(d \log d)$ compute for projection and reconstruction and $O(d)$ memory, without materializing the full-dimensional dictionary. We further introduce an efficient table-free lexicographic coding scheme that makes combinatorial encoding practical at larger dimensions. Beyond images, we adapt the framework to an autoregressive video flow model and develop a streaming compression scheme that periodically re-encodes recently reconstructed frames into a fresh KV-cache prefix, preserving temporal context across segments at no additional transmitted bits. This enables long-form, close to real-time generative video compression on a single GPU. Across image and video benchmarks, H-DDCM achieves competitive rate-distortion-perception performance while substantially reducing the memory and computational overhead of codebook-based training-free generative compression.

---


### 802. [Looped Reasoning Finishes Earlier Than You Think](https://arxiv.org/abs/2610.18174)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sumin Park, T. Konstantin Rusch  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped reasoning with dynamic depth can be viewed as relaxation toward solution attractors in a learned dynamical landscape. In practice, however, latent trajectories often oscillate, cycle, or drift rather than cleanly converge to stable fixed points. How these non-stationary dynamics contribute to reasoning and constrain convergence remains unclear. We show that slowly decaying oscillatory modes can impose their convergence rate on coupled latent dynamics, creating a bottleneck. Yet damping these modes indiscriminately can disrupt the reasoning computation they support. This tension motivates an architectural approach: introducing rotational degrees of freedom along which symmetry-generated rotational motion leaves the reasoning-relevant quotient dynamics unchanged by construction. We propose QRR (Quotient Recurrent Reasoner), a gauge-equivariant recurrent architecture with an exact per-token phase-rotation symmetry. Motion along these symmetry directions leaves the quotient representation unchanged and is dynamically decoupled from reasoning-relevant dynamics. Empirically, QRR achieves stable and faster convergence to solution roots in quotient space, without forming a dominant slow oscillatory bottleneck, while matching or surpassing recent recurrent reasoning models on Sudoku, Maze, and Mini-ARC.

---


### 803. [Unsupervised and Supervised Approaches for Infrared Small Target Detection : Overview, Challenges and Perspectives (Part 2)](https://arxiv.org/abs/2610.18291)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Thierry Bouwmans, Anastasia Zakharova, Belmar Garcia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Since the rise of supervised deep learning modelet dets, researchers has attempt to solve infrared small targection using various models like conventional neural networks, GANS, Transformers, Mixture of Experts and recent graph/hypergraph neural networks. Moreover, these deep neural networks methods surpassed the traditional unsupervised models and the low-rank and sparse decomposition unsupervised models reviewed in "Traditional and Recent Approaches for Infrared Small Target Detection : Overview, Challenges and Perspectives (Part 1). In this context, the aim of this paper is to provide a complete survey of the deep learning models in infrared small target detection. First, we categorize the different approaches found in the literature in terms of the modeling models of strategies. Then, we have discussed them in terms of the critical situations that they claim to handle. Furthermore, we present the specific performance evaluation. Then, we conclude with several promising directions for future research.

---


### 804. [The Smart Buildings Challenge: Learning Foundation Models for Real-World Optimization at Scale](https://arxiv.org/abs/2610.18511)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Judah Goldfeder, Ayush Rai, Philippe M. Wyder 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Buildings cause nearly 40\% of carbon emissions in the US. Of total building emissions, HVAC systems are responsible for approximately 40-60\% and account for 15\% of global energy consumption. Despite advances in artificial intelligence, most buildings still operate as inefficiently as they did decades ago. Building optimization, perhaps more so than any other optimization problem, has enormous potential for Machine Learning (ML) driven impact on climate change, in both the short and long term. One of the biggest obstacles for building optimization is the lack of policy transfer. Most building control systems, whether simulation or learning based, don't generalize: they only work well for the building they were developed for, but not for other buildings. To solve this problem, we propose a challenge for the development of building foundation models that easily adapt to new buildings with minimal configuration and thereby enable building optimization to scale across the globe. Participants will build control policies on a set of simulated buildings, and have their policies evaluated on an unseen set of buildings. The buildings vary in size, layout, weather, material properties, and HVAC system. Successful outcomes from this initiative promise a massive leap forward in global sustainability efforts and demonstrate the great potential of ML to combat climate change.

---


### 805. [Beyond the Encoder: Object-Centric Representations Emerging from Segmentation Foundation Models](https://arxiv.org/abs/2610.18543)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Michalis Pistos, Bartłomiej W. Papież  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models are increasingly used as feature extractors for downstream tasks with limited data, typically through representations obtained from their encoders. However, foundation models trained for structured tasks such as segmentation also form object-specific representations during task execution, whose transferability remains largely unexplored. We investigate Segment Anything Model 2 (SAM2) object pointers, compact object-level representations produced through the segmentation pathway, as transferable representations for downstream tumour prediction. Through experiments on two PET/CT tumour prediction tasks, we find that object pointers learned using segmentation supervision alone already encode tumour-discriminative information, despite never being optimised for the downstream labels. We further introduce task-guided object pointers, where an auxiliary objective jointly shapes the object pointer space for the downstream prediction together with segmentation. Task-guided pointers improve cancer-type classification, outperforming conventional encoder-based transfer and radiomics, while segmentation-only pointers perform best on the more challenging recurrence prediction task. Representation analyses reveal associations between object pointers and interpretable radiomics features, class-dependent organisation of the learned representation space, and explicit spatial grounding around the segmented tumour. Together, these findings suggest that useful transferable representations can emerge through the execution of a foundation model's primary task, providing an alternative to conventional encoder-based transfer.

---


### 806. [Reading Right, Acting Wrong: Diagnosing Decision Failures of System One Models in Agent Loops](https://arxiv.org/abs/2610.18579)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yubo Li, Ramayya Krishnan, Rema Padman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> System One models choose an agent's next action by scoring a supplied set of options in a single pass. This makes them fast and cheap, but when they choose wrongly there is nothing to inspect: did the model misread what the agent has seen, or read it correctly and still act wrongly? We answer behaviorally. On a frozen benchmark of agent decision states from simulated environments, customer-service policies, tool use, web navigation and coding, we pair every next-action question with factual probes about the same state, each answered independently. Across seventeen fast systems and a reasoning model, the answer is consistent: most wrong actions follow correct reading, and the more accurate a system, the more of its errors take this form. These errors are not noise; they gather on the same states across systems of every kind. Where the probed facts provably determine the action, models that read every fact still fail to combine them, and their own answers, composed by code, repair the failure. On real states, what is missing is often not a fact but the next sub-goal.

---


### 807. [Kwai Summary Attention V2 Technical Report](https://arxiv.org/abs/2610.18654)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** OneRec Team, Chenglong Chu, Guohong Mu 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Summary-token architectures such as Kwai Summary Attention (KSA) compress distant context into learnable Summary token per chunk, and hybrid variants interleave these layers with full attention to retain exact access to the original text. In such hybrid KSA-Full architecture, the interleaving inserted summary tokens are served as a streaming flow role across different layers. Although effective, however, it also introduce some bottlenecks: (1) the different layers summary compression chunk must be same, therefore hard to reach a flexible KV Cache compression, e.g., different layer set different summary compression chunk window. (2) in the full-attention layers, the summary token introduced additional computation cost, but such layer ignore them and still pay quadratic prefilling, therefore unfriendly to the computation side. Motivated by them, we developed the KSA V2, which not only achieves a more flexible KV cache memory compression but also reduces the computation cost in Full attention layer. Specifically, we found that the summary tokens can serve two roles: the KV memory and sparse indexer.

---


### 808. [Knowing the User Is Not Knowing What We Established: Grounding Awareness in Personal Agents](https://arxiv.org/abs/2610.18684)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiajun Chen, Xinyue Chen, Yicheng Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal-agent memory has largely focused on learning what users know, prefer, and want. However, knowing the user does not necessarily mean knowing what the user and the agent have established together. An assistant's proposal should not become an authorized instruction merely because it is remembered. We introduce Grounding Awareness, the ability to distinguish accepted, unacknowledged, revised, and scoped arrangements when selecting actions. We develop a controlled benchmark to test whether agents can tell the difference between proposals users have accepted and those they have not, and whether they apply accepted arrangements only where appropriate. Across multiple agents and memory systems, we find that strong memory performance does not ensure Grounding Awareness. More surprisingly, providing more complete user information can increase execution of unacknowledged proposals, while persistent memory can cause agents to treat these proposals as if they were user instructions. We trace these failures through memory writing, retrieval, and action selection. Finally, we introduce Grounding Layer, a lightweight, training-free extension that explicitly tracks grounding status and checks consequential actions, substantially improving agent behavior without modifying models or memory systems.

---


### 809. [Code-Switching Detection via Language-Selective Dimensions in Speech Foundation Models](https://arxiv.org/abs/2610.18726)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jie Chi, Zakaria Aldeneh, Masha Fedzechkina 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Code-switching (CS), the alternation between languages within an utterance, is common in multilingual speech but underrepresented in pretraining corpora. Increasing CS coverage requires finding relevant utterances in large speech collections so that they can be included in training data. One way to find such utterances is to transcribe the speech and detect language alternation in the text, but this depends on obtaining accurate multilingual transcriptions. We propose a lightweight method that detects CS directly from speech. It uses frame-level language information in pretrained speech encoders to determine whether both languages are present within an utterance. Specifically, we identify language-selective hidden-state dimensions using monolingual recordings and aggregate their frame-level activations into a CS prediction. With a small CS set used to tune a decision rule, we show that the Whisper-small encoder achieves a mean F1 of $0.798$ across 14 language pairs in CS-FLEURS, compared with $0.776$ for a CNN and $0.751$ for a HuBERT linear baseline trained for monolingual language identification. Our findings suggest that pretrained speech encoders already encode the information needed to identify CS utterances, and they provide a lightweight tool for building more representative multilingual corpora.

---


### 810. [Rubrics from the Task, Verdicts from Evidence: Pointwise Rubric Rewards with Tool-Augmented Judges](https://arxiv.org/abs/2610.18766)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianci Liu, Haoyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based reward models (RMs) evaluate responses against explicit criteria. However, existing methods often derive criteria from observed response candidates, introducing response-induced bias that may limit rubric generalizability. Their judges also struggle with mechanical constraints when relying on reading alone, and commonly used pairwise judges provide only relative preferences, complicating their direct use for policy optimization. We propose ReVeR, a pointwise rubric RM that derives hard rules and graded principles by reasoning about the instruction alone and evaluates responses independently through tool-augmented judging. Both components are trained through label-blind distillation, in which preference labels only filter a teacher's outputs, yielding ReVeR-Traces, a large-scale dataset of rubric-reasoning and judging trajectories. Experiments demonstrate that ReVeR outperforms pairwise rubric RMs in average preference accuracy, most clearly on instruction following, as well as in test-time scaling and downstream policy optimization. We further find that generator RL improves preference accuracy while reducing rubric fidelity, and that higher preference accuracy does not necessarily translate into better downstream policies. These findings highlight that rubric fidelity, preference accuracy, and downstream utility are distinct properties, shedding light on future RM research.

---


> [!TIP]
> 当前位于：**801-810**（第 17/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | **801-810**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
