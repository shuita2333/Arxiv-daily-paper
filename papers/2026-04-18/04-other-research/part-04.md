# 📦 其他研究 | 2026年04月18日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-234](./part-05.md)

---

### 151. [xFODE+: Explainable Type-2 Fuzzy Additive ODEs for Uncertainty Quantification](https://arxiv.org/abs/2604.14880)

**<font color=#1a73e8>作者：</font>** Ertugrul Kececi, Tufan Kumbasar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in Deep Learning (DL) have boosted data-driven System Identification (SysID), but reliable use requires Uncertainty Quantification (UQ) alongside accurate predictions. Although UQ-capable models such as Fuzzy ODE (FODE) can produce Prediction Intervals (PIs), they offer limited interpretability. We introduce Explainable Type-2 Fuzzy Additive ODEs for UQ (xFODE+), an interpretable SysID model which produces PIs alongside point predictions while retaining physically meaningful incremental states. xFODE+ implements each fuzzy additive model with Interval Type-2 Fuzzy Logic Systems (IT2-FLSs) and constraints membership functions to the activation of two neighboring rules, limiting overlap and keeping inference locally transparent. The type-reduced sets produced by the IT2-FLSs are aggregated to construct the state update together with the PIs. The model is trained in a DL framework via a composite loss that jointly optimizes prediction accuracy and PI quality. Results on benchmark SysID datasets show that xFODE+ matches FODE in PI quality and achieves comparable accuracy, while providing interpretability.

---


### 152. [The Missing Knowledge Layer in AI: A Framework for Stable Human-AI Reasoning](https://arxiv.org/abs/2604.14881)

**<font color=#1a73e8>作者：</font>** Rikard Rosenbacke, Carl Rosenbacke, Victor Rosenbacke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly integrated into decision-making in areas such as healthcare, law, finance, engineering, and government. Yet they share a critical limitation: they produce fluent outputs even when their internal reasoning has drifted. A confident answer can conceal uncertainty, speculation, or inconsistency, and small changes in phrasing can lead to different conclusions. This makes LLMs useful assistants but unreliable partners in high-stakes contexts.
Humans exhibit a similar weakness, often mistaking fluency for reliability. When a model responds smoothly, users tend to trust it, even when both model and user are drifting together. This paper is the first in a five-paper research series on stabilising human-AI reasoning. The series proposes a two-layer approach: Parts II-IV introduce human-side mechanisms such as uncertainty cues, conflict surfacing, and auditable reasoning traces, while Part V develops a model-side Epistemic Control Loop (ECL) that detects instability and modulates generation accordingly.
Together, these layers form a missing operational substrate for governance by increasing signal-to-noise at the point of use. Stabilising interaction makes uncertainty and drift visible before enforcement is applied, enabling more precise capability governance. This aligns with emerging compliance expectations, including the EU AI Act and ISO/IEC 42001, by making reasoning processes traceable under real conditions of use.
The central claim is that fluency is not reliability. Without structures that stabilise both human and model reasoning, AI cannot be trusted or governed where it matters most.

---


### 153. [xFODE: An Explainable Fuzzy Additive ODE Framework for System Identification](https://arxiv.org/abs/2604.14883)

**<font color=#1a73e8>作者：</font>** Ertugrul Kececi, Tufan Kumbasar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in Deep Learning (DL) have strengthened data-driven System Identification (SysID), with Neural and Fuzzy Ordinary Differential Equation (NODE/FODE) models achieving high accuracy in nonlinear dynamic modeling. Yet, system states in these frameworks are often reconstructed without clear physical meaning, and input contributions to the state derivatives remain difficult to interpret. To address these limitations, we propose Explainable FODE (xFODE), an interpretable SysID framework with integrated DL-based training. In xFODE, we define states in an incremental form to provide them with physical meanings. We employ fuzzy additive models to approximate the state derivative, thereby enhancing interpretability per input. To provide further interpretability, Partitioning Strategies (PSs) are developed, enabling the training of fuzzy additive models with explainability. By structuring the antecedent space during training so that only two consecutive rules are activated for any given input, PSs not only yield lower complexity for local inference but also enhance the interpretability of the antecedent space. To train xFODE, we present a DL framework with parameterized membership function learning that supports end-to-end optimization. Across benchmark SysID datasets, xFODE matches the accuracy of NODE, FODE, and NLARX models while providing interpretable insights.

---


### 154. [FSDETR: Frequency-Spatial Feature Enhancement for Small Object Detection](https://arxiv.org/abs/2604.14884)

**<font color=#1a73e8>作者：</font>** Jianchao Huang, Fengming Zhang, Haibo Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small object detection remains a significant challenge due to feature degradation from downsampling, mutual occlusion in dense clusters, and complex background interference. To address these issues, this paper proposes FSDETR, a frequency-spatial feature enhancement framework built upon the RT-DETR baseline. By establishing a collaborative modeling mechanism, the method effectively leverages complementary structural information. Specifically, a Spatial Hierarchical Attention Block (SHAB) captures both local details and global dependencies to strengthen semantic representation. Furthermore, to mitigate occlusion in dense scenes, the Deformable Attention-based Intra-scale Feature Interaction (DA-AIFI) focuses on informative regions via dynamic sampling. Finally, the Frequency-Spatial Feature Pyramid Network (FSFPN) integrates frequency filtering with spatial edge extraction via the Cross-domain Frequency-Spatial Block (CFSB) to preserve fine-grained details. Experimental results show that with only 14.7M parameters, FSDETR achieves 13.9% APS on VisDrone 2019 and 48.95% AP50 tiny on TinyPerson, showing strong performance on small-object benchmarks. The code and models are available at this https URL.

---


### 155. [RACER: Retrieval-Augmented Contextual Rapid Speculative Decoding](https://arxiv.org/abs/2604.14885)

**<font color=#1a73e8>作者：</font>** Zihong Zhang, Zuchao Li, Lefei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive decoding in Large Language Models (LLMs) generates one token per step, causing high inference latency. Speculative decoding (SD) mitigates this through a guess-and-verify strategy, but existing training-free variants face trade-offs: retrieval-based drafts break when no exact match exists, while logits-based drafts lack structural guidance. We propose $\textbf{RACER}$ ($\textbf{R}$etrieval-$\textbf{A}$ugmented $\textbf{C}$ont$\textbf{e}$xtual $\textbf{R}$apid Speculative Decoding), a lightweight and training-free method that integrates retrieved exact patterns with logit-driven future cues. This unification supplies both reliable anchors and flexible extrapolation, yielding richer speculative drafts. Experiments on Spec-Bench, HumanEval, and MGSM-ZH demonstrate that RACER consistently accelerates inference, achieving more than $2\times$ speedup over autoregressive decoding, and outperforms prior training-free methods, offering a scalable, plug-and-play solution for efficient LLM decoding. Our source code is available at $\href{this https URL}{this https URL}$.

---


### 156. [Cooperate to Compete: Strategic Data Generation and Incentivization Framework for Coopetitive Cross-Silo Federated Learning](https://arxiv.org/abs/2604.14886)

**<font color=#1a73e8>作者：</font>** Thanh Linh Nguyen, Nguyen Van Huynh, Quoc-Viet Pham  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In data-sensitive domains such as healthcare, cross-silo federated learning (CFL) allows organizations to collaboratively train AI models without sharing raw data. However, practical CFL deployments are inherently coopetitive, in which organizations cooperate during model training while competing in downstream markets. In such settings, training contributions, including data volume, quality, and diversity, can improve the global model yet inadvertently strengthen rivals. This dilemma is amplified by non-IID data, which leads to asymmetric learning gains and undermines sustained participation. While existing competition-aware CFL and incentive-design approaches reward organizations based on marginal training contributions, they fail to account for the costs of strengthening competitors. In this paper, we introduce CoCoGen+, a coopetition-compatible data generation and incentivization framework that jointly models non-IID data and inter-organizational competition while endogenizing GenAI-based synthetic data generation as a strategic decision. Specifically, CoCoGen+ formulates each training round as a weighted potential game, where organizations strategically decide how much synthetic data to generate by balancing learning performance gains against computational costs and competition-caused utility losses. We then provide a tractable equilibrium characterization and derive implementable generation strategies to maximize social welfare. To promote long-term collaboration, we integrate a payoff redistribution-based incentive mechanism to compensate organizations for their contributions and competition-caused utility degradation. Experiments on varying learning tasks validate the feasibility of CoCoGen+. The results show how non-IID data, competition intensity, and incentives shape organizational strategies and social welfare, while CoCoGen+ outperforms baselines in efficiency.

---


