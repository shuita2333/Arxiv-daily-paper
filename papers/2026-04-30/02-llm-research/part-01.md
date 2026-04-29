# 🧠 大模型相关研究 | 2026年04月30日

> 本类共 **92** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-92](./part-02.md)

---

### 1. [Architecture Determines Observability in Transformers](https://arxiv.org/abs/2604.24801)

**<font color=#1a73e8>作者：</font>** Thomas Carmichael  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive transformers make confident errors, but activation monitoring can catch them only if the model preserves an internal signal that output confidence does not expose. This preservation is determined by architecture and training recipe. We define observability as the linear readability of per-token decision quality from frozen mid-layer activations after controlling for max-softmax confidence and activation norm. The correction is essential. Confidence controls absorb 57.7% of raw probe signal on average across 13 models in 6 families.
Observability is not a generic property of transformers. In Pythia's controlled suite, every tested run with the 24-layer, 16-head configuration collapses to rho_partial ~0.10 across a 3.5x parameter gap and two Pile variants, while six other configurations occupy a separated healthy band from 0.21 to 0.38. The output-controlled residual collapses at the same points, and neither tested nonlinear probes nor layer sweeps recover healthy-range signal. Checkpoint dynamics show the collapse is emergent during training. Both configurations at matched hidden dimension form the signal at the earliest measured checkpoint, but training erases it in the (24L, 16H) class while predictive loss continues improving.
Across independent recipes the collapse map changes but the phenomenon persists. Qwen 2.5 and Llama differ by 2.9x at matched 3B scale with probe seed distributions that do not overlap, while Mistral 7B preserves observability where Llama 3.1 8B collapses despite similar broad architecture. A WikiText-trained observer transfers to downstream QA without training on those tasks, catching errors confidence misses. At 20% flag rate, its exclusive catch rate is 10.9-13.4% of all errors in seven of nine model-task cells. Architecture selection is a monitoring decision.

---


### 2. [Intrinsic Mutual Information as a Modulator for Preference Optimization](https://arxiv.org/abs/2604.24804)

**<font color=#1a73e8>作者：</font>** Peng Liao, Peijia Zheng, Lingbo Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline preference optimization methods, such as Direct Preference Optimization (DPO), offer significant advantages in aligning Large Language Models (LLMs) with human values. However, achieving optimal performance with these methods typically involves additional hyperparameter tuning, resulting in substantial time overhead. Although prior work has proposed a range of improvements, these methods remain limited in effectiveness and have not fully eliminated reliance on hyperparameter tuning. In this work, we propose RMiPO, a lightweight and efficient framework for offline preference optimization. RMiPO leverages intrinsic Response-level Mutual information for Preference Optimization with hyperparameter modulation, dynamically decoupling preference contributions at negligible additional computational cost. Extensive experimental results demonstrate that RMiPO achieves consistently superior performance over existing methods while reducing training overhead by more than 15\%. Our code is available at this https URL.

---


### 3. [ITAS: A Multi-Agent Architecture for LLM-Based Intelligent Tutoring](https://arxiv.org/abs/2604.24808)

**<font color=#1a73e8>作者：</font>** Iizalaarab Elhaimeur, Nikos Chrisochoides  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model tutors are easy to build in a notebook and hard to run in a real course. We describe ITAS (Intelligent Teaching Assistant System), a multi-agent tutoring system that a graduate quantum computing course used for a semester at Old Dominion University. The system has three layers. The teaching layer is a Spoke-and-Wheel of three parallel specialist agents (Video, Code, Guidance) followed by a Synthesizer, plus a separate autograder that evaluates both the correctness and the approach of checkpoint submissions. The operational layer is four Cloud Run microservices with session state in Cloud SQL and interaction events streamed through Pub/Sub to BigQuery. The feedback layer is a narrow-scope conversational agent that answers instructor questions over per-lesson pseudonymized event streams, addressing what we call the Blind Instructor Problem: LLM tutors accumulate more data about students than the instructor can reach through routine channels. The architecture is a direct response to specific failures of an earlier prototype, and we describe which of those fixes carried forward and which were dropped for this iteration. We report on a pilot deployment (five students, one course, one semester) interpreted as system-behavior evidence rather than learning-outcome evidence: the teaching layer handled 334 chat turns without the task-boundary hallucinations that domain consolidation would have risked, the operational layer captured 10,628 events across five modules, and the feedback layer surfaced two findings the instructor acted on mid-semester. We do not claim the pilot generalizes. We do claim that the system as described is one workable answer to the question of what an LLM-based ITS needs to look like end-to-end to run in a real course.

---


### 4. [Nautile-370M: Spectral Memory Meets Attention in a Small Reasoning Model](https://arxiv.org/abs/2604.24809)

**<font color=#1a73e8>作者：</font>** Maixent Chenebaux  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Nautile-370M, a 371-million-parameter small language model designed for efficient reasoning under strict parameter and inference budgets. Nautile-370M uses a hybrid backbone in which two SeqCond Attention (SCA) layers, a linear-time spectral sequence operator inspired by SeqCondenser, alternate with one transformer layer. This design aims to retain the long-context efficiency and state-tracking benefits of structured sequential models while preserving the expressive token-to-token routing of attention. The model was trained on a single Cloud TPU v4-64 pod slice provided through the Google TPU Research Cloud (TRC) program; the subsequent reinforcement learning stage was carried out on a single NVIDIA DGX Spark. We prove that the SCA readout mechanism can exactly retrieve any individual token from the prefix summary and can reproduce any output of softmax attention as a special case, establishing that SCA is at least as expressive as full self-attention in the continuous limit. We also describe the training data pipeline and outline a reinforcement learning stage specialized for reasoning, verification, and response quality.

---


### 5. [Incompressible Knowledge Probes: Estimating Black-Box LLM Parameter Counts via Factual Capacity](https://arxiv.org/abs/2604.24827)

**<font color=#1a73e8>作者：</font>** Bojie Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Closed-source frontier labs do not disclose parameter counts, and the standard alternative -- inference economics -- carries $2\times$+ uncertainty from hardware, batching, and serving-stack assumptions external to the model. We exploit a tighter intrinsic bound: storing $F$ facts requires at least $F/$(bits per parameter) weights, so measuring how much a model \emph{knows} lower-bounds how many parameters it \emph{has}. We introduce \textbf{Incompressible Knowledge Probes (IKPs)}, a benchmark of 1{,}400 factual questions spanning 7 tiers of obscurity, designed to isolate knowledge that cannot be derived by reasoning or compressed by architectural improvements.
We calibrate a log-linear mapping from IKP accuracy to parameter count on 89 open-weight models (135M--1,600B) spanning 19 vendors, achieving $R^2 = 0.917$; leave-one-out cross-validation confirms generalization (median fold error $1.59\times$, $68.5\%$ within $2\times$ and $87.6\%$ within $3\times$). For Mixture-of-Experts models, total parameters predict knowledge ($R^2 = 0.79$) far better than active parameters ($R^2 = 0.51$). We evaluate 188 models from 27 vendors and estimate effective knowledge capacity for all major proprietary frontier models; for heavily safety-tuned models the estimates are lower bounds, since refusal policy can hide tens of percentage points of "refused but known" capacity.
The widely-reported saturation of reasoning benchmarks does not imply the end of scaling. Procedural capability compresses under the "Densing Law," but across 96 dated open-weight models the IKP time coefficient is $-0.0010$/month (95\% CI $[-0.0031, +0.0008]$) -- indistinguishable from zero, and rejecting the Densing prediction of $+0.0117$/month at $p < 10^{-15}$. Factual capacity continues to scale log-linearly with parameters across generations and across vendors.

---


### 6. [On the Trainability of Masked Diffusion Language Models via Blockwise Locality](https://arxiv.org/abs/2604.24832)

**<font color=#1a73e8>作者：</font>** Yuxiang Wang, Yu Xiang, Baojian Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (MDMs) have recently emerged as a promising alternative to standard autoregressive large language models (AR-LLMs), yet their optimization can be substantially less stable. We study blockwise MDMs and compare them with AR-LLMs on three controlled tasks that stress different aspects of structured generation: in-context linear regression, graph path-finding, and Sudoku solving. We find that standard random-masking MDMs fail to reliably learn linear regression, exhibit high variance training dynamics on graph path-finding, while outperforming AR-LLMs on Sudoku. To mitigate these instabilities, we propose two locality aware blockwise models, namely Jigsaw and Scatter, that inject left-to-right inductive bias by enforcing autoregressive locality within blocks while preserving iterative refinement at the block level. Empirically, Jigsaw matches AR-LLM stability on linear regression and remains strong on Sudoku, while Scatter retains diffusion's planning advantage on path-finding. Our results indicate that standard random-masking MDMs, even with blockwise variants, may be a suboptimal instantiation of diffusion LMs for ordered generation, motivating models beyond random masking.

