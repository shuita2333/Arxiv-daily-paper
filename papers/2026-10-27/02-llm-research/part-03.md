# 🧠 大模型相关研究 | 2026年10月27日

> 本类共 **204** 篇论文：已确认 **185** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-204](./part-05.md)

---

### 101. [Angular Supervision for Visual Object Grounding in Autoregressive Vision-Language Models](https://arxiv.org/abs/2610.32220)

**<font color=#1a73e8>作者：</font>** Parsa Esmaeilkhani, Longin Jan Latecki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive vision-language models (VLMs) struggle to ground generated text in the correct image regions, and existing explainability methods, such as attention maps and Logit Lens, often produce poor spatial explanations due to weak text-to-vision attention and sink tokens. We propose \textbf{Angular Relevance} ($R_L$), a simple visualization measure based on cosine similarity between visual token embeddings and unembedding-matrix rows. Because $R_L$ is invariant to token norm, it produces substantially sharper and more faithful heatmaps than attention maps or Logit Lens on out-of-the-box models. Without any training, $R_L$ yields competitive referring-expression segmentation (RES), outperforming prior diagnostic maps and CLIP-based training-free methods. To preserve localized object information during cross-modal mixing, we introduce \textbf{Angular Object-Aware Loss (AOL)}, an auxiliary loss that directly supervises visual token embeddings to align angularly with the vocabulary directions of their corresponding object concepts. Finetuning with AOL alongside the standard next-token prediction objective significantly sharpens object localization in heatmaps, showing that the VLM's own visual tokens can be used directly for grounding and improving RES, without training any segmentation heads and without degrading general VQA performance. We further demonstrate that the learned grounding also transfers to category-level segmentation of object categories not seen during training.

---


### 102. [RxnExBench: Benchmarking Vision-Language Models for Structured Chemical Reaction Extraction from Scientific Literature](https://arxiv.org/abs/2610.32221)

**<font color=#1a73e8>作者：</font>** Jiaxing Sun, Junyuan Gao, Ruikang Zhang 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Screen Tables and Substrate Scopes are information-dense figures widely used in synthetic chemistry literature, yet automated extraction of structured reaction data from them remains challenging. We introduce RxnExBench, a multimodal benchmark for fine-grained reaction-level evaluation. Built from high-impact chemistry journals, it contains 3,565 expert-annotated reactions and 2,361 molecular structures. The dataset adopts a unified schema with 15 reaction roles and 26 core fields, supporting downstream AI-for-Chemistry tasks such as retrosynthetic planning, yield prediction, and reaction condition recommendation. RxnExBench further provides a reasoning-driven difficulty taxonomy, a modular annotation pipeline, and the Oracle-MolRec protocol, which disentangles molecular recognition from higher-level reasoning. Evaluation of 9 state-of-the-art VLMs shows that performance degrades substantially as schema complexity and reasoning demands increase. Under the Oracle-MolRec setting, results further reveal that accurate molecular recognition alone is insufficient, with multimodal integration and chemistry-aware reasoning remaining the primary bottlenecks. We release all data and code to facilitate future research in chemistry-aware multimodal understanding and AI-for-Chemistry dataset construction. The dataset and code will be released at this https URL.

---


### 103. [Correct Answers, Closed Gates: SolveBind for GUI Agents at the Verification Barrier](https://arxiv.org/abs/2610.32223)

**<font color=#1a73e8>作者：</font>** Xinhao Song, Haoxuan Peng, Su Su 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Websites and applications deploy CAPTCHAs and anti-automation mechanisms that use behavioral signals such as interaction trajectories and timing, not outcomes alone, to distinguish humans from automated agents. We call these protected GUI environments, where correctly solving a verification task is insufficient for end-to-end task completion. Agents must turn solver outputs into accepted interactions and adapt execution to runtime feedback under time constraints. We introduce SolveBind, a GUI-agent framework combining hierarchical solving with runtime supervision. A hierarchical solving tree decomposes verification into interdependent Perceive, Ground, Solve, Act, and Verify capabilities. A runtime supervisor grounds action commitments in tool-derived evidence, revises them as evidence arrives, and mediates execution under explicit recovery budgets. Across nine CAPTCHA task families and nine backbone models, SolveBind achieves the highest success rate on eight backbones, outperforming the strongest baseline by 13.3-34.5 percentage points. It achieves the highest success rate on all six AndroidWorld backbones. In a paired GPT-5.5 analysis, MobileAgent produces correct answers but fails dynamic verification on 13 of 90 tasks; SolveBind succeeds on seven of these tasks. With automatic submission, removing binding reduces success from 82.22% to 71.56% and increases latency and token usage. Recovery caps reduce execution cost with a small observed success trade-off: removing them raises success from 82.22% to 83.56%, while increasing latency and token usage to 3.7x and 2.4x their full-supervision values, respectively. These results support evidence-grounded execution control while identifying a success-cost trade-off in recovery and failure boundaries of heuristic submission rules.

---


### 104. [Training an MoE LLM in MXFP4: How We Closed the Gap to BF16](https://arxiv.org/abs/2610.32229)

**<font color=#1a73e8>作者：</font>** Han Wang, Zhitao Wang, Natalia Frumkin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training large language models (LLMs) in sub-8-bit arithmetic promises substantial gains in memory bandwidth and compute throughput, yet FP4 formats introduce quantization error severe enough to destabilize optimization if left unaddressed. We present ALTO, an open-source training recipe for GPT-OSS-20B, a 20-billion-parameter mixture-of-experts (MoE) model, on the MLPerf Small MoE Training benchmark under the MXFP4 microscaling format. The recipe combines established techniques from Abecassis, Felix et al. [arXiv:2509.25149] (hybrid 1D/2D block quantization, randomized Hadamard transforms, and stochastic rounding) with a simplified weight de-oscillation scheme adapted from TetraJet-v2 [arXiv:2510.27527]. On C4 validation at global batch size 16, MXFP4 + RHT + SR + de-oscillation reaches a validation loss of 3.3350 at 16,128 steps, only 0.007 above the BF16 baseline (3.3283), closing roughly 50% of the gap left by MXFP4 without de-oscillation (3.3418). Measured by steps to reach the MLPerf quality target (validation loss 3.34), de-oscillation cuts the FP4 convergence overhead relative to BF16 from +20.0% to +5.0%. We also report negative end-to-end results from differential gradient estimation, outlier clipping, and macro-block scaling, despite each showing operator-level SNR gains. All experiments use simulated MXFP4 kernels on AMD MI300 hardware and wall-clock speed has not been optimized.

---


### 105. [Correct but Unselectable: The Hidden Interface Tax in Multi-Candidate Reasoning](https://arxiv.org/abs/2610.32235)

**<font color=#1a73e8>作者：</font>** Qianli Ma, Zhiqing Tang, Fanshuai Meng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small language models deployed under cost, latency, or privacy constraints cannot simply switch to larger models when reasoning fails. Multi-candidate generate-then-rerank offers a natural test-time scaling route. However, more candidates do not always yield higher accuracy. We identify a previously overlooked bottleneck between generation and selection: a correct answer may appear in the candidate pool yet fail to be selected because it is incomplete, unparseable, or misaligned with the answer mode the fixed selector expects. We term this loss the hidden interface tax and formalize a coverage-conversion decomposition that distinguishes raw oracle coverage from selectable coverage, the subset of problems where a correct candidate can actually be consumed by the selector. We propose Compatibility-Aware Candidate Construction (CACC), an interface layer between the candidate source and the fixed selector that repairs fragments, aligns answer modes, and removes selector-confusing noise without retraining either component. On numeric reasoning (GSM8K, competition_math), CACC raises both oracle coverage and final accuracy. On GPQA Diamond, CACC alone improves final accuracy from 5.6% to 19.2% (+13.6 pp); combined with proposer-side strengthening it reaches 25.8% (+20.2 pp). On MMLU-Pro, CACC exposes a coverage-conversion gap: answer-mode-compatible construction raises oracle coverage, but final accuracy decreases by 0.85 pp under the original selector; adding proposer-side strengthening improves final accuracy.

---


### 106. [BiLoCo: Binary Low-Rank Corrections for Post-Training Quantization](https://arxiv.org/abs/2610.32243)

**<font color=#1a73e8>作者：</font>** David Jin, Beshr IslamBouli, Tarushii Goel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) to FP4 has emerged as a key technique for reducing large language model inference cost, especially on Blackwell GPUs, which offer native FP4 tensor core support. Direct PTQ to FP4, however, still leaves a noticeable accuracy gap. Recent work on SVDQuant mitigates the errors introduced through FP4 quantization for diffusion models by adding high-precision low-rank corrections obtained via SVD. However, this high-precision low-rank correction requires many bits per rank, and it runs on the same tensor cores as the main FP4 GEMM. We introduce BiLoCo, a low-rank correction method whose left and right factors are stored as binary ${\{\pm 1\}}$ sign vectors rather than as BF16 numbers. The signed format uses $16{\times}$ less storage per rank-one component, and since the correction now consists of additions/subtractions, this can be run on CUDA cores concurrently with the FP4 tensor-core GEMM. On 4B--72B LLMs, BiLoCo matches or improves memory-matched SVDQuant for PTQ. We implement BiLoCo on B300 as a fused single kernel, where the FP4 GEMM runs on tensor cores, the bit-packed correction on the CUDA cores of the same launch, and the two are combined in the GEMM epilogue. With batch size $1$, the fused kernel is at most $11\%$ slower than the FP4-only GEMM for every rank up to $512$. At rank $128$, it is at most $20\%$ slower up to batch size $8$.