### 157. [MemoSight: Unifying Context Compression and Multi Token Prediction for Reasoning Acceleration](https://arxiv.org/abs/2604.14889)

**<font color=#1a73e8>作者：</font>** Xinyu Liu, Xin Liu, Bo Jin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Chain-of-thought (CoT) reasoning enables LLMs to solve challenging reasoning problems, as KV cache grows linearly with the number of generated tokens, CoT reasoning faces scaling issues in terms of speed and memory usage. In this work, we propose MemoSight (Memory-Foresight-based reasoning), a unified framework that integrates both context compression and multi-token prediction to mitigate the efficiency issues while maintaining CoT reasoning performance. Our framework adopts the same minimalist design for both context compression and multi-token prediction via special tokens and their corresponding position layout tailored to each token type. Comprehensive experiments on four reasoning benchmarks demonstrate that MemoSight reduces the KV cache footprint by up to 66% and accelerates inference by 1.56x, while outperforming existing CoT compression methods.

---


### 158. [Governing Reflective Human-AI Collaboration: A Framework for Epistemic Scaffolding and Traceable Reasoning](https://arxiv.org/abs/2604.14898)

**<font color=#1a73e8>作者：</font>** Rikard Rosenbacke, Carl Rosenbacke, Victor Rosenbacke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have advanced rapidly, from pattern recognition to emerging forms of reasoning, yet they remain confined to linguistic simulation rather than grounded understanding. They can produce fluent outputs that resemble reflection, but lack temporal continuity, causal feedback, and anchoring in real-world interaction. This paper proposes a complementary approach in which reasoning is treated as a relational process distributed between human and model rather than an internal capability of either.
Building on recent work on "System-2" learning, we relocate reflective reasoning to the interaction layer. Instead of engineering reasoning solely within models, we frame it as a cognitive protocol that can be structured, measured, and governed using existing systems. This perspective emphasizes collaborative intelligence, combining human judgment and contextual understanding with machine speed, memory, and associative capacity.
We introduce "The Architect's Pen" as a practical method. Like an architect who thinks through drawing, the human uses the model as an external medium for structured reflection. By embedding phases of articulation, critique, and revision into human-AI interaction, the dialogue itself becomes a reasoning loop: human abstraction -> model articulation -> human reflection.
This reframes the question from whether the model can think to whether the human-AI system can reason. The framework enables auditable reasoning traces and supports alignment with emerging governance standards, including the EU AI Act and ISO/IEC 42001. It provides a practical path toward more transparent, controllable, and accountable AI use without requiring new model architectures.

---


### 159. [Comparison of Modern Multilingual Text Embedding Techniques for Hate Speech Detection Task](https://arxiv.org/abs/2604.14907)

**<font color=#1a73e8>作者：</font>** Evaldas Vaiciukynas, Paulius Danenas, Linas Ablonskis 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online hate speech and abusive language pose a growing challenge for content moderation, especially in multilingual settings and for low-resource languages such as Lithuanian. This paper investigates to what extent modern multilingual sentence embedding models can support accurate hate speech detection in Lithuanian, Russian, and English, and how their performance depends on downstream modeling choices and feature dimensionality. We introduce LtHate, a new Lithuanian hate speech corpus derived from news portals and social networks, and benchmark six modern multilingual encoders (potion, gemma, bge, snow, jina, e5) on LtHate, RuToxic, and EnSuperset using a unified Python pipeline. For each embedding, we train both a one class HBOS anomaly detector and a two class CatBoost classifier, with and without principal component analysis (PCA) compression to 64-dimensional feature vectors. Across all datasets, two class supervised models consistently and substantially outperform one class anomaly detection, with the best configurations achieving up to 80.96% accuracy and AUC ROC of 0.887 in Lithuanian (jina), 92.19% accuracy and AUC ROC of 0.978 in Russian (e5), and 77.21% accuracy and AUC ROC of 0.859 in English (e5 with PCA). PCA compression preserves almost all discriminative power in the supervised setting, while showing some negative impact for the unsupervised anomaly detection case. These results demonstrate how modern multilingual sentence embeddings combined with gradient boosted decision trees provide robust soft-computing solutions for multilingual hate speech detection applications.

---


### 160. [Multi-User mmWave Beam and Rate Adaptation via Combinatorial Satisficing Bandits](https://arxiv.org/abs/2604.14908)

**<font color=#1a73e8>作者：</font>** Emre Özyıldırım, Barış Yaycı, Umut Eren Akturk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study downlink beam and rate adaptation in a multi-user mmWave MISO system where multiple base stations (BSs), each using analog beamforming from finite codebooks, serve multiple single-antenna user equipments (UEs) with a unique beam per UE and discrete data transmission rates. BSs learn about transmission success based on ACK/NACK feedback. To encode service goals, we introduce a satisficing throughput threshold $\tau_r$ and cast joint beam and rate adaptation as a combinatorial semi-bandit over beam-rate tuples. Within this framework, we propose SAT-CTS, a lightweight, threshold-aware policy that blends conservative confidence estimates with posterior sampling, steering learning toward meeting $\tau_r$ rather than merely maximizing. Our main theoretical contribution provides the first finite-time regret bounds for combinatorial semi-bandits with satisficing objective: when $\tau_r$ is realizable, we upper bound the cumulative satisficing regret to the target with a time-independent constant, and when $\tau_r$ is non-realizable, we show that SAT-CTS incurs only a finite expected transient outside committed CTS rounds, after which its regret is governed by the sum of the regret contributions of restarted CTS rounds, yielding an $O((\log T)^2)$ standard regret bound. On the practical side, we evaluate the performance via cumulative satisficing regret to $\tau_r$ alongside standard regret and fairness. Experiments with time-varying sparse multipath channels show that SAT-CTS consistently reduces satisficing regret and maintains competitive standard regret, while achieving favorable average throughput and fairness across users, indicating that feedback-efficient learning can equitably allocate beams and rates to meet QoS targets without channel state knowledge.

---


### 161. [Efficient Fuzzy Private Set Intersection from Secret-shared OPRF](https://arxiv.org/abs/2604.14909)

**<font color=#1a73e8>作者：</font>** Xinpeng Yang, Meng Hao, Chenkai Weng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Private set intersection (PSI) enables a sender holding a set $Q$ of size $m$ and a receiver holding a set $W$ of size $n$ to securely compute the intersection $Q \cap W$. Fuzzy PSI (FPSI) is a PSI variant where the receiver learns the items $q \in Q$ for which there exists some $w \in W$ satisfying $\mathsf{dist}(q, w) \le \delta$ under a given distance metric. Although several FPSI works are proposed for $L_{p}$ distance metrics with $p \in [1, \infty]$, they either heavily rely on expensive homomorphic encryptions, or incur undesirable complexity, e.g., exponential to the element dimension, both of which lead to poor practical efficiency.
In this work, we propose efficient FPSI protocols for $L_{p \in [1, \infty]}$ distance metrics, primarily leveraging significantly cheaper symmetric-key operations. Our protocols achieve linear communication and computation complexity in the set sizes $m,n$, the dimension $d$, and the distance threshold $\delta$. Our core building block is an oblivious programmable PRF with secret-shared outputs, which may be of independent interest. Furthermore, we incorporate a prefix technique that reduces the dependence on the distance threshold $\delta$ to logarithmic, which is particularly suitable for large $\delta$.
We implement our FPSI protocols and compare them with state-of-the-art constructions. Experimental results demonstrate that our protocols consistently and significantly outperform existing works across all settings. Specifically, our protocols achieve a speedup of $12{\sim}145\times$ in running time and a reduction of $3{\sim}8\times$ in communication cost compared to Gao et al.~(ASIACRYPT'24) and a speedup of $9{\sim}80\times$ in running time and a reduction of $5{\sim}19\times$ in communication cost compared to Dang et al.~(CCS'25).

---


### 162. [Reward-Aware Trajectory Shaping for Few-step Visual Generation](https://arxiv.org/abs/2604.14910)