---


### 7. [Co-Director: Agentic Generative Video Storytelling](https://arxiv.org/abs/2604.24842)

**<font color=#1a73e8>作者：</font>** Yale Song, Yiwen Song, Nick Losier 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While diffusion models generate high-fidelity video clips, transforming them into coherent storytelling engines remains challenging. Current agentic pipelines automate this via chained modules but suffer from semantic drift and cascading failures due to independent, handcrafted prompting. We present Co-Director, a hierarchical multi-agent framework formalizing video storytelling as a global optimization problem. To ensure semantic coherence, we introduce hierarchical parameterization: a multi-armed bandit globally identifies promising creative directions, while a local multimodal self-refinement loop mitigates identity drift and ensures sequence-level consistency. This balances the exploration of novel narrative strategies with the exploitation of effective creative configurations. For evaluation, we introduce GenAD-Bench, a 400-scenario dataset of fictional products for personalized advertising. Experiments demonstrate that Co-Director significantly outperforms state-of-the-art baselines, offering a principled approach that seamlessly generalizes to broader cinematic narratives. Project Page: this https URL

---


### 8. [Latent Agents: A Post-Training Procedure for Internalized Multi-Agent Debate](https://arxiv.org/abs/2604.24881)

**<font color=#1a73e8>作者：</font>** John Seon Keun Yi, Aaron Mueller, Dokyun Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate has been shown to improve reasoning in large language models (LLMs). However, it is compute-intensive, requiring generation of long transcripts before answering questions. To address this inefficiency, we develop a framework that distills multi-agent debate into a single LLM through a two-stage fine-tuning pipeline combining debate structure learning with internalization via dynamic reward scheduling and length clipping. Across multiple models and benchmarks, our internalized models match or exceed explicit multi-agent debate performance using up to 93% fewer tokens. We then investigate the mechanistic basis of this capability through activation steering, finding that internalization creates agent-specific subspaces: interpretable directions in activation space corresponding to different agent perspectives. We further demonstrate a practical application: by instilling malicious agents into the LLM through internalized debate, then applying negative steering to suppress them, we show that distillation makes harmful behaviors easier to localize and control with smaller reductions in general performance compared to steering base models. Our findings offer a new perspective for understanding multi-agent capabilities in distilled models and provide practical guidelines for controlling internalized reasoning behaviors. Code available at this https URL

---


### 9. [Contrastive Image-Metadata Pre-Training for Materials Transmission Electron Microscopy](https://arxiv.org/abs/2604.24909)

**<font color=#1a73e8>作者：</font>** Georgia Channing, Debora Keller, Marta D. Rossell 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The vast majority of transmission electron microscopy (TEM) data never gets published and ends up on a backup drive until deleted to free up space. These left-over datasets are rich in detail and variation, often paired with automatically saved metadata of instrument state and acquisition parameters. In this work, we introduce a dataset of 7,330 high-angle annular dark-field scanning-TEM (HAADF-STEM) images from a single instrument to learn a joint embedding space between image metadata and HAADF image. These embeddings link image style with acquisition parameters, which allows us to train a generative style transfer network that can convert experimental images into the style they would have had if they were recorded with different instrument parameters. We evaluate the performance of the network and explore the usefulness of the technique for physical denoising.

---


### 10. [Agentic AI for Remote Sensing: Technical Challenges and Research Directions](https://arxiv.org/abs/2604.24919)

**<font color=#1a73e8>作者：</font>** Muhammad Akhtar Munir, Muhammad Umer Sheikh, Akashah Shabbir 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth Observation (EO) is moving beyond static prediction toward multi-step analytical workflows that require coordinated reasoning over data, tools, and geospatial state. While foundation models and vision-language models have expanded representation learning and language-grounded interaction for remote sensing, and agentic AI has demonstrated long-horizon reasoning and external tool use, EO is not a straightforward extension of generic agentic AI. EO workflows operate over georeferenced, multi-modal, and temporally structured data, where operations such as reprojection, resampling, compositing, and aggregation actively transform the underlying state and can constrain subsequent analysis. As a result, errors may propagate silently across steps, and correctness depends not only on internal coherence, but also on geospatial consistency, temporally valid comparisons, and physical validity. This position paper argues that these challenges are structural rather than incidental. We identify the implicit assumptions commonly made in generic agentic models, analyze how they break in geospatial workflows, and characterize the resulting failure modes in multi-step EO pipelines. We then outline design principles for EO-native agents centered on structured geospatial state, tool-aware reasoning, verifier-guided execution, and learning objectives aligned with geospatial and physical validity. Finally, we present research directions spanning EO-specific benchmarks, hybrid supervised and reinforcement learning, constrained self-improvement, and trajectory-level evaluation beyond final-answer accuracy. Building reliable geospatial agents therefore requires rethinking agent design around the physical, geospatial, and workflow constraints that govern EO analysis.

---


### 11. [Large Language Models Explore by Latent Distilling](https://arxiv.org/abs/2604.24927)

**<font color=#1a73e8>作者：</font>** Yuanhao Zeng, Ao Lu, Lufei Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generating diverse responses is crucial for test-time scaling of large language models (LLMs), yet standard stochastic sampling mostly yields surface-level lexical variation, limiting semantic exploration. In this paper, we propose Exploratory Sampling (ESamp), a decoding approach that explicitly encourages semantic diversity during generation. ESamp is motivated by the well-known observation that neural networks tend to make lower-error predictions on inputs similar to those encountered before, and incur higher prediction error on novel ones. Building on this property, we train a lightweight Distiller at test time to predict deep-layer hidden representations of the LLM from its shallow-layer representations to model the LLM's depth-wise representation transitions. During decoding, the Distiller continuously adapts to the mappings induced by the current generation context. ESamp uses the prediction error as a novelty signal to reweight candidate token extensions conditioned on the current prefix, thereby biasing decoding toward less-explored semantic patterns. ESamp is implemented with an asynchronous training--inference pipeline, with less than 5% worst case overhead (1.2% in the optimized release). Empirical results show that ESamp significantly boosts the Pass@k efficiency of reasoning models, showing superior or comparable performance to strong stochastic and heuristic baselines. Notably, ESamp achieves robust generalization across mathematics, science, and code generation benchmarks and breaks the trade-off between diversity and coherence in creative writing. Our code has released at: this https URL.

---


### 12. [S-SONDO: Self-Supervised Knowledge Distillation for General Audio Foundation Models](https://arxiv.org/abs/2604.24933)

**<font color=#1a73e8>作者：</font>** Mohammed Ali El Adlouni, Aurian Quelennec, Pierre Chouteau 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General audio foundation models have recently achieved remarkable progress, enabling strong performance across diverse tasks. However, state-of-the-art models remain extremely large, often with hundreds of millions of parameters, leading to high inference costs and limited deployability on edge devices. Knowledge distillation is a proven strategy for model compression, but prior work in audio has mostly focused on supervised settings, relying on class logits, intermediate features, or architecture-specific techniques. Such assumptions exclude models that output only embeddings, such as self-supervised or metric-learning models. We introduce S-SONDO (Self-Supervised KnOwledge DistillatioN for General AuDio FOundation Models), the first framework to distill general audio models using only their output embeddings. By avoiding the need for logits or layer-level alignment, S-SONDO is architecture-agnostic and broadly applicable to embedding-based teachers. We demonstrate its effectiveness by distilling two audio foundation models into three efficient students that are up to 61 times smaller while retaining up to 96% of teacher performance. We also provide practical insights on loss choice and clustering-based balanced data sampling. Code is available here: this https URL.

---


### 13. [Rethinking Layer Redundancy in Large Language Models: Calibration Objectives and Search for Depth Pruning](https://arxiv.org/abs/2604.24938)

