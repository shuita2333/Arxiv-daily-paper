# 🧠 大模型相关研究 | 2026年05月22日

> 本类共 **143** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-143**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-143**

---

### 101. [Cross-lingual robustness of LLM-brain alignment and its computational roots](https://arxiv.org/abs/2605.21049)

**<font color=#1a73e8>作者：</font>** Ni Yang, Rui He, Philipp Homan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) reliably predict neural activity during language comprehension and transformer depth has been interpreted as mirroring hierarchical cortical organization. However, it remains unclear whether such alignment extends to subcortical regions, overlaps spatially across languages, and what the computational roots of such alignment are. Here, we used a multilingual, whole-brain encoding framework to examine brain-LLM alignment across three typologically distinct languages: Mandarin, English, and French during naturalistic story listening. Our results show that across languages, transformer-based models predicted activity in a distributed landscape spanning widely distributed cortical functional networks like limbic, ventral attention, default mode network, and subcortical structures. Spatial alignment patterns showed substantial cross-linguistic overlap and remained largely stable across model layers, with limited layer progression consistent with functional cortical hierarchies. Contrary to previous evidence, contextual embeddings did not outperform static embeddings. To test candidate computational explanations, we examined whether layer-wise brain scores reflect surprisal and intrinsic dimensionality, and thereby predictive processing and information compression. Neither of these two computational metrics mirrored neural alignment profiles. Our findings suggest that brain-LLM alignment is spatially robust and cross-linguistically stable but not explainable from predictive uncertainty or representational geometry. Rather than directly reflecting shared hierarchical computation, neural predictivity may primarily arise from distributed lexical-semantic correspondences that generalize across languages.

---


### 102. [Multimodal LLMs under Pairwise Modalities](https://arxiv.org/abs/2605.21059)

**<font color=#1a73e8>作者：</font>** Yan Li, Yunlong Deng, Yuewen Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the impressive results achieved by multimodal large language models (MLLMs), their training typically relies on jointly curated multimodal data, requiring substantial human effort to construct multi-way aligned datasets and thereby limiting scalability across domains. In this work, we explore training MLLMs by only leveraging multiple paired modalities as a surrogate for the full joint multimodal distribution. Specifically, we first provide a theoretical analysis of the conditions under which the representations are identifiable with only observing pairwise modalities. Building on this analysis, we propose a representation learning framework for aligning latent representations across modalities using only pairwise data. The framework consists of two stages: latent representation alignment and cross-modal recomposition. Specifically, in the first stage, we learn the shared latent space across modalities by both self-modal reconstruction and pair-wise contrastive learning. We also incorporate an inductive bias in the contrastive learning process by partially aligning and minimal latent specification. In stage two, we integrate the encoder of newly introduced modalities with the decoders of the pre-trained modalities to facilitate cross-modal transfer and generation. We evaluate our method by newly adding 3D point clouds and tactile modalities into pre-trained MLLMs with three modality pairs and show that, by learning an aligned latent representation space, our model achieves strong cross-modal performance.

---


### 103. [APM: Evaluating Style Personalization in LLMs with Arbitrary Preference Mappings](https://arxiv.org/abs/2605.21063)

**<font color=#1a73e8>作者：</font>** Philipp Spohn, Leander Girrbach, Zeynep Akata  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Typical LLM responses tend to follow a default style, even though users often have distinct preferences regarding tone, verbosity, and formality that they do not explicitly state in their prompts. Evaluating whether personalization methods can adapt to these implicit preferences is challenging, since users typically provide prompts rather than reference responses, style preferences are not factually verifiable, and reference-free LLM judges may conflate personalization with general response quality. To address these challenges, we introduce the Arbitrary Preference Mapping (APM) benchmark, which decouples user attributes (e.g. enthusiastic) from response principles (e.g. persuasive) via a hidden, randomized mapping $\mathbf{C}$ that maps user attributes to preferences about response traits. Because $\mathbf{C}$ carries no semantic content and is resampled across runs, models cannot exploit stereotypical associations and must infer preferences from conversation history. Using this unbiased evaluation methodology, we adapt retrieval-augmented, prompt-optimization, and routing personalization methods and evaluate them on Llama-3.1-8B and Qwen-3.5-27B. Our results show that routing is the most reliable approach, while RAG only improves with the stronger base LLM, and soft prompt optimization fails to improve significantly over a non-personalized baseline. Our extensive evaluation reveals that in this realistic setting, personalization remains challenging, but our adapted methods show promise.

---


### 104. [Fine-grained Claim-level RAG Benchmark for Law](https://arxiv.org/abs/2605.21071)

**<font color=#1a73e8>作者：</font>** Souvick Das, Sallam Abualhaija, Domenico Bianculli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid progress of large language models (LLMs) is shifting semantic search toward a question-answering paradigm, where users ask questions and LLMs generate responses. In high-stake domains such as law, retrieval-augmented generation (RAG) is commonly used to mitigate hallucinations in generated responses. Nonetheless, prior work shows that RAG systems, whether general-purpose or legal-specific, still hallucinate at varying rates, making fine-grained evaluation essential. Despite the need, existing evaluation frameworks for legal RAG systems lack the granularity required to provide detailed analysis of retrieval and generation performance separately. Moreover, current benchmarks are largely English-only and centered on legal expert queries, overlooking non-expert needs. We introduce ClaimRAG-LAW, a comprehensive dataset for legal RAG that supports French and English, targets both experts and non-experts, and includes diverse question types reflecting realistic scenarios. We further apply a fine-grained evaluation framework of state-of-the-art legal RAG systems, revealing limitations in retrieval, generation, and claim-level analysis in the legal domain.

---


### 105. [SpectralEarth-FM: Bringing Hyperspectral Imagery into Multimodal Earth Observation Pretraining](https://arxiv.org/abs/2605.21075)

**<font color=#1a73e8>作者：</font>** Nassim Ait Ali Braham, Aaron Banze, Conrad M. Albrecht 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth observation (EO) foundation models (FMs) are increasingly trained on multisensor data, spanning multispectral imagery (MSI), synthetic aperture radar (SAR), and derived geospatial layers, but hyperspectral imagery (HSI) remains underrepresented. Conversely, existing hyperspectral FMs are trained on HSI alone, leaving joint pretraining and fusion of HSI with co-located EO sensors unexplored. We introduce SpectralEarth-FM, a hierarchical transformer for multisensor EO input with heterogeneous spectral dimensionality. The architecture combines spectral tokenization for hyperspectral inputs, sensor-specific encoders, a cross-sensor fusion module, and a shared hierarchical encoder, enabling joint processing of HSI and lower-channel observations. To pretrain SpectralEarth-FM, we curate SpectralEarth-MM, a dataset that co-locates HSI from three spaceborne sensors (EnMAP, EMIT, DESIS) with Sentinel-2, Landsat-8/9 optical imagery, Landsat land surface temperature (LST), and Sentinel-1 SAR, over common geographic footprints. It comprises approximately 2M globally distributed locations, 25M georeferenced patches, and over 40TB of data. Pretraining uses a Joint-Embedding Predictive Architecture (JEPA)-style objective that matches representations between global views and single-sensor local views from the same location. We evaluate SpectralEarth-FM on hyperspectral downstream tasks and standard EO benchmarks following the PANGAEA protocol, achieving state-of-the-art results across both evaluation settings.

---


### 106. [AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions](https://arxiv.org/abs/2605.21082)

