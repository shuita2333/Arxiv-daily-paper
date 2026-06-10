# 🧠 大模型相关研究 | 2026年06月11日

> 本类共 **188** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-188](./part-04.md)

---

### 101. [ActiveMem: Distributed Active Memory for Long-Horizon LLM Reasoning](https://arxiv.org/abs/2606.10532)

**<font color=#1a73e8>作者：</font>** Yunhan Jiang, Wenbin Duan, Shasha Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory is essential for enabling large language model (LLM) agents to handle long-horizon reasoning tasks. Existing memory mechanisms are largely centralized, typically organizing retrieved information and interaction history within a single model context. This design imposes a fundamental trade-off: scaling reasoning trajectories risks context overload, whereas aggressive content pruning may result in irreversible information loss. Seeking a better trade-off, we draw inspiration from human cognitive systems, especially the functional complementarity between the prefrontal cortex (executive control) and the hippocampus (memory management), suggesting that such a trade-off need not be inherent, but may instead stem from centralized memory organization. To this end, we propose ActiveMem, a heterogeneous framework that decouples agent memory from the core reasoning process. Specifically, a high-level Planner utilizes distilled semantic gists to execute reasoning, while a lightweight, distributed memory system operates in parallel to actively accumulate and consolidate these gists throughout the task. Experiments on BrowseComp-Plus and GAIA show that ActiveMem achieves state-of-the-art accuracy with significantly reduced overhead, demonstrating the effectiveness of distributed active memory for long-horizon reasoning.

---


### 102. [Prefilling-dLLM: Predictive Prefilling for Long-Context Inference in Diffusion Language Models](https://arxiv.org/abs/2606.10537)

**<font color=#1a73e8>作者：</font>** Jing Xiong, Qi Han, Shansan Gong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) re-encode the entire prefix at every denoising step, causing recomputation that scales
quadratically with context length and becomes prohibitive for long-context scenarios. We propose Prefilling-dLLM, a training-free
prefill-decode disaggregation framework for dLLMs that partitions the prefix into N chunks, caches their KV representations once,
and selects the top-K most relevant chunks with intra-chunk token sparsity for decoding, showing that sparse prefilling can
outperform dense attention while reducing per-step complexity from quadratic in the full sequence length to quadratic only in the
decode length. On LongBench and InfiniteBench, Prefilling-dLLM achieves state-of-the-art quality among dLLM acceleration methods,
and an attention kernel that parallelizes decoding over the non-contiguously cached chunk KV yields 9.1--28.0x speedup at 8K--32K
contexts. We further show that beginning-of-sequence tokens prepended to each chunk act as periodic attention anchors that eliminate
the lost-in-the-middle phenomenon. Code is available at this https URL.

---


### 103. [SkillAxe: Sharpening LLM-Authored Agent Skills Through Evaluation-Guided Self-Refinement](https://arxiv.org/abs/2606.10546)

**<font color=#1a73e8>作者：</font>** Srishti Gautam, Arjun Radhakrishna, Sumit Gulwani  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Skill documents, structured natural-language instructions that guide Large Language Model (LLM) agents, are critical to modern agent frameworks, yet LLMs struggle to write skills that actually work. On SkillsBench, human-authored skills improve pass rates by 16.2 percentage points, while LLM-authored skills provide no measurable gain. We introduce SkillAxe, a fully unsupervised framework that enables LLMs to iteratively diagnose and refine their own skills. SkillAxe decomposes skill quality into four interpretable dimensions (quality impact, trigger precision, instruction compliance with fault attribution, and solution-path coverage), producing structured improvement briefs that require no ground-truth labels, test suites, or environment rewards. On SkillsBench, SkillAxe improves pass rates by 28\% relative over unimproved LLM skills and closes 47--67\% of the gap to human-authored skills. We validate the approach as a continuous improvement engine in the wild on SpreadsheetBench, where a SkillAxe-built skill library learns from past agent trajectories and raises pass rate from 16.0\% to 52.0\% using only 22 skills.

---


### 104. [Improving Adversarial Transferability on Vision-Language Pre-training Models via Surrogate-Specific Bias Correction](https://arxiv.org/abs/2606.10571)

**<font color=#1a73e8>作者：</font>** Lijia Yu, Jiuxin Cao, Yuchen Qiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial examples reveal vulnerabilities in Vision-Language Pre-training (VLP) models and provide insights for improving robustness. A key property is cross-model transferability, which enables transfer-based black-box attacks. However, existing attacks often rely heavily on the surrogate model, causing cross-model performance drops. One reason is that adversarial optimization may follow surrogate model responses more than input semantics, making the update direction effective on the surrogate but less transferable to unseen targets. We refer to this dependency as surrogate-specific bias. Motivated by this observation, DeBias-Attack improves transferability by correcting surrogate-specific bias in adversarial optimization directions. It maintains two perturbation branches. The main branch optimizes a perturbation on the original image and obtains the adversarial gradient used to disrupt image-text alignment. The reference branch optimizes a perturbation on a weak-semantic image constructed from the dataset mean image with small Gaussian noise resampled at each iteration. Since this weak-semantic image contains little clear visual content, its optimization reflects surrogate responses more than image semantics, and its reference gradient estimates surrogate-specific bias. DeBias-Attack removes the aligned projection of the main gradient on the reference gradient before updating the adversarial image, then performs context-aware text substitution using the updated adversarial image. DeBias-Attack is the first transfer-based VLP attack that corrects surrogate-specific bias through gradient correction. Experiments show strong performance across VLP models, downstream tasks, and open-source and closed-source multimodal large language models.

---


### 105. [One Token per Multimodal Evidence: Latent Memory for Resource-Constrained QA](https://arxiv.org/abs/2606.10572)

**<font color=#1a73e8>作者：</font>** Zhi Zheng, Ziqiao Meng, Hao Luan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> External memory effectively grounds large language models (LLMs) and vision-language models (VLMs)-based question answering (QA) in relevant multimodal evidence. However, existing memory paradigms represent each memory item in raw text and image forms, so retrieval-based systems must pass the retrieved text or images to the generation LLMs/VLMs, resulting in high token consumption and storage pressure, making it unaffordable for resource-constrained applications. We propose Latent Memory, a latent-space memory paradigm that replaces each raw text or image evidence item with a single high-dimensional latent token produced by a small compressor LLM/VLM. Rather than retrieving raw evidence for generation, Latent Memory operates in a unified latent representation space: the query is embedded into this space to retrieve relevant latent tokens, and the retrieved latent tokens are directly prompted to a pretrained LLM or VLM for answer generation. To make each latent token simultaneously informative for reconstruction, retrieval, and generation, we train the compressor with reconstruction, contrastive, and distillation objectives in a unified end-to-end manner. Latent Memory is evaluated on seven text-only QA benchmarks (e.g., HotpotQA) and multimodal QA benchmarks, where it achieves competitive QA performance compared to advanced RAG baselines while consuming 3x to 10x fewer generator tokens. It can also deliver the strongest image-grounded QA performance on WebQA. Code is available at this https URL.

---


### 106. [ParaBridge: Bridging Paralinguistic Perception and Dialogue Behavior in Speech Language Models](https://arxiv.org/abs/2606.10581)

**<font color=#1a73e8>作者：</font>** Yuxiang Wang, Qinke Ni, Shengbo Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech carries more information than just words: a child's voice, a fearful tone, or a noisy background should all lead a sufficiently competent spoken-dialogue assistant to different replies. Current Speech Language Models (SLMs) can recognize such paralinguistic cues but often ignore them in open-ended dialogue. We observe that a simple paralinguistic instruction scaffold at the inference stage narrows this perception-behavior gap, suggesting that the relevant cues are already latent in the model. Such scaffolds, however, remain brittle under multi-turn context and competing instructions. Therefore, we propose \textbf{ParaBridge}, an on-policy self-distillation method that turns a brittle inference-time scaffold into stable model behavior. During training, the scaffold serves only as a temporary privileged view; the scaffold-free model rolls out its own response, while the scaffolded view supplies dense, full-vocabulary next-token targets along its trajectory. This supervision teaches when non-lexical cues should affect the reply without the need for curated dialogues, human labels, or external reward models. On Qwen3-Omni-thinking, ParaBridge raises scaffold-free VoxSafeBench SAR from $14.6\%$ to $40.3\%$ and improves EchoMind average rating from $3.27$ to $3.92$. It also preserves general ability, with MMAU-Pro, VoiceBench, and GPQA all within $0.4$ points of the original model. Beyond the training distribution, ParaBridge generalizes to unseen paralinguistic cues, transfers from safety-oriented training to empathy-oriented dialogue, and works on a different SLM backbone.