**<font color=#1a73e8>作者：</font>** Minkyu Kim, Vincent-Daniel Yun, Youngrae Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Depth pruning improves the inference efficiency of large language models by removing Transformer blocks. Prior work has focused on importance criteria and search algorithms, often treating layer redundancy as an inherent structural property of pretrained networks. In contrast, we adopt a \emph{functional perspective}, where redundancy is jointly influenced by the model and the evaluation objective, suggesting that a universal ranking may not be sufficient. Through an empirical study across three LLM families, two calibration objectives, and seven search algorithms, we observe that different objectives yield qualitatively different redundant layers, and that perplexity and downstream accuracy rankings do not consistently align. Under a fixed objective, however, search algorithms tend to produce similar solutions. Overall, our results suggest that the calibration objective may play a more influential role than the choice of search algorithm, indicating that further attention to objective design could be beneficial.

---


### 14. [ADE: Adaptive Dictionary Embeddings -- Scaling Multi-Anchor Representations to Large Language Models](https://arxiv.org/abs/2604.24940)

**<font color=#1a73e8>作者：</font>** Orhan Demirci, Sezer Aptourachman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Word embeddings are fundamental to natural language processing, yet traditional approaches represent each word with a single vector, creating representational bottlenecks for polysemous words and limiting semantic expressiveness. While multi-anchor representations have shown promise by representing words as combinations of multiple vectors, they have been limited to small-scale models due to computational inefficiency and lack of integration with modern transformer architectures. We introduce Adaptive Dictionary Embeddings (ADE), a framework that successfully scales multi-anchor word representations to large language models. ADE makes three key contributions: (1) Vocabulary Projection (VP), which transforms the costly two-stage anchor lookup into a single efficient matrix operation; (2) Grouped Positional Encoding (GPE), a novel positional encoding scheme where anchors of the same word share positional information, preserving semantic coherence while enabling anchor-level variation; and (3) context-aware anchor reweighting, which leverages self-attention to dynamically compose anchor contributions based on sequence context. We integrate these components into the Segment-Aware Transformer (SAT), which provides context-aware reweighting of anchor contributions at inference time. We evaluate ADE on AG News and DBpedia-14 text classification benchmarks. With 98.7% fewer trainable parameters than DeBERTa-v3-base, ADE surpasses DeBERTa on DBpedia-14 (98.06% vs. 97.80%) and approaches it on AG News (90.64% vs. 94.50%), while compressing the embedding layer over 40x -- demonstrating that multi-anchor representations are a practical and parameter-efficient alternative to single-vector embeddings in modern transformer architectures.

---


### 15. [Nemotron 3 Nano Omni: Efficient and Open Multimodal Intelligence](https://arxiv.org/abs/2604.24954)

**<font color=#1a73e8>作者：</font>** NVIDIA, Amala Sanjay Deshmukh, Kateryna Chumachenko 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Nemotron 3 Nano Omni, the latest model in the Nemotron multimodal series and the first to natively support audio inputs alongside text, images, and video. Nemotron 3 Nano Omni delivers consistent accuracy improvements over its predecessor, Nemotron Nano V2 VL, across all modalities, enabled by advances in architecture, training data and recipes. In particular, Nemotron 3 delivers leading results in real-world document understanding, long audio-video comprehension, and agentic computer use. Built on the highly efficient Nemotron 3 Nano 30B-A3B backbone, Nemotron 3 Nano Omni further incorporates innovative multimodal token-reduction techniques to deliver substantially lower inference latency and higher throughput than other models of similar size. We are releasing model checkpoints in BF16, FP8, and FP4 formats, along with portions of the training data and codebase to facilitate further research and development.

---


### 16. [BenchGuard: Who Guards the Benchmarks? Automated Auditing of LLM Agent Benchmarks](https://arxiv.org/abs/2604.24955)

**<font color=#1a73e8>作者：</font>** Xinming Tu, Tianze Wang, Yingzhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As benchmarks grow in complexity, many apparent agent failures are not failures of the agent at all - they are failures of the benchmark itself: broken specifications, implicit assumptions, and rigid evaluation scripts that penalize valid alternative approaches. We propose employing frontier LLMs as systematic auditors of evaluation infrastructure, and realize this vision through BenchGuard, the first automated auditing framework for task-oriented, execution-based agent benchmarks. BenchGuard cross-verifies all benchmark artifacts via structured LLM protocols, optionally incorporating agent solutions or execution traces as additional diagnostic evidence. Deployed on two prominent scientific benchmarks, BenchGuard identified 12 author-confirmed issues in ScienceAgentBench - including fatal errors rendering tasks unsolvable - and exactly matched 83.3% of expert-identified issues on the BIXBench Verified-50 subset, catching defects that prior human review missed entirely. A full audit of 50 complex bioinformatics tasks costs under USD 15, making automated benchmark auditing a practical and valuable complement to human review. These findings point toward AI-assisted benchmark development, where frontier models serve not only as subjects of evaluation but as active participants in validating the evaluation infrastructure itself.

---


### 17. [Compute Aligned Training: Optimizing for Test Time Inference](https://arxiv.org/abs/2604.24957)

**<font color=#1a73e8>作者：</font>** Adam Ousherovitch, Ambuj Tewari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling test-time compute has emerged as a powerful mechanism for enhancing Large Language Model (LLM) performance. However, standard post-training paradigms, Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL), optimize the likelihood of individual samples under a base policy, creating a misalignment with test time procedures that rely on aggregated or filtered outputs. In this work, we propose Compute Aligned Training, which aligns training objectives with test-time strategies. By conceptualizing inference strategies as operators on the base policy, we derive new loss functions that maximize performance when said strategies are applied. We instantiate such loss functions for SFT and RL across common test time strategies. Finally, we provide empirical evidence that this training method substantially improves test time scaling over standard training.

---


### 18. [PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference](https://arxiv.org/abs/2604.24971)

**<font color=#1a73e8>作者：</font>** Ishan Patel, Ishan Joshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present PolyKV, a system in which multiple concurrent inference agents share a single, asymmetrically compressed KV cache pool. Rather than allocating a separate KV cache per agent -- the standard paradigm -- PolyKV writes a compressed cache once and injects it into N independent agent contexts via HuggingFace DynamicCache objects. Compression is asymmetric: Keys are quantized at int8 (q8_0) to preserve softmax stability, while Values are compressed using TurboQuant MSE -- a Fast Walsh-Hadamard Transform (FWHT) rotation followed by 3-bit Lloyd-Max quantization with centroids tuned to N(0,1). We evaluate across two model scales (SmolLM2-1.7B-Instruct and Llama-3-8B-Instruct), three context lengths (600-7,194 tokens), and up to 15 concurrent agents. PolyKV achieves a stable 2.91x compression ratio across all configurations. On Llama-3-8B with 15 agents sharing a 4K-token context, PolyKV reduces KV cache memory from 19.8 GB to 0.45 GB -- a 97.7% reduction -- while maintaining only +0.57% perplexity degradation and a mean BERTScore F1 of 0.928. PPL delta does not grow with agent count and improves as context length increases, inverting to -0.26% at 1,851 coherent tokens. To our knowledge, no prior work combines a single shared, lossy-compressed KV pool with multi-reader concurrent agent access.

---


### 19. [Dynamic Decision Learning: Test-Time Evolution for Abnormality Grounding in Rare Diseases](https://arxiv.org/abs/2604.24972)

**<font color=#1a73e8>作者：</font>** Jun Li, Mingxuan Liu, Jiazhen Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical abnormality grounding for rare diseases is often hindered by data scarcity, making supervised fine-tuning impractical and single-pass inference highly unstable. We propose Dynamic Decision Learning (DDL), a framework that enables frozen large vision-language models (LVLMs) to refine their decisions across both language and visual spaces by optimizing instructions and consolidating predictions under visual perturbations. This process improves localization quality and produces a consensus-based reliability score that quantifies model confidence. Results on brain imaging benchmarks, including a rare-disease dataset with 281 pathology types across models ranging from 3B to 72B parameters, show that DDL improves mAP@75 by up to 105% on rare-disease cases and outperforms adaptation baselines and supervised fine-tuning. Furthermore, DDL demonstrates stronger calibration between reliability scores and localization accuracy under severe distribution shifts and increasing task difficulty. Code is available at: this https URL

---


### 20. [A Survey on LLM-based Conversational User Simulation](https://arxiv.org/abs/2604.24977)

**<font color=#1a73e8>作者：</font>** Bo Ni, Leyao Wang, Yu Wang 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> User simulation has long played a vital role in computer science due to its potential to support a wide range of applications. Language, as the primary medium of human communication, forms the foundation of social interaction and behavior. Consequently, simulating conversational behavior has become a key area of study. Recent advancements in large language models (LLMs) have significantly catalyzed progress in this domain by enabling high-fidelity generation of synthetic user conversation. In this paper, we survey recent advancements in LLM-based conversational user simulation. We introduce a novel taxonomy covering user granularity and simulation objectives. Additionally, we systematically analyze core techniques and evaluation methodologies. We aim to keep the research community informed of the latest advancements in conversational user simulation and to further facilitate future research by identifying open challenges and organizing existing work under a unified framework.