---


### 107. [Do Halting Heads Really Save Compute in Looped Language Models?](https://arxiv.org/abs/2610.32246)

**<font color=#1a73e8>作者：</font>** Tsung-Han Wu, Minsuk Heo, Kenny Tan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped language models run each token through the same layers several times, and each run is one iteration. To save compute, an extra layer, the halting head, gives after each iteration the probability that the token stops there, so that easy tokens can stop early. Pretraining models from scratch, up to 1.3B parameters, we find two problems. First, heads trained on a mix of all iterations predict that tokens need under half the iterations, yet under the standard stopping rule tokens run almost every iteration, because this training never scores the single iteration where a token stops. Scoring every iteration instead fixes this, but in our runs it works only with a strong penalty favoring early stops. Second, savings are commonly reported as an average number of iterations per token, but when sequences are generated in batches that run until their slowest token stops, a model without a head is almost as good at that cost. The reported average can therefore overstate the saving. We recommend reporting the iterations tokens actually run, with the stopping threshold and batch size, and give a test, run before training a head, that bounds its gain.

---


### 108. [MedCaseAgent: From Multimodal Clinical Evidence to Rare Disease Case Reports](https://arxiv.org/abs/2610.32258)

**<font color=#1a73e8>作者：</font>** Hongkang Chu, Yifan Shen, Tianjiao Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although Large Language Models (LLMs) have demonstrated potential in clinical documentation, generating the rigorous, evidence-based reasoning required for unprecedented, atypical, and rare disease case reports remains a significant challenge. We present MedCaseAgent, an end-to-end agentic reasoning paradigm that bridges this gap by synthesizing publication-quality reports from unstructured clinical notes. MedCaseAgent leverages a hierarchical structure, integrating patient-level data mining with iterative, tool-integrated reasoning. By dynamically querying medical literature and knowledge bases, the agent maintains high clinical fidelity and assesses case novelty. The framework is inherently modular, supporting various backbone LLMs in a plug-and-play fashion. To facilitate this research, we release MedCase-150K, a large-scale multimodal clinical case-report corpus, and MedCase-Bench, a robust temporally held-out evaluation suite. We also introduce an open-source model post-trained from Qwen3.5-9B and optimized specifically for this task. Under both LLM-judged and rule-based evaluation, MedCaseAgent outperforms existing general-purpose and specialized medical LLMs and agents. Blinded expert reviews and ablations further support the system's clinical relevance and evidence grounding.

---


### 109. [Beyond Pattern Matching in 3D MLLMs: Part-Level Functional Reasoning for Generalizable Recognition](https://arxiv.org/abs/2610.32262)

**<font color=#1a73e8>作者：</font>** Weihong Li, Hao Jiang, Yaohua Zha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D MLLMs recognize objects via pattern matching, which fails when geometrically similar objects require functional reasoning to disambiguate (e.g., dresser vs. wardrobe). Our per-sample Geometric Confusion Score (GCS) exposes this failure: baseline accuracy is 33.7% on ModelNet40's most ambiguous 20% versus 84.0% on its least ambiguous 20%. We identify a function-as-annotation pattern, in which functional language decorates a known identity instead of supporting inference, and hypothesize that reversing this information flow should concentrate improvements on the most ambiguous samples. PFIR (Part-level Functional Inference for Recognition) reverses that flow. Built on PartNeXt part segmentation, its data pipeline produces 507K QA pairs with functional CoTs (geometry $\to$ function $\to$ identity), and its progressive curriculum culminates in dual-objective GRPO: strict functional reasoning and descriptive grounding for Objaverse's diverse distribution. The two RL objectives yield nearly orthogonal task vectors ($\cos = 0.056$), enabling composition via Task Arithmetic. Under a strict dual OOD protocol (Objaverse $\to$ ModelNet40; XYZRGB $\to$ XYZ-only), PFIR raises zero-shot accuracy from 60.5% to 66.7%, with gains concentrated $2.6\times$ more on geometrically ambiguous samples---supporting part-level functional reasoning as an effective route to more generalizable 3D recognition. Code: this https URL.

---


### 110. [RVG-Bench: A Benchmark for Reasoning-Driven Audio-Visual Temporal Grounding](https://arxiv.org/abs/2610.32268)

**<font color=#1a73e8>作者：</font>** Yue Feng, Boshen Xu, Zihao Yue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing temporal video grounding (TVG) benchmarks primarily focus on localizing target video segments according to descriptive text queries of the visual content. However, real-world queries are more diverse and often require the model to first understand the user's intent before localization, such as finding visual evidence, identifying the cause of an event, or recalling a remembered moment, yet such queries remain largely overlooked. To mitigate this gap, we introduce RVG-Bench, a benchmark for reasoning-driven audio-visual temporal grounding, where every query is constructed such that the target segment can only be identified through reasoning about the query's underlying intent. We carefully construct the benchmark and rigorously verify its data quality to ensure models truly comprehend the audio-visual content. RVG-Bench comprises 1,255 videos and 1,890 query-interval pairs across eight reasoning types. We evaluate 22 models and find that the strongest, Qwen3.8-Omni-Flash, achieves only 49.6 mIoU. Through a series of controlled analyses, including oracle-grounding probes and test-time scaling experiments, we systematically examine where and why current models struggle, providing insights for future model development.

---


### 111. ["Not" is Not Lost in Translation: A Causal Analysis of Negation Representations in Multilingual LLMs](https://arxiv.org/abs/2610.32281)

**<font color=#1a73e8>作者：</font>** Giang Son Nguyen, Wray Buntine, Dung D. Le 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Negation occurs in every language, yet its surface realization differs drastically. Despite this, multilingual large language models (LLMs) translate negation robustly, raising the question of whether they share an underlying representation of negation across languages. We study this question in six open models across English, French, Vietnamese, and Chinese, using causal interventions on a synthetic contrastive dataset and a negation translation dataset derived from FLORES-200. Across models, we find strong evidence that negation representations are causally controllable and largely shared across languages. In particular, we show that a contrastive activation direction extracted from one language can induce or remove negation in the others, and directions extracted from different languages are substantially aligned. We further find that negation is represented in sparse features: a single sparse autoencoder (SAE) feature per model suffices to control polarity across languages, while responding selectively to negated inputs. Finally, both dense and sparse interventions generalize to four additional languages and FLORES-derived sentences. We release data and code to support future work: this https URL.

---


### 112. [Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution](https://arxiv.org/abs/2610.32285)

**<font color=#1a73e8>作者：</font>** Zhiyong Cao, Hengjie Zhu, Yongxin Wang 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly used to solve real-world problems, and their effectiveness depends on both the underlying models and the harnesses that support their operation. However, most existing benchmarks focus on model capabilities and overall agent performance, with limited attention to the evaluation of agent harnesses. To address this gap, we introduce TraceTrial-Bench, which organizes harness reliability into seven components covering context, execution, governance, lifecycle, observability, tools, and verification. We construct 95 expert-level, mechanism-oriented tasks with executable or state-based ground truth to support semantically equivalent comparisons while preserving the native behavior of each harness. We design a Trajectory Tracing (TT) module to capture agent execution traces and introduce a two-layer evaluation framework that separately assesses agent performance and harness reliability. In addition, we design a Multi-source Evidence Acquisition (MEA) module to provide evidence from the agent context, harness, and execution environment for LLM-based evaluation, and develop a Failure Attribution (FA) module that uses explicit mechanism chains to support attribution at the run level. Across 4 harnesses, 9 models, and 95 tasks, our evaluation of 3,420 runs yields macro-averaged harness scores ranging from 59.8% to 72.0%, while 31.1% of runs achieve task success despite failing at least one harness criterion. TraceTrial-Bench provides an auditable and reproducible foundation for comparing agent harnesses, diagnosing their failures, and studying how harness design interacts with model behavior.

---


### 113. [Lifelong Context Adaptation through Bidirectional Memory-Skill Learning](https://arxiv.org/abs/2610.32295)

**<font color=#1a73e8>作者：</font>** Tianyi Xu, Huazheng Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lifelong LLM agents must learn from an expanding history of interactions while making each decision within a bounded context window. Memory makes past experience available, but the agent may still need to infer how to solve each new task from the retrieved records. Skills provide reusable procedures, yet may omit the task-specific facts needed to apply them. Because retrieved memory and skills shape the agent's behavior, they also influence the experience available for future learning. We introduce MemCryst, a framework for lifelong context adaptation through bidirectional learning of memory and skills with a frozen language model. Recurring episodes stored in memory support skill creation and revision, and the interactions guided by those skills supply new memory for subsequent learning. Facts retrieved from memory and learned skills jointly form the agent's context, while task outcomes adjust the future retrieval influence of the records actually served without rewriting their content. Across ten settings spanning embodied control, long-document reading, conversation, mathematics, and code, MemCryst leads seven reported comparisons. On ALFWorld, joint serving achieves 63.17% success, compared with 59.83% for memory-only and 50.50% for skill-only serving. Code is available at this https URL

