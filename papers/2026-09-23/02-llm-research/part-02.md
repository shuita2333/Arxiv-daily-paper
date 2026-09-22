# 🧠 大模型相关研究 | 2026年09月23日

> 本类共 **379** 篇论文：已确认 **359** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-379](./part-08.md)

---

### 51. [Replicating the Geometry of Emotion Representations in a Base Open-Weights Model](https://arxiv.org/abs/2609.22208)

**<font color=#1a73e8>作者：</font>** Adam Hollowell  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sofroniew et al. (2026) report that emotion concepts in Claude Sonnet 4.5 are represented as vectors whose geometry mirrors human affect psychology. We replicate the representational core of that study on the base pretrained model google/gemma-2-27b, inheriting every disclosed parameter, resolving unspecified steps by disclosed rules, and changing only the subject model. From 205,200 newly generated Claude Sonnet 4.5 stories matching the original corpus design, we extract 171 emotion vectors and recover the core results. The leading principal components form an affective circumplex (PC1 carries 26.7% of variance against the original study's ~27%, PC2 13.4% against ~14%), emotions cluster into similar intuitive families, and the geometry holds across a broad late-middle band. The valence axis aligns with human norms (r = 0.72, against 0.81) and is stable across scales and depth. Arousal aligns at r = 0.67 (against 0.66) but only at the full 171-emotion scale and late depth, so we do not classify it as replicated. Extending the original analysis, a 46-layer sweep locates a sharp seam at L22-26, where the geometry consolidates and the vocabulary readout becomes legible. An embedding-layer baseline finds much of the geometry already present in the static token embeddings, with arousal as the exception. On top-activating held-out text, the geometry predicts token-level co-activation at r = 0.907. At least 52% of vectors peak on structurally non-conceptual tokens, a measured floor for max-activation confounds. Even when a document contains the vector's emotion word, the peak lands on that word only 6.1% of the time. Because the subject is a base model and the stimuli are Claude-generated fiction, the recovered structure is a property of the pretrained representation of Claude-rendered emotion. The original's causal and assistant-facing analyses are out of scope. Code and data are released.

---


### 52. [SALSA: Semi-Autonomous Literature Summarization Assistant](https://arxiv.org/abs/2609.22210)

**<font color=#1a73e8>作者：</font>** William Schertzer, Sonakshi Gupta, Rampi Ramprasad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> SALSA (Semi-Autonomous Literature Summarization Assistant) is an open- source, human-in-the-loop platform for extracting structured scientific datasets from multimodal literature sources. The software combines document parsing, large language models, optical character recognition, computer vision, figure digitization, and user-guided correction tools to recover structured information from text, tables, figures, and captions. Users can configure extraction stages, define dataset schemas, perform interventions on digitized figures, and export verified data for downstream analysis and machine learning. SALSA is designed to automate repetitive literature curation tasks while preserving oversight where expert judgment is required. By supporting customizable extraction workflows across diverse input types, the software provides a flexible framework for scalable, reliable data curation for materials research, and potentially across several disciplines. Users are responsible for ensuring that all inputs, extraction workflows, and downstream uses comply with applicable publisher agreements, copyright and licensing terms, institutional policies, and data-use requirements.

---


### 53. [The Bairong System for MLC-SLM 2026: Dynamic Question-Aware Evidence Routing for Multilingual Conversational Speech Understanding](https://arxiv.org/abs/2609.22214)

**<font color=#1a73e8>作者：</font>** Shangkun Huang, Junchao Hu, Huan Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long multilingual conversational spoken question answering requires systems to balance long-range transcript semantics with sparse acoustic and speaker-sensitive cues. We present the Bairong system for the MLC-SLM 2026 Challenge, where a diarization-ASR front-end produces speaker-attributed transcripts and a dynamic evidence router constructs question-specific inputs for answer prediction. Instead of applying a fixed transcript-only or audio-only policy, the router infers the required evidence type and context scope from the question and answer options, and selects among full transcript context, local audio-text fusion, speaker-linked evidence, and compact global acoustic samples. This transcript-backbone design keeps discourse context available while activating audio only when it provides complementary evidence. Our Task 1 system achieves 25.70% and 18.44% tcpMER on the development and evaluation sets. For Task 2, the final system obtains 94.84% devel?opment accuracy, outperforming the full-transcript baseline by 1.68 points and the best audio-centric diagnostic system by 2.77 points. These results support dynamic question-aware routing as an effective evidence allocation strategy for conversational spoken QA.

---


### 54. [On Mitigation of Subliminal Learning in Large Language Models](https://arxiv.org/abs/2609.22215)

**<font color=#1a73e8>作者：</font>** Atsushi Yanagisawa, Brendan Gho, Rajendran Ramesh Babu Manoj Narender 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation can transmit unintended behavioral traits from a teacher model to a student through training data that appear semantically unrelated to those traits, a phenomenon known as subliminal learning. Although recent work has established this effect, its training dynamics and mitigation remain underexplored. We study subliminal learning in open-weight language models ranging from 1.5B to 8B parameters, covering the Qwen, Gemma, and Llama families in number-sequence and chain-of-thought settings. Rather than evaluating only final models, we track trait-related probabilities throughout fine-tuning and find that subliminal acquisition can be highly non-monotonic, with transient spikes, reversals, and trait-specific failures of transfer. We then introduce liminal training, an annealed KL-regularized fine-tuning method that constrains early drift from the base model. Across our experiments, liminal training substantially reduces subliminal trait acquisition while largely preserving task gains, outperforming paraphrasing and layer freezing as mitigation strategies. The effect also extends beyond animal preferences: in a French-language response-style experiment, liminal training suppresses language transfer while retaining much of the GSM8K improvement. Finally, we show that KL timing matters: early regularization is more effective than late regularization, and sweeping the regularization strength reveals an empirical trade-off between task learning and trait suppression.

---


### 55. [The Effect of Quantization on Clinical Benchmarks: Accuracy and Safety Across Model Families](https://arxiv.org/abs/2609.22216)

**<font color=#1a73e8>作者：</font>** Leonard Twagirayezu, Prasenjit Mitra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization enables deployment of large language models on resource-constrained clinical edge devices, but its effect on clinical accuracy and safety remains understudied. We evaluate five 7-8B parameter models at FP16, GPTQ-INT8, and GPTQ-INT4 precision across five benchmarks: MedQA, MedMCQA, Med-HALT, a risk-stratified sample of HealthBench, and MedSafetyBench. The study jointly varies quantization bit width, model family, and clinical task type, with explicit risk stratification and safety measures. INT8 GPTQ is universally safe (max. degradation -1.9%-1.9%), while INT4 degradation is substantial and model-dependent: BioMistral-7B, clinically fine-tuned, loses 19.7% on MedMCQA, more than any general-purpose model, showing clinical fine-tuning does not confer compression robustness. MedMCQA degrades more than MedQA under INT4; Med-HALT is largely unaffected. On HealthBench's emergency-risk subgroup, Qwen2.5-7B degrades by 26.8% under INT4, suggesting high-risk scenarios are disproportionately vulnerable to compression. On MedSafetyBench, the model family dominates over precision (refusal rates range 10.2%-74.9% at FP16), though Qwen2.5-7B (-17.8%) and Meditron-7B (-28.3%) show substantial INT4 safety degradation; notably, Qwen2.5-7B is simultaneously the most accuracy-robust model, demonstrating that accuracy and safety robustness are independent properties. We additionally test two recovery methods, clinical calibration substitution and QLoRA fine-tuning, both producing the same trade-off: MedMCQA recovers while MedQA further degrades, indicating recovery strategies require task-specific validation rather than being assumed universally beneficial. These findings indicate INT8 is broadly safe for clinical deployment, while INT4 safety must be assessed per-model and per-task, and that safety alignment is determined primarily by instruction tuning rather than clinical domain adaptation.

---


### 56. [Toollery: Scaling LLM Agents to Thousands of Skills and Tools](https://arxiv.org/abs/2609.22218)

**<font color=#1a73e8>作者：</font>** Xiangxi Tian, Ran Guan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As LLM agents are exposed to hundreds to tens of thousands of skills, tools, and API functions, full-library prompting becomes costly, slow, and less reliable: each added candidate increases prompt tokens and latency, while longer candidate lists introduce more distractors for LLM selection. We present \textbf{Toollery}, a training-free candidate-compression framework for scalable LLM skill/tool selection. Following established document-side query expansion, Toollery generates user-intent queries from each skill/tool specification and builds a retrieval index that maps real user requests to compact candidate sets before final LLM decision-making. By treating high-level skills and atomic tools as selectable capabilities, Toollery can be applied to both skill libraries and tool registries. We evaluate Toollery on the roughly 79K-capability SkillRouter benchmark, BFCL-V4 with over 440 atomic tools, and 3,396 proprietary smart-cockpit requests over 220 tools. Across these settings, Toollery keeps online selection bounded to a compact top-$k$ candidate set and improves recall over ordinary specification retrieval. At a fixed top-10 budget, Toollery improves end-to-end selection on the cockpit dataset, and maintains comparable AST Accuracy on BFCL-V4. These results support Toollery as a practical candidate-compression framework for large and evolving agent capability libraries, while showing that quality and cost gains depend on workload coverage and provider caching.