**<font color=#1a73e8>作者：</font>** Rui Li, Bingyu Li, Yuanzhi Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving high-fidelity generation in extremely few sampling steps has long been a central goal of generative modeling. Existing approaches largely rely on distillation-based frameworks to compress the original multi-step denoising process into a few-step generator. However, such methods inherently constrain the student to imitate a stronger multi-step teacher, imposing the teacher as an upper bound on student performance. We argue that introducing \textbf{preference alignment awareness} enables the student to optimize toward reward-preferred generation quality, potentially surpassing the teacher instead of being restricted to rigid teacher imitation. To this end, we propose \textbf{Reward-Aware Trajectory Shaping (RATS)}, a lightweight framework for preference-aligned few-step generation. Specifically, teacher and student latent trajectories are aligned at key denoising stages through horizon matching, while a \textbf{reward-aware gate} is introduced to adaptively regulate teacher guidance based on their relative reward performance. Trajectory shaping is strengthened when the teacher achieves higher rewards, and relaxed when the student matches or surpasses the teacher, thereby enabling continued reward-driven improvement. By seamlessly integrating trajectory distillation, reward-aware gating, and preference alignment, RATS effectively transfers preference-relevant knowledge from high-step generators without incurring additional test-time computational overhead. Experimental results demonstrate that RATS substantially improves the efficiency--quality trade-off in few-step visual generation, significantly narrowing the gap between few-step students and stronger multi-step generators.

---


### 163. [Beyond Prompts: Unconditional 3D Inversion for Out-of-Distribution Shapes](https://arxiv.org/abs/2604.14914)

**<font color=#1a73e8>作者：</font>** Victoria Yue Chen, Emery Pierson, Léopold Maillard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven inversion of generative models is a core paradigm for manipulating 2D or 3D content, unlocking numerous applications such as text-based editing, style transfer, or inverse problems. However, it relies on the assumption that generative models remain sensitive to natural language prompts. We demonstrate that for state-of-the-art native text-to-3D generative models, this assumption often collapses. We identify a critical failure mode where generation trajectories are drawn into latent ``sink traps'': regions where the model becomes insensitive to prompt modifications. In these regimes, changes to the input text fail to alter internal representations in a way that alters the output geometry. Crucially, we observe that this is not a limitation of the model's \textit{geometric} expressivity; the same generative models possess the ability to produce a vast diversity of shapes but, as we demonstrate, become insensitive to out-of-distribution \textit{text} guidance. We investigate this behavior by analyzing the sampling trajectories of the generative model, and find that complex geometries can still be represented and produced by leveraging the model's unconditional generative prior. This leads to a more robust framework for text-based 3D shape editing that bypasses latent sinks by decoupling a model's geometric representation power from its linguistic sensitivity. Our approach addresses the limitations of current 3D pipelines and enables high-fidelity semantic manipulation of out-of-distribution 3D shapes. Project webpage: this https URL

---


### 164. [Dual-Axis Generative Reward Model Toward Semantic and Turn-taking Robustness in Interactive Spoken Dialogue Models](https://arxiv.org/abs/2604.14920)

**<font color=#1a73e8>作者：</font>** Yifu Chen, Shengpeng Ji, Zhengqing Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Achieving seamless, human-like interaction remains a key challenge for full-duplex spoken dialogue models (SDMs). Reinforcement learning (RL) has substantially enhanced text- and vision-language models, while well-designed reward signals are crucial for the performance of RL. We consider RL a promising strategy to address the key challenge for SDMs. However, a fundamental barrier persists: prevailing automated metrics for assessing interaction quality rely on superficial proxies, such as behavioral statistics or timing-prediction accuracy, failing to provide reliable reward signals for RL. On the other hand, human evaluations, despite their richness, remain costly, inconsistent, and difficult to scale. We tackle this critical barrier by proposing a Dual-Axis Generative Reward Model, which is trained to understand complex interaction dynamics using a detailed taxonomy and an annotated dataset, produces a single score and, crucially, provides separate evaluations for semantic quality and interaction timing. Such dual outputs furnish precise diagnostic feedback for SDMs and deliver a dependable, instructive reward signal suitable for online reinforcement learning. Our model achieves state-of-the-art performance on interaction-quality assessment across a wide spectrum of datasets, spanning synthetic dialogues and complex real-world interactions.

---


### 165. [LongAct: Harnessing Intrinsic Activation Patterns for Long-Context Reinforcement Learning](https://arxiv.org/abs/2604.14922)

**<font color=#1a73e8>作者：</font>** Bowen Ping, Zijun Chen, Tingfeng Hui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has emerged as a critical driver for enhancing the reasoning capabilities of Large Language Models (LLMs). While recent advancements have focused on reward engineering or data synthesis, few studies exploit the model's intrinsic representation characteristics to guide the training process. In this paper, we first observe the presence of high-magnitude activations within the query and key vectors when processing long contexts. Drawing inspiration from model quantization -- which establishes the criticality of such high-magnitude activations -- and the insight that long-context reasoning inherently exhibits a sparse structure, we hypothesize that these weights serve as the pivotal drivers for effective model optimization. Based on this insight, we propose LongAct, a strategy that shifts from uniform to saliency-guided sparse updates. By selectively updating only the weights associated with these significant activations, LongAct achieves an approximate 8% improvement on LongBench v2 and enhances generalization on the RULER benchmark. Furthermore, our method exhibits remarkable universality, consistently boosting performance across diverse RL algorithms such as GRPO and DAPO. Extensive ablation studies suggest that focusing on these salient features is key to unlocking long-context potential.

---


### 166. [Improving Sparse Autoencoder with Dynamic Attention](https://arxiv.org/abs/2604.14925)

**<font color=#1a73e8>作者：</font>** Dongsheng Wang, Jinsen Zhang, Dawei Su 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, sparse autoencoders (SAEs) have emerged as a promising technique for interpreting activations in foundation models by disentangling features into a sparse set of concepts. However, identifying the optimal level of sparsity for each neuron remains challenging in practice: excessive sparsity can lead to poor reconstruction, whereas insufficient sparsity may harm interpretability. While existing activation functions such as ReLU and TopK provide certain sparsity guarantees, they typically require additional sparsity regularization or cherry-picked hyperparameters. We show in this paper that dynamically sparse attention mechanisms using sparsemax can bridge this trade-off, due to their ability to determine the activation numbers in a data-dependent manner. Specifically, we first explore a new class of SAEs based on the cross-attention architecture with the latent features as queries and the learnable dictionary as the key and value matrices. To encourage sparse pattern learning, we employ a sparsemax-based attention strategy that automatically infers a sparse set of elements according to the complexity of each neuron, resulting in a more flexible and general activation function. Through comprehensive evaluation and visualization, we show that our approach successfully achieves lower reconstruction loss while producing high-quality concepts, particularly in top-n classification tasks.

---


### 167. [Hybrid Latents -- Geometry-Appearance-Aware Surfel Splatting](https://arxiv.org/abs/2604.14928)

**<font color=#1a73e8>作者：</font>** Neel Kelkar, Simon Niedermayr, Klaus Engel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce a hybrid Gaussian-hash-grid radiance representation for reconstructing 2D Gaussian scene models from multi-view images. Similar to NeST splatting, our approach reduces the entanglement between geometry and appearance common in NeRF-based models, but adds per-Gaussian latent features alongside hash-grid features to bias the optimizer toward a separation of low- and high-frequency scene components. This explicit frequency-based decomposition reduces the tendency of high-frequency texture to compensate for geometric errors. Encouraging Gaussians with hard opacity falloffs further strengthens the separation between geometry and appearance, improving both geometry reconstruction and rendering efficiency. Finally, probabilistic pruning combined with a sparsity-inducing BCE opacity loss allows redundant Gaussians to be turned off, yielding a minimal set of Gaussians sufficient to represent the scene. Using both synthetic and real-world datasets, we compare against the state of the art in Gaussian-based novel-view synthesis and demonstrate superior reconstruction fidelity with an order of magnitude fewer primitives.

---


### 168. [Generative Data Augmentation for Skeleton Action Recognition](https://arxiv.org/abs/2604.14933)

**<font color=#1a73e8>作者：</font>** Xu Dong, Wanqing Li, Anthony Adeyemi-Ejeye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton-based human action recognition is a powerful approach for understanding human behaviour from pose data, but collecting large-scale, diverse, and well-annotated 3D skeleton datasets is both expensive and labor-intensive. To address this challenge, we propose a conditional generative pipeline for data augmentation in skeleton action recognition. Our method learns the distribution of real skeleton sequences under the constraint of action labels, enabling the synthesis of diverse and high-fidelity data. Even with limited training samples, it can effectively generate skeleton sequences and achieve competitive recognition performance in low-data scenarios, demonstrating strong generalisation in downstream tasks. Specifically, we introduce a Transformer-based encoder-decoder architecture, combined with a generative refinement module and a dropout mechanism, to balance fidelity and diversity during sampling. Experiments on HumanAct12 and the refined NTU-RGBD (NTU-VIBE) dataset show that our approach consistently improves the accuracy of multiple skeleton-based action recognition models, validating its effectiveness in both few-shot and full-data settings. The source code can be found at here.

---


