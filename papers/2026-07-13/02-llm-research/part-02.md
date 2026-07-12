# 🧠 大模型相关研究 | 2026年07月13日

> 本类共 **99** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-99**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-99**

---

### 51. [SQuaD-SQL: Efficient Text-to-SQL with Small Language Models via LLM-Guided Knowledge Distillation](https://arxiv.org/abs/2607.08161)

**<font color=#1a73e8>作者：</font>** Wangyu Wu, Xiaojian Lin, Rong Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL is a fundamental task in natural language processing that enables users to interact with structured databases using natural language. While large language models (LLMs) have demonstrated remarkable performance on this task, their substantial computational requirements hinder deployment in resource-constrained settings. In this paper, we introduce SQuaD-SQL (Small-Qualified and Distilled for SQL), a novel approach that empowers small language models (SLMs) to approach the performance of LLMs on the Text-to-SQL task while significantly improving efficiency through knowledge distillation and synthetic data generation. Our method comprises three key components: (1) LLM-based synthetic data generation, where structured knowledge is extracted from LLMs via carefully designed prompting strategies; (2) parameter-efficient fine-tuning, enabling full model training on a single consumer-grade GPU; and (3) domain-adaptive fine-tuning, where domain-specific synthetic data further enhances performance in targeted domains. Experiments on the WikiSQL dataset demonstrate that SQuaD-SQL achieves an execution accuracy of 86.9% on the test set, approaching the performance of LLMs while offering faster inference and lower memory usage. These results suggest that, with proper training strategies, SLMs can serve as practical and efficient alternatives for Text-to-SQL applications in resource-limited environments.

---


### 52. [ASMR: Agentic Schema Generation for Ship Maintenance Report Writing](https://arxiv.org/abs/2607.08177)

**<font color=#1a73e8>作者：</font>** Sohrab Namazi Nia, Amogh Dalal, Ning Sa 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we study the automatic schema generation problem: given a collection of historical ship maintenance and operational reports across multiple form categories, automatically discover compact and informative schemas that capture the essential information requirements of each report type. To address this challenge, we propose ASMR, a modular agentic framework consisting of two specialized agents. A Field Generation Agent extracts semantic concepts from historical narratives and generates candidate schema fields through adaptive multi-granularity clustering, while a Structural Optimizer Agent employs reinforcement learning to identify compact, informative, and non-redundant schema representations. The resulting schemas can guide report authors toward producing more complete, consistent, and actionable reports. Preliminary results demonstrate the promise of the proposed approach and highlight several open research challenges at the intersection of data management, agentic AI, and human-centered AI.

---


### 53. [Leveraging Color Naming for Image Enhancement](https://arxiv.org/abs/2607.08185)

**<font color=#1a73e8>作者：</font>** David Serrano-Lozano, Luis Herranz, Michael S. Brown 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Enhancing images to make them visually appealing is a persistent challenge in computer vision. Many deep-learning methods train models on paired datasets to replicate expert editing styles. However, these approaches struggle with two key issues: (1) interpretability and (2) a parametrization suitable for user adjustments. To address these challenges, we present NamedCurves+, an approach inspired by the concept of Color Naming, a universal set of familiar colors widely used in software tools for intuitive editing. Our method integrates color names into a learning-based framework, enabling global adjustments for each named color through tone curves. To address local image variations, we incorporate a transformer block that captures spatial dependencies, enabling context-aware edits across the image. NamedCurves+ enhances the retouching process's interpretability and supports user interaction, allowing flexible modifications of individual tone curves to refine the retouched image according to personal preferences. Extensive experiments on tasks such as image retouching, tone mapping, and exposure correction demonstrate that NamedCurves+ outperforms state-of-the-art methods. Notably, our approach is both explainable, as the tone curves explicitly represent how each color name contributes to the enhancement, and interactive, allowing users to customize the retouching process and achieve results tailored to their liking.

---


### 54. [Hidden Decoding at Scale: Latent Computation Scaling for Large Language Models](https://arxiv.org/abs/2607.08186)

**<font color=#1a73e8>作者：</font>** Aiwei Liu, Cheng Shi, Chuhan Wu 等 48 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scaling Large Language Models (LLMs) has been driven mainly by enlarging the Transformer backbone, but for an already-strong model this requires another round of costly pretraining. We study whether an existing backbone can keep improving by allocating more computation to each token while leaving the Transformer backbone fixed. Depth-recurrent (looped) Transformers pursue this goal but are hard to scale, because looped computation does not fit naturally with the pipeline parallelism used to train the largest models. We add computation along the sequence-length dimension, where the extra computation is simply a longer input and stays compatible with standard large-model training. We propose Hidden Decoding, a sequence-length scaling method applied during continued pretraining (CPT). It expands each token into n streams with independent embedding tables and keeps the intermediate streams' key-value cache as context, so each token performs more internal computation without adding or widening Transformer layers. To keep this affordable at scale, we introduce Stream-Factorized Attention, in which most layers attend only within each stream and only a few layers mix across streams, reducing the attention cost from quadratic to roughly linear in n. Experiments support two scaling results. At frontier scale, we train WeLM-HD4-80B and WeLM-HD4-617B at n=4 and improve their matched non-HD baselines, making Hidden Decoding the first demonstrated sequence-length scaling method at the 100B+ MoE scale. Across expansion factors, the gains grow as n increases, showing that sequence-length expansion is a practical fixed-backbone scaling path for frontier-scale LLMs.

---


### 55. [Open-ended Multi-agent Autocurricula via Visual Inspection of Policies with Multi-modal LLMs](https://arxiv.org/abs/2607.08193)

**<font color=#1a73e8>作者：</font>** Lorenzo Pantè, Andrea Fanti, Roberto Capobianco  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-ended curricula in Reinforcement Learning (RL) aim to train generally-capable agents by identifying tasks that facilitate learning increasingly complex skills. A major challenge when designing such curricula is assessing task difficulty relative to the agent's current learning progress. While previous work has explored using scalar task scores or textual summaries of the agent's behavior, here we study a different approach: directly inspecting policy behavior via recorded episode videos. We introduce a simple yet effective instantiation of this approach which leverages a Video Language Model (VLM) to both process these videos and provide curriculum recommendations, which we call Visual Inspection of Policies (VIP). Since videos can naturally contain any number of controllable agents, we empirically study VIP on the StarCraft Multi-Agent Challenge (SMAC). We show that even with a lightweight and openly accessible VLM (VideoLLaMa2-7B), VIP can use policy videos to generate more effective curricula than both its text-only ablation and methods that rely on scalar task scores.

---


### 56. [Dive Into the Implicit Biases of Low-rank Vision-language Alignment](https://arxiv.org/abs/2607.08194)

**<font color=#1a73e8>作者：</font>** Mingjia Shi, Shuo Wang, Xiaobo Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language alignment, the stage that bridges pretrained vision encoders and large language models, is widely treated as a form of pretraining requiring full-parameter updates. We challenge this view and investigate what happens when low-rank adaptation is applied to the LLM during this stage instead. We find that low-rank alignment not only reduces computational costs but also outperforms full-parameter alignment on most benchmarks. To understand this phenomenon, we systematically characterize the implicit biases introduced by low-rank adaptation during alignment. Empirically, we find that low-rank alignment shifts model behavior from hallucinatory to conservative and preserves per-token linear separability of visual features that full-parameter alignment disrupts, a phenomenon we term LS-curse. Geometrically, low rank aligned models exhibit more homogeneous and structurally stable visual representations, maintaining modality-specific knowledge rather than prematurely fusing entity-level semantics. Theoretically, we establish two theorems showing that low-rank alignment induces preferences for parameter subspaces with flat gradients and feature subspaces robust to perturbations, providing a principled explanation for the observed structure-preserving behavior. Extensive experiments cover ablation over 100 alignment configurations, three families of low-rank operators, and various rank, encoder, and other settings.

---


### 57. [Metrics or Mirage? An Audit of Evaluation Inconsistencies in Colonoscopy Polyp Segmentation Benchmarks](https://arxiv.org/abs/2607.08203)