**<font color=#1a73e8>作者：</font>** Minghao Chen, Xinyi Hu, Zhou Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) based agents have demonstrated proficiency in multi-step interactions with graphical user interfaces (GUIs). While most research focuses on improving single-task performance, practical scenarios often involve repetitive GUI tasks for which invoking LLM reasoning repeatedly, i.e., the ReAct paradigm, is inefficient. Prior to LLMs, traditional Robotic Process Automation (RPA) offers runtime efficiency but demands significant manual effort to develop and maintain. To bridge this gap, we propose AutoRPA, a framework that automatically distills the decision logic of ReAct-style agents into robust RPA functions. AutoRPA introduces two core innovations: (1) A translator-builder pipeline, where a translator agent converts hard-coded ReAct actions into soft-coded procedures, and a builder agent synthesizes robust RPA functions via retrieval-augmented generation over multiple trajectories; (2) A hybrid repair strategy during code verification, combining RPA execution with ReAct-based fallback for iterative refinement. Experiments across multiple GUI environments demonstrate that RPA functions generated by AutoRPA successfully solve similar tasks while reducing token usage by 82% to 96%, significantly improving runtime efficiency and reusability.

---


### 107. [TextSculptor: Training and Benchmarking Scene Text Editing](https://arxiv.org/abs/2605.21090)

**<font color=#1a73e8>作者：</font>** Yiheng Lin, Siyu Jiao, Xiaohan Lan 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Multimodal Large Language Models (MLLMs) and diffusion-based generative models have substantially improved prompt-driven image editing. However, scene text editing remains challenging, as it requires models to precisely modify textual content while preserving visual realism and non-target regions. Current open-source models still lag behind proprietary systems, largely due to the scarcity of high-quality training data and the lack of standardized benchmarks tailored to text editing. To address these challenges, we present TextSculptor, a comprehensive framework for data construction and evaluation of scene text editing. We first develop an automated data construction pipeline that combines text-aware image synthesis with programmatic text rendering and compositing. Based on this pipeline, we build TextSculpt-Data, a large-scale dataset containing 3.2M training samples, including 1.2M OCR-verified text-to-image samples and 2M paired text editing samples with naturally aligned source-target images and strong background consistency. We further introduce TextSculpt-Bench, a benchmark covering four fundamental text editing tasks: text addition, text replacement, text removal, and hybrid editing. To support reliable evaluation, we design a tailored protocol that measures text accuracy, visual quality, and background preservation through OCR-based text alignment, multimodal judgment, and background-region similarity. Extensive experiments show that TextSculptor improves open-source text editing performance and narrows the gap to proprietary models. The data and benchmark are available at this https URL.

---


### 108. [WCXB: A Multi-Type Web Content Extraction Benchmark](https://arxiv.org/abs/2605.21097)

**<font color=#1a73e8>作者：</font>** Murrough Foley  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web content extraction - isolating a page's main content from surrounding boilerplate - is a prerequisite for search indexing, retrieval-augmented generation, NLP dataset construction, and large language model training. Progress in this area has been constrained by the limitations of existing evaluation benchmarks, which are small (100-800 pages), restricted to news articles, or based on web pages from over a decade ago. We introduce the Web Content Extraction Benchmark (WCXB), a dataset of 2,008 web pages from 1,613 domains spanning seven structurally distinct page types: articles, forums, products, collections, listings, documentation, and service pages. The dataset includes a 1,497-page development set and a 511-page held-out test set with matched page type distributions. Ground truth annotations were produced through a five-stage pipeline: LLM-assisted drafting, automated verification, four-pass frontier model review, snippet and quality verification scripts, and human review. We evaluate 13 extraction systems - 11 heuristic and 2 neural - and find that while top systems converge on articles (F1 = 0.93), performance diverges sharply on structured page types (F1 = 0.41-0.84), revealing blind spots invisible to existing article-only benchmarks. The dataset is released under CC-BY-4.0 with HTML source files, ground truth annotations, page type labels, and baseline results.

---


### 109. [ACL-Verbatim: hallucination-free question answering for research](https://arxiv.org/abs/2605.21102)

**<font color=#1a73e8>作者：</font>** Gábor Recski, Szilveszter Tóth, Nadia Verdha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Academic researchers need efficient and reliable methods for collecting high-quality information from trusted sources, but modern tools for AI-assisted research still suffer from the tendency of Large Language Models (LLMs) to produce factually inaccurate or nonsensical output, commonly referred to as hallucinations. We apply the extractive question answering system VerbatimRAG to research papers in the ACL Anthology, directly mapping user queries to verbatim text spans in retrieved documents. We contribute a novel ground truth dataset for the task of mapping user queries to relevant text spans in research papers, and use it to train and evaluate a variety of extractive models. Human annotation is performed by NLP researchers and is based on synthetic user queries generated using a custom pipeline based on the ScIRGen methodology, paired with chunks of research papers retrieved by VerbatimRAG. On this benchmark, a 150M-parameter ModernBERT token classifier trained on silver supervision from our pipeline achieves the best word-level F1 (53.6), ahead of the strongest evaluated LLM extractor (48.7).

---


### 110. [Reasoning-Trace Collapse: Evaluating the Loss of Explicit Reasoning During Fine-Tuning](https://arxiv.org/abs/2605.21127)

**<font color=#1a73e8>作者：</font>** Lukas Twist, Helen Yannakoudakis, Jie M. Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explicit reasoning models are trained to produce intermediate reasoning traces before final answers, but downstream fine-tuning is often performed on ordinary instruction-response data that contains no such traces. We show that this mismatch can induce reasoning-trace collapse: a fine-tuned model continues to produce plausible final answers while losing the structurally valid explicit reasoning traces that made it a reasoning model in the first place. We introduce a structural evaluation framework that separates answer correctness from reasoning-trace validity, measuring valid, empty, missing, and truncated reasoning alongside reasoning-conditioned task performance. Using this framework, we study four open-weight reasoning models and find that standard supervised fine-tuning can rapidly suppress valid reasoning traces, and that answer-only metrics can substantially obscure this failure: in several settings, performance conditional on valid reasoning remains high while the rate of valid reasoning falls sharply. We further show that simple loss-masking strategies can substantially mitigate collapse without requiring teacher-generated reasoning traces. These results suggest that evaluations of fine-tuned reasoning models should report structural reasoning reliability metrics in addition to final-answer performance, especially when adaptation data does not contain explicit reasoning traces.

---


### 111. [SMoA: Spectrum Modulation Adapter for Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2605.21147)

**<font color=#1a73e8>作者：</font>** Yongkang Liu, Xing Li, Mengjie Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As the number of model parameters increases, parameter-efficient fine-tuning (PEFT) has become the go-to choice for tailoring pre-trained large language models. Low-rank Adaptation (LoRA) uses a low-rank update method to simulate full parameter fine-tuning, which is widely used to reduce resource requirements. However, decreasing the rank encounters challenges with limited representational capacity. Theory suggests that LoRA fine-tuning with rank r converges toward the top r singular values of the pre-trained weight matrix. As the rank increases, more principal singular directions are preserved, which generally improves the model's performance. However, a larger rank also introduces more trainable parameters, leading to higher computational cost. To overcome this dilemma, we propose SMoA, a \textbf{S}pectrum \textbf{Mo}dulation \textbf{A}dapter that enlarges the accessible family of spectrum-aware updates under a smaller parameter budget. SMoA partitions the layer into multiple aligned spectral blocks and applies one in-block Hadamard-modulated low-rank branch to each diagonal block, yielding broader coverage of pretrained spectral directions. We provide theoretical analysis and empirical results on multiple tasks. In our experiments, SMoA improves average performance in the current lower-budget setting over LoRA and competitive LoRA-style baselines.