### 169. [XQ-MEval: A Dataset with Cross-lingual Parallel Quality for Benchmarking Translation Metrics](https://arxiv.org/abs/2604.14934)

**<font color=#1a73e8>作者：</font>** Jingxuan Liu, Zhi Qu, Jin Tei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic evaluation metrics are essential for building multilingual translation systems. The common practice of evaluating these systems is averaging metric scores across languages, yet this is suspicious since metrics may suffer from cross-lingual scoring bias, where translations of equal quality receive different scores across languages. This problem has not been systematically studied because no benchmark exists that provides parallel-quality instances across languages, and expert annotation is not realistic. In this work, we propose XQ-MEval, a semi-automatically built dataset covering nine translation directions, to benchmark translation metrics. Specifically, we inject MQM-defined errors into gold translations automatically, filter them by native speakers for reliability, and merge errors to generate pseudo translations with controllable quality. These pseudo translations are then paired with corresponding sources and references to form triplets used in assessing the qualities of translation metrics. Using XQ-MEval, our experiments on nine representative metrics reveal the inconsistency between averaging and human judgment and provide the first empirical evidence of cross-lingual scoring bias. Finally, we propose a normalization strategy derived from XQ-MEval that aligns score distributions across languages, improving the fairness and reliability of multilingual metric evaluation.

---


### 170. [Prompt-to-Gesture: Measuring the Capabilities of Image-to-Video Deictic Gesture Generation](https://arxiv.org/abs/2604.14953)

**<font color=#1a73e8>作者：</font>** Hassan Ali, Doreen Jirak, Luca Müller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gesture recognition research, unlike NLP, continues to face acute data scarcity, with progress constrained by the need for costly human recordings or image processing approaches that cannot generate authentic variability in the gestures themselves. Recent advancements in image-to-video foundation models have enabled the generation of photorealistic, semantically rich videos guided by natural language. These capabilities open up new possibilities for creating effort-free synthetic data, raising the critical question of whether video Generative AI models can augment and complement traditional human-generated gesture data. In this paper, we introduce and analyze prompt-based video generation to construct a realistic deictic gestures dataset and rigorously evaluate its effectiveness for downstream tasks. We propose a data generation pipeline that produces deictic gestures from a small number of reference samples collected from human participants, providing an accessible approach that can be leveraged both within and beyond the machine learning community. Our results demonstrate that the synthetic gestures not only align closely with real ones in terms of visual fidelity but also introduce meaningful variability and novelty that enrich the original data, further supported by superior performance of various deep models using a mixed dataset. These findings highlight that image-to-video techniques, even in their early stages, offer a powerful zero-shot approach to gesture synthesis with clear benefits for downstream tasks.

---


### 171. [FedGUI: Benchmarking Federated GUI Agents across Heterogeneous Platforms, Devices, and Operating Systems](https://arxiv.org/abs/2604.14956)

**<font color=#1a73e8>作者：</font>** Wenhao Wang, Haoting Shi, Mengying Yuan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Training GUI agents with traditional centralized methods faces significant cost and scalability challenges. Federated learning (FL) offers a promising solution, yet its potential is hindered by the lack of benchmarks that capture real-world, cross-platform heterogeneity. To bridge this gap, we introduce FedGUI, the first comprehensive benchmark for developing and evaluating federated GUI agents across mobile, web, and desktop platforms. FedGUI provides a suite of six curated datasets to systematically study four crucial types of heterogeneity: cross-platform, cross-device, cross-OS, and cross-source. Extensive experiments reveal several key insights: First, we show that cross-platform collaboration improves performance, extending prior mobile-only federated learning to diverse GUI environments; Second, we demonstrate the presence of distinct heterogeneity dimensions and identify platform and OS as the most influential factors. FedGUI provides a vital foundation for the community to build more scalable and privacy-preserving GUI agents for real-world deployment. Our code and data are publicly available at this https URL..

---


### 172. [Frequency-Enhanced Dual-Subspace Networks for Few-Shot Fine-Grained Image Classification](https://arxiv.org/abs/2604.14958)

**<font color=#1a73e8>作者：</font>** Meijia Wang, Guochao Wang, Haozhen Chu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot fine-grained image classification aims to recognize subcategories with high visual similarity using only a limited number of annotated samples. Existing metric learning-based methods typically rely solely on spatial domain features. Confined to this single perspective, models inevitably suffer from inherent texture biases, entangling essential structural details with high-frequency background noise. Furthermore, lacking cross-view geometric constraints, single-view metrics tend to overfit this noise, resulting in structural instability under few-shot conditions. To address these issues, this paper proposes the Frequency-Enhanced Dual-Subspace Network (FEDSNet). Specifically, FEDSNet utilizes the Discrete Cosine Transform (DCT) and a low-pass filtering mechanism to explicitly isolate low-frequency global structural components from spatial features, thereby suppressing background interference. Truncated Singular Value Decomposition (SVD) is employed to construct independent, low-rank linear subspaces for both spatial texture and frequency structural features. An adaptive gating mechanism is designed to dynamically fuse the projection distances from these dual views. This strategy leverages the structural stability of the frequency subspace to prevent the spatial subspace from overfitting to background features. Extensive experiments on four benchmark datasets - CUB-200-2011, Stanford Cars, Stanford Dogs, and FGVC-Aircraft - demonstrate that FEDSNet exhibits excellent classification performance and robustness, achieving highly competitive results compared to existing metric learning algorithms. Complexity analysis further confirms that the proposed network achieves a favorable balance between high accuracy and computational efficiency, providing an effective new paradigm for few-shot fine-grained visual recognition.

---


### 173. [Blazing the trails before beating the path: Sample-efficient Monte-Carlo planning](https://arxiv.org/abs/2604.14974)

**<font color=#1a73e8>作者：</font>** Jean-Bastien Grill, Michal Valko, Rémi Munos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> You are a robot and you live in a Markov decision process (MDP) with a finite or an infinite number of transitions from state-action to next states. You got brains and so you plan before you act. Luckily, your roboparents equipped you with a generative model to do some Monte-Carlo planning. The world is waiting for you and you have no time to waste. You want your planning to be efficient. Sample-efficient. Indeed, you want to exploit the possible structure of the MDP by exploring only a subset of states reachable by following near-optimal policies. You want guarantees on sample complexity that depend on a measure of the quantity of near-optimal states. You want something, that is an extension of Monte-Carlo sampling (for estimating an expectation) to problems that alternate maximization (over actions) and expectation (over next states). But you do not want to StOP with exponential running time, you want something simple to implement and computationally efficient. You want it all and you want it now. You want TrailBlazer.

---


### 174. [Hybrid Decision Making via Conformal VLM-generated Guidance](https://arxiv.org/abs/2604.14980)

**<font color=#1a73e8>作者：</font>** Debodeep Banerjee, Burcu Sayin, Stefano Teso 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building on recent advances in AI, hybrid decision making (HDM) holds the promise of improving human decision quality and reducing cognitive load. We work in the context of learning to guide (LtG), a recently proposed HDM framework in which the human is always responsible for the final decision: rather than suggesting decisions, in LtG the AI supplies (textual) guidance useful for facilitating decision making. One limiting factor of existing approaches is that their guidance compounds information about all possible outcomes, and as a result it can be difficult to digest. We address this issue by introducing ConfGuide, a novel LtG approach that generates more succinct and targeted guidance. To this end, it employs conformal risk control to select a set of outcomes, ensuring a cap on the false negative rate. We demonstrate our approach on a real-world multi-label medical diagnosis task. Our empirical evaluation highlights the promise of ConfGuide.

---


### 175. [AI-Enabled Covert Channel Detection in RF Receiver Architectures](https://arxiv.org/abs/2604.14987)

**<font color=#1a73e8>作者：</font>** Abdelrahman Emad Abdelazim, Alan Rodrigo Diaz-Rizo, Hassan Aboushady 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Covert channels (CCs) in wireless chips pose a serious security threat, as they enable the exfiltration of sensitive information from the chip to an external attacker. In this work, we propose an AI-based defense mechanism deployed at the RF receiver, where the model directly monitors raw I/Q samples to detect, in real time, the presence of a CC embedded within an otherwise nominal signal. We first compact a state-of-the-art convolutional neural network (CNN), achieving an 80% reduction in parameters, which is an essential requirement for efficient edge deployment. When evaluated on the open-source hardware Trojan (HT)-based CC dataset, the compacted CNN attains an average accuracy of 90.28% for CC detection and 86.50% for identifying the underlying HT, with results averaged across SNR values above 1 dB. For practical communication scenarios where SNR > 20 dB, the model achieves over 97% accuracy for both tasks. These results correspond to a minimal performance degradation of less than 2% compared to the baseline model. The compacted CNN is further benchmarked against alternative classifiers, demonstrating an excellent accuracy-model size trade-off. Finally, we design a lightweight CNN hardware accelerator and demonstrate it on an FPGA, achieving very low resource utilization and an efficiency of 107 GOPs/W. Being the first AI hardware accelerator proposed specifically for CC detection, we compare it against state-of-the-art AI accelerators for RF signal classification tasks such as modulation recognition, showing superior performance.

