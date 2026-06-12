# 🧠 大模型相关研究 | 2026年06月13日

> 本类共 **128** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-128**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-128**

---

### 101. [Low-Latency Real-Time Audio Game Commentary System via LLM-Based Parallel Text Generation](https://arxiv.org/abs/2606.13322)

**<font color=#1a73e8>作者：</font>** Ryota Kawamatsu, Anum Afzal, Yuki Saito 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a low-latency real-time audio game commentary system that generates spoken commentary directly from live gameplay video. In this end-to-end setting, a key bottleneck is accumulated waiting time; conventional pipelines capture frames, generate text, and synthesize speech sequentially for each utterance, and do not request the next generation until speech playback has completed. This strict sequentiality causes long and unnatural silence between utterances. To address this latency bottleneck, our system runs text generation in parallel with speech playback and buffers multiple candidate utterances ahead of time, enabling immediate synthesis at playback boundaries. Experiments on fast-paced game videos show that our parallel design reduces the mean inter-utterance silence from 9.6 seconds to 0.3 seconds compared to sequential baselines. It also improves similarity to professional speaking--silence timing patterns by over 40 %, and a user study with 120 experienced game players confirms significantly improved perceived speaking rhythm. Our demo video is available at: this https URL.

---


### 102. [Dual-Domain Equivariant Generative Adversarial Network for Multimodal CT-PET Synthesis](https://arxiv.org/abs/2606.13341)

**<font color=#1a73e8>作者：</font>** Gabriel Steele, Alzahra Altalib, Alessandro Perelli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a Dual-Domain Equivariant Generative Adversarial Network (DDE-GAN) for multimodal CT-PET image synthesis. Traditional GAN-based approaches often operate solely in the spatial domain and ignore geometric consistency, resulting in limited structural fidelity. DDE-GAN addresses these challenges by jointly learning from both spatial and frequency (Fourier) domains, capturing complementary anatomical and spectral information. Furthermore, rotational equivariance embedded in the physics of the CT and PET measurements are integrated into the loss of both the generator and discriminator to ensure consistent responses under rotations, improving anatomical accuracy. A hierarchical dual-domain training strategy enforces intra- and inter-domain consistency through multi-stage loss functions. Evaluated on the HECKTOR 2022 CT-PET dataset, DDE-GAN achieves superior synthesis quality over baseline models for CT-PET image synthesis. The results demonstrate that combining dual-domain learning with geometric equivariance substantially enhances multimodal image synthesis accuracy and robustness, enabling practical applications in PET completion and data augmentation.

---


### 103. [From Passive Generation to Investigation: A Proactive Scientific Peer Review Agent](https://arxiv.org/abs/2606.13349)

**<font color=#1a73e8>作者：</font>** Haishuo Fang, Yue Feng, Iryna Gurevych  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown promise in automating scientific peer review. However, existing approaches often struggle to generate in-depth reviews supported by concrete evidence. We argue that a key limitation is the lack of flexibility to proactively investigate suspicious parts of a paper based on accumulated evidence, as human reviewers do. In this paper, we explore how to enable an LLM-based review agent to perform such proactive investigation. We find that this can be naturally formulated as a Markov Decision Process (MDP), and propose ProReviewer, a scientific peer review agent that proactively reviews a paper guided by a maintained, structured review log. The structured review log serves as a workspace for the agent to track evidence and intermediate findings collected during review. Experiments show that ProReviewer with an 8B backbone, trained by supervised fine-tuning and optimized by reinforcement learning, achieves the highest average score across five quality dimensions, outperforming prompt-based methods with much larger frontier LLMs by up to 39% and the strongest fine-tuned baseline by 16% relatively. It also attains the highest win rates against baselines in human evaluation.

---


### 104. [IterCAD: An Iterative Multimodal Agent for Visually-Grounded CAD Generation and Editing](https://arxiv.org/abs/2606.13368)

**<font color=#1a73e8>作者：</font>** Tao Hu, Jiaxin Ai, Licheng Wen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-Aided Design is pivotal in modern manufacturing, yet existing automated methods predominantly rely on open-loop, one-shot generation, creating a mismatch with iterative real-world practices. In this paper, we present IterCAD, a unified multimodal agent framework for closed-loop, interactive CAD generation and editing. We formulate the task as a multi-turn interaction between a multimodal agent and an executable CAD sandbox, covering three tasks: Drawing-to-Code, Text-to-Code, and Interactive Editing. To support this, we develop a data synthesis pipeline incorporating advanced industrial manufacturing features to generate standard-compliant multi-view engineering drawings, complex code-editing tasks, and high-fidelity interaction trajectories. We optimize the agent via progressive SFT followed by geometry-aware reinforcement learning with viable-prefix masking to enhance code executability and geometric fidelity. Finally, we introduce the IterCAD-Bench evaluation suite and propose the Chamfer Distance Tolerance-Recall (CD-TR) curve alongside its AUC-TR metric, establishing a survivor-bias-free standard that unifies code validity and geometric precision. Extensive experiments demonstrate that IterCAD achieves highly competitive performance across multiple benchmarks, significantly outperforming existing approaches in both code executability and geometric precision, while exhibiting superior capabilities in closed-loop iterative refinement.