---


### 112. [Automated ICD Classification of Psychiatric Diagnoses: From Classical NLP to Large Language Models](https://arxiv.org/abs/2605.21154)

**<font color=#1a73e8>作者：</font>** Fernando Ortega, Raúl Lara-Cabrera, Jorge Dueñas-Lerín 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mental health has become a global priority, leading to a massive administrative burden in the coding of clinical diagnoses. This study proposes the automation of psychiatric diagnostic analysis by mapping free-text descriptions to the International Classification of Diseases (ICD) using Natural Language Processing (NLP) and Machine Learning (ML) techniques. Utilizing a specialized dataset of 145,513 Spanish psychiatric descriptions, various text representation paradigms were evaluated, ranging from classical frequency-based models (BoW, TF-IDF) to state-of-the-art Large Language Models (LLMs) such as e5\_large, BioLORD, and Llama-3-8B. Results indicate that transformer-based embeddings consistently outperform traditional methods by capturing implicit semantic cues and nuanced medical terminology. The e5\_large model, through end-to-end fine-tuning, achieved the highest performance with a $F1_{micro}$ score of 0.866. This research demonstrates that adapting LLMs to specific clinical nomenclature is essential for overcoming the challenges of ``long-tail'' label distributions and the inherent ambiguity of psychiatric discourse.

---


### 113. [Learning First Integrals via Backward-Generated Data and Guided Reinforcement Learning](https://arxiv.org/abs/2605.21160)

**<font color=#1a73e8>作者：</font>** Jingfeng Zhong, Zhengxiang Liu, Zhijie Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The discovery of first integrals is of fundamental scientific importance for understanding conservation laws in dynamical systems. However, existing symbolic computation tools and Large Language Models (LLMs) remain limited on this task because high-quality training data are scarce and successful solutions often depend on mathematical intuition. This paper presents FISolver, an LLM-based solver developed to address this challenge. First, we introduce a "Backward Generation" algorithm that systematically builds large-scale datasets of (differential equation, first integral) pairs by deriving differential equations from sampled integrals, thereby alleviating the data scarcity bottleneck. Second, we apply supervised fine-tuning to a compact mathematical model and further improve its performance through reinforcement learning with a Levenshtein Distance-based shaped reward. In addition, we design data synthesis and blending strategies that support effective adaptation to difficult problem families from sparse examples. Experiments show that FISolver, while requiring substantially lower computational cost, significantly outperforms larger mathematical LLMs and commercial solvers such as Mathematica on challenging benchmarks, indicating a new data-driven route for automated discovery of first integrals.

---


### 114. [ChunkFT: Byte-Streamed Optimization for Memory-Efficient Full Fine-Tuning](https://arxiv.org/abs/2605.21177)

**<font color=#1a73e8>作者：</font>** Yongkang Liu, Zijing Wang, Mengjie Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work presents \textsc{ChunkFT}, a memory-efficient fine-tuning framework that reformulates full-parameter fine-tuning around a dynamically activated working set. \textsc{ChunkFT} enables gradient computation for arbitrary sub-tensors without modifying the network architecture, providing an algorithmic foundation for optimizing arbitrary sub-networks while avoiding standard dense gradient computation. We provide a theoretical convergence analysis of \textsc{ChunkFT} in the deterministic setting. Empirically, we apply \textsc{ChunkFT} to fine-tune Llama 3-8B and Llama 3-70B using a single RTX 4090-24GB GPU and 2$\times$ H800-80GB GPUs, respectively. Full-parameter fine-tuning of a 7B model with a 1K input length requires only 13.72GB of GPU memory. The results demonstrate the effectiveness of \textsc{ChunkFT} in memory usage, running time, and optimization quality. Moreover, downstream evaluations on language understanding, mathematical reasoning, and MT-Bench show that \textsc{ChunkFT} consistently outperforms existing memory-efficient baselines. Notably, \textsc{ChunkFT} achieves performance comparable to, and in some cases exceeding, full-parameter fine-tuning. Our repository is on this https URL.

---


### 115. [RankE: End-to-End Post-Training for Discrete Text-to-Image Generation with Decoder Co-Evolution](https://arxiv.org/abs/2605.21195)

**<font color=#1a73e8>作者：</font>** Siyong Jian, Siyuan Li, Luyuan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Discrete autoregressive (AR) text-to-image (T2I) models pair a VQ tokenizer with an AR policy, and current post-training pipelines optimize only the policy while keeping the VQ decoder frozen. Recent diffusion T2I work, exemplified by REPA-E, has shown that the VAE itself constitutes a key alignment bottleneck, yet no analogous investigation exists for discrete AR models. We show that policy-only optimization induces Latent Covariate Shift: as the policy evolves, the resulting token distribution diverges from the ground-truth distribution on which the decoder was trained, such that reward scores improve while decoded image quality degrades. To address this mismatch, we propose RankE, the first end-to-end post-training framework for discrete T2I generation. Rather than optimizing the policy against a fixed decoder, RankE co-evolves both components through alternating optimization: each module maximizes a ranking-based alignment objective while being regularized by a stability-preserving anchor suited to its parameter space. This co-evolution breaks the fidelity--alignment trade-off that plagues frozen-decoder approaches: on LlamaGen-XL (775M), standard RL improves CLIP but degrades FID, whereas RankE improves both simultaneously (FID 15.21, CLIP 33.76 on MS-COCO 30K). Consistent gains on Janus-Pro (1B) confirm that decoder co-evolution reliably converts reward optimization into pixel-space quality improvements.

---


### 116. [PREFINE: Preference-Based Implicit Reward and Cost Fine-Tuning for Safety Alignment](https://arxiv.org/abs/2605.21225)

**<font color=#1a73e8>作者：</font>** Richa Verma, Bavish Kulur, Sanjay Chawla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address the problem of making a pre-trained reinforcement learning (RL) policy safety-aware by incorporating cost constraints without retraining it from scratch. While costs could be numerically encoded, we assume a more general setting is when costs are provided as preferences. Given a reward-optimized policy and a small dataset of preferred (low-cost) and dispreferred (high-cost) trajectories, our goal is to fine-tune the policy to generate low-cost behaviors while retaining high rewards. Unlike standard RLHF in language models, where preferences are defined over responses to the same prompt, our setting involves trajectory-level preferences in continuous control environments. We introduce PREFINE: Preference-based Implicit Reward and Cost Fine-Tuning for Safety Alignment which is a preference-based fine-tuning method that adapts Direct Preference Optimization (DPO), which is now widely used for LLM fine-tuning, to the sequential decision making setting. PREFINE constructs policy-sampled counterfactual trajectories to establish meaningful preference contrasts and jointly optimizes for reward retention and safety alignment. Empirically, PREFINE reduces constraint violations and catastrophic failures by over 60% while maintaining original reward behavior. PREFINE produces policies that achieve low-cost, high-reward performance with significantly improved data and computational efficiency compared to full offline RL or imitation learning, bridging preference alignment and safe policy adaptation in continuous domains.

---


### 117. [Do LLMs Know What Luxembourgish Borrows? Probing Lexical Neology in Low-Resource Multilingual Models](https://arxiv.org/abs/2605.21227)