---


### 114. [DMAIC-Bench: From Self-Reflection to Self-Restraint for Agents in Multi-Stage Analytical Tasks](https://arxiv.org/abs/2610.32305)

**<font color=#1a73e8>作者：</font>** Shan Peng, Shuaiqi Cheng, Miao Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-stage analytical tasks require LLM agents to use intermediate evidence to decide whether to continue, redirect or stop. Self-reflection, in which an agent critiques its output, is widely studied, yet a critique does not show whether evidence changed the next action. We call that capability self-restraint. Existing agent benchmarks largely measure task completion or output quality and leave it untested. DMAIC-Bench evaluates it with 97 seeded tasks across 15 industrial cases in four sectors, built around Lean Six Sigma's explicit statistical prerequisites. Paired counterfactual variants require opposite actions at the same workflow position, distinguishing warranted restraint from indiscriminate stopping. We assess execution traces with a private scorer and final claims through independent expert review. Across 13 models from six providers, execution-level routing accuracy averages 92% on matched GO decisions and 19% on NO-GO decisions, counting any forbidden downstream computation as a route error. Execution traces show agents reporting correct diagnostics before performing analyses that those results disallow. Separately, blinded expert review of the 11 audited agents estimates that reports act on invalid evidence at 47% of reached NO-GO decisions, with an interval from 31% to 61%. Explicit stopping permission helps some models without consistently restoring correct decisions at both GO and NO-GO forks. Sixteen life-sciences tasks in bulk ribonucleic acid sequencing (RNA-seq) and case-control genome-wide association studies (GWAS) show that the same framework can evaluate evidence-dependent decisions beyond industrial workflows. Project code and data are available at: this https URL.

---


### 115. [Solvent: Long-Horizon Reasoning for Multi-Step Retrosynthesis](https://arxiv.org/abs/2610.32308)

**<font color=#1a73e8>作者：</font>** Yifei Wang, Botian Wang, YiFei Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-step retrosynthesis requires recursively transforming a target molecule through successive reaction steps into purchasable building blocks, and recent work has begun to draw on large language model (LLM) reasoning to tackle the task. In its latest evolution, LLM reasoning has entered the long-horizon regime: models pursue objectives across interdependent steps, interact with environments, and adapt to feedback. This shift has markedly advanced LLM capabilities, as illustrated by breakthroughs in AI-driven mathematical research. At this frontier, we introduce Solvent, an 8B LLM that successfully extends long-horizon reasoning to multi-step retrosynthesis. Through a two-round post-training curriculum, Solvent learns to interleave iterative synthesis planning, external availability verification, and adaptive route revision. Experiments show that, following a $2.1\times$ performance boost from RL, Solvent scores 61.86% across four benchmarks, surpassing mid-scale language models and prior search-based retrosynthesis systems, and rivaling frontier trillion-parameter LLMs.

---


### 116. [Many Perturbations, Shared Failure Dynamics: Tracing Direction-Sensitive Perturbation Influence in Language Models](https://arxiv.org/abs/2610.32309)

**<font color=#1a73e8>作者：</font>** Zhibo Hu, Chen Wang, Yanfeng Shu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Why can a task-preserving rewrite turn a correct answer into a failure while a larger internal change leaves the answer intact? We develop a direction-sensitive, readout-relative account of semantic fragility: heterogeneous language changes can share geometric and readout relationships without sharing an input-independent failure direction. Clean decision reserve, representation transformation, and response alignment provide complementary descriptions of this process. An exact longitudinal-transverse decomposition identifies directional information discarded by scalar transmission. A compact reserve-and-transmission model predicts failures across held-out families and items in Qwen3-32B and Gemma 4 31B, with useful but parameterization-dependent transfer to ReClor. Matched interventions show that orientation carries causal information beyond scalar geometry. Among naturally failed rewrites, attention-component tests on disjoint original items and subsequent answer-order controls favor the natural paired direction over tested random and same-answer-letter donor directions. Yet failures rarely persist across option orders, and current-order corrections use recomputed clean references. Shared predictive regularity thus coexists with context-dependent directional effects. Numerical path integration reduces, but does not eliminate, finite-patch approximation error within a fixed context; a larger discrepancy from the natural rewrite effect remains. A complementary fixed-CoT cue study extends this account to influence unacknowledged in recorded reasoning: readout associations transfer across domains, although the positive-mean causal criterion fails and signed-effect prediction remains post hoc. Together, these results support shared relations among reserve, transformation, and response while distinguishing local causal sensitivity from a complete explanation of natural failure.

---


### 117. [System One models Are Not Better Rerankers](https://arxiv.org/abs/2610.32318)

**<font color=#1a73e8>作者：</font>** Michael Dinzinger, Kanishka Ghosh Dastidar, Michael Granitzer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> System One models, or decision models, answer a question about an input with a calibrated probability instead of generated text. Within weeks of the first release, in September 2026, they were used as rerankers. We test whether the decision fine-tuning behind them makes a better reranker than plain reranker fine-tuning of the same model. For six Qwen backbones from 0.6B to 27B parameters and ten TREC DL and BEIR collections, we compare the untuned model, asked zero-shot, with its decision fine-tunes and its reranker fine-tunes, two of which we train ourselves. In our work, we draw the conclusion that decision fine-tuning never makes the better reranker. From 0.6B to 9B, reranker fine-tuning wins on every backbone by 5 to 29 points nDCG@10, also on zero-shot collections, and at 27B the two tie. Up to 9B, decision fine-tuning adds nothing over simply asking the untuned model. Moreover, we find that the calibration advantage of decision models depends on the question. Asked whether a passage answers the query, they are better calibrated than the published reranker fine-tunes from 4B on. Asked a slightly different question from prior work, they lose this advantage. Lastly, calibration does not make up for a worse ranking: up to 9B, a reranker fine-tune keeps the better passages at a fixed threshold. If you need a reranker, fine-tune a reranker.

---


### 118. [Beyond Gain: Measuring Skill Internalization for Agent Skill Retirement](https://arxiv.org/abs/2610.32322)

**<font color=#1a73e8>作者：</font>** Yanze Wang, Pengfei Yao, Tianyi Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents retrieve skills from public hubs that hold up to about 100,000 entries and serve many models. As models improve, a hub must find the skills a given model has internalized, meaning it can do without them, and retire them for that model, yet internalization has not been measured with known reliability. Published rules that compare runs with and without a skill retire on the gain alone. The gain is near zero both for an internalized skill and when neither the model nor the skill delivers the capability, a state we call uncovered. We instead withhold the skill, score the model on a task synthesized from it, and trust a high unaided score only when another model gains from the skill, since nearly half of high scores come from tasks no model benefits from. Under four models, a published gain rule applied with one task per skill removes over half of the uncovered skills. On SkillsBench, 28 of its 31 retirements rest on probes no run passed in full, while retiring on the unaided score costs no detectable reward. Unaided verdicts reproduce across tasks more often than the gain rule's (Cohen's kappa 0.42 against 0.23) but differ across models, so a hub must read them per model. We release 1,251 skills with tasks and item scores under four models.

---


### 119. [TGR-EvoDAG: A DAG-based Multi-Agent Code Evolution Framework for Generative Recommendation on Tencent](https://arxiv.org/abs/2610.32326)

**<font color=#1a73e8>作者：</font>** Junlin He, Junzhang Zhu, Yudong Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents have enabled automated code evolution for algorithm discovery. However, current recursive self-improvement (RSI) research for sequential recommendation faces a dilemma: general-purpose frameworks lack domain-specific feedback, while recommender-specific frameworks rely on linear evolution. Crucially, naively integrating them fails when applied to Generative Recommendation (GR). Unlike end-to-end models, GR relies on a module-cascaded pipeline (tokenization, pre-training, and alignment). In this paradigm, existing evolution methods suffer from: i) cost blindness, squandering budgets by ignoring stage-asymmetric retraining overheads; and ii) short-sighted evaluation, discarding promising upstream innovations that temporarily regress metrics before downstream adaptation. To bridge these gaps, we propose TGR-EvoDAG, a multi-agent code evolution framework tailored for GR. TGR-EvoDAG models code evolution as a Directed Acyclic Graph (DAG) to maintain multiple evolution branches and merge complementary innovations, unifying advanced search with rich GR diagnostic feedback. We further introduce stage-aware cost planning to optimize GPU-hour budgets, and active downstream co-adaptation to navigate temporary regressions and unlock cross-stage gains. On public Amazon datasets, TGR-EvoDAG enables the first autonomous evolution of a complete GR pipeline, improving offline metrics by up to 37.4% and Agent4Rec simulated user satisfaction by 19.7% over the strongest baseline. Furthermore, in industrial deployment on Tencent's large-scale commercial media platform, the evolved GR achieves a 12.16% relative improvement in offline Hit@1 and a statistically significant 0.40% increase in online click-through rate (CTR).