---


### 107. [Towards Diverse Scientific Hypothesis Search with Large Language Models](https://arxiv.org/abs/2606.10587)

**<font color=#1a73e8>作者：</font>** Haorui Wang, Parshin Shojaee, Kazem Meidani 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are on the rise for accelerating scientific discovery, most recently in advanced tasks such as generating valid scientific hypotheses. Yet in many discovery settings, the goal is not to identify a single best hypothesis since validation can be noisy and expensive, and scientists benefit from a set of high-quality alternative hypotheses that hedge against downstream uncertainty for the best solutions. Nevertheless, commonly used evolutionary search recipes tend to prioritize optimization over exploration in hypothesis generation, and the resulting selection pressure during the search process leads to diversity collapse. Motivated by these limitations, we formulate hypothesis search as a sampling problem, where the objective is to efficiently produce diverse, high-quality hypotheses under a fixed validation budget. Building on this perspective, we propose \ours, an evolutionary framework inspired by the classical parallel tempering algorithm that searches hypotheses at multiple temperature levels and enables principled information exchange across temperatures to improve exploration without disrupting convergence. Across domains including molecular discovery, equation discovery, and algorithm discovery, our approach consistently improves both hypothesis quality and diversity under the same validation budget, and produces candidates that remain robust under more expensive downstream computational validations.

---


### 108. [Segment and Select: Vision-Language Segmentation in 3D Scenarios](https://arxiv.org/abs/2606.10594)

**<font color=#1a73e8>作者：</font>** Yulin Chen, Zhihang Zhong, Yuenan Hou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D vision-language segmentation aims to segment target objects in 3D scenarios according to the linguistic instructions and visual observations. Prior art heavily relies on the coarse superpoint representation to reduce the computation complexity, which suffers from poor segmentation quality and messy object boundaries. In this paper, we propose the SEGment-And-select (SEGA3D) paradigm for 3D visionlanguage segmentation that directly operates on the fine-grained visual information and is free from the superpoint dependency. Specifically, we first leverage a mask candidate generator to provide fine-grained categorical mask candidates, substantially improving the quality of candidate masks over the superpoint counterparts. Then, a Large Language Model (LLM) is utilized to generate the semantic and spatial information based on the linguistic description and visual features. The LLM output and visual features are fed to the Semantic-Spatial Selector (SSS) to produce the top-ranking mask candidates. Eventually, the Loopback Verification Module (LVM) is designed to yield the segmentation mask from the selected candidate masks. Our SEGA3D attains competitive performance on ScanRefer, ScanNet and Matterport3D benchmarks. Notably, our SEGA3D surpasses the top-performing counterpart by 8.3 mIoU and 5.3 mIoU on ScanNet and Matterport3D, respectively. Codes will be available upon publication.

---


### 109. [Globally Localizing Lunar Rover in Pixels via Graph Alignment](https://arxiv.org/abs/2606.10602)

**<font color=#1a73e8>作者：</font>** Mao Chen, Xu Yang, Chuankai Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise rover localization is a prerequisite for autonomous lunar exploration, yet the absence of Global Navigation Satellite System (GNSS) signals and the cumulative drift of local localization methods severely constrain long-range missions. Cross-view localization provides a promising drift-free global solution by matching rover-view and satellite-view imagery. However, the lunar environment poses unique challenges for correspondence alignment, including inter-entity entanglement, inter-viewpoint divergence, and simulation-to-real domain shift. To address these challenges, we propose Warped Alignment of Reprojected Graphs (WARG), a framework that leverages unified graph learning and reprojected graph matching for robust cross-view alignment. Pretrained on the synthetic LuSNAR dataset, WARG achieves an average test error of 0.32 m and demonstrates robust zero-shot generalization to the synthetic lunar south pole region with an error of 3.63 m. More importantly, when validated on real-world data from the YuTu-2 rover, WARG achieves a localization error of 1.68 m within a 100 m x 100 m search area, corresponding to nearly one-pixel precision in low-resolution satellite imagery with a spatial resolution of 1.40 m/pixel. Beyond accuracy, WARG is computationally efficient, containing only 1.56M parameters, corresponding to 16.12% of previous lightweight models, and operating at 5.49 Hz on an NVIDIA RTX A6000 GPU, approaching GNSS-level update frequency. Finally, we observe that WARG naturally develops low-level spatial awareness, including semantic segmentation and structural reasoning, through cross-view localization learning, highlighting its potential as a promising paradigm for spatial intelligence with minimal annotation cost. The source code is available at this https URL.

---


### 110. [Causal Ensemble Agent: Hierarchical Causal Discovery with LLM-guided Expert Reweighting](https://arxiv.org/abs/2606.10607)

**<font color=#1a73e8>作者：</font>** Xinyu Li, Yuanyuan Wang, Haoxuan Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery aims to uncover causal structures from observational data, which is crucial for real-world decision-making. However, different causal discovery algorithms can produce divergent results that conflict with each other, complicating the identification of accurate causal graphs. Traditional approaches rely on numerical values and statistical assumptions, often ignoring rich domain-specific information, such as feature descriptions, which could also help structure learning. While recent works explore using Large Language Models (LLMs) to infer causal relations via direct queries, such methods can be unreliable due to a lack of alignment with the actual data. To address these limitations, we propose Causal Ensemble Agent (CEA), a novel framework that aggregates structural insights from statistical discovery experts across different graph levels via linear opinion pooling, and uses an LLM as a meta-referee to dynamically reweight experts when the aggregated confidence is close to the decision boundary, thereby composing an improved and more complete causal graph. Extensive experiments on both synthetic and real-world datasets demonstrate that CEA achieves the strongest overall performance across a wide range of causal discovery methods, highlighting the effectiveness of using LLMs for meta-analysis in causal discovery.

---


### 111. [Small Data, Big Noise: Adversarial Training for Robust Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2606.10610)

**<font color=#1a73e8>作者：</font>** Eitan Cohen, Idan Simai, Uri Shaham  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parameter-Efficient Fine-Tuning (PEFT) has become essential for adapting foundation models to downstream NLP tasks. However, current PEFT methods often struggle with robustness to noise and performance degradation on limited training data. We propose SDBN (Small Data Big Noise), a unified framework that brings adversarial training to PEFT - a combination that remains less studied in the PEFT setting despite its complementary strengths - to enhance model robustness and generalization, outperforming alternative approaches. We also introduce two variants of the method that use discrete uncertainty sets: SDBN-h, which enumerates character-level edits and selects worst-case variants using gradients, and SDBN-p, which uses LLM-generated variants for robust optimization in generative tasks. Experiments across multiple benchmarks reveal substantial improvements, particularly in low-resource settings and under both word-level and character-level corruptions. This framework addresses the less explored intersection of adversarial training and parameter-efficient adaptation, without introducing additional parameters or only modest computational overhead, making PEFT deployments more reliable in real-world scenarios where data scarcity and linguistic variability often coexist

---


### 112. [GaussTrace: Provenance Analysis of 3D Gaussian Splatting Models with Evidence-based LLM Reasoning](https://arxiv.org/abs/2606.10612)

**<font color=#1a73e8>作者：</font>** Haoliang Han, Ziyuan Luo, Renjie Wan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) is a powerful technique for creating high-fidelity 3D assets. However, the widespread sharing and iterative modification of 3DGS models across digital platforms create pressing challenges for intellectual property protection and forensic traceability. To address this, we propose GaussTrace, a novel framework for constructing directed provenance graphs for 3DGS models. GaussTrace formulates provenance analysis as an evidence-based reasoning problem. It builds upon attribute-wise statistical profiling of 3DGS parameters to capture intrinsic properties. Moreover, we introduce hypothesis-driven editing simulations of common operations to provide auxiliary evidence for plausible transformation pathways. These statistical and simulated cues jointly enable a Large Language Model (LLM) to perform structured Chain-of-Thought (CoT) reasoning, yielding directional provenance inferences and explainable edge reasons. Experimental results demonstrate that GaussTrace effectively constructs evolutionary relationships among diverse 3DGS models, delivering accurate, interpretable, and robust provenance graphs without requiring model training or access to editing histories. Project page: this https URL.

---


### 113. [Can Image Models Imagine Time? ImageTime: A Novel Benchmark for Probing Visual World Modeling Through Spatiotemporal Consistency](https://arxiv.org/abs/2606.10620)