**<font color=#1a73e8>作者：</font>** Nina Hosseini-Kivanani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for writing assistance in small contact languages, yet it is unclear whether they respect community norms around lexical borrowing and neology. We introduce LexNeo-Bench, a 3{,}050-instance token-level benchmark derived from LuxBorrow, a large-scale Luxembourgish news corpus, where target tokens are labelled as native or as French, German, or English borrowings. Using this benchmark, we probe three multilingual LLMs across 34 prompt settings on two tasks: borrowing type classification and a binary lexical-innovation proxy (borrowing versus native). Without external context, models perform only slightly above chance on borrowing classification, so we construct a linguistic knowledge graph that encodes donor language, morphological patterns, and lexical analogues, and inject instance-specific subgraphs into the prompt. Knowledge-graph prompts raise borrowing classification accuracy from 25 -- 35\% up to 71 -- 81\% and largely close the gap between small and large models, while leaving neology detection difficult and sensitive to few-shot design. Our results show that lexicon-aware prompting is highly beneficial for robust borrowing judgments in low-resource contact languages and that lexical resources can serve as structured context for LLM evaluation. This study was carried out within the ENEOLI COST Action and examines borrowing as a form of lexical innovation in multilingual Luxembourgish data.

---


### 118. [LamPO: A Lambda Style Policy Optimization for Reasoning Language Models](https://arxiv.org/abs/2605.21235)

**<font color=#1a73e8>作者：</font>** Zhe Yuan, Yipeng Zhou, Jinghan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become an effective paradigm for improving reasoning language models on tasks such as mathematics, coding, and scientific question answering. However, widely used group-relative objectives, such as GRPO, summarize each sampled group with scalar statistics and therefore discard fine-grained relational information among candidate responses. This weakens credit assignment under sparse outcome rewards, especially when multiple generated solutions differ only subtly in reasoning quality. We propose \textbf{LamPO}, a \textbf{Lambda-Style Policy Optimization} method that replaces scalar group advantages with a \emph{Pairwise Decomposed Advantage}. LamPO aggregates pairwise reward gaps within each response group and modulates each comparison by a confidence-aware weight computed from sequence log-probability differences, while retaining the critic-free and clipped-update structure of PPO-style optimization. When reference solutions are available, we further add a lightweight ROUGE-L-based dense auxiliary reward to reduce reward sparsity. Experiments on AIME24, AIME25, MATH-500, and GPQA-Diamond with Qwen3-1.7B, Qwen3-4B, and Phi-4-mini show that LamPO consistently improves over GRPO and recent RLVR variants, with more stable training dynamics and better sample efficiency.

---


### 119. [APEX: Autonomous Policy Exploration for Self-Evolving LLM Agents](https://arxiv.org/abs/2605.21240)

**<font color=#1a73e8>作者：</font>** Yibo Li, Jiashuo Yang, Zhi Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents have shown strong performance across a wide range of complex tasks, including interactive environments that require long-horizon decision making. But these agents cannot learn on the fly at test time. Self-evolving agents address this by accumulating memory and reflection across episodes rather than requiring model-weight updates. However, these agents often suffer from exploration collapse: as memory grows, behavior concentrates around familiar high-reward routines, reducing the chance of discovering better alternatives. To address this problem, we propose Autonomous Policy EXploration (APEX), which builds and maintains an explicit strategy space through a strategy map-a directed acyclic graph of milestones with prerequisite dependency edges. In APEX, Fork Discovery expands the map with evidence-grounded unexplored directions, while Policy Selection balances exploration and exploitation during planning. Evaluated on nine Jericho text-adventure games and WebArena, a realistic web interaction benchmark, APEX outperforms all baselines. Extensive ablations validate each component's contribution and demonstrate robustness across diverse settings, demonstrating APEX's effectiveness for sustained exploration in self-evolving agents.

---


### 120. [FedCoE: Bridging Generalization and Personalization via Federated Coordinated Dual-level MoEs](https://arxiv.org/abs/2605.21264)

**<font color=#1a73e8>作者：</font>** Penglin Dai, Fulian Li, Xincao Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) has emerged as a promising paradigm for privacy-preserving distributed learning. However, existing FL methods face a fundamental challenge. Traditional averaging-based approaches suffer from parameter divergence under non-IID conditions, while personalized FL methods overfit to local data and fail to generalize to new clients (cold-start problem). Mixture-of-Experts naturally addresses this by routing heterogeneous data to specialized experts rather than forcing uniform aggregation. In this paper, we propose FedCoE, a Federated Coordinated dual-level mixture-of-Experts framework that effectively balances global generalization with local personalization. FedCoE maintains multiple independent global expert models on the server and employs a shared gating network to dynamically model client-expert correlations during aggregation, effectively mitigating expert drift and gating inconsistency. To address the cold-start challenge, we introduce an adaptive mechanism that enables new clients to immediately leverage the global expert pool without extensive local training. Extensive experiments demonstrate that FedCoE achieves 78.00% global accuracy and 89.32% personalized accuracy on average, outperforming the baseline by 8.82% and 29.19%, respectively. In cold-start scenarios, FedCoE delivers 77.27% accuracy without any local fine-tuning, outperforming baselines by over 12.54%.

---


### 121. [How Much Online RL is Enough? Informative Rollouts for Offline Preference Optimization in RLVR](https://arxiv.org/abs/2605.21266)

**<font color=#1a73e8>作者：</font>** Richa Verma, Balaraman Ravindran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Verifiable Rewards (RLVR) has emerged as a powerful paradigm for reasoning in language models, with GRPO as its primary example. However, GRPO requires continuous online rollout generation, making it computationally expensive and difficult to scale. While Direct Preference Optimization (DPO) offers a stable and efficient offline alternative, it is typically expected to underperform w.r.t. online RL methods such as GRPO when trained on rollouts from a cold supervised fine-tuned (SFT) policy. We introduce G2D (GRPO to DPO)}, a three-stage pipeline that performs a short GRPO warm-up, constructs a static preference dataset, and fine-tunes a model offline with DPO. Across a set of values of the number of online steps (K) in GRPO on Qwen2.5-7B and Llama-3.1-8B, we find that offline DPO with moderate warm-up matches or outperforms GRPO at substantially lower compute cost in our setting. On Qwen2.5-7B, G2D at K=150 achieves 62.4% on MATH-500, outperforming GRPO (51.6%) by 10.8% at ~4x lower compute. On Llama-3.1-8B, G2D at K=500 achieves 49.4%, surpassing GRPO in our experimental setting. We show that performance is not governed by the number of preference pairs, which does not vary much w.r.t. K, but by their informativeness. Moderate warm-up produces rollouts with calibrated uncertainty, yielding stronger contrastive signal, while excessive warm-up leads to overconfident policies and less informative data. Our results recast the offline-online gap in RLVR as primarily a data informativeness problem, and identify short online RL warm-up with appropriate difficulty calibration of the fine-tuning dataset as a compute-efficient alternative to online RL.

---


### 122. [A Mechanistic Study of Tabular Foundation Models](https://arxiv.org/abs/2605.21288)

**<font color=#1a73e8>作者：</font>** Marin Biloš, James T. Wilson, Anderson Schneider 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models with different architectures converge in accuracy across a range of classification and regression tasks. This raises questions a leaderboard cannot answer: (i) whether the models execute the same in-context algorithm, (ii) where row, column, and class-permutation invariances originate, and (iii) how robust they are under perturbations engineered against the inferred mechanism. We characterize all three. The model families realize qualitatively distinct similarity-based readouts: from an attention-weighted vote over context labels to a class-conditional mean readout, each confirmed by causal intervention. We find that the representation collapse highlighted in prior work is not a practical concern for them. Each model's permutation invariances trace to specific positional parameters whose removal preserves accuracy and makes approximate invariance exact. Perturbations engineered against each readout reproduce predicted failure modes; hub and rank attacks isolate them from refit baselines. Together these results give a mechanistic account of contemporary tabular foundation models and identify which inductive biases govern both their accuracy and characteristic failures.