---


### 21. [Adaptive Prompt Embedding Optimization for LLM Jailbreaking](https://arxiv.org/abs/2604.24983)

**<font color=#1a73e8>作者：</font>** Miles Q. Li, Benjamin C. M. Fung, Boyang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing white-box jailbreak attacks against aligned LLMs typically append discrete adversarial suffixes to the user prompt, which visibly alters the prompt and operates in a combinatorial token space. Prior work has avoided directly optimizing the embeddings of the original prompt tokens, presumably because perturbing them risks destroying the prompt's semantic content. We propose Prompt Embedding Optimization (PEO), a multi-round white-box jailbreak that directly optimizes the embeddings of the original prompt tokens without appending any adversarial tokens, and show that the concern is unfounded: the optimized embeddings remain close enough to their originals that the visible prompt string is preserved exactly after nearest-token projection, and quantitative analysis shows the model's responses stay on topic for the large majority of prompts. PEO combines continuous embedding-space optimization with structured continuation targets and an adaptive failure-focused schedule. Counterintuitively, later PEO rounds can benefit from heuristic composite response scaffolds that are not natural standalone templates, yet ASR-Judge shows that the resulting gains are not merely empty formatting or scaffold-only outputs. Across two standard harmful-behavior benchmarks and competing white-box attacks spanning discrete suffix search, appended adversarial embeddings, and search-based adversarial generation, PEO outperforms all of them in our experiments.

---


### 22. [Assessing Y-Axis Influence: Bias in Multimodal Language Models on Chart-to-Table Translation](https://arxiv.org/abs/2604.24987)

**<font color=#1a73e8>作者：</font>** Seok Hwan Song, Azher Ahmed Efat, Wallapak Tavanapong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chart-to-table translation converts chart images into structured tabular data. Accurate translation is crucial for Multimodal Language Model (MLM) to answer complex queries. We observe imbalances in the number of images across different aspects of the y-axis information in public chart datasets. Such imbalances can introduce unintended biases, causing uneven MLM performance. Previous works have not systematically examined these biases. To address this gap, we propose a new framework, FairChart2Table, for analyzing y-axis-related bias on five state-of-the-art models. Key Findings: (1) There are significant y-axis biases related to the digit length of the major tick values, the number of major ticks, the range of values, and the tick value format (e.g., abbreviation or scientific format). (2) The number of legends/entities in chart images impacts MLM performance. (3) Prompting MLM with y-axis information can significantly enhance the performance for some MLMs.

---


### 23. [Sparse Personalized Text Generation with Multi-Trajectory Reasoning](https://arxiv.org/abs/2604.24996)

**<font color=#1a73e8>作者：</font>** Bo Ni, Haowei Fu, Qinwen Ge 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) advance, personalization has become a key mechanism for tailoring outputs to individual user needs. However, most existing methods rely heavily on dense interaction histories, making them ineffective in cold-start scenarios where such data is sparse or unavailable. While external signals (e.g., content of similar users) can offer a potential remedy, leveraging them effectively remains challenging: raw context is often noisy, and existing methods struggle to reason over heterogeneous data sources. To address these issues, we introduce PAT (Personalization with Aligned Trajectories), a reasoning framework for cold-start LLM personalization. PAT first retrieves information along two complementary trajectories: writing-style cues from stylistically similar users and topic-specific context from preference-aligned users. It then employs a reinforcement learning-based, iterative dual-reasoning mechanism that enables the LLM to jointly refine and integrate these signals. Experimental results across real-world personalization benchmarks show that PAT consistently improves generation quality and alignment under sparse-data conditions, establishing a strong solution to the cold-start personalization problem.

---


### 24. [Why Does Reinforcement Learning Generalize? A Feature-Level Mechanistic Study of Post-Training in Large Language Models](https://arxiv.org/abs/2604.25011)

**<font color=#1a73e8>作者：</font>** Dan Shi, Zhuowen Han, Simon Ostermann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL)-based post-training often improves the reasoning performance of large language models (LLMs) beyond the training domain, while supervised fine-tuning (SFT) frequently leads to general capabilities forgetting. However, the mechanisms underlying this contrast remain unclear. To bridge this gap, we present a feature-level mechanistic analysis methodology to probe RL generalization using a controlled experimental setup, where RL- and SFT-tuned models are trained from the same base model on identical data. Leveraging our interpretability framework, we align internal activations across models within a shared feature space and analyze how features evolve during post-training. We find that SFT rapidly introduces many highly specialized features that stabilize early in training, whereas RL induces more restrained and continually evolving feature changes that largely preserve base models' representations. Focusing on samples where RL succeeds but the base model fails, we identify a compact, task-agnostic set of features that directly mediate generalization across diverse tasks. Feature-level interventions confirm their causal role: disabling these features significantly degrades RL models' generalization performance, while amplifying them improves base models' performance. The code is available at this https URL.

---


### 25. [Why Search When You Can Transfer? Amortized Agentic Workflow Design from Structural Priors](https://arxiv.org/abs/2604.25012)

**<font color=#1a73e8>作者：</font>** Shiyi Du, Jiayuan Liu, Weihua Du 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated agentic workflow design currently relies on per-task iterative search, which is computationally prohibitive and fails to reuse structural knowledge across tasks. We observe that optimized workflows converge to a small family of domain-specific topologies, suggesting that this combinatorial search is largely redundant. Building on this insight, we propose SWIFT (Synthesizing Workflows via Few-shot Transfer), a framework that amortizes workflow design into reusable structural priors. SWIFT first distills compositional heuristics and output-interface contracts from contrastive analysis of prior search trajectories across source tasks. At inference time, it conditions a single LLM generation pass on these priors together with cross-task workflow demonstrations to synthesize a complete, executable workflow for an unseen target task, bypassing iterative search entirely. On five benchmarks, SWIFT outperforms the state-of-the-art search-based method while reducing marginal per-task optimization cost by three orders of magnitude. It further generalizes to four additional unseen benchmarks and transfers successfully from GPT-4o-mini to three additional foundation models (Grok, Qwen, Gemma). Controlled ablations reveal that workflow demonstrations primarily transfer topological structure rather than surface semantics: replacing all operator names with random strings still retains over 93% of the full system's average performance.

---


### 26. [Leverage Laws: A Per-Task Framework for Human-Agent Collaboration](https://arxiv.org/abs/2604.25040)

**<font color=#1a73e8>作者：</font>** Stan Loosmore  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose a per-task leverage ratio for human-agent collaboration: human work displaced by an agent, divided by the human time required to specify the task, resolve mid-run interrupts, and review the result. The denominator decomposes into three channels through which a conserved per-task information requirement must flow, each with its own time-cost scalar. We show that information density itself is directional and bounded by separate ceilings on human-to-agent and agent-to-human flow, and that the asymptotic behavior of leverage decomposes into two scaling axes (capability and memory) with a non-zero floor on the planning term set by irreducible task novelty bounded by human throughput. We extend this per-task analysis to a windowed leverage measure that accommodates recurring tasks, spawned subtasks, and amortized system-design investment. The per-task ceiling does not bind the windowed measure, though both remain bounded: $L_{\text{task}}$ by per-task novelty, $L_{\text{window}}$ by the stock of accumulated planning investment that pays out within the window. The framework operationalizes aspects of earlier qualitative work on supervisory control (Sheridan, 1992), common ground (Clark & Brennan, 1991), and mixed-initiative interaction (Horvitz, 1999) within a single normative ratio, and produces a list of testable empirical questions that we leave as open problems.

---


### 27. [Analyzing LLM Reasoning to Uncover Mental Health Stigma](https://arxiv.org/abs/2604.25053)