---


### 105. [A Quantitative Experimental Repeated Measures Study of Training Dynamics in a Small Llama Style Language Model Under a Compute-Aware Token Budget](https://arxiv.org/abs/2606.13370)

**<font color=#1a73e8>作者：</font>** Joe Dwyer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study examines training dynamics in a small Llama-style language model trained under a fixed, compute-constrained token budget. Rather than evaluating efficiency solely through endpoint performance, the study uses a quantitative experimental repeated measures design to analyze how validation loss, validation perplexity, rolling volatility, backslide behavior, spike behavior, and between-seed variability change across token-based training intervals. Six independent training runs were conducted on a 4.26-million-parameter model using the TinyStories corpus, CPU-based full-precision training, and a target budget of approximately 20 million cumulative training tokens. Metrics were collected across 21 intervals, producing 126 seed-by-interval observations. Repeated measures ANOVA showed statistically significant interval effects for validation loss, validation perplexity, and rolling volatility. Descriptive trajectories revealed rapid early improvement followed by non-monotonic degradation during later training intervals. Mean validation loss decreased from 8.3552 at initialization to 2.7996 near 4 million tokens, but increased to 3.9010 by the final checkpoint. Validation perplexity followed the same pattern, falling sharply early in training before rising later. Derived telemetry further showed recurrent validation-loss backslides and no interval-summary evidence of a stable phase under the predefined criteria. These findings suggest that compute-aware language model evaluation should examine training trajectories rather than endpoint metrics alone. In constrained compute settings, additional token exposure may increase computational cost without producing proportional generalization gains, and interval-level telemetry can reveal instability, regression, and diminishing returns that final metrics may obscure.

---


### 106. [MoVerse: Real-Time Video World Modeling with Panoramic Gaussian Scaffold](https://arxiv.org/abs/2606.13376)

**<font color=#1a73e8>作者：</font>** Yang Zhou, Ziheng Wang, Yuqin Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present MoVerse, a real-time video world model that creates an interactively navigable scene from a single narrow-field-of-view image. This setting is challenging because the input observes only a small fraction of the environment, while interactive roaming requires a complete surrounding world, persistent geometry, controllable camera motion, and temporally coherent high-fidelity observations. MoVerse addresses this problem by separating world construction from observation rendering. It first expands the input into a gravity-aligned 360$^\circ$ panorama with topology-aware diffusion, closing the missing field of view before 3D reasoning. It then lifts the panorama into a persistent 3D Gaussian scaffold using panoramic geometry-aware residual prediction, yielding a dense and directly renderable spatial memory. Finally, a Gaussian-conditioned video renderer translates scaffold renderings along user-specified camera trajectories into photorealistic video. To make this renderer practical for interaction, we train a bidirectional diffusion teacher for high-quality conditional rendering and distill it into a causal autoregressive student for bounded-latency streaming. This design combines the controllability and long-range consistency of explicit 3D representations with the perceptual quality of generative video models. MoVerse supports real-time scene roaming at 8~FPS on a single NVIDIA RTX~4090 GPU, demonstrating a practical path toward single-image world creation with interactive video output.

---


### 107. [Hölder++: Improving the Quality-Coherence Trade-off in Multimodal VAEs](https://arxiv.org/abs/2606.13381)

**<font color=#1a73e8>作者：</font>** Huyen Vo, María Martínez-García, Isabel Valera  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing approaches for multimodal variational autoencoders (VAEs) face a trade-off between generative quality and coherence-i.e., they struggle to generate realistic and diverse samples that, at the same time, are semantically consistent across modalities. A recent work shows that using a simple approximation to Hölder pooling as an aggregation method improves coherence over the SOTA MMVAE+, despite assuming a single shared representation across all modalities. Yet, it slightly compromises sample diversity. Inspired by this insight, we propose Hölder++, a novel multimodal VAE that improves the generative quality-coherence trade-off through: (i) the first implementation of Hölder pooling without any approximation for multimodal VAEs; (ii) an extended architecture that models distinct shared and private (i.e., modality-specific) representations (Hölder+); and (iii) hierarchical inference that further enhances the disentanglement between the shared and private representations (Hölder++). Our experiments corroborate that Hölder++ consistently improves the generative quality-coherence trade-off, yields more structured latent spaces, and learns shared representations that are informative for downstream tasks.