---


### 123. [TimeSRL: Generalizable Time-Series Behavioral Modeling via Semantic RL-Tuned LLMs -- A Case Study in Mental Health](https://arxiv.org/abs/2605.21295)

**<font color=#1a73e8>作者：</font>** Yuang Fan, Lilin Xu, Millie Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Longitudinal passive sensing enables continuous health prediction, yet models often fail under cross-dataset distribution shifts. Traditional ML overfits cohort-specific artifacts, while Large Language Models (LLMs) struggle to reason reliably over long, heterogeneous time-series. We introduce TimeSRL, a two-stage LLM framework that routes predictions through an explicit semantic bottleneck. The model first abstracts raw signals into high-level natural language, then predicts behavioral outcomes from these abstractions alone. This forces the model to reason over semantic concepts that we argue generalize better than raw numbers. We optimize this process end-to-end using Group Relative Policy Optimization (GRPO) with Reinforcement Learning from Verifiable Rewards (RLVR), learning outcome-aligned abstractions without gold intermediate annotations. Instantiated on mental-health prediction, TimeSRL achieves state-of-the-art performance on a benchmark designed to stress-test cross-cohort generalization under a rigorous leave-one-dataset-out (LOSO) protocol, reducing mean absolute error (MAE) over strong non-LLM ML and LLM baselines by 3.1--10.1% and 9.5--44.1% for anxiety, and 3.2--9.6% and 27.4--57.6% for depression (all $p$s<0.05). TimeSRL significantly outperforms prior methods in cross-benchmark transfer across different sensing pipelines, rivaling its own within-domain performance without target-domain fine-tuning. These results demonstrate that semantic abstractions are reusable and point to a new direction for generalizable behavior modeling via RL-tuned LLMs.

---


### 124. [Tracing the ongoing emergence of human-like reasoning in Large Language Models](https://arxiv.org/abs/2605.21299)

**<font color=#1a73e8>作者：</font>** Paolo Morosi, Nikoleta Pantelidou, Fritz Günther 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans effortlessly go beyond literal meanings: If you mow the lawn, I will give you fifty dollars, is typically understood as implying that the speaker will pay only if the lawn is mowed, whereas If you are hungry, there is pizza in the oven implies that pizza is available regardless of the hearers hunger. Large Language Models - LLMs - show human-like performance on many tasks, yet it remains unclear whether they reason like humans. To address this, we conducted a population-matching experiment assessing how twentyfive LLMs compute conditional inferences across four languages, compared to an equal number of humans per language. We find that humans enrich logical reasoning through pragmatic inferences across languages. Model behavior is more variable. Some LLMs perfectly follow the truth-table of conditionals but they ignore pragmatic inferences, while others deviate from the truth-table, adhering to a single interpretation across the board, thus reflecting accurate rule-based processing but not human-like reasoning. Overall, LLMs are accurate semantic operators, but fail to capture the pragmatic enrichments characteristic of human reasoning. Crucially, LLM accuracy is neither predicted nor boosted by open vs. closed status, training orientation, or architecture type, suggesting that pragmatic reasoning is still an emerging ability in the cognitive toolkit of artificial systems.

---


### 125. [Reducing Object Hallucination in LVLMs via Emphasizing Image-negative Tokens](https://arxiv.org/abs/2605.21300)

**<font color=#1a73e8>作者：</font>** Meng Shen, Minghao Wu, Deepu Rajan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object hallucination is a significant challenge that hinders the application of large vision-language models (LVLMs) in practice. We hypothesize that one possible origin of hallucination is the model's tendency to prioritize text generation over meaningful interaction with images. To explore this, we examine the generation process and categorize text tokens into three groups: image-positive, invariant, and negative, based on their visual dependence on input image tokens. Our analysis reveals that most generated tokens are minimally influenced by the image information. This suggests that during the model's training stage, more emphasis is placed on learning how to follow textual instructions, rather than extracting information from images. Based on this finding, we propose adjusting the training weights of different tokens depending on their visual dependence to control hallucination. Additionally, we remove a portion of the training data that potentially contains more hallucinations as a data filtering strategy. Both methods achieve a reduction in hallucination without compromising response length or introducing additional computational costs during inference. We validate our methods across three LVLM variants, demonstrating the effectiveness and general applicability.

---


### 126. [SymbolicLight V1: Spike-Gated Dual-Path Language Modeling with High Activation Sparsity and Sub-Billion-Scale Pre-Training Evidence](https://arxiv.org/abs/2605.21333)

**<font color=#1a73e8>作者：</font>** Ting Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natively trained spiking language models struggle to combine Transformer-like language quality, stable multi-domain pre-training, and high activation sparsity. We present SymbolicLight V1, a spike-gated dual-path language model that combines binary Leaky Integrate-and-Fire spike dynamics with a continuous residual stream. Its Dual-Path SparseTCAM module replaces dense self-attention with an exponential-decay aggregation path for long-range memory and a spike-gated local attention path for short-range precision, complemented by a dynamic context-conditioned decoding head and a bilingual tokenizer.
A 194M-parameter SymbolicLight V1 model trained from scratch on a 3B-token Chinese-English corpus reaches held-out validation PPL 8.88-8.93 across four independent runs at >89% per-element activation sparsity. It trails GPT-2 201M by 7.7% in PPL while surpassing GPT-2 124M under the reported comparison. Component ablations at matched 0.5B-token training budgets show that the spike-gated local attention path is the largest contributor, and that replacing LIF dynamics with a deterministic top-k mask at matched sparsity causes a larger degradation, indicating that temporal integration rather than sparsity alone drives performance. We also report a 0.8B-parameter scale-up run trained on 48.8B tokens as evidence of optimization and sparsity preservation, not as a primary quality comparison. Current dense-hardware inference is slower than GPT-2, so neuromorphic deployment is presented as a future sparsity-driven opportunity rather than an achieved hardware speedup.

---


### 127. [Text Analytics Evaluation Framework: A Case Study on LLMs and Social Media](https://arxiv.org/abs/2605.21338)

**<font color=#1a73e8>作者：</font>** Yuefeng Shi, Nedjma Ousidhoum, Jose Camacho-Collados  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs have demonstrated exceptional proficiency in a wide range of NLP tasks. However, a notable gap remains in practical data analysis scenarios, particularly when LLMs are required to process long sequences of unstructured documents, such as news feeds or, as specifically addressed in this paper, social media posts. To empirically assess the effectiveness of LLMs in this setting, we introduce a question-based evaluation framework comprising 470 manually curated questions designed to evaluate LLMs' semantic understanding and reasoning abilities over aggregated text data. We apply our benchmark on diverse Twitter datasets covering various NLP tasks, including sentiment analysis, hate speech detection, and emotion recognition. Our results reveal that the performance depends heavily on input scale and the complexity of the data sources, declining noticeably in multi-label or target-dependent scenarios. In addition, as task complexity increases, performance drops progressively from basic semantic existence identification to more demanding operations such as comparison, counting, and calculation. Furthermore, as the input size grows beyond 500 instances, we identify a common limitation across LLMs, particularly Open-weights models: performance degrades substantially, especially on numerical tasks. These findings highlight critical architectural bottlenecks in current LLMs for performing rigorous quantitative analysis over large text collections.

---


### 128. [Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents](https://arxiv.org/abs/2605.21347)

