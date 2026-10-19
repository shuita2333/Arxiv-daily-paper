# 🧠 大模型相关研究 | 2026年10月20日

> 本类共 **258** 篇论文：已确认 **247** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-258**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-258**

---

### 251. [Batched Contextual Reinforcement II: Does RLVR Need Long Rollout Windows?](https://arxiv.org/abs/2610.22887)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bangji Yang, Hongbo Ma, Ruihan Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long rollout windows make reinforcement learning with verifiable rewards (RLVR) expensive, yet simply shortening them can remove the correctness signal: when every single-problem rollout truncates before an answer, group-relative accuracy advantages vanish. As a technical continuation of Batched Contextual Reinforcement (BCR), we study how concurrent rewards relax this dependence on long windows. Concurrent Constraint Reinforcement (CCR) places three independently verifiable problems in one capped training completion. Correct answers completed before truncation retain credit, while a shared budget encourages shorter useful reasoning without an explicit length penalty. We connect this mechanism to conditional reward- and update-variance analyses and study 4B and 8B mathematical reasoning models. Against single-problem GRPO with a 32k window, CCR with an 8,000-token window reduces tokens per training step from 975,464 to 174,957 on 4B and from 793,832 to 165,788 on 8B, saving 82.1% and 79.1%, respectively. An 8B training trace shows increasing accuracy reward alongside shorter completions. Single-problem evaluations provide supporting evidence of retained reasoning quality. These results identify reward-preserving training structure as a practical route to lower per-step cost in short-window RLVR.

---


### 252. [ODSS-Net: Orthogonally Decoupled Shared-Specific Representations for Multi-Modal Object Re-Identification](https://arxiv.org/abs/2610.22922)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhifeng Ma, Yuhong Feng, Chongyi Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal object re-identification (ReID) leverages complementary information from heterogeneous sensors. Cross-modal alignment and fusion remain challenging. Existing methods mainly reduce modality gaps via feature alignment and fusion. However, alignment may entangle modality-shared structural information with modality-specific cues, while conventional fusion may not fully exploit complementary information. To address these issues, we propose ODSS-Net, a framework for orthogonally decoupled shared-specific representation learning and adaptive fusion of complementary modality-specific features. First, a Shared Structural Feature Construction (SSFC) module suppresses modality-dependent appearance variations and extracts modality-shared structural information. Then, an Orthogonal Specific Feature Learning (OSFL) module aggregates identity-relevant local information and removes the shared-aligned component via geometric orthogonal projection. Finally, a Sample Adaptive Mixture of Experts (SAMoE) module uses the shared structure as routing context to adaptively refine and fuse modality-specific features. Experiments on three benchmarks demonstrate the effectiveness of ODSS-Net for multi-modal object ReID.

---


### 253. [A100: A Hybrid Vision Foundation Model for Agricultural Plant Image Analysis](https://arxiv.org/abs/2610.22991)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mayur Pratim Das, Ajai Dubey, Aksshay Mathew P 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The use of accurate vision models for crop monitoring, disease diagnosis, and plant phenotyping in agriculture is hindered by the lack of expertly annotated data, especially in developing countries. We propose A100, an agricultural vision foundation model that is pre-trained using self-supervised learning on 3 million unlabeled images from fields covering more than 100 crop species. A100 uses a hybrid CNN-Transformer backbone that fuses MBConv stages for local feature extraction with Transformer stages for global contextual representation. A100 uses pre-training with the integration of DINO self-distillation, iBOT masked patch reconstruction, and KoLeo uniformity regularization, resulting in features that are better than ImageNet-12K supervised representations for agricultural applications without any fine-tuning. By utilizing a frozen backbone, the accuracy for crop classification of A100 is 95.37%, which is +2.56% better than ImageNet-12K, and reduces the leaf count error by 10.4% on the GroMo25 phenotyping benchmark, proving that the same backbone can be used for classification and regression tasks. After full fine-tuning, the performance of A100 is 99.90% on 32-class crop identification and 99.02% on 44-class disease detection. On the difficult PlantDoc dataset, A100 outperforms all baselines, such as CvT-13 (64.89% against 63.56%). Remarkably, A100 obtains 98.01% accuracy on plant classification using just 1% of the labelled data (about 284 images per category), showing great label efficiency for use cases with limited labeling. Under an identical protocol, A100 also outperforms the publicly released agricultural foundation models FoMo4Wheat and LeafVision by more than 14 points at 1% labels. We plan to publicly release our pretrained model to allow agricultural professionals to adapt A100 for various plant analysis applications using limited annotations.

---


### 254. [Distill Until Divergence: Error-Truncated Hindsight Distillation for Agentic RL](https://arxiv.org/abs/2610.23048)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yibin Huang, Conghui Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon interaction requires agents to make multiple decisions in a changing environment. Outcome-based GRPO lacks fine-grained guidance for intermediate decisions. Recent methods distill completed trajectories into reusable skills and use hindsight-conditioned OPD to provide dense token-level credit. However, skill-induced probability shifts do not necessarily represent reward-aligned credit; especially after an erroneous action changes subsequent interaction states, skill-conditioned supervision may become mismatched with the current state. To address this mismatch, we propose \methodname{}, which routes two complementary hindsight skills according to trajectory outcomes and error boundaries: Positive skills capture successful workflows to reinforce successful trajectories and pre-error decisions, while Negative skills capture failure-specific corrections to target decisive errors. The post-error suffix is optimized exclusively by GRPO, retaining outcome-based learning without extending potentially mismatched hindsight supervision. Extensive experiments demonstrate competitive task performance and support effective fine-grained credit allocation.

---