---


### 108. [MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392)

**<font color=#1a73e8>作者：</font>** Xunhao Lai, Weiqi Xu, Yufeng Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ultra-long-context capability is becoming indispensable for frontier LLMs: agentic workflows, repository-scale code reasoning, and persistent memory all require the model to jointly attend over hundreds of thousands to millions of tokens, yet the quadratic cost of softmax attention makes this untenable at deployment scale. We introduce MiniMax Sparse Attention (MSA), a blockwise sparse attention built upon Grouped Query Attention (GQA). A lightweight Index Branch scores key-value blocks and independently selects a Top-k subset for each GQA group, enabling group-specific sparse retrieval while maintaining efficient block-level execution; the Main Branch then performs exact block-sparse attention over only the selected blocks. Designed around a principle of simplicity and scalability, MSA is deliberately streamlined, making it straightforward to deploy efficiently across a broad range of GPUs. To translate sparsity into practical speedups, we co-design MSA with a GPU execution path that uses exp-free Top-k selection and KV-outer sparse attention to improve tensor-core utilization under block-granular access. On a 109B-parameter model with native multimodal training, MSA performs on par with GQA while reducing per-token attention compute by 28.4x at 1M context. Paired with our co-designed kernel, MSA achieves 14.2x prefill and 7.6x decoding wall-clock speedups on H800. Our inference kernel is available at: this https URL. A production-grade natively multimodal model powered by MSA has been publicly released at: this https URL.

---


### 109. [Mod-Guide: An LLM-based Content Moderation Feedback System to Address Insensitive Speech toward Indigenous Ethnic and Religious Minority Communities](https://arxiv.org/abs/2606.13397)

**<font color=#1a73e8>作者：</font>** Dipto Das, Achhiya Sultana, Ankit Singh Chauhan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Language operates as a mechanism of both marginalization and resistance, especially for minority communities navigating insensitive and harmful speech online. As content moderation increasingly depends on large language models (LLMs), concerns arise about whether these systems can recognize culturally insensitive speech-language that disregards or marginalizes the cultural and religious perspectives of historically underrepresented communities, often through implicit erasure, misrepresentation, or normative framing, rather than overt hostility. Focusing on Bangladesh's Hindu and Chakma communities -- the country's largest religious and Indigenous ethnic minorities, respectively -- this paper investigates the epistemic limits of LLM-based moderation systems and explores methods for incorporating minority perspectives. We co-created a culturally grounded corpus of insensitive speech with community members and integrated their narratives into moderation pipelines using retrieval augmented generation (RAG). Our tool, Mod-Guide, improves LLM sensitivity to minority viewpoints by leveraging contextual cues derived from lived experience. Through mixed-method evaluations involving both minority and majority participants, we demonstrate that RAG-enhanced moderation responses are more contextually accurate and perceived differently across ethnic lines. This work advances research in human-computer interaction, AI ethics, and social computing by foregrounding restorative justice and hermeneutical inclusion in the design of content moderation systems.

---


### 110. [Why Sampling Is Not Choosing: Intentionality, Agency, and Moral Responsibility in Large Language Models](https://arxiv.org/abs/2606.13441)

**<font color=#1a73e8>作者：</font>** Joseph Keshet  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have prompted claims that such systems exhibit agency or qualify as moral agents. This paper argues that these attributions are misguided. We maintain that moral responsibility requires commitment-bearing agency grounded in intrinsic intentionality and self-attributed action, and that such agency constitutes the form of free will relevant to responsibility. Although LLMs generate coherent and normatively evaluable outputs, their operation is fully characterized by probabilistic input-output mappings learned from data. Their apparent intentionality is derived rather than intrinsic, and their outputs are neither owned as commitments nor guided by reasons. Variability introduced by stochastic sampling does not amount to choice or authorship. We address objections from the intentional stance, functionalism, compatibilism, and the presence of moral reasoning in model outputs, arguing that none suffice to establish genuine agency.

---


### 111. [VISA: VLM-Guided Instance Semantic Auditing for 3D Occupancy World Models](https://arxiv.org/abs/2606.13460)