**<font color=#1a73e8>作者：</font>** Akshay Manglik, Apaar Shanker, Kaustubh Deshpande 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diagnosing failures in LLM agents remains largely manual. Practitioners inspect a small subset of execution traces, form ad-hoc hypotheses, and iterate. This process misses patterns that only emerge across trace populations and does not scale to production corpora where individual traces span tens of thousands of tokens. We formalize the problem of corpus-level trace diagnostics. Given a corpus of execution traces, the goal is to produce grounded natural-language insights that characterize systematic behavioral patterns across trace groups, each linked to supporting evidence. We present the Insights Generator (IG), a multi-agent system that answers diagnostic questions by proposing and testing hypotheses across the trace corpus to produce an evidence-backed insights report. We evaluate IG across qualitative and objective dimensions, spanning rubric-based report assessment and downstream performance improvements achieved by implementing IG insights. Human experts using IG reports improve scaffold performance by 30.4pp over the unmodified baseline scaffold, and coding agents leveraging IG-derived insights show consistent and stable gains. Across benchmarks, IG's scout-investigator architecture produces findings comparable in detection coverage to competing approaches, while domain experts rated IG reports as leading depth and evidence quality.

---


### 129. [LASH: Adaptive Semantic Hybridization for Black-Box Jailbreaking of Large Language Models](https://arxiv.org/abs/2605.21362)

**<font color=#1a73e8>作者：</font>** Abdullah Al Nomaan Nafi, Fnu Suya, Swarup Bhunia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Jailbreak attacks expose a persistent gap between the intended safety behavior of aligned large language models and their behavior under adversarial prompting. Existing automated methods are increasingly effective but each commits to a single attack family (e.g., one refinement loop, one tree search, one mutation space, or one strategy library) and no single family dominates: the best-performing method shifts across target models and harm categories, suggesting complementary strengths that per-prompt composition could exploit. We introduce LASH (LLM Adaptive Semantic Hybridization), a black-box framework that treats outputs from multiple base attacks as reusable seed prompts and adaptively composes them for each target request. Given a seed pool, LASH searches over seed subsets and softmax-normalized mixture weights; a composition module synthesizes a single candidate prompt, and a derivative-free genetic optimizer updates the weights using black-box target feedback and a two-stage fitness function combining keyword-based refusal detection with LLM-judge scoring. On JailbreakBench, which contains 100 harmful prompts across 10 categories, we evaluate LASH on six common target models. LASH achieves an average attack success rate of 84.5% under keyword-based evaluation and 74.5% under two-stage evaluation, where responses are first filtered for refusals and then scored by an LLM judge for whether they substantively fulfill the original harmful request. LASH outperforms five state-of-the-art baselines on both metrics with only 30 mean target queries. LASH also remains competitive under three defense mechanisms and induces more success-like internal representations. These results suggest that adaptive composition across heterogeneous jailbreak strategies is a promising direction for black-box red-teaming.

---


### 130. [Combating Harms of Generative AI in CS1 with Code Review Interviews and a Flipped Classroom](https://arxiv.org/abs/2605.21374)

**<font color=#1a73e8>作者：</font>** Peter Fowles, Erik Falor, Sulove Bhattarai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Background and Context: Large Language Models (LLMs) are more accessible and accurate than ever before, raising significant concerns for computing educators. One major concern is students using LLMs to bypass the effort needed to understand concepts and metacognitive strategies essential for success in computer science.
Objectives: We contribute a unique approach to assessing and building up student understanding through weekly oral code review assessments. These formative assessments incentivize students to understand their submitted code, regardless of whether or not the code was generated by AI tools. We also use a flipped classroom to provide time for students to learn concepts outside of class and provide ample time for students to schedule code review interviews.
Methods: For this paper, we collected data from three semesters. We analyze student exam scores, keystroke logs, and surveys to understand how the new course policies affected student learning, behavior, and attitudes.
Findings: Pairwise comparison of exam results reveals a statistically insignificant increase in average scores for Fall 2025 compared to previous semesters. Keystroke logs show a significant increase in characters pasted per total characters input into coding assignments in Fall 2025, pointing towards higher AI usage. Survey results show positive student sentiment towards code reviews at the end of Fall 2025, with nearly all negative feedback being addressable through better scheduling and more rigorous TA training.
Implications: Oral code reviews with a flipped classroom appear to be effective at mitigating harms of LLM use while providing space for students to freely experiment with these tools. Our work suggests that students in Fall 2025 still show adequate understanding of material covered in written exams, despite dramatic increases in LLM usage for coding assignments.

---


### 131. [Post-Hoc Understanding of Metaphor Processing in Decoder-Only Language Models via Conditional Scale Entropy](https://arxiv.org/abs/2605.21391)

**<font color=#1a73e8>作者：</font>** Lawhori Chakrabarti, Jennifer Johnson-Leung, Bert Baumgaertner 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Metaphor requires a language model to resolve a token whose contextual meaning diverges from its basic literal sense. Understanding how transformer models organize this reinterpretation across depth remains an open problem in mechanistic interpretability. We introduce conditional scale entropy (CSE), a wavelet-derived measure of how broadly transformer computation engages across frequency scales at each layer position. Two theorems establish that CSE is invariant to update magnitude, isolating the structural pattern of updates from their intensity. Using CSE, we find that metaphorical tokens produce significantly higher spectral breadth than literal tokens at contiguous layer positions on every decoder-only architecture tested, from 124M to 20B parameters (GPT-2 family, LLaMA-2 7B, GPT-oss 20B). The effect survives cluster-based permutation correction, recurs in the early-to-mid relative depth range across models, and converges with an independent analysis of 200 naturalistic VUA pairs. Specificity controls further show that the effect is not explained by semantic complexity or by matched propositional content. These results identify multi-scale coordination as a consistent signature of metaphorical language processing in the decoder-only architectures examined, and establish CSE as a principled tool for characterizing cross-depth structure in transformers.

---


### 132. [What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema](https://arxiv.org/abs/2605.21404)

**<font color=#1a73e8>作者：</font>** Mahdi Naser Moghadasi, Faezeh Ghaderi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We read twelve well-known LLM agent benchmark papers and recorded, dimension by dimension, what each paper actually says about how its evaluation was run. The motivation came from a familiar frustration: two papers will report results on the same benchmark with the same model name and disagree, and you cannot tell why -- the scaffold, the sampling settings, the subset, or the evaluator version. In many cases the published artifact does not let you answer. This paper is an implementation report on the attempt. We designed a small audit schema (five fields: benchmark identity, harness specification, inference settings, cost reporting, failure breakdown), wrote a scoring codebook with the boundary cases we hit during pilot scoring, applied it to twelve canonical papers (eight agent, four classical static), and recorded what we saw. We score the disclosure of an agent run, not its correctness, and make no claim that disclosure implies a trustworthy result. The mean audit score across the eight agent-benchmark papers is 0.38 (out of 1.0), and across the four classical static benchmarks 0.66; the largest gap is on cost (none of the eight agent benchmark papers disclose inference cost in any form) and on harness specification (none fully disclose a content-addressed container image of the evaluation environment). We release the schema as a JSON Schema file, the codebook as a Markdown document, and the raw scoring sheet as a CSV. The scoring was performed by a single auditor in one pass; a multi-rater audit is the natural next step, and we discuss what we think it would change.

---


### 133. [Preference-aware Influence-function-based Data Selection Method for Efficient Fine-Tuning](https://arxiv.org/abs/2605.21422)