---


### 176. [ConGISATA: A Framework for Continuous Gamified Information Security Awareness Training and Assessment](https://arxiv.org/abs/2604.14996)

**<font color=#1a73e8>作者：</font>** Ofir Cohen, Ron Bitton, Asaf Shabtai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The incidence of cybersecurity attacks utilizing social engineering techniques has increased. Such attacks exploit the fact that in every secure system, there is at least one individual with the means to access sensitive information. Since it is easier to deceive a person than it is to bypass the defense mechanisms in place, these types of attacks have gained popularity. This situation is exacerbated by the fact that people are more likely to take risks in their passive form, i.e., risks that arise due to the failure to perform an action. Passive risk has been identified as a significant threat to cybersecurity. To address these threats, there is a need to strengthen individuals' information security awareness (ISA). Therefore, we developed ConGISATA - a continuous gamified ISA training and assessment framework based on embedded mobile sensors; a taxonomy for evaluating mobile users' security awareness served as the basis for the sensors' design. ConGISATA's continuous and gradual training process enables users to learn from their real-life mistakes and adapt their behavior accordingly. ConGISATA aims to transform passive risk situations (as perceived by an individual) into active risk situations, as people tend to underestimate the potential impact of passive risks. Our evaluation of the proposed framework demonstrates its ability to improve individuals' ISA, as assessed by the sensors and in simulations of common attack vectors.

---


### 177. [Flow of Truth: Proactive Temporal Forensics for Image-to-Video Generation](https://arxiv.org/abs/2604.15003)

**<font color=#1a73e8>作者：</font>** Yuzhuo Chen, Zehua Ma, Han Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid rise of image-to-video (I2V) generation enables realistic videos to be created from a single image but also brings new forensic demands. Unlike static images, I2V content evolves over time, requiring forensics to move beyond 2D pixel-level tampering localization toward tracing how pixels flow and transform throughout the video. As frames progress, embedded traces drift and deform, making traditional spatial forensics ineffective. To address this unexplored dimension, we present **Flow of Truth**, the first proactive framework focusing on temporal forensics in I2V generation. A key challenge lies in discovering a forensic signature that can evolve consistently with the generation process, which is inherently a creative transformation rather than a deterministic reconstruction. Despite this intrinsic difficulty, we innovatively redefine video generation as *the motion of pixels through time rather than the synthesis of frames*. Building on this view, we propose a learnable forensic template that follows pixel motion and a template-guided flow module that decouples motion from image content, enabling robust temporal tracing. Experiments show that Flow of Truth generalizes across commercial and open-source I2V models, substantially improving temporal forensics performance.

---


### 178. [What Is the Minimum Architecture for Prolepsis? Early Irrevocable Commitment Across Tasks in Small Transformers](https://arxiv.org/abs/2604.15010)

**<font color=#1a73e8>作者：</font>** Éric Jacopin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When do transformers commit to a decision, and what prevents them from correcting it? We introduce \textbf{prolepsis}: a transformer commits early, task-specific attention heads sustain the commitment, and no layer corrects it. Replicating \citeauthor{lindsey2025biology}'s (\citeyear{lindsey2025biology}) planning-site finding on open models (Gemma~2 2B, Llama~3.2 1B), we ask five questions. (Q1)~Planning is invisible to six residual-stream methods; CLTs are necessary. (Q2)~The planning-site spike replicates with identical geometry. (Q3)~Specific attention heads route the decision to the output, filling a gap flagged as invisible to attribution graphs. (Q4)~Search requires ${\leq}16$ layers; commitment requires more. (Q5)~Factual recall shows the same motif at a different network depth, with zero overlap between recurring planning heads and the factual top-10. Prolepsis is architectural: the template is shared, the routing substrates differ. All experiments run on a single consumer GPU (16\,GB VRAM).

---


### 179. [Quality-Aware Calibration for AI-Generated Image Detection in the Wild](https://arxiv.org/abs/2604.15027)

**<font color=#1a73e8>作者：</font>** Fabrizio Guillaro, Vincenzo De Rosa, Davide Cozzolino 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Significant progress has been made in detecting synthetic images, however most existing approaches operate on a single image instance and overlook a key characteristic of real-world dissemination: as viral images circulate on the web, multiple near-duplicate versions appear and lose quality due to repeated operations like recompression, resizing and cropping. As a consequence, the same image may yield inconsistent forensic predictions based on which version has been analyzed. In this work, to address this issue we propose QuAD (Quality-Aware calibration with near-Duplicates) a novel framework that makes decisions based on all available near-duplicates of the same image. Given a query, we retrieve its online near-duplicates and feed them to a detector: the resulting scores are then aggregated based on the estimated quality of the corresponding instance. By doing so, we take advantage of all pieces of information while accounting for the reduced reliability of images impaired by multiple processing steps. To support large-scale evaluation, we introduce two datasets: AncesTree, an in-lab dataset of 136k images organized in stochastic degradation trees that simulate online reposting dynamics, and ReWIND, a real-world dataset of nearly 10k near-duplicate images collected from viral web content. Experiments on several state-of-the-art detectors show that our quality-aware fusion improves their performance consistently, with an average gain of around 8% in terms of balanced accuracy compared to plain average. Our results highlight the importance of jointly processing all the images available online to achieve reliable detection of AI-generated content in real-world applications. Code and data are publicly available at this https URL

---


### 180. [Autogenesis: A Self-Evolving Agent Protocol](https://arxiv.org/abs/2604.15034)

**<font color=#1a73e8>作者：</font>** Wentao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in LLM based agent systems have shown promise in tackling complex, long horizon tasks. However, existing agent protocols (e.g., A2A and MCP) under specify cross entity lifecycle and context management, version tracking, and evolution safe update interfaces, which encourages monolithic compositions and brittle glue code. We introduce \textbf{\textsc{Autogenesis Protocol (AGP)}}, a self evolution protocol that decouples what evolves from how evolution occurs. Its Resource Substrate Protocol Layer (RSPL) models prompts, agents, tools, environments, and memory as protocol registered resources\footnote{Unless otherwise specified, resources refer to instances of the five RSPL entity types: \emph{prompt}, \emph{agent}, \emph{tool}, \emph{environment}, \emph{memory} with agent \emph{outputs}.} with explicit state, lifecycle, and versioned interfaces. Its Self Evolution Protocol Layer (SEPL) specifies a closed loop operator interface for proposing, assessing, and committing improvements with auditable lineage and rollback. Building on \textbf{\textsc{AGP}}, we present \textbf{\textsc{Autogenesis System (AGS)}}, a self-evolving multi-agent system that dynamically instantiates, retrieves, and refines protocol-registered resources during execution. We evaluate \textbf{\textsc{AGS}} on multiple challenging benchmarks that require long horizon planning and tool use across heterogeneous resources. The results demonstrate consistent improvements over strong baselines, supporting the effectiveness of agent resource management and closed loop self evolution.

---


### 181. [When Fairness Metrics Disagree: Evaluating the Reliability of Demographic Fairness Assessment in Machine Learning](https://arxiv.org/abs/2604.15038)

**<font color=#1a73e8>作者：</font>** Khalid Adnan Alsayed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The evaluation of fairness in machine learning systems has become a central concern in high-stakes applications, including biometric recognition, healthcare decision-making, and automated risk assessment. Existing approaches typically rely on a small number of fairness metrics to assess model behaviour across group partitions, implicitly assuming that these metrics provide consistent and reliable conclusions. However, different fairness metrics capture distinct statistical properties of model performance and may therefore produce conflicting assessments when applied to the same system. In this work, we investigate the consistency of fairness evaluation by conducting a systematic multi-metric analysis of demographic bias in machine learning models. Using face recognition as a controlled experimental setting, we evaluate model performance across multiple group partitions under a range of commonly used fairness metrics, including error-rate disparities and performance-based measures. Our results demonstrate that fairness assessments can vary significantly depending on the choice of metrics, leading to contradictory conclusions regarding model bias. To quantify this phenomenon, we introduce the Fairness Disagreement Index (FDI), a measure designed to capture the degree of inconsistency across fairness metrics. We further show that disagreement remains high across thresholds and model configurations. These findings highlight a critical limitation in current fairness evaluation practices and suggest that single-metric reporting is insufficient for reliable bias assessment.