**<font color=#1a73e8>作者：</font>** Sreehari Sankar, Aliakbar Nafar, Mona Barman 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language models (LLMs) are increasingly being explored for mental health applications, recent studies reveal that they can exhibit stigma toward individuals with psychological conditions. Existing evaluations of this stigma primarily rely on multiple-choice questions (MCQs), which fail to capture the biases embedded within the models' underlying logic. In this paper, we analyze the intermediate reasoning steps of LLMs to uncover hidden stigmatizing language and the internal rationales driving it. We leverage clinical expertise to categorize common patterns of stigmatizing language directed at individuals with psychological conditions and use this framework to identify and tag problematic statements in LLM reasoning. Furthermore, we rate the severity of these statements, distinguishing between overt prejudice and more subtle, less immediately harmful biases. To broaden the reasoning domain and capture a wider array of patterns, we also extend an existing mental health stigma benchmark by incorporating additional psychological conditions. Our findings demonstrate that evaluating model reasoning not only exposes substantially more stigma than traditional MCQ-based methods but it helps to identify the flaws in the LLMs' logic and their understanding of mental health conditions.

---


### 28. [Beyond Accuracy: Benchmarking Cross-Task Consistency in Unified Multimodal Models](https://arxiv.org/abs/2604.25072)

**<font color=#1a73e8>作者：</font>** Weixing Wang, Liudvikas Zekas, Anton Hackl 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified Multimodal Models (uMMs) aim to support both visual understanding and visual generation within a shared representation. However, existing evaluation protocols assess these two capabilities independently and do not examine whether they are semantically aligned. As a result, it remains unclear whether current uMMs learn coherent unified representations that remain consistent across tasks given a visual concept. We introduce XTC-Bench, a scene-graph-grounded evaluation framework that measures cross-task visual semantic consistency. By deriving both generation prompts and understanding queries from a structured scene graph, our framework enables fact-level alignment analysis across objects, attributes, and relations. We propose Continuous Cross-Task Agreement (CCTA), a fine-grained metric that quantifies semantic agreement between generation and understanding over matched atomic facts, isolating internal consistency from standalone task accuracy. Extensive experiments on eight open-source and one commercial unified models reveal that high generation or understanding performance does not imply strong cross-task alignment, and architectural analysis shows consistency is governed by how tightly learning objectives are coupled across modalities, not by architectural unification alone. XTC-Bench provides a reproducible and model-agnostic framework for diagnosing representation-level misalignment, offering a concrete direction for advancing unified multimodal modeling beyond isolated task performance.

---


### 29. [Evaluating Risks in Weak-to-Strong Alignment: A Bias-Variance Perspective](https://arxiv.org/abs/2604.25077)

**<font color=#1a73e8>作者：</font>** Hamid Osooli, Kareema Batool, Rick Gentry 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Weak-to-strong alignment offers a promising route to scalable supervision, but it can fail when a strong model becomes confidently wrong on examples that lie in the weak teacher's blind spots. Understanding such failures requires going beyond aggregate accuracy, since weak-to-strong errors depend not only on whether the strong model disagrees with its teacher, but also on how confidence and uncertainty are distributed across examples. In this work, we analyze weak-to-strong alignment through a bias-variance-covariance lens that connects misfit theory to practical post-training pipelines. We derive a misfit-based upper bound on weak-to-strong population risk and study its empirical components using continuous confidence scores. We evaluate four weak-to-strong pipelines spanning supervised fine-tuning (SFT), reinforcement learning from human feedback (RLHF), and reinforcement learning from AI feedback (RLAIF) on the PKU-SafeRLHF and HH-RLHF datasets. Using a blind-spot deception metric that isolates cases where the strong model is confidently wrong while the weak model is uncertain, we find that strong-model variance is the strongest empirical predictor of deception across our settings. Covariance provides additional but weaker information, indicating that weak-strong dependence matters, but does not by itself explain the observed failures. These results suggest that strong-model variance can serve as an early-warning signal for weak-to-strong deception, while blind-spot evaluation helps distinguish whether failures are inherited from weak supervision or arise in regions of weak-model uncertainty.

---


### 30. [Agentic Architect: An Agentic AI Framework for Architecture Design Exploration and Optimization](https://arxiv.org/abs/2604.25083)

**<font color=#1a73e8>作者：</font>** Alexander Blasberg, Vasilis Kypriotis, Dimitrios Skarlatos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rapid advances in Large Language Models (LLMs) create new opportunities by enabling efficient exploration of broad, complex design spaces. This is particularly valuable in computer architecture, where performance depends on microarchitectural designs and policies drawn from vast combinatorial spaces.
We introduce Agentic Architect, an agentic AI framework for computer architecture design exploration and optimization that combines LLM-driven code evolution with cycle-accurate simulation. The human architect specifies the optimization target, seed design, scoring function, simulator interface, and benchmark split, while the LLM explores implementations within these constraints. Across cache replacement, data prefetching, and branch prediction, Agentic Architect matches or exceeds state-of-the-art designs. Our best evolved cache replacement design achieves a 1.062x geomean IPC speedup over LRU, 0.6% over Mockingjay (1.056x). Our evolved branch predictor achieves a 1.100x geomean IPC speedup over Bimodal, 1.5% over its Hashed Perceptron seed (1.085x). Finally, our evolved prefetcher achieves a 1.76x geomean IPC speedup over no prefetching, 17% over its VA/AMPM Lite seed (1.59x) and 21% over SMS (1.55x).
Our analysis surfaces several findings about agentic AI-driven microarchitecture design. Across evolved designs, components often correspond to known techniques; the novelty lies in how they are coordinated. The architect's role is shifting, but the human remains central. Seed quality bounds what search can achieve: evolution can refine and extend an existing mechanism, but cannot compensate for a weak foundation. Likewise, objectives, constraints, and prompt guidance affect reliability and generalization. Overall, Agentic Architect is the first end-to-end open-source framework for agentic AI architecture exploration and optimization.

---


### 31. [Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling](https://arxiv.org/abs/2604.25098)

**<font color=#1a73e8>作者：</font>** Ocean Monjur, Shahriar Kabir Nahin, Anshuman Chhabra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While current Large Language Models (LLMs) exhibit remarkable reasoning capabilities through test-time compute scaling (TTS), their massive parameter counts and high inference costs have motivated the development of pruning methods that can reduce model size without sacrificing performance. However, specific to reasoning LLMs, prior work has shown that structured pruning (methods which removes entire set of layer blocks), significantly degrades TTS reasoning performance. In this work, we revisit this assumption and instead investigate whether unstructured pruning (methods that carefully remove only certain redundant/detrimental weights) exhibits similar limitations. Surprisingly, our extensive experiments across four reasoning benchmarks on two reasoning LLMs: s1.1-7B and Qwen3-8B, consistently show that unstructured pruning augments TTS performance compared to structured pruning, and at times can even outperform the unpruned full-weight LLMs. Furthermore, we also empirically study the impact of different layer-wise sparsity allocation strategies, which are an important parametric choice for instantiating unstructured pruning methods. These findings challenge the conventional notion that pruning always reduces TTS performance and in fact, suggest that carefully undertaken pruning can improve TTS effectiveness even further.

---


### 32. [One Perturbation, Two Failure Modes: Probing VLM Safety via Embedding-Guided Typographic Perturbations](https://arxiv.org/abs/2604.25102)

**<font color=#1a73e8>作者：</font>** Ravikumar Balakrishnan, Sanket Mendapara  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Typographic prompt injection exploits vision language models' (VLMs) ability to read text rendered in images, posing a growing threat as VLMs power autonomous agents. Prior work typically focus on maximizing attack success rate (ASR) but does not explain \emph{why} certain renderings bypass safety alignment. We make two contributions. First, an empirical study across four VLMs including GPT-4o and Claude, twelve font sizes, and ten transformations reveals that multimodal embedding distance strongly predicts ASR ($r{=}{-}0.71$ to ${-}0.93$, $p{<}0.01$), providing an interpretable, model agnostic proxy. Since embedding distance predicts ASR, reducing it should improve attack success, but the relationship is mediated by two factors: perceptual readability (whether the VLM can parse the text) and safety alignment (whether it refuses to comply). Second, we use this as a red teaming tool: we directly maximize image text embedding similarity under bounded $\ell_\infty$ perturbations via CWA-SSA across four surrogate embedding models, stress testing both factors without access to the target model. Experiments across five degradation settings on GPT-4o, Claude Sonnet 4.5, Mistral-Large-3, and Qwen3-VL confirm that optimization recovers readability and reduces safety aligned refusals as two co-occurring effects, with the dominant mechanism depending on the model's safety filter strength and the degree of visual degradation.

---


### 33. [Diagnosis, Bad Planning & Reasoning. Treatment, SCOPE -- Planning for Hybrid Querying over Clinical Trial Data](https://arxiv.org/abs/2604.25120)