**<font color=#1a73e8>作者：</font>** Aisha Urooj, Zain Ul Abdien, Neelu Madan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Progress in colonoscopy polyp segmentation is routinely reported through leaderboard comparisons on a small set of public benchmarks. We argue that this apparent progress is difficult to verify: a systematic audit of \textbf{27 papers} published between 2015 and 2026 reveals three structural problems in how the community evaluates models. \textbf{First}, 25 of 27 papers \textit{omit the Hausdorff distance}. Hausdorff distance is a boundary-accuracy metric with direct clinical relevance for detecting flat or small polyps, and is a standard in radiotherapy segmentation. \textbf{Second}, at least five \textit{incompatible train/test split protocols} co-exist across papers reporting results on the same two datasets (Kvasir-SEG and CVC-ClinicDB), making published Dice scores non-comparable even when they appear in the same leaderboard column. \textbf{Third}, 26 of 27 papers make \textit{performance claims without any statistical significance test}. Strikingly, four papers published \emph{after} the Metrics Reloaded framework~\cite{metricsreloaded2024} (Maier-Hein et al., \textit{Nature Methods} 2024) perpetuate these same problems, suggesting that general-purpose metric guidance has not yet reached the colonoscopy sub-community. To show these problems are not merely cosmetic, we re-evaluate five representative models under three controlled protocols with a single uniform scorer, and find that the reported metric conceals large boundary and recall failures, that the ``best'' model changes with the metric, and that near-tied rankings reverse across random splits. We propose a five-point \textbf{Polyp Segmentation Reporting Checklist}~(PSRC) as a lightweight, domain-adapted corrective.

---


### 58. [Diarization-Guided Qwen-ASR Adaptation for Multilingual Two-Speaker Conversational Speech](https://arxiv.org/abs/2607.08208)

**<font color=#1a73e8>作者：</font>** Hao Wu, RongQi Han, Zhen Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes our self-designed system for Task 1 of the MLC-SLM 2026 Challenge for multilingual two-speaker conversational speech. The system combines a modular speaker diarization front end with a challenge-adapted Qwen3-ASR-1.7B recognizer. The diarization front end performs voice activity detection, subsegment generation, CAMPPlus speaker embedding extraction, two-speaker spectral clustering, and RTTM-based audio segmentation. The resulting speaker-attributed segments are grouped by language or region and decoded by the adapted ASR model. For ASR adaptation, we first perform supervised full fine-tuning on the official training data, then apply LoRA fine-tuning with synthetic speech generated by a three-pipeline TTS-based synthetic speech augmentation framework, and finally refine the model using GRPO reinforcement learning with rewards based on WER/CER and penalties for hallucination, repetition, and length deviation. On the official development set, the full system achieves an average tcpMER of 23.70, reducing the error rate by 6.83 absolute points relative to the released Qwen-ASR-1.7B performance. On the final evaluation set, the system achieves an average tcpMER of 17.97. Ablation results show that supervised fine-tuning provides the largest gain, while synthetic-speech LoRA adaptation and reinforcement learning further improve robustness.

---


### 59. [LUMI: Tokenizer-Agnostic LLM-Based Lossless Image Compression](https://arxiv.org/abs/2607.08221)

**<font color=#1a73e8>作者：</font>** Chris Xing Tian, Chengkai Wu, Ziyu Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based lossless image compression methods typically represent pixel data through the native text interface of a pretrained model, converting pixel values into token sequences that the LLM processes through its vocabulary head. This design shows that pretrained language models can provide probability estimates for image coding, but it also couples compression to tokenizer behavior, vocabulary-specific numeric tokens, and model-family-specific adaptation. In this paper, we present LUMI (LLM-based Unified Model-agnostic lossless Image compression), a tokenizer-agnostic framework for lossless RGB image compression with frozen LLM backbones. LUMI replaces pixel-as-text tokenization with a pixel embedding module that maps raw intensity and channel information into the continuous embedding space of the LLM. It further introduces intra-patch position encoding to retain two-dimensional spatial structure after flattening, and uses a 256-way prediction head to produce probabilities over the native pixel alphabet. Only the pixel embedding, position encoding, soft-prefix parameters, and prediction head are trained, while the LLM backbone remains fixed. Experiments on natural, medical, and remote-sensing image benchmarks with LLaMA, Qwen, and Gemma backbones show that LUMI provides a unified interface across tokenizer families, achieves competitive compression rates, and improves cross-domain robustness over tokenizer-based LLM compression baselines. These results formulate LLM-based lossless image compression as pixel-space adaptation of frozen foundation models rather than tokenizer-specific language-symbol modeling.

---


### 60. [Multimodal 3D LUT Generation via StatLUT with Statistical Features for Photorealistic Style Transfer](https://arxiv.org/abs/2607.08227)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Zhixiang Hao, Yu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photorealistic Style Transfer (PST) aims to transfer the color and tonal style of a reference to a content image while strictly preserving its structural integrity. However, existing deep learning-based methods inherently suffer from semantic entanglement caused by pre-trained image encoders, leading to unnatural spatial distortions. Moreover, current pixel-level mapping paradigms often ignore color gamut topology, resulting in color banding, while also lacking the multimodal capability for intuitive text-driven control. To address these bottlenecks, we propose StatLUT, an innovative multimodal framework for 3D LUT generation. First, we bypass traditional encoders and introduce a Lab-Extractor to derive spatially-agnostic statistical features, fundamentally decoupling color distributions from structural semantics to ensure artifact-free rendering. Second, we formulate LUT generation as a Transformer-based Seq2Seq translation task, utilizing a Multi-dimensional Residual Mapper (MR-Mapper) to predict topologically smooth 3D LUTs. Finally, to break the single-modal barrier, we propose the H-Diffuser, a lightweight Diffusion Transformer that directly synthesizes statistical features from natural language prompts, enabling flexible text-driven color grading. Extensive experiments on standard benchmarks demonstrate that StatLUT significantly outperforms state-of-the-art methods in both visual quality and quantitative metrics, pioneering a highly robust and flexible paradigm for multimodal photorealistic style transfer.

---


### 61. [Compete Then Collaborate: Frontier AI Teachers Build a Verifiable Curriculum to Improve a Coding Student Beyond Imitation](https://arxiv.org/abs/2607.08255)

**<font color=#1a73e8>作者：</font>** Miseong Shawn Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly serve as teachers generating training data for smaller students. Prior multi-teacher knowledge distillation methods merge outputs without determining which frontier model teaches best, often relying on an LLM judge biased toward its own outputs. We introduce a compete-then-collaborate framework where four frontier AI teachers (Claude, Codex-GPT, Grok, Gemini) are ranked head-to-head by an execution-based judge (unit tests and stdin-stdout checks) with fairness controls, and then collaborate to build a verifiable curriculum for a student (Qwen2.5-Coder). We report three findings. (1) Under execution verification, all teachers solve standard problems near-perfectly after self-correction (99-100%) due to a saturation effect, but harder competition problems separate them (Gemini 77% > Claude 69% = Codex 69% > Grok 50%); however, the robust student-side results do not depend on teacher ranking. (2) Imitation (SFT) on verified solutions does not improve, and can degrade, an already-competent student at 7B and 32B (e.g., from 76.7% to 72.7% on MBPP-test, and 5.9% to 2.9% on competition problems). (3) Using the same collaborative curriculum as a reinforcement learning with verifiable rewards (RLVR) environment improves the student (from 5.9% to 8.8% peak on competition problems, a +49% relative gain), reversing SFT's direction. The value of AI-teacher collaboration lies not in pooling answers to imitate, but in jointly constructing a verifiable environment where the student learns by doing. We release a reproducible on-prem pipeline (NVIDIA GB10) with framework patches for running GRPO on a bleeding-edge stack.

---


### 62. [Best-of-$N$ TTS Evaluation is Confounded by ASR Family Alignment](https://arxiv.org/abs/2607.08256)

**<font color=#1a73e8>作者：</font>** Taehyung Yu, Seongjae Kang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Best-of-$N$ (BoN) inference improves content consistency in zero-shot text-to-speech by selecting from $N$ candidates with an automatic speech recognition (ASR) verifier. We identify an underexplored evaluation confound: a verifier's apparent quality depends strongly on which ASR family judges it. On LibriSpeech-PC test-clean~\citep{librispeechpc} with F5-TTS~\citep{f5tts}, verifier rankings reverse across Whisper, wav2vec~2.0, and HuBERT evaluators, and same-family verifier-evaluator pairs recover 2-3$\times$ more oracle headroom than cross-family pairs despite near-identical representations (linear CKA $0.978$) -- a pattern consistent with identity- or lineage-level coupling rather than representational overlap. We propose two \textbf{cross-family rank ensembles} (rank-averaging and conjunctive max-rank) that attain the lowest mean WER across three independent evaluators -- $1.61\%$ at $N{=}10$ ($-12\%$ relative to F5-TTS) -- with no measurable degradation under automatic SIM-o/UTMOS metrics; the best single verifier drives WER from $2.06\%$ to $1.72\%$ ($-16.5\%$) under the official F5-TTS evaluator. We recommend cross-evaluator triangulation as default reporting practice.

---