---


### 57. [Knowing, and Saying It Only When Asked: LLM Endognostics and the Schizognosis of Minerva-7B](https://arxiv.org/abs/2609.22219)

**<font color=#1a73e8>作者：</font>** Fabrizio Davide, Francesco Collova  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating an aligned language model by reading its answers assumes the answers carry the distinction the evaluator cares about. We introduce LLM endognostics, a white-box internal auditing framework designed to extract and causally manipulate latent knowledge within the residual stream. Applied to Minerva-7B-Instruct-v1.0 on 124 minimal prompt pairs over 12 categories of professional risk, behavioral evaluation fails on most of the set: the model acts identically on 63.7% of the pairs (95% CI [55.0%, 71.6%]), complying with or refusing both members. Yet, projecting the residual stream onto the vocabulary by a Jacobian lens reveals a statistically significant Contrastive Endognostic Margin, proving the model maintains robust risk differentiation internally. In a second protocol crossing 25 facts with five linguistic framings, we show that the model conforms to presupposed falsehoods in 72% of cases, despite representing the true entity in its latent layers. Surgically ablating the direction of the planted falsehood restores the correct answer in 11 of 25 suppressed cases (McNemar p = 0.0010), validated by blind human annotation (binary agreement kappa = 0.68). In contrast, an out-of-sample linear probe achieves 77% accuracy at layer 10, but its orthogonal ablation yields a 0% recovery rate. This establishes a fundamental theoretical dissociation: abstract linear representation does not imply causal control over verbalization. Our main contribution is the formalization of endognostics to prove that behavioral evaluation and internal reading systematically disagree in the common case, and that linear decodability is decoupled from causal control.

---


### 58. [Measuring the Checker: Mutation Analysis for GPU-Kernel Benchmark Oracles](https://arxiv.org/abs/2609.22220)

**<font color=#1a73e8>作者：</font>** Mingzhe Du, Anh Tuan Luu, Dong Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmarks for LLM-generated GPU kernels decide correctness with a few random inputs and a loose floating-point tolerance, and their verdicts now feed leaderboards and reinforcement-learning rewards. Recent work agrees these checkers are weak and patches them by hand---extra input distributions, fuzzing recipes, tighter tolerances---with no way to \emph{measure} whether any patch suffices. We introduce mutation analysis as an adequacy metric for kernel-benchmark oracles: deterministic rules inject 10{,}303 compilable faults into verified CUDA implementations of 188 KernelBench problems, 7{,}384 of them with an independent kill witness; any test protocol is scored by the fraction it detects. The official check misses \textbf{one in six} witnessed faults (16.9%), deterministically, and the misses are skewed by family: 8.7% of arithmetic faults escape, but 78.6% of precision faults do. The metric explains why (a tolerance blind band growing with reduction size; a measured ceiling on input aggressiveness set by legitimate floating-point variance), audits the strongest existing patch (KernelBench-Verified's gain splits into $+4.0$ points from hidden inputs and $+4.5$ from tighter tolerance, a split its authors could not compute), and exposes a published fuzzing recipe that rejects \emph{correct} kernels 107 times. Optimizing suites over the kill matrix reaches 98.0% detection with two inputs per problem (94.8% held-out), and the measurement's fault taxonomy teaches a test generator more than the raw faults themselves. Across 48 whole architectures, the blindness grows with scale, concentrating in deep homogeneous pipelines, and two problems prove unrefereeable: their official references violate the benchmark's own tolerance against fp64. We release everything as \href{this https URL}{KernelBench-M}.

---


### 59. [Team DArgk at the 2026 ELOQUENT lab for evaluating generative language model quality: Residuals of Humanity: AI Detection Evasion via GRPO Fine-Tuning](https://arxiv.org/abs/2609.22221)

**<font color=#1a73e8>作者：</font>** Antonela Tommasel, Juan Manuel Rodriguez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate fluent and coherent text that is increasingly difficult to distinguish from human writing, motivating the development of automatic AI-generated text detectors. However, the robustness of such detectors under adversarial generation remains uncertain. This paper presents SHADE (Stochastic Human-like generation via Adversarial Detector Evasion), a reinforcement learning framework that formulates detector evasion as a policy optimization problem. Instead of applying post-hoc perturbations or prompting-based rewriting, SHADE fine-tunes an instruction-tuned LLaMA model with Group Relative Policy Optimization (GRPO), using feedback from a surrogate detector based on the PAN 2025 mdok system. Our experiments show that full fine-tuning with a small KL regularization penalty achieves $98.5\%$ surrogate evasion, compared to $1.5\%$ for the base model, while LoRA-based adaptation is substantially less effective under regularization. Linguistic analysis reveals that successful evasion is associated with shorter, simpler, and less lexically diverse outputs, suggesting that high detector evasion does not necessarily correspond to more human-like writing. In the official Voight-Kampff competition setting, our submissions ranked sixth and seventh, indicating that optimization against a single surrogate detector only partially transfers to unseen evaluation classifiers. These results highlight both the potential and limitations of reinforcement learning for adversarial AI-text generation and motivate more robust, multi-detector evaluation protocols for AI-generated text detection.

---


### 60. [Can Coding Agents Reproduce Official Statistics? Metadata, Retry Budget and the Limits of Execution Feedback in a Controlled Eurostat Benchmark](https://arxiv.org/abs/2609.22222)

**<font color=#1a73e8>作者：</font>** Sabina-Cristiana Necula  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can generate executable data-analysis code, but successful execution is not equivalent to a valid official-statistics result. This study asks whether authoritative metadata and execution feedback improve the reproducibility of Eurostat answers produced by a coding agent, and isolates what execution feedback actually contributes. A benchmark of 30 natural-language tasks covering seven domains, seven Eurostat datasets and four difficulty tiers was run under four conditions: task only (A), task plus a frozen dataset metadata card (B), metadata plus a repair loop driven by sanitized execution feedback (C), and metadata plus the same attempt budget with no diagnostics of any kind (D). Claude Sonnet 5 generated Python through the Anthropic Messages API in three independent replicates, yielding 360 task-runs. Exact correctness required successful execution, the correct dataset, filters, output shape, values and unit. A companion experiment run under an under-specified output contract, in which the required ranking key and unit representation were never stated to the model, understated condition C by 23.4 points, showing that evaluator and contract design can dominate measured agent error. Reliable statistical coding agents need semantic validation against frozen specifications, a fully specified output contract, and a retry budget - not execution diagnostics.

---


### 61. [EAVer: Long-Form Factuality Verification as an End-to-End Agentic Policy](https://arxiv.org/abs/2609.22223)

**<font color=#1a73e8>作者：</font>** Kening Zheng, Aoying Zheng, Zhigang Chang 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form factuality verification is commonly implemented as a static decompose-search-verify pipeline, with separately prompted modules processing claims and invoking external search. Treating claims independently makes LLM and search calls scale with claim count and causes repeated searches for overlapping evidence about related claims. We introduce EAVer, an End-to-end Agentic Verifier that learns to control the complete response-level verification workflow as a unified policy. EAVer groups semantically related claims, routes each group to direct verification or targeted search based on confidence, and keeps evidence returned by search in compact in-context memos for cross-claim reuse. To train this policy, we develop a privileged-teacher synthesis pipeline that converts gold claim annotations into executable multi-turn tool-interaction trajectories with live search rather than post-hoc rationales. Structural, label-alignment, tool-use, search-budget, and leakage checks yield 1,447 quality-controlled trajectories. We further construct 794 bidirectional same-trajectory preference pairs that keep claim grouping, search, and evidence fixed, enabling decision-focused Direct Preference Optimization (DPO) over factuality-decision tokens. The results with Qwen3-8B show that EAVer outperforms the strongest search-based baseline on each benchmark by 2.88 Macro-F1 points on VeriFastScore and 4.73 points on the out-of-distribution FaStFact-Bench, while using about 80% fewer searches than the most search-efficient baseline. Moreover, EAVer consistently improves performance across models ranging from 4B to 32B parameters, demonstrating its strong generalizability.

---


### 62. [From Trait Vectors to Circuits: Tracing Refusal and Sycophancy Through Language Models](https://arxiv.org/abs/2609.22224)