---


### 182. [CoGrid & the Multi-User Gymnasium: A Framework for Multi-Agent Experimentation](https://arxiv.org/abs/2604.15044)

**<font color=#1a73e8>作者：</font>** Chase McDonald, Cleotilde Gonzalez  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The increasing integration of artificial intelligence (AI) in everyday life brings with it new challenges and questions for regarding how humans interact with autonomous agents. Multi-agent experiments, where humans and AI act together, can offer important opportunities to study social decision making, but there is a lack of accessible tooling available to researchers to run such experiments. We introduce two tools designed to reduce these barriers. The first, CoGrid, is a multi-agent grid-based simulation library with dual NumPy and JAX backends. The second, Multi-User Gymnasium (MUG), translates such simulation environments directly into interactive web-based experiments. MUG supports interactions with arbitrary numbers of humans and AI, utilizing either server-authoritative or peer-to-peer networking with rollback netcode to account for latency. Together, these tools can enable researchers to deploy studies of human-AI interaction, facilitating inquiry into core questions of psychology, cognition, and decision making and their relationship to human-AI interaction. Both tools are open source and available to the broader research community. Documentation and source code is available at {cogrid, multi-user-gymnasium}.this http URL. This paper details the functionality of these tools and presents several case studies to illustrate their utility in human-AI multi-agent experimentation.

---


### 183. [Implicit Neural Representations: A Signal Processing Perspective](https://arxiv.org/abs/2604.15047)

**<font color=#1a73e8>作者：</font>** Dhananjaya Jayasundara, Vishal M. Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations (INRs) mark a fundamental shift in signal modeling, moving from discrete sampled data to continuous functional representations. By parameterizing signals as neural networks, INRs provide a unified framework for representing images, audio, video, 3D geometry, and beyond as continuous functions of their coordinates. This functional viewpoint enables signal operations such as differentiation to be carried out analytically through automatic differentiation rather than through discrete approximations. In this article, we examine the evolution of INRs from a signal processing perspective, emphasizing spectral behavior, sampling theory, and multiscale representation. We trace the progression from standard coordinate based networks, which exhibit a spectral bias toward low frequency components, to more advanced designs that reshape the approximation space through specialized activations, including periodic, localized, and adaptive functions. We also discuss structured representations, such as hierarchical decompositions and hash grid encodings, that improve spatial adaptivity and computational efficiency. We further highlight the utility of INRs across a broad range of applications, including inverse problems in medical and radar imaging, compression, and 3D scene representation. By interpreting INRs as learned signal models whose approximation spaces adapt to the underlying data, this article clarifies the field's core conceptual developments and outlines open challenges in theoretical stability, weight space interpretability, and large scale generalization.

---


### 184. ["From remembering to shaping": Narrating Shared Experiences by Co-Designing Cultural Heritage Artifacts in Collaborative VR](https://arxiv.org/abs/2604.15058)

**<font color=#1a73e8>作者：</font>** Yushang Yang, Fanxu Meng, Fiona Fui-Hoon Nah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The ways people remember and recall places reveal an invisible aspect of cultural heritage (CH), reflecting how individuals and communities relate to these places. Heritage is communal, emerging through collaboratively constructed narratives rather than individual records. To probe how people may share collective memories, we designed an immersive two-person workflow for collaboratively co-designing 3D artifacts and environments in virtual heritage locations, using Generative AI (GenAI) to instantiate these intangible memories. Observations of the co-creation process revealed that participants merged prompts and model placements when negotiating different perspectives. They used spatial operations to compose scenes, and also to express personal and embodied experiences of CH. When GenAI failed to meet their needs, participants engaged in creative appropriation, re-purposing unsatisfactory generated objects as sources of design inspiration to further shared narratives. While GenAI may have a homogenizing effect on CH expression, this work shows how people may overcome limitations in immersive collaborative workflows.

---


### 185. [Attention-Gated Convolutional Networks for Scanner-Agnostic Quality Assessment](https://arxiv.org/abs/2604.15059)

**<font color=#1a73e8>作者：</font>** Chinmay Bakhale, Anil Sao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion artifacts present a significant challenge in structural MRI (sMRI), often compromising clinical diagnostics and large-scale automated analysis. While manual quality control (QC) remains the gold standard, it is increasingly unscalable for massive longitudinal studies. To address this, we propose a hybrid CNN-Attention framework designed for robust, site-invariant MRI quality assessment. Our architecture integrates a hierarchical 2D CNN encoder for local spatial feature extraction with a multi-head cross-attention mechanism to model global dependencies. This synergy enables the model to prioritize motion relevant artifact signatures, such as ringing and blurring, while dynamically filtering out site-specific intensity variations and background noise. The framework was trained end-to-end on the MR-ART dataset using a balanced cohort of 200 subjects. Performance was evaluated across two tiers: Seen Site Evaluation on a held-out MR-ART partition and Unseen Site Evaluation using 200 subjects from 17 heterogeneous sites in the ABIDE archive. On seen sites, the model achieved a scan-level accuracy of 0.9920 and an F1-score of 0.9919. Crucially, it maintained strong generalization across unseen ABIDE sites (Acc = 0.755) without any retraining or fine-tuning, demonstrating high resilience to domain shift. These results indicate that attention-based feature re-weighting successfully captures universal artifact descriptors, bridging the performance gap between diverse imaging environments and scanner manufacturers.

---


### 186. [No More Guessing: a Verifiable Gradient Inversion Attack in Federated Learning](https://arxiv.org/abs/2604.15063)

**<font color=#1a73e8>作者：</font>** Francesco Diana, Chuan Xu, André Nusser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient inversion attacks threaten client privacy in federated learning by reconstructing training samples from clients' shared gradients. Gradients aggregate contributions from multiple records and existing attacks may fail to disentangle them, yielding incorrect reconstructions with no intrinsic way to certify success. In vision and language, attackers may fall back on human inspection to judge reconstruction plausibility, but this is far less feasible for numerical tabular records, fueling the impression that tabular data is less vulnerable.
We challenge this perception by proposing a verifiable gradient inversion attack (VGIA) that provides an explicit certificate of correctness for reconstructed samples. Our method adopts a geometric view of ReLU leakage: the activation boundary of a fully connected layer defines a hyperplane in input space. VGIA introduces an algebraic, subspace-based verification test that detects when a hyperplane-delimited region contains exactly one record. Once isolation is certified, VGIA recovers the corresponding feature vector analytically and reconstructs the target via a lightweight optimization step.
Experiments on tabular benchmarks with large batch sizes demonstrate exact record and target recovery in regimes where existing state-of-the-art attacks either fail or cannot assess reconstruction fidelity. Compared to prior geometric approaches, VGIA allocates hyperplane queries more effectively, yielding faster reconstructions with fewer attack rounds.

---


### 187. [Learning Where to Embed: Noise-Aware Positional Embedding for Query Retrieval in Small-Object Detection](https://arxiv.org/abs/2604.15065)

**<font color=#1a73e8>作者：</font>** Yangchen Zeng, Zhenyu Yu, Dongming Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer-based detectors have advanced small-object detection, but they often remain inefficient and vulnerable to background-induced query noise, which motivates deep decoders to refine low-quality queries. We present HELP (Heatmap-guided Embedding Learning Paradigm), a noise-aware positional-semantic fusion framework that studies where to embed positional information by selectively preserving positional encodings in foreground-salient regions while suppressing background clutter. Within HELP, we introduce Heatmap-guided Positional Embedding (HPE) as the core embedding mechanism and visualize it with a heatbar for interpretable diagnosis and fine-tuning. HPE is integrated into both the encoder and decoder: it guides noise-suppressed feature encoding by injecting heatmap-aware positional encoding, and it enables high-quality query retrieval by filtering background-dominant embeddings via a gradient-based mask filter before decoding. To address feature sparsity in complex small targets, we integrate Linear-Snake Convolution to enrich retrieval-relevant representations. The gradient-based heatmap supervision is used during training only, incurring no additional gradient computation at inference. As a result, our design reduces decoder layers from eight to three and achieves a 59.4% parameter reduction (66.3M vs. 163M) while maintaining consistent accuracy gains under a reduced compute budget across benchmarks. Code Repository: this https URL

---


### 188. [Beyond the Laplacian: Doubly Stochastic Matrices for Graph Neural Networks](https://arxiv.org/abs/2604.15069)