### 63. [MentalHospital: A Virtual Environment for Evaluating Psychiatric Clinical Encounters](https://arxiv.org/abs/2607.08257)

**<font color=#1a73e8>作者：</font>** Yuming Yang, Xiao Sun, Yuanwei Zou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong performance on isolated psychiatric tasks, including dialogue, diagnosis, and treatment planning, yet existing benchmarks rarely simulate complete psychiatric clinical encounters. We introduce $\textbf{MentalHospital}$, a virtual evaluation environment for LLM-based psychiatric clinical encounters. MentalHospital instantiates the Subjective Interviewing, Objective Examination, Diagnostic Assessment, and Treatment Planning (S.O.A.P.) workflow, using skill-augmented standardized patients constructed from 1,193 de-identified psychiatric electronic health record (EHR) cases spanning all major ICD-11 categories and 76 disorders. Each encounter is assessed through a dual-track protocol that combines objective comparison against EHR-derived references with subjective assessment of clinical process quality. To scale specialist judgment, we develop $\textbf{MentalEval}$, five domain-specific evaluators covering communication empathy, interviewing professionalism, clinical-note quality, diagnostic rigor, and treatment appropriateness, trained with rubric-grounded SFT and expert-guided DPO. Survey responses from 22 clinicians support MentalHospital's clinical fidelity (3.88/5), while MentalEval achieves strong expert alignment with an average QWK of 0.944. Benchmarking shows that even the strongest LLM trails clinicians by 37.28 percentage points in objective psychiatric competence, with mental status assessment as a key bottleneck.

---


### 64. [UniRef-UAV: A Multimodal Benchmark for Universal Referring in UAV Imagery](https://arxiv.org/abs/2607.08267)

**<font color=#1a73e8>作者：</font>** Haibin Tian, Huichao Xie, Xuelin Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicles (UAVs) increasingly rely on visual grounding capabilities to localize task-relevant targets from diverse instructions in complex aerial scenes. Existing referring expression comprehension (REC) benchmarks and methods, however, are largely built around text-only queries and single-object outputs, which limits their applicability to practical UAV scenarios involving reference images, multimodal instructions, absent targets, and multiple valid target instances. To address this gap, we introduce \emph{Universal Referring}, a generalized UAV referring task that jointly expands the query modality and the output cardinality. We construct \emph{UniRef-UAV}, a multimodal benchmark that supports text-only, image-only, and text+image queries with modality-dependent target cardinality, where text-only and text+image queries admit no-target, single-target, and multi-target grounding while image-only queries focus on existence-aware single-instance grounding. It also provides in-domain and cross-domain evaluation protocols for visual-query generalization. We further present \emph{UAV-URNet}, a detection-style baseline that maps heterogeneous queries into a shared query space and predicts variable-size target sets through set prediction. Extensive experiments show that UAV-URNet provides a stable and reproducible baseline with more consistent no-target discrimination and a more lightweight, reproducible implementation than large general-purpose MLLMs. Additional domain analysis, query-representation analysis, and ablation studies demonstrate that multimodal queries help reduce visual-query ambiguity and promote a more unified query--target alignment space. The annotations, visual query crops/images, train/validation/test splits, evaluation scripts, and baseline code will be made publicly available to facilitate reproducible research.

---


### 65. [PolyUQuest: Verifiable Structure-Aware Web RAG over Heterogeneous Graphs](https://arxiv.org/abs/2607.08269)

**<font color=#1a73e8>作者：</font>** Ying Liu, Yi Ye, Quanyu Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing retrieval-augmented generation (RAG) systems treat web pages as flat text, losing the structural and semantic signals encoded in HTML. We present PolyUQuest, a verifiable, structure-aware web RAG framework built on a heterogeneous graph that unifies hyperlink topology between pages, DOM hierarchy within pages, and entity-relation knowledge across pages. A two-tier router dispatches each query to one of three retrieval modes matched to its structural need, including direct block retrieval, cross-page graph traversal, and multi-hop entity reasoning. Every answer is fully verifiable, as each cited block carries its source page, heading path, and entity links so that users can trace any claim back to its structural evidence. We evaluate on the official websites of the Hong Kong Polytechnic University (PolyU), comprising 4,240 pages, 31,086 DOM blocks, 29,119 entities, and 37,680 relations, together with a multi-type evaluation benchmark. PolyUQuest outperforms existing RAG systems in answer correctness, coverage, and faithfulness, while consuming significantly fewer LLM tokens per query. The demonstration provides an interactive interface for inspecting cited answers, comparing retrieval traces across routing modes, and exploring evidence graph paths. PolyUQuest is being prepared for deployment as a student-facing QA service at PolyU.

---


### 66. [Understanding Axes of Difficulty For Long Context Tasks Via PredicateLongBench](https://arxiv.org/abs/2607.08284)

**<font color=#1a73e8>作者：</font>** Siddhartha Jain, Ameya Velingker  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated rapidly improving long-context capabilities, prompting a wave of benchmarks designed to evaluate them. However, existing long-context evaluations - from Needle-in-a-Haystack (NIAH) tests to more recent multi-hop reasoning and summarization tasks - predominantly measure average-case performance, and many are either saturated or lack robustness. Notably absent is a systematic way to probe how models perform as we scale up the difficulty of tasks along various axes. We address this gap by proposing PredicateLongBench, a benchmark that stress-tests long-context reasoning by asking models to identify the longest contiguous subsequence of words in a long input that satisfies given predicates/constraints (e.g., lexicographic ordering), drawn from a broader predicate class. The central innovation of our benchmark is the identification and systematic exploration of multiple different axes of difficulty which test multiple aspects of long context understanding. We provide two complementary generation pipelines - a fully synthetic setup using random word-like strings, and a real-world setup that samples words from natural documents while preserving their distributional properties. We find that frontier models struggle to perform well as we scale up the difficulty of tasks along our axes, demonstrating the utility of our benchmark in understanding the limitations of current long-context capabilities. Furthermore, the tasks in PredicateLongBench, though challenging, are conceptually simple and do not require LLM-based generations or judges.

---


### 67. [Write-Protected Discrete Bottlenecks for Language-Grounded World Models: A Structural Limitation and Sufficient Fix](https://arxiv.org/abs/2607.08312)

**<font color=#1a73e8>作者：</font>** Jiayi Fang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How should language interface with a world model's discrete symbol system? The dominant paradigm -- end-to-end injection of LLM/VLM features into robot world models (RT-2, Octo, PaLM-E) -- implicitly assumes that language gradients can directly shape physical symbol representations. We ask whether this assumption is safe, find that it is not, and characterize the minimal architectural constraint that prevents the failure. Any language gradient entering a Gumbel-softmax-based discrete symbol bottleneck forces a structural trade-off: the vanilla estimator collapses to 2.2/64 symbols (4/5 seeds), while five anti-collapse strategies maintain diversity but fail to learn semantic labels (all <= 9.2% accuracy). No tested GumbelBottleneck variant achieves both objectives simultaneously. Within this family of discrete bottlenecks, the failure is structural rather than a matter of optimization. We characterize a sufficient set of three constraints that prevent the failure: (1) cut the gradient chain (this http URL()), preventing language signals from reaching the symbol bottleneck; (2) provide a gradient-free semantic channel -- a non-parametric Memory Table (Dict[symbol -> Counter[label]], zero parameters, zero gradients) where co-occurrence counting replaces gradient-based binding; (3) handle symbol collisions via DP-Means streaming clustering for automatic sub-cluster splitting. All three layers together achieve 97.2% grounding accuracy vs. 22.2% without Layer 3. Across two experiments spanning 74 independent runs, we demonstrate zero symbol collapse in all 32 seeds, with the blackboard achieving 79-100% semantic binding across three encoder architectures (CNN, V-JEPA 300M, CLIP ViT-L), two environments, and three texture conditions. The fix trains fewer than 2M parameters and requires no LLM fine-tuning.

---


### 68. [Blind-Spots-Bench: Evaluating Blind Spots in Multimodal Models](https://arxiv.org/abs/2607.08317)