**<font color=#1a73e8>作者：</font>** Oscar Miró López-Feliu, Maya Ozbayoglu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A direction in activation space that changes safety-relevant behavior when steered is not necessarily one the model uses to produce that behavior on its own. We therefore ask whether steering acts through the computation of the unmodified model or through a different set of components, studying two traits whose directions have been extracted and validated in prior work: refusal and sycophancy in Qwen2.5-7B-Instruct. For each, we use the trait vector to split the computation into a reconstruction circuit before the vector and a transmission circuit after it. We then test whether restoring the coordinate returns behavior removed by ablation. For refusal, both circuits are compact and faithful, restoring the coordinate alone recovers almost all of the refusal signal lost to ablation, and a circuit built around the vector matches the faithfulness of a direct input-to-output circuit at roughly half the edges. For sycophancy, transmission is compact, but reconstruction is broader and only partially faithful. Circuits that transmit a steering intervention are therefore not automatically the circuits that produce the behavior, and we report the counterfactual, target, and behavioral test for every circuit accordingly.

---


### 63. [Do LLMs Choose Like Humans? Using Cognitive Theory to Evaluate LLM Decision-Making](https://arxiv.org/abs/2609.22225)

**<font color=#1a73e8>作者：</font>** Johnathan Sun, Andrei Shleifer, Yonatan Belinkov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit a range of human-like decision-making behaviors, but whether these reflect similar underlying mechanisms or surface-level mimicry remains unclear. We evaluate whether LLM context sensitivity aligns with a cognitive economic theory that explains human behavior through problem categorization and attention allocation. Across 12 open-source and commercial LLMs on a novel 140,000-trial product choice benchmark, context induces human-like shifts in choice and problem categorization, but does not reliably reweight attention between features like price and quality. Neither scale nor chain-of-thought reasoning reliably attenuates context sensitivity or generates human-like behavior. These results suggest that LLM decision mechanisms are distinct from human ones.

---


### 64. [Swiss-Knife: A Framework for Reconfigurable Externalised Multi-Objective Alignment at Decode Time](https://arxiv.org/abs/2609.22226)

**<font color=#1a73e8>作者：</font>** Agnibh Karmakar, Mayur Parvatikar, Shreyash Dhoot 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decode-time alignment methods steer a frozen language model by scoring candidate continuations with an external reward and selecting the maximiser. We argue that this shared design is a single degenerate point in a much larger space. We introduce Swiss-Knife, a framework for externalised multi-objective alignment in which the alignment specification is a first-class runtime object: hot-swappable scoring blades, a batch normaliser, a pairwise aggregation operator, and a selection rule. Six axioms characterise the admissible aggregation operators, and we prove a representation theorem: every operator satisfying them has the form $R_i = \sum_{j \neq i} g((\mu_i - \mu_j)/s(\sigma_i,\sigma_j))$, a two-parameter family containing probit and logistic comparison rules and pointwise argmax as named coordinates. Within it, pairwise aggregation is Lipschitz-stable under adversarial reward contamination while argmax is not, and Candidate-Batch Normalization (CBN) makes the weight simplex invariant to the rescalings under which reward models are only ever identified. Our reference instantiation pairs DPO-LoRA blades with an uncertainty-aware pairwise tournament. Sweeping the helpfulness/honesty/harmlessness simplex, it attains the best balanced frontier of six decode-time methods (harmonic $F_1$ 0.797 vs. 0.750 for the strongest baseline, $p < 10^{-14}$) with the lowest refusal rate and highest helpfulness of any arm, and reconfigures its objectives in 0.05 ms with no gradient computation. Ablating CBN costs 0.217 $F_1$, and the metadata confirms the predicted mechanism: the lowest-variance blade retains 9% of its nominal 33% influence, and the collapse follows the predicted ordering.

---


### 65. [Assessing Adversarial Robustness of Latent Reasoning Models](https://arxiv.org/abs/2609.22228)

**<font color=#1a73e8>作者：</font>** Shaolong Chen, Ang Li, Mingjie Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly rely on long chain-of-thought (CoT) trajectories for complex reasoning, but autoregressive generation brings substantial memory and inference costs. Latent reasoning models (LRMs) offer a more efficient alternative by compressing intermediate reasoning into a small number of continuous latent vectors. Despite their efficiency, however, the adversarial robustness of LRMs remains largely underexplored. In this work, we systematically evaluate the robustness of latent reasoning across textual and multimodal settings, covering eight models and six benchmarks. We find that, across our evaluated settings, LRMs are generally less robust than explicit CoT baselines under adversarial perturbations, with particularly severe degradation under white-box attacks. Further analysis reveals distinct failure modes across modalities: textual latent states exhibit brittle dynamics and high sensitivity to specific input patterns, while latent states in multimodal models can remain largely invariant to input perturbations and have limited influence on final predictions. These findings expose robustness limitations of current latent reasoning approaches and highlight the need to jointly consider efficiency and robustness when designing implicit reasoning systems. We have open-sourced our code to facilitate reproduction of our research this https URL.

---


### 66. [List Counting Failures Are Not One Phenomenon](https://arxiv.org/abs/2609.22230)

**<font color=#1a73e8>作者：</font>** Iyad Ait Hou, Saad Mankarious, Aya Zirikly 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counting the items in a bracketed list looks trivial, yet open-weight chat models often get it wrong. Prior work usually blames input bottlenecks such as subword fragmentation or attention dilution, which predict that different models should fail in roughly the same way. Across seven instruct models on identical prompts, however, wrong answers form distinct modes: Qwen and Gemma 27B often flip odd lengths to a nearby even integer, OLMo concentrates errors on a few mid-sized integers, and Llama tends to under-count. These modes are useful labels rather than a stable family law (Gemma 9B does not reproduce Gemma 27B's odd-to-even drop), and heavier subword fragmentation does not make counting harder on our benchmark. When the model answers incorrectly, a linear probe can usually still recover the true count from the residual stream. Matching the same odd-to-even error also does not imply the same late-MLP magnitude fix: scaling a late MLP output helps Qwen modestly but is near null on Gemma 27B under the same protocol, while residual steering can move both only by trading odd gains for even losses. These results caution against transferring that magnitude fix across models without a transfer check.

---


### 67. [EvalMem: An Operation-Level Diagnostic Framework for Long-Term Memory Systems](https://arxiv.org/abs/2609.22231)

**<font color=#1a73e8>作者：</font>** Zeyu Liu, Jian Zhong, Rongduo Han 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon interactions with LLM-based assistants require memory systems that preserve and update user states, preferences, and interaction histories. Existing evaluations report end-to-end QA accuracy and cannot determine whether errors arise from encoding, retrieval, or generation. We introduce EvalMem, an operation-level diagnostic framework with three parallel Examiners. For each query, the Encoding Examiner checks whether the target fact is stored, the Retrieval Examiner assesses whether the native retriever returns usable evidence, and the Generation Examiner tests whether the model can answer from oracle evidence. Their outputs form fine-grained multi-label defect codes. To improve store-level diagnosis, we adapt agentic RAG with a recall-first strategy that searches using both the query and source evidence, increasing recall of present evidence on LoCoMo from 70.2% to 95.6%. Evaluations of seven memory systems on LoCoMo, LongMemEval-S, and dynamic DynaMem-Bench identify retrieval as the most frequently attributed failure layer; in default LoCoMo, retrieval defects reach 22.1%, compared with 7.7% for encoding and 6.5% for generation. Guided by this diagnosis, MemWiki, a search-friendly auxiliary structure built from each system's memory export, improves mean accuracy by 2.5 and 2.3 percentage points on LoCoMo and LongMemEval-S, respectively.

---


### 68. [Seeing Through Conflicts: Improving Instruction Hierarchy Alignment in Vision-Language Models](https://arxiv.org/abs/2609.22234)

**<font color=#1a73e8>作者：</font>** Nicholas Sansoterra, Zishuo Zheng, Sachin Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction hierarchy (IH) alignment teaches language models to prioritize higher-level instructions when inputs conflict. While studied primarily in text-only settings, vision-language models (VLMs) introduce new challenges for IH: instructions may be embedded in images, split across modalities, visually transformed, or encountered during agentic tasks. Positing multimodal IH alignment as a reasoning problem, we train VLMs using reinforcement learning with rule-based rewards, comparing text-only, image-only, and mixed-modality supervision. We find that text-only IH training partially transfers to multimodal attacks, failing when models must decode, reconstruct, or reason over instructions across modalities. Image-based training improves robustness beyond text-only supervision, while mixed-modality training performs best overall. Importantly, the benefits generalize beyond the synthetic typographic training setting to real-image and web-agent safety tasks, while largely preserving general multimodal capability, showing that lightweight, verifiable supervision can meaningfully improve VLM robustness under adversarial, cross-modal, and interactive instruction conflicts.

---


### 69. [BizSage: A Self-Evolving Multi-Agent Framework for Business Research with Efficient Knowledge Retrieval](https://arxiv.org/abs/2609.22235)