**<font color=#1a73e8>作者：</font>** Zhaobo Hu, Vincent Gauthier, Mehdi Naima  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) conventionally rely on standard Laplacian or adjacency matrices for structural message passing. In this work, we substitute the traditional Laplacian with a Doubly Stochastic graph Matrix (DSM), derived from the inverse of the modified Laplacian, to naturally encode continuous multi-hop proximity and strict local centrality. To overcome the intractable $O(n^3)$ complexity of exact matrix inversion, we first utilize a truncated Neumann series to scalably approximate the DSM, which serves as the foundation for our proposed DsmNet. Furthermore, because algebraic truncation inherently causes probability mass leakage, we introduce DsmNet-compensate. This variant features a mathematically rigorous Residual Mass Compensation mechanism that analytically re-injects the truncated tail mass into self-loops, strictly restoring row-stochasticity and structural dominance. Extensive theoretical and empirical analyses demonstrate that our decoupled architectures operate efficiently in $O(K|E|)$ time and effectively mitigate over-smoothing by bounding Dirichlet energy decay, providing robust empirical validation on homophilic benchmarks. Finally, we establish the theoretical boundaries of the DSM on heterophilic topologies and demonstrate its versatility as a continuous structural encoding for Graph Transformers.

---


### 189. [Emulation-based System-on-Chip Security Verification: Challenges and Opportunities](https://arxiv.org/abs/2604.15073)

**<font color=#1a73e8>作者：</font>** Tanvir Rahman, Shuvagata Saha, Ahmed Y. Alhurubi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Increasing system-on-chip (SoC) heterogeneity, deep hardware/software integration, and the proliferation of third-party intellectual property (IP) have brought security validation to the forefront of semiconductor design. While simulation and formal verification remain indispensable, they often struggle to expose vulnerabilities that emerge only under realistic execution conditions, long software-driven interactions, and adversarial stimuli. In this context, hardware emulation is emerging as an increasingly important pre-silicon verification technology because it enables higher-throughput execution of RTL designs under realistic hardware/software workloads while preserving sufficient fidelity for security-oriented analysis.
This paper presents a comprehensive survey and perspective on emulation-based security verification and validation. We organize the landscape of prior work across assertion-based security checking, coverage-driven exploration, adversarial testing, information-flow tracking, fault injection, and side-channel-oriented evaluation. We provide a structured view of emulation-enabled security verification workflows, including instrumentation, stimulus generation, runtime monitoring, and evidence-driven analysis. We also examine practical challenges related to observability, scalability, property specification, and the definition of security-oriented coverage metrics for emulation-based verification. Finally, we discuss emerging directions such as AI-assisted emulation, digital security twins, chiplet-scale security exploration, automated vulnerability assessment, and cloud-scale secure emulation. Overall, this paper positions emulation as a promising foundation for the next generation of pre-silicon hardware security assurance.

---


### 190. [Where are the Humans? A Scoping Review of Fairness in Multi-agent AI Systems](https://arxiv.org/abs/2604.15078)

**<font color=#1a73e8>作者：</font>** Simeon Allmendinger, Luca Deck, Lucas Mueller  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rapid advances in Generative AI are giving rise to increasingly sophisticated Multi-Agent AI (MAAI) systems. While AI fairness has been extensively studied in traditional predictive scenarios, its examination in MAAI remains nascent and fragmented. This scoping review critically synthesizes existing research on fairness in MAAI systems. Through a qualitative content analysis of 23 selected studies, we identify five archetypal approaches. Our findings reveal that fairness in MAAI systems is often addressed superficially, lacks robust normative foundations, and frequently overlooks the complex dynamics introduced by agent autonomy and system-level interactions. We argue that fairness must be embedded structurally throughout the development lifecycle of MAAI, rather than appended as a post-hoc consideration. Meaningful evaluation requires explicit human oversight, normative clarity, and a precise articulation of fairness objectives and beneficiaries. This review provides a foundation for advancing fairness research in MAAI systems by highlighting critical gaps, exposing prevailing limitations, and suggesting pathways.

---


### 191. [Building Extraction from Remote Sensing Imagery under Hazy and Low-light Conditions: Benchmark and Baseline](https://arxiv.org/abs/2604.15088)

**<font color=#1a73e8>作者：</font>** Feifei Sang, Wei Lu, Hongruixuan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building extraction from optical Remote Sensing (RS) imagery suffers from performance degradation under real-world hazy and low-light conditions. However, existing optical methods and benchmarks focus primarily on ideal clear-weather conditions. While SAR offers all-weather sensing, its side-looking geometry causes geometric distortions. To address these challenges, we introduce HaLoBuilding, the first optical benchmark specifically designed for building extraction under hazy and low-light conditions. By leveraging a same-scene multitemporal pairing strategy, we ensure pixel-level label alignment and high fidelity even under extreme degradation. Building upon this benchmark, we propose HaLoBuild-Net, a novel end-to-end framework for building extraction in adverse RS scenarios. At its core, we develop a Spatial-Frequency Focus Module (SFFM) to effectively mitigate meteorological interference on building features by coupling large receptive field attention with frequency-aware channel reweighting guided by stable low-frequency anchors. Additionally, a Global Multi-scale Guidance Module (GMGM) provides global semantic constraints to anchor building topologies, while a Mutual-Guided Fusion Module (MGFM) implements bidirectional semantic-spatial calibration to suppress shallow noise and sharpen weather-induced blurred boundaries. Extensive experiments demonstrate that HaLoBuild-Net significantly outperforms state-of-the-art methods and conventional cascaded restoration-segmentation paradigms on the HaLoBuilding dataset, while maintaining robust generalization on WHU, INRIA, and LoveDA datasets. The source code and datasets are publicly available at: this https URL.

---


### 192. [Beyond Independent Frames: Latent Attention Masked Autoencoders for Multi-View Echocardiography](https://arxiv.org/abs/2604.15096)

**<font color=#1a73e8>作者：</font>** Simon Böhi, Irene Cannistraci, Sergio Muñoz Gonzalez 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Echocardiography is a widely used modality for cardiac assessment due to its non-invasive and cost-effective nature, but the sparse and heterogeneous spatiotemporal views of the heart pose distinct challenges. Existing masked autoencoder (MAE) approaches typically process images or short clips independently, failing to capture the inherent multi-view structure required for coherent cardiac representation. We introduce Latent Attention Masked Autoencoder (LAMAE), a foundation model architecture tailored to the multi-view nature of medical imaging. LAMAE augments the standard MAE with a latent attention module that enables information exchange across frames and views directly in latent space. This allows the model to aggregate variable-length sequences and distinct views, reconstructing a holistic representation of cardiac function from partial observations. We pretrain LAMAE on MIMIC-IV-ECHO, a large-scale, uncurated dataset reflecting real-world clinical variability. To the best of our knowledge, we present the first results for predicting ICD-10 codes from MIMIC-IV-ECHO videos. Furthermore, we empirically demonstrate that representations learned from adult data transfer effectively to pediatric cohorts despite substantial anatomical differences. These results provide evidence that incorporating structural priors, such as multi-view attention, yields significantly more robust and transferable representations.

---


### 193. [HyperSpace: A Generalized Framework for Spatial Encoding in Hyperdimensional Representations](https://arxiv.org/abs/2604.15113)

**<font color=#1a73e8>作者：</font>** Shay Snyder, Andrew Capodieci, David Gorsich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vector Symbolic Architectures (VSAs) provide a well-defined algebraic framework for compositional representations in hyperdimensional spaces. We introduce HyperSpace, an open-source framework that decomposes VSA systems into modular operators for encoding, binding, bundling, similarity, cleanup, and regression. Using HyperSpace, we analyze and benchmark two representative VSA backends: Holographic Reduced Representations (HRR) and Fourier Holographic Reduced Representations (FHRR). Although FHRR provides lower theoretical complexity for individual operations, HyperSpaces modularity reveals that similarity and cleanup dominate runtime in spatial domains. As a result, HRR and FHRR exhibit comparable end-to-end performance. Differences in memory footprint introduce additional deployment trade-offs where HRR requires approximately half the memory of FHRR vectors. By enabling modular, system-level evaluation, HyperSpace reveals practical trade-offs in VSA pipelines that are not apparent from theoretical or operator-level comparisons alone.

---


### 194. [FedIDM: Achieving Fast and Stable Convergence in Byzantine Federated Learning through Iterative Distribution Matching](https://arxiv.org/abs/2604.15115)