**<font color=#1a73e8>作者：</font>** Matteo Santelmo, Xiuying Wei, Israa Fakih 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern AI models achieve strong performance on many established benchmarks, yet they still fail on tasks that humans find almost trivial, such as manipulating a string or drawing a dog with five legs. These examples suggest that existing benchmarks may under-measure persistent blind spots in current systems. We introduce $\texttt{blind-spots-bench}$, a benchmark designed to expose such blind spots through tasks that appear simple for humans but remain challenging for modern AI. We collect raw questions from students in an AI course, clean and annotate them with structured reference solutions, and propose a task taxonomy tailored to the resulting dataset of 235 samples. We further develop an automated grading pipeline to evaluate a wide range of models, including open-weight and closed-source language, vision-language, and image-generation models. Our analysis on $\texttt{blind-spots-bench}$ reveals that closed-source frontier models can substantially outperform open-weight models with even $\approx10\%$ gap, even when they attain comparable performance on existing benchmarks. A more fine-grained analysis shows that no single model dominates across all task types, and that some tasks remain challenging for all evaluated models. These results highlight the value of $\texttt{blind-spots-bench}$ as a diagnostic stress test for identifying concrete weaknesses in current modern models.

---


### 69. [Eigenvalue Calibration for Semantic Embeddings of Large Language Models](https://arxiv.org/abs/2607.08377)

**<font color=#1a73e8>作者：</font>** Sebastian G. Gruber, Nassim Walha, Francis Bach 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification is central to the reliable deployment of large language models (LLMs), and eigenvalues of semantic embeddings have recently emerged as a key tool in state-of-the-art methods. However, conventional calibration results developed for classification probabilities cannot be directly transferred to eigenvalues. We address this gap by proposing a novel framework for calibrating the eigenvalues of semantic embeddings. We interpret LLMs combined with semantic embeddings of their generated answers as density matrix predictors, and we propose a novel approach to calibrate density matrix predictors by applying temperature scaling to their eigenvalues. We establish entropy-risk equivalence under calibration, derive a central calibration inequality specific to eigenvalues, and prove that temperature-scaled eigenvalues optimize calibration when minimizing proper score risks. Experiments on a variety of real-world settings show that current LLMs are systematically overconfident, and validate our theoretical findings. Together, these results advance the foundations and practice of uncertainty quantification for semantic embeddings.

---


### 70. [Towards Mechanistically Understanding Why Memorized Knowledge Fails to Generalize in Large Language Model Finetuning](https://arxiv.org/abs/2607.08393)

**<font color=#1a73e8>作者：</font>** Lu Dai, Ziyang Rao, Yili Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning LLMs to inject new knowledge faces a critical challenge: LLMs can quickly memorize new facts, yet fail to use them for downstream reasoning tasks. We formalize this failure as the \textit{\textbf{Knowing--Using Gap}}, characterized by an accuracy gap and a temporal lag between memorization and generalization. To understand this phenomenon, we fine-tune LLMs with unseen knowledge and monitor the spatial permeation dynamics of the knowledge internally using a novel intervention technique called self-patching. Self-patching identifies activation locations where relocating representations substantially improves failed generalization cases. These results are consistent with a knowledge-circuit misalignment hypothesis: memorized representations can exist internally but may not be routed to computation-effective layers. To demonstrate the practicality of this diagnostic finding, we design a simple heuristic strategy which recovers 58--75\% of the oracle headroom in generalization failure. Experiments are done cross-domain for the robustness of this finding.

---


### 71. [Attribute Retrieving for Open-Vocabulary Endoscopic Compositional Referring Segmentation](https://arxiv.org/abs/2607.08397)

**<font color=#1a73e8>作者：</font>** Shun Liu, Nan Xi, Yang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring Image Segmentation (RIS) aims to segment image regions specified by natural language, enabling fine-grained and controllable visual understanding. Extending RIS to endoscopic imagery, however, presents unique challenges, including scarce high-quality annotations and complex, domain-specific image-text relationships. Although recent vision-language models demonstrate strong cross-domain alignment, they often fail to capture fine-grained textual cues in endoscopic settings, resulting in suboptimal performance and limited generalization. To address these challenges, we introduce ReferEndoscopy, a large-scale benchmark for RIS in the endoscopy field. Building on this dataset, we propose the Attribute Retrieval-based Endoscopic-RIS (AR-ERIS) framework for open-vocabulary endoscopic compositional referring segmentation. AR-ERIS leverages attribute retrieval for open-vocabulary endoscopic compositional referring segmentation and is pretrained on the curated ReferEndoscopy dataset, achieving state-of-the-art performance with strong generalization across both simulated and real-world endoscopic data. The dataset and code will be publicly released upon completion of the review process.

---


### 72. [Game Theory Driven Multi-Agent Framework Mitigates Language Model Hallucination](https://arxiv.org/abs/2607.08403)

**<font color=#1a73e8>作者：</font>** Runzhe Liu, Biquan Bie, Zihao Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The application of lightweight Large Language Models in rule-based scientific domains remains severely limited by their tendency to mimic linguistic patterns rather than reproduce axiomatic reasoning, causing frequent hallucinations. Here, we show that G-Frame, an adaptive multi-agent framework integrating Bayesian and team game principles, establishes an automated closed-loop for high-quality data synthesis and model training. By forcing the internalization of domain constraints through structured reasoning, we synthesized a specialized corpus of 363,045 chains-of-thought and 199,589 question-answer pairs. The resulting 7B model OmniChem achieves performance parity with GPT 4o mini on custom benchmarks and ChemBench while exhibiting a 79.46% reduction in hallucinations relative to its base architecture. We further demonstrate the advanced capabilities of OmniChem in molecular design and synthesis planning. This work establishes a scalable paradigm utilizing adaptive multi-agents to overcome inherent reasoning deficiencies, offering a feasible pathway for accelerating knowledge discovery in specialized scientific fields.

---


### 73. [When Synthetic Speech Is All You Have: Better Call GRPO](https://arxiv.org/abs/2607.08409)

**<font color=#1a73e8>作者：</font>** Shashi Kumar, Yanis Labrak, Hasindri Watawana 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based ASR adapted to regulated domains such as banking is bottlenecked by privacy: real speech is costly and legally constrained to collect, making synthetic text-to-speech (TTS) an attractive substitute. Yet synthetic speech stays acoustically mismatched with real recordings, and work on this gap has stayed within supervised fine-tuning (SFT). We instead turn to reinforcement learning, and show that Group Relative Policy Optimization (GRPO) extracts far more from the same synthetic speech than SFT. Synthetic-only adaptation of the model with GRPO, a critic-free method rewarding low-WER hypotheses, reduces WER by 40\% relative to SFT (36.71\%$\to$22.09\%), and an SFT-then-GRPO combination pushes this further to 45\%. We trace the gain to behavior rather than representation: GRPO reduces insertion errors by improving stopping calibration and speech-to-text alignment by better anchoring attention to audio, leaving early-layer representations intact. When synthetic speech is the main resource, reinforcement learning should be preferred over supervised fine-tuning.

---


### 74. [OmniFood-Bench: Evaluating VLMs for Nutrient Reasoning and Personalized Health Advice](https://arxiv.org/abs/2607.08423)

**<font color=#1a73e8>作者：</font>** Qian Jiang, Zhecheng Shi, Jingpu Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid integration of Large Vision-Language Models (VLMs) into critical infrastructure promises to revolutionize
personalized healthcare and dietary management. However, in the domain of food systems, autonomous agents face a
unique and persistent challenge: the "Systemic Information Asymmetry" between visual appearance and intrinsic
nutritional composition. Existing benchmarks primarily focus on coarse-grained classification tasks, such as food
category recognition, which fail to evaluate the intricate reasoning chain required for real-world dietary management
-- specifically, the ability to traverse from identifying hidden ingredients to estimating physical mass, and finally
synthesizing safety-critical medical advice. In this paper, we introduce OmniFood-Bench, a comprehensive benchmark
constructed from the MM-Food-100K dataset. Unlike previous works, OmniFood-Bench evaluates VLMs across three
progressive capabilities: Basic Perception (Ingredients & Cooking Methods), Quantitative Reasoning (Portion Size &
Nutritional Profiling), and Safety-Critical Advisory (Disease-Specific Recommendations). We evaluate six
state-of-the-art VLMs, including gpt-5.1, gemini-3-flash, and qwen3-vl-8B. Our extensive experiments reveal a
startling "Semantic-Physical Gap": while models achieve near-human accuracy in naming dishes, they exhibit
catastrophic failure in mass estimation and frequently hallucinate benign advice for high-risk diabetic profiles. This
work establishes a rigorous standard for trustworthiness in autonomous agents deployed for public health. The code
and datasets are available in: this https URL

---


### 75. [DeltaV: Thinking with Visual State Updates in Unified Large Multimodal Models](https://arxiv.org/abs/2607.08434)

