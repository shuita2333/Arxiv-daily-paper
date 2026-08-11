# 🧠 大模型相关研究 | 2026年08月12日

> 本类共 **438** 篇论文：已确认 **404** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

---

### 251. [Position Bias in Ordinal Classification: A Systematic Evaluation](https://arxiv.org/abs/2608.08869)

**<font color=#1a73e8>作者：</font>** Yu Wang, Jeffrey Zhou, Menglin Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used for ordinal classification, yet semantically equivalent changes to prompt organization can alter their predictions. We conduct systematic experiments to characterize positional bias from label order, demonstration order, and demonstration placement. First, we apply the three probes to ten frontier LLMs on a common ordinal-classification task; every model is sensitive to all three positional sources, showing that the problem is pervasive. Second, we vary eight prompt-, task-, and model-level factors across five datasets; accuracy and stability are often misaligned, and only lower scale cardinality consistently improves both. Third, we compare pointwise, pairwise, and listwise inference, alternative aggregation and debiasing methods, and joint configurations; the tested corrections do not provide a reliable remedy, while a comparison-based listwise formulation offers the best balance but transfers unevenly across models and bias sources. These findings show that positional robustness depends on the full system configuration rather than the model alone. Ordinal-classification systems should therefore be selected jointly for predictive performance and stability.

---


### 252. [DistillCache: KL-Guided Adaptive KV-Cache Eviction for Memory-Efficient LLM Inference](https://arxiv.org/abs/2608.08878)

**<font color=#1a73e8>作者：</font>** Asaad Althoubi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based large language models (LLMs) achieve strong performance across many tasks, but their Key-Value (KV) cache grows linearly with sequence length, creating a severe memory bottleneck for long-context inference. Existing heuristic eviction methods (e.g., H$_2$O and SnapKV) rely on static attention or positional signals that often fail to capture a token's future predictive influence. We propose DistillCache, a reinforcement learning framework that formulates KV-cache eviction as a sequential decision problem. DistillCache learns a lightweight policy network using rich internal model signals (attention statistics, value norms, entropy, and position) and trains it with REINFORCE via a per-step KL-divergence reward to preserve the full-cache output distribution. On a 7B-parameter instruction-tuned Transformer (Mistral-7B-Instruct-v0.3), DistillCache retains 94.2% of full-cache accuracy on LongBench at a 25% cache budget, outperforming both strong heuristic baselines (H$_2$O, SnapKV) by up to 2.7 absolute points and, under our re-implementations, concurrent RL-based methods (ForesightKV, RLKV) by up to 1.4 points on long-context tasks. On reasoning benchmarks, DistillCache is competitive with the best concurrent method and surpasses it under aggressive compression. It also delivers up to 2.1x full-cache throughput while maintaining competitive practical efficiency. These results highlight the effectiveness of learned, distribution-aware policies for memory-efficient long-context LLM inference.

---


### 253. [Theory-Guided Deception Detection: A RAG-Based Artificial Intelligence Exploration](https://arxiv.org/abs/2608.08881)

**<font color=#1a73e8>作者：</font>** David M. Markowitz, Timothy R. Levine  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The current work developed seven Retrieval-Augmented Generation (RAG) models based on leading deception theories and compared how deception judgments were made relative to baseline models. Across 700 statements drawn from five published deception datasets, four large language models (gpt-4o, claude-sonnet-4-6, ollama/llama3, deepseek-v4-flash), and two run-types (RAG vs. baseline), a total of 39,200 deception judgments were rendered. Detection accuracies were consistent with typical human accuracies and not statistically different across RAG (54.5%) and baseline models (54.6%). RAG-based models (57.0%) were less truth-biased than baseline models (59.7%), but the effect size was quite small. Theoretical perspective mattered little for accuracy yet mattered substantially for response bias, which ranged from highly lie-biased (the verifiability approach, 32.2%) to highly truth-biased (truth-default theory, 88.1%). Content effects and model effects further moderated the results. Theory-guided AI judgments are unreliable with current parameters, yet they might show promise with additional datasets, model testing, and theory-to-data matching.

---


### 254. [AquiLLM: An Architecture for Supporting Tacit Knowledge Capture in Research Groups](https://arxiv.org/abs/2608.08883)

**<font color=#1a73e8>作者：</font>** Jack Stark, Srinath Saikrishnan, Vikram Seenivasan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in retrieval-augmented generation (RAG) and large language models (LLMs) enable researchers to integrate AI into scientific workflows. However, using proprietary commercial AI systems raises concerns about transparency, reproducibility and privacy, which are essential for scientific practices. To this end, AquiLLM was developed as an open-source modular RAG-LLM framework using open-weight models, designed to support research groups in capturing tacit knowledge. In this work, we present a series of architectural improvements and feature enhancements to AquiLLM, including local embedding and reranking, multimodal capabilities, OpenAI-compatible inference interfaces, user interface improvements, semantic and episodic memory capabilities, and skills support. These enhancements were informed by discussions with domain experts, including astrophysicists and environmental researchers, and represent a step toward AI systems more closely aligned with scientific research practices.

---


### 255. [Full-bandwidth transformer](https://arxiv.org/abs/2608.08888)

**<font color=#1a73e8>作者：</font>** Xi Wang, Ziyang Cai, Zheng Zhan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoregressive transformers compute along two axes: horizontally across generated tokens, and vertically through model depth. Dense attention gives each token broad horizontal access to the past, but the vertical feedback channel between decoding steps remains narrow: only the sampled token returns to the bottom of the stack, while the top-layer hidden state is discarded. We introduce the \emph{full-bandwidth transformer}, which widens this channel with \emph{latent feedback}: at each decoding step, the previous top-layer hidden state is fused with the sampled token embedding through a gated linear unit and fed back as the next input. Latent feedback lets non-verbalized computation re-enter the stack with a renewed depth budget, while preserving the standard transformer architecture, KV cache, and language-modeling objective. To train full-bandwidth transformers without losing parallel teacher forcing, we use a scheduled multi-pass objective that introduces latent feedback late in pretraining and mixes a small fraction of deeper feedback passes for stability. We train 1B-parameter full-bandwidth transformers up to 400B tokens and find that latent feedback improves validation loss, 5-shot language-model evaluation, math and coding generation, and instruction-tuned performance. With negligible per-token decoding overhead, full-bandwidth transformers match or approach standard transformers trained with roughly $1.5\times$ more tokens, and manage to produce shorter reasoning traces at equal or better accuracy.

---


### 256. [LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing](https://arxiv.org/abs/2608.08889)

**<font color=#1a73e8>作者：</font>** Juncheng Dong, Ding Tong, Ishan Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recommendation systems thrive on personalization, where ''correctness'' is rarely a binary truth but a matter of subjective human preference. As Large Language Models (LLMs) are deployed as autonomous verifiers of safety and quality guidelines, they face a distinctive challenge: context-aware preference alignment. Recent gains in Reinforcement Learning with Verifiable Rewards (RLVR) are indexed mostly on objective, mathematical tasks. Through a large-scale study spanning both proprietary and open-source models on four real-world verification tasks from a production recommender platform, we ask whether explicit reasoning generalizes to subjective, human-centric industry rubrics. We expose a fundamental vulnerability: rigid, math-centric reasoning traces actively degrade verification, and applying standard RLVR triggers a phenomenon we term reasoning collapse, in which the policy abandons deliberation in favor of rapid heuristic guessing. We introduce a conditional length-penalized post-training algorithm that intertwines verification accuracy with bounded reasoning length, halting collapse and recovering performance. Finally, we show that a reasoning trace's efficacy is tightly coupled with its socio-linguistic framing: across 1500 synthesized personas, verification accuracy swings by nearly 0.38 macro-F1 depending solely on the adopted reasoning persona---evidence that much subjective-verification error is really reasoning-style mismatch. This observation motivates a mid-training architecture that routes reasoning through contextually aligned personas. This work offers both a scalable algorithmic patch and a long-term architectural blueprint for aligning reasoning models with real-world subjective constraints.

---


### 257. [From Recovery to Drop-off: How Action Post-training Reduces a VLM's Late-Layer Depth Decodability](https://arxiv.org/abs/2608.08904)

**<font color=#1a73e8>作者：</font>** Alexander Hackett, Arnaud Denis-Remillard, Axel Cassou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How much of a vision-language model's (VLM) spatial understanding remains after the action post-training process of building a vision-language-action model (VLA)? We probe depth perception, a primitive of spatiogeometric understanding, from every decoder layer of a weight-matched open-source base VLM/VLA pair: Molmo2-ER and MolmoAct2-LIBERO. First, the VLA decodes depth worse at every layer, a persistent gap we call the floor. Second, the degradation is not uniform: while the base VLM's depth decodability improves through its final layers, the VLA's collapses, an additional late-layer drop we call the cliff. We causally localize the cliff to late-layer MLP interference: ablating the late-layer MLP writes recovers the majority of the terminal decodability cliff, while matched attention ablations and the same intervention in the weight-matched base VLM produce no comparable recovery. A module-level decomposition explains this dissociation: the base VLM carries depth most accessibly in accumulated MLP writes, whereas action post-training collapses depth decodability in the late accumulated writes.

---