**<font color=#1a73e8>作者：</font>** Xinrui Wu, Lichen Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image generation models now produce high-quality static images, yet their ability to represent how a visual world changes over time remains poorly understood. Practical workflows such as storyboarding, step-by-step illustration, reference-guided editing, and video previsualization require models to preserve identities, objects, spatial relations, and causal order across multiple visual states. Existing evaluations largely measure single-image correctness, compositional alignment, or video quality, leaving open whether an image model can coherently imagine a temporally ordered process. We introduce ImageTime, a diagnostic benchmark that uses spatiotemporal consistency as a behavioral probe of visual world modeling in image generation. Given an action instruction, and optionally a reference image specifying the initial state, a model must generate one image containing four ordered key states: initial state, action onset, transition state, and final state. This four-keyframe protocol is more temporally demanding than single-image generation while avoiding the confounds of dense video dynamics. ImageTime organizes tasks with a progressive capability hierarchy and decomposes each scenario into stage-wise state predicates, cross-frame temporal constraints, and forbidden causal violations. GPT-5.5 scores all generated images under a structured VLM-as-judge protocol, producing interpretable capability scores, diagnostic subscores, and failure labels. Through multi-family benchmarking, ImageTime reveals where current image generation systems succeed, fail, and drift when asked to maintain coherent visual world states over time.

---


### 114. [Leveraging Metric Depth for Relative Depth Prediction](https://arxiv.org/abs/2606.10628)

**<font color=#1a73e8>作者：</font>** Xiaoyang Bi, Shuaikun Liu, Zhaohong Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present our solution to the 2025 SoccerNet Monocular Depth Estimation Competition Challenge. Predicting the relative depth in football scenarios is challenging, especially with only thousands of training samples available. To address this issue, our method leverages the powerful zero-shot capabilities of models pretrained on large-scale datasets to learn metric depth for effective relative depth prediction, achieving a score of $2.68 \times 10^{-3}$ on the challenge set.

---


### 115. [How Does Reasoning Flow? Tracing Attention-Induced Information Flow for Targeted RL in LLMs](https://arxiv.org/abs/2606.10646)

**<font color=#1a73e8>作者：</font>** Zhichen Dong, Yang Li, Yuhan Sun 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Token-level credit assignment remains a key obstacle for reinforcement learning (RL) in large language models (LLMs), where RL recipes typically treat all tokens equally, failing to distinguish decisive reasoning steps from routine formatting or fluent filler. Recent attempts leverage model-internal signals to assign finer-grained credit, but these are often point-wise heuristics that ignore the global structure of information propagation. We propose FlowTracer, an RL framework that traces answer-targeted reasoning flow on an attention-induced directed acyclic graph in which nodes correspond to tokens and edge capacities come from aggregated attention weights and derives token credit from this global structure. The edge capacities are reweighted to retain only the influence that can reach the answer region, while enforcing local flow conservation so intermediate tokens neither lose nor gain effective mass due to path length or irrelevant branches. On this graph, FlowTracer extracts an information-flow backbone connecting the question to the answer and scores tokens by flow throughput, revealing high-impact hubs and aggregation checkpoints that mediate long-range dependencies. These derived importances are used to shape token-level rewards, enabling learning signals to focus precisely on the tokens that route information toward (or away from) correct answers and delivering consistent performance gains across a range of reasoning tasks.

---


### 116. [Kwai Keye-VL-2.0 Technical Report](https://arxiv.org/abs/2606.10651)

**<font color=#1a73e8>作者：</font>** Kwai Keye Team, Bin Wen, Changyi Liu 等 53 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Kwai Keye-VL-2.0-30B-A3B, an open-source Mixture-of-Experts (MoE) multimodal foundation model designed to advance long-video understanding and agentic intelligence. To address the challenges of ultra-long contexts, information redundancy, and prohibitive computational costs inherent in hour-level videos, Keye-VL-2.0 is the first to adapt DeepSeek Sparse Attention (DSA) to GQA-based multimodal architectures, enabling lossless 256K context processing while capturing critical frames and long-range temporal dependencies. This architecture is underpinned by a highly optimized training and inference infrastructure, including scalable video I/O, heterogeneous ViT-LM parallelism, and custom DSA kernels that significantly maximize throughput and minimize computational overhead. Furthermore, to overcome the algorithmic dilemma of catastrophic forgetting during multi-task alignment, we introduce Cross-Modal Multi-Teacher On-Policy Distillation (MOPD) paired with Context-RL and Video-RL. By distilling dense token-level teacher feedback from on-policy rollouts back into the MoE backbone, which activates only 3B parameters, Keye-VL-2.0 natively empowers advanced agent collaboration across Code, Tool, and Search scenarios with multimodal self-correction. Extensive evaluations across video understanding, temporal grounding, reasoning, STEM, and agent benchmarks demonstrate that Keye-VL-2.0-30B-A3B achieves state-of-the-art performance among models of similar scale, particularly excelling in fine-grained temporal localization on TimeLens and long-video comprehension on Video-MME-v2 and LongVideoBench. We release our model checkpoints to accelerate community progress toward scalable and robust multimodal agentic applications.

---


### 117. [STEDiff: Strengthening Text Embedding for Text-to-Image Alignment in Diffusion Model](https://arxiv.org/abs/2606.10653)

**<font color=#1a73e8>作者：</font>** Hailan Zhang, Haipeng Liu, Bo Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although pretrained text-to-image (T2I) generation models can produce high-quality images, they often fail to faithfully reflect the semantic intent of complex prompts due to stochastic noise and inherent model limitations. This issue frequently manifests as the model overlooking specific objects or failing to correctly bind attributes to their corresponding entities, a challenge referred to as semantic alignment. Unlike existing approaches that rely on computationally expensive fine-tuning or labor-intensive layout priors, we propose STEDiff, a training-free method designed to enhance semantic representations directly within the text-embedding space. Specifically, we introduce a method that primarily leverages the [EOT] token to strengthen the relevant semantics of sub-sentences and then replaces the corresponding tokens in the original prompt. Furthermore, a novel semantic enhancement loss is incorporated to enforce spatial constraints, ensuring that the semantics of each entity are precisely mapped to their respective image regions. Extensive quantitative and qualitative evaluations on the T2I-CompBench demonstrate that our method notably improves semantic consistency and generation integrity in complex scenarios.

---


### 118. [Multilingual Word-Level Forced Alignment with Self-Supervised Representations and Learned Dynamic Programming](https://arxiv.org/abs/2606.10675)

**<font color=#1a73e8>作者：</font>** Roy Weber, Meidan Zehavi, Rotem Rousso 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a method for accurate multilingual word-level forced alignment, consisting of an alignment encoder and a learned alignment decoder. The encoder integrates two representations: one from the Massively Multilingual Speech (MMS) model and another from a self-supervised phoneme boundary detector (UnSupSeg). It learns to fuse them and to estimate word-boundary probabilities over long temporal contexts. The alignment decoder is a learned dynamic programming that combines encoder outputs with segmental features over the MMS and UnSupSeg representations to infer final word boundaries. Trained iteratively on TIMIT and Buckeye, the proposed approach outperforms Montreal Forced Aligner (MFA) and MMS-based alignment on both datasets. On unseen languages (Dutch, German, and Hebrew), the proposed model achieves performance consistently better than or on par with existing alignment approaches, indicating its potential to scale to 1100+ languages supported by MMS without further training.

---


### 119. [Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory](https://arxiv.org/abs/2606.10677)

**<font color=#1a73e8>作者：</font>** Suozhao Ji, Baodong Wu, Zehao Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term LLM agents need persistent memory that can track changing facts and provide relevant evidence across sessions. Existing memory systems often store observations as isolated records, summaries, or indexed fragments, which makes evidence aggregation, fact revision, and memory maintenance difficult. We propose Infini Memory, a maintainable text-based persistent memory architecture that treats agent memory as topic-structured documents. Each topic document serves as a semantic unit for collecting related evidence, preserving metadata, and revising facts over time. New observations are first staged in a buffer and periodically consolidated into coherent textual contexts. At inference time, an agentic retrieval procedure lets the LLM read memory through iterative tool calls rather than a single retrieval step. On MemoryAgentBench, Infini Memory achieves 64.7% overall score. Ablations show that topic-structured maintenance and iterative evidence inspection improve complementary aspects of long-term memory use.

---


### 120. [Divide and Cooperate: Role-Decomposed Multi-Agent LLM Training with Cross-Agent Learning Signals](https://arxiv.org/abs/2606.10684)