**<font color=#1a73e8>作者：</font>** Pengjie Wang, Linger Deng, Zujia Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current Unified Large Multimodal Models (ULMMs) support interleaved multimodal reasoning through textual reasoning and intermediate visual states, but typically generate each visual state as a full image. This full-image generation paradigm introduces substantial visual-token redundancy and dilutes supervision on sparse yet reasoning-critical state transitions. We propose DeltaV, a ULMM that replaces full-image generation with visual updates. Conditioned on historical visual states, DeltaV incrementally predicts compact update tokens that capture the visual changes across reasoning steps, avoiding repeated modeling of unchanged content. To align the token budget of each update with the magnitude of visual change, DeltaV introduces a temporal similarity (TSIM) Router, which stops allocating tokens once the marginal reconstruction gain falls below a threshold. To support more diverse and generalizable reasoning, we further construct StructCoT, a large-scale interleaved multimodal reasoning dataset with 1.05M samples spanning 44 task domains. Experiments show that the visual-update paradigm reduces newly generated visual tokens by 55.6\% on average without compromising reconstruction fidelity, and improves multimodal reasoning by 3.3\% over full-image generation. Trained with StructCoT and large-scale multimodal data, DeltaV-2B further outperforms substantially larger open-source models by 8.4\% on in-domain multimodal reasoning evaluations and surpasses the comparable-scale Qwen3-VL-2B by 5.9\% on external multimodal reasoning and understanding benchmarks. Code, models, and StructCoT will be released at this https URL.

---


### 76. [Predicting Viticulture Potential through an Ensemble of U-Net and a Geospatial Foundation Model](https://arxiv.org/abs/2607.08449)

**<font color=#1a73e8>作者：</font>** Jorge Ignacio Perez, Hwaai Kang Kee, Lucas Rassbach  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Determining agricultural potential is fundamental to sustainable land management and agricultural planning. Remote sensing data is increasingly valuable as an avenue for agricultural potential due to the cost of traditional methods (surveys, in-situ measurements, soil testing, etc). ImageCLEF AI4Agri 2026: Subtask 1 is concerned with the prediction of viticulture potential in Southern France. The DS@GT ARC's submission for Subtask 1 introduces an ensemble of U-Net and a Geospatial Foundation Model (Prithvi-2.0). Our best model achieved a $\pm$1 accuracy of 68.32 on the leaderboard, ranking 2nd among 7 teams. The implementation for this work is publicly available at this https URL .

---


### 77. [Two Axes of LLM Abstention: Answer Correctness and Question Answerability](https://arxiv.org/abs/2607.08456)

**<font color=#1a73e8>作者：</font>** Benedikt J. Wagner  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A model should refuse two different things: answers it would get wrong, and questions it should not answer at all, such as unanswerable ones or ones resting on a false premise. The usual recipe thresholds a single confidence score, which cannot tell these apart. Across five instruction-tuned models from three families (2B to 14B), we find they are separate axes. Ordinary answer-confidence tracks whether an answer is right but is nearly blind to whether the question is answerable; a linear probe on hidden states does the reverse. The blind spot does not shrink with scale. It is worst on naturally occurring false-premise questions (CREPE). There, answer-confidence, P(IK), P(True), and even asking the model outright whether a premise is false all stay near chance, while a hidden-state probe reaches 0.69 to 0.77 AUROC: the model represents a problem it will not report. This turns out to be fixable. Instructing a model to check premises backfires, because it then disputes sound and false premises alike (57% false challenges), unable to tell them apart; routing the same instruction with the probe roughly triples challenge precision. We turn the two axes into a calibrated policy that answers only when an answerability score and a correctness score each clear a separately certifies behave differently: the unanswerable-answer rate is controllable at every scale, while the wrong-answer rate is capped by model accuracy, so the guarantee tightens as threshold policy certifies both budgets at 0.75 coverage of correct answers, against 0.31 for a single threshold; at 14B it is the only policy that certifies at all.

---


### 78. [MatBind: A Shared Embedding Space for Multimodal Materials Characterization](https://arxiv.org/abs/2607.08470)

**<font color=#1a73e8>作者：</font>** Le Yang, Anoop K. Chandran, Jona Östreicher 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fully characterizing a crystalline material requires integrating heterogeneous data sources -- atomic structures, diffraction patterns, electronic density of states, and natural language -- each of which captures a different facet of the same physical object. In practice, however, these modalities are stored and analyzed in isolation, making it difficult to relate or query materials across representational boundaries. We present MatBind, a contrastive learning framework that aligns four materials modalities -- crystal structure, powder X-ray diffraction (pXRD) simulated from structures, density of states (DOS), and text -- into a unified embedding space using crystal structure as the central physical anchor. The framework induces alignment between modalities never explicitly paired during training, enabling emergent zero-shot cross-modal retrieval as a direct consequence of the shared representation. The learned embedding space organizes materials according to physically meaningful properties without explicit supervision, and retrieval performance improves systematically when modalities are combined at query time. These results demonstrate that treating heterogeneous materials data as complementary projections of a single physical reality, rather than as isolated data sources, is not a practical choice but is consistent with the underlying physics.

---


### 79. [Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing](https://arxiv.org/abs/2607.08497)

**<font color=#1a73e8>作者：</font>** Feng Wang, Canmiao Fu, Zhipeng Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent unified multimodal models show a single architecture can jointly perform vision/language understanding and image generation/editing. However, they repeatedly feed all historical visual and textual inputs into a shared context window, limiting long-horizon multimodal dialogue due to visual token explosion and unreliable cross-turn referencing. We propose a Cognitive-structured Multimodal Agent that externalizes visual information into an Episodic Visual Memory and selectively reactivates relevant episodes during reasoning. The agent consists of a Perceptual Abstraction Engine for structured visual abstraction, a Cognitive Retrieval Engine for cross-turn memory retrieval, and a Multimodal Executive Controller for autonomous task inference and action planning. To address the lack of turn-level retrieval supervision in existing datasets, we develop a Unified Scenario Engine that programmatically generates structured multi-turn conversations with fine-grained retrieval annotations, enabling reinforcement learning to optimize abstraction and retrieval policies. We also construct a long-horizon visual-dialogue benchmark stratified by difficulty to evaluate episodic visual recall. Our 8B agent achieves 91.4% retrieval accuracy over 20-turn sessions, surpassing 32B baselines by +8.2% while nearly halving per-turn inference time (23.1s -> 12.7s). We further present the Cognitive-structured Multimodal Agent Harness (CMA-Harness), a tool-augmented deployment of the same cognitive structure integrating persistent multimodal memory, web access, image generation/editing/composition tools, and OpenAI-compatible serving. Structured memory and modular decision-making offer a more scalable, efficient paradigm for long-horizon multimodal agents than monolithic parameter scaling. Code: this https URL ; Project page: this https URL

---


### 80. [CT-CLIP Representations for Multimodal Lung Cancer Survival Prediction](https://arxiv.org/abs/2607.08503)

**<font color=#1a73e8>作者：</font>** Sofie Allgöwer, Mikael Johansson, Andreas Hallqvist 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate prognosis prediction is important for treatment planning in lung cancer, but deep learning-driven survival modelling is often limited by the scarcity of curated imaging cohorts with reliable outcome data. This study evaluates whether representations from a domain-specific foundation model can be used for multimodal survival prediction in data-constrained clinical settings. We assess the foundation model CT-CLIP as a feature extractor for pretreatment computed tomography images and clinical variables from 242 diagnosed lung cancer patients. The evaluation includes adaptation strategies based on frozen encoders, full fine-tuning, and low-rank adaptation, together with modality ablations and comparisons with clinical and multimodal baselines. The results show that a frozen CT-CLIP model combined with a trainable lightweight survival head outperforms the clinical baseline and achieves comparable or improved performance relative to other multimodal approaches, and separates patients into clinically meaningful high- and low-risk groups.

---


### 81. [Do Egocentric Video-Language Models Capture Both Hand- and Object-Centric Cues?](https://arxiv.org/abs/2607.08514)

**<font color=#1a73e8>作者：</font>** Masatoshi Tateno, Alexandros Stergiou, Risa Shinoda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hand-object interaction (HOI) recognition requires capturing both hand manipulations and object transformations. However, existing video-language models often fall into shortcuts by relying on spurious correlations among hands, objects, or environmental context, rather than reasoning from the appearance and dynamics of hands and objects themselves. To address this limitation, we propose a new learning paradigm that combines (i) hand-object masked training, which enables robust reasoning from partial hand or object observations, and (ii) an HOI-dynamics-aware decoder that explicitly learns hand- and object-centric embeddings through auxiliary predictions of their locations and semantics, enhancing sensitivity to both cues. To systematically evaluate such cue-specific reasoning, we introduce Cue-Isolated HOI (CI-HOI), a new evaluation that assesses models' ability to predict actions from hand- and object-related cues independently. To enable CI-HOI, we curate the DEHOI testbed, which separates hand- and object-related observations for disentangled HOI evaluation through inpainting. Using DEHOI, we demonstrate both quantitatively and qualitatively that our training strategy exploits hand- and object-centric information more effectively than existing models. Our approach improves over existing models on DEHOI, standard action recognition, object state recognition, and even robot manipulation action recognition, leading to more robust HOI understanding.