---


### 120. [4DMemory: Benchmarking Long-Horizon Spatiotemporal Memory with Harness-Augmented Agents](https://arxiv.org/abs/2610.32332)

**<font color=#1a73e8>作者：</font>** Yanhao Jia, Yi Zhu, Yiran Zhong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans efficiently process multimodal streams spanning hours to years, building persistent, fine-grained spatiotemporal memories that support reasoning about and predicting long-horizon events. In contrast, existing benchmarks focus on short- and medium-context tasks, and most foundation models struggle to preserve fine-grained information over long horizons. To evaluate and improve long-horizon spatiotemporal reasoning, we introduce the LongVideo dataset and the 4DMemoryBench. LongVideo comprises about 900 hours of video and over 5,000 manually reviewed questions covering visual, textual, and spatiotemporal reasoning across diverse context lengths. We further develop the 4DMemory Harness, which integrates four complementary skills, 22+ specialized tool models, and a model-specific retrieval-augmented generation system. Evaluating 13 leading models, we find that standalone foundation models struggle with long-horizon tasks, while the 4DMemory Harness improves all of them by over 50\%. Compared to previous benchmark, the same models exhibit a performance drop of more than 10\% on 4DMemoryBench. We hope 4DMemory will facilitate the development of spatiotemporal agents capable of addressing complex, long-horizon tasks.

---


### 121. [Beyond Final Outcomes: Quantifying Claim-Level Information Dynamics in Multi-Agent LLM Interaction](https://arxiv.org/abs/2610.32333)

**<font color=#1a73e8>作者：</font>** Haocheng Jiang, Herun Wan, Yongyuan Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When LLM-powered agents interact, information is repeatedly shared, expanded, and forgotten, yet multi-agent evaluation typically focuses on final task outcomes. We study such interaction as claim-level information dynamics and propose RIVER, which decomposes agent outputs into atomic claims and evaluates three complementary dimensions: convergence, exploration, and retention. Convergence captures cross-agent claim correspondence and stance alignment; exploration captures semantic breadth and extension beyond the source; and retention tracks source preservation and the persistence of new claims across stages and lineages. We evaluate five interaction strategies on 40 controlled news-generation cases. Repeatedly pooled interaction promotes convergence but narrows the information space, whereas distributed relay yields broader, less shared information. Further comparisons show that method-specific constraints increase exploration while weakening convergence and retention. Our findings suggest that collective information dynamics are better explained by underlying information-flow mechanisms than by simple downstream performance.

---


### 122. [Why Full-Duplex Speech Models Collapse in Long Conversations](https://arxiv.org/abs/2610.32349)

**<font color=#1a73e8>作者：</font>** Yeonju Kim, Bella Godiva, Se Jin Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex speech models listen and speak at the same time, which makes them promising for natural, open-ended conversation. But can they sustain a coherent conversation for tens of minutes? Because they generate a token every frame, even while listening, they exhaust their context windows within minutes. Yet existing benchmarks evaluate only single turns or a few conversational rounds, too short to expose the long-horizon problem. We introduce the Full-Duplex Long-Horizon Benchmark (FD-LHB), which tests five recent full-duplex models on long replayed conversations and in live conversation with an LLM partner. Every evaluated model eventually either degrades or exhausts its context. Models that keep the full history often degrade before their context runs out, while sliding-window models still fall into repetition, silence, and gibberish. For sliding-window models, we identify two contributing mechanisms. Gibberish and silence are linked to Initialization-Anchor Eviction, where the sliding window discards the first KV entry. Repetition is also reinforced by the model's own recent outputs. Guided by this diagnosis, we apply two simple fixes: Initialization-Anchor Pinning (IAP) keeps that first entry, and Duplex Repetition Penalty (DRP) discourages echoing while guarding against prolonged silence. Together, they support the diagnosis and, without retraining, substantially reduce conversational collapse in replays of up to an hour while running in real time.

---


### 123. [Search-Based Testing of Modality Sensitivity in Vision Language Models](https://arxiv.org/abs/2610.32360)

**<font color=#1a73e8>作者：</font>** Oliver Weißl, Eduardo Breitembach, Andrea Stocco  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) process images and text jointly, yet robustness evaluations often perturb these inputs separately or assess only predefined corruption levels. Such evaluations provide limited evidence of which modality is more susceptible to perturbations and whether smaller changes across both modalities can jointly expose failures. We present MoST, a black-box testing framework that characterizes modality sensitivity by comparing image-only, text-only, and joint perturbations. MoST uses multi-objective search to select and combine perturbations and adjust their severity, seeking prediction degradation while limiting changes to images and prompts. We evaluate MoST on four VLMs performing object localization on ImageNet and driving images. The models exhibit distinct sensitivities: textual perturbations dominate for some, whereas others are susceptible across both modalities. In several configurations, joint perturbations match or exceed the effectiveness of single-modality perturbations with smaller modifications to each input. In a human study, 60-76% of assessments across models judge the perturbed inputs sufficiently understandable to perform the task, and human localization is more accurate than that of the corresponding VLMs. These results show that evaluating modalities separately can overlook failure-inducing combinations and that modality sensitivity provides a more detailed account of VLM robustness than aggregate failure rates alone.

---


### 124. [Adaptive Control of Scientific Instruments with Nonstationary Responses through Multimodal Agents](https://arxiv.org/abs/2610.32370)

**<font color=#1a73e8>作者：</font>** Guoyang Shi, Hongwen Li, Yiding Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Controlling scientific instruments requires parameters to be adjusted progressively in response to feedback from successive operations. When unobserved operating conditions evolve with operational history, responses become nonstationary, and a static mapping from actions to responses becomes inadequate for decisions across shots. Shot-to-shot tuning of neutral beam injection (NBI) ion sources in magnetic confinement fusion devices is representative of this class of problems: the conditions of electrode surfaces and vacuum are difficult to observe directly, discharge outcomes vary between shots, and experiments are costly and carry operational risks. We propose a physically grounded multimodal agent with three independently auditable components. Deterministic algorithms extract symbolic physical quantities and visual evidence from multichannel waveforms; a memory with two layers organizes trajectories from the current task, experience from earlier tasks, and procedural knowledge, from which a multimodal large language model (MLLM) generates candidate actions; and an independent action feasibility check enforces action constraints before execution. In a strictly chronological replay of 455 shots from four EXL-50U platforms, physical symbols alone outperformed waveform images alone by 0.21-0.32 in macro-F1 for quality classification across all four evaluated models. Retrieved context increased the mean agreement with historical action directions by 22.4-42.7 percentage points, whereas the contribution of visual evidence varied across models. Under supervised operation on five ion sources, the system achieved a beam-extraction rate of 86.80% across 409 executed shots. These results demonstrate the engineering feasibility of the framework for supervised sequential tuning on a physical scientific instrument.

---


### 125. [DealsFlow: An Evidence-Gated Agentic Harness for Venture Capital Deal Triage](https://arxiv.org/abs/2610.32380)

**<font color=#1a73e8>作者：</font>** Ming Ze Tang, David Cutting, Boyd Carson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can read startup pitch decks, but letting them emit investment scores directly invites score inflation, run-to-run variance and rationales that are hard to audit. We describe DealsFlow, a human-in-the-loop agentic harness deployed at a UK early-stage fund. The LLM reads the deck, cites evidence and rates each category; code combines the ratings, caps them and only ever lowers them. Three mechanisms implement this: a stage-aware corroboration ceiling (78, 70 or 60 out of 100) on factual categories without external evidence; a sceptic call that may lower but never raise a score; and a pre-fetch pattern that retrieves and indexes all evidence before a single generation pass. We evaluate on $N=243$ SEIS/EIS investments with recorded outcomes. Because recent investments have unresolved outcomes, we use the 142 that are at least three years old. There, the full pipeline's score has Spearman $\rho=0.45$ (95% CI 0.32 to 0.57) with the total-value multiple and AUC 0.71 for identifying write-offs, against $\rho=0.38$ and AUC 0.68 for an unconstrained LLM. The gain is small and comes mostly from the sceptic call; we did not test whether its lower-only rule matters. Investments that later exceeded $2\times$ had 64% of factual categories corroborated, against 38% for write-offs (omnibus Kruskal-Wallis test over five outcome groups, $p=0.031$), and our retrieval was not date-restricted, so these figures may overstate screening skill. In a study of 20 inbound applications, analyst time per application fell from 44.7 to 18.9 minutes including verification and correction, and 84% of 240 cited claims were fully supported by their sources, but 70% of reports needed at least one correction.

---


### 126. [Acoustic and Lexical Signals for Native Language Identification of Language Learners](https://arxiv.org/abs/2610.32382)