**<font color=#1a73e8>作者：</font>** Ruiqi Xian, Yuehan Xian, Jing Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic 3D occupancy provides a voxelized world state for autonomous driving and robot decision making, but object and rare-class errors can affect free-space interpretation, collision checking, and temporal state propagation. We show that a common VLM strategy, aligning 3D voxel or object features with crop-caption embeddings, improves text-space similarity without reliably improving closed-set occupancy mIoU. Motivated by this mismatch, we propose VISA, a training-time semantic auditing approach for existing occupancy world models. VISA queries an offline VLM on a representative crop of each physical object instance, obtains a structured audit with class hypotheses, plausible confusions, reliability, attributes, and evidence, and propagates it along the object track. The audit is grounded to matched 3D object voxels and distilled into semantic logits through reliability-weighted taxonomy, attribute-factor, and scene-level audit graph losses, while inference remains unchanged and requires no VLM. On nuScenes, averaged across three runs, VISA improves OccWorld from 19.06 to 20.05 mIoU and GaussianWorld from 21.36 to 21.91 mIoU; on GaussianWorld, object mIoU improves from 18.18 to 19.16 and rare-class mIoU from 15.60 to 16.79. These results suggest that VLMs are better suited to closed-set occupancy as reliability-aware semantic auditors than as generic caption-embedding targets.

---


### 112. [Leveraging Audio-LLMs to Filter Speech-to-Speech Training Data](https://arxiv.org/abs/2606.13507)

**<font color=#1a73e8>作者：</font>** Qixu Chen, Satoshi Nakamura  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale mined corpora provide abundant training data for end-to-end speech-to-speech translation (S2ST) but may contain noise, misalignment, and semantic errors. Filtering noisy data is crucial to maintain robust speech translation performance. We study how to train an audio-language model to make keep/drop decisions on paired speech directly from audio. To obtain reliable supervision without manual labels, we adopt a scalable two-stage Rank-to-Distill strategy. A lightweight ranker generates keep/drop pseudo-labels from noisy speech pairs, then trains an audio large language model to predict keep/drop directly from raw paired speech. The resulting model jointly captures acoustic fidelity and cross-lingual semantic consistency for the selection of speech-conditioned data. Experiments on CVSS-C and SpeechMatrix show consistent improvements over unfiltered training, yielding up to +1.4 ASR-BLEU for end-to-end S2ST.

---


### 113. [Uncertainty-Aware Hybrid Retrieval for Long-Document RAG](https://arxiv.org/abs/2606.13550)

**<font color=#1a73e8>作者：</font>** Hoin Jung, Xiaoqian Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval augmented generation (RAG) depends critically on the quality and granularity of retrieved evidence. Large retrieval units preserve context but often introduce irrelevant content, which can dilute answer bearing evidence and worsen long context utilization. Fine-grained units are more compact, but they may be difficult to retrieve reliably because short chunks can lack semantic, lexical, or bridging cues needed to match the query. We propose Uncertainty-aware Multi-Granularity RAG (UMG-RAG), a training-free hybrid retrieval framework that treats chunk granularity as query-specific reliability estimation. Instead of training a new retriever or modifying the generator, UMG-RAG uses existing dense and sparse retrievers as complementary experts across multiple chunk granularities. For each query, it converts each expert-granularity score list into an evidence distribution, estimates reliability from distribution entropy, and fuses candidates according to query-specific semantic, lexical, and granularity confidence. We further introduce UMGP-RAG, a parent promotion variant that uses fine-grained hits to locate relevant evidence while returning broader non-redundant parent chunks for local coherence. Experiments on question answering benchmarks show that uncertainty-aware fusion and parent promotion improve generation quality while maintaining a lightweight, plug-and-play retrieval pipeline.

---


### 114. [A2D2: Fine-Tuning Any-Length Discrete Diffusion for Adaptive Decoding](https://arxiv.org/abs/2606.13565)

**<font color=#1a73e8>作者：</font>** Sophia Tang, Yuchen Zhu, Molei Tao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models offer a simple and stable likelihood-based framework for sequence generation, recently extended to any-length settings via token insertion. Principled reward-guided fine-tuning for any-length discrete diffusion, however, remains largely unexplored. We introduce Fine-Tuning Any-Length Discrete Diffusion for Adaptive Decoding (A2D2), a unified framework for reward-guided fine-tuning of any-length discrete diffusion models via joint optimization of the insertion and unmasking policies together with a quality-based inference schedule. We derive the Radon-Nikodym derivative for the joint insertion-unmasking path measures, enabling theoretically guaranteed convergence to the intractable reward-tilted sequence distribution without requiring target samples. Building on this, we establish unmasking and insertion quality as tractable approaches for minimizing decoding error and introduce the Adaptive Joint Decoding (AJD) loss, which provably yields the optimal path measure that generates the reward-tilted distribution. Empirically, A2D2 improves reward optimization while enhancing generation flexibility and accuracy over prior fixed-length fine-tuning and inference-time guidance methods.

---


### 115. [ArogyaSutra: A Multi-Agent Framework for Multimodal Medical Reasoning in Indic Languages](https://arxiv.org/abs/2606.13572)