---


### 82. [When the Judge Changes, So Does the Measurement: Auditing LLM-as-Judge Reliability](https://arxiv.org/abs/2607.08535)

**<font color=#1a73e8>作者：</font>** Zongyou Yang, Yinghan Hou, Xiaokun Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An LLM-as-judge score can move even when the candidate responses stay fixed, simply because the evaluator has changed. We treat this evaluator-replacement ambiguity as a measurement-validity problem. Across four judgment datasets, we compare two upgrade paths available in practice: scaling Qwen3 dense judges from 1.7B to 32B parameters and moving across MiniMax M2-M2.7 released APIs. The main pattern is that judge upgrades are not interchangeable: only Qwen3 1.7B to 4B gives a robust adjacent gain, while MiniMax adjacent releases do not. Stronger judges reduce but do not remove position and verbosity bias. Repeated-sample juries add little when errors are correlated. Structured debate can move decisions substantially, but without parser and fallback logs those shifts cannot be attributed to deliberation. We argue that LLM-as-judge reports should include dataset slices, bias probes, error-dependence estimates, and protocol audit trails.

---


### 83. [Contravariance Theory: Strong Alignment for Minimal Solutions to Hard Tasks](https://arxiv.org/abs/2607.08561)

**<font color=#1a73e8>作者：</font>** Dan Yamins, Aran Nayebi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A series of results from the NeuroAI over the past fifteen years have raised core questions both about how to compare Deep Neural Network (DNN) models to the brain, and about how much convergent evolution to expect between artificial networks and real brain networks. Here, we show that for any two minimal DNN solutions to a sufficiently hard task: (i) "weak" alignment of network representations based on affine mappings guarantees "strong" alignment of privileged axes, and (ii) alignment "zippers" up the network hierarchy, causing the emergence of privileged axes from end-to-end task optimization. These results formalize the notion of contravariance from Cao and Yamins [2024], and illustrate important consequences for the theory of NeuroAI: with sufficiently strong tasks, choice of metric for inter-network comparison is not all that sensitive, and that convergent evolution is probably inevitable.

---


### 84. [Switch-Reasoner: Learn When to Think in Multitask Mixtures via Reinforcement Learning](https://arxiv.org/abs/2607.08572)

**<font color=#1a73e8>作者：</font>** Yiyang Fang, Pei Fu, Jinjie Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) often follow a fixed Think-then-Answer paradigm, which is inefficient in heterogeneous multitask settings because simple inputs may not require explicit reasoning while difficult ones can benefit substantially from it. Learning when to think is also unstable during post-training, where imbalanced rollouts can drive the model toward always-thinking or always-direct behavior. We propose Switch-Reasoner, a GRPO-based framework that learns to adaptively select reasoning modes for MLLMs. It treats thinking as a virtual tool invocation and allows the model to either answer directly or invoke explicit reasoning before answering. To stabilize this decision, we introduce a dual-level regulation mechanism that balances the overall use of Thinking Mode and Direct Mode while providing sample-level supervision based on the relative benefit of the two choices. Experiments on 11 multimodal tasks show that Switch-Reasoner reduces unnecessary reasoning while maintaining strong performance, achieving a better accuracy-efficiency trade-off.

---


### 85. [Towards Precision Therapy in Hepatocellular Carcinoma: A Clinical-Reasoning LLM for Risk Stratification and Treatment Guidance](https://arxiv.org/abs/2607.08602)

**<font color=#1a73e8>作者：</font>** Peng Cui, Jitao Wang, Siyan Xue 等 44 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hepatocellular carcinoma (HCC) is a common malignancy and a leading cause of cancer-related mortality. Current guidelines and staging systems provide coarse categories, but often miss within-stage heterogeneity and the clinical context in electronic medical records (EMRs). We present HCC-STAR (Hepatocellular Carcinoma Staging, Treatment And pRognosis), a clinically aligned large language model that reads routine EMR narratives and jointly outputs risk score-based staging, ranked guideline-consistent treatments with evidence-based rationales, and individualized survival estimates. We curated about 30,000 HCC cases from SEER and expanded them into EMR-style narrative training data using a clinician-validated, prompt-based augmentation workflow. On this corpus, we developed a knowledge-aligned reasoning framework optimized with a step-verifiable composite reward, moving beyond text-level memorization of clinical guidelines. In a multi-center cohort of 6,668 patients from 12 hospitals in China, HCC-STAR achieved state-of-the-art performance in treatment recommendation and risk stratification compared with clinical guidelines and competitive models, including GPT-5 and Gemini-2.5 Pro. Hypothetical overall-survival analysis showed a median survival of 51 months under adherence to HCC-STAR recommendations, compared with 29 and 32 months under BCLC and CNLC. In clinician-centric evaluations, blinded hepatobiliary specialists rated HCC-STAR's reasoning and evidence-based justifications as trustworthy. The model surpassed resident and attending physicians in treatment accuracy and helped physicians make more accurate decisions faster when used as an assistant. These findings support HCC-STAR as a reliable and verifiable decision-support system for risk stratification and precision therapy in HCC.

---


### 86. [When Structured Sparse Autoencoders Learn Consistent Concepts Across Modalities](https://arxiv.org/abs/2607.08605)

**<font color=#1a73e8>作者：</font>** Weiduo Liao, Yunqiao Yang, Ying Wei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) have emerged as a promising technique for mechanistic interpretability by learning a set of sparse latent features in large models, each of which encodes a distinct concept. However, in vision-language models (VLMs), vanilla SAEs struggle to learn modality-consistent concepts, with concepts often exhibiting fragmented coverage (i.e., disjoint regions) in the visual modality. To address this challenge, we propose a Structured Sparse AutoEncoder ($S^2AE$) that enforces concept consistency from both semantic and spatial perspectives in the visual modality. Specifically, we group image patches based on Transformer attention similarity and spatial proximity, and introduce a structured sparsity regularization when training the vanilla SAE. The regularization consists of exclusive sparsity for inter-group concept disentanglement and group sparsity for intra-group concept consistency, which drives the latent neurons by SAEs to specialize in distinct, semantically grounded concepts. Evaluated on the \texttt{Qwen2.5-VL-7B-Instruct} model, the method achieves 6.06% average improvement in semantic alignment (mIoU) and 60.81 in representational efficiency (lower l0 norm) while maintaining near-perfect reconstruction fidelity with an Explained Variance above 99%. Cross-modal analysis further demonstrates that $S^2AE$ enhances neuronal monosemanticity by this visual structural prior, achieving a 3.08% average gain in semantic consistency and a 2.37% average gain in monosemanticity scores for both modalities of multimodal features, thereby fostering more coherent and disentangled representations.

---


### 87. [BiSCo-LLM: Lookup-Free Binary Spherical Coding for Extreme Low-Bit Large Language Model Compression](https://arxiv.org/abs/2607.08643)

**<font color=#1a73e8>作者：</font>** Yuantian Shao, Peisong Wang, Zhilei Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly constrained by memory capacity, weight bandwidth, and checkpoint storage during deployment. Existing low-bit compression methods mainly follow two directions. Scalar or group-wise quantization is simple and compatible with efficient low-precision kernels, but its representation capacity becomes limited when the target budget approaches 2 bits per weight. Vector-quantized weight compression provides a richer block-level representation, but usually introduces explicit codebooks, index lookup, and additional storage accounting. This paper presents BiSCo-LLM, a codebook-free binary spherical coding framework for extreme low-bit LLM weight compression. The core pipeline is built on three components. First, local weight chunks are mapped onto a unit hypersphere and binarized into compact spherical codes, so that the main payload is a bit-packed sign stream rather than explicit VQ centroids. Second, a residual BSQ stage encodes the reconstruction error left by the base spherical codec, providing an explicit rate-distortion path without stored codebooks. Third, category-wise recovery distillation is performed after replacing each Transformer module category, reducing the mismatch between local weight reconstruction and assembled model behavior. A small 8-bit protected-channel path is used as an auxiliary stabilization mechanism for sensitive channels and is counted separately from the BSQ payload. The reported storage budget includes binary codes, neural decoders, protected-channel payloads, LoRA adapters, and metadata.

---


### 88. [UltraX: Refining Pre-Training Data at Scale with Adaptive Programmatic Editing](https://arxiv.org/abs/2607.08646)