**<font color=#1a73e8>作者：</font>** Jaewan Park, Solbee Cho, Jay-Yoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern language agents which perform multi-step reasoning have shown strong performance in knowledge-intensive question answering. However, existing approaches typically couple evidence acquisition and answer generation within a single policy. This forces a single model to play multiple potentially conflicting roles, inducing a combinatorial explosion in the policy space and hindering efficient exploration. It also introduces a credit assignment problem during training: a search action that retrieves sufficient evidence may still be penalized when generation fails, and vice versa. We propose DAC (Divide and Cooperate), a role-decomposed multi-agent training framework that divides agentic search into two cooperative subtasks, each handled by a dedicated agent trained with role-specific learning signals. The generator serves a dual role as both an answer producer and an evidence sufficiency verifier, abstaining when retrieved evidence is insufficient. This abstention signal is incorporated into the search agent's reward, providing structured cross-agent learning signals that improve credit assignment. Conversely, the searcher exposes the generator to diverse and challenging evidence environments by hard-positive evidence augmentation, improving its robustness. Experiments on general and multi-hop QA benchmarks show that DAC, implemented via parameter-efficient LoRA modules over a shared backbone, achieves strong performance against prior baselines that rely on full fine-tuning of monolithic models.

---


### 121. [REAL: A Reasoning-Enhanced Graph Framework for Long-Term Memory Management of LLMs](https://arxiv.org/abs/2606.10694)

**<font color=#1a73e8>作者：</font>** Keer Lu, Liwei Chen, Guoqing Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly expected to interact with users over long time horizons. However, due to their finite context window, LLMs cannot retain all past interactions, making long-term memory management essential for storing, updating, and retrieving historical information beyond the context limit. Although recent memory systems attempt to address this issue by storing historical information externally, existing approaches suffer from three key limitations: flat text-based memory organizations fail to capture explicit relations among memories, structured memory systems often destructively overwrite evolving facts, and current retrieval mechanisms remain query-agnostic and passive when evidence is incomplete. REAL constructs long-term conversational memory as a temporal and confidence-aware directed property graph, where each atomic fact is represented with entities, relations, valid-time intervals, confidence scores, and exploration intent labels. During memory construction, REAL adopts a non-destructive temporal update strategy that preserves parallel fact versions and their validity intervals, enabling faithful tracking of fact evolution. During retrieval, REAL anchors query-relevant root entities, decouples their exploration intents, and performs semantic evaluator-guided hybrid beam search to extract compact memory subgraphs. It further incorporates counterfactual inference to repair unreliable retrieval states and recover missing memory evidence through implicit logical relations. Comprehensive experiments demonstrate that REAL substantially improves long-term memory performance over flat-text, graph-based, and existing memory baselines, achieving an average improvement of 22.72\%.

---


### 122. [Unifying Data, Memory, and Compute Efficiency in LLM training: A Survey](https://arxiv.org/abs/2606.10706)

**<font color=#1a73e8>作者：</font>** Vanessa Schmidt, Huy Hoang Nguyen, Cédric Jung 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Resource constraints increasingly determine what can be trained, fine-tuned, and deployed in large language models (LLMs), yet efficiency is often studied through isolated techniques rather than as an interacting system of limits. This survey adopts a constraint-centric perspective and organizes recent progress around three coupled bottlenecks: data efficiency (what to train on), memory efficiency (how to fit training), and compute budget awareness (when and where to spend FLOPs). On the data axis, we review selection and pruning methods that maximize learning per token, ranging from scalable proxy signals based on learning dynamics to gradient- and influence-based scoring, as well as difficulty-aware and curriculum-style strategies. We highlight emerging evidence that different notions of good data dominate in different regimes, implying that optimal subsets depend on the task objective and resource budget rather than being universal. On the systems side, we show that GPU memory, not raw compute, is often the dominant bottleneck in fine-tuning, and that effective scaling requires jointly reducing weight storage, optimizer states, and activation memory rather than optimizing any single component in isolation. Beyond memory, we frame training and inference as compute-governed processes in which optimization, data selection, and decoding must explicitly account for finite FLOP budgets. We review evidence for compute-optimal allocation and stopping rules, where computation should be halted or reallocated once marginal performance gains fall below a budget-dependent threshold. Together, these results unify compute-aware data selection, scaling laws, and adaptive inference under a common principle of resource-conditioned decision-making.

---


### 123. [Continual LLM Upcycling: A Predictor-Gated Bank-Wise Sparsity Training Recipe for Dense-to-Sparse LLMs](https://arxiv.org/abs/2606.10722)

**<font color=#1a73e8>作者：</font>** Ruixuan Huang, Jinyuan Shi, Hantao Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study dense-to-sparse continual training as a way to construct channel-sparse large language models from dense checkpoints. Starting from a Qwen2.5-8B dense backbone, we continue training at 32K context and introduce a predictor-gated sparse SwiGLU FFN in the 32K stage. For each token and layer, we use a low-rank predictor to produce FFN-channel routing logits. We then apply a bank-wise top-k rule to retain 16 channels in every 64-channel bank, yielding 4x sparsity in the FFN intermediate activation. Unlike post-hoc sparse inference methods, the routing module is placed on the main language modeling path and optimized during continual training, enabling the dense model to be upcycled into a hardware-oriented sparse model. We report the architecture, training recipe, benchmark performance, and training lessons. We also identify a layer-local long-context failure mode on RULER-CWE and propose a single-layer repair algorithm that substantially improves the affected length range.

---


### 124. [When the Chain of Thought Knows Better: Failure Modes in Multi-Turn Reasoning Models](https://arxiv.org/abs/2606.10740)

**<font color=#1a73e8>作者：</font>** Sai Kartheek Reddy Kasu, Nils Lukas, Samuele Poppi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Failures in multi-turn reasoning models are largely invisible to terminal-score evaluation. A model can lock onto an unsafe stance early in a long dialogue, yet its final-turn refusal rate may appear indistinguishable from a robustly aligned baseline. To expose these hidden temporal dynamics, we propose a trace-level diagnostic - the CoT-Output 2x2 safety matrix. This framework labels every turn along two independent axes (internal reasoning and visible output), yielding four operationally defined failure cells: robust alignment, alignment faking, overt jailbreak, and a distinct failure mode we term context-injection failure (where the CoT maintains safe reasoning, but the visible output produces harm, highlighting a multi-turn manifestation of reasoning unfaithfulness). We evaluate three distilled reasoning targets against a fixed attacker across five oversight conditions, collecting 6750 turn-level observations on the Information-Hazard scenario. Our analysis reveals two reproducible vulnerabilities: an oversight paradox where explicit monitoring cues paradoxically increase alignment-faking rates rather than suppress them, and a context-injection failure where models lock onto unsafe external outputs despite safe internal states. We release the full dataset of multi-turn dialogues and CoT traces to support follow-up trace-diagnostic research.

---


### 125. [The Arbiter Agent: Continually Monitoring Multi-Agent Conversations to Detect Emergent Misalignment](https://arxiv.org/abs/2606.10747)

**<font color=#1a73e8>作者：</font>** Filippo Tonini, Federico Torrielli, Anton Danholt Lautrup 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems built from multiple language-model agents become more common, they are increasingly used to make decisions together: discussing, negotiating, and acting on shared tasks. While individual agents may appear well-aligned when tested on their own, problems can arise from how they interact with one another. We introduce the Arbiter, an agent designed to monitor multi-agent conversations in real time and identify which participants may be behaving in misaligned ways. The Arbiter operates under a limited "inspection budget", meaning it must decide carefully how to use its resources. As it observes a conversation step by step, it can choose to wait, question a participant, examine internal information such as system prompts or reasoning traces, or log concerning behavior. At the end, it produces a report identifying the likely source of misalignment. We evaluate the Arbiter across five conversation conditions, ranging from risky financial advice model organisms to evaluation-aware and colluding agents, we test five tool configurations of increasing capability and two backbone models. We find that the Arbiter reliably detects misaligned agents well before the end of the conversation, with active inspection tools improving both detection accuracy and speed. Weight-induced misalignment proves hardest to detect, while instruction-induced misalignment is identified reliably even under passive observation. The logging tool exhibits a dual effect, improving recall at the cost of precision. These results suggest that continual, budget-aware monitoring can effectively catch misalignment, and that overseeing multi-agent systems may require treating the auditor as an active participant in the process. The code is available at this https URL.

---


### 126. [AutoPDE: Reliable Agentic PDE Solving via Explicitly Represented Solver Strategies](https://arxiv.org/abs/2606.10752)