**<font color=#1a73e8>作者：</font>** Tanmoy Kanti Halder, Akash Ghosh, Subhadip Baidya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have shown promising reasoning capabilities in general domains, yet their performance remains limited in specialized settings such as healthcare, especially in multilingual and low-resource scenarios. This gap is critical in regions like rural India, where patients often express complex medical queries in native Indic languages and rely on multimodal inputs such as medical images. Existing English-centric MLLMs struggle to support such use cases, limiting equitable access to AI-driven healthcare assistance. To address this challenge, we introduce ArogyaBodha, a large-scale multilingual multimodal medical question-answer dataset constructed from eight heterogeneous sources, covering 31 body systems, six imaging modalities, and 21 clinical domains across English and seven major Indian languages. We further propose ArogyaSutra, an actor-critic-based multi-agent framework that integrates tool grounding with dual-memory mechanisms for step-wise, reasoning-aware decision making, and uses stored actor-critic simulation trajectories for distillation. Experiments show that our dataset and framework improve multilingual medical reasoning accuracy across all Indic languages, with ablations validating the contribution of each component. The source code and dataset are available at: this https URL ArogyaSutra/

---


### 116. [Reward Modeling for Multi-Agent Orchestration](https://arxiv.org/abs/2606.13598)

**<font color=#1a73e8>作者：</font>** King Yeung Tsang, Zihao Zhao, Vishal Venkataramani 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Systems (MAS) built on Large Language Models (LLMs) require effective orchestration to coordinate specialized agents, yet training such orchestrators is hindered by limited supervision and high computational cost. We propose Orchestration Reward Modeling (OrchRM), a self-supervised framework for evaluating orchestration quality without human annotations. OrchRM leverages intermediate artifacts from multi-agent executions to construct win-lose pairs for Bradley-Terry reward model training. Unlike existing MAS test-time scaling and orchestrator training frameworks that rely on costly sub-agent rollouts, OrchRM operates directly at the orchestration level, enabling efficient and high-performing reward-guided orchestrator training and MAS test-time scaling. OrchRM improves training efficiency by up to 10x in token usage while improving MAS test-time scaling performance by up to 8% in accuracy. These gains consistently transfer across multiple domains, including mathematical reasoning, web-based question answering, and multi-hop reasoning, demonstrating orchestration-level reward modeling as a scalable direction for robust multi-agent orchestration. Code will be available at this https URL.

---


### 117. [Beyond the Commitment Boundary: Probing Epiphenomenal Chain-of-Thought in Large Reasoning Models](https://arxiv.org/abs/2606.13603)

**<font color=#1a73e8>作者：</font>** Daniel Scalena, Sara Candussio, Luca Bortolussi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning is the dominant paradigm for inference-time scaling in language models, yet the causal influence of individual steps on the final answer poorly understood. We estimate each step's causal importance via early exit and use this measure to study how answers form across the reasoning traces of several model families. Across diverse tasks, we find that reasoning typically crosses a \emph{commitment boundary} -- a sharp transition from transient intermediate guesses to a stable, high-confidence answer. This transition often happens in a single step, well before the model's reasoning block ends, and is followed by \emph{epiphenomenal} CoT steps that leave the final answer probability unaltered. Using attention probes, we show that answer-formation stages can be linearly decoded from intermediate reasoning steps with high accuracy and generalize robustly to unseen reasoning tasks. We exploit this signal to early-exit reasoning blocks at the commitment boundary, reducing the length of CoTs up to 55\% on average with negligible impact on model performance.

---


### 118. [Reasoning as Pattern Matching: Shared Mechanisms in Human and LLM Everyday Reasoning](https://arxiv.org/abs/2606.13607)

**<font color=#1a73e8>作者：</font>** Zach Studdiford, Gary Lupyan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When large language models (LLMs) fail to generalize or make haphazard errors in reasoning, it is often taken as evidence that LLMs are not truly reasoning, but rather performing a kind of pattern matching. The implication is that people's behavior does not exhibit the same types of failures because human reasoning uses principled and abstract world models. We evaluate human participants and 25 LLMs on their ability to engage in common-sense reasoning about a variety of everyday situations and observe similar patterns of errors in both people and models. We then identify the set of attention heads driving LLM responses and find that these heads implement a form of pattern-matching. These attention heads allow us to predict seemingly inexplicable reasoning errors in people caused by ostensibly irrelevant prompt details. Taken together, our results suggest that everyday causal reasoning in people and LLMs is more consistent with a form of pattern-matching than with abstract world models.

---


### 119. [Beyond Uniform Tokens: Adaptive Compression for Time Series Language Models](https://arxiv.org/abs/2606.13624)