**<font color=#1a73e8>作者：</font>** He Yang, Dongyi Lv, Wei Xi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most existing Byzantine-robust federated learning (FL) methods suffer from slow and unstable convergence. Moreover, when handling a substantial proportion of colluded malicious clients, achieving robustness typically entails compromising model utility. To address these issues, this work introduces FedIDM, which employs distribution matching to construct trustworthy condensed data for identifying and filtering abnormal clients. FedIDM consists of two main components: (1) attack-tolerant condensed data generation, and (2) robust aggregation with negative contribution-based rejection. These components exclude local updates that (1) deviate from the update direction derived from condensed data, or (2) cause a significant loss on the condensed dataset. Comprehensive evaluations on three benchmark datasets demonstrate that FedIDM achieves fast and stable convergence while maintaining acceptable model utility, under multiple state-of-the-art Byzantine attacks involving a large number of malicious clients.

---


### 195. [NFTDELTA: Detecting Permission Control Vulnerabilities in NFT Contracts through Multi-View Learning](https://arxiv.org/abs/2604.15118)

**<font color=#1a73e8>作者：</font>** Hailu Kuang, Xiaoqi Li, Wenkai Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Permission control vulnerabilities in Non-fungible token (NFT) contracts can result in significant financial losses, as attackers may exploit these weaknesses to gain unauthorized access or circumvent critical permission checks. In this paper, we propose NFTDELTA, a framework that leverages static analysis and multi-view learning to detect permission control vulnerabilities in NFT contracts. Specifically, we extract comprehensive function Control Flow Graph (CFG) information via two views: sequence features (representing execution paths) and graph features (capturing structural control flow). These two views are then integrated to create a unified code representation. We also define three specific categories of permission control vulnerabilities and employ a custom detector to identify defects through multi-view feature similarity analysis. Our evaluation of 795 popular NFT collections identified 241 confirmed permission control vulnerabilities, comprising 214 cases of Bypass Auth Reentrancy, 15 of Weak Auth Validation, and 12 of Loose Permission Management. Manual verification demonstrates the detector's high reliability, achieving an average precision of 97.92% and an F1-score of 81.09%. Furthermore, NFTDELTA demonstrates enhanced efficiency and scalability, proving its effectiveness in securing NFT ecosystems.

---


### 196. [SRMU: Relevance-Gated Updates for Streaming Hyperdimensional Memories](https://arxiv.org/abs/2604.15121)

**<font color=#1a73e8>作者：</font>** Shay Snyder, Andrew Capodieci, David Gorsich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sequential associative memories (SAMs) are difficult to build and maintain in real-world streaming environments, where observations arrive incrementally over time, have imbalanced sampling, and non-stationary temporal dynamics. Vector Symbolic Architectures (VSAs) provide a biologically-inspired framework for building SAMs. Entities and attributes are encoded as quasi-orthogonal hyperdimensional vectors and processed with well defined algebraic operations. Despite this rich framework, most VSA systems rely on simple additive updates, where repeated observations reinforce existing information even when no new information is introduced. In non-stationary environments, this leads to the persistence of stale information after the underlying system changes. In this work, we introduce the Sequential Relevance Memory Unit (SRMU), a domain- and cleanup-agnostic update rule for VSA-based SAMs. The SRMU combines temporal decay with a relevance gating mechanism. Unlike prior approaches that solely rely on cleanup, the SRMU regulates memory formation by filtering redundant, conflicting, and stale information before storage. We evaluate the SRMU on streaming state-tracking tasks that isolate non-uniform sampling and non-stationary temporal dynamics. Our results show that the SRMU increases memory similarity by $12.6\%$ and reduces cumulative memory magnitude by $53.5\%$. This shows that the SRMU produces more stable memory growth and stronger alignment with the ground-truth state.

---


### 197. [How to Correctly Make Mistakes: A Framework for Constructing and Benchmarking Mistake Aware Egocentric Procedural Videos](https://arxiv.org/abs/2604.15134)

**<font color=#1a73e8>作者：</font>** Olga Loginova, Frank Keller  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable procedural monitoring in video requires exposure to naturally occurring human errors and the recoveries that follow. In egocentric recordings, mistakes are often partially occluded by hands and revealed through subtle object state changes, while existing procedural datasets provide limited and inconsistent mistake and correction traces. We present PIE-V (Psychologically Inspired Error injection for Videos), a framework for constructing and benchmarking mistake-aware egocentric procedural videos by augmenting clean keystep procedures with controlled, human-plausible deviations. PIE-V combines a psychology-informed error planner conditioned on procedure phase and semantic step load, a correction planner that models recovery behavior, an LLM writer that performs cascade-consistent rewrites, and an LLM judge that validates procedural coherence and repairs failures. For video segment edits, PIE-V synthesizes replacement clips with text-guided video generation and stitches them into the episode to preserve visual plausibility. Applied to 17 tasks and 50 Ego-Exo4D scenarios, PIE-V injects 102 mistakes and generates 27 recovery corrections. For benchmarking, we introduce a unified taxonomy and a human rubric with nine metrics that cover step-level and procedure-level quality, including plausibility, procedure logic with annotator confidence, state change coherence, and grounding between text and video. Using this protocol, we audit several existing resources and compare PIE-V against a freeform LLM generation baseline under the same criteria. Together, the framework and rubric support post-completion verification for egocentric procedural mistake detection and correction.

---


### 198. [KVNN: Learnable Multi-Kernel Volterra Neural Networks](https://arxiv.org/abs/2604.15141)

**<font color=#1a73e8>作者：</font>** Haoyu Yun, Hamid Krim, Yufang Bao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Higher-order learning is fundamentally rooted in exploiting compositional features. It clearly hinges on enriching the representation by more elaborate interactions of the data which, in turn, tends to increase the model complexity of conventional large-scale deep learning models. In this paper, a kernelized Volterra Neural Network (kVNN) is proposed. The key to the achieved efficiency lies in using a learnable multi-kernel representation, where different interaction orders are modeled by distinct polynomial-kernel components with compact, learnable centers, yielding an order-adaptive parameterization. Features are learned by the composition of layers, each of which consists of parallel branches of different polynomial orders, enabling kVNN filters to directly replace standard convolutional kernels within existing architectures. The theoretical results are substantiated by experiments on two representative tasks: video action recognition and image denoising. The results demonstrate favorable performance-efficiency trade-offs: kVNN consistently yields reduced model (parameters) and computational (GFLOPs) complexity with competitive and often improved performance. These results are maintained even when trained from scratch without large-scale pretraining. In summary, we substantiate that structured kernelized higher-order layers offer a practical path to balancing expressivity and computational cost in modern deep networks.

---


### 199. [An Axiomatic Benchmark for Evaluation of Scientific Novelty Metrics](https://arxiv.org/abs/2604.15145)

**<font color=#1a73e8>作者：</font>** Miri Liu, ChengXiang Zhai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rigorous evaluation of the novelty of a scientific paper is, even for human scientists, a challenging task. With the increasing interest in AI scientists and AI involvement in scientific idea generation and paper writing, it also becomes increasingly important that this task be automatable and reliable, lest both human attention and compute tokens be wasted on ideas that have already been explored. Due to the challenge of quantifying ground-truth novelty, however, existing novelty metrics for scientific papers generally validate their results against noisy, confounded signals such as citation counts or peer review scores. These proxies can conflate novelty with impact, quality, or reviewer preference, which in turn makes it harder to assess how well a given metric actually evaluates novelty. We therefore propose an axiomatic benchmark for scientific novelty metrics. We first define a set of axioms that a well-behaved novelty metric should satisfy, grounded in human scientific norms and practice, then evaluate existing metrics across ten tasks spanning three domains of AI research. Our results reveal that no existing metric satisfies all axioms consistently, and that metrics fail on systematically different axioms, reflecting their underlying architectures. Additionally, we show that combining metrics of complementary architectures leads to consistent improvements on the benchmark, with per-axiom weighting achieving 90.1% versus 71.5% for the best individual metric, suggesting that developing architecturally diverse metrics is a promising direction for future work. We release the benchmark code as supplementary material to encourage the development of more robust scientific literature novelty metrics.

---


### 200. [Fabricator or dynamic translator?](https://arxiv.org/abs/2604.15165)

**<font color=#1a73e8>作者：</font>** Lisa Vasileva, Karin Sim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are proving to be adept at machine translation although due to their generative nature they may at times overgenerate in various ways. These overgenerations are different from the neurobabble seen in NMT and range from LLM self-explanations, to risky confabulations, to appropriate explanations, where the LLM is able to act as a human translator would, enabling greater comprehension for the target audience. Detecting and determining the exact nature of the overgenerations is a challenging task. We detail different strategies we have explored for our work in a commercial setting, and present our results.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-234](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