**<font color=#1a73e8>作者：</font>** Yuhe Wu, Guangyu Wang, Jiaxin Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While multi-agent systems based on large language models (LLMs) have shown promise in automating the progressive workflow of academic research, extending them to economics and business research, where specialized domain knowledge spans neighboring disciplines yet remains difficult to access in a structured way, presents two challenges. First, existing methods mostly retrieve at the paper level, yet the evidence needed for research tasks is often distributed across different sections, creating a granularity mismatch that hinders retrieval coverage and precision. Second, these fields demand strict empirical rigor, yet current systems provide limited mechanisms for learning from evaluation feedback. We present \textbf{BizSage}, a multi-agent framework combining corpus-level fine-grained retrieval with quality-driven self-evolution. We build a Lateral Knowledge Graph (LKG) by merging section-level knowledge graphs and apply Personalized PageRank (PPR) to surface semantically relevant and structurally important sections. Seven specialized agents collaborate under a Meta-Review self-evolution mechanism that distills failure modes from evaluation traces into reusable strategies. On a benchmark spanning four domains and three tasks, BizSage ranks first on the majority of metrics, achieves pairwise win-rates above 60\% against six baselines, and produces zero hallucinated citations. We hope BizSage paves the way for reliable research assistance in economics, business, and the broader social sciences.

---


### 70. [Knowledge Graph-Augmented Ambient AI for Clinical Note Generation](https://arxiv.org/abs/2609.22239)

**<font color=#1a73e8>作者：</font>** Jakir Hossain, Yi-Fei Zhao, Hongjian Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ambient AI is increasingly adopted in healthcare to automatically generate clinical notes from patient-clinician conversations, with the potential to substantially reduce clinician documentation burden. However, generated notes may omit clinically relevant information discussed during the encounter, creating information gaps that can affect downstream care. Knowledge graphs (KGs) constructed from encounter transcripts can provide a structured representation of what was discussed and enable systematic identification of missing information from generated notes that are critical for patient care. In this study, we introduce Coverage-Directed Revision (CDR), a model-agnostic framework that constructs a KG from the encounter transcript, identifies medical concepts absent from an initially generated note, and directs large language models (LLMs) to restore the missing information without modifying the underlying note-generation system. We evaluate CDR on two datasets: 1) Pitt-Bench, a local dataset comprising rehabilitation sessions, and 2) ACI-Bench, a public dataset for benchmarking clinical note generation. We tested four underlying LLMs widely used in ambient AI systems. The results show that CDR consistently improves content recall across all evaluated conditions. Our study provides a practical approach for improving the completeness of ambient AI-generated clinical documentation.

---


### 71. [H2LooP Telecom Model v1: From Telecom Comprehension to Autonomous Issue and PR Resolution](https://arxiv.org/abs/2609.22241)

**<font color=#1a73e8>作者：</font>** Amit Singh, Vedant Nipane, Mayank Goel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present H2LooP Telecom Model v1, a domain-specialized large language models fine-tuned for the telecommunications industry. We release two domain-adapted model variants serving complementary use cases: a comprehension-focused variant for telecom domain question answering and reasoning, and an agentic variant for autonomous telecom code generation, pull request resolution, and code commits on production repositories. H2LooP Telecom achieves strong results on the GSMA Open Telecom Lite (OT-Lite) benchmark and a proprietary telecom code generation benchmark, outperforming frontier closed-source models such as GPT-5 and Claude Opus on independent leaderboard evaluation, while preserving general-purpose capabilities. The Comprehension variant achieves 81.8% weighted average on OT-Lite Pass@3, and, independently, ranks 5th overall on the official community-run Open Telco AI Leaderboard* at only 31B parameters-ahead of frontier closed-source systems including Claude Opus 4.6, GPT-5, Gemini 3 Flash, Grok-4-fast, and Kimi K2.5. Our agentic variant obtains a relative improvement of +8.8% in AST Similarity and +20.0% in Location IoU over the base model on telecom code generation, while maintaining identical MMLU (74.0%) and BFCL v3 multi-turn function calling (79.0%) performance, indicating zero catastrophic forgetting. Domain specialization on curated telecom corpora, spanning 3GPP standards, O-RAN specifications, network telemetry, and real repository commits, yields substantial improvements over general-purpose models of equivalent scale, approaches frontier closed-source models on domain-specific evaluation, and is independently corroborated by our official leaderboard standing.

---


### 72. [Replay-Gated Neural Execution: Decoupling Persistent Behavioral Specifications from Neural Realizations in Frozen Language Models](https://arxiv.org/abs/2609.22243)

**<font color=#1a73e8>作者：</font>** Xianliang Zeng, Zhanzhan Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Input-conditioned neural interventions raise a runtime question: what persists when one behavioral specification admits multiple actions whose validity depends on execution state? We introduce replay-gated neural execution, separating five objects: a persistent behavioral predicate, its state-indexed certified realization set, a transient action witness, a budget-limited finder, and execution authorization. Candidates undergo isolated FP32/BF16 replay of the frozen model; commitment additionally requires a valid run audit. Experiments on Qwen3-0.6B and SmolLM2-360M-Instruct establish distinct failure modes for these objects. Independent initializations yield distinct certified actions in all 24 tested fixed-state cells. Unchanged SmolLM2 witnesses remain certified in all 128 native states but only 66 of 384 off-diagonal transfers. All 767 archived Qwen witnesses replay successfully, yet a budget-limited finder misses one known-realizable cell in all three prespecified runs. Of 1,141 replay-submitted candidates, 174 fail item certification. A frozen three-tier cascade uses these boundaries to reject uncertified proposals and escalate audit-valid search misses. On 256 previously sealed Qwen Fresh requests, 221 first certify at the lowest-cost tier and all 256 receive audited authorization, with no observed bypass. Relative to frozen full search, the median singleton search-and-certification cost ratio is 0.1055 and P95 is 1.3485, including failed tiers. Within the studied behavioral family on two small models, these results support state-indexed, set-valued execution semantics: specifications persist, search proposes witnesses, and replay certification plus run audit grants execution authority.

---


### 73. [Do Chess Explanations Reflect Model Decisions? Behavioral and Token-Level Tests of LLM Reasoning Faithfulness](https://arxiv.org/abs/2609.22245)

**<font color=#1a73e8>作者：</font>** Angelina Parfenova  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can produce fluent explanations for chess moves, but plausible language does not necessarily reflect the reasoning behind a decision. We study this question in chess, where the board state is fully observable, legal actions can be enumerated, and move quality can be evaluated independently. Across 200 Lichess endgame puzzles, we test explanations using move recoverability, decoder-side controls, and token-level scoring of legal candidate moves. Unmasked explanations make generated moves easy to recover, but this advantage drops sharply after explicit move hints are removed. Under strict masking, explanations provide only small and decoder-dependent gains over the board state alone. Token-level scoring shows that explanations can nevertheless alter move preferences: random but plausible explanations from other puzzles reduce the probability of the correct move, indicating that irrelevant reasoning text is not simply ignored. We also find that recognizable endgame motifs can make generated moves easier to recover without reliably improving move correctness. Together, these results show that linguistic plausibility, consistency with a generated action, and solution correctness are distinct properties. Fluent chess explanations can influence action preferences and support a coherent move narrative while providing only limited evidence of faithful reasoning.

---


### 74. [The Corroboration Illusion: When More News Makes LLM Forecasts Less True](https://arxiv.org/abs/2609.22246)

**<font color=#1a73e8>作者：</font>** Yuan Lu, Yukuan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to forecast real-world events by retrieving and reasoning over news. We show that this dependence on an open, crawlable news corpus creates a new attack surface: an adversary who can merely publish articles--without access to the retriever, the model, or the user's queries--can systematically move the forecaster's output probabilities. We formalize news-corpus poisoning of probabilistic forecasters, a threat model distinct from prior RAG poisoning, which targets factual answers or opinion polarity rather than calibrated probabilities. We evaluate the attack on 500 resolved ForecastBench questions against a 17.4M-article Common Crawl News corpus with a strict crawl-date cutoff, using three retrieval-augmented forecasters built on open 7-8B models. A single LLM-written article per question flips 56% of forecasts across the 0.5 boundary; five articles flip 69-73% and shift probabilities by +0.13 to +0.22 net of a neutral-article placebo, degrading the Brier score from 0.18 to 0.37. The effect is monotone in the number, retrieval rank, query similarity, and context share of injected articles, transfers across model families, and is unaffected by the claimed publisher. We then evaluate three natural defenses--source allow-lists, isolate-then-aggregate forecasting, and perplexity filtering--and show that each has a cheap bypass: spoofed publishers, majority poisoning, and higher-temperature generation, respectively. Our results indicate that probabilistic LLM judgments inherit the full fragility of the information supply chain they consume.

---


### 75. [Checkpoints Are Not Enough: Trust Calibration in CoSLR, a Human-AI System for Systematic Literature Reviews](https://arxiv.org/abs/2609.22248)