**<font color=#1a73e8>作者：</font>** Suparno Roy Chowdhury, Manan Roy Choudhury, Tejas Anvekar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study clinical trial table reasoning, where answers are not directly stored in visible cells but must be reasoned from semantic understanding through normalization, classification, extraction, or lightweight domain reasoning. Motivated by the observation that current LLM approaches often suffer from "bad reasoning" under implicit planning assumptions, we focus on settings in which the model must recover implicit attributes such as therapy type, added agents, endpoint roles, or follow-up status from partially observed clinical-trial tables. We propose SCOPE (Structured Clinical hybrid Planning for Evidence retrieval in clinical trials), a multi-LLM planner-based framework that decomposes the task into row selection, structured planning, and execution. The planner makes the source field, reasoning rules, and output constraints explicit before answer generation, reducing ambiguity relative to direct prompting. We evaluate SCOPE on 1,500 hybrid reasoning questions over oncology clinical-trial tables against zero-shot, few-shot, chain-of-thought, TableGPT2, Blend-SQL, and EHRAgent. Results show that explicit multi-LLM planning improves accuracy for reasoning-based questions while offering a stronger accuracy-efficiency tradeoff than heavier agentic baselines. Our findings position clinical trial reasoning as a distinct table understanding problem and highlight hybrid planner-based decomposition as an effective solution

---


### 34. [M$^3$-VQA: A Benchmark for Multimodal, Multi-Entity, Multi-Hop Visual Question Answering](https://arxiv.org/abs/2604.25122)

**<font color=#1a73e8>作者：</font>** Jiatong Ma, Longteng Guo, Yuchen Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present M$^3$-VQA, a novel knowledge-based Visual Question Answering (VQA) benchmark, to enhance the evaluation of multimodal large language models (MLLMs) in fine-grained multimodal entity understanding and complex multi-hop reasoning. Unlike existing VQA datasets that focus on coarse-grained categories and simple reasoning over single entities, M$^3$-VQA introduces diverse multi-entity questions involving multiple distinct entities from both visual and textual sources. It requires models to perform both sequential and parallel multi-hop reasoning across multiple documents, supported by traceable, detailed evidence and a curated multimodal knowledge base. We evaluate 16 leading MLLMs under three settings: without external knowledge, with gold evidence, and with retrieval-augmented input. The poor results reveal significant challenges for MLLMs in knowledge acquisition and reasoning. Models perform poorly without external information but improve markedly when provided with precise evidence. Furthermore, reasoning-aware agentic retrieval surpasses heuristic methods, highlighting the importance of structured reasoning for complex multimodal understanding. M$^3$-VQA presents a more challenging evaluation for advancing the multimodal reasoning capabilities of MLLMs. Our code and dataset are available at this https URL.

---


### 35. [What Makes Good Instruction-Tuning Data? An In-Context Learning Perspective](https://arxiv.org/abs/2604.25132)

**<font color=#1a73e8>作者：</font>** Guangzeng Han, Xiaolei Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction-tuning datasets often contain substantial redundancy and low-quality samples, necessitating effective data selection methods. We propose an instruction data selection framework based on weighted in-context influence (wICI), which measures how effectively each candidate example reduces instruction-following difficulty for semantically related peers. Through systematic experiments, we address three key questions: what constitutes effective instruction tuning data from an in-context perspective, whether sample difficulty correlates with in-context influence, and how in-context influence translates to instruction tuning effectiveness. Experiments across multiple models and benchmarks demonstrate that our method consistently outperforms existing baselines under constrained data budgets, while empirically showing that sample difficulty negatively correlates with in-context influence.

---


### 36. [FAMA: Failure-Aware Meta-Agentic Framework for Open-Source LLMs in Interactive Tool Use Environments](https://arxiv.org/abs/2604.25135)

**<font color=#1a73e8>作者：</font>** Amir Saeidi, Venkatesh Mishra, Souradeep Mukhopadhyay 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models are being increasingly deployed as the decision-making core of autonomous agents capable of effecting change in external environments. Yet, in conversational benchmarks, which simulate real-world customer-centric issue resolution scenarios, these agents frequently fail due to the cascading effects of incorrect decision-making. These challenges are particularly pronounced for open-source LLMs with smaller parameter sizes, limited context windows, and constrained inference budgets, which contribute to increased error accumulation in agentic settings. To tackle these challenges, we present the Failure-Aware Meta-Agentic (FAMA) framework. FAMA operates in two stages: first, it analyzes failure trajectories from baseline agents to identify the most prevalent errors; second, it employs an orchestration mechanism that activates a minimal subset of specialized agents tailored to address these failures by injecting a targeted context for the tool-use agent before the decision-making step. Experiments across open-source LLMs demonstrate performance gains up to 27% across evaluation modes over standard baselines. These results highlight that targeted curation of context through specialized agents to address common failures is a valuable design principle for building reliable, multi-turn tool-use LLM agents that simulate real-world conversational scenarios.

---


### 37. [Frictive Policy Optimization for LLMs: Epistemic Intervention, Risk-Sensitive Control, and Reflective Alignment](https://arxiv.org/abs/2604.25136)

**<font color=#1a73e8>作者：</font>** James Pustejovsky, Nikhil Krishnaswamy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose Frictive Policy Optimization (FPO), a framework for learning language model policies that regulate not only what to say, but when and how to intervene in order to manage epistemic and normative risk. Unlike standard alignment methods that optimize surface-level preference or task utility, FPO treats clarification, verification, challenge, redirection, and refusal as explicit control actions whose purpose is to shape the evolution of belief, commitment, and uncertainty over time. We formalize alignment as a risk-sensitive epistemic control problem in which intervention decisions are selected based on their expected effect on downstream epistemic quality rather than on immediate reward alone. We introduce a compact taxonomy of frictive interventions, a structured friction functional that operationalizes multiple alignment failure modes, and a unified family of FPO methods spanning reward shaping, preference pairing, group-relative ranking, and risk-conditioned trust regions. We further propose an evaluation framework that measures epistemic competence directly through clarification behavior, calibration, contradiction repair, refusal proportionality, and information efficiency. Together, these results provide a formal and algorithmic foundation for learning agents that are aligned not only in outcome, but in epistemic conduct.

---


### 38. [Semantic Layers for Reliable LLM-Powered Data Analytics: A Paired Benchmark of Accuracy and Hallucination Across Three Frontier Models](https://arxiv.org/abs/2604.25149)

**<font color=#1a73e8>作者：</font>** Michael Rumiantsau, Ivan Fokeev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs deployed for natural-language querying of analytical databases suffer from two intertwined failures - incorrect answers and confident hallucinations - both rooted in the same cause: the model is forced to infer business semantics that the schema does not encode. We test whether supplying those semantics as context closes the gap.
We benchmark three frontier LLMs (Claude Opus 4.7, Claude Sonnet 4.6, GPT-5.4) on 100 natural-language questions over the Cleaned Contoso Retail Dataset in ClickHouse, using a paired single-shot protocol. Each model is evaluated twice: once given only the warehouse schema, and once given the schema plus a 4 KB hand-authored markdown document describing the dataset's measures, conventions, and disambiguation rules.
Adding the document improves accuracy by +17 to +23 percentage points across all three models. With it, the three models are statistically indistinguishable (67.7-68.7%); without it, they are also indistinguishable (45.5-50.5%). Every cross-cluster comparison is significant at p < 0.01. The presence of the semantic-layer document accounts for essentially all of the significant variance; model choice within tier does not.
We interpret this as a structural result: explicit business semantics suppress the dominant class of text-to-SQL errors not by making the model more capable, but by changing what the model is being asked to do.

---


### 39. [Prior-Aligned Data Cleaning for Tabular Foundation Models](https://arxiv.org/abs/2604.25154)