### 255. [Scene-Designer: Learning Design Intelligence for Agentic 3D Scene Generation](https://arxiv.org/abs/2610.23121)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xuanyu Liu, Hongyan Feng, Miao Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating complete, coherent, and usable 3D indoor scenes from natural language requires strong \textbf{design intelligence}: the ability to design high-quality scenes and critique their quality. However, existing approaches either rely on general-purpose models lacking domain-specific design experience or learn from static scenes. In this work, we introduce \textbf{Scene-Designer}, an agentic framework that learns design intelligence through complementary design and critique experiences. We construct two datasets: \textbf{Scene-OTA-35K}, which provides Observation--Thought--Action supervision for learning scene design and efficient error correction, and \textbf{Scene-OTC-15K}, which provides Observation--Thought--Critic supervision for learning scene quality critique across physical validity, functional correctness, and layout coherence. Based on these experiences, we propose \textbf{Scene-GRPO}, a Critic-guided GRPO framework that improves design decisions and reduces unnecessary trial-and-error corrections. Extensive experiments demonstrate that Scene-Designer achieves superior performance in physical validity, functional correctness, and layout coherence, while the learned Scene-Critic significantly outperforms general-purpose models in scene critique. Moreover, test-time Critic guidance further improves scene generation, showing that the Critic can provide useful guidance beyond training. Additional analysis suggests a trend of mutual enhancement between scene design and critique abilities.

---


### 256. [LongForge: Measuring and Improving Long-Context Instruction Data via Evidence-Assertion Reasoning Graphs](https://arxiv.org/abs/2610.23167)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ziyang Chen, Junlong Jia, Xing Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing quality control for long-context instruction-tuning data is a one-shot judgment inside the generation pipeline that leaves only a scalar, revealing neither which document parts an answer uses nor how many reasoning steps it writes down; the data can thus be neither audited nor controlled. We formalize data quality as a property of the alignment structure among document, question, and answer, and build LongForge, which pairs an analyzer that measures long-context data with a synthesizer that generates it. The analyzer reverse-reconstructs each sample into an evidence-assertion reasoning graph and programmatically computes four dimensions on it: breadth, depth, correctness, and completeness. Every reading traces back to specific evidence spans and reasoning steps, making data auditable. Measuring seven mainstream datasets reveals two previously unquantified defects: breadth barely grows with document length, and depth is generally low, the two being nearly orthogonal. The synthesizer then embeds the analyzer into generation, gating on correctness and completeness and deferring breadth and depth to a training-time mixture over measured values, which makes the training distribution controllable. On two backbones, its two mixtures, LongForge-1 and LongForge-N, outperform the strongest baseline by 2.2-4.7 points on average over six long-context benchmarks, and in a controlled comparison that holds the gate and the candidate pool fixed, raising breadth and depth alone is worth a further 1.16 points, making the structural distribution of training data a lever on downstream quality rather than only a description of it.

---


### 257. [Beyond Reward Scoring: Online Multi-Agent Preference Learning for Multimodal Response Generation](https://arxiv.org/abs/2610.23256)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ziyun Zou, Jiwoo Hong, Yifan Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal preference alignment often follows a score-based RLHF pipeline: a reward model is first trained to learn human preferences, then used to score on-policy responses and optimize the response model's generation. This turns preference supervision into a scalar signal for generation: a model may learn to produce answers with higher preference scores, but is rarely trained explicitly to learn the reasons underlying human preferences. We therefore ask whether making preference understanding an internal capability of the response model can improve its generation. To investigate this question, we propose \textbf{PrefMind}, an online dual-agent reinforcement learning framework with two trainable agents: a response Generator and a preference Critic. Given a pair of candidate responses, the agents analyze and discuss which response better aligns with human preference. Human labels supervise their judgments and corrections. For pairs on which both the Generator and revised Critic correctly identify the human-preferred response, the Generator produces an improved answer, and the Critic compares it against the original preferred response to provide a generation reward. Both agents are jointly updated from interactions sampled with their current policies. Through this process, \textbf{PrefMind} trains the Generator to understand human preferences via explicit judgment and correction, and to translate this understanding into better responses. Experiments across three model scales show improvements in both standalone preference judgment and downstream response generation.

---


### 258. [Agentic Physics-Grounded Video Generation via Memory-Augmented In-Context Reasoning](https://arxiv.org/abs/2610.23677)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xikang Guan, Shaocong Yang, Yanqi Bao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical plausibility is essential for realistic video generation. Existing methods impose physical guidance before synthesis via simulations or refined prompts, but this can limit dynamic diversity, miss errors that emerge only after generation, and require repeated regeneration when inconsistencies remain. We therefore study a generate-diagnose-repair paradigm that preserves the original generation capability and selectively repairs physical inconsistencies afterward, raising two key questions: what to repair and how to repair? To address them, we introduce PhysRepair, an agentic video generation framework that combines causal reasoning over the observed physical failure with prior repair experience to enable localized and adaptive correction. Specifically, Spatiotemporal Causal Constraints identify the first invalid physical state and its causally affected states, producing a repair specification that guides physically plausible local regeneration while preserving unaffected content. Experience-augmented In-context Learning combines the ongoing repair context with relevant experience from previous repairs, allowing the agent to adapt its repair decisions across diverse physical failures and accumulate completed trajectories for future cases. Experiments on Physics-IQ Verified across solid mechanics, fluid dynamics, optics, thermodynamics, and magnetism demonstrate that PhysRepair consistently improves the physical plausibility of generated videos over existing methods. Our project page is available at this https URL.

---


> [!TIP]
> 当前位于：**251-258**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-258**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