**<font color=#1a73e8>作者：</font>** Qihao Lin, Guanxu Chen, Dongrui Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As LLMs continue to scale, improving training efficiency increasingly depends on using data more effectively. Data selection addresses this problem by allocating a limited training budget to samples that best promote a target behavior. Existing methods usually represent the target behavior with a set of target examples, but often treat these examples as equally important. This can be inefficient because target examples may differ in their relevance to the current model: examples closer to the model's current behavior provide more actionable guidance than those farther away. We propose PRISM (PReference-aware Influence-function-based Data Selection Method for Efficient Fine-Tuning), which uses the current model's preference to weight target examples and construct a preference-aware target representation. PRISM then scores candidate training samples by their alignment with this representation, concentrating the data budget on samples more likely to move the model toward the target behavior. Theoretical analysis shows that this preference weighting yields a more effective first-order direction for increasing target-behavior preference. Experiments across model families and scales show that PRISM improves both efficient fine-tuning and safety-oriented SFT repair, demonstrating that precise target-behavior characterization is key to budget-efficient data selection.

---


### 134. [PALS: Power-Aware LLM Serving for Mixture-of-Experts Models](https://arxiv.org/abs/2605.21427)

**<font color=#1a73e8>作者：</font>** Can Hankendi, Rana Shahout, Minlan Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) inference has become a dominant workload in modern data centers, driving significant GPU utilization and energy consumption. While prior systems optimize throughput and latency by batching, scheduling, and parallelism, they largely treat GPU power as a static constraint rather than a controllable resource. In this paper, we present a power-aware runtime for LLM serving, PALS, that treats GPU power caps as a first-class control knob and jointly optimizes them with software parameters such as batch size. The system combines lightweight offline power-performance models with a feedback-driven controller to select configurations that satisfy throughput targets while maximizing energy efficiency. We implement PALS within an existing LLM serving framework, vLLM, demonstrating that it requires no model retraining or API changes. Across multi-GPU systems and both dense and mixture-of-experts (MoE) models, PALS improves energy efficiency by up to 26.3%, reduces QoS violations by 4x to 7x under power constraints, and tracks dynamic power budgets. These results highlight the potential of integrating power control directly into LLM inference runtimes, enabling energy-proportional and grid-interactive AI systems.

---


### 135. [torchtune: PyTorch native post-training library](https://arxiv.org/abs/2605.21442)

**<font color=#1a73e8>作者：</font>** Mark Obozov, Maxime Griot, Joseph Cummings 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLMs typically require multistage training pipelines to achieve strong downstream performance, with post-training serving as the main interface for adapting open-weight models. We introduce torchtune, a PyTorch-native library designed to streamline the post-training lifecycle of LLMs, enabling efficient fine-tuning, experimentation, and deployment-oriented workflows. Unlike many existing fine-tuning frameworks, which often optimize for ease of use, specialized recipes, or hardware efficiency at the cost of transparency and extensibility, torchtune emphasizes modularity, hackability, and direct access to the underlying PyTorch components. In this paper, we present the design principles behind torchtune, describe how they are reflected in its model builders, training recipes, and distributed training stack, and evaluate the library across representative post-training settings. We compare against popular fine-tuning frameworks, including Axolotl and Unsloth, and show that torchtune provides strong performance and memory efficiency across many settings while remaining flexible enough for rapid research iteration. These results position torchtune as a practical foundation for reproducible LLMs post-training research.

---


### 136. [TempGlitch: Evaluating Vision-Language Models for Temporal Glitch Detection in Gameplay Videos](https://arxiv.org/abs/2605.21443)

**<font color=#1a73e8>作者：</font>** Yakun Yu, Ashley Wiens, Adrián Barahona-Ríos 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly being explored for video game quality assurance, especially gameplay glitch detection. Most existing evaluations, however, treat glitches as static visual anomalies, asking models to detect failures from a single frame. We argue that this framing misses a key distinction: some glitches are spatial and visible in an isolated frame, whereas others are temporal and become evident only through changes across ordered frames. A preliminary study confirms this gap, showing that temporal glitches are substantially harder for VLMs to detect than spatial ones. To enable systematic evaluation of this underexplored setting, we introduce TempGlitch, a controlled gameplay video benchmark for temporal glitch detection. TempGlitch covers five temporal glitch types with balanced per-category samples, together with paired glitch-free videos that enable reliable binary evaluation. We evaluate 12 proprietary and open-weight VLMs across multiple frame-sampling settings. Our results show that current VLMs remain near chance on TempGlitch, often collapsing into either overly conservative behavior that misses most glitches or overly sensitive behavior that flags clean videos as glitchy. Moreover, denser frame sampling and larger model size do not reliably resolve these failures. TempGlitch provides a focused testbed for temporal reasoning, robust gameplay understanding, and automated glitch detection with VLMs. Code and data are available at the project website.

---


### 137. [ProtoPathway: Biologically Structured Prototype-Pathway Fusion for Multimodal Cancer Survival Prediction](https://arxiv.org/abs/2605.21454)

**<font color=#1a73e8>作者：</font>** Amaya Gallagher-Syed, Costantino Pitzalis, Myles J. Lewis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce ProtoPathway, an interpretable-by-design multimodal framework for cancer survival prediction that unifies whole slide imaging and transcriptomics through encoders producing biologically grounded representations on both sides of the fusion. On the histopathology side, $K$ learnable morphological prototypes, trained end-to-end with the survival objective, serve as the slide representation itself: patches flow into prototype tokens via soft assignment, compressing variable-length patch sets into fixed task-adaptive tokens. On the genomic side, a bipartite graph neural network encodes gene expression within the Reactome pathway hierarchy, producing pathway embeddings that reflect both constituent genes and their broader biological context through bidirectional message passing over a shared gene--pathway graph. Cross-modal attention then operates over a compact prototype $\times$ pathway matrix in which prototypes query pathways, modeling the biological direction in which molecular programs give rise to tissue morphology. Because both axes carry stable task-learned identity, the attention matrix is itself an interpretability output, yielding native inference-time attribution across the full biological hierarchy, from genes through pathways and prototypes to spatial tissue maps. We evaluate on five TCGA cancer cohorts, demonstrating competitive or superior survival prediction with substantially improved biological interpretability and reduced computational cost, with interpretability claims validated through fold-stratified rank-based population-level analysis. Our source code, model weights, and Reactome pathways, together with a unified codebase reimplementing all multimodal survival baselines under identical preprocessing and evaluation, are available at: this https URL.

---


### 138. [Mem-$π$: Adaptive Memory through Learning When and What to Generate](https://arxiv.org/abs/2605.21463)

**<font color=#1a73e8>作者：</font>** Xiaoqiang Wang, Chao Wang, Hadi Nekoei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Mem-$\pi$, a framework for adaptive memory in large language model (LLM) agents, where useful guidance is generated on demand rather than retrieved from external memory stores. Existing memory-augmented agents typically rely on similarity-based retrieval from episodic memory banks or skill libraries, returning static entries that often misalign with the current context. In contrast, Mem-$\pi$ uses a dedicated language or vision-language model with its own parameters, separate from the downstream agent, to generate context-specific guidance for complex tasks. Conditioned on the current agent context, the model jointly decides when to produce guidance and what guidance to produce. We train it with a decision-content decoupled reinforcement learning (RL) objective, enabling it to abstain when generation would not help and otherwise produce concise, useful guidance. Across diverse agentic benchmarks spanning web navigation, terminal-based tool use, and text-based embodied interaction, Mem-$\pi$ consistently outperforms retrieval-based and prior RL-optimized memory baselines, achieving over 30% relative improvement on web navigation tasks.

---