**<font color=#1a73e8>作者：</font>** Laure Berti-Equille  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular Foundation Models (TFMs) achieve state-of-the-art zero-shot accuracy on small tabular datasets by meta-learning over synthetic data-generating processes -- making them highly attractive for practitioners who cannot afford large annotated corpora. However, their in-context learning mechanism assumes approximately clean inputs: missing values, outliers, and duplicates in the real-world data create a prior mismatch that degrades both accuracy and confidence calibration simultaneously. Correcting this mismatch requires sequential decisions over cleaning operators whose interactions no static preprocessing rule can anticipate -a natural fit for reinforcement learning~(RL). We introduce L2C2, the first deep RL framework framing tabular data cleaning as prior alignment: a learned policy sequences operators to minimize the distributional gap between dirty input and the TFM's synthetic prior. Six experiments on ten OpenML benchmark datasets establish: 1) three of seven reward designs collapse to degenerate trivial cleaning strategies -- principled reward engineering is scientifically non-trivial; 2) the novel TFMAwareReward reward we propose selects structurally distinct pipelines on 4/10 datasets and achieves higher TabPFN accuracy on those diverging cases (mean 0.851 vs. 0.843; Wilcoxon p=0.063, n=4) while never underperforming; 3) parameterized cleaning actions improve best-found pipeline reward on 9/10 datasets (Wilcoxon p=0.004); and 4) a policy pre-trained on one single source dataset exceeds scratch training at the 2,000-step fine-tuning checkpoint on all three held-out datasets (up to +28.8% after full fine-tuning) demonstrating cross-dataset transfer of prior-alignment knowledge. These findings establish that prior alignment is a principled data preparation strategy for TFM deployment on real-world tabular data.

---


### 40. [Accurate and Robust Generative Approach for Overcoming Data Sparsity and Imbalance in Landslide Modeling with A Tabular Foundation Model](https://arxiv.org/abs/2604.25159)

**<font color=#1a73e8>作者：</font>** Kaixuan Shao, Gang Mei, Yinghan Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Landslide investigation relies on sufficient and well-balanced observational data influenced by geological, hydrological, and anthropogenic factors. Available landslide inventories are often sparse and imbalanced, which limits understanding of triggering conditions and failure mechanisms. Data generation provides an effective approach to help capture feature dependencies from limited landslide observations. However, existing generation approaches for landslides often struggle to capture complex relationships among features and lack robustness across multiple scenarios and interacting factors. Here, we propose an accurate and robust approach for generating multi-feature landslide datasets by utilizing a tabular foundation model. By leveraging the capacity to learn from limited observations, the proposed approach effectively preserves the multivariate dependencies and statistical characteristics inherent in landslide occurrences. Comparative experiments on 20 landslide inventories demonstrate that the generated datasets closely align with observed distributions, maintain realistic feature dependencies, and exhibit robustness across different environmental contexts. This work provides an effective approach to overcome data sparsity and imbalance and strengthens landslide susceptibility modeling and risk assessment under limited observations.

---


### 41. [From Insight to Action: A Novel Framework for Interpretability-Guided Data Selection in Large Language Models](https://arxiv.org/abs/2604.25167)

**<font color=#1a73e8>作者：</font>** Ling Shi, Xinwei Wu, Xiaohu Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While mechanistic interpretability tools like Sparse Autoencoders (SAEs) can uncover meaningful features within Large Language Models (LLMs), a critical gap remains in transforming these insights into practical actions for model optimization. We bridge this gap with the hypothesis that data selection guided by a model's internal task features is a effective training strategy. Inspired by this, we propose Interpretability-Guided Data Selection (IGDS), a framework that first identifies these causal task features through frequency recall and interventional filtering, then selects ``Feature-Resonant Data'' that maximally activates task features for fine-tuning. We validate IGDS on mathematical reasoning, summarization, and translation tasks within Gemma-2, LLaMA-3.1, and Qwen3 models. Our experiments demonstrate exceptional data efficiency: on the Math task, IGDS surpasses full-dataset fine-tuning by a remarkable 17.4% on Gemma-2-2B while using only 50% of the data, and outperforms established baselines focused on data quality and diversity. Analysis confirms a strong positive correlation between feature amplification and task performance improvement. IGDS thus provides a direct and effective framework to enhance LLMs by leveraging their internal mechanisms, validating our core hypothesis.

---


### 42. [CroSearch-R1: Better Leveraging Cross-lingual Knowledge for Retrieval-Augmented Generation](https://arxiv.org/abs/2604.25182)

**<font color=#1a73e8>作者：</font>** Rui Qi, Fengran Mo, Sijin Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A multilingual collection may contain useful knowledge in other languages to supplement and correct the facts in the original language for Retrieval-Augmented Generation (RAG). However, the vanilla approach that simply concatenates multiple pieces of knowledge from different languages into the context may fail to improve effectiveness due to the potential disparities across languages. To better leverage multilingual knowledge, we propose CroSearch-R1, a search-augmented reinforcement learning framework to integrate multilingual knowledge into the Group Relative Policy Optimization (GRPO) process. In particular, the approach adopts a multi-turn retrieval strategy with cross-lingual knowledge integration to dynamically align the knowledge from other languages as supplementary evidence into a unified representation space. Furthermore, we introduce a multilingual rollout mechanism to optimize reasoning transferability across languages. Experimental results demonstrate that our framework effectively leverages cross-lingual complementarity and improves the effectiveness of RAG with multilingual collections.

---


### 43. [Knowledge-Data Dually Driven Paradigm for Accurate Landslide Susceptibility Prediction under Data-Scarce Conditions Using Geomorphic Priors and Tabular Foundation Model](https://arxiv.org/abs/2604.25196)

**<font color=#1a73e8>作者：</font>** Yuting Yang, Gang Mei, Feng Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Landslide susceptibility prediction is critical for geohazard risk assessment and mitigation. Conventional data-driven paradigm achieves high predictive accuracy but require sufficient conditioning factors and large-scale landslide inventories. However, in practical engineering applications across mountainous and plateau regions, data-scarce conditions are commonly observed, where such data requirements are rarely satisfied, rendering conventional data-driven paradigm inapplicable. To address this issue, we propose a knowledge-data dually driven paradigm for accurate landslide susceptibility prediction under data-scarce conditions. The essential idea behind the proposed novel paradigm is the integration of the geomorphic prior knowledge with scarce landslide data. To validate the proposed paradigm, we first applied it to a data-rich region in central Italy, where a conventional data-driven paradigm trained on the full dataset served as the baseline. By utilizing only 30% of the available landslide data, the proposed paradigm achieved comparable predictive accuracy to the baseline, demonstrating its effectiveness under data-scarce conditions. The paradigm was further evaluated in a genuinely data-scarce environment for application, the Qilian Permafrost Region of the Tibetan Plateau, where it also yielded reliable susceptibility predictions, confirming its applicability under data-scarce conditions.

---


### 44. [BARRED: Synthetic Training of Custom Policy Guardrails via Asymmetric Debate](https://arxiv.org/abs/2604.25203)

**<font color=#1a73e8>作者：</font>** Arnon Mazza, Elad Levi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deploying guardrails for custom policies remains challenging, as generic safety models fail to capture task-specific requirements, while prompting LLMs suffers from inconsistent boundary-case performance and high inference costs. Training custom classifiers achieves both accuracy and efficiency, yet demands substantial labeled data that is costly to obtain. We present BARRED (Boundary Alignment Refinement through REflection and Debate), a framework for generating faithful and diverse synthetic training data using only a task description and a small set of unlabeled examples. Our approach decomposes the domain space into dimensions to ensure comprehensive coverage, and employs multi-agent debate to verify label correctness, yielding a high-fidelity training corpus. Experiments across diverse custom policies demonstrate that small language models finetuned on our synthetic data consistently outperform state-of-the-art proprietary LLMs (including reasoning models) and dedicated guardrail models. Ablation studies confirm that both dimension decomposition and debate-based verification are critical for ensuring the diversity and label fidelity required for effective fine-tuning. The BARRED framework eliminates the reliance on extensive human annotation, offering a scalable solution for accurate custom guardrails.

---


### 45. [When the Forger Is the Judge: GPT-Image-2 Cannot Recognize Its Own Faked Documents](https://arxiv.org/abs/2604.25213)

**<font color=#1a73e8>作者：</font>** Jiaqi Wu, Yuchen Zhou, Dennis Tsang Ng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> OpenAI's GPT-Image-2 has effectively erased the visual boundary between authentic and AI-edited document images: a single number on a receipt can be replaced in under a second for a few cents. We release AIForge-Doc v2, a paired dataset of 3,066 GPT-Image-2 document forgeries with pixel-precise masks in DocTamper-compatible format, and benchmark four lines of defence: human inspectors (N=120, n=365 pair-votes via the public 2AFC site this http URL), TruFor (generic forensic), DocTamper (qcf-568, document-specific), and the same GPT-Image-2 model as a zero-shot self-judge -- asked, to avoid the trivial "image is mostly real" reading, whether any region was generated or edited by an AI image model. Human 2AFC accuracy is 0.501, indistinguishable from chance: even side-by-side, inspectors cannot tell GPT-Image-2 receipt forgeries from authentic counterparts. The three computational judges sit only modestly above (TruFor 0.599, DocTamper 0.585, self-judge 0.532). The self-judge fails consistently, not by chance: across five prompt strategies and four policies for handling ambiguous responses, AUC never rises above 0.59. To rule out the possibility that the two forensic detectors are broken on our source domain rather than blind to AI inpainting, we calibrate each on a same-domain traditional-tampering set built for its training distribution: TruFor reaches AUC 0.962 on cross-camera splicing of our dataset, DocTamper reaches 0.852 on cross-document OCR-token splicing with two-pass JPEG re-encoding. Both retain near-published performance on traditional tampering; switching to GPT-Image-2 inpainting drops AUC by 0.27-0.36 (0.962->0.599 TruFor; 0.852->0.585 DocTamper), isolating a detection gap specific to GPT-Image-2 inpainting. We release the dataset, pipeline, four-judge protocol, and calibration sets.