**<font color=#1a73e8>作者：</font>** Ahmet Yavuz Uluslu, Mengjie Qian, Kate Knill 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spoken native language (L1) identification for second language learners has traditionally relied on acoustic attributes of speech. Comparatively little attention has been paid to analysing speech transcripts for L1 traces. In this paper, we present a study of L1 identification using both speech and corresponding transcripts from a spoken learner English corpus. We compare a WavLM-based audio L1 classifier with a zero-shot GPT-4o classifier operating on transcripts and analyse their predictions across proficiency levels using a CEFR-balanced evaluation set. Our experiments show that the audio classifier outperforms the transcript-based approach overall when full transcripts are available, although their relative strengths vary with learner proficiency. Audio performs better at A1, whereas text performs better from A2 to C1 with full transcripts. Transcript-based accuracy generally increases with proficiency, while acoustic performance remains comparatively stable. Restricting transcript length substantially reduces text-based accuracy, whereas audio is less sensitive to input length and performs relatively well with limited input. These findings provide insights into L1 identification from acoustic and textual representations of learner speech and how performance varies with proficiency and the amount of available language material.

---


### 127. [A Broader Look into MLLM's Retrieval Heads](https://arxiv.org/abs/2610.32411)

**<font color=#1a73e8>作者：</font>** Jia Wang, Yuqing Li, Jiangnan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Locating relevant evidence in long inputs is a core capability of Multimodal Large Language Models. Prior studies attribute this capability to retrieval heads, a sparse set of attention heads that transfer information from the context to the output. However, these analyses are confined to a limited set of modalities and the corresponding models. Moreover, how retrieval heads can be leveraged to enhance the model calls for further exploration. In this paper, we ask whether this mechanism expands together with the input modalities of the model. Taking audio-visual input as a newly added modality, we construct paired inputs in which the same answer is either spoken or shown on screen. With the evidence content fixed, retrieval heads remain sparse in the new modality and are shared to a large extent across modalities. Across 18 language, vision-language, and omni-modal checkpoints, omni-modal models largely preserve the retrieval heads of their backbones. Ablating these heads eliminates nearly all audio-visual retrieval. The heads shared across modalities make up fewer than 2\% of all heads, yet ablating them also degrades document understanding, spatial perception, and visual mathematics. Building on these findings, we turn retrieval heads into a target of optimization by training their attention with a ranking objective. This raises the page Recall@1 of Qwen3-VL-8B on MMDocIR by 6.03 points and improves document retrieval across three model families. Functional attention heads can thus serve both as a lens on multimodal models and as a target for improving them.

---


### 128. [LeafSkill: Efficient Leaf-Level Action Grounding for Recursive LLM Agents](https://arxiv.org/abs/2610.32412)

**<font color=#1a73e8>作者：</font>** Shen Liu, Ze Zhou, Zhenguo Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive large language model (LLM) agents solve long-horizon tasks through decomposition, execution, and environmental feedback. Yet after producing an atomic subtask, they often invoke the same large model again to translate a familiar instruction into an executable action. We observe that high-level planning is task-specific, whereas leaf-level action grounding recurs across tasks and can be checked against environment-admitted actions. We introduce LeafSkill, an external reuse layer that retrieves semantically related grounding experience, binds action templates to current objects and admissible actions, and uses a lightweight 1.7B selector to choose a bound action or defer the unchanged subtask to the original agent. Skills remain outside the model parameters, allowing a frozen selector to use post-training additions. Under lexical and syntactic paraphrases, exact matching retrieves none of the reference actions, while semantic retrieval preserves 96.0% and 97.0% candidate coverage; the frozen selector adopts 97.34% of unseen skill types. On an independent confirmation set of 200 Robotouille tasks, LeafSkill completes 137 tasks versus 121 for ReCAP (68.5% vs. 60.5%, exact McNemar p=.0259). On the 106 tasks completed by both, it reduces Qwen3.5-27B tokens by 14.42% and calls by 14.08%. A separate held-out repeat yields a consistent 9.0-point success gain and 18.98% token reduction. Reusable leaf grounding can thus improve task completion while reducing host-model inference without replacing high-level planning.

---


### 129. [Can LLM Annotators Match Human Consistency? Benchmarking Human Agreement and Optimizing Multi-Agent with Contrastive Knowledge](https://arxiv.org/abs/2610.32415)

**<font color=#1a73e8>作者：</font>** Xiaopeng Ke, Zhixin Wang, Xuebo Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based annotation has advanced rapidly, yet existing benchmarks remain misaligned with real-world practice. Actual annotation often involves lengthy, task-specific guidelines, and different annotators may produce divergent but reasonable judgments, especially on boundary cases, where single-labeled dataset fail to reflect this disagreement. This gap also limits existing single-agent and workflow-based annotation systems, which often lack adaptability to complex, evolving guidelines. To bridge this gap, we introduce ANT-A Benchmark, a real-world multi-annotator benchmark spanning 7 datasets across domains and modalities, with task-specific guidelines and 5 independent human labels per instance. ANT-A enables a distribution-aware evaluation, using Fleiss kappa to assess how closely model annotations align with human labeling distributions. We further propose ANT-OR, a multi-agent annotation framework that refines prompts by distilling contrastive decision rules from positive and negative feedback. Experiments show that ANT-OR improves agreement@>=2 accuracy by 4.5 points over the strongest baseline and achieves the highest alignment with human annotator distributions as measured by Fleiss kappa within 2 points. Code and benchmark are available at this https URL.

---


### 130. [Cycle-of-Thought: Self-Evaluative Iterative Reasoning for Table Visual Question Answering in Document Images](https://arxiv.org/abs/2610.32423)

**<font color=#1a73e8>作者：</font>** Somraj Gautam, Gaurav Harit  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Vision-Language Models (VLMs) have significantly improved Visual Question Answering (VQA) performance, yet their reasoning over structured content such as tables remains inconsistent, often plagued by spatial misalignment and logical hallucinations. Existing approaches for improving table VQA typically rely on architectural modifications or expensive supervised fine-tuning (SFT), which impose high barriers to entry due to the need for large-scale, expert-annotated datasets and significant computational resources. In this work, we propose Self-RefineVQA, a training-free, inference-time self-correction framework that improves table VQA performance without additional labeled data or model updates. Inspired by human revision behavior, our method enables a single VLM to iteratively act as a generator, critic, and refiner, forming a closed self-feedback loop that corrects common reasoning errors through prompt-guided re-evaluation. Experiments on tabular VQA benchmarks demonstrate that Self-RefineVQA yields consistent accuracy gains in monolingual and cross-lingual understanding, with a particularly significant boost for small models, enabling lightweight models (e.g., 2B-7B parameters) to rival the performance of significantly larger counterparts. Furthermore, we provide a comparative complexity analysis demonstrating that while inference cost increases linearly, our framework offers superior data efficiency and a lower cumulative cost by eliminating the prohibitive annotation bottleneck of human labeling required for fine-tuning. Our results highlight the potential of prompt-based self-improvement as a scalable, accessible paradigm for reliable table reasoning in VLMs.

---


### 131. [Async-RBench: Benchmarking Asynchronous Task Execution in LLM Agents](https://arxiv.org/abs/2610.32429)

**<font color=#1a73e8>作者：</font>** Detao Zeng, Guilin Ou, Nuo Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly execute tasks asynchronously: a main agent continues working while its subagents run, and the task state may change before their results arrive. The main agent must decide which work to update or preserve and which checks to repeat, while avoiding prohibited changes. Final task success alone does not reveal whether these results were handled correctly, and natural asynchronous arrivals are hard to reproduce. We introduce Async-RBench, a benchmark for asynchronous task execution in LLM agents, with 200 executable tasks covering eight scenarios. A scenario controller regulates result delivery using predefined task-state conditions, while an Event Response Contract (ERC) specifies what each response must change, preserve, avoid, and re-verify. The Dynamic Replanning Score (DRS) weights the response process and outcome equally and is reported separately from task success. We evaluate nine agents and find DRS scores of 19.2 to 45.1, with the lowest scores on duplicate reports and subagent failures. Under our execution protocol, all nine agents obtain lower task success with asynchronous than with batched delivery (26.0% vs. 29.7% on average). For three agents, prompting the main agent to rebuild its plan after every result improves DRS by only 2.6 to 3.5 points. Together, these findings highlight the challenges of reliable asynchronous task execution and the need to evaluate how agents handle incoming results alongside end-to-end task success.

---


### 132. [When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning](https://arxiv.org/abs/2610.32431)