### 139. [Leveraging LLMs for Grammar Adaptation: A Study on Metamodel-Grammar Co-Evolution](https://arxiv.org/abs/2605.21465)

**<font color=#1a73e8>作者：</font>** Weixing Zhang, Bowen Jiang, Rahul Sharma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In model-driven engineering, metamodel evolution leads to the need to adapt corresponding grammars to maintain consistency, which typically requires tedious manual work. Existing rule-based methods can achieve partial automation but have limitations when handling complex grammar scenarios. This paper proposes a Large Language Model-based approach that automatically applies adaptations to new grammars after evolution by learning grammar adaptations from previous versions. We evaluated this approach on six real-world Xtext domain-specific languages, using four DSLs as a training set to develop prompting strategies, two DSLs as a test set for validation, and conducting a longitudinal case study on QVTo. The evaluation used three Large Language Models (Claude Sonnet 4.5, ChatGPT 5.1, Gemini 3) and measured grammar adaptation quality from three dimensions: grammar rule-level adaptation consistency, output similarity, and metamodel conformance. Results show that on the test set, all three LLMs achieved 100% adaptation consistency and output similarity, while the rule-based approach achieved only 84.21% on DOT and 62.50% on Xcore. In the QVTo longitudinal study, the LLM-based approach successfully reused learned adaptations across all three evolution steps without manual grammar editing, while the rule-based approach required manual adjustments in two of three transitions. However, on large-scale grammars (EAST-ADL, 297 rules), LLMs' adaptation consistency was far below 90%. This study demonstrates the advantages of LLM-based approaches in handling complex grammar scenarios, while revealing their limitations in large-scale grammar adaptation.

---


### 140. [DelTA: Discriminative Token Credit Assignment for Reinforcement Learning from Verifiable Rewards](https://arxiv.org/abs/2605.21467)

**<font color=#1a73e8>作者：</font>** Kaiyi Zhang, Wei Wu, Yankai Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards (RLVR) has emerged as a central technique for improving the reasoning capabilities of large language models. Despite its effectiveness, how response-level rewards translate into token-level probability changes remains poorly understood. We introduce a discriminator view of RLVR updates, showing that the policy-gradient update direction implicitly acts as a linear discriminator over token-gradient vectors and thereby determines which token probabilities are increased or decreased during learning. Under standard sequence-level RLVR, this discriminator is constructed from positive- and negative-side centroids formed by advantage-weighted averaging of token-gradient vectors. However, such centroid construction can be dominated by shared high-frequency patterns, such as formatting tokens, diluting sparse yet discriminative directions that better distinguish high-reward responses from low-reward ones. To address this limitation, we propose $\textbf{DelTA}$, a discriminative token credit assignment method that estimates token coefficients to amplify side-specific token-gradient directions and downweight shared or weakly discriminative ones. These coefficients reweight a self-normalized RLVR surrogate, making the effective side-wise centroids more contrastive and thereby reshaping the RLVR update direction. On seven mathematical benchmarks, DelTA outperforms the strongest same-scale baselines by 3.26 and 2.62 average points on Qwen3-8B-Base and Qwen3-14B-Base, respectively. Additional results on code generation, a different backbone, and out-of-domain evaluations further demonstrate the generalization ability of DelTA.

---


### 141. [You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories](https://arxiv.org/abs/2605.21468)

**<font color=#1a73e8>作者：</font>** Zhepei Wei, Xinyu Zhu, Wei-Lin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become a dominant paradigm for improving reasoning in large language models (LLMs), yet the underlying geometry of the resulting parameter trajectories remains underexplored. In this work, we demonstrate that RLVR weight trajectories are extremely low-rank and highly predictable. Specifically, we find that the majority of downstream performance gains are captured by a rank-1 approximation of the parameter deltas, where the magnitude of this projection evolves near-linearly with training steps. Motivated by this, we propose a simple and compute-efficient method RELEX (REinforcement Learning EXtrapolation), which estimates the rank-1 subspace from a short observation window and extrapolates future checkpoints via linear regression, with no learned model required. Across three models (i.e., Qwen2.5-Math-1.5B, Qwen3-4B-Base, and Qwen3-8B-Base), RELEX produces checkpoints that match or exceed RLVR performance on both in-domain and out-of-domain benchmarks, requiring as few as 15% steps of full RLVR training. Remarkably, RELEX is able to extrapolate far beyond the observation window at no training cost, predicting checkpoints up to 10-20$\times$ beyond the observed prefix with continued improvement (e.g., observe only the first 50 steps and extrapolate to 1000 steps). Our ablation analysis confirms the minimalist sufficiency of RELEX: neither increasing the subspace rank nor employing non-linear modeling yields further gains in extrapolation. Finally, we show that RELEX's success stems from a "denoising" effect: by projecting updates onto the rank-1 subspace, the model discards stochastic optimization noise that would otherwise degrade performance during extrapolation. Our code is available at this https URL.

---


### 142. [WikiVQABench: A Knowledge-Grounded Visual Question Answering Benchmark from Wikipedia and Wikidata](https://arxiv.org/abs/2605.21479)

**<font color=#1a73e8>作者：</font>** Basel Shbita, Pengyuan Li, Anna Lisa Gentile  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Question Answering (VQA) benchmarks have largely emphasized perception-based tasks that can be solved from visual content alone. In contrast, many real-world scenarios require external knowledge that is not directly observable in the image to answer correctly. We introduce WikiVQABench, a human-curated knowledge-grounded VQA benchmark constructed by systematically combining Wikipedia images, their associated article captions, and structured knowledge from Wikidata. Our pipeline uses large language models (LLMs) to generate candidate multiple-choice image-question-answer sets. All generated instances are subsequently reviewed and curated by human annotators to ensure factual correctness, visual-text consistency, and that each question requires external knowledge in addition to visual evidence for correct resolution. WikiVQABench comprises a substantial collection of Wikipedia images with curated multiple-choice questions designed to benchmark knowledge-aware vision-language models (VLMs). Evaluation of fifteen VLMs (256M-90B parameters) reveals a wide performance range (24.7%-75.6% accuracy), demonstrating that the benchmark effectively discriminates model capabilities on knowledge-intensive reasoning. The dataset and benchmarking code are publicly available.

---


### 143. [EvoStruct: Bridging Evolutionary and Structural Priors for Antibody CDR Design via Protein Language Model Adaptation](https://arxiv.org/abs/2605.21485)

**<font color=#1a73e8>作者：</font>** Mansoor Ahmed, Sujin Lee, Umar Khayaz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivariant graph neural network (GNN) methods for antibody complementarity-determining region (CDR) design achieve the highest sequence recovery but suffer from severe vocabulary collapse. The current best GNN methods over-predict very few amino acids, such as tyrosine and glycine, while ignoring functionally important residues. We trace this failure to GNN encoders learning amino acid distributions de novo from limited structural data, discarding substitution patterns encoded in evolutionary databases. To resolve this, we propose EvoStruct, which bridges a frozen protein language model (PLM) with 3D structural context from an E(3)-equivariant GNN via a cross-attention adapter. Unlike prior PLM-structure adapters for general protein design, EvoStruct targets the vocabulary collapse problem specific to CDR design through progressive PLM unfreezing and R-Drop consistency regularization. On the CHIMERA-Bench dataset, EvoStruct achieves the highest amino acid recovery and lowest perplexity among several antibody design methods, improving sequence recovery by 16% and reducing perplexity by 43% relative to the best GNN baselines, while recovering 2.3x greater amino acid diversity and the highest binding-pair correlation with ground truth.

---


> [!TIP]
> 当前位于：**101-143**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-143**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