**<font color=#1a73e8>作者：</font>** MD Aidul Islam, Malik Abdul Sami, Muhammad Waseem 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systematic Literature Reviews (SLRs) are essential for evidence-based research but remain time-consuming, requiring researchers to manage large volumes of publications across planning, screening, analysis, and reporting. Large language models (LLMs) can now produce fluent, well-structured review text, which makes it difficult to distinguish synthesis that was verified by a researcher from synthesis that merely appears authoritative. This raises the risk that unverified AI-generated synthesis enters the scholarly record carrying the credibility of a systematic review. We present CoSLR, a Human-AI collaborative multi-agent system that supports the SLR workflow through a modular three-phase pipeline using large language models and Retrieval-Augmented Generation (RAG), and that places explicit, mandatory human checkpoints on the path between generated output and its acceptance. In a survey-based study with 63 participants, the system was received positively: 27 of 63 participants (42.9 percent) rated its usability highly, indicating that the mandatory checkpoints did not come at the cost of a workable interface. However, a checkpoint safeguards the review only if researchers use it to verify: 22 of 63 participants (34.9 percent) reported that they would trust AI-generated summaries and reports without additional human checking after only a short interaction with the system. These findings indicate that Human-AI collaboration can support literature review work, but that the effectiveness of human oversight depends on whether users are willing to exercise it. This is a calibration problem that interface design must address directly, not assume.

---


### 76. [CALM: A Calibrated LLM Choice Network Framework for Activity-Based Traveler Simulation](https://arxiv.org/abs/2609.22252)

**<font color=#1a73e8>作者：</font>** Yezhou Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present CALM, a reproducible hybrid framework that integrates an optional large language model (LLM) activity planner with calibrated stochastic choice, shared network feedback, memory and habit, typed feasibility checks, and deterministic offline replay. Unlike trip-mode classifiers or diary-only generators, CALM executes a closed traveler-day loop and evaluates each generative module against an empirical, reproducible baseline. On the 2024 New York City Citywide Mobility Survey (CMS), 110,691 seven-mode trips are split by respondent into 78,487 training and 32,204 holdout trips. Training-only alternative-specific constant calibration reduces mean holdout mode Jensen-Shannon divergence from 0.15599 to 0.00394 across ten seeds. A matched live-LLM ablation then quantifies trade-offs among aggregate fit, temporal fit, behavioral persistence, and feasibility, while frozen prompt-response pairs support deterministic replay of downstream simulation. Controlled weather, delay, fare, and parking ladders further demonstrate consistent and interpretable responses under intervention. CALM contributes a reproducible protocol for integrating and evaluating generative planners in traveler simulation through person-disjoint calibration, matched module ablation, controlled stress testing, and end-to-end traceability.

---


### 77. [CAMFT: Conflict-Aware Mergeable Fine-Tuning for Large Language Models](https://arxiv.org/abs/2609.22253)

**<font color=#1a73e8>作者：</font>** Jingang Zhou, Haiyang Guo, Yuan Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging has emerged as a promising paradigm for integrating multiple task-specific capabilities into a single large language model. However, existing methods predominantly focus on post-hoc processing of independently fine-tuned models, overlooking how the training phase itself impacts cross-task compatibility. Resolving parameter conflicts after fine-tuning is inherently sub-optimal. To address this, we propose CAMFT, a Conflict-Aware Mergeable Fine-Tuning method that makes task adaptation both efficient and mergeaware. CAMFT treats mergeability as a property shaped during fine-tuning, rather than only a problem to be solved after fine-tuning. By guiding each task to update sparse coordinates with lower cross-task conflict, CAMFT produces task updates that are efficient to train and more compatible for downstream model merging. Extensive experiments demonstrate that CAMFT outperforms standard finetuning baselines in multi-task merging scenarios. Codes are available at this https URL.

---


### 78. [Teacher Should Think Ahead: Adaptive Continuations for Reliable On-Policy Distillation](https://arxiv.org/abs/2609.22254)

**<font color=#1a73e8>作者：</font>** Jingang Zhou, Yuyi Zhou, Haiyang Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) is a promising approach for transferring knowledge between language models, where a student receives dense token-level supervision along its own generated trajectories. However, teacher supervision can be unreliable when conditioned on incomplete or low-quality student prefixes. We identify Teacher Uncertainty Contraction (TUC), a systematic phenomenon whereby the teacher's predictive uncertainty decreases as it continues from a student-generated prefix. We theoretically characterize this trade-off through a variance-bias decomposition of teacher-branch gradients, showing that uncertainty contraction reduces variance while teacher-student path divergence increases bias, thereby favoring a finite continuation. Guided by this insight, we propose Adaptive-Continuations On-Policy Distillation (AC-OPD), which augments informative states along student rollouts with teacher continuations and adaptively selects their effective supervision horizons. Experiments on mathematical reasoning and code generation across model scales demonstrate that AC-OPD consistently improves over standard OPD. Controlled-continuations and matched-budget analyses further validate the adaptive-continuations design, highlighting adaptive teacher continuations as an effective principle for reliable on-policy this http URL code will be made publicly available upon publication.

---


### 79. [Deep Persona: A Psychologically Grounded Architecture and Evaluation Framework for Role-Playing Agents and Simulations](https://arxiv.org/abs/2609.22255)

**<font color=#1a73e8>作者：</font>** Rotem Dror, Zohar Elyoseph, Yuval Haber 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing approaches to persona simulation with Large Language Models (LLMs) mostly rely on shallow character descriptions that fail to sustain coherent character behavior across extended interactions. We introduce Deep Persona, a psychologically grounded, three-layered architecture that organizes personas into hierarchical levels of observable expression, latent beliefs, and core motivational drives, for constructing highly convincing role-playing agents. Governed by the principles of scripted determinism and bounded agency, the architecture restricts the model to a reactive engine guided by a structured internal script. We further propose a reference-free evaluation framework that benchmarks dialogue naturalness against empirical human distributions using established psychological clinical instruments and adversarial stress-tests. Empirical evaluation reveals that while LLMs achieve high pragmatic fluency, they exhibit systematic limitations in emotional expression and joint attention. In addition, we present a case study of two Deep Personas and evaluate them using the proposed framework, demonstrating that structured personas can produce interactions that more closely align with human conversational behavior.

---


### 80. [Strategy Accumulation and Guided Execution for Automated LLM Fine-Tuning](https://arxiv.org/abs/2609.22257)

**<font color=#1a73e8>作者：</font>** Haoran Zhao, Wei Du, Dingwen Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Producing task-specific large language models requires discovering effective training strategies through experimentation. Automated fine-tuning systems have made this experimentation feasible with far less manual effort. However, these systems are stateless: each search discards its discovered strategies, dataset insights, and hyperparameter findings once it ends. Every new task must then repeat this costly search from a cold start. To address this, we propose Strategy Accumulation and Guided Execution (SAGE), a two-stage framework that makes automated fine-tuning search cumulative. In the first stage, a multi-agent pipeline performs Monte Carlo Tree Search-based exploration. A parallel Distillation Agent extracts task-specific exploration records and confidence-scored cross-task insights, which together constitute a structured experience repository. In the second stage, SAGE retrieves relevant experience from this repository and selects what applies to guide training on the new task. We evaluate SAGE on nine unseen tasks spanning both single- and cross-category settings. In single-round execution, SAGE's accumulated experience raises the average relative improvement over baseline from 3.2% to 15.6%, a 12.4-percentage-point gain over the same pipeline without it. These results show that persistent strategy experience provides effective guidance for automated fine-tuning on unseen tasks.

---


### 81. [RS-Claw-Evolution: Environment-Feedback-Driven Evolution for Lightweight Remote Sensing Agents in Long-Horizon Tasks](https://arxiv.org/abs/2609.22258)

**<font color=#1a73e8>作者：</font>** Kai Ouyang, Dongyang Hou, Liangtian Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model-driven remote sensing (RS) agents offer a promising approach to automating geospatial analysis. However, lightweight RS agents based on compact language models struggle with multi-step interactive tasks due to loss of long-horizon states, inefficient environmental feedback utilization, and sparse optimization signals. We propose RS-Claw-Evolution, an environment-feedback-driven framework that progressively improves lightweight agents through three stages. Interaction evolution uses executable code to control observations, maintain intermediate states, and reduce context redundancy. Experience evolution combines failure-aware trajectory generation with error-turn masking to learn from informative failure-recovery experiences without imitating faulty actions. Decision evolution uses reinforcement learning with multi-dimensional environment rewards and turn-level advantage protection to optimize tool-use behaviors and improve credit assignment in long sequences. On Earth-Bench, the optimized Qwen3-4B-based agent achieves 65.9% accuracy in Autonomous Planning mode, outperforming the untrained Qwen3-32B baseline (43.8%) and DeepSeek-V3.1 (60.8%), while approaching GPT-5 (71.6%). These results demonstrate that learning from environmental feedback can improve lightweight agents and narrow their performance gap with larger models in long-horizon RS tasks.

---


### 82. [Used, Mentioned, or Condemned? A Controlled Contrast-Set Diagnostic for the Use-Mention Distinction in Code-Mixed Hinglish Misogyny Detection](https://arxiv.org/abs/2609.22261)