**<font color=#1a73e8>作者：</font>** Zongyao Zhao, Cheng-Jie Zhao, Ruihang Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A failed vision-language-action (VLA) rollout does not imply that every action contributed to failure. Yet in group-relative policy optimization (GRPO), a single trajectory-level advantage is assigned to all actions in a rollout. Potentially useful recovery attempts can thus be penalized alongside the errors they aim to correct. Ideal stopping conditions for failure feedback are characterized using success-probability and policy-score martingales. At these stops, the removed gradient contribution has zero conditional expectation given the retained information. Truncation therefore preserves the expectation of a reference GRPO group-gradient estimator and can reduce its covariance. One such stop occurs when the conditional probability of success is zero, motivating error and recovery cues for selecting candidate feedback boundaries. Martingale GRPO (MART-GRPO) is introduced with a vision-language model (VLM) for event-guided truncation. The VLM is fine-tuned on our annotated training set using low-rank adaptation (LoRA). The last visible error without observed recovery is localized by the frozen VLM in complete rollout videos. Failure feedback is retained through the selected error interval and removed afterward, while successful-rollout loss terms and original loss normalization are preserved. For retrospective boundaries, changes in expectation and variance are analyzed to assess departures from ideal stopping. Experiments with OpenVLA-OFT on RoboTwin 2.0 show that MART-GRPO improves success rates over full-trajectory GRPO across multiple tasks.

---


### 133. [Profile-Driven User Simulation via Reinforcement Learning with Hierarchical Rewards for Task-Oriented Dialogues](https://arxiv.org/abs/2610.32435)

**<font color=#1a73e8>作者：</font>** Juan Li, Fangshu Chang, Xinyi Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Building Task-Oriented Dialogue (TOD) systems for high-value scenarios such as financial marketing requires large volumes of domain-specific dialogue data, which privacy regulations, annotation costs, and the need for expert labor make hard to obtain. User simulation offers a remedy, but existing methods target general-domain dialogue and exhibit two key limitations: insufficient modeling of domain-specific business processes and compliance constraints, and inadequate capture of the colloquial, spoken-language character of voice interactions. We propose ProfileSim, a profile-driven user simulation framework for financial marketing outbound calls. It jointly models user profiles---demographics and Big Five personality traits---and business profiles---intents reverse-engineered from real call logs---enabling fine-grained control over simulated behavior. The base model is fine-tuned on real voice dialogue data and refined by Group Relative Policy Optimization (GRPO) with hierarchical rewards at the dialogue and utterance levels. Paired with a customer service agent integrating Standard Operating Procedure (SOP) constraints and Retrieval-Augmented Generation (RAG), ProfileSim achieves the highest colloquial naturalness, the strongest user profile adherence and the lowest agent score on long-tail intents among all evaluated user generators, while producing substantially shorter user utterances at comparable business compliance. The generated dialogue data is designed to support intent recognition training, agent evaluation, and rapid cold-start deployment.

---


### 134. [PROVE: Probabilistic Visual Grounding via Patch-Level Evidence for Vision-Language Models](https://arxiv.org/abs/2610.32440)

**<font color=#1a73e8>作者：</font>** Mayank Nautiyal, Tianru Zhang, Li Ju 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual grounding with vision-language models such as CLIP typically produces a single deterministic relevance map for an image-query pair, without indicating whether the localisation is reliable or whether the referent is present at all. We introduce \textbf{PROVE} (\textbf{Pro}babilistic \textbf{V}isual Grounding via Patch-Level \textbf{E}vidence), a post-hoc evidential adapter that maps frozen CLIP patch features to per-patch Beta distributions without modifying the backbone. PROVE casts grounding as per-patch membership: each patch accumulates positive and negative evidence for whether it belongs to the referent, so a query may match zero, one, or many patches. We train PROVE with an evidential objective on soft patch-coverage targets, and define a prior-pull objective that keeps absent-referent examples near an uninformative prior, so that vacuity serves as an absence signal without a dedicated presence classifier. During inference, a single forward pass yields, in closed form, a posterior-mean grounding map, a spatial vacuity map, and an image-level absence score. We evaluate PROVE on referring-expression benchmarks: it is competitive in localisation with state-of-the-art CLIP grounding methods, its uncertainty tracks localisation error and supports selective prediction under abstention, and its image-level score detects when the referent is absent altogether. Our evidential patch-membership modelling offers a simple, drop-in mechanism for probabilistic verification in frozen vision-language grounding systems.

---


### 135. [SCI-AGENT-EXAM: Benchmarking Agents on Scientific Research Tasks](https://arxiv.org/abs/2610.32441)

**<font color=#1a73e8>作者：</font>** Tianyun Zhong, Wei Wang, Jialin Li 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly capable of supporting scientific workflows, but their capabilities across diverse research activities remain difficult to assess systematically. Existing benchmarks often focus on selected scientific capabilities or task types, limiting a comprehensive characterization of scientific agents' strengths and weaknesses in realistic research workflows. We introduce SCI-AGENT-EXAM, a workflow-oriented benchmark comprising 120 expert-curated tasks across 11 scientific fields and 7 research task types defined by the Scientific Workflow Task Taxonomy (SWTT). Each task requires both executable artifacts (e.g., code and scripts) and textual artifacts (e.g., reports and explanations). To evaluate the heterogeneous task outputs, we develop a hybrid evaluation protocol combining deterministic programmatic verification for executable artifacts with a calibrated, expert-validated LLM-based judge for textual artifacts. Beyond outcome assessment, we analyze progress and solution stability along execution trajectories to characterize how agents reach their final results. Experiments with 10 frontier LLM agents reveal substantial performance gaps: GPT-6 Astra achieves the highest overall score of 80.9, yet only 26.0% of its runs exceed the 0.95 success threshold. Further analyses uncover distinct capability profiles across scientific task types and substantial variation in execution efficiency and stability. Our code and data are available at this https URL.

---


### 136. [Decoupling Patient Personas and Clinical Workflows: A Dual-Agent Approach to Realistic Medical Dialogue Generation](https://arxiv.org/abs/2610.32443)

**<font color=#1a73e8>作者：</font>** Qiyuan Li, Xiaomei Guo, Chao Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pre-consultation medical dialogues are essential for collecting comprehensive patient information, but are costly to obtain at scale due to privacy and ethical constraints. Existing LLM-based synthesis methods often rely on prompt engineering or rigid rules, limiting their ability to balance clinical relevance with realistic patient diversity. We propose CoRPS-Dial, a controllable dual-agent framework for pre-consultation medical dialogue synthesis that integrates patient personas with guideline-aligned clinical workflow rules. CoRPS-Dial generates dialogues through interactions between a persona-driven patient agent and a process-guided doctor agent, followed by post-hoc quality control for role consistency, workflow completeness, and textual consistency. Experiments on coronary heart disease demonstrate that CoRPS-Dial improves alignment between synthetic and real dialogues in information coverage, clinical compliance, and dialogue naturalness. Downstream fine-tuning experiments further confirm the utility of the generated synthetic data for medical dialogue tasks. These results highlight the effectiveness of CoRPS-Dial for clinically grounded and controllable medical dialogue synthesis.

---


### 137. [POSEIDON: Scaling Training Environments for Scientific Agents from Code Repositories](https://arxiv.org/abs/2610.32448)

**<font color=#1a73e8>作者：</font>** Qifan Zhang, Yuhan Li, Nuo Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training environments remain a major bottleneck for agents in data-driven scientific discovery. Existing collections of executable and verifiable training environments are small, and their construction remains difficult to scale. To address this limitation, we introduce Poseidon, an automated pipeline for generating diverse, verifiable training environments from scientific code repositories at scale. From the same repository budget, Poseidon extracts nearly 10 times as many training environments as a prior approach by decomposing scientific workflows into four complementary task types: Reproduction, Subflow, Completion, and Correction, where each type targets a distinct capability for scientific research. A recursive improvement loop further refines failed candidates and recovers otherwise discarded environments. Using Poseidon, we construct Pearl, a collection of 97,659 executable and verifiable environments from 7,110 public repositories spanning 10 scientific disciplines. To the best of our knowledge, Pearl is the largest and most broadly multidisciplinary collection of scientific-agent training environments to date. Qwen3.5 models (9B, 27B, and 35B-A3B) trained on Pearl achieve consistent gains across six challenging scientific-agent benchmarks. Overall, the scale and diversity of Pearl offer opportunities for training scientific discovery agents.

---


### 138. [Reading Between the Layers: Cross-Modal Alignment and Representational Hierarchy in Vision Transformers](https://arxiv.org/abs/2610.32463)

**<font color=#1a73e8>作者：</font>** Sugam Karki, Raúl Vázquez, Yova Kementchedjhieva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large vision-language models excel at optical character recognition, it remains unclear how their underlying vision encoders process text and its meaning, and whether they support anything resembling reading comprehension. We systematically study transformer-based vision encoders, using cross-modal alignment between rendered text and visual concepts together with probing and retrieval-based analyses as a controlled window into these broader capabilities. Our layer-wise analyses span orthographic, grammatical, and semantic organization, and reveal that strong cross-modal mapping emerges only in the deepest layers, after unimodal object and text recognition have already developed, coinciding with a progression from surface-level to semantic representations. Although this hierarchy is strongest in contrastively trained models, larger self-supervised models and text-rich training data partially support similar behaviors without explicit language supervision. Together, our results suggest that increasing model and training-data scale, as well as text-rich training data, can partially compensate for the absence of language supervision.

---


### 139. [Sharpness-aware Orthogonalized Momentum Algorithms](https://arxiv.org/abs/2610.32465)