**<font color=#1a73e8>作者：</font>** Jialin Gan, Xin Qiu, Guangzhe Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have enabled time series (TS) analysis by jointly modeling numerical observations and textual context through a shared token interface. However, TS tokens and prompt tokens exhibit fundamentally different information structures, making uniform token processing inefficient. In this paper, we study token efficiency in TS language modeling from an asymmetric-token perspective. We show that TS tokens have highly uneven spectral contributions, where many tokens share redundant frequency patterns while a small subset preserves critical temporal evidence. We also observe that prompt-token influence attenuates with model depth, suggesting that full prompt retention across all layers is unnecessary. Based on these findings, we develop an adaptive token budgeting framework that compresses TS tokens via frequency-domain structure and progressively reduces prompt tokens across layers. Experiments across forecasting, classification, imputation, and anomaly detection demonstrate up to \textit{\textbf{7.68$\times$}} inference acceleration and performance gains in \textit{\textbf{78\%}} of evaluated settings, showing the effectiveness of asymmetric token compression for scalable TS foundation models.

---


### 120. [Operads for compositional reasoning in LLMs](https://arxiv.org/abs/2606.13634)

**<font color=#1a73e8>作者：</font>** Nathaniel Bottman, Kyle Richardson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Question decomposition, i.e. breaking a complex query into simpler sub-queries whose answers are composed to produce a final answer, is a widely used strategy for improving LLM reasoning, yet it currently lacks a rigorous mathematical foundation. In this paper, we propose operads, mathematical structures that model many-in, one-out operations and compositions thereof, as a natural framework for describing question decomposition. We define the questions operad $Q$, in which operations correspond to question templates and composition corresponds to substitution of sub-answers, and show how QA models can be interpreted as algebras over $Q$. Beyond reframing existing practice, this operadic perspective points toward new methods, in particular a notion of operadic consistency, which measures whether a QA model's answers agree across the partial collapses of a question decomposition tree. Empirical evaluation of operadic consistency is reported in our companion paper (Bottman, Liu, and Richardson, 2026), which finds it strongly correlated with accuracy across twelve LLMs and four multi-hop QA datasets and outperforming standard temperature-based self-consistency baselines. We argue that operads are the natural mathematical home for question decomposition, and that invariants such as operadic consistency open new directions for analyzing and improving the reliability of multi-step reasoning.

---


### 121. [Operadic consistency: a label-free signal for compositional reasoning failures in LLMs](https://arxiv.org/abs/2606.13649)

**<font color=#1a73e8>作者：</font>** Nathaniel Bottman, Yinhong Liu, Kyle Richardson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting LLM reasoning failures at inference time without ground-truth labels has motivated a wide range of confidence baselines, including self-consistency, semantic entropy, and P(True), built on within-question sampling and self-evaluation. Operad theory, the formalism for systems built by iterated substitution, suggests a complementary diagnostic: a model's direct answer to a compositional query should agree with the answer it produces by composing a stated decomposition of the same query. We instantiate this idea as operadic consistency (OC), a per-question signal. Across twelve instruction-tuned LLMs (4B to 671B parameters, open-weights and closed-source) on four multi-hop QA datasets, OC is strongly correlated with accuracy on every dataset (Pearson $r \in [0.86, 0.94]$, all $p \leq 0.0004$), and is the only signal we evaluate with $r \geq 0.85$ uniformly across all four datasets. Chain-of-thought self-consistency (CoT-SC; Wang et al., 2023) matches OC on HotpotQA and DROP ($r = 0.93, 0.87$) but drops to $r \approx 0.45$ on MuSiQue and StrategyQA. At the per-question level, OC contributes information beyond CoT-SC and semantic entropy on every dataset (cluster-robust $p \leq 10^{-16}$ for the OC coefficient), and the conclusion is robust to additionally controlling for constructed decomposition-aware baselines ($p \leq 10^{-13}$). The same signal yields selective-prediction improvements (accuracy at fixed coverage) over a tuned CoT-SC baseline at the equal-cost $K = 3$ budget (AUARC lifts of +0.086 to +0.096 and AUROC lifts of +0.092 to +0.164; 95% CIs exclude zero on every cell). On five frontier thinking models, where the decomposition is extracted from the model's own chain of thought, the same equal-cost comparison gives positive selective-prediction point-estimate lift on all 16 (dataset, budget, metric) cells tested, with 95% CIs excluding zero on 12 of the 16.

---


### 122. [HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents](https://arxiv.org/abs/2606.13663)