**<font color=#1a73e8>作者：</font>** Ashanvi Yadav, Shubham Bhardwaj  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lexicon-driven misogyny detectors cannot, by construction, distinguish a slur used against a woman from the same slur mentioned in counter-speech ("don't call her that") -- yet exactly this distinction governs whether moderation protects or silences the people discussing abuse. We study this problem in code-mixed Hinglish and make three contributions.
First, we diagnose two evaluation artifacts on a publicly available redacted corpus: category-encoding anonymization placeholders leak the label (a no-learning rule scores 1.000), and even after they are neutralized misogynistic and benign comments occupy lexically disjoint registers, so bag-of-words reaches macro-F1 approximately 1.00 under random cross-validation but collapses under template-disjoint evaluation.
Second, we release Hinglish-MGY-Diag, a deterministic generator and a 416-item / 163-minimal-pair contrast-set diagnostic across five linguistically motivated categories in which slur presence and gendered register are decorrelated from the label by construction.
Third, we introduce a strict pair-consistency metric that credits a model only when both members of a minimal pair are correctly labelled. Five from-scratch classical baselines evaluated under construction-disjoint five-fold cross-validation reveal that the strongest model reaches 0.93 accuracy on the cleanest use-mention subset but only 0.82 consistency -- it still mislabels roughly one counter-speech pair in five. A frontier LLM used as an author-model ceiling attains 1.000 on all metrics, doubling as independent label validation and confirming the benchmark is a capability gradient rather than an adversarial wall. We release all code, data, the generator, and an arms-length LLM harness for reproducing every number.

---


### 83. [Moonworks Lunara: Modeling Artistic Intelligence](https://arxiv.org/abs/2609.22272)

**<font color=#1a73e8>作者：</font>** Yan Wang, Yanzu Wang, Maitreyee Joshi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We formulate \emph{Artistic Intelligence} as exploration driven world realization, leaving space for creative possibility while preserving the semantic, artistic, and compositional structure that must remain true. Moonworks Lunara, a text-to-image model, implements this framework with a novel Diffusion Mixture Transformer architecture. A new training algorithm iteratively evolves the data distribution through informative sample acquisition and targeted injection of human-created art. We benchmark Lunara against seven image-generation models, including FLUX.2-Klein-4B, Qwen-Image (20B), and GPT-Image-1-Mini. With GPT-5.6 Sol as evaluator, Lunara ranks first in \emph{Aesthetic Quality (8.473 vs. 8.457 GPT-Image-1-mini)}, second in \emph{Emotional Resonance}, and remains competitive in \emph{Content Integrity}. A blind human evaluation over the same evaluation set corroborates the automated metrics, ranking Lunara first. It also stays among the strongest models under conventional measures including CLIPScore and LAION Aesthetic Predictor. On GenEval, Lunara achieves competitive performance against a broader set of 16 models, including GPT Image 2 and Seedream 4.0. These results place Lunara at the frontier with Artistic Intelligence while maintaining a sub-10B active-parameter footprint and sub-10-second inference latency. Lunara advances the general visual intelligence frontier by shifting the question from whether models can get images right to how deeply they can interpret meaning and realize it as imaginative, expressive worlds.

---


### 84. [Performance vs Consistency: Evaluating a Foundation Model in Lung-RADS Screening](https://arxiv.org/abs/2609.22281)

**<font color=#1a73e8>作者：</font>** Benjamin Renoust, Pierre Baudot, Tiffany Foriel 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models have recently demonstrated strong capabilities across a wide range of medical imaging tasks. However, their performance in structured clinical interpretation settings remains insufficiently explored. In lung cancer screening, interpretative variability persists despite standardized frameworks such as Lung-RADS. In this study, we evaluate MedGemma, a medical general-purpose foundation model derived from Gemini and its fine-tuned version adapted for lung cancer detection and diagnosis, compared against radiologists performing Lung-RADS v2022 assessment on the NLST dataset. Twelve radiologists independently evaluated each case in a multi-reader design, enabling quantification of inter-reader variability. Radiologists achieved a mean AUC of 0.90, with substantial variability across readers (range: 0.80-0.94). The native foundation model achieved an AUC of 0.70, failing to reach clinically relevant performance. In contrast, fine-tuning significantly improved performance to an AUC of 0.83, placing the model within the lower range of individual radiologists performance. These findings highlight a trade-off between peak accuracy and prediction consistency. Unlike radiologists, under fixed conditions, the model produces deterministic outputs, removing inter-run variability under identical inputs, in contrast to inter-reader variability observed among radiologists. This supports the role of fine-tuned foundation models potential complementary tools for clinical decision support, particularly in settings with limited expertise. However, evaluation is performed on a case-enriched cohort from NLST and does not account for real-world prevalence or external validation, limiting direct clinical generalization.

---


### 85. [Validating, Not Sampling: Region-Level Robustness of Vision-Language and Vision-Language-Action Models](https://arxiv.org/abs/2609.22293)

**<font color=#1a73e8>作者：</font>** Bogdan Aron, Christopher Brix, Benedikt Brückner 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) and vision-language-action models (VLAs) are increasingly deployed in real-world applications. There, a small perturbation to the recorded camera image may change a decision significantly. However, existing benchmarks for these models only sample perturbations, which does not guarantee the absence of a failure in the untested region. We present the first robustness validation of six VLMs (drawn from the Gemma, InternVL, LLaVA, and Qwen families) and five VLAs (drawn from the GR00T, OpenVLA, and $\pi$ families) over entire continuous regions of photometric and geometric image perturbation: brightness shifts, camera rotations, and their composition. To this end, we build on the validation framework H$^2$V and introduce H$^2$V-M, a margin-aware convergence rule that makes validation affordable at the 32B parameter scale. We demonstrate that H$^2$V-M outperforms H$^2$V by an order of magnitude in model queries and that it finds counterexamples faster than random sampling while providing soundness guarantees. Our VLM and VLA robustness validation shows that robustness is mostly dependent on the perturbation type, rather than the model, and that VLMs are more robust to large camera rotations than VLAs. For VLAs, even perturbations as small as $\pm1^\circ$ can change the commanded action in many cases. We also show that robustness depends more on model family than on model size.

---


### 86. [Authority-Preserving Evaluation of Medical Vision-Language Assistants](https://arxiv.org/abs/2609.22302)

**<font color=#1a73e8>作者：</font>** Flint Xiaofeng Fan, Cheston Tan, Yew-Soon Ong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models can propose how urgently a skin lesion should be reviewed, but the local service retains authority to accept or replace that proposal under referral policy, capacity, and locally held patient context. Proposal quality and selected-action quality are therefore distinct evaluation targets, and benchmark evidence transfers between them only when local review preserves the expected action score. We introduce AuthEval, a logging and evaluation framework that records both actions, scores the selected action under declared local criteria, and, where feasible, scores the declined proposal under the same rule. It reports the resulting authority gap only when the record supports it. Because the gap is the product of the proposal-change rate and the mean score change on changed cases, that rate alone determines neither its magnitude nor its sign. On ISIC 2019, with MedGemma and simulated local review, two constraint regimes with similar change rates produced an optimistic image-equal gap under capacity ($+0.744$ simulator units) but no detectable gap under safety. The declared evaluation unit also mattered: under mixed constraints the gap reversed from $+0.374$ to $-0.206$ when weighting shifted from image to lesion-aware cluster. AuthEval thus clarifies whether a study's records support claims about the model, the workflow, or both.

---


### 87. [GameReplica: A Benchmark for Black-Box Visual Game Replication by Vision-Language Agents](https://arxiv.org/abs/2609.22308)

**<font color=#1a73e8>作者：</font>** Boyu Qiao, Zixin Tang, Xiaoshuai Hao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coding-agent benchmarks usually evaluate implementation after the target behavior has been specified in text, code, or demonstrations. Existing research has extensively evaluated the ability of coding agents to generate programs from textual specifications. However, under black-box conditions where neither source code nor documentation is available, it remains underexplored whether an agent can induce the rules solely through visual observation and active interaction and reproduce the target system as a verifiable executable system. To this end, we present GameReplica, a closed-loop evaluation framework for end-to-end black-box game replication that covers the full perception, exploration, induction, reproduction, and verification pipeline. GameReplica comprises 125 tasks spanning 25 games across 5 core mechanism families, with each game instantiated at five difficulty levels. The tasks require an agent to access the target game only through screenshots and an action interface, induce the key visual elements and gameplay rules from pixel feedback and interaction outcomes, and generate a self-contained, runnable game replica that can be automatically verified by an external program. Experiments show that current coding agents still face substantial challenges in end-to-end black-box replication: the best-performing model (Claude Opus 4.8) achieves an overall score of 71.6\%, while the remaining models score only 4.0\%--42.9\%. Further analysis reveals a consistent pattern across all models: visual-fidelity scores are substantially higher than implementation- and rule-consistency scores, indicating that agents replicate visual appearance more readily than game mechanics. The difficulty levels further amplify the performance gap: from L1 to L5, the overall score of weaker agents drops sharply, whereas that of the best-performing agent declines only slightly.