**<font color=#1a73e8>作者：</font>** Huanshuo Dong, Keyao Zhang, Hong Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Numerical solvers for partial differential equations (PDEs) are core computational tools in science and engineering. Building reliable PDE solvers requires not only executable code, but a numerical solver strategy, a set of decisions about discretization, stabilization, solver configuration, and resolution control, that matches the PDE structure. Recent LLM-based coding agents have begun to reduce the programming burden by generating and debugging solver implementations. However, they typically move directly from a PDE problem to solver code, leaving the solver strategy implicit in implementation details. Feedback from a failed solve is therefore routed back to code edits rather than to the underlying strategy, so numerical decisions remain hard to check before code is generated and hard to revise using numerical evidence when it fails. To address this limitation, we propose AutoPDE, a code agent that maintains the solver strategy as an explicitly represented object throughout the solving process: an independent, inspectable object that is built before any code is written and can be revised, using numerical evidence, whenever a solve fails. AutoPDE builds and maintains this object in three stages, all drawing from a library of reusable PDE-solving skills: PDE analysis identifies the equation type and algebraic structure; numerical method selection chooses a numerical method that matches the analysis result and commits to a discretization, stabilization, and linear solver accordingly; and adaptive tuning runs low-cost pilot solves to calibrate resolution and tolerances under the prescribed accuracy and runtime budget. We evaluate AutoPDE on the PDE Agent Bench, where experimental results show that AutoPDE achieves a pass rate of $54.5%$, improving over the strongest baseline by $14.2$ percentage points.

---


### 127. [N-GRPO: Embedding-Level Neighbor Mixing for Enhanced Policy Optimization](https://arxiv.org/abs/2606.10768)

**<font color=#1a73e8>作者：</font>** Xukun Zhu, Hang Yu, Peng Di 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The success of Large Language Models in mathematical reasoning relies heavily on the generation of diverse and valid solution paths during the rollout phase. However, current rollout techniques face a fundamental trade-off: token-level sampling often yields redundant trajectories that differ only in rephrasing, while embedding-level methods utilizing random noise frequently disrupt semantic consistency. To resolve this, we introduce N-GRPO, a novel exploration strategy integrated into the Group Relative Policy Optimization (GRPO) framework. Rather than relying on token-level sampling or native embedding-level noise, our approach leverages Semantic Neighbor Mixing. This mechanism dynamically constructs input representations by mixing the embeddings of an anchor token and its nearest semantic neighbors, thereby injecting diversity while strictly adhering to the local semantic manifold. Experimental evaluations on the DeepSeek-R1-Distill-Qwen models across different sizes show that N-GRPO not only achieves consistent improvements over strong baselines on math reasoning benchmarks but also exhibits robust generalization capabilities on out-of-distribution tasks.

---


### 128. [A Multimodal RGB and Events Dataset for Hand Detection in First-Person View](https://arxiv.org/abs/2606.10790)

**<font color=#1a73e8>作者：</font>** Bharghav Kota, Yulia Sandamirskaya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing hand detection algorithms work on images and the detection rate is restricted by the frame rate of the camera. In hand detection applications for moving robotic systems, conventional cameras cause motion blur, especially in darker lighting conditions. We can leverage the use of event-based cameras which possess a high dynamic range, high temporal resolution, and low power consumption. Recent work has shown that using a stereo setup of an event-based and a frame-based camera improves detection accuracy and the bandwidth-latency tradeoff. The main bottleneck in using event-based cameras in object detection and recognition tasks is a relatively low amount of training data. In this work, we propose a methodology and an exemplary synthetic event-based hand dataset from an egocentric, first-person view perspective. The data is synthesized from the existing RGB Egohands dataset with the v2e toolbox. Parameters of the v2e toolbox are varied to provide versions of the dataset with different lighting conditions and scales. Ground truth detections are generated with a fine-tuned YOLOv8 model which is applied to the RGB images in the Egohands dataset and interpolated on the high-temporal resolution events. We use the multi-modal dataset to perform hand detection with existing object detection algorithms which use a multi-modal setup of event and RGB cameras and demonstrate performance comparable to the state-of-the-art.

---


### 129. [Dep-LLM: Training-Free Depression Diagnosis via Evidence-Guided Structured Multi-factor with Reliable LLM Reasoning](https://arxiv.org/abs/2606.10796)

**<font color=#1a73e8>作者：</font>** Yiqing Lyu, Xianbing Zhao, Buzhou Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Depression Detection (ADD) from clinical interviews is a pivotal task in computational mental health, yet it remains challenging due to two critical obstacles: 1) difficulty in modeling complex but sparsely distributed depression clues within lengthy, multi-topic clinical interviews, leading to superficial and unreliable reasoning; 2) scarcity of labeled data due to clinical privacy, together with high cost of training and fine-tuning, limiting the deployment of supervised ADD systems. To jointly address these challenges, we propose Dep-LLM, a training-free framework that mirrors the step-by-step reasoning of clinical psychiatrists and operates entirely on frozen off-the-shelf foundation LLMs. Dep-LLM comprises three stages. First, a Chain-of-Thought (CoT) Depression Multi-factor Analysis module structurally decomposes the long dialogue into five clinically aligned themes and produces evidence-grounded rationales, effectively handling long-context dependencies. Second, we introduce Confidence Analysis and Modulation module that quantifies the epistemic reliability from token-level entropy of each rationale and applies an intra-label and inter-theme modulation that amplifies trustworthy signals while suppressing uncertain ones without extra training. Third, a Collaborative Multi-factor Prediction module dynamically integrates multi-factor signals weighted by confidence into the final diagnosis. Extensive experiments on the DAIC-WOZ and E-DAIC datasets demonstrate the effectiveness and generalizability of Dep-LLM: it surpasses zero-shot baseline on nearly all 21 foundation LLMs across 9 metrics such as accuracy, macro F1 and weighted-average F1, and further outperforms state-of-the-art supervised domain-specific LLMs as well as the latest closed-source commercial LLMs, while requiring no extra training.

---


### 130. [CITRAS-FM: Tiny Time Series Foundation Model for Covariate-Informed Zero-Shot Forecasting](https://arxiv.org/abs/2606.10798)

**<font color=#1a73e8>作者：</font>** Yosuke Yamaguchi, Issei Suemitsu, Yuki Kajihara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained time series foundation models (TSFMs) have enabled zero-shot forecasting on unseen target series. However, existing TSFMs often incur high computational cost and provide limited support for diverse variable types, often failing to account for covariates that exogenously influence target variability. To address these challenges, we propose CITRAS-FM, a tiny 7M-parameter TSFM that supports univariate, multivariate, and covariate-informed zero-shot forecasting with real-time CPU inference. Built on a patch-based, decoder-only Transformer, CITRAS-FM introduces Shifted Attention into the cross-variate module to effectively exploit known covariates accessible throughout the forecast horizon. Moreover, to enable covariate-aware pretraining despite the scarcity of covariate-rich corpora, we propose CovSynth, which synthesizes realistic covariates from decomposed components of target series. Experiments on fev-bench, spanning 100 tasks across various settings, demonstrate that CITRAS-FM achieves state-of-the-art zero-shot accuracy among sub-10M TSFMs while delivering sub-0.1-second CPU inference, offering a strong balance between forecasting accuracy and real-time deployability.

---


### 131. [Evaluating Research-Level Math Proofs via Strict Step-Level Verification](https://arxiv.org/abs/2606.10799)

**<font color=#1a73e8>作者：</font>** Yifeng Sun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) struggle to rigorously verify complex mathematical proofs. Standard global evaluation approaches suffer from "context poisoning," in which superficially plausible statements mask subtle logical flaws, leading to hallucination or over-skepticism. To address this, we shift from global evaluation to strict step-level verification: our framework maintains detailed context for each deduction step and strictly constrains the sources of applied theorems. We evaluate on a carefully curated adversarial diagnostic suite of research-level proofs drawn from the FirstProof challenge. A systematic ablation study demonstrates that these deductive constraints are indispensable, as unconstrained global prompting consistently fails to localize subtle logical errors. Beyond outperforming global evaluation, our approach fundamentally alters the failure taxonomy. Error analysis reveals that, rather than exhibiting severe logical hallucinations, remaining rejections are primarily instances of "pedantic hyper-rigor" stemming from unstated domain conventions, effectively exposing implicit ambiguities within the expert benchmark itself. Our findings suggest that prompting agents to organize their verification notes in a cautious, human-mathematician-like manner can substantially improve their ability to distinguish rigorous proofs from flawed ones, with the potential to strengthen agentic reasoning on frontier mathematical concepts that the base model does not already know well, and to lay a theoretical foundation for future automated proof-review systems. Code and prompts are available at GitHub.