**<font color=#1a73e8>作者：</font>** Yaxin Du, Yifan Zhou, Yujie Ge 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-augmented LLM agents commonly rely on step-wise atomic tool calls, where each invocation, observation, and value transfer is exposed in the main reasoning trace. This creates an \emph{execution-granularity mismatch}: locally deterministic tool workflows are unfolded into repeated model-visible decisions, consuming context and forcing the model to manage low-level dataflow in the trace. We introduce \textbf{HyperTool}, a unified executable MCP-style tool interface that changes the model-visible unit of tool execution. A model invokes HyperTool with a code block that can call existing tools through their original schemas, manipulate returned values, and pass intermediate results locally, folding deterministic tool subroutines into a single outer call. To train models to use this interface, we synthesize HyperTool-format trajectories from cross-tool compositional tasks and verify them in real MCP environments. On MCP-Universe, HyperTool improves average accuracy from 15.69\% to 35.29\% on Qwen3-32B and from 9.93\% to 33.33\% on Qwen3-8B, and surpass GPT-OSS and Kimi-k2.5 on average accuracy, showing that our HyperTool can substantially improve multi-step tool use.

---


### 123. [Influcoder: Distilling Decoders' Gradient Influence Rankings into an Encoder for Data Attribution](https://arxiv.org/abs/2606.13668)

**<font color=#1a73e8>作者：</font>** Dimitri Kachler, Damien Sileo, Pascal Denis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the growth of LLMs' (Large Language Models) capabilities, there has been an increasing push to curate high quality datasets by filtering samples in the training data. In general, Data Attribution (DA) methods aim to estimate how individual samples in a training dataset can precondition a model to generate certain outputs. As an example, one might be interested in which samples in the data could be the source of toxic behavior after training the LLM. Many methods quantify this conditioning through the paradigm of influence functions. While methods of this family are effective in its function, they lack the necessary processing speed and storage compactness to be practically implemented on large datasets. We propose a method, Influcoder, as a quick and cost-effective approach to influence-based Data Attribution at scale.

---


### 124. [Automated reproducibility assessments in the social and behavioral sciences using large language models](https://arxiv.org/abs/2606.13670)

**<font color=#1a73e8>作者：</font>** Tobias Holtdirk, Pietro Marcolongo, Anna Steinberg Schulten 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reproducibility in the social and behavioral sciences is typically evaluated by independent researchers who reanalyze the original data to assess whether the published findings can be recovered. However, such approaches are resource-intensive and difficult to scale. Here, we show that large language models (LLMs) can automate reproducibility assessments. Using N=76 published studies with predefined claims from the behavioral and social sciences, we compare LLM-generated analysis with the original findings and human reanalysis. For 7 studies, the LLM could not produce a viable effect size estimate. For the remaining studies, our LLM pipeline recovered the original effect sizes in 41% of studies using a +/-0.05 tolerance in Cohen's d. Further, our LLM pipeline reached the same qualitative conclusion as the original study in 96% of cases, where conclusions indicate whether the reanalysis supports the original claim. For comparison, human reanalysts recovered the original effect sizes in 34% of studies and reached the same qualitative conclusion in 74% of cases. Together, these results show that LLMs can serve as a scalable tool for automated reproducibility assessment and provide a foundation for systematic auditing of empirical results in the social and behavioral sciences.

---


### 125. [SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning](https://arxiv.org/abs/2606.13673)

**<font color=#1a73e8>作者：</font>** Seokju Cho, Ryo Hachiuma, Abhishek Badki 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning, the ability to determine where objects are, how they relate, and how they move in 3D, remains a fundamental challenge for vision-language models (VLMs). Tool-augmented agents attempt to address this by augmenting VLMs with specialist perception modules, yet their effectiveness is bounded by the action interface through which those tools are invoked. In this work, we study how the design of this interface shapes the agent's capacity for open-ended spatial reasoning. Existing spatial agents either employ single-pass code execution, which commits to a full analysis strategy before any intermediate result is observed, or rely on a structured tool-call interface that often offers less flexibility for freely composing operations or tailoring the analysis to each task. Both designs offer limited flexibility for open-ended, complex 3D/4D spatial reasoning. We therefore propose SpatialClaw, a training-free framework for spatial reasoning that adopts code as the action interface. SpatialClaw maintains a stateful Python kernel pre-loaded with input frames and a suite of perception and geometry primitives, letting a VLM-backed agent write one executable cell per step conditioned on all prior outputs, enabling the agent to flexibly compose and manipulate perception results and adapt its analysis to both intermediate text and visual observations and the demands of each problem. Evaluated across 20 spatial reasoning benchmarks spanning a broad range of static and dynamic 3D/4D spatial reasoning tasks, SpatialClaw achieves 59.9% average accuracy, outperforming the recent spatial agent by +11.2 points, with consistent gains across six VLM backbones from two model families without any benchmark- or model-specific adaptation.

---