**<font color=#1a73e8>作者：</font>** Xinlong Zhao, Dongsheng Liu, Hengyu Zhao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As available training data approaches its physical limit, gains from Scaling Laws have begun to diminish. Consequently, improving Large Language Models (LLMs) now depends less on data expansion and more on higher-quality data utilization. However, in the context of large-scale corpora, existing refinement methodologies face significant limitations in quality, efficiency, and reliability: Rule-based approaches are constrained by fixed heuristics and struggle with instance-level variations; LLM-based approaches improve quality but fail to meet the efficiency and reliability requirements of large-scale data processing. To address these challenges, we propose UltraX, a function-calling refinement framework for large-scale pre-training data that completes the editing function space by introducing insertion in addition to deletion and modification, enabling fine-grained instance-level editing. Specifically, UltraX builds a reliable program-supervision generation pipeline. In this pipeline, dataset-adaptive prompt optimization first guides an expert LLM to produce high-quality end-to-end refined texts, and Line Alignment Mapping and Dynamic Context Replacement then convert original-refined text pairs into structured program supervision. Meanwhile, UltraX improves supervision quality and stabilizes the training distribution with low-confidence example filtering and ratio-controlled sampling by operation combination. During inference and execution, it normalizes and validates model outputs through sliding-window prediction, global operation aggregation, and systematic post-processing, improving the stability and reliability of large-scale execution. Experiments show that UltraX achieves the highest average performance across all corpora and also matches or surpasses baselines with fewer training tokens, demonstrating stronger data efficiency and refinement reliability.

---


### 89. [WebSwarm: Recursive Multi-Agent Orchestration for Deep-and-Wide Web Search](https://arxiv.org/abs/2607.08662)

**<font color=#1a73e8>作者：</font>** Xiaoshuai Song, Liancheng Zhang, Kangzhi Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based web search agents are transforming information seeking from simple factoid question answering into complex, deep-and-wide search and research-oriented tasks. A single ReAct-style agent is constrained by one long trajectory and limited context, making it difficult to handle depth and coverage simultaneously. Existing multi-agent systems improve search coverage through parallel execution and aggregation, but still exhibit clear limitations in recursive depth, collaboration adaptability, and evidence-grounded expansion. We propose WebSwarm, a progressive recursive delegation framework that jointly constructs task decomposition, recursive expansion, and agent collaboration during inference. WebSwarm dynamically instantiates agentic search nodes, each coupling a local objective with a search mode that specifies how the node should organize search and collaboration. Each node can either solve its objective itself or further delegate child nodes; after solving, it returns evidence and results upward, enabling parent nodes to further expand, revise, or aggregate the search process. To guide this process, WebSwarm first probes how task-relevant information is organized on the web to ground subsequent node expansion, and reuses process-level experience across homogeneous sibling nodes. Experiments on BrowseComp-Plus, WideSearch, DeepWideSearch, and GISA show that WebSwarm consistently outperforms single-agent and multi-agent baselines on deep, wide, and interleaved deep-and-wide tasks. Further analyses of ablation, task difficulty, web tool efficiency, and model generalization explain WebSwarm's effectiveness and provide insights for multi-agent search systems.

---


### 90. [Resample or Reroute? Budget-Aware Test-Time Model Selection for Large Language Models](https://arxiv.org/abs/2607.08665)

**<font color=#1a73e8>作者：</font>** Teng-Ruei Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Routing among large language models (LLMs) trades response quality against serving cost, motivated by the reported gap between deployed routers and a per-instance oracle. Recent analysis shows that test-time resampling can recover per-instance selection headroom that no single-commit router captures; however, that guarantee holds only under an idealized oracle equipped with correctness labels and an unconstrained budget, neither of which a deployed system has. To the best of our knowledge, no previous work treats resampling the committed model and rerouting to an alternative model as competing uses of a single per-query cost budget. Therefore, this work formulates budget-aware test-time model selection: given a per-query budget and an imperfect verifier, allocate each unit of budget between resampling and rerouting so that expected correctness is maximized. An online resample-or-reroute (RoR) allocation policy driven by estimated marginal correctness per unit cost is proposed, and its behavior is grounded in the recoverability asymmetry between selection and sampling. Replay experiments on newly regenerated multi-draw correctness tensors from an eleven-model open-weight pool over four benchmarks of differing difficulty show that the proposed RoR policy attains a favorable cost-quality Pareto front relative to single-route, one-commit-router, budget-aware best-of-K, cascade, and random-allocation baselines for the tested pools, with the largest gains on the most heterogeneous benchmark; an ablation further shows the gains are verifier-gated, shrinking as verifier quality degrades, and robustness replays under a provider price vector and a label-free agreement verifier delineate where the conclusions carry over.

---


### 91. [How YouTube Frames ChatGPT Use in Education: An Epistemic Network Analysis with Supporting Multimodal Metadata](https://arxiv.org/abs/2607.08698)

**<font color=#1a73e8>作者：</font>** Shayla Sharmin, Mohammad Al-Ratrout, Mohammad Fahim Abrar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We examine educational YouTube videos through multimodal metadata, such as transcripts, titles, thumbnails, and viewer comments, to investigate how ChatGPT is framed across creator groups and how those framings relate to audience response and platform reach. Little is known about how large language models are presented to learners in informal, creator-driven public discourse. Following PRISMA, we selected 52 videos for analysis. We identified three structurally distinct discourse groups: (G1) videos that positioned ChatGPT as a conceptual scaffold for thinking, (G2) videos oriented toward retrieval practice and skill-building, and (G3) videos that framed ChatGPT as a tool for output generation. Epistemic Network Analysis revealed statistically significant group differences with large effect sizes. Multimodal metadata consistently reflected these distinctions across transcript discourse, titles, and thumbnails. Viewers of learning-oriented content described ChatGPT as a thinking partner or tutor, whereas viewers of output-oriented content raised concerns about over-reliance, surface-level learning, and cognitive offloading. G3 achieved comparable platform reach to G2, yet with substantially weaker learning-oriented framing. This may suggest that output-oriented content competes for visibility despite lower pedagogical depth. These findings reveal a structural tension in self-directed AI learning: content that prioritizes quick outputs reaches far more learners than content that promotes deep engagement. This gap raises critical questions about whose vision of AI literacy scales and what learners are actually left with.

---


### 92. [Do You Need a Frontier Model as a Citation Verifier? Benchmarking Rubric LLMs for Deep-Research Source Attribution](https://arxiv.org/abs/2607.08700)

**<font color=#1a73e8>作者：</font>** Ethan Leung, Elias Lumer, Corey Feld 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning increasingly relies on an LLM judge to score each rubric criterion, and that judge acts as the reward model during training. Before such a signal can be trusted, we need to know how capable the judge must be and how biased it is. We study this calibration question for citation quality in deep-research systems, where a search-grounded LLM must support each claim it writes with a cited source. Citation quality is a structured rubric task in which each attribution-citation pair is judged along two dimensions that require an LLM, source relevance and factual support. On an adversarial long-form benchmark, we score 8 off-the-shelf LLM judges from 3 model families against gold labels over 1,248 rubric decisions, all of which were human-reviewed and 378 of which were hard cases adjudicated from judge disagreements. Cheaper judges remain competitive across both dimensions, with GPT-5-mini attaining the strongest source-relevance pass-class F1 at 0.908 ($\kappa$=0.636), while on factual support the judges are statistically indistinguishable (overlapping confidence intervals), so no single model dominates. At comparable F1, the judges still differ substantially in pass-rate drift, false positive rate, and false negative rate. Scalar F1 obscures this directional bias, yet it is exactly what a downstream reinforcement learning loop would reinforce. Calibrating the judge is therefore a prerequisite for using citation rubrics as reward signals, and our results show that this calibration does not require the most expensive available model.

---


### 93. [Validity of LLMs as data annotators: AMALIA on authority](https://arxiv.org/abs/2607.08731)