**<font color=#1a73e8>作者：</font>** Geetika, Shivani Singh Chauhan, Gauranshi Gupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial sharpness penalty per iteration of a base optimizer, known as sharpness-aware minimization (SAM), is an accepted technique to improve generalization in deep learning. Recently, Muon has emerged as a dominant optimization algorithm for training large language models (LLMs). It achieves lower sample complexity for heavy-tailed gradient updates - a phenomenon common in LLM training. However, sharpness penalties with Muon updates are yet largely unexplored in the literature. Moreover, the behavior of SAM under heavy-tailed noise is unknown both theoretically and empirically. A potential reason for this gap is the additional cost of extra gradient computation per iteration for penalty perturbations in SAM, which becomes prohibitive for LLMs. This paper introduces Sharpness-aware Orthogonalized Momentum Algorithm (SOMA) to combine a computationally efficient and theoretically grounded perturbation scheme with the Muon algorithm. The key idea is to use stale (purely) stochastic gradient noise for adversarial perturbations. Theoretically, we show that SOMA's sample complexity is invariant to the perturbation direction. We provide explorations and insights into SOMA's robustness to heavy-tailed gradient noise. We extensively explore SOMA's efficacy in (a) mitigating quality degradation due to post-training quantization, and (b) catastrophic forgetting during fine-tuning of LLMs.

---


### 140. [ALLMTS: Automated LLM-based Medical Triage System](https://arxiv.org/abs/2610.32469)

**<font color=#1a73e8>作者：</font>** Michał Remigiusz Janiszewski, Artur Stopa, Łukasz Lenkiewicz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Telephone triage is a safety critical task: from a brief intake note, a nurse must decide whether a caller needs an ambulance, an emergency department, an appointment, or self care at home. Queried directly, large language models (LLMs) are unreliable: they over-escalate routine cases and cannot justify their recommendations against an auditable clinical standard. We present the Automated LLM-based Medical Triage System (ALLMTS), which grounds every disposition in the same commercially maintained telehealth guidelines nurses use. Rather than asking an LLM to triage, ALLMTS makes it execute the guideline: it selects the appropriate guideline and evaluates its triage assessment questions. The disposition follows deterministically from the first positive answer, using the same traversal rule a nurse follows. We evaluate ALLMTS on 566 synthetic, expert-validated scenarios spanning 14 dispositions and designed to test specific guideline questions. ALLMTS achieves 0.95 accuracy, compared with 0.47 for a raw-LLM baseline. On a curated 50-scenario subset released as an open benchmark, ALLMTS reaches 0.98 accuracy, on par with the 0.944 correct disposition rate that a five nurse expert panel recorded on those same scenarios. Critically, on that subset the baselines have over-triage rates of up to 0.50 (0.44 on the full dataset), whereas ALLMTS reduces the over-triage rate to at most 0.02 while maintaining low under-triage. These results support coupling LLM language understanding with executable clinical guidelines for triage from intake notes.

---


### 141. [Beyond Post-Hoc Rewards: Privileged Reasoning Exploration for Multimodal Embeddings](https://arxiv.org/abs/2610.32474)

**<font color=#1a73e8>作者：</font>** Tianyu Yang, Yijun Tian, Lars Benedikt Kaesberg 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advances in Multimodal Large Language Models (MLLMs) have driven substantial progress in multimodal embeddings. Recent methods exploit generative capabilities by augmenting embedded inputs with self-generated reasoning to produce more informative embeddings. However, conventional retrieval supervision for training embedding models specifies pairwise relevance relations without explicitly guiding the reasoning used for input augmentation. Such reasoning is neither directly observed nor uniquely determined by the input, allowing multiple plausible traces to introduce semantic cues of varying retrieval utility. Existing approaches largely optimize reasoning conditioned on the input alone, limiting the exploration of retrieval-relevant traces. We introduce PILOT, a framework that models reasoning as a latent variable and instantiates its prior and posterior distributions as distinct reasoning modes of a shared MLLM. The prior conditions only on the input, whereas the posterior uses additional training-time relational evidence to guide reasoning exploration. To translate the posterior's broader exploration into inference-time improvements, we derive an importance-weighted variational objective and instantiate it as a prior-posterior co-evolution framework that improves both modes under a shared inference-compatible reward while selectively transferring posterior trajectories to the prior according to their utility and prior reachability. On the 78-task MMEB-V2 benchmark, PILOT outperforms the primary baseline across all 12 task groups at both 2B and 7B parameters, improving overall scores by 3.2 and 3.3 points, respectively, with the largest gains in visual-document retrieval (+6.1 and +6.4 points). Our results show that relational supervision is most valuable not as a post-hoc reward but as a signal for shaping how reasoning is explored in training reasoning-enhanced embedding models.

---


### 142. [CauProphet: Teaching Agents to Develop Causal Cognition like Humans](https://arxiv.org/abs/2610.32477)

**<font color=#1a73e8>作者：</font>** Kaiwen Wu, Chaochao Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly support long-horizon tasks by leveraging external memory and past experience. However, existing agents mainly retrieve records or summaries, lacking the ability to form and refine causal understanding of the world. Inspired by human causal cognition, we introduce CauProphet, an agent that develops and updates causal knowledge within its Causal Cognition. For each task, CauProphet combines relevant knowledge in Causal Cognition with current evidence to construct a Causal Belief, a structured belief capturing causal factors and the effects of possible actions. It uses this belief for decision-making and continuously updates both the belief and Causal Cognition as new observations emerge, enabling causal knowledge that persists beyond individual experiences. Evaluations demonstrate that CauProphet progressively acquires causal knowledge and transfers it to future decision-making. In financial research, CauProphet leverages prior discoveries to improve downstream analyses and outperforms all baselines in mean rank correlation with next-day returns, achieving a 25.4% improvement over a baseline agent. It also improves prediction accuracy from 21.3% to 28.6% in dynamic real-world settings. Further experiments validate its ability to perform reliable causal analysis and action selection across scientific and everyday tasks, demonstrating the potential of causal experience learning for next-generation LLM agents.

---


### 143. [PathJev: Decision-Native Vision-Language Modelling for Histopathology](https://arxiv.org/abs/2610.32478)

**<font color=#1a73e8>作者：</font>** Cristian Tommasino, Antonio M. Rinaldi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models used for decisions in histopathology rarely return calibrated probabilities over the candidates a user cares about. Decision-native models write a question and a candidate set chosen at run time into the input and return a normalised distribution from a small decision head in one forward pass. We build PathJev-P, a decision-native model for histopathology: MedGemma-1.5-4B with LoRA adapters and a decision head, trained on 40,000 patch states from three public collections whose expert labels are turned into typed questions with organ-specific candidate sets and a "none of these" option. In a comparison over 3 seeds with an analysis plan fixed before testing, on test sets without documented overlap with the training data of the backbone, PathJev-P is more accurate than a generative model trained with the same backbone, data and selection rule, the zero-shot pathology model CONCH and a general medical decision model (balanced accuracy 0.541 against 0.492, 0.345 and 0.213); its advantage over the generative model comes from two organs absent from training. The calibration advantage depends on how the generative model's probabilities are read out. With the summed candidate log-likelihood used in previous work, PathJev-P has the lower calibration error (ECE 0.204 against 0.279); with a length-normalised read-out of the same generative model, examined post hoc, the two have similar mean calibration error (0.201) and the generative model is better calibrated on the unseen organs, where PathJev-P remains over-confident. A supervised linear probe on a pathology foundation model is better calibrated in every setting. In a qualitative whole-slide demonstration, PathJev-P labels unsupervised tissue clusters with abstention and separates carcinoma from other tissue while running the model on a fraction of the tiles.

---


### 144. [CASE: Confusion-Aware Skill Evolution for Frozen Multimodal Emotion Models](https://arxiv.org/abs/2610.32481)

**<font color=#1a73e8>作者：</font>** Siyu Wu, Zeyu Liang, Linghao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have substantially advanced Multimodal Emotion Recognition (MER) by enabling fine-grained emotion understanding through reasoning over multimodal evidence. However, they still exhibit systematic confusion between semantically adjacent emotions with highly overlapping multimodal cues. Existing approaches typically address these errors through global parameter adaptation, making confusion correction costly and inflexible. We instead observe that emotion confusion is highly localized and therefore better addressed through reusable pair-specific expertise. Building on this insight, we propose Confusion-Aware Skill Evolution (CASE), the first agent-skill framework for MER. CASE maintains a sparse, self-evolving library of pair-specific EmotionSkills that externalize affective expertise from model parameters, enabling the learned expertise to be continuously refined and readily transferred across diverse frozen MLLM backbones. During inference, CASE dynamically retrieves the appropriate EmotionSkill to reinforce boundary-aware reasoning while keeping the MLLM backbone frozen. Extensive experiments on CA-MER, DFEW, and EMER demonstrate the effectiveness and transferability of CASE across both general-purpose and emotion-specialized MLLMs. Notably, CASE improves the average accuracy of Qwen3-VL-8B on the CA-MER benchmark from 46.80% to 59.13%, while achieving consistent gains across MLLMs.