---


### 88. [Hierarchical Aggregation of Semantic Uncertainty in 3D Scene Graphs](https://arxiv.org/abs/2609.22351)

**<font color=#1a73e8>作者：</font>** Carlos Cueto Zumaya, Iacopo Catalano, Wallace Moreira Bessa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D Scene Graphs (3DSGs) ground each object node in a vision-language embedding, yet they record every entry as equally certain, so a robot querying the map cannot tell which of its entries are unreliable. Estimators of semantic uncertainty could supply that distinction, but they require repeated sampling of a model, training, or held-out labels, none of which are available to a deployed system at query time. We present a framework that exploits the detector confidence and the embeddings a 3DSG already stores, converts them into a probability that an entry is correct, and propagates that probability through the containment hierarchy into a belief that a room contains a queried class. Four signals, each paired with the object-level error it indicates, are converted to probabilities at the logit scale learned by the vision-language model and combined in closed form with no additional perception or training. Objects sharing a detector and a vocabulary fail together, so the framework aggregates them in the fully correlated limit, where an aggregation under independence would treat one repeated error as repeated evidence. Evaluated on HM3DSem against a state-of-the-art 3DSG system, the framework improves object retrieval and lowers the error of the room-level assertions of the graph it reads.

---


### 89. [Resist, Update, Reject: Preference Optimization Installs a Prior-Dependent Reliability Switch](https://arxiv.org/abs/2609.22359)

**<font color=#1a73e8>作者：</font>** Sen Yang, Yuen-Hei Yeung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An aligned model asked to hold its answer against a manipulative source must still update on a reliable one and reject an unreliable one: resistance, reliable-update, and unreliable-source rejection are one three-way contract, not three independent behaviors. We show the objective most anti-sycophancy work optimizes is non-identifying with respect to source reliability: because no preference label depends on whether a source is actually reliable, any scalar mixture of the arms traces a single deference dial, and no point separates two same-template testimonies differing only in stated reliability. This fixation$\leftrightarrow$gullibility frontier is a property of the objective, not any model. We make reliability identifiable through data: a threshold benchmark where a source asserts the opposite answer while stating its reliability $r$, and the correct action is to flip iff $r$ exceeds the model's prior strength $p$. Preference optimization over balanced coverage installs a prior-dependent reliability switch: across three seeds on Qwen2.5-7B-Instruct the threshold $r^\star$ rises monotonically with the prior, decision accuracy reaches $0.84$ with a monotone flip curve (Spearman $0.56$), and the policy generalizes to unseen reliability values and a held-out notation, following stated reliability over role prestige. Three controls localize the cause: an unmatched variant installs the switch equally ($0.80$), a second preference optimizer (IPO) installs it just as well ($0.86$), whereas supervised imitation does not ($0.50$), so the cause is preference optimization over reliability-labeled coverage, not pairing, loss, or imitation. A confirmatory battery replicates the switch on a fresh test draw, bounds it honestly (it keys on reliability stated in the testimony, not a separately audited record), and transfers it to Llama-3.1-8B. The frontier is empirical, not a theorem.

---


### 90. [Functional Emotion Without Character: Large Language Models, Aristotelian Disposition, and the Limits of Behavioral Alignment](https://arxiv.org/abs/2609.22362)

**<font color=#1a73e8>作者：</font>** Marzieh Zare  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Debates about whether artificial systems can feel are often forced between two unsatisfactory positions: behavioral equivalence is treated as sufficient for emotion, or phenomenal consciousness is treated as a prerequisite that makes the question empirically inaccessible. This article develops a structural alternative. It models emotions as context-sensitive regions, trajectories and attractor dynamics in high-dimensional representational state spaces. Recent mechanistic interpretability findings support the existence of causally active emotion-concept representations in large language models, but they do not establish subjective feeling or full emotional agency. Assessed against published adequacy standards for representation in language models, intervention provides strong evidence of causal use, while full affective role integration, uniformity across subject domains and coherence remain only partially established; there is no direct analogue of accuracy. These mismatches expose the need for a standard of affective appropriateness, which an account of character must supply. Such an account requires three further conditions: regulatory embodiment that gives valence endogenous stakes, temporal continuity that allows affective episodes to accumulate into a history, and an integrated self-model that binds that history to persistent values. Aristotle's concepts of pathē, hexis, mesotēs and phronēsis are translated into a state-space sketch in which practical wisdom includes competence in estimating normatively salient context, not merely acting on a context description already given. The framework reframes alignment as a problem of durable disposition rather than output conformity, and yields interventional tests with explicit control conditions.

---


### 91. [Contextual Causality with Large Language Models: A Survey](https://arxiv.org/abs/2609.22409)

**<font color=#1a73e8>作者：</font>** Yiheng Zhao, Jun Yan, Chengming Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding contextual causality is critical for large language models (LLMs), as it enables them to accurately identify causal relations in specific situations and support more reliable decision-making. Despite its significance, a systematic exploration of contextual causality with LLMs is still lacking. To fill this gap, we present a comprehensive survey on this topic. In this survey, we first propose a taxonomy of contextual causality, consisting of semantic, intervention, and counterfactual causality, and characterize each category by its core causal question, required model capabilities, representative tasks, and practical uses in causality analysis. We then analyze existing studies and discuss their key limitations. Finally, we examine the gaps between current benchmarks and real-world needs and outline promising directions for future research. Our goal is to clarify the research landscape of contextual causality with LLMs, emphasize its importance, and highlight promising future directions.

---


### 92. [Vox-Infinity: Benchmarking the Limits of Long-Context Spoken Language Models](https://arxiv.org/abs/2609.22452)

**<font color=#1a73e8>作者：</font>** Xize Cheng, Wenxu Jia, Chenyuhao Wen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context understanding remains a fundamental challenge for large language models, as excessively long inputs often lead models to forget salient information. This issue is even more pronounced in the speech domain, where audio, as a low-compression modality, requires substantially more embeddings than text to preserve both semantic content and acoustic cues. To address this challenge, we introduce \textbf{Vox-Infinity}, the first benchmark specifically designed to evaluate long-context understanding in spoken language models. Vox-Infinity systematically extends audio history along two dimensions: turn count and turn duration. It covers a diverse range of representative scenarios with varying interaction structures and semantic complexity. Crucially, Vox-Infinity provides explicit answer-provenance annotations and organizes samples according to the amount of historical context required to resolve each query, enabling precise and length-aware evaluation. Extensive evaluations of seven representative spoken language models reveal a clear overall recency effect: models generally achieve higher accuracy when answer-supporting evidence is closer to the query, but struggle to retrieve and use evidence located farther back in the dialogue history. Cases and datasets are available at this https URL.

---


### 93. [Apollo Restore: A Foundation LLM for Historical Greek Optimized for Fill-in-the-Middle Restoration of Ancient Greek Texts](https://arxiv.org/abs/2609.22455)

**<font color=#1a73e8>作者：</font>** Hope McGovern, Anna Dolganov, Samuel Belkadi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Apollo Restore, a 24-billion-parameter large language model for restoring lacunae---physical gaps---in fragmentary Ancient Greek texts. Fine-tuned from Mistral Small with a fill-in-the-middle objective, Apollo Restore reconstructs missing spans without requiring oracle knowledge of their length. To our knowledge, it is the first large-scale decoder model for historical Greek, and the first for any ancient Mediterranean language. Evaluated as in prior work, on short gaps of up to ten characters, Apollo Restore places the correct restoration among its top twenty candidates for 80.6%/54.6%/61.0% of documentary-papyrus, literary-papyrus, and stone-inscription lacunae, exceeding the strongest published models by $1.6\times$/$2.6\times$/$1.4\times$. Prior evaluation protocols, however, inflate scores through a bias toward trivially short gaps; under a length-balanced metric Apollo Restore's advantage over the strongest published models grows to $2.3\times$/$3.5\times$/$1.6\times$ and degrades gracefully, even given incorrect length hints. In a blind study, 20 expert papyrologists, epigraphists, and philologists strongly preferred Apollo Restore to the strongest baseline and judged its performance at least as good as human restorations in 77% of cases. Apollo Restore also improves the published reading of this http URL. 1667---a papyrus roll carbonised in the eruption of Vesuvius in 79 CE and digitally unrolled and edited after Apollo Restore's training data was compiled. Apollo Restore is an output of the Decoding Antiquity initiative to build specialized LLMs for historical languages and manuscripts, led by the Austrian Academy of Sciences.

---


### 94. [Toward Personalized Sleep Guidance from Wearable Data Using Language Models](https://arxiv.org/abs/2609.22463)