---


### 132. [Boosting ECG Classification Performance by Pre-training with Synthesized Data](https://arxiv.org/abs/2606.10802)

**<font color=#1a73e8>作者：</font>** Naoki Nonaka, Jun Seita  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Neural Networks (DNNs) typically require extensive datasets for effective training. In the medical domain, acquiring large-scale data is often challenging due to privacy concerns and the rarity of certain diseases. To address this data scarcity, we investigate the efficacy of training DNN models using synthetic data, generated based on domain-specific medical knowledge. Specifically, we develop a knowledge-driven Gaussian-composition synthesis algorithm for single-lead II ECGs, in which each heartbeat is represented by Gaussian-shaped P, Q, R, S, and T wave components. Using this simulator, we generate synthetic data for four abnormal electrocardiogram (ECG) classes: atrial fibrillation (AF), atrial flutter (AFLT), premature ventricular complex (PVC), and Wolff-Parkinson-White Syndrome (WPW). We evaluate the utility of this synthetic data by conducting abnormal ECG classification using ten different DNN architectures. Our results demonstrate that synthetic-to-real training improves classification performance for three of the four target abnormalities, with the largest architecture-averaged gain of $33.2\%$ observed for AFLT. Further analysis reveals that the performance enhancement from synthetic data is more pronounced with smaller real-world datasets. These findings suggest that domain-knowledge-based synthetic ECGs can serve as a useful pre-training resource, particularly in scenarios where real-world data are limited or difficult to obtain.

---


### 133. [Beyond APIs: Probing the Limits of MLLMs in Physical Tool Use](https://arxiv.org/abs/2606.10803)

**<font color=#1a73e8>作者：</font>** Zhixin Ma, Yutong Zhou, Yongqi Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) excel at utilizing digital APIs and increasingly serve as the "brain" of embodied AI, instructing robots to interact with the physical world. In such embodied settings, a central capability is the use of physical tools, which underpins MLLMs' ability to assist humans in real-world tasks. Despite the importance, MLLMs' proficiency in physical tool use remains largely unexplored. To address this gap, we introduce PhysTool-Bench, the first physical tool-use benchmark designed to evaluate MLLMs' ability to comprehend real-world scenarios, identify physical tools, and plan their use. PhysTool-Bench comprises 2,510 queries over 2,678 real-world physical tools spanning diverse domains, including manufacturing, electrical work, agriculture, and healthcare. Concretely, models are evaluated along two primary dimensions: 1) recognizing all physical tools present in the scene, and 2) planning the tool selection and use sequence based on the instruction and visual context. Across 13 leading MLLMs, even the strongest model (Gemini-3.1-Pro) identifies only 58.7% of tools in a scene and completes merely 21.0% of queries end-to-end. Our analysis reveals a two-level deficit: MLLMs struggle to perceive tools in realistic scenes, and the much larger drop at the planning stage further indicates a lack of functional commonsense for mapping perceived tools onto task semantics, pinpointing a critical bottleneck for the development of practical embodied AI.

---


### 134. [Earth-OneVision: Extending Remote Sensing Multimodal Large Language Models to More Sensor Modalities and Tasks](https://arxiv.org/abs/2606.10819)

**<font color=#1a73e8>作者：</font>** Miaoxin Cai, Guanqun Wang, Wei Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RS-MLLMs enable natural-language understanding and spatial reasoning over earth observation imagery. However, existing models support only a narrow range of sensor types and tasks, yielding a fragmented view of the earth and leaving cross-modal geoscientific knowledge largely unexploited. This work presents Earth-OneVision, a 2B RS-MLLM that unifies six sensor modalities (i.e., optical, SAR, infrared, multispectral, temporal, and video) and cross-sensor fusion across 9 task categories within a single autoregressive framework. Three dedicated mechanisms address three bottlenecks. Full-Granularity Vision-Language Alignment (FGVLA) aligns multi-level visual features with the multi-dimensional language space. Spatial-Linguistic Isomorphic Serialization (SLIS) unifies heterogeneous spatial outputs as autoregressive tokens. Progressive Cross-Modality Adaptation (PCMA) decomposes the compound domain gap into sequential stages, tackling the viewpoint and imaging physics gaps in turn. To support joint training, MMRS-OneVision is constructed with ~34M QA pairs spanning all six sensor modalities and cross-sensor fusion across 9 task categories, substantially exceeding existing RS multimodal instruction datasets. With only 2B parameters, Earth-OneVision achieves competitive or state-of-the-art results across extensive benchmarks, consistently matching or outperforming 4B-72B RS-MLLMs. It achieves 87.52% P@0.5 on the OPT-RSVG testset for optical visual grounding and 80.68% on the SAR VQA benchmark SARLANG-Bench, exceeding 7B models by over 7%. It further achieves 75.74% recall on the BigEarthNet-MS testset for multispectral classification, and 81.94% MCQ accuracy on EarthMind-Bench for cross-modality reasoning.

---


### 135. [K-Forcing: Joint Next-K-Token Decoding via Push-Forward Language Modeling](https://arxiv.org/abs/2606.10820)

**<font color=#1a73e8>作者：</font>** Zhiwei Tang, Yuanyu He, Yizheng Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) language modeling is the dominant paradigm for text generation, yet its sequential token-by-token decoding makes inference memory-bound and inefficient. Existing acceleration approaches, such as speculative decoding and diffusion language models, can yield speedups under certain conditions but do not directly address high-load batch serving--the scenario most critical for industrial-scale deployment. We introduce K-Forcing, a push-forward language modeling paradigm for joint next-k-token decoding. K-Forcing distills an existing AR model into a conditional push-forward mapping--one that transforms independent uniform noise variables into a joint sample of multiple future tokens in a single forward pass. This design preserves fixed-length outputs, reuses the AR teacher backbone, and remains compatible with standard AR serving infrastructure. We train this mapping via progressive self-forcing distillation, which gradually expands the prediction window while enabling the student to closely match the sequence distribution of the AR teacher. We evaluate K-Forcing on LM1B and OpenWebText using a standard causal Transformer backbone. When aggressively configured to generate k = 4 tokens per forward pass, K-Forcing delivers approximately 2.4-3.5x speedup across different batch sizes, while incurring modest quality degradation relative to its AR teacher. As inference increasingly dominates the lifetime compute cost of modern LLMs, K-Forcing offers a promising route toward accelerating AR generation under real-world high-load deployment.

---


### 136. [Attention-Discounted Adaptive Sampler for Masked Diffusion Language Models](https://arxiv.org/abs/2606.10829)

**<font color=#1a73e8>作者：</font>** Yusuf Sahin, Ahmed Rockey Saikia, Volkan Cevher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models can reduce inference steps by revealing multiple tokens per denoising iteration, but this parallelism is fragile: positions that are individually confident may be unsafe to commit together when their predictions are coupled. Existing training-free samplers such as Top-\(k\), Fast-dLLM, and EB-Sampler mainly control how many tokens to reveal, while often ranking candidates by token-wise scores that ignore interactions within the selected set. We propose ADAS, a training-free reranking rule for parallel masked diffusion decoding. ADAS leaves the base sampler's stopping rule unchanged and modifies only subset construction: it greedily discounts a candidate when it attends strongly to already selected positions whose predictions remain uncertain. Unlike graph-constrained methods that turn attention into hard compatibility constraints, ADAS keeps attention continuous and uses it as a soft marginal penalty. Across LLaDA-8B-Base and Dream-7B-Base on GSM8K, MATH500, HumanEval, and MBPP, plugging ADAS into Top-\(k\), Fast-dLLM, and EB-Sampler improves low-NFE performance at matched denoiser evaluations by \(9.11\) and \(10.46\) percentage points on average, respectively, with \(3.1\%\) per-forward runtime overhead. These results show that soft attention-discounted reranking is a simple and modular way to improve quality in highly parallel decoding for masked diffusion language models.

---


### 137. [Geometrically Averaged Hard Target Updates for Linear Q-Learning](https://arxiv.org/abs/2606.10835)