### 258. [ToolVision: Learning When and How to Use Visual Tools with Capability-Aligned Supervision](https://arxiv.org/abs/2608.08907)

**<font color=#1a73e8>作者：</font>** Delin Mao, Chenghao Sun, Jingwei Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thinking with images allows a multimodal model to compensate for limited perception by invoking visual tools through code. Yet the prevailing SFT-then-RL recipe creates a different supervision misalignment at each stage. SFT is expected to teach how to use tools, but trajectories from stronger teachers may succeed through perceptual capabilities that a smaller student cannot reliably reproduce or exploit, causing the student to imitate tool-call patterns without learning how to make them useful. RL is expected to teach when to use tools, but outcome-only rewards make fallible tool execution a liability and suppress tool use, whereas a blanket bonus for every correct tool-using trajectory encourages valid but ineffective operations. To address these two misalignments, we introduce ToolVision. During SFT, a multi-agent pipeline explores candidate trajectories, and a committee including student-scale models scores stepwise evidence gain to rank and prune the search branches. Only successfully executed trajectories with correct final answers are retained for SFT. Before RL, ToolVision compares the learner's performance with and without tools, then rewards successful tool use only on questions where tools provide a clear benefit. Both signals are constructed automatically from public task data without additional human annotations of tool use or necessity. ToolVision-8B improves over its base on all seven main benchmarks, surpasses Thyme-7B, CodeVision-8B, and CodeDance-7B on all three high-resolution benchmarks, and outperforms Qwen3-VL-32B-Thinking on V* and HRBench 8K. We will publicly release the datasets and source code.

---


### 259. [Tied Trit-Planes: Constraining PTQTP to a Uniform Nine-Level Quantizer, with a Persistent Folded Format for Disk-Streamed Mixture-of-Experts Serving](https://arxiv.org/abs/2608.08910)

**<font color=#1a73e8>作者：</font>** Matteo Grella  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> PTQTP decomposes LLM weight matrices into two ternary (trit) planes with two free per-group scales. Tying the scales to a fixed ratio of three collapses the decomposition into a single uniform nine-level quantizer, a known balanced-ternary identity. To our knowledge, at the time of writing, this work is the first to impose that identity as a constraint inside PTQTP's solver. The two trit planes then fold losslessly into one 4-bit code plane that we make the persistent serving representation: disk bytes, expert-cache bytes, and kernel input are the same 4.0625-bits/weight blocks, consumed in one integer dot pass. For this conjunction (ratio-3 nine-level code, CPU-SIMD kernels, SSD expert streaming, identical persistent bytes) we likewise found no precedent. We apply this to the routed experts of DeepSeek-V4-Flash-0731, a 284B-A13B mixture-of-experts model, quantizing in one shot from the released MXFP4 expert weights and streaming experts from SSD on a 64 GB laptop. Against a 4.5-bit Q4_K baseline, measured one process per fixture with an expert-lossless anchor arm as reference control, the tied model matches the official serving API on 5/5 fixtures at step 0 (Q4_K: 4/5) and 12/14 captured continuation steps (11/14), scores 86 vs. 84 on a 100-item MMLU subset, decodes 6.7% faster in decode phase, and ships 9% smaller files: no detected fidelity difference at these small evaluation sizes, and every fixture-level difference between the arms traces to a single measured near-tie cell. The tied fit nevertheless shows higher weight-reconstruction error and worse perplexity, a measured dissociation between proxy metrics and reference fidelity. A cumulative trunk-ternarization ladder and bitwise-pinned aarch64/x86-64 kernels complete the report. All code, formats, and evaluation artifacts are open source in the fucina inference stack.

---


### 260. [Decoding Phenotypes: A Framework for Fusing Genomic Language Models and Neuroimaging](https://arxiv.org/abs/2608.08926)

**<font color=#1a73e8>作者：</font>** Tianli Tao, Ziyang Wang, Emma Robinson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neuroimaging and genetic testing are two important clinical references for nervous system diseases, offering complementary diagnostic information. However, integrating genomic and neuroimaging data for precise disease diagnosis is challenging due to cross-modality heterogeneity. Existing imaging-genetics approaches mainly encode genetic information as hard-coded labels, which lose the local sequence context around disease-associated variants. To address this limitation, we propose GeneFuse, a multimodal learning framework that aligns genetic representations from pre-trained Genomic Language Models (GLMs) with features extracted from images. GeneFuse integrates two components: (1) Genotype-Conditioned Feature Modulation (GCFM), a FiLM-inspired module that uses genomic embeddings to modulate image feature maps; and (2) Uncertainty-aware Genomic Residual Fusion (U-GRF), a fusion strategy that uses imaging-derived predictive uncertainty to gate the contribution of genotypic features. We evaluate GeneFuse on early cognitive decline identification (NC vs. MCI) and dementia screening (NC vs. AD). In the APOE-centered setting, GeneFuse achieves AUROCs of 0.77 and 0.83, outperforming existing imaging-genetics fusion methods. These results indicate that GLM-derived genomic embeddings provide additional information to imaging.

---


### 261. [Integrated Multimodal AI System for Retrieval-Augmented Reasoning, Object Sensing, and Damage Analysis](https://arxiv.org/abs/2608.08935)

**<font color=#1a73e8>作者：</font>** Kalelo Dukuray, Israel Pina, Evan Perez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work presents a unified multimodal AI system for damage assessment that integrates retrieval-augmented generation (RAG) models, thermal spectrum perception, vision foundation model pipelines, and exploratory wireless signal sensing. A RAG component is developed to ground a locally hosted language model in project-specific documentation, including specialized damage level classification criteria to mitigate hallucinations during inference. Controlled comparisons against static few-shot prompting demonstrate that dynamic retrieval improves grounding and factual consistency. We further compare vector-based RAG with a knowledge graph variant constructed via entity-relation extraction, and show that graph-based retrieval produces stronger responses for damage assessment queries requiring cross-document reasoning, motivating hybrid dense, sparse, and graph-aware retrieval. To address limitations of EO imagery under adverse lighting and weather conditions, infrared (IR)/thermal sensing is employed for object detection and segmentation. Our detectors generate candidate detections, yielding improved segmentation of a broad array of objects. Paired IR versus visible spectrum tracking experiments reveal failure modes, motivating multimodal fusion for robust object detection and damage analysis. Vision foundation and vision-language models are leveraged to generate synthetic damage imagery and classify damage severity with high accuracy, supporting training and validation of downstream damage assessment models. Finally, exploratory Wireless-based sensing demonstrates potential to detect presence, motion, and post-event environmental changes where EO and IR sensing are ineffective.

---


### 262. [Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access](https://arxiv.org/abs/2608.08942)

**<font color=#1a73e8>作者：</font>** Lier Jin, Lan Hu, Binqi Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly integrated into healthcare, education, public services, and everyday decision making. They should provide comparable assistance regardless of a user's literacy, communication style, or prompt-engineering expertise. However, existing research on prompt robustness primarily focuses on adversarial attacks, prompt injection, and prompt optimization, while overlooking whether semantically equivalent requests receive different responses simply because they are phrased differently. We refer to this accessibility challenge as "Prompt Privilege": users with greater prompting expertise systematically obtain better model performance despite expressing the same underlying intent.
To address this problem, we present a unified framework for measuring and mitigating accessibility disparities in LLM interactions. We introduce Prompt Equity Score (PES), a quantitative metric for evaluating performance consistency across user populations, and Prompt Equity Transformer (PET), an LLM-based agent that automatically transforms user requests into semantically equivalent, accessibility-oriented prompts while preserving their intent. PET shifts prompt optimization from the user to the AI system, functioning as an intelligent accessibility layer between users and foundation models. Experiments on the MedQA benchmark demonstrate measurable prompt privilege, with statistically significant performance disparities between low-literacy and expert-prompting cohorts. Applying PET eliminates these disparities while preserving semantic fidelity, demonstrating that accessibility-oriented prompt normalization can improve equitable AI access. By introducing prompt privilege as a new dimension of AI accessibility and PET as a practical solution, this work advances system-centered accessibility and provides a foundation for more fair, trustworthy, and inclusive AI systems.

---


### 263. [Idea Search: Guiding Tree Search with Ideas to Explore Diverse Scientific Methods](https://arxiv.org/abs/2608.08958)

**<font color=#1a73e8>作者：</font>** Xuefei Julie Wang, Hao Cui, Michael P. Brenner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tree Search-based test-time scaling of LLMs is a powerful tool for automated scientific coding. However, pure Tree Search sometimes struggles with systematic exploration, becoming trapped in local optima, or unproductive loops, especially in the vast search space of scientific methods. To address this limitation, we propose Idea Search, a framework that systematically integrates a dynamic "Idea Bank" into Tree Search. Idea Search involves three steps: (1) decomposing existing methods into atomic ideas, (2) sampling from this bank of ideas to guide branches of code mutations, and (3) dynamically updating the bank with new ideas discovered through execution. On single-cell RNA-sequencing (scRNA-seq) batch integration, Idea Search reliably breaks the plateau of a strong pure Tree Search baseline, improving the mean score from 0.678 to 0.697 and reaching a best score of 0.728. We then characterize which design choices drive these gains: bank augmentation helps bandit sampling but not random sampling, "Exploratory" prompting that prioritizes new ideas surfaces the rare best-performing solutions, while increasing sampling-level exploration is counterproductive.