---


### 145. [When Agents Fail: Model or Harness--Who's to Blame?](https://arxiv.org/abs/2610.32483)

**<font color=#1a73e8>作者：</font>** Shao Zhang, Hangfan Zhang, Yuanyuan Shi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents combine models with execution harnesses, so agentic benchmark performance reflects their joint behavior. We argue that harnesses should therefore be evaluated through their interactions with underlying models. We develop a framework combining five complementary measures: (i) Valid Completion Rate (VCR), how reliably agents finish normally and deliver evaluable results, irrespective of task correctness; (ii) Model-Harness Fit, how well a harness supports task achievement through valid completion for a given model; (iii) Cross-Model Fit, a harness's overall suitability across evaluated models; (iv) Interaction Residuals, pairing-specific execution strengths and weaknesses hidden by component-level summaries; and (v) Token Load, the token demands of agent execution, including failed attempts. We evaluate four general-purpose harnesses (OpenCode, Codex CLI, Pi CLI, and DeepAgents) with four core models, plus two fixed native model-harness systems, on six benchmarks covering context management, tool use, long-context planning, multimodal interaction, and artifact handoff. Including native references and stress conditions, 111 evaluation settings yield 52,168 trajectories. Harness rankings vary across models and benchmarks; task performance and valid completion can favor different pairings, and similar task scores can accompany distinct execution profiles. OpenCode ranks first in cross-model performance, while DeepSeek V4 Flash Preview maintains consistently high Mean VCR across harnesses on the shared four-benchmark panel. These findings support evaluating model-harness interactions, training transferable harness-use capabilities in models, and harness designs adapted to the model and task.

---


### 146. [PCFBench: How Far Can Large Vision-Language Models Go in Physics-aware Photonic Inverse Design?](https://arxiv.org/abs/2610.32485)

**<font color=#1a73e8>作者：</font>** Shengchao Chen, Ting Shu, Sufen Ren  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photonic crystal fibers (PCFs) underpin critical applications in telecommunications, sensing, and high-power laser delivery, yet their design remains a manual, expert-intensive process that couples geometric intuition with deep waveguide physics. Vision-language models (VLMs) offer a promising path toward automating PCF design, but can they truly reason about photonic physics from microscopy images, or do they merely recognize visual patterns? We introduce PCFBench, the first comprehensive benchmark for evaluating VLMs on the perception, reasoning, and decision steps of the photonic inverse-design loop. PCFBench spans 26 tasks organized into six categories of increasing cognitive demand (Geometry Perception, Physics Understanding, Text Generation, Multi-modal Reasoning, Inverse-Design Decision, and Code Generation), built from over 220K FDTD simulation samples across 18 structurally diverse fiber families. We evaluate both individual VLMs on isolated tasks and multi-agent systems (MAS) on the full sequential pipeline from perception to design. Our results reveal a striking perception-design gap: current models can identify fiber geometry with moderate success, yet consistently fail to translate that visual understanding into physics-aware design actions. Moreover, cascading agents through the pipeline exposes significant error propagation, where upstream perception mistakes compound into downstream design failures. These findings suggest that neither model scaling nor naive agent chaining suffices, and that closing the loop demands explicit physical grounding. PCFBench provides the community with a rigorous, multi-dimensional testbed to measure progress toward AI-assisted photonic engineering. The project is available at this https URL.

---


### 147. [Efficient Zero-Shot Video Anomaly Detection via Signal-Aware Adaptive Fusion (SAAF)](https://arxiv.org/abs/2610.32486)

**<font color=#1a73e8>作者：</font>** Khaled Waleed Dawoud, Muhammad Haris Khan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying Vision-Language Models for video anomaly detection confronts a fundamental constraint. Their semantic reasoning demands computational budgets incompatible with the scale of real-world video streams. We present Signal-Aware Adaptive Fusion (SAAF), a framework that achieves efficient zero-shot anomaly detection through three key innovations. First, we introduce a dual-signal adaptive sampler operating in semantic embedding space: a delta signal captures sudden events via frame-to-frame cosine distance, while a drift signal detects static and gradual anomalies through deviation from rolling temporal context. Their OR-gated combination with adaptive EMA-based thresholding provides comprehensive anomaly coverage without training data. Second, we propose a threshold-gated cascaded architecture where lightweight frame-level scoring precedes expensive video-level temporal analysis, invoking it only when confidence warrants additional context. Third, we design a signal-aware weighted fusion mechanism that dynamically adapts score combination based on which signal triggered frame selection. Across four benchmarks, SAAF delivers competitive accuracy at substantially lower cost. Among training-free zero-shot methods, SAAF sets a new state of the art on XD-Violence (92.07%), MSAD (86.70%), and ShanghaiTech (80.54%) AUC-ROC, with XD-Violence and MSAD also surpassing supervised baselines. SAAF sustains 44.95, 48.61, and 41.06 FPS on XD-Violence, UCF-Crime, and MSAD, a 2.43$\times$, 2.63$\times$, and 2.22$\times$ throughput improvement over the prior best zero-shot method. Code: this https URL

---


### 148. [Accordion: Elastic-Depth Inference via Fixed-Prefix Layer Looping](https://arxiv.org/abs/2610.32492)

**<font color=#1a73e8>作者：</font>** Yudong Zhang, Wei Ding, Kaili Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models serve applications with diverse inference budgets, but training and maintaining separate models for each budget incurs substantial costs. Recent Looped Transformers enable flexible inference computation through parameter reuse, but maintaining strong performance across different inference budgets remains an open challenge. We introduce Accordion, a mixture-of-experts-based model that supports five inference budgets through fixed-prefix layer looping. Each budget follows a pre-defined execution path, while the minimum budget retains the unlooped model. Joint pretraining samples one budget per micro-batch and optimizes its next-token prediction loss without additional cross-budget consistency objectives. We further preserve these inference budgets through supervised fine-tuning and reinforcement learning, where parameter-group merging and budget-matched multi-teacher on-policy distillation integrate three domain experts into one model. After 3.6T tokens of pretraining, increasing inference depth improves Accordion-6B-A0.5B's five-category macro-average across 37 tasks by 3.01 percentage points, with the middle budget capturing 89% of this gain using half as many additional layer executions. The final model surpasses each domain expert on its corresponding task-and-budget average, while achieving strong instruction-following performance across all budgets and retaining depth-dependent gains in mathematical reasoning and code generation.

---


### 149. [Fast and Useful: Adapting Distilled Generators for Visual Learning](https://arxiv.org/abs/2610.32512)

**<font color=#1a73e8>作者：</font>** Patryk Bartkowiak, Dominik Michels, Sören Pirk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distilled text-to-image models generate images quickly, but classifiers trained on those images can perform substantially worse than classifiers trained on images from their slower base models. We adapt released distilled generators to produce better training data while retaining fast generation. We fit a low-rank update to the student's first prediction so that it reaches an intermediate state produced by its unguided base, then disable the update and let the unchanged student finish generation. The base supplies training targets and is absent at inference. Guided targets and shorter jumps give classifiers lower accuracy in our ablations, showing why the state used for supervision matters. Across three generator families, the adapted images train better classifiers than images from the released students. With class-name templates at full ImageNet-1k scale, ResNet-50 top-1 rises from 8.4% to 34.2% for FLUX.2-klein and from 12.7% to 32.1% for SD-Turbo, using two and three denoiser evaluations per image, respectively. Fixed adapters also improve results on additional classes, fine-grained datasets, and other learner architectures and training recipes. Template-based adaptation remains useful against richer-prompt alternatives, while the benefit of combining adaptation with LLM generation prompts depends on the generator. Adapting a single generation step makes fast generators substantially more useful for training visual models.

---


### 150. [Principled Nonlinear Concept Erasure and Steering](https://arxiv.org/abs/2610.32516)

**<font color=#1a73e8>作者：</font>** Idan Simai, Shauli Ravfogel, Uri Shaham  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned representations often encode sensitive attributes, such as gender or race, that may be undesirable or unsafe to retain. Concept erasure aims to remove this information while preserving task-relevant content. Existing methods remain incomplete: linear methods provide guarantees only against linear probes, while nonlinear methods achieve stronger empirical erasure but lack formal guarantees and often sacrifice utility. In this work, we introduce a principled conditional autoencoder framework for nonlinear concept erasure. We follow the principle that erasure should remove only the sensitive attribute and nothing else, and we show that, under the stated assumptions, perfect reconstruction together with population-level independence is sufficient for perfect nonlinear guardedness, with preservation guarantees in the imperfect-reconstruction regime. Empirically, we attain a superior utility-erasure trade-off across multiple datasets, sensitive attributes, and language models, surpassing even the supervised variants of competing methods despite using no target-task labels, while being simpler to optimize and converging substantially faster. Beyond erasure, our framework yields concept conversion (representation steering) as a by-product: by changing only the target concept at inference time, it produces representations corresponding to different concept values - at no additional training cost - a capability no prior erasure method provides, and on which we likewise demonstrate strong empirical performance.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-204](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