### 126. [InterleaveThinker: Reinforcing Agentic Interleaved Generation](https://arxiv.org/abs/2606.13679)

**<font color=#1a73e8>作者：</font>** Dian Zheng, Harry Lee, Manyuan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent image generators have demonstrated impressive photorealism and instruction-following capabilities in single-image generation and editing. However, constrained by their architectures, they cannot achieve interleaved generation (text-image sequence), which has crucial applications in visual narratives, guidance, and embodied manipulation. Even the latest open-source Unified Multimodal Models (UMMs) exhibit limited performance in this regard. In this paper, we introduce InterleaveThinker, the first multi-agent pipeline designed to endow any existing image generator with interleaved generation capabilities. Specifically, we employ a planner agent to organize the image-text input sequence, instructing the image generator on the required execution at each step. Subsequently, we introduce a critic agent to evaluate the generator's outputs, identify samples that deviate from the planned instructions, and refine the instructions for regeneration. To implement this pipeline, we construct the Interleave-Planner-SFT-80k and Interleave-Critic-SFT-112k to perform a format cold-start. Then we develop Interleave-Critic-RL-13k to reinforce the step-wise instruction correction capability within a generation trajectory using GRPO. Since a single interleaved generation trajectory may involve over 25 generator calls, optimizing the entire trajectory is computationally impractical. Therefore, we propose accuracy reward and step-wise reward, allowing single-step RL to effectively guide the entire generation trajectory. The results show that InterleaveThinker improves performance across various image generators. On interleaved generation benchmarks, it achieves performance comparable to Nano Banana and GPT-5. Surprisingly, it also significantly enhances the base model on reasoning-based benchmarks; for example, on 4-step FLUX.2-klein, we observe substantial gains on WISE and RISE.

---


### 127. [Learning to Reason by Analogy via Retrieval-Augmented Reinforcement Fine-Tuning](https://arxiv.org/abs/2606.13680)

**<font color=#1a73e8>作者：</font>** Zilin Xiao, Qi Ma, Chun-cheng Jason Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) has become a standard mechanism for grounding language models in external knowledge, yet conventional retrieval based on lexical or semantic similarity is poorly suited for complex reasoning tasks: a semantically similar problem may demand an entirely different solution strategy, while a superficially different problem may share the same underlying reasoning pattern. We propose Retrieval-Augmented Reinforcement Fine-Tuning (RA-RFT), a post-training framework that teaches language models to reason by analogy. RA-RFT uses gold-relevance distillation to train a retriever that ranks contexts by expected reasoning benefit rather than semantic overlap, and then fine-tunes the policy model via reinforcement fine-tuning methods with retrieved analogous demonstrations, so the model learns to leverage reasoning traces under verifiable outcome rewards. We further analyze the diversity of retrieved contexts and find that reasoning-aware retrieval surfaces complementary solution strategies that provide distinct reasoning scaffolds for individual problems. Across challenging mathematical reasoning benchmarks, RA-RFT consistently outperforms standard reinforcement fine-tuning methods. For example, it improves AIME 2025 average@32 accuracy by 7.1 and 2.8 points over GRPO for Qwen3-1.7B and Qwen3-4B respectively -- suggesting that reasoning-aware retrieval is a complementary axis of improvement and orthogonal to advances in reward design or training curricula.

---


### 128. [EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments](https://arxiv.org/abs/2606.13681)

**<font color=#1a73e8>作者：</font>** Jundong Xu, Qingchuan Li, Jiaying Wu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have achieved strong performance on a wide range of benchmarks, yet most evaluations assume static environments. In contrast, real-world deployment is inherently dynamic, requiring agents to continually align their knowledge, skills, and behavior with changing environments and updated task conditions. To address this gap, we introduce EvoArena, a benchmark suite that models environment changes as sequences of progressive updates across terminal, software, and social domains. We further propose EvoMem, a patch-based memory paradigm that records memory evolution as structured update histories, enabling agents to reason about environmental evolution through changes in their memory. Experiments show that current agents struggle on EvoArena, achieving an average accuracy of 39.6% across evolving terminal, software, and social-preference domains. EvoMem consistently improves performance, yielding an average gain of 1.5% on EvoArena and also improving standard benchmarks such as GAIA and LoCoMo by 6.1% and 4.8%. Beyond individual tasks, EvoMem further improves chain-level accuracy by 3.7% on EvoArena, where success requires completing a consecutive sequence of related evolutionary subtasks. Mechanistic analysis shows that EvoMem improves evidence capture in the memory, indicating better preservation of complete evolving environment states. Our results highlight the importance of modeling evolution in both evaluation and memory for reliable agent deployment.

---


> [!TIP]
> 当前位于：**101-128**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-128**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