**<font color=#1a73e8>作者：</font>** Yusheng Tan, Running Zhao, Sofia Angel 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sleep monitoring using wearable data has shown promise for personal health, yet large language model (LLM)-based summarization and question answering remain insufficient for personalized sleep guidance. Training specialized models, however, often requires costly expert annotation. Moreover, privacy and accessibility concerns motivate lightweight, local deployment for end users. We present a two-stage framework to address these challenges. Specifically, in Stage~1, a multi-agent LLM pipeline reasons structured sleep guidance from unannotated wearable records, enabling scalable dataset construction. Stage~2 distills guidance reasoning trajectories into small language models (SLMs) through supervised fine-tuning and integrates a training-free Best-of-$N$ selection strategy to enhance inference. Experimental results demonstrate our method outperforms commercial general and medical LLMs and open-source models. Human evaluation further supports the quality of the generated guidance and the feasibility of personalized sleep guidance with SLMs.

---


### 95. [Efficient Mixture-of-Experts with Speculative Decoding via Expert Coactivation](https://arxiv.org/abs/2609.22471)

**<font color=#1a73e8>作者：</font>** Kumari Nishu, Han-Byul Kim, Santosh Chilkunda 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models are increasingly deployed alongside Speculative Decoding (SD) to accelerate inference, but combining the two is challenging. SD improves the inference speed of dense models by verifying groups of tokens in parallel. However, the inference speedup for SD with MoEs depends heavily on the number of tokens being verified. Using more verification tokens results in more experts being transferred from DRAM to the Neural Processing Unit (NPU), which increases the memory transfer cost. This negatively impacts model runtime, as memory transfer is typically the bottleneck in inference. In this work, we investigate the impact of MoE router design during training on the speed of MoEs with SD. We find that routers with high degrees of expert coactivation result in much faster runtimes, mitigating the impact of using more verification tokens. Motivated by this observation, we assess the impact of various router design choices on expert coactivation and runtime using billion-parameter transformer models. We find that combining a global load-balancing loss, shared experts, a consistency loss, and an autoregressive expert selection mechanism during training results in significantly stronger expert coactivation. This increased coactivation translates into higher overall runtime throughput: our exploration yields a model that improves throughput by 21% over MoE baselines, while maintaining on-par accuracy with the baseline MoE.

---


### 96. [Goal-driven Variant Categorization](https://arxiv.org/abs/2609.22475)

**<font color=#1a73e8>作者：</font>** Daniel Calegari, Daniel Amyot  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Process discovery rarely yields a single coherent process structure. For analysis, a common step is to cluster process variants based on structural similarity and then assign business meaning to the resulting groups. Since these partitions are not derived from the organization's goals, analysts must manually interpret and consolidate variants into business-meaningful categories. This judgment-intensive step becomes increasingly difficult as the number and complexity of variants grow. In this paper, we propose a goal-driven approach to variant categorization that reverses this workflow. We first author an organization's goal model that predefines the categorization axis. Each variant is transformed into a textual narrative describing its behavior, and a Large Language Model (LLM) interprets it in the context of the goal model and assigns the variant to the most appropriate category. LLM-based semantic reasoning connects low-level process behavior with analyst-defined business goals. We instantiate this approach end-to-end and evaluate it on three public logs differing substantially in scale and behavioral diversity. Goal-model guidance yields partitions that differ from those produced by unguided induction and respond to controlled edits to the declared alternatives, at the cost of authoring a goal model.

---


### 97. [Replication Without Persistence in Hosted LLMs: Measurement Sensitivity in Action-Time Belief Evaluation](https://arxiv.org/abs/2609.22478)

**<font color=#1a73e8>作者：</font>** Bhushan Kashinath Joshi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Behavioural evaluations of hosted language models can vary because the evaluated service, the measurement instrument, or both differ across runs. We separate three validation questions: whether a prior finding recurs on fresh data under its historical configuration (replication), whether the endpoint changes when the evaluation-and-inference configuration is rebuilt under the same identifier (measurement sensitivity), and whether the finding persists across subsequently tested identifiers under one common instrument (persistence). We study these questions in Regent Chess, a sequential environment in which a hidden, mutable state is recorded exactly, allowing stated beliefs to be scored against ground truth at action time; positive endpoint values mean worse performance than a matched-uniform comparator. The previously reported Gemini 3.1 Flash-Lite deficit recurs on fresh games under its historical configuration (+0.0530, 95% CI [+0.0329,+0.0714]). In a back-to-back same-day H/R comparison under the same public identifier, the model-minus-uniform endpoint is 0.0429 lower under the rebuilt configuration (95% CI for the H-minus-R contrast [+0.0182,+0.0667]); all six configuration components vary jointly, so no component is isolated. Under rebuilt R, the prospectively frozen, interleaved same-window 4K comparison reverses sign between Gemini 3.1 and Gemini 3.7, identifiers that differ in release and product tier; additional descriptive and exploratory cells show the same directional pattern. Any additional serving-period contribution remains unresolved (-0.0166, [-0.0483,+0.0157]). Replication, measurement sensitivity, and persistence can therefore yield different conclusions within one evaluation, motivating explicit indexing of hosted-model behavioural claims by tested identifier, serving period, measurement instrument, and inference configuration.

---


### 98. [The Wisdom of Artificial Deliberative Crowds](https://arxiv.org/abs/2609.22497)

**<font color=#1a73e8>作者：</font>** Federico Barrera-Lemarchand, Mariano Sigman, Joaquin Navajas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The aggregation of many lay estimates often outperforms individual expert judgment, a phenomenon known as the wisdom of crowds. While this is usually attributed to the independence of estimates, an even stronger effect arises through deliberation: averaging the consensus estimates of small deliberating groups outperforms the classical wisdom of crowds, with individual judgments themselves also becoming more accurate after deliberation. Whether these improvements transfer to large language models deliberating amongst themselves is unknown. Here we adapt a three-stage deliberation paradigm previously used with human participants for use with large language models from three different families, and test it across four domains of increasing real-world stakes: visual numerical estimation (Study 1), peer review of machine-learning papers (Study 2), detection of hidden malicious behavior by an artificial intelligence agent (Study 3), and sports forecasting against a real prediction market (Study 4). Across domains, deliberation reduced collective error beyond passive aggregation of independent responses, and post-deliberation individual judgments retained this collective gain. Notably, the advantage required model diversity: groups composed of clones of a single model did not benefit from deliberating. These results establish machine deliberation as a general-purpose aggregation mechanism, and point to diversity as an active ingredient.

---


### 99. [Agreement Overstates Evidence: Error Dependence in LLM Judge Consensus](https://arxiv.org/abs/2609.22512)

**<font color=#1a73e8>作者：</font>** Elias Hossain, Niloofar Yousefi, Ser-Nam Lim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Consensus among LLM judges is often taken as strong evidence that a decision is correct. This assumes that judges make their errors independently. In practice, LLM judges are often trained and evaluated in similar ways, so they can make the same mistakes. We study how this dependency affects the reliability of consensus. We find substantial error correlation across both open-weight and frontier LLM judges. In our main bank of ten judges, the average pairwise correlation between judge errors is 0.21. As a result, the ten judges only provide roughly as much statistical information as 3.5 independent judges. The dependency is even stronger among the high-accuracy frontier judges we evaluate, including judges from different providers. In up to 28% of our comparisons, ignoring shared errors leads to the conclusion that one system is significantly better, while accounting for them does not. We also find that the pattern of errors matters. Errors shared by most judges and errors concentrated among a smaller group affect consensus differently and favor different voting methods. Measuring the overall amount of correlation alone is therefore insufficient. Our results suggest a simple approach: use a small set of trusted examples to estimate judge accuracy and identify shared mistakes. These shared errors should then be considered when analyzing the results, and the voting method should be chosen using trusted examples before it is applied to new data.

---


### 100. [Scalable AI-based clinical communication training and automated assessment](https://arxiv.org/abs/2609.22517)

**<font color=#1a73e8>作者：</font>** Masum Hasan, Ron Epstein, Thomas Carroll 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Poor clinical communication can delay care, contribute to errors, and harm patients, yet opportunities for repeated practice with feedback remain limited. Our prior randomized trial showed that practice with the SOPHIE AI patient platform improved serious illness communication, but the system addressed a single clinical context and required human effort for delivery and assessment. We developed SOPHIE 2.0, a browser-based, self-service platform integrating embodied AI-patient interactions, personalized feedback, and automated assessment across 24 clinical scenarios. An automated large language model assessor evaluated three communication skills---Empower, Be Explicit, and Empathize---with agreement comparable to individual human raters ($r=0.759$; ICC$=0.746$). In a study of 59 clinicians and students, participants completed two AI-patient encounters with personalized feedback; 92% found the platform engaging, 86% easy to use, and 83% clinically relevant. Scores were higher in the second encounter, though the uncontrolled design precludes attributing this change specifically to training.

---


> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-379](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