---


### 264. [Reading is not Reasoning: Bridging the Agentic Policy Gap in Vision-Text Compression](https://arxiv.org/abs/2608.08960)

**<font color=#1a73e8>作者：</font>** Cheng Fan, Junyi Zhou, Tingzhang Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-step language-model agents repeatedly process growing interaction histories, leading to substantial context costs. Vision--text compression reduces these costs by rendering history as images, but the resulting modality shift creates a marked capability gap. Through controlled evaluations of history recovery, matched-state decisions, and complete trajectories, we show that this gap cannot be explained by OCR quality alone. Visual-history agents exhibit systematic drift in action selection, query formulation, stopping, and evidence use, revealing an agentic policy gap. We introduce \textbf{CAPS}, a two-stage \textbf{C}ross-modal \textbf{A}gentic \textbf{P}olicy \textbf{S}elf-distillation framework that uses the same model's stronger text-history policy to supervise its visual-history counterpart. Offline trajectory self-distillation transfers successful text-policy behavior to visual-history inputs, while online policy self-distillation provides dense supervision on states visited by the visual-history policy during reinforcement learning. On SearchQA, CAPS improves over AgentOCR by 5.0\% and 3.4\% with 3B and 7B backbones, respectively. On full-history ALFWorld, the corresponding gains are 15.6\% and 14.5\%. Across settings, CAPS reduces average memory-context cost by up to 63.3\% and peak cost by up to 83.4\% relative to matched text-history policies. These results show that explicit cross-modal policy self-distillation can preserve agent capability under vision--text compression. Our code will be made publicly available in a future release.

---


### 265. [Gradient Under Microscope: Benchmarking Resource Utilization of Memory-Efficient Gradient Computation Methods](https://arxiv.org/abs/2608.08961)

**<font color=#1a73e8>作者：</font>** Sarthak Mahapatra, Zihan Zhou, Khatoon Khedri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI training's rising resource intensity is straining electricity supplies and carbon budgets, motivating systematic study of memory-efficient training on constrained hardware. We benchmark five gradient optimizers (SGD, Adam, Adagrad, Adadelta, and Conjugate Gradient Descent) under three memory strategies (standard training, gradient checkpointing, and gradient accumulation) across four transformer architectures (ViT, ModernBERT, Llama 3.1 1B, and NanoVLM), measuring training loss, GPU utilization, training time, and memory usage. Gradient accumulation emerges as the most reliable strategy, cutting training loss by roughly an order of magnitude on the vision-language model and about four-fold on the language model without additional GPU memory. Contrary to common practice, Adam is not universally superior: Adadelta and SGD outperform it on the encoder and autoregressive architectures. Gradient checkpointing's effect is strongly architecture-dependent, improving vision transformer loss while severely degrading the encoder model, and it increases training time by up to 60% on memory-bound models. GPU utilization is governed primarily by architecture, ranging from 8-15% for the memory-bound language model to 96-99% for compute-bound vision models. These findings provide practical guidelines for optimizer and gradient-strategy selection in resource-efficient model training and deployment.

---


### 266. [Math-Vision Diagrams: A Comprehensive Benchmark for Evaluating LLM Mathematical Diagram Generation Capabilities](https://arxiv.org/abs/2608.08964)

**<font color=#1a73e8>作者：</font>** Harish Kashyap, Kiran Byadarhaly, Sriram Chakaravarthy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The generation of mathematically precise diagrams from tex- tual prompts has emerged as a critical yet underexplored capability of Large Language Models (LLMs). This has been of interest to researchers in the areas of curriculum preparation, automated ranking of problem sets, and scientific publishing. For LLMs to achieve this, it requires per- fect coordination between Spatial Reasoning, Mathematical Reasoning, and Rendering systems. While existing benchmarks such as MathVision, MathVista are built for Math Reasoning or DiagramGenBenchmark, Mer- maidSeqBench on general purpose diagram generation, no prior work provides a standardized set of prompt, image pairs that can be used to evaluate the LLMs specifically on math diagram generation. This includes fields that span both both text-to-code and text-to-image paradigms. We introduce Math-Vision Diagrams, the first benchmark specifically designed to evaluate LLMs on mathematical diagram generation, and the first to assess text-to-code and text-to-image generation paradigms together in a single unified setting, agnostic of the underlying coding lan- guage or model type. Building on the Math-Vision benchmark, we select a subset of 2920 images out of 3040 from high-quality competition problems with essential visual context. A novel pipeline combining an ensemble of LLMs with Subject Matter Expert (SME) curation is presented, together with a suite of evaluation metrics. Testing several leading models against this benchmark, we demonstrate that LLMs struggle with math diagram generation. All code, data, curation pipeline, and evaluation scripts will be fully open-sourced.

---


### 267. [How Can Rhetoric Reward-Hack AI Reviewers? Dissecting Rhetorical Sensitivity in AI-Based Peer Review](https://arxiv.org/abs/2608.08975)

**<font color=#1a73e8>作者：</font>** Ming Li, Chenguang Wang, Xirui Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models increasingly participate in scientific evaluation, we investigate a potential form of reward hacking: how rhetorical choices shape AI-review judgments when reported scientific content is preserved and how these effects vary across evaluation conditions. We construct a controlled corpus of 4,200 full-paper manuscripts derived from 120 anonymized ICLR 2026 submissions. Two LLM rewriters transform six rhetorical dimensions in opposing directions, and five LLM reviewers evaluate the resulting manuscripts under standard and strict protocols. We also test joint, recursive, and reviewer-guided rewriting. Our results show that rhetorical sensitivity is structured rather than uniform. Evidence framing and novelty stance produce the largest positive-negative contrasts in overall assessment, with scope framing forming a weaker second tier; the remaining dimensions have smaller or less stable effects. This hierarchy persists across human-assessed quality levels, but score movement depends strongly on the AI reviewer's original score: lower scores tend to rise, higher scores tend to fall, and directional contrasts are clearest in the middle ranges. More elaborate workflows do not reliably yield larger gains. Joint rewriting is strongly rewriter-dependent, reviewer guidance does not consistently outperform an unguided second pass, and repeated rewriting yields diminishing, configuration-dependent returns. Across conditions, the rewriter primarily determines the separation between opposing variants, whereas the reviewer determines the magnitude and sign of their score effects. Strict review lowers mean OA by 1.36 points without consistently changing rhetorical sensitivity. These findings identify when rhetorical presentation influences AI scientific review and motivate evaluation systems robust to content-preserving variation in scientific writing.

---


### 268. [Muscle Memory for Agents: Compile not Merely Retrieve](https://arxiv.org/abs/2608.08995)

**<font color=#1a73e8>作者：</font>** Pouya Ghiasnezhad Omran, Soujanya Lanka, Qin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Memory for LLM agents has converged on a single architectural pattern: store experience as text, embeddings, reflections, or rules; retrieve at inference time; let a general-purpose orchestrator interpret what to do. This paper argues that the pattern is the wrong default for personalization. We position Muscle Memory - the practice of compiling recurring user intent into purpose-built specialist agents - as a distinct memory paradigm from retrieval, and we argue that compilation is a better fit for the workloads where current assistants impose a multi-turn tax on their users: making them repeatedly correct format, depth, and scope to obtain a domain-appropriate answer. We support the position with a reference implementation and empirical evidence. The implementation is a four-phase pipeline (Harvest $\rightarrow$ Analyze $\rightarrow$ Augment $\rightarrow$ Evaluate) that mines conversational history, separates behavioral from task patterns, and emits quality-gated executable compiled specialists with two-stage trigger matching. On 90 held-out scenarios across five user personas, the augmented assistant wins 32 of 36 cases where a specialist fires, an 88.9% win rate, with a +2.05 personalization gain and only a $-0.28$ accuracy cost on a 1-4 scale. We discuss why compilation is better suited than retrieval in this regime, what the result implies for the broader memory design space, and what open problems remain.

---


### 269. [Mind the Hook: Source-Level Auditing of Privacy Defenses in Retrieval-Augmented Generation](https://arxiv.org/abs/2608.09001)

**<font color=#1a73e8>作者：</font>** Yanhang Li, Zhichao Fan, Zexin Zhuang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Black-box privacy scores for retrieval-augmented generation (RAG) are difficult to interpret unless the audited defense's active pipeline hook is known. We propose an active-path audit: inventory source-level hooks over retrieval, retrieved content, and generation; map each metric to the leakage channel it observes; and validate generated-text effects with exact-match canaries. In our benchmark reimplementations, the DP-style defenses modify retrieval scores only: their generation hooks are TODO-flagged stubs that return responses unchanged. This active path explains why they affect membership-inference behavior but track No-Defense on generated-text named-entity leakage, measured by NEL_strict. By contrast, the end-to-end LPRAG path is canary-validated on the email channel, recovering 53/150 canaries under No-Defense and 0/150 under LPRAG. These findings concern our reimplementations on our stack, not released defenses or defense families; the contribution is a methodology and case study, not a universal ranking

---


### 270. [SignLlama: Enhancing Gloss-free Sign Language Translation by Prioritizing Visual Features for LLMs](https://arxiv.org/abs/2608.09006)