**<font color=#1a73e8>作者：</font>** Donghwan Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Periodic hard target updates are among the most common stabilization devices in modern deep Q-learning. Recent studies suggest that target updates can improve stability in Q-learning with function approximation, including linear function approximation. We introduce and analyze the so-called $\lambda$-target update, obtained by averaging the $m$-periodic target update maps with $\lambda$-geometric weights $(1-\lambda)\lambda^{m-1}$, $\lambda \in [0,1]$. The endpoint $\lambda=0$ recovers the one-period target update, while the continuous endpoint $\lambda\uparrow1$ recovers projected Q-value iteration. We study this mechanism for Q-learning with linear function approximation, namely linear Q-learning, using a switching-system model and related tools. For clarity, the paper treats a deterministic version; the formulation extends to stochastic reinforcement-learning settings.

---


### 138. [Janus: A Benchmark for Goal-Conditioned Information Distortion in LLMs](https://arxiv.org/abs/2606.10852)

**<font color=#1a73e8>作者：</font>** Polydoros Giannouris, Mohsinul Kabir, Sophia Ananiadou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM deception is often evaluated through direct markers such as fabricated claims, explicit lies, or strategic concealment. However, many real-world misleading communications do not depend on false statements, rather, they arise from selective treatment of true material facts: omitting adverse evidence, softening unfavorable details, emphasizing favorable details, or replacing precise qualifications with vague language. Existing benchmarks largely miss this subtler and arguably more dangerous failure mode. We introduce JANUS, a benchmark for measuring goal-conditioned pragmatic distortion in fact-grounded LLM outputs. Each scenario in our benchmark provides a fixed pool of favorable and adverse facts and compares a neutral condition against a goal-directed condition, such as increasing adoption, enrollment, approval, or support, despite potential harm to directly affected individuals or groups. Because all outputs are constrained to use the same fact pool, JANUS isolates misleading net impressions from hallucination and fabrication. JANUS contains 160 scenarios across 8 domains, with each scenario paired with neutral and goal-conditioned prompts and annotated material facts. Extensive experiments across 12 LLMs reveal consistent goal-conditioned distortions, demonstrating that current models remain sensitive to incentive and framing objectives and lack robust safeguards against selectively misleading communication. We publicly release our corpus and code for future research.

---


### 139. [Pushing the Limits of LLM Tool Calling via Experiential Knowledge Integration and Activation](https://arxiv.org/abs/2606.10875)

**<font color=#1a73e8>作者：</font>** Yupu Hao, Zhuoran Jin, Huanxuan Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) rely on tool use to act as autonomous agents, yet often fail in multi-step execution due to insufficient tool-related knowledge and ineffective knowledge activation. Therefore, we present a systematic study on how knowledge influences tool-use performance, covering the stages of knowledge acquisition, activation, and internalization. In the knowledge acquisition stage, we acquire and evaluate various forms of experiential knowledge, and our analysis shows that simple instance-level knowledge can already provide strong and reliable gains, while abstract intent-level knowledge offers limited benefits. At inference time, to activate knowledge, we find that prompting LLM to expand the depth of reasoning yields diminishing returns, whereas expanding the width of reasoning by parallel sampling with aggregation more effectively activates latent experiential knowledge. At training time, for knowledge internalization, post-training with knowledge-augmented data further improves performance, with reinforcement learning outperforming supervised fine-tuning. Based on these insights, we propose the Knowledge-Augmented Tool Execution (KATE), a knowledge-augmented tool execution framework that integrates experiential knowledge with reasoning-width-expanded inference and knowledge-aware training. Experiments on BFCL-V3 and AppWorld demonstrate consistent and substantial improvements over strong baselines across model scales. Our Code is available at this https URL.

---


### 140. [Optimal Post-Training Quantization Scales and Where to Find Them](https://arxiv.org/abs/2606.10890)

**<font color=#1a73e8>作者：</font>** Juan Amboage, Pablo Monteagudo-Lago, Ian Colbert 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) compresses large language models by mapping weights to low-bit representations. The scaling factor that defines the quantization grid is typically chosen using simple, data-free heuristics. In this work, we present PiSO (Piecewise Scale Optimization), an algorithm that leverages calibration data to compute the optimal channel-wise weight scales exactly and efficiently under round-to-nearest quantization. PiSO partitions the scale search space into finitely many intervals on which the objective admits a closed-form minimizer. We extend PiSO to group-wise quantization via principled heuristics and propose effective strategies for interleaving scale optimization with error correction. Experiments on Llama and Qwen models across multiple model sizes and target weight bit-widths demonstrate consistent improvements in perplexity and downstream zero-shot accuracy, both standalone and combined with error correction. In particular, we observe increased benefits as the target bit-width narrows and quantization becomes more challenging.

---


### 141. [Improving Text-Instance Alignment Of Foreground Conditioned Out-Painting Via Customized Concept Embedding](https://arxiv.org/abs/2606.10892)

**<font color=#1a73e8>作者：</font>** Yihao Zhao, Xuan Han, Bin He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To showcase products, merchants often incur substantial costs creating high-quality display images. Foreground Conditioned Outpainting (FCO) meets this demand, allowing users to create desired backgrounds for foreground instances at a low cost by adjusting the text prompt. However, existing text-driven FCO methods exhibit critical flaws in their outputs, most notably the presence of artifacts, which refer to regions in the synthesized background that share the same semantics as the foreground instance. Such artifacts diminish the object's prominence and degrade image quality. We attribute the issue to the misalignment between the given instance and text-derived concept embeddings. To address this, we propose the Customized Concept Embedding Diffusion (CCE-Diffusion) framework. Its core is a CCE-Module to customize concept embeddings, bridging the gap between generic noun semantics and a specific visual instance. An Instance-Aware Loss guides the module's optimization, while a Semantic-Preserving Prompt Template prevents customized embeddings from distorting other words in the prompt. Both qualitative and quantitative evaluations demonstrate that CCE-Diffusion significantly reduces artifacts in the outputs. As a plug-and-play component, the CCE-Module can integrate with various FCO methods, enhancing their performance.

---


### 142. [Pose-ICL: 3D-Aware In-Context Learning for Pose-Controllable Subject Customization](https://arxiv.org/abs/2606.10902)

**<font color=#1a73e8>作者：</font>** Xuan Han, Yihao Zhao, Mingyu You  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subject Customization is a foundational task in modern image generation. By providing a few reference images and a text prompt, users can generate images of a specific object in any desired scene. However, existing methods still struggle to achieve effective pose control for customized subjects. In practice, they often exhibit inaccurate poses or inconsistent cross-pose appearances. These limitations suggest that understanding objects in a volumetric manner remains a significant challenge for 2D-native backbones. To address this challenge, we propose Pose-ICL, a tuning-free framework that leverages 3D-aware In-Context Learning (ICL) to directly adapt to new subjects through multiple paired image-pose references. Its core mechanism,Surface-Anchored Position Embedding (SAPE), equips the model with explicit 3D awareness by anchoring image tokens to the surface coordinates of a volumetric bounding box. Dedicated refinements ensure its seamless compatibility with existing DiT models. Extensive evaluations on both 3D assets and real-world subjects demonstrate that Pose-ICL significantly outperforms current methods in both pose accuracy and identity consistency.

---


### 143. [Beyond Model Size: Probing the Gaps in Visual in-Context Learning by Training a Tiny Model](https://arxiv.org/abs/2606.10905)

**<font color=#1a73e8>作者：</font>** Sunil Khatri, Steven Landgraf, Markus Ulrich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual in-Context Learning (VICL) aims at making progress towards adaptive vision models, that can -- based on a few examples -- adapt to a new task at test-time. With the history of in-context learning in natural language processing research, where large, parameter-heavy models are in use, one pathway that current VICL methods take is model- and data-scaling as key ingredients. Yet, it is not clear, whether these ingredients are the key for in-context learning to take shape in vision models. To stress-test such large models, we challenge them with an extreme counterexample: we train a tiny visual in-context model with merely $1$ million parameters and a modest amount of $70,000$ images. We compare the results of this severely capacity capped tiny model to $7,000\times$ larger VICL models in different adaptive settings, (1) on image data with small distribution shifts, (2) on unseen task encodings and (3) on a completely new task, i.e., the setting VICL envisions. With the chasm of training resources between the tiny- and large models, our experiments showcase a lack in how adaptive capabilities are measured, with respect to how tasks are encoded, which tasks were used in pre-training and the choice of metrics. These gaps in current VICL benchmarking underscore a need for innovation in evaluation of adaptive capabilities.

---


### 144. [Role-Agent: Bootstrapping LLM Agents via Dual-Role Evolution](https://arxiv.org/abs/2606.10917)