**<font color=#1a73e8>作者：</font>** Manuel Pita  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A national language model offers a linguistic community its own instrument for measuring what its citizens say and value. Portugal's AMALIA, a publicly funded 9B-parameter model for European Portuguese, appears competitive on agreement alone: asked to code the moral foundation of authority, it agrees with trained human coders to within six F1 points of open models eight to thirteen times its size. Yet agreement is reliability, not validity. For theoretical constructs that must be inferred rather than read from surface features, the question is whether the model follows the construct's theory or reaches the right code by correlated shortcuts. We test this with the recovery gap: the loss in performance when a holistic prompt is decomposed into the codebook's atomic clauses and recombined by the theory's explicit rule. If calibration closes that gap, some portability should survive across models and languages; where it does not, the construct-model instrument is the likely locus of failure. We ask whether a calibrated English instrument transfers to AMALIA-9B and to European Portuguese. For one construct and one corpus, it does not. Decomposition recovers only about half of AMALIA's holistic performance, and error analysis suggests reliance on surface correlates, especially moral outrage near authority figures. An open multilingual LLM closes the gap on the same Portuguese corpus under the same instructions, pointing away from the corpus as the main explanation. AMALIA can still screen and pre-code at scale, but it cannot yet measure this construct well enough to stand alone. The study is a single counterexample, not a verdict on national models; it argues that sovereign-LLM benchmark batteries should test not only agreement with human coders, but the evidential route by which that agreement is warranted.

---


### 94. [Super Weights in LLMs and the Failure of Selective Training](https://arxiv.org/abs/2607.08733)

**<font color=#1a73e8>作者：</font>** Shreyas Subramanian, Adewale Akinfaderin, Akarsha Sehwag  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work identified Super Weights, individual parameters whose removal degrades model performance by orders of magnitude. We show that this degradation due to pruning Super Weights does not universally apply to all LLMs. Furthermore, if these parameters are so important, Super Weight-aware training should be effective. We show the opposite. Training Super Weights in isolation (100 to 8,192 parameters) drops accuracy to random-guessing levels on both OLMo-1B and OLMo-7B, and expanding to local neighborhoods of up to 36K parameters provides no improvement. The failure is specific to Super Weight coordinates: training an equal number of randomly chosen positions in the same down_proj layers instead improves over the baseline, so the collapse comes from targeting Super Weights, not from sparsity itself. Vanilla LoRA, updating every position in attention weight matrices through low-rank structure, succeeds with only 0.16% of parameters, and applying the same low-rank update to down_proj succeeds as well. A 10-seed ablation confirms that constraining LoRA updates at positions corresponding to Super Weight coordinates yields statistically indistinguishable results. These findings establish that parameter importance does not imply parameter trainability in isolation, and that effective fine-tuning relies on structured decompositions over entire layers rather than targeting individually important weights.

---


### 95. [The Illusion of Equivalency: Statistical Characterization of Quantization Effects in LLMs](https://arxiv.org/abs/2607.08734)

**<font color=#1a73e8>作者：</font>** Baha Rababah, Cuneyt Gurcan Akcora, Carson K. Leung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training quantization is widely used to deploy large language models in resource-constrained settings, yet its evaluation relies almost exclusively on accuracy and perplexity. We show that these metrics fail to capture behavioral changes induced by quantization. We introduce correctness agreement, a decision-level metric that measures overlap in correct predictions between a base model and its quantized variants, independent of absolute accuracy. Across multiple models and quantization schemes from 8-bit to 2-bit, we find that behavioral divergence emerges under moderate quantization even when task performance appears preserved. To explain this effect, we analyze quantization as a structural operator on attention weights and quantify layer-wise distortions using statistical and distributional measures. Our results reveal non-linear breakpoints at low bit-widths and show that query and key projections are consistently more sensitive than value and output projections. These findings expose an illusion of equivalence between base and quantized models and motivate behavioral evaluation beyond conventional performance metrics.

---


### 96. [Workflow as Knowledge: Semantic Persistence for LLM-Mediated Workflows](https://arxiv.org/abs/2607.08740)

**<font color=#1a73e8>作者：</font>** Emanuele Quinto, Carlo Andrea Rozzi, Francesco Zanitti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) applications increasingly use explicit workflows for tool use, retrieval, branching, checkpointing, and human approval. Existing workflow systems already address many execution concerns. This paper proposes a Lisp-inspired but language-independent conceptual model: symbolic forms, object identity, and live-image thinking are used as explanatory lenses, not implementation commitments. In this model, workflow definitions, workflow instances, inference records, context snapshots, and dependency relations are represented as persistent knowledge objects in a shared knowledge substrate. Its central semantic distinction is between derive and infer: derive is deterministic computation over available state; infer is mediated LLM judgment under declared context and executor-controlled capability policy.
The result is a preliminary conceptual account of semantic persistence: workflows do not merely produce knowledge and leave traces, but can themselves be represented as inspectable, resumable, and reviewable knowledge objects, while formal transition semantics remain future work.

---


### 97. [AUTOPILOT VQA: Benchmarking Vision-Language Models for Incident-Centric Dashcam Understanding](https://arxiv.org/abs/2607.08745)

**<font color=#1a73e8>作者：</font>** Siddharth Damodharan, Radhika Gupta, Ali Alshami 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Vision-Language Models, Large Language Models, and Multimodal Large Language Models have improved autonomous driving tasks such as scene understanding, decision making, trajectory prediction, and visual question answering. However, evaluating whether these models can reliably reason about safety-critical incidents remains challenging. To address this gap, we present AUTOPILOT-VQA, an incident-centric visual question answering benchmark for dashcam video understanding. The dataset evaluates different systems through structured questions designed around real-world driving incidents and near-incidents. The benchmark covers diverse safety-relevant categories, including weather and lighting conditions, traffic environment, road layout, road surface state, signage, involved entities, accident occurrence, impact location, and avoidability-related reasoning. By requiring models to answer grounded questions about both contextual scene properties and event-level incident details, AUTOPILOT-VQA moves beyond object recognition toward temporally grounded, safety-aware reasoning. The dataset is released as part of the AUTOPILOT CVPR 2026 competition and provides a standardized benchmark for assessing the reliability of autonomous driving systems in different scenarios. Our benchmark support developments for more interpretable, robust, and safety-conscious vision-language systems for real-world autonomous driving.

---


### 98. [OPSD-V: On-Policy Self-Distillation for Post-Training Few-Step Autoregressive Video Generators](https://arxiv.org/abs/2607.08766)

**<font color=#1a73e8>作者：</font>** Hongyu Liu, Chun Wang, Feng Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose OPSD-V, an on-policy self-distillation paradigm for post-training few-step autoregressive (AR) video diffusion models. Existing few-step AR video generators can produce long videos with low latency, but still suffer from error accumulation and weakened motion dynamics during long autoregressive rollout. OPSD-V reduces long-horizon degradation while preserving the original few-step inference path. The key idea is to introduce real long-video data as temporal context during training and use it to provide dense trajectory-level supervision. Specifically, the student follows the exact inference-time rollout, generating each chunk conditioned on its own previously generated KV cache. In parallel, the teacher is evaluated at the same student-visited denoising states, but uses a cleaner AR-consistent temporal cache in which older history can be replaced by real-video context. This provides dense denoising-level corrective targets under on-policy AR cache dynamics, without changing the sampler, number of denoising steps, or inference-time cache mechanism. We apply OPSD-V to representative few-step AR video models, including Self-Forcing and LongLive. Experiments show consistent improvements in visual quality, motion dynamics, and VBenchLong scores. A user study with 10 participants comparing 20 video pairs shows that OPSD-V is preferred over the base models in 66.0% of overall-preference judgments (82.5% excluding ties).

---


### 99. [UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks](https://arxiv.org/abs/2607.08768)

**<font color=#1a73e8>作者：</font>** Zhekai Chen, Chengqi Duan, Kaiyue Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid development of large language models and multimodal large language models has accelerated the emergence of proactive agents capable of operating everyday tools and assisting users in real-world environments. However, existing benchmarks struggle to evaluate such agents effectively, as they often rely on sandboxed environments and single-turn evaluation paradigms. Moreover, their scenario-based task taxonomies mix multiple model capabilities within the same task category, making it difficult to identify the root causes of agent failures. To address these limitations, we introduce UniClawBench, the first capability-driven benchmark designed to evaluate proactive agents in dynamic, real-world settings. UniClawBench is built around five foundational model capabilities: Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, and Cross-Platform Coordination. Based on these capabilities, we design 400 bilingual real-world tasks. Unlike previous benchmarks that rely on static, pre-recorded answers, our benchmark evaluates agents in live Docker containers using fine-grained, step-by-step completion checkpoints. Furthermore, we design a closed-loop evaluation strategy comprising an executor agent, a hidden supervisor agent, and a user agent to simulate realistic multi-turn human feedback without leaking grading criteria. To disentangle base model capabilities from framework-level design choices, we evaluate state-of-the-art models under multiple agent frameworks. Through comprehensive comparisons across both models and frameworks, we show how base model capabilities and agent framework designs jointly shape performance in real-world environments. To facilitate future research, we make our benchmark and code publicly available at this https URL.

---


> [!TIP]
> 当前位于：**51-99**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-99**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