**<font color=#1a73e8>作者：</font>** Shiwei Gan, Xiao Liu, Yafeng Yin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved remarkable success across a wide range of tasks. However, fine-tuning LLMs for Gloss-Free Sign Language Translation (GFSLT) remains a challenge. In this paper, we investigate how to effectively adapt LLMs to the GFSLT task. We show that there are two key issues that need to be solved: (1) the inherent distributional gap between visual feature inputs and text feature inputs makes it difficult for LLMs to interpret visual inputs; and (2) existing approaches typically concatenate visual and textual features in an autoregressive framework, which leads to the model overemphasizing textual inputs and deprioritizing visual cues, as LLMs are pretrained predominantly on text-centric data. To address the first challenge, we propose a simple yet effective method named Filtered Pseudo-Gloss CTC Pretraining, which leverages filtered pseudo-gloss sequences generated from text sequences to supervise the training of the visual backbone. To tackle the second issue, we introduce a Visual-Prioritized Distillation training strategy. Specifically, we define a visual-only prediction path in which text inputs are masked, and the model is required to generate the target sequence relying solely on visual inputs. To guide this path, the outputs from the standard visual-textual prediction are then distilled into the visual-only prediction path, encouraging the model to prioritize visual features. Comprehensive experiments and qualitative analyses demonstrate the effectiveness of the proposed model. The proposed SignLlama achieves very competitive performance on multiple datasets for GFSLT tasks, without using any extra modalities or external sign language datasets for pretraining.

---


### 271. [Dynamic Distribution-Aware Uncertainty Tracking in Vision-Language Representation Learning](https://arxiv.org/abs/2608.09011)

**<font color=#1a73e8>作者：</font>** Ao Zhou, Zhiwei Jiang, Zifeng Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty Quantification (UQ) aims to measure the reliability of model predictions, serving as a critical safeguard for deploying Vision-Language Models (VLMs) in safety-critical scenarios. Post-hoc approaches are widely adopted due to their lightweight nature, mapping the outputs of VLMs to uncertainty measures through learnable modules or inductive summarization. However, Post-hoc approaches remain inherently confined to fitting the failure patterns of the source domain, ignoring the dynamic nature of test distributions. To address this challenge, we propose a Dynamic Distribution-Aware Uncertainty Quantification framework (DDA-UQ) that shifts the paradigm from static mapping to a dynamic distribution-aware process. During training, we leverage a Gaussian Mixture Model to model the VVLMs'embedding space and extract distributional evidence, thereby dynamically deriving uncertainty estimates. During inference, the design dynamically responds to changes in the data distribution. Extensive experiments demonstrate that our approach significantly outperforms state-of-the-art methods.

---


### 272. [How People Evaluate AI-, Expert-, and Peer-Style Financial Advice](https://arxiv.org/abs/2608.09019)

**<font color=#1a73e8>作者：</font>** Aryan Ramchandra Kapadia, Eshwar Chandrasekharan, Koustuv Saha  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As generative AI increasingly becomes a common source of daily decision-making, including financial choices, it is critical to understand how people evaluate AI-generated financial advice. We conducted a preregistered vignette experiment (N = 285) in which substantive financial content---including facts, numerical values, recommendation direction, and core reasoning---was held constant while communication style varied across AI Financial Assistant (AI), Certified Financial Planner (Expert), and Online Community Forum (OC) advice. Displayed source attribution was independently manipulated through correctly labeled, unlabeled, and mislabeled conditions, allowing us to separate attribution effects from source-specific communication cues. Expert advice was rated more favorably than AI advice on 9 of 10 outcomes (|d|=0.20--0.47), and this advantage remained visible without source labels, where Expert advice outperformed AI advice on 8 of 10 outcomes (up to d=0.60). Correct labels added limited differentiation, whereas mislabeling increased ratings of AI advice for situational fit and overall quality (d=0.42 for each) and attenuated the Expert advantage in situational fit (d=-0.36). Descriptive analyses further showed that AI advice was most responsive to displayed attribution and, conversely, that advice-style differences were most visible under an AI label. These findings show that financial-advice evaluations are shaped jointly by displayed attribution and message-level communication cues. We position disclosure not as a neutral transparency mechanism, but as an interpretive frame whose accuracy and interaction with message cues can shape trust and reliance.

---


### 273. [PolicyKG: An Agentic LLM Pipeline for Translating Institutional Policies into SHACL Knowledge Graphs](https://arxiv.org/abs/2608.09028)