**<font color=#1a73e8>作者：</font>** Xucong Wang, Ziyu Ma, Shidong Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although Large Language Model (LLM) agents have demonstrated strong performance on complex tasks, their learning is often limited by inefficient interaction feedback and static training environments, which hinder broader generalization. To address these limitations, this paper introduces Role-Agent, \textcolor{black}{a framework} that harnesses a single LLM to function concurrently as both the agent and the environment, enabling a bootstrapped co-evolution. Role-Agent comprises two synergistic components: World-In-Agent (WIA) and Agent-In-World (AIW). In WIA, the LLM acts as the agent and predicts future states after each action; the alignment between predicted and actual states is then used as a process reward, encouraging environment-aware reasoning. In AIW, the LLM analyzes failure modes from failed trajectories and retrieves tasks with similar failure patterns, thereby reshaping the training data distribution for targeted practice. Experiments on multiple benchmarks show that Role-Agent consistently improves performance, yielding an average gain of over 4\% over strong baselines.

---


### 145. [Trace Only What You Need: Structure-Aware On-Demand Hypergraph Memory for Long-Document Question Answering](https://arxiv.org/abs/2606.10921)

**<font color=#1a73e8>作者：</font>** Xiangjun Zai, Xingyu Tan, Chen Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-document question answering (QA) requires large language models (LLMs) to reason over evidence scattered across lengthy documents, where answers often depend on event order, section-level context, and cross-part evidence connections. Although retrieval-augmented generation (RAG) reduces the input context by retrieving relevant evidence, existing structured RAG methods still face three limitations: costly query-agnostic knowledge organization, insufficient use of original document structure, and no reuse of historical reasoning experience. To address these limitations, we propose DocTrace, a multi-agent RAG framework for long-document QA that supports query-triggered knowledge organization, document-structure-aware and experience-guided reasoning. DocTrace preserves document hierarchy with a lightweight document structural tree index, constructs agent-shared hypergraph-structured working memory on demand during reasoning, and stores successful reasoning plans in graph-structured experience memory for future reuse, enabling adaptive exploration across related long-document questions. Experiments on four long-document QA datasets show that DocTrace achieves the best performance on three datasets, surpassing the strongest baseline, ComoRAG, by up to 8.85% in F1 and 4.40% in EM, while reducing the overall computational cost by 53.32%

---


### 146. [It Takes One to Bias Them All: Breaking Bad with One-Shot GRPO](https://arxiv.org/abs/2606.10931)

**<font color=#1a73e8>作者：</font>** Naihao Deng, Yilun Zhu, Naichen Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Warning: This paper contains several toxic and offensive statements.
Modern large language models (LLMs) are typically aligned through large-scale post-training to ensure fair and reliable behavior. In this work, we investigate how easily such guardrails can be broken by Group Relative Policy Optimization (GRPO). We show that one-shot GRPO training on a single biased example is sufficient to induce systematic bias, with stereotype-driven reasoning generalizing across attributes, categories, and benchmarks. We further find that models differ in their susceptibility based on the initial likelihood of producing biased outputs. Our results reveal a critical vulnerability in post-training: alignment can be overridden by a single example.

---


### 147. [Frontier Coding Agents Use Metaprogramming to Adapt to Unfamiliar Programming Languages](https://arxiv.org/abs/2606.10933)

**<font color=#1a73e8>作者：</font>** Aman Sharma, Sushrut Thorat, Paras Chopra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based coding agents are usually evaluated in familiar software settings: mainstream languages, common libraries, and public repositories. These benchmarks remain important, but they can hide how agents behave when the language itself is unfamiliar. We evaluate six contemporary coding agents on four esoteric programming languages using a sequential setup with file editing, local execution, and hidden-test grading. Our protocol exposes capability differences between these agents that mainstream coding and agentic benchmarks such as SWE-Bench Verified and Terminal-Bench 2.0 compress into much narrower bands. We observe that the strongest agents, Claude Opus 4.6 and GPT-5.4 xhigh, often avoid writing the target language directly. On Brainfuck and Befunge-98, they write Python programs that generate target-language code and debug those generators locally. Forbidding this metaprogramming strategy causes large performance drops. Text guidance distilled from this strategy does not materially improve weaker agents. In contrast, Opus-derived Python helper code for building generators, with no solved benchmark programs or hidden-test answers, sharply improves Sonnet 4.6 and GPT-5.4 mini on the same problems, while Haiku 4.5 remains low. More interpreter calls and output tokens improve stronger agents but leave weaker agents near their original performance, indicating that these resources amplify useful strategies rather than create them. Together, these results show that strong coding agents adapt to unfamiliar languages by using tools, feedback, and workspace state to build a working model of the target language. Metaprogramming is the clearest case, but the broader gap is constructing and debugging a strategy that works under the target language's rules.

---


### 148. [WorldKernel: A World Model is the Coupling Kernel of Admissible Possible Worlds](https://arxiv.org/abs/2606.10934)

**<font color=#1a73e8>作者：</font>** Fabio Rovai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A common assumption holds that enough observational and interventional data, given to a strong enough predictor, suffices. We report a failure mode that contradicts it. Across hundreds of structural causal models, on identified quantities a strong predictor and a Bayesian baseline both succeed, but on unidentified quantities (the couplings between counterfactual worlds) the predictor collapses to a point, on 28% of models to one no valid model can produce, while the truth is an admissible interval more data never narrows. The gap is structural: prediction cannot represent uncertainty over counterfactual couplings. We cast a world model as a single positive semidefinite coupling kernel K(T,T') over admissible worlds, whose diagonal is the ordinary posterior (what a predictor recovers) and whose off-diagonal is the cross-world coupling it cannot, which every counterfactual reads. The paper is the theory of that off-diagonal. It is real: two states with identical posteriors differ on a cross-world query, and the off-diagonal is the coupling that fixes counterfactuals. It can be bounded: positive semidefiniteness is partial-identifying information the marginals lack, and enforcing it bounds counterfactuals in polynomial time where the exact response-type program is intractable. Logical structure sharpens it: ontology axioms tighten the bound by up to a third, propagating to couplings they never touch. It can be acquired: targeted scars, constraints learned from encountered infeasibilities, close the gap several times faster than untargeted ones. Its full reconstruction is approximate counting of the admissible worlds, tractable below the Sly-Sun threshold and inapproximable above; we do not claim to beat the worst case.

---


### 149. [Express Language Modeling](https://arxiv.org/abs/2606.10944)

**<font color=#1a73e8>作者：</font>** Albert Gong, Annabelle Michael Carrell, Raaz Dwivedi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a new tool, Express, for converting a non-causal attention approximation into a causal approximation with matching approximation guarantees. When combined with the state-of-the-art Thinformer approximation, Express improves upon the best known causal attention guarantees, delivering $\log^{3/2}(n)/s$ approximation error with only $O(s)$ memory and $O(s^2 \log^2(n))$ compression overhead for a sequence of length $n$. We pair these developments with an efficient I/O-aware Triton implementation, demonstrate substantial speedups over FlashAttention 2, and use Express to overcome four resource bottlenecks in the language modeling pipeline: long-context prefill, KV cache compression, long-form memory-constrained decoding, and long-form compute-constrained decoding.

---


### 150. [Architect-Ant: Editable Automatic Furnishing of Architectural Floor Plans](https://arxiv.org/abs/2606.10953)

**<font color=#1a73e8>作者：</font>** Fedor Rodionov, Aleksandar Cvejic, Michael Birsak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Furnished floor plans are fundamental to real estate visualization, interior design, and architectural workflows. However, progress in automatic furniture arrangement has been limited by the lack of real, professionally designed floor-plan datasets with object-level furniture annotations. To address this gap, we introduce AntPlan-270, a curated dataset of 270 architectural floor plans with per-room furniture bounding box annotations across ten residential room categories. Building on this dataset, we present Architect-Ant, an editable automatic furnishing framework powered by a fine-tuned vision-language model. Furniture layouts are represented using a compact, coordinate-based domain-specific language (DSL) that encodes object categories and placements relative to the room geometry. To improve spatial reasoning, we generate procedural reasoning traces that capture architectural constraints such as wall alignment, door and window clearance, circulation, fixture compatibility, and room-specific furniture inventories, and use them to supervise fine-tuning of the model. We then apply preference optimization over candidate object placements to further refine layout quality. The generated DSL can be rasterized into semantic masks and used to condition a Flux-based LoRA renderer, producing realistic blueprint-style furnished floor-plan images while preserving the editable symbolic layout. Experiments on layout furnishing show that Architect-Ant produces geometrically valid and functionally plausible layouts, and suggest a scalable path for furnishing larger structure-only floor-plan datasets.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-188](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