---


### 46. [ValueAlpha: Agreement-Gated Stress Testing of LLM-Judged Investment Rationales Before Returns Are Observable](https://arxiv.org/abs/2604.25224)

**<font color=#1a73e8>作者：</font>** Sidi Chang, Peiying Zhu, Yuxiao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon investment decisions create a pre-realization evaluation problem: realized returns are the eventual arbiter of investment quality, but they arrive too late and are too noisy to guide many model-development and governance decisions. LLM judges offer a tempting substitute for pre-deployment evaluation of AI-finance systems, but unvalidated judges may reward verbosity, confidence, or rubric mimicry rather than financial judgment. This paper introduces \textbf{ValueAlpha}, a preregistered agreement-gated stress-test protocol for deciding when LLM-judged investment-rationale claims are publishable, qualified, or invalid.
In a controlled market-state capital-allocation prototype with 1,000 honest decision cycles and 100 preregistered adversarial controls (1,100 trajectories, 5,500 judge calls), ValueAlpha clears the aggregate agreement gate at \(\bar{\kappa}_w = 0.7168\) but prevents several overclaims. Lower-rank systems collapse into a tie-class, one rubric dimension fails the per-dimension gate (\texttt{constraint\_awareness}, \(\bar{\kappa}_w = 0.2022\)), single-judge rankings are family-dependent, and terse-correct rationales receive a \(\Delta = -2.81\) rubric-point penalty relative to honest rationales. A targeted anchor-specificity probe further shows that financial constructs such as constraint awareness are operationally load-bearing.
The contribution is therefore not a leaderboard and not a claim to measure true investment skill. ValueAlpha is a pre-calibration metrology layer for AI-finance evaluation: it determines whether a proposed LLM-judge-based investment-rationale claim is stable enough, agreed enough, and uncontaminated enough to be reported at all.

---


### 47. [DRAGON: A Benchmark for Evidence-Grounded Visual Reasoning over Diagrams](https://arxiv.org/abs/2604.25231)

**<font color=#1a73e8>作者：</font>** Anirudh Iyengar Kaniyar Narayana Iyengar, Tampu Ravi Kumar, Gaurav Najpande 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diagram question answering (DQA) requires models to interpret structured visual representations such as charts, maps, infographics, circuit schematics, and scientific diagrams. Recent vision-language models (VLMs) often achieve high answer accuracy on these tasks, yet correct answers do not guarantee that models ground their reasoning in the diagram regions that support the prediction. Models may instead rely on textual correlations or dataset artifacts without identifying the visual evidence required to verify the answer. This limitation prevents reliable evaluation of diagram reasoning and reduces interpretability. We introduce DRAGON, a benchmark for evaluating evidence-grounded visual reasoning in diagrams. Given a diagram, a question, and the correct answer, a model must predict bounding boxes that correspond to the visual elements required to justify the answer. These evidence regions may include answer-bearing components, textual labels, legends, axes, connectors, and other supporting structures involved in the reasoning process. The DRAGON dataset contains 11,664 annotated question instances collected from six diagram QA datasets: ChartQA, Circuit-VQA, InfographicsVQA, MapIQ, MapWise, and AI2D. We release a 2,445-instance benchmark test set with human-verified reasoning evidence annotations and a standardized evaluation framework. We evaluate eight recent VLMs and analyze their ability to localize reasoning evidence across diverse diagram domains. DRAGON enables systematic evaluation of diagram reasoning and supports future research on models that ground their predictions in visual evidence.

---


### 48. [VLM Judges Can Rank but Cannot Score: Task-Dependent Uncertainty in Multimodal Evaluation](https://arxiv.org/abs/2604.25235)

**<font color=#1a73e8>作者：</font>** Divake Kumar, Sina Tayebati, Devashri Naik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used as automated judges for multimodal systems, yet their scores provide no indication of reliability. We study this problem through conformal prediction, a distribution-free framework that converts a judge's point score into a calibrated prediction interval using only score-token log-probabilities, with no retraining. We present the first systematic analysis of conformal prediction for VLM-as-a-Judge across 3 judges and 14 visual task categories. Our results show that evaluation uncertainty is strongly task-dependent: intervals cover ~40% of the score range for aesthetics and natural images but expand to ~70% for chart and mathematical reasoning, yielding a quantitative reliability map for multimodal evaluation. We further identify a failure mode not captured by standard evaluation metrics, ranking-scoring decoupling, where judges achieve high ranking correlation while producing wide, uninformative intervals, correctly ordering responses but failing to assign reliable absolute scores. Finally, we show that interval width is driven primarily by task difficulty and annotation quality, i.e., the same judge and method yield 4.5x narrower intervals on a clean, multi-annotator captioning benchmark. Code: this https URL

---


### 49. [Below-Chance Blindness: Prompted Underperformance in Small LLMs Produces Positional Bias Rather than Answer Avoidance](https://arxiv.org/abs/2604.25249)

**<font color=#1a73e8>作者：</font>** Jon-Paul Cacioli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting sandbagging--the deliberate underperformance on capability evaluations--is an open problem in AI safety. We tested whether symptom validity testing (SVT) logic from clinical malingering detection could identify sandbagging through below-chance performance (BCB) on forced-choice items. In a pre-registered pilot at the 7-9 billion parameter instruction-tuned scale (3 models, 4 MMLU-Pro domains, 4 conditions, 500 items per cell, 24,000 total trials), the plausibility gate failed. Zero of 12 model-domain cells showed significant below-chance performance under sandbagging instruction. Exploratory analyses revealed three qualitatively distinct failure modes. Qwen-2.5-7B and Phi-3.5-mini largely ignored the sandbagging instruction, with 62-88% response identity with the honest baseline. Llama-3-8B complied substantially but implemented underperformance as a positional heuristic, collapsing its response distribution onto middle-alphabet options (E at 31.8%, F at 26.1%) regardless of where the correct answer fell. This produced accuracy boosts of up to 33 percentage points when the correct answer coincidentally occupied the model's preferred position. An explicit anti-task instruction ("pick the least likely answer") drove two of three models below chance, with accuracy as low as 0.024. The capability for answer-aware avoidance therefore exists but is not activated by "deliberately underperform." BCB did not fail as a logical marker of answer-aware avoidance. It was not observed in this regime because the model showing the largest behavioural shift exhibited behaviour consistent with a position-dominant response policy rather than content-aware answer avoidance. We propose that positional-distribution shift may be a more effective behavioural signature than below-chance accuracy for detecting prompted underperformance at this model scale.

---


### 50. [DGLight: DQN-Guided GRPO Fine-Tuning of Large Language Models for Traffic Signal Control](https://arxiv.org/abs/2604.25259)

**<font color=#1a73e8>作者：</font>** Chenbo Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic signal control (TSC) plays a central role in reducing congestion and maintaining urban mobility. This dissertation introduces DGLight, a critic-guided reinforcement-learning framework for adapting a pretrained large language model to TSC. DGLight first trains a CoLight-based Deep Q-Network critic to estimate traffic-aware action values from structured intersection states, then uses the frozen critic to score candidate language-model actions and optimize the policy with Group Relative Policy Optimization (GRPO). The resulting controller maps traffic states to interpretable reasoning traces and signal decisions while learning from dense per-state supervision rather than raw cumulative environment rewards. Experiments on TSC benchmarks covering Jinan and Hangzhou show that DGLight is the strongest overall method among the compared LLM-based controllers, remains competitive with strong RL baselines, and transfers well to city datasets not used to fit the critic. Qualitative examples further show that the model's generated reasoning is interpretable and aligned with the chosen signal phase. The project code is available $\href{this https URL}{here}$.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-92](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