**<font color=#1a73e8>作者：</font>** Ponkrit Kaewsawee, Chaklam Silpasuwanchai, Chutiporn Anutariya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Institutional policies stay in natural language while the systems that check compliance demand machine-readable constraints. Bridging that gap is still done by hand.
PolicyKG closes the loop. It is an LLM pipeline that reads a policy PDF, classifies each sentence as an obligation, permission, or prohibition, lifts the label into first-order deontic logic, and emits SHACL constraints. Four stages run on a LangGraph state machine with per-stage validators. The piece that matters most is the Corpus Adapter: a YAML vocabulary registry that grounds LLM predicates in a target ontology. Retargeting to a new domain means swapping the registry, not retraining a model.
On the Asian Institute of Technology Policies and Procedures corpus (1,663 sentences, 443 rules), PolicyKG reaches 86.9% deontic classification accuracy (Cohen's kappa = .709). Three annotators independently re-label a 50-item sample and agree at Fleiss' kappa = .844. SHACL shape correctness on a 69-shape subset is F1 = .866. The FOL path handles 79.2% of rules; the rest go through a direct NL-to-SHACL fallback.
We audited every one of the 443 rules for second- or higher-order constructs. An automated regex checklist flagged none, and a first-author pass on the 92 FOL-fallback cases confirmed the same. The exact upper 95% Clopper-Pearson bound on the true HOL rate is 0.67%. This is an audit finding for one corpus, not a proof of FOL sufficiency for institutional policy.
Swapping the AIT registry for a GDPR registry raises exact property alignment from 1/15 to 11/15 (Fisher's exact p < .001; Cohen's h = 1.53). On the LexDeMod lease-contract benchmark (N = 200), Macro F1 drops to .370 because lease English uses "shall be entitled" for permission -- exactly the vocabulary mismatch registry swap is meant to fix. Repeated runs produce hash-identical SHACL outputs.

---


### 274. [Tree-of-Experience: Hierarchical Experience Management for Self-Evolving Agents](https://arxiv.org/abs/2608.09044)

**<font color=#1a73e8>作者：</font>** Zihao Deng, Yining Zhu, Leiming Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual self-evolution requires LLM agents to transform environmental interactions into reliable and reusable experience. Existing methods typically refine individual trajectories or abstract shared knowledge from related trajectories, but their experience representations are often disconnected from the underlying reasoning process. This limits feedback attribution, cross-task transfer, and update and retrieval efficiency, particularly in complex reasoning tasks with outcome-level feedback. To overcome this limitation, we propose \textbf{T}ree-\textbf{o}f-\textbf{E}xperience (ToE), a structured experience-management framework that aligns experience organization with the hierarchical reasoning process of LLM agents. Specifically, ToE organizes the experience into a shared tree of analytical perspectives and reasoning paths, whose reliability is calibrated through environmental outcomes to support systematic updating, transfer, and efficient retrieval. The experimental results on \textsc{Game of 24} and \textsc{FinEvolveBench} show that ToE substantially improves both problem-solving performance and efficiency. On \textsc{Game of 24}, ToE achieves a 31.4\% relative improvement in accuracy over the experience-free ToT baseline. On \textsc{FinEvolveBench}, ToE improves tsIC by an average of 41.24\% over the experience-free pipeline across 12 evaluation settings, whereas conventional experience-management methods often underperform experience-free baselines.

---


### 275. [Measuring the Tokenization Premium: A Cost Audit for Underserved Language Communities](https://arxiv.org/abs/2608.09046)

**<font color=#1a73e8>作者：</font>** Avijit Roy, Proma Roy, Hrishitva Patel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as general-purpose educational and technical assistance systems, but their underlying infrastructure does not treat languages equally. One underexamined source of disparity is tokenization: semantically equivalent content can require substantially different token counts across languages, affecting API cost, latency, and usable context length before a model is invoked. We introduce the Tokenization Equity Audit (TEA), a reproducible benchmark for measuring tokenization premiums in technical tutoring content. TEA evaluates three widely used tokenizers, GPT-4o's o200k base, Qwen2.5-7B, and Mistral-7B, on a 120-item Python debugging corpus translated from English into Bengali, Hindi, Arabic, Tamil, and Yoruba. Bengali and Hindi serve as the primary validated cases, while the remaining languages provide exploratory cross-script and cross-family comparisons. Across this corpus, Bengali requires (1.56\times) as many GPT-4o tokens as English, reducing a nominal 128k-token context window to an effective 82k-token English-equivalent capacity for the same semantic content. With the Qwen2.5 and Mistral tokenizers, Bengali requires up to (4.5\times) the English token count. Yoruba, despite using the Latin script, exhibits the highest GPT-4o tokenization premium at (2.37\times), indicating that tokenization inequity cannot be explained by script family alone. These results demonstrate that tokenization can create measurable economic and functional barriers, highlighting the need to treat tokenization as an equity-relevant infrastructure layer for underserved language communities, particularly where educational systems depend on low-cost or offline-capable AI tools.

---


### 276. [Security and Privacy Taxonomy Generation from Mobile App Reviews](https://arxiv.org/abs/2608.09049)

**<font color=#1a73e8>作者：</font>** Moghis Fereidouni, Vinaik Chhetri, Umar Farooq 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mobile app reviews are a rich, continuously renewing source of how users experience privacy and security, yet existing taxonomies of these concerns are hand-crafted and cannot keep pace with the evolving nature of the data. Automating taxonomy construction is the natural response, but scalability is the core challenge: current LLM- and clustering-based methods are developed for scientific corpora of a few thousand documents and do not extend to app review collections numbering in the hundreds of thousands. We address this gap in two ways. First, we filter app reviews for privacy- and security-related content, yielding a comprehensive corpus of over 600K reviews. Second, we introduce TaxoScale, a pipeline that handles taxonomy construction at this scale by extending an expert-defined taxonomy via Recursive Hierarchical Clustering and LLM-based node naming. TaxoScale outperforms strong automatic-taxonomy baselines on path, level, coverage, and novelty metrics, and discovers novel branches absent from prior taxonomies.

---


### 277. [Telemetry and Concealment in Self-Adapting Generative AI: Logging Architecture, Adversarial Model Hiding, and the Limits of Detection](https://arxiv.org/abs/2608.09069)

**<font color=#1a73e8>作者：</font>** Sriram Nagaraj  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model risk management (MRM) guidance assumes a static model lifecycle, in which models are developed, independently validated, and implemented without further autonomous modification. Continually self-adapting generative AI systems --- models that update their own weights during production deployment --- fundamentally violate this assumption and render point-in-time validation inadequate. This paper addresses the resulting governance problem in two parts. Part I develops a rigorous telemetry architecture for such models, operating simultaneously in discrete and continuous time. We establish a Minimal Sufficient Statistic for audit purposes, construct a tamper-evident Merkle chain for discrete weight sequences, derive the appropriate continuous-time generalization via the Ito formula, and propose event-driven logging via KL divergence stopping times that is both computationally tractable and meaningful for validation. Part II asks what happens when the model provider is adversarial. A firm deploying such a model has strong incentives to conceal learning updates that would trigger mandatory validation review. We formalize this as the Model Hiding Problem and provide a systematic taxonomy of six distinct attack strategies against the Part I architecture, spanning discrete and continuous time, with a formal countermeasure for each. Together the two parts establish a dual-regime architecture in which continuous telemetry is necessary but not sufficient, narrowing---but never replacing---periodic invasive audit. The framework is model-architecture-agnostic and is designed to satisfy the three pillars of traditional MRM.

---


### 278. [SLAC: Access-Driven CPU-to-GPU Side-channel Attacks via System-Level Cache on Apple Silicon](https://arxiv.org/abs/2608.09075)

**<font color=#1a73e8>作者：</font>** Tianhong Xu, Saion K. Roy, Ruyi Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern heterogeneous System-on-Chip designs integrate CPU cores and a GPU that share a last-level cache (LLC) or system-level cache (SLC). This sharing exposes a new cross-domain attack surface, and existing attacks on integrated platforms either exploit coarse-grained cache-occupancy contention or require the adversary to co-reside on the GPU with the victim to obtain accurate timing measurements. In this work, we target Apple Silicon heterogeneous SoCs and discover that GPU memory accesses leave set-level footprints in the shared SLC, observable to an unprivileged CPU process. This keen observation enables the first fine-grained, access-driven, Prime+Probe-style CPU-to-GPU cache side-channel attacks against GPU workloads. We first reverse-engineer the Apple M1 SLC set-indexing functions and the interactions between local private caches and the SLC. Building on these findings, we construct the CPrime+CProbe SLC side-channel technique, which monitors GPU victim activity from the CPU at cache-set granularity. We then introduce an accelerated variant, GPrime+CProbe, in which an adversary leverages the GPU for faster SLC priming, yielding a 6.4x increase in the covert-channel throughput. Lastly, we demonstrate two end-to-end privacy attacks using the new side-channels: a graph-edge reconstruction attack on Graph Neural Networks (GNNs) that achieves 90% edge accuracy across five datasets, and an LLM privacy attack that recovers input keywords with up to 94.8% accuracy and model responses with up to 88.9% accuracy across TinyLlama and GPT-2 Medium models. Our results reveal a new class of microarchitectural vulnerabilities in Apple Silicon and call for secure system cache designs for heterogeneous SoCs.

---


### 279. [When Confidence Fails: Overconfidence in LLMs under Uncertainty and Missing Clinical Information](https://arxiv.org/abs/2608.09080)

**<font color=#1a73e8>作者：</font>** Maryam Tahermazandarani, Adnan Mahmood, Fahmida Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved strong performance in medical question answering and clinical reasoning tasks. However, their reliability under uncertainty remains poorly understood which raises critical concerns for deployment in high-stakes clinical settings. In such environments, incorrect predictions are inherently risky, but confident incorrect predictions can be particularly harmful as they may mislead clinical decision-making. In this paper, we conduct a systematic behavioral analysis of LLMs under clinical information uncertainty. We propose an evaluation framework based on the MedMCQA dataset consisting of two complementary uncertainty settings. First, we introduce linguistic uncertainty cues through prompt modifications to simulate ambiguous clinical contexts. Second, we construct an answer removal setting, wherein the correct option is deliberately excluded mandating the model to recognize insufficient information and abstain. We analyze both model accuracy and confidence behavior using multiple calibration metrics including calibration gap, Expected Calibration Error (ECE), and Unsafe Confident Error Rate (UCER) across 500 medical questions. Our results reveal a consistent failure mode, i.e., although accuracy degrades under increasing uncertainty, model confidence remains misaligned with accuracy. This leads to a substantial increase in unsafe confident errors, indicating that model confidence remains largely insensitive to clinically meaningful information loss. Furthermore, we observe significant variation across models in their ability to abstain when the correct answer is unavailable, with some models persistently producing high confidence hallucinated answers. These findings expose critical limitations in the epistemic reliability of current LLMs and highlight the need for uncertainty aware evaluation methods prior to their deployment in clinical workflows.

---


### 280. [Who Bridges Safety? Identifying and Targeting Cross-Lingual Shared Safety Pathways](https://arxiv.org/abs/2608.09095)

**<font color=#1a73e8>作者：</font>** Shuyi Miao, Wangjie Qiu, Pengyang Shao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Uncovering the internal mechanisms underlying the safety capabilities of large language models (LLMs) is crucial for developing trustworthy artificial intelligence. Currently, mechanistic interpretability studies on multilingual safety are largely confined to local components, such as isolated neurons. However, this static and fragmented perspective overlooks the synergy among components and fails to elucidate how safety signals dynamically propagate within the model to drive safety decisions ultimately. In this work, we move beyond isolated neurons to identify and target the cross-layer functional pathways formed during safety signal propagation, thereby uncovering the mechanisms driving the cross-lingual safety gap. Specifically, we first identify monolingual safety pathways and validate their impact on refusing harmful requests. Subsequent cross-lingual analyses reveal a sparse subset of cross-lingual shared safety pathways, confirming that this intersection acts as the internal bridge transferring safety capabilities from high-resource (HR) languages to non-high-resource (NHR) languages. Building on these mechanistic findings, we propose a pathways-targeted alignment method based on the cross-lingual shared safety pathways. Experimental results show that updating only a small fraction of pathway parameters significantly improves safety in NHR languages while largely preserving the model's general capabilities.

---


### 281. [SI-Edit: Toward Sketch-Instruction Guided Local Image Editing with Pixel-Level Precision](https://arxiv.org/abs/2608.09097)

**<font color=#1a73e8>作者：</font>** Weixin Ye, Wei Wang, Hongguang Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid advances in generative models, achieving pixel-level precision in sketch-based image editing remains a persistent challenge, particularly for fine-grained local deformations. This gap stems primarily from the critical shortage of high-quality, publicly available benchmark datasets that jointly provide geometric constraints and semantic instructions. To address this issue, we first introduce **SI-Data**, a high-quality dataset specifically designed for instruction-guided local sketch editing. We develop an automated pipeline leveraging Multimodal Large Language Models (MLLMs) to synthesize comprehensive quadruplets comprising original images, local geometric sketches, semantic instructions, and corresponding edited images. By providing both reliable spatial anchors and explicit semantic intent, SI-Data uniquely enables collaborative spatial-semantic learning. Building upon this, we propose a collaborative framework called **SI-Edit** that integrates semantic instructions with precise geometric constraints. Furthermore, to address the lack of standardized evaluation, we establish a comprehensive set of metrics designed to measure both structural fidelity (e.g., sketch-to-edge alignment) and semantic adherence. Experimental results demonstrate that SI-Edit provides more reliable structural control than baselines for sketch-based image editing, and achieves precise, pixel-level local refinements aligned with user intent. The data and code are released on the [project page](this https URL).

---


### 282. [Real Data Closes Synthetic-to-Real Gap in Optical Chemical Structure Recognition](https://arxiv.org/abs/2608.09100)

**<font color=#1a73e8>作者：</font>** Yani Guan, Dengpan Dong, Zi Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Millions of chemical structures appear in patents and papers only as drawings, and using that information at scale requires reading the drawings. OCSR appears nearly solved on synthetic images yet remains difficult on real documents: the starting recognizer, Qwen2.5-VL-7B, exceeds 91% accuracy on synthetic renders but falls below 16% on three real-world benchmarks (ACS, CLEF-IP, USPTO). To identify the main source of improvement, 21 recognizers were fine-tuned on mixtures of synthetically rendered structures and labeled real depictions from patents, journal figures, and hand-drawn collections, varying the vision language model (VLM) base, the fraction of real training data, and the vision-tower adaptation strategy. Labeled real training images make the largest difference. For Qwen2.5-VL, ACS exact match rises from 0.15 with no real data to 0.37 at 9.5% and 0.46 at 50.2%; a controlled experiment across three base models reproduces the trend. A vision-tower LoRA, in contrast, does nothing for Qwen (+0.00, paired p=1.00), substantially helps InternVL3-8B (+22.8 to +34.6 pt), and modestly helps GLM-4.1V-9B (+1.0 to +9.6 pt), so its value depends on the base model. The best configuration reaches 0.96 exact match on clean renders and 0.49, 0.65, 0.84, and 0.76 on ACS, CLEF-IP, UOB, and USPTO, respectively. Gaps between base models are largest without real data (0.21), shrink to 0.06 at 70% real data, and reorder the ranking; base model and real-data mixture must therefore be selected together. Small-scale experiments on handwritten image-to-LaTeX recognition and chart-to-table conversion show that base-model rankings also vary beyond chemistry. More generally, model and adaptation choices for visual structure recognition should be evaluated on the target task.

---


### 283. [LexKairos: Benchmarking Legal Temporal Capabilities in LLMs](https://arxiv.org/abs/2608.09106)

**<font color=#1a73e8>作者：</font>** Chenyang Li, Zejia Feng, Yuqin Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong performance across a wide range of legal tasks. In legal practice, time is a critical concept that governs the validity of statutes, the progression of legal cases, and the enforcement of procedural deadlines. However, legal temporal capabilities remain underexplored in existing legal AI benchmarks. To address this gap, we propose LexKairos, a comprehensive benchmark for evaluating the temporal capabilities of LLMs in the Chinese legal context across three dimensions: statutory temporal knowledge, case temporal modeling, and statute-case temporal reasoning. LexKairos comprises nine sub-tasks drawn from real-world Chinese judicial cases and statutes. We conduct systematic evaluations of eight LLMs under multiple inference settings, including vanilla, Chain-of-Thought (CoT), and thinking modes. Our results show that Gemini-3-Flash achieves the strongest overall performance, yet even the best-performing model exhibits notable limitations on tasks demanding precise time-sensitive statutory metadata recall or complex reasoning in time limits, indicating that legal temporal knowledge and reasoning remain open challenges for current LLMs. Data and code are available at this https URL.

---


### 284. [Different Feedback, Different Updates: Selective Self-Learning from User Interactions for Large Language Models](https://arxiv.org/abs/2608.09109)

**<font color=#1a73e8>作者：</font>** Xuanchen Li, Haitao Li, Yujia Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> User feedback offers natural supervision for persistent LLM improvement, but a single message may support multiple behavioral changes with different scopes of generalization. We introduce SLIFT, a selective self-learning framework built on a task-relative view of user feedback. SLIFT decomposes each feedback message into atomic components and interprets each component relative to the original task as Fix, Spec, or Null: requirements for task validity, compatible condition-specific refinements, or content with no reliable positive update direction. To incorporate each change at the appropriate scope, SLIFT trains two complementary LoRA adapters on a shared frozen backbone: a Generalist that consolidates Fix requirements into default behavior through feedback-conditioned self-distillation, and a Specialist that observes only the task and Generalist response to supply residual guidance for applicable, unmet Spec refinements. Null components induce no positive update. Across backbones, SLIFT achieves strong performance on both MemoryBench and WildFB, with targeted analyses further examining its underlying mechanisms. We release our code at this https URL.

---


### 285. [RAVEN-Eval: Rubric-Guided Automatic Evaluation for AI Video Generation Models Based on LMM Preference Judgement](https://arxiv.org/abs/2608.09111)

**<font color=#1a73e8>作者：</font>** Ziheng Jia, Jiaying Qian, Zicheng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI video generation has advanced rapidly and entered widespread commercial use. As a result, quality differences among videos produced by state-of-the-art AI video generation models~(AIVGMs) have become increasingly difficult to discern using conventional evaluation criteria, such as visual fidelity and semantic instruction following. Meanwhile, human evaluation now requires more expertise and sustained attention, substantially increasing annotation costs. This calls for automated evaluation that can reliably distinguish fine-grained differences among advanced AIVGMs with minimal human intervention. To address this challenge, we present RAVEN-Eval, a rubric-guided automated evaluation framework for AIVGMs, built primarily on the LMM-as-a-judge paradigm. Through an automatic task curation and quality-filtering pipeline, RAVEN-Eval curates 150 text-to-video~(T2V) tasks and 100 image-to-video~(I2V) tasks, and systematically collects more than 4,500 AIGVs. At its core, RAVEN-Eval adopts rubric-guided automated LMM preference judgement, in which LMM judges conduct pairwise comparisons according to task-specific rubrics. It further introduces an anchor-based model insertion approach to reduce the evaluation cost of incorporating new models. Finally, we evaluate 20 high-performance AIVGMs, as well as the judging capabilities of 13 LMM judges, and establish the RAVEN-Eval Leaderboards. Overall, RAVEN-Eval paves a scalable path for automatic and trustworthy evaluation of rapidly evolving AIVGMs.

---


### 286. [Motif 3: Technical Report](https://arxiv.org/abs/2608.09119)

**<font color=#1a73e8>作者：</font>** Junghwan Lim, Joon Son Chung, Sungmin Lee 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Motif 3, a decoder-only Mixture-of-Experts language model with 314 billion total parameters and 13.2 billion activated per token. Each sparse MoE layer contains 384 routed experts, with eight selected per token. This fine-grained sparsity provides substantial expert capacity while limiting computation. Motif 3 is built around Grouped Differential Latent Attention (GDLA), which integrates grouped differential attention with the compressed key-value representation of Multi-head Latent Attention. The architecture further incorporates modified manifold-constrained hyper-connections, Expert Specific PolyNorm activations, and multi-token prediction to improve optimization stability, expert specialization, and inference efficiency. We pretrain Motif 3 on approximately 12.5 trillion tokens spanning web documents, STEM, code, mathematics, multilingual content, and domain-specialized corpora. Expert-balancing and numerical-stabilization techniques support stable training at scale, while selective MXFP8 computation and communication, memory-efficient fused kernels, and window-aware context parallelism enable training with context lengths up to 256K tokens. Our post-training pipeline combines general supervised fine-tuning, six specialist teachers trained with reinforcement learning, a software-engineering teacher trained with supervised fine-tuning, and Multi-teacher On-Policy Distillation. The resulting unified model consolidates complementary capabilities in reasoning, coding, tool use, professional work, long-context understanding, calibrated abstention, and instruction following. Across a broad evaluation suite, Motif 3 demonstrates competitive performance against leading open weight models, including strong results on long-horizon agentic tasks, mathematical reasoning, scientific knowledge, and hallucination-sensitive evaluation.

---


### 287. [MELLON - Multimodal Enhanced LLM for Online Navigation](https://arxiv.org/abs/2608.09121)

**<font color=#1a73e8>作者：</font>** Ruiyu Li, Haoyang Cai, Zhitong Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web navigation agents are capable of addressing various types of tasks on different websites. Current baselines on web navigation are either unimodal or lack strong reasoning abilities given multimodal inputs. Focusing on the WebShop benchmark, a real-world website simulation, we explore the alignment of text and images, as well as multimodal reasoning and planning abilities, to enhance the performance of web navigation agents. We propose three innovative multimodal enhancements: Multimodal Enhanced LLM for Online Navigation (MELLON), VQAgent, and Multimodal Ranker. MELLON demonstrates a significant improvement in task completion accuracy, with a 9.26% increase after just one epoch of training. Our findings suggest the necessity of further exploration into multimodal approaches, with a focus on more extensive training and alignment strategies to enhance the effectiveness of web navigation agents.

---


### 288. [Visual Distortion Detection in UGC Images Using Large Multimodal Models](https://arxiv.org/abs/2608.09122)

**<font color=#1a73e8>作者：</font>** Ziheng Jia, Yingji Liang, Jiaying Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The localized depiction of perceptual quality has long been a crucial, yet underexplored, challenge in image quality assessment (IQA). Existing approaches based on large multimodal models (LMMs) predominantly rely on text-driven supervised fine-tuning (SFT).
However, this training paradigm exhibits notable limitations in detection accuracy. Moreover, synthetically distorted images, which are often used as the primary training data source,
show a significant generalization gap when deployed in real-world scenarios; thus, the \textbf{synthetic-to-authentic (\textit{S2A})} problem represents a critical challenge. Motivated by these issues, we propose \textbf{\textit{VIGIL}}, which leverages the LMM architecture for precise visual distortion detection. From a candidate pool of over 1000K samples, we construct the \textbf{\textit{VIGIL-140K}} training set, which consists of over 140K distorted images. These images are obtained through rigorous quality filtering and carefully crafted distortion injection, covering 8 major synthetic distortion categories.
Our model leverages different layers of the large language model (LLM) decoder, treating them as \textit{multiple detectors} that perform synchronous distortion detection using multi-level features. Additionally, we retain distortion cues from predictions assigned to the non-distortion class, which helps mitigate the ambiguous foreground-background (\textit{FG-BG}) separation commonly encountered in the \textit{S2A} problem.
After post-processing, our model consistently outperforms strong baselines on both in-domain synthetic distortion detection and \textit{S2A} tasks.

---


### 289. [RISE-RL: Rubric-Informed Selective Exploration for Open-Ended Reinforcement Learning](https://arxiv.org/abs/2608.09123)

**<font color=#1a73e8>作者：</font>** Jinkun Hou, Zhuo Liu, Huimin Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligning Large Language Models (LLMs) for open-ended tasks is challenging because responses must satisfy multidimensional criteria without following a single correct generation trajectory. Existing rubric-based reinforcement learning (RL) methods compress fine-grained criterion-level feedback into scalar rewards, making persistent capability gaps difficult to target under limited on-policy exploration. We propose $\textbf{RISE-RL}$ (Rubric-Informed Selective Exploration), which uses repeatedly missed rubric criteria to elicit privileged trajectories that are difficult to discover through unguided exploration alone. RISE-RL retains only trajectories whose complete-rubric reward exceeds the mean reward of natural rollouts, and then re-evaluates them under the original prompt to emphasize behaviors that remain weakly supported by the natural policy. The resulting guidance signal is optimized through a separate auxiliary objective and removed once its additional benefit diminishes. Experiments with 4B and 14B models across writing, chat, health, and science show that RISE-RL achieves the highest mean score on every evaluated benchmark under guidance-free evaluation. Compared with standard Rubric-RL, it improves the average score by 1.3 points at the 4B scale and $\textbf{3.3 points at the 14B scale}$, including a $\textbf{6.0-point}$ gain on CreativeWriting-V3. It also improves creative-writing diversity and yields gains on objectively scored medical and scientific benchmarks. These results indicate that selective internalization through reward filtering and policy support shaping is effective for open-ended reinforcement learning.

---


### 290. [ChronoState: Hidden Elapsed-Time Conditioning for Temporal-State Action Selection in Frozen-Backbone Language Models](https://arxiv.org/abs/2608.09124)

**<font color=#1a73e8>作者：</font>** Sam Siavoshian, Omar Ramadan, Amir K. Saeed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Temporal decisions in language-model systems often depend on both symbolic task state and elapsed wall-clock time, such as cache expiration, job completion, quota resets, deadlines, or stale sessions. We study whether elapsed time can be supplied as a non-token, system-side scalar and composed with visible symbolic state by a frozen-backbone language model. We introduce ChronoState, a compositional temporal-state benchmark in which symbolic state appears in the prompt, elapsed seconds tau are supplied through a hidden chronometric-injection channel, and the model selects a forced-choice temporal action. Here, "hidden" means hidden from the user-visible token sequence, not from model computation. Using Qwen2.5-3B-Instruct as a frozen bf16 backbone with a 31-dimensional sinusoidal-plus-log time encoding, gated FiLM residual modulation, and a rank-8 LoRA action surface, hidden-time CI reaches 0.9305 +/- 0.0134 accuracy and 0.9410 +/- 0.0103 balanced accuracy. No-time and shuffled-time controls fall to 0.5511 +/- 0.0042 and 0.3323 +/- 0.0097, respectively, with high shuffled-time wrong-state consistency supporting causal dependence on the injected scalar within the trained distribution. Generalization remains strong for held-out templates, durations, and multi-constraint compositions, but held-out quota-family transfer is weak at 0.5065 +/- 0.0559, while a fair prompt+LoRA timestamp baseline reaches 0.9893 +/- 0.0052. Thus, ChronoState supports a narrow conclusion: hidden elapsed time can be composed with symbolic task state under direct supervision, but does not establish autonomous time tracking, broad unseen-family abstraction, or superiority over prompt-injected timestamps.

---


### 291. [Subjective Multi-Bias Detection with Large Language Models](https://arxiv.org/abs/2608.09126)

**<font color=#1a73e8>作者：</font>** Ruiyu Li, Zhiying Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this project, we delved into the pervasive challenge of bias detection within the text content. More specifically, our focus lies on the identification of subjective bias, a type of bias that introduces improper attitudes or portrays a statement at odds with the actual truth. The subjective bias can jeopardize the authenticity and reliability of texts, leading to misconceptions and potential social tensions, especially when expressed through offensive language.
Following prior work [1], we tackled with three different types of subjective biases in text: (1) framing bias with the use of one-sided words or phrases containing a particular point of view; (2) epistemological bias which includes subtle linguistic features that can affect the believability of the texts; (3) demographic bias with word/phrase usage under presuppositions of a particular demographic factor (i.e., gender or religion).
In terms of the data we utilize, the input consists of texts that may harbor subjective biases. The output is a classification or annotation that reveals the presence or absence of such biases within the provided content. More specifically, we detected three different types of multi-span biases in corpus WIKIBIAS [2] with more than 4,000 sentence pairs from Wikipedia edits. The data is labelled by bias type for span pairs with the following categories: (1) framing bias, (2) epistemological bias, (3) demographic bias, and (4) no bias. The project codes are released at this https URL.

---


### 292. [Social Gym and SPaRTan: Benchmarking and Improving LLM Social Reasoning via Multi-Agent Game Tournaments](https://arxiv.org/abs/2608.09128)

**<font color=#1a73e8>作者：</font>** Keyu He, Xuhui Zhou, Maarten Sap  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly deployed in multi-agent social settings where they must cooperate, negotiate, and adapt to other agents. Measuring and improving these social skills is hard because, unlike math or logic, social interaction offers no objective ground truth: evaluations fall back on LLM judges, which are costly, subjective, and noisy, and models get no reliable signal to learn from. To address both, we first introduce Social Gym, an environment of 21 multi-agent social games (e.g., Werewolves, Resistance, Spyfall) whose rule-decided outcomes make agent performance verifiable and objective, with an Elo tournament that produces a cross-game leaderboard. Benchmarking experiments show that while GPT-5-mini tops the leaderboard, no model excels at all games uniformly or in all game roles, pointing to limitations of social reasoning. Motivated by this, we additionally propose SPaRTan (Self-Play and Reflect-Transfer), a training-free self-improvement loop: a model plays a game, reflects on its trajectories and their outcomes to produce a transferable playbook, and applies that playbook in subsequent games. Our results show that SPaRTan playbooks help GPT-5-mini agents level their performance on weaker roles, but largely do not improve Qwen3-32B's performance. Together, Social Gym and SPaRTan offer a reproducible, verifiable foundation for measuring and improving LLM social reasoning without weight updates.

---


### 293. [Beyond Direct Identifiers: Probabilistic Privacy Risk Estimation for Privacy-Conscious LLM Query Delegation](https://arxiv.org/abs/2608.09140)

**<font color=#1a73e8>作者：</font>** Li Siyan, Zhou Yu, Julia Hirschberg  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent work on protecting privacy during user-LLM interactions often focuses on direct, explicit identifiers: the personally-identifiable information (PII) captured by standard detectors. One such approach is Privacy-Conscious Delegation (PCD), where a local LLM acts as an intermediary. However, privacy risk does not stem solely from explicit identifiers but also PII-free self-disclosures, leaving users identifiable through combinations of quasi-identifying traits. We investigate a probabilistic variant of PCD, where we augment its objectives with an LLM-driven probabilistic estimation of k-anonymity. To facilitate this, we first create the PUPA-SD dataset, which contains naturalistic user queries with self-disclosure. Our preliminary results indicate that optimizing PAPILLON on PUPA-SD improves quality on unseen conversations across a variety of local models and produces the best privacy-utility balance for Llama-3.2-3B, while smaller models struggle to jointly optimize quality and privacy. We propose k-anonymity as a useful auxiliary metric for tackling PCD.

---


### 294. [An Agentic Generative Large Language Model for Treatment Planning of Colorectal Cancer](https://arxiv.org/abs/2608.09142)

**<font color=#1a73e8>作者：</font>** Mengxian Lyu, Cheng Peng, Tim Jang 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Treatment planning in precision oncology requires synthesizing heterogeneous patient information with rapidly evolving clinical guidelines to ensure guideline-concordant care. While large language models (LLMs) show promise in many diagnostic tasks, their adoption for high-stakes treatment planning is hindered by complex reasoning, adherence to timely clinical guidelines, and safety concerns. In this study, we present GatorOnco, an agentic LLM for colorectal cancer (CRC) treatment planning. GatorOnco is developed using a total of 282 billion tokens of biomedical text, including healthcare system-scale clinical text comprising 166 billion tokens from UF Health. We implemented a domain-adaptation method that integrates pre-training, model merging, a two-stage post-training approach, and agent-based reinforcement learning. An agentic retrieval-augmented generation (RAG) approach dynamically integrates time-sensitive clinical guidelines into the reasoning process. In a blind, randomized clinical evaluation conducted by five UF Health oncologists, GatorOnco significantly outperformed open-source LLMs (P < 0.01) and achieved expert-level performance comparable to UF Health oncologists. Compared with expert oncologists, GatorOnco received significantly higher ratings for readability (4.46 vs. 4.19, P < 0.01) and completeness (3.91 vs. 3.52, P < 0.01), while showing statistically comparable performance in correctness (4.09 vs. 4.11, P = 0.921), currency (4.04 vs. 3.98, P = 0.478), and safety (4.22 vs. 4.22, P = 0.999). These findings demonstrate that integrating agentic reasoning with large-scale domain adaptation can help bridge the gap for generative AI in high-stakes cancer treatment planning.

---


### 295. [Right Answer, Wrong Heat: Explanation-Aware Evaluation and Thermal-Grounded Feedback for MLLMs on Infrared Images](https://arxiv.org/abs/2608.09145)

**<font color=#1a73e8>作者：</font>** Yongsong Huang, Xiaofeng Liu, Tomo Miyazaki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> General-purpose multimodal large language models (MLLMs) are increasingly applied to infrared images, where they are commonly scored by answer accuracy alone. However, a correct answer does not ensure that the model's explanation is grounded in infrared thermal evidence. We introduce an explanation-aware evaluation framework that separates answer correctness, output-level explanation groundedness, and thermal grounding for infrared visual questions. Using a Dual-LLM Consensus Judge with a preliminary human-anchor calibration check, we find that correct answers can still rely on weak or visible-light evidence; withholding the original infrared image and showing only a visible-like rendering erodes thermal grounding with little accuracy change; and this erosion is observed most strongly for more capable models but disappears when infrared remains available. We further propose Thermal-Grounded Feedback (TGF), a training-free feedback loop that diagnoses explanation-side failures and revises the explanation while preserving the selected answer. On local paired-input validation, TGF improves explanation-side grounding without changing answers. These findings suggest that future trustworthy MLLMs for infrared scene understanding should be evaluated and developed to produce thermally grounded explanations rather than merely accurate answers.

---


### 296. [RefineAny3D: Depth Refinement as Semantic Alignment for Monocular 3D Detection](https://arxiv.org/abs/2608.09147)

**<font color=#1a73e8>作者：</font>** Zhihao Zhang, Gengwei Zhang, Tianlong Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular 3D object detection spans two regimes: closed-set detectors operating within a fixed category vocabulary, and open-vocabulary detectors that localize arbitrary categories by leveraging depth foundation models for 3D geometry. We find that current depth foundation models, despite their strong zero-shot generalization, lack the object-level precision 3D detection demands: substituting a state-of-the-art depth foundation model for a strong detector's predicted depth degrades accuracy, even falling below the detector's own prediction. Rather than pushing detectors or depth models to be more accurate end-to-end, we treat object-level depth refinement as a stand-alone task and present RefineAny3D, a vision-language model that corrects depth without ever predicting a numerical value. Our key insight is that depth error has a direct visual signature in image space: when projected onto the image, a correctly placed box tightly encloses the object, while a too-far box projects too small and a too-close box projects too large. Depth refinement thus reduces to a visual alignment problem rather than a metric regression problem, which we instantiate by extending the VLM's vocabulary with action tokens that replace numerical depth output with categorical decisions, and by supervising the model on a large-scale chain-of-thought dataset that grounds each decision in explicit visual evidence. Applied as a single post-hoc step, RefineAny3D delivers consistent gains across closed-set detectors, open-vocabulary detectors, and 3D auto-labeling tools, and generalizes to novel categories, scenes, and cameras without retraining.

---


### 297. [UNSPECIFIC: General Constraint Synthesis for Breaking Copy-and-Paste Shortcut in LLM Instruction Following](https://arxiv.org/abs/2608.09154)

**<font color=#1a73e8>作者：</font>** Jeet Sharma, Balpreet Kaur, Jeremiah Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly expected to follow long lists of constraints in complex instructions, and synthesizing instructions from a reference document (i.e., back-translation) is a widely used method to measure/enhance LLMs' ability to follow complex instructions. However, this method introduces a critical loophole: the constraint synthesis model copies text from the reference as a very specific constraint and the evaluated LLM trivially satisfies the constraint by copying its text in the response. To address these issues, we propose UNSPECIFIC, a novel framework that synthesizes constraints common to two similar reference articles to reduce copy-pasting, selectively hardens only trivially satisfied constraints to balance difficulty and naturalness, and evaluates satisfaction on both the generated article and its summary to penalize superficial instruction following. Consequently, we built the UNSPECIFIC benchmark on news, story, and blog domains to analyze the copy-pasting behavior of LLMs. Our results show that our synthesized constraints are not only more challenging (e.g., the satisfaction rate of GPT-5 Mini drops from 90% to 78%) and natural (LLM win-rate gap improves by 30%) from a human perspective but also mitigate the copy-pasting. We also find that a large portion of constraints are satisfied superficially (i.e., not satisfied in the core narrative of the article). The code and datasets are released at this https URL.

---


### 298. [Beyond Tier Labels: Role- and Deployment-Dependent Model Substitution in Multi-Call LLM Workflows](https://arxiv.org/abs/2608.09155)

**<font color=#1a73e8>作者：</font>** Renxiang Wang, Jiaming Cui  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large multi-call LLM systems pose a scientific problem that query-level routing does not capture: the value of a model depends on where it enters a dependent computation and on the deployment that surrounds that call. Existing routers typically decide \emph{where} to spend a stronger model while treating the benefit of the substitution itself as known. We separate these two decisions through a predicate-action factorization and evaluate it in controlled solve-merge-verify workflows spanning 8-64 solve calls and four three-tier model ladders. The resulting evidence reveals a consistent principle beneath apparently conflicting outcomes. On numeric frequency counting, all-strong reduces RMSE from 4.818 to 1.538 in the Mixed Qwen/GPT ladder, whereas the average Qwen-only ordering reverses. Input-matched interventions further show that the same medium-to-strong action has sharply different value across roles and scales. A semantic task-and-contract shift reverses the Mixed ordering again, while allocation ablations distinguish useful sparse placement from under-coverage and indiscriminate escalation. Together, these results establish model substitution as a deployment-conditioned action rather than a property implied by a tier label, and they provide a practical sequence for large-scale workflow routing: calibrate the action, resolve its role-conditioned effect, and then optimize its placement.

---


### 299. [SwiftQK: Fast and Communication-Efficient Tensor Parallelism for Query-Key Normalization](https://arxiv.org/abs/2608.09160)

**<font color=#1a73e8>作者：</font>** Gyudong Kim, Wonjun Han, Young Geun Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Query-Key Normalization (QK-Norm) improves the training stability and quality of modern Large Language Models (LLMs). However, under Tensor Parallelism (TP), layerwise QK-Norm introduces additional cross-GPU communication because the normalization factor depends on the full hidden vector. We present SwiftQK, a multi-GPU RMSNorm kernel that exchanges only scalar normalization statistics and overlaps the remaining Peer-to-Peer reduction with independent element-wise computation in a deadlock-safe persistent kernel. Evaluations on recent LLMs show that SwiftQK reduces QK-Norm latency by 81.4--93.9% relative to the standard TP QK-Norm using full-vector All-Gather. In end-to-end serving, SwiftQK reduces TPOT on average by 29.5% over the All-Gather-based baseline and by 14.3% over an optimized scalar-aggregation implementation.

---


### 300. [CIDER: A Dataset of Contextual Disclosure Boundaries for Privacy Preference Alignment](https://arxiv.org/abs/2608.09164)

**<font color=#1a73e8>作者：</font>** Bingcan Guo, Eryue Xu, Jijie Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligning large language models (LLMs) with human privacy preferences requires capturing individuals' disclosure boundaries beyond general privacy norms. However, a gap remains in eliciting such nuanced preferences to evaluate alignment in realistic settings. We introduce CIDER, a dataset of 14,850 human annotations from 169 users, forming 1,650 contextual disclosure boundary sets across 60 interpersonal communication scenarios involving information sharing that violates privacy norms. Each boundary represents a real user's disclosure decisions over 9 sharing variants in a scenario, for a given communication role and AI-mediated condition. We formulate a task in which models predict a user's disclosure decision from historical boundaries, with varying levels of contextual information. Across 12 open and proprietary models, in-context personalization improves prediction accuracy by up to 11.41 percentage points using only 6 historical examples. Larger models such as GPT-5.4 (with medium reasoning effort) and Claude Sonnet 4.6 are better at leveraging semantic context to understand user-specific, context-dependent disclosure preferences for more accurate predictions, while smaller models tend to rely on structured heuristics based on disclosure granularity and identifiability. Personalization generally improves prediction accuracy, but the improvement is often accompanied by imbalanced shifts in false-positive and false-negative rates across models, with only Claude Sonnet 4.6 achieving balanced improvements in both. Our findings reveal both the promise and limitations of inference-time personalization for privacy preference modeling and position CIDER as a resource for advancing personalized privacy alignment.

---


> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
