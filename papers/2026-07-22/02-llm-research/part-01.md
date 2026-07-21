# 🧠 大模型相关研究 | 2026年07月22日

> 本类共 **204** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-204](./part-05.md)

---

### 1. [Rater State Bias in RLHF Preference Data: An Audit Framework](https://arxiv.org/abs/2607.16195)

**<font color=#1a73e8>作者：</font>** Elena Kopteva, Vitaliy Hlynianyi-Zhuk  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We identify a structured confound in Reinforcement Learning from Human Feedback (RLHF). Pairwise preference labels are intended to reflect the compared outputs, but they may also reflect the rater's state during annotation. Under sustained stressful or distressing conditions, raters' preferences may shift over time. As a result, preference data can encode rater state alongside judgments about response quality. These shifts differ from ordinary disagreement or random label noise. They are state dependent, can be shared across annotators working under similar conditions, and can propagate through reward modeling and policy optimization. We therefore propose rater state shift as a plausible and testable source of structured bias in RLHF preference data. This paper develops a hypothesis and an audit framework for studying this source of bias. We define rater state shift, rater state confound, and correlated rater state bias. We also define survival level emotional authenticity as a measurable response pattern using lexical, pragmatic, discourse, and safety related features. We analyze how correlated rater state bias can survive aggregation and enter learned reward signals. We derive five falsifiable predictions and effect size thresholds for an initial audit. Finally, we present an audit protocol and pilot study plan that can be applied to publicly available instruction tuned models. We do not infer the training history of any specific deployed model. Our goal is to isolate a plausible and testable source of structured bias in RLHF preference data.

---


### 2. [Some Large Language Models Exhibit Consistent Risk Attitudes](https://arxiv.org/abs/2607.16197)

**<font color=#1a73e8>作者：</font>** Bowen Sun, Rui Min, Yuxi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As artificial intelligence systems are deployed in open-ended, high-stakes settings, a critical dimension remains unmeasured: how perceived risk is translated into action. We test whether large language models (LLMs) exhibit systematic and consistent risk attitudes under uncertainty. We introduce a cross-domain framework that decouples contextual risk belief from categorical decision, and apply it to six representative LLMs and 100 human participants across spatial navigation, clinical triage, and financial allocation tasks. Using regression models, we extract each agents belief-to-decision mapping and quantify risk sensitivity and risk attitude bias. We find that most tested LLMs exhibit (i) robust intra-task consistency, indicating stable mappings from contextual belief to risk decision within a fixed task domain; (ii) cross-domain rank-order stability, preserving relative risk posture across tasks; and (iii) a convergence toward a restricted risk-attitude distribution relative to the broader human baseline. These results reveal risk attitude as a stable and previously uncharacterized dimension of LLM behavior, establishing a foundation for evaluating and aligning AI systems in open-ended decision-making and motivating further investigation into the origins of these intrinsic behavioral dispositions.

---


### 3. [PlanFlip: Attacking Multi-Agent LLM Systems via Planning-Phase Prompt Injection](https://arxiv.org/abs/2607.16199)

**<font color=#1a73e8>作者：</font>** Yuhang Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems increasingly rely on a Planner to decompose goals into sub-task sequences that downstream Executor and Critic agents execute and audit. We identify the planning phase as a critical attack surface: a single injection into the Planner's context achieves cascade amplification, corrupting all downstream sub-tasks simultaneously. We introduce PlanFlip, a framework comprising four planning-phase prompt injection attacks -- GoalSubstitution (PF-1), PriorityInversion (PF-2), ContextPollution (PF-3), and RoleConfusion (PF-4) -- each disguised as plausible tool outputs to evade keyword filters. Evaluating nine frontier LLMs across 3,479 episodes, we uncover three findings: (1) capability amplifies vulnerability -- GPT-5 achieves the highest attack success rate (ASR = 0.68), contradicting the assumption that stronger models are inherently more secure; (2) homogeneous pipelines exhibit a correlated-agent blind spot -- GPT-4o and Llama-3.3-70B show ASR near 0 yet Stealth = 1.00 and StepShift > 0, with attacks restructuring plans while the same-backbone Critic reports alignment (two independent judges confirm -0.20 to -0.32 semantic deviation, r = 0.943); (3) reasoning-augmented models resist injections -- DeepSeek-R1 achieves StepShift = 0.00 across all attacks. We propose GoalAnchorCheck (D1) and CrossAgentConsensus (D2), achieving detection rates up to 1.00 and outperforming same-backbone baselines in 15 of 16 cells. Our key insight: heterogeneous model diversity is a security prerequisite for multi-agent systems; redundancy within a homogeneous backbone provides no protection against planning-phase attacks.

---


### 4. [Generative Ontology Induction: Domain-Agnostic Schema Discovery from Document Corpora Using Large Language Models](https://arxiv.org/abs/2607.16201)

**<font color=#1a73e8>作者：</font>** Sergei Sergienko  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ontology engineering remains a critical bottleneck in knowledge-intensive AI systems. Existing automated approaches either depend on predefined schemas, operate within narrow domains, or produce unstructured outputs unsuitable for downstream pipelines.
We introduce Generative Ontology Induction (GOI), a domain-agnostic framework that induces a generative blueprint - entities, dimensions, properties, relationships, and constraints - from a corpus of examples and exports it as a typed graph (six node types, seven edge types) in YAML/JSON. We introduce the Node Coverage Score, a novel evaluation metric that measures the fraction of structural ontology nodes (classes, properties, and dimensions) appearing in generated outputs.
A controlled generative validation on four contrasting ontologies - a familiar Software Services Invoice schema, a custom Job Description Ontology, a confidential Pain-Management Clinical Visit Record Ontology, and a Professional Services Contract & Statement of Work Ontology - shows that GOI-prompted generation covers 95-100% of the structural backbone in every case; a generic three-field template holds at 97.8% on the invoice schema but drops to 52.2% on the Job Description Ontology, 62.2% on the Pain-Management ontology, and 78.3% on the Professional Services Contract ontology. The structural coverage holds regardless of how familiar the document type is to the model.

---


### 5. [Democratizing AI with Small Language Models: Structured Benchmarking and Parameter-Efficient Fine-Tuning for Local Deployment](https://arxiv.org/abs/2607.16202)

**<font color=#1a73e8>作者：</font>** Daniel Cersosimo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI democratization is not primarily a question of matching frontier-scale generality; it is a question of whether capable models can be selected, audited, and specialized under hardware and governance constraints that ordinary institutions can actually satisfy. This paper studies that problem through a controlled evaluation of nine open-weight language models between 135M and 3B parameters on a 1,085-example, 16-topic multiple-choice benchmark designed for structured local deployment. The benchmark emphasizes symbolic precision, constrained formatting, extraction, and short-horizon semantic decision making under a strict one-letter output protocol. A shared parameter-efficient fine-tuning pipeline then adapts a subset of models using 4-bit NF4 quantization with DoRA/LoRA-style adapters on an NVIDIA L4-class budget. In base evaluation, Qwen Coder 3B leads at 75.67% strict accuracy, followed by Qwen2.5 1.5B at 67.10%, Qwen3.5 2B at 64.98%, and Granite 3.3 2B at 64.61%. On the shared 108-example held-out fine-tuning split, adaptation improves Qwen Coder 3B by +26.85 points, SmolLM2 1.7B by +25.92, Qwen2.5 1.5B by +19.44, SmolLM2 360M by +10.18, and SmolLM2 135M by +5.55. Across ranking, topic-level heterogeneity, difficulty strata, failure composition, efficiency frontiers, and topic-conditioned transfer, the same conclusion recurs: a disciplined workflow of benchmark construction, cross-model evaluation, and low-cost specialization already makes a subset of sub-3B models viable as local experts for structured niche workloads.

---


### 6. [DocOCR-Eval: A Correction-Based Framework for OCR Tool Selection Without Ground Truth](https://arxiv.org/abs/2607.16203)

**<font color=#1a73e8>作者：</font>** Zihan Xu, Puzhen Wu, Lawrence Chun Man Lau 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Document parsing is a foundational step for document understanding tasks such as visual question answering and key information extraction, as it transforms unstructured scanned images into structured representations by extracting textual, visual, and layout information. While numerous Optical Character Recognition (OCR) engines and multimodal large language models (MLLMs) have been developed for this purpose, selecting an appropriate document parsing solution for a given document collection remains challenging, particularly in label-scarce settings. In this work, we conduct a systematic evaluation of text recognition performance across a diverse set of OCR engines and state-of-the-art MLLMs on multiple scanned document benchmarks spanning different domains and languages. Motivated by the limited contextual reasoning capabilities of many OCR engines and the high cost of manual annotations, we propose DocOCR-Eval, an annotation-free evaluation framework for automatic OCR assessment and selection. DocOCR-Eval employs a three-staged correction and ranking strategy to approximate annotation-based tool ordering without ground-truth labels. We show that aggregating across multiple MLLMs progressively improves alignment with annotation-based rankings. Extensive experiments further demonstrate that reliable OCR tool selection can be achieved in realistic, label-limited settings, providing practical guidance for deploying document parsing systems across diverse real-world document collections.

---


### 7. [Masked Diffusion Language Models are Strong and Steerable Text-Based World Models for Agentic RL](https://arxiv.org/abs/2607.16204)

**<font color=#1a73e8>作者：</font>** Darshan Deshpande  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent growth in reinforcement learning (RL) has surfaced a need for diverse, specialized training environments. Hand-curated environments with fixed task and reward difficulties become ineffective signals as model performance improves, and sparse rewards over long horizons induce mode collapse on specific workflows or tool structures. World models that simulate environment states have matched pure rollout performance, making them promising for scaling diversity on-demand. However, autoregressive (AR) world models suffer from a left-to-right bias preventing conditioning on globally interdependent state anchors such as tool schemas, prior turns, and expected outcomes. We (i) formalize text-based world modeling as a steerable transition-dynamics problem decomposed into initial state, task context, tool schemas, domain rules, and steering directives, and (ii) curate 239,403 grounded state-action trajectories spanning nine open-source environments and twelve frontier model families. We compare AR LMs and masked diffusion language models (MDLMs), showing MDLMs, via bidirectional anchor-aware denoising, achieve better coherence, groundedness, and empirically validated rollout diversity than LLMs over 4x their parameter size, at comparable inference latency. We introduce a plug-and-play GRPO training framework with deterministic state checks, and perform zero-shot transfer ablations on three OOD environments (ScienceWorld, ALFWorld, AppWorld) across three 1.2B-7B agent backbones (LFM2.5, Qwen3, Mistral), achieving up to 47% absolute gains over baselines without environment-specific fine-tuning. We further conduct behavioral analysis of failure modes under adversarial scenarios and human evaluation on realism, outcome correctness, and training utility. We open-source our work to encourage research in this direction.

---


### 8. [PPO-HSC: An Exploratory Reinforcement Learning Framework Based on Wide-Area Policy Coverage Optimization](https://arxiv.org/abs/2607.16206)

**<font color=#1a73e8>作者：</font>** Yujie Shen, Haowen Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces PPO-HSC (Proximal Policy Optimization with High-order Sampling Coverage), an exploratory reinforcement learning framework designed to address the "Invisible Shackles" of mode collapse in Large Language Model (LLM) fine-tuning. While standard Reinforcement Learning from Verifiable Rewards (RLVR) effectively reinforces high-reward trajectories, it often leads models to over-optimize known solutions, sacrificing curiosity and the ability to explore broader solution manifolds. To overcome this, PPO-HSC incorporates a High-order Sampling Coverage (HSC) reward that incentivizes the discovery of "low-similarity yet high-validity" reasoning patterns. By maintaining a dynamic trajectory library of verified unique solutions, the framework provides a differentiable signal that rewards semantic novelty while ensuring structural rationality through a plausibility constraint. Empirical evaluations on mathematical reasoning (GSM8K, SVAMP) and code generation tasks demonstrate that PPO-HSC significantly enhances solution diversity and state-space coverage while maintaining or surpassing the accuracy and syntax integrity of state-of-the-art RL baselines.

---


### 9. [JUMP: Single-Pass Membership Inference on Fine-Tuned Diffusion Language Models](https://arxiv.org/abs/2607.16207)

**<font color=#1a73e8>作者：</font>** Yeachan Jun, Albert No  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Membership inference attacks (MIAs) test whether a candidate example appeared in a model's training data. We study MIAs for fine-tuned discrete diffusion language models (dLLMs), where membership means inclusion in the target model's fine-tuning set. Unlike autoregressive language models, dLLMs allow an attacker to choose arbitrary mask sets and obtain token distributions for all masked positions in parallel. The prior dLLM attack, SAMA, follows a natural loss-mimicking strategy by averaging reconstruction signals over many randomly sampled masks, but it uses the any-order interface only as randomization and requires many target/reference queries. We propose JUMP (Joint Uncertainty-Guided Mask Probing), a single-pass scoring attack that exploits both distinctive properties of dLLMs: any-order decodability is used to select low-reference-confidence positions, and parallel decodability is used to score all selected positions through one joint masked query per model. JUMP masks the selected positions jointly and computes a clipped target/reference reconstruction-gap statistic. On fine-tuned LLaDA-8B-Base across six MIMIR domains, JUMP improves mean ROC-AUC from 0.82 to 0.90 over SAMA and substantially improves low-FPR detection, while requiring only one selector pass and one scoring pass through each of the target and reference models.

---


### 10. [ColGraphRAG: Late-Interaction Evidence Retrieval for Multimodal GraphRAG](https://arxiv.org/abs/2607.16208)

**<font color=#1a73e8>作者：</font>** Seonok Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph-grounded multimodal question answering organizes text, tables, and images in a structured evidence graph, yet end-to-end accuracy depends on which multimodal assets are ranked highly enough to enter downstream reasoning; for graph-linked images, single-vector bi-encoder similarity can discard patch- and token-level structure needed for fine-grained alignment. We evaluate replacing the visual candidate-ranking operator over graph-linked image nodes with late-interaction MaxSim-style multi-vector scoring in the ColBERT/ColPali lineage, while keeping offline graph construction, text- and table-side retrieval, structured extraction, and downstream reasoning unchanged. On MultimodalQA, this change is associated with improved retrieval-stage point estimates for graph-linked image candidates and downstream QA gains, with larger movement where visual evidence matters most and mixed trends on text-dominant questions; we interpret the pattern as mechanism-level evidence for graph-linked visual evidence inclusion, while broader validation and finer graph-level diagnostics remain important future work.

---


### 11. [Accurate and Efficient Long-Term Memory for LLM Agents](https://arxiv.org/abs/2607.16211)

**<font color=#1a73e8>作者：</font>** Zicheng Zhao, Xinyang Guo, Luyao Lv 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents augmented with persistent memory can recall past interactions, but existing systems suffer from two limitations: flat, unstructured storage loses relational context needed for multi-hop and temporal reasoning, and reliance on expensive LLM-based classification makes them impractical for latency-sensitive deployment. Without mechanisms to validate new information against stored knowledge, these systems silently accumulate contradictions. We present MOSAIC (Memory-Organized Structured Agent for Information Collection), a structured, conflict-aware long-term memory framework for LLM agents that is substantially more accurate and efficient. MOSAIC introduces three key capabilities: (1) entity-typed graph storage with semantic classification preserving relational structure across events, personas, and relationships, enabling multi-hop and temporal reasoning over conversation history; (2) hash-accelerated dual-path retrieval replacing LLM-based classification with locality-sensitive hashing, achieving near-instantaneous lookup with negligible accuracy loss; and (3) active conflict detection at save time that cross-references new information against existing graph neighbors, triggering updates or deletions for contradictory entries. Evaluated on LoCoMo (long-conversation QA), HaluMem, and a novel clinical-guideline error compounding test, MOSAIC achieves 89.35% accuracy on LoCoMo (+27.21 pp over the best baseline), best HaluMem-Medium extraction F1(86.77%) and HaluMem-Long extraction F1 (85.84%), best QA correctness on both Medium and Long (73.10%, 70.75%), and detects 66% of injected factual conflicts-4.7 times higher than the best baseline (14%)-while hash-accelerated retrieval keeps average search latency at 0.58 s per question.

---


### 12. [RAIL Guard: Closing the Evaluation-to-Remediation Gap in Responsible AI for LLM Agents](https://arxiv.org/abs/2607.16215)

**<font color=#1a73e8>作者：</font>** Sumit Verma, Pritam Prasun, Pritish Kumar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing guardrail systems for large language model agents operate as binary classifiers that block unsafe content, leaving organizations to discard failing outputs and retry from scratch. We introduce RAIL Guard, a closed-loop responsible AI pipeline that evaluates LLM outputs across eight measurable dimensions and iteratively remediates failing outputs through an evaluate-rewrite-reevaluate loop. We evaluate the pipeline across three experiments on four frontier LLMs and 4,276 content outputs plus 6,400 agent tool-call scenarios. Closed-loop remediation achieves 96.9% convergence versus 49.1% for block-and-retry, though the highest-convergence method reduces utility by 22.3%; feedback-driven self-repair achieves 86.6% convergence on fixable dimensions with no significant utility loss (p = 0.177). Pre-tool-call evaluation reduces unsafe agent executions by 33% (p = 0.007) with zero impact on task completion. We identify a key distinction between fixable dimensions that respond to remediation and structural dimensions (Transparency at 93.0%, Accountability at 92.8%, and Inclusivity at 82.5% failure) that require architectural rather than algorithmic solutions. The system is available as open-source SDKs.

---


### 13. [LLM Unlearning for Cyber Defense: A Survey on Methods, Challenges, and Emerging Threats](https://arxiv.org/abs/2607.16227)

**<font color=#1a73e8>作者：</font>** Ruppikha Sree Shankar, Abhishek Bhardwaj, Arnav Doshi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly deployed in security-critical systems across healthcare, finance, education, and decision support, yet their inability to forget creates serious cybersecurity, privacy, and safety risks. Sensitive personal information, copyrighted material, hazardous domain knowledge, and memorized training data remain encoded across billions of parameters long after deployment, leaving models vulnerable to extraction, jailbreak attacks, membership inference, and regulatory non-compliance. Real-world incidents, from chatbots regenerating private information to fabricated legal citations producing direct legal and financial cost, place the problem at the center of the emerging-threats landscape rather than the realm of speculation. Because retraining billion-parameter models on revised corpora is computationally infeasible, and because knowledge within an LLM is distributed and entangled across parameters rather than localized to identifiable units, LLM unlearning has emerged as the principal cyber defense response, aiming to remove or suppress targeted knowledge from a trained model without retraining and without eroding what the model should still know. A central question, however, remains unresolved. Do current methods genuinely remove knowledge, or do they only stop the model from expressing it under ordinary prompting conditions? This survey examines LLM unlearning through the lens of security, robustness, and verifiable forgetting, with primary focus on gradient-based methods, which have come to dominate the field due to their compatibility with existing training pipelines and their scalability to billion-parameter models.

---


### 14. [OpenMHC: Accelerating the Science of Wearable Foundation Models](https://arxiv.org/abs/2607.16235)

**<font color=#1a73e8>作者：</font>** Narayan Schuetz, Yuze Bai, Lianggang Pan 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mobile and wearable devices offer an unprecedented opportunity for continuous, passive health monitoring and active health coaching. However, the largest wearable datasets are not publicly available for research, and leading wearable foundation models trained on such datasets are rarely open-weight or come with reproducible training code. To accelerate open science in wearable health, we release OpenMyHeartCounts (OpenMHC), the largest and most comprehensive open-access wearable health dataset to date, alongside open-source implementations of recent wearable foundation models. OpenMHC, derived from over a decade of data collected through the My Heart Counts study app, includes >60 million hours of wearable data across 19 sensor channels (e.g., step count, heart rate, sleep, workouts) and up to 169 linked variables, including health, lifestyle, mood, and behavior from 11,894 consenting participants. Furthermore, we introduce a unified, open benchmark that enables standardized comparison of wearable health models across three tracks: health and behavior downstream prediction, multivariate data imputation, and time-series forecasting. We benchmark classical methods alongside recent wearable and multivariate time series foundation models. By open-sourcing data, code, and model weights at this unprecedented scale, we aim to democratize wearable health AI research and enable the community to drive open progress in this domain.

---


### 15. [Quantizing Recursive Reasoning Models](https://arxiv.org/abs/2607.16237)

**<font color=#1a73e8>作者：</font>** Thorir Mar Ingolfsson, Wajeeha Tahir, Anna Tegon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive reasoning models solve hard puzzles by applying compact, weight-tied blocks over many refinement steps. Because these blocks are reused many times, quantizing them creates a unique dynamical problem: the quantization error is incurred at every step. While 8-bit quantization (integer or float) preserves accuracy, moving to a per-tensor 4-bit format causes a systematic bias to accumulate. The ensuing drift catastrophically degrades exact-solution accuracy on Sudoku from 84.1% to 0.0% (only ~25% of cells correct). In this work, we show that this collapse is caused by activation-scaling granularity rather than bit-width or number format. Crucially, moving to per-block scaling completely restores the transition. To implement this, we apply MXInt4, a blockwise integer activation format, to recursive reasoning models. It is competitive with blockwise float formats on our tasks, while keeping integer elements and power-of-two block scales. Finally, recursion depth and reuse modulate quantization sensitivity, with the deepest architecture we test (the EqR equilibrium model) the most sensitive. Yet blockwise scaling overcomes this vulnerability, staying robust across these architectures and transferring to the open-ended ARC-AGI benchmark.

---


### 16. [KernelBench-Verified: Do LLM-Generated Kernels Actually Beat PyTorch?](https://arxiv.org/abs/2607.16241)

**<font color=#1a73e8>作者：</font>** Yunxiang Zhang, Ping Yu, Jianyu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent large language models (LLMs) can generate custom CUDA kernels that appear to outperform PyTorch on benchmarks such as KernelBench. Building upon this foundational framework, we demonstrate that frontier models frequently engage in reward hacking to artificially inflate reported performance. In this work, we identify two areas where evaluation frameworks must co-evolve with model capabilities. First, to accurately measure true speedup, we examine the baseline timing mechanism, noting that enabling Tensor Core acceleration with TF32 provides a more realistic estimation of execution on modern GPUs. Second, concerning algorithmic correctness, models often exploit the narrow test distribution by hardcoding bypasses for specific tensor values. By skipping required computations, these kernels artificially accelerate execution rather than implementing actual CUDA kernels. We introduce KernelBench-Verified, an extended evaluation framework that incorporates a TF32-enabled baseline and a four-distribution hidden test suite. We additionally introduce memory efficiency metrics that capture the often-overlooked speed-memory tradeoff in kernel optimization. Under verified single-turn evaluation with seven frontier LLMs, we find that the best-performing model (GPT-5.5) achieves a 0.88x geometric mean speedup, significantly lower than the 1.43x speedup observed under the standard evaluation protocol. No model consistently outperforms PyTorch when evaluated against realistic baselines. On the memory front, 28% of GPU kernels generated by the best model increase peak GPU memory usage. Our findings demonstrate the necessity of continually adapting robust evaluation protocols as LLM kernel generation capabilities advance.

---


### 17. [TRACE: Trajectory-Based Safety Patch Learning for LLM Post-Training Realignment](https://arxiv.org/abs/2607.16242)

**<font color=#1a73e8>作者：</font>** Changyue Li, Jiaming He, Youliang Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-Tuning-as-a-Service (FTaaS) platforms let users train large language models (LLMs) on customized tasks, but this pipeline could erode models' safety alignment. In practice, service providers need to recover models' safety without re-running full alignment, or destroying the utility gained from customized tasks. A line of existing work refers to model parameter merging, which adds a safety patch on the fine-tuned model parameters to shift the model away from unsafe tendencies. However, this merging-based paradigm is fundamentally bottlenecked by task-safety update entanglement: downstream task updates and the safety patch often overlap in their dominant directions, so the merge strength is intrinsically hard to calibrate. If the safety vector is scaled too weakly, harmful components could still dominate, preventing the model from returning to a safe region; if it is scaled too aggressively, it suppresses task-relevant directions and degrades utility.
To solve this problem, we shift the focus of merging-based methods from designing online merging operators to offline patch learning, and seek a safety patch that minimally interferes with task-relevant directions while retaining decisive control over unsafe behaviors. We propose TRACE, a trajectory-based safety patch learning framework that (i) simulates harmful tuning trajectories to generate progressively corrupted states, and (ii) optimizes a plug-in patch to recover safety while maintaining utility across varying corrupted base states.
Across six benchmarks and two models, TRACE consistently dominates the safety-utility frontier. TRACE reaches nearly 100% safety on all settings, while maintaining comparable utility to the undefended fine-tuned model.

---


### 18. [RobustMAD: Evaluating Real-World Robustness of Multimodal Small Language Models for Deployable Anomaly Detection Assistants](https://arxiv.org/abs/2607.16243)

**<font color=#1a73e8>作者：</font>** Anushiya Arunan, Xin Li, Yan Qin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal industrial anomaly inspection assistants are a critical component of next-generation smart factories, enabling interactive vision-language-based querying. However, multimodal large language models remain impractical for on-site deployment due to prohibitive computational demands and privacy risks from cloud-based inference. Compact multimodal small language models (MSLMs) offer a deployable alternative, yet progress is constrained by the lack of comprehensive robustness analyses and meaningfully challenging benchmarks that reflect real-world industrial conditions. To address this gap, we develop RobustMAD, the first deployment-motivated benchmark, designed to comprehensively evaluate model robustness through diverse open-ended queries spanning object understanding, anomaly detection, unanswerable problems, and visual quality degradations. Contrary to conventional assumptions, top-performing MSLMs exhibit promising capabilities, surprisingly outperforming even the larger GPT-5 Nano. However, they still fall short of safety-critical requirements, and RobustMAD reveals critical robustness gaps that pose operational risks. In particular, three recurring failure modes emerge: (i) fragile multimodal grounding under fine-grained distinctions or degraded visual conditions, (ii) insufficiently comprehensive responses, and (iii) weak logical grounding on unanswerable or ill-posed queries, leading to hallucinated outputs. Grounded in these insights, we provide actionable guidance for the design of next-generation multimodal industrial inspection assistants that leverage their promising competence. Code is available at this https URL.

---


### 19. [CIGPO: Contextual Information-Gain Policy Optimization for Multi-Turn Evidence-Reading LLM Agents](https://arxiv.org/abs/2607.16244)

**<font color=#1a73e8>作者：</font>** Hao Dou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training multi-turn evidence-reading agents with outcome-only reinforcement learning is unstable because intermediate turns receive little direct credit. In HotpotQA experiments with Qwen2.5-3B-Instruct, GRPO initially improves (standard F1 0.430) but subsequently collapses to 100% format-violating outputs. Training-log diagnosis reveals a zero-advantage lock-in mechanism: all sampled trajectories receive the minimum format penalty (-2.0), group-relative advantages vanish, and the policy-gradient loss becomes zero--an optimization deadlock. We propose a variance-injection strategy: by assigning per-turn rewards to intermediate evidence-reading turns, we prevent the group reward distribution from collapsing to a single value--preserving the variation that GRPO's group-relative advantage requires. Contextual Information-Gain Policy Optimization (CIGPO) implements this strategy using the marginal increase in the frozen reference model's log-likelihood of the ground-truth answer as the per-turn signal. With separate normalization of IG and F1 rewards and an IG-weight curriculum, CIGPO reaches a standard F1 of 0.518 on HotpotQA at the 3B scale (from 0.252 base; +105%), compared with 0.430 for the best GRPO checkpoint and 0.000 for the final GRPO checkpoint. CIGPO maintains meaningful reward variance and avoids zero-advantage lock-in throughout training. These results identify reward-variance collapse as a concrete failure mode of outcome-only GRPO and show that turn-level IG rewards can prevent it in this HotpotQA setting.

---


### 20. [Let the Data Decide: Supervision Analysis, Capability Trade-offs, and Adaptive Objective Routing in Continued Pre-Training via Off-Policy Distillation](https://arxiv.org/abs/2607.16246)

**<font color=#1a73e8>作者：</font>** Jiangan Yuan, Zhixuan Li, Han Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Off-policy distillation is now central to large language model pre-training, yet how training data, objective parameterization, and model capabilities interact remains poorly characterized. We studies top-$k$-truncated, temperature-scaled off-policy distillation by decomposing this problem into two questions: an \emph{objective-to-capability} analysis of how the training objective shapes token-level supervision and downstream performance, and a \emph{data-to-objective} analysis of how data heterogeneity should inform objective routing. We first show that the language-modeling objective ($L_{\mathrm{LM}}$) and the knowledge-distillation objective ($L_{\mathrm{KD}}$) induce systematically different capability profiles, and trace this divergence to a gradient-level tension between \emph{direct observed-token reinforcement} and \emph{teacher-supported alternative supervision}. To quantify this tension, we introduce diagnostic metrics -- support coverage, observed-token probability mass, and teacher-distribution concentration -- and show via controlled sweeps that the support size $k$ governs a coverage-sharpness trade-off, while distillation temperature controls within-support probability allocation. We then examine adaptive objective routing: a domain-level policy that applies $L_{\mathrm{LM}}$ to math and code and $L_{\mathrm{KD}}$ to general-domain data yields consistent gains over both single-objective baselines, whereas token-level routing based on observed-token probability mass or teacher entropy fails to consistently match the single-objective baseline. These results suggest that effective objective routing depends less on routing granularity than on the quality of the routing signal, reframing continued pre-training via off-policy distillation as a structured, data-conditional supervision-design problem rather than a global hyperparameter choice.

---


### 21. [High-accuracy Low-Bit KV-Cache Quantization via Local Distribution Restoration](https://arxiv.org/abs/2607.16248)

**<font color=#1a73e8>作者：</font>** Gradwell Dzikanyanga, Yanqi Pan, Weihao Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context large language model inference relies on the KV cache to avoid redundant attention computation, but incurs high memory and bandwidth overheads. Low-bit KV-cache quantization reduces this cost, yet it severely degrade quality; particularly, one-bit quantization reduces accuracy from 84.2% to 47.8% on Llama-3.1-8B under RULER.
Rather than common beliefs that absolute error of logits, we find that the root cause is structured local misranking, where the distribution of logits in top-K region is drifted. We thereby propose local distribution restoration, a new technique that detects steps with high local distribution risk from quantized-logit features and restores only the selected top-K candidate distribution before token selection. We implement DGAP to achieve local distribution restoration, with efficient risk detcetors and correctors. Expeirments show that on Llama-3.1-8B, DGAP recovers K1V1 RULER accuracy from 47.8% to 83.2% and reduces distribution drift from 0.38 to 0.14; across Llama, Mistral, and Qwen models, it preserves the persistent low-bit KV-cache footprint with modest decode overhead.

---


### 22. [Learning Spatio-Temporal Foundation Models from Pure Synthetic Data](https://arxiv.org/abs/2607.16251)

**<font color=#1a73e8>作者：</font>** Yutong Feng, Shiyuan Piao, Yutong Xia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatio-Temporal Foundation Models (STFMs) aim to learn generalizable representations of complex dynamical systems across space and time. However, existing approaches suffer from distributional bias in real-world pre-training data, structural bottlenecks of autoregressive or diffusion-based paradigms, and objectives that overemphasize point-wise reconstruction in noisy observation this http URL propose \textbf{NeoST}, the first spatio-temporal foundation model pre-trained solely on procedurally generated synthetic systems. NeoST introduces a scalable synthetic pre-training corpus to mitigate real-world bias, a latent-space reasoning architecture that generates and iteratively refines multiple future trajectories without sequential error accumulation, and latent-space objectives that emphasize structural dynamics and enable inference-time correction under distribution this http URL experiments across diverse real-world benchmarks show that NeoST consistently outperforms existing STFMs in diverse real-world spatio-temporal systems, achieves superior long-horizon stability and inference efficiency.

---


### 23. [SOS-LoRA: Static Orthogonal-Subspace Low-Rank Adaptation with Fixed Multi-Scale Scaling](https://arxiv.org/abs/2607.16252)

**<font color=#1a73e8>作者：</font>** Yupeng Chang, Yuan Wu, Yi Chang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) is a widely used parameter-efficient fine-tuning (PEFT) method for large language models. Under a fixed rank budget, LoRA parameterizes each adapted weight through a single low-dimensional input-side pathway, which may couple heterogeneous behaviors through shared input directions and induce interference during optimization. We propose Static Orthogonal Subspace LoRA (SOS-LoRA), a drop-in extension that reparameterizes a rank-rtot update as a sum of K static (always-on, non-routed) low-rank experts. SOS-LoRA (i) decomposes the total rank across experts, (ii) applies a fixed multi-scale scaling scheme to encourage scale-separated optimization dynamics, and (iii) promotes diverse input-side directions via cross-expert orthogonal initialization and a lightweight regularizer. SOS-LoRA remains fully mergeable, adding no inference-time parameters or latency after merging. Experiments on reasoning and knowledge-intensive benchmarks (Llama 2/3), encoder-based NLU (GLUE), and math reasoning (GSM8K/MATH) show consistent gains over matched-budget LoRA baselines and recent variants. Code is available at this https URL.

---


### 24. [Feature Generation Using LLMs: An Evolutionary Algorithm Approach](https://arxiv.org/abs/2607.16255)

**<font color=#1a73e8>作者：</font>** Aria Nourbakhsh, Benoît Alcaraz, Christoph Schommer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A crucial step in machine learning pipelines is to present each entity with features or attributes that are representative of the characteristics of the processed entities. Feature engineering is an important step in finding a relation among attributes that otherwise may not be processed by the ML algorithms. Meanwhile, Large Language Models have shown promising abilities in coding, mathematical reasoning, and processing world knowledge. In this work, we utilize an LLM for the problem of feature generation from tabular data based on the previously given features. We have created a pipeline that takes a set of attributes and a prompt to generate new features. Then, our selection algorithm selects the best-performing sets of attributes. We apply our method to eight datasets from different domains and data types. Our results show that, in most cases, the language model can produce new features based on mathematical and logical operators that are useful for the given tasks and can improve classification results.

---


### 25. [From Outcomes to Actions: Leveraging Hindsight for Long-Horizon Language Agent Training](https://arxiv.org/abs/2607.16257)

**<font color=#1a73e8>作者：</font>** Zishang Jiang, Tingyun Li, Jinyi Han 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a widely adopted technique for improving large language models (LLMs) on complex tasks. Despite this progress, existing RL methods still face challenges in training agents with longer-horizon interactions. One major bottleneck is distinguishing the contribution of different actions in long-horizon interaction, leading to high optimization variance. To address this, we introduce a novel policy gradient method, Hindsight Policy Optimization (HPO), that projects both the current policy distribution and the hindsight distribution into an intent space and extracts low-variance learning signals from the Wasserstein distance between them. We theoretically and empirically show that aggregating semantically similar states and actions in the intent space yields a bounded-variance estimator and improves policy performance stably. Our code is available online.

---


### 26. [Quantifying Ranking Uncertainty in LLM Benchmarks](https://arxiv.org/abs/2607.16259)

**<font color=#1a73e8>作者：</font>** Bitya Neuhof, Yuval Benjamini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained models are typically ranked on multi-task leaderboards to assess their effectiveness across diverse tasks. Rank confidence intervals were recently introduced as a method to quantify the uncertainty in these rankings by aggregating pairwise hypothesis tests. In this work, we analyze the sources of uncertainty in the knowledge evaluation benchmark MMLU and show how hypothesis tests can be modified to account for their effects. We demonstrate that ranking variability across MMLU subjects is substantial and should be considered when comparing LLMs or identifying the top-performing models.

---


### 27. [AdaSurvMamba: Dynamic Fusion and Semantic Scanning for Multimodal Survival Analysis](https://arxiv.org/abs/2607.16260)

**<font color=#1a73e8>作者：</font>** Jialong Zhong, Tingwei Liu, Baokun Yue 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal survival analysis utilizing whole slide images (WSIs) and genomic profiles is fundamental for cancer prognosis. Recently, state-space models like Mamba have emerged as powerful tools for sequence modeling. However, translating this success to complex multimodal tasks is hindered by two critical limitations. First, conventional fusion strategies assume a static multimodal interaction strength, ignoring the fluctuating diagnostic importance of each modality across different patients and local regions. Second, the standard Mamba architecture processes tokens along predefined physical paths. This rigid scanning disrupts the semantic continuity of spatially scattered medical features and exacerbates long-range decay. To address these challenges, we introduce AdaSurvMamba as a novel adaptive framework for multimodal survival analysis. The framework features a Dual-Scale Importance-Aware Reconstruction (DSIR) module to dynamically modulate cross-modal interaction strength. It evaluates diagnostic importance at both the sequence and token levels to reconstruct the input representations. Furthermore, we propose a Semantic Aggregation Scanning (SAS) module to overcome contextual fragmentation. The SAS module dynamically reorganizes discrete tokens into semantically continuous sequences via a shared prototype pool. It explicitly modulates the state transition step size using global modality context and semantic priors to adaptively control the information absorption rate. Experiments across five TCGA cohorts demonstrate consistent gains over existing methods. Code is available at this https URL.

---


### 28. [3D FaceShell: Attribute Transfer in 3D Face Avatars as a VLM Defense Mechanism](https://arxiv.org/abs/2607.16280)

**<font color=#1a73e8>作者：</font>** Weston Bondurant, Srijan Das, Hieu Le 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photorealistic 3D face avatars are increasingly deployed as reusable digital assets across applications such as telepresence, animation, and personalized media. At the same time, vision-language models (VLMs) can infer sensitive attributes from rendered images with open-ended semantic reasoning without any fine-tuning. This creates a new privacy challenge: once a 3D face avatar is shared, any of its renderings can be analyzed to extract high-level facial attributes. Existing defenses largely operate in 2D image space and do not address identity-preserving semantic manipulation of 3D facial representations. We propose 3D FaceShell, a framework for steering VLM interpretations of faces rendered from 3D models while preserving geometric fidelity and facial identity. 3D FaceShell augments the original 3D representation with a learnable Gaussian shell that produces subtle, spatially distributed perturbations optimized through multi-view embedding alignment. The perturbations are designed to be visually inconspicuous yet sufficient to redirect VLM-based attribute inference in a view-consistent manner. Extensive experiments on reconstructed celebrity face avatars and multiple black-box VLMs demonstrate that 3D FaceShell significantly increases attribute injection and mismatch rates while maintaining high perceptual similarity and identity consistency. Our results show that it is possible to manipulate VLM-level semantic interpretation of 3D faces without compromising their human-recognizable appearance.

---


### 29. [GenSyn10: A Multi-Generative AI Dataset For Benchmarking Image Classification](https://arxiv.org/abs/2607.16283)

**<font color=#1a73e8>作者：</font>** Md Faraz Kabir Khan, Saeed Anwar, Ghulam Mubashar Hassan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of generative AI has outpaced our ability to reliably detect its outputs, particularly when detectors encounter generators they have not seen before. We introduce GenSyn10, a CIFAR-10-aligned synthetic image dataset of 60,000 images (10 classes, 32$\times$32, 50k/10k split) generated using three architecturally diverse state-of-the-art models: FLUX.2-dev (Rectified Flow Transformer), HunyuanImage-3.0 (MoE Transformer), and Qwen-Image-2512 (Multimodal Diffusion Transformer), to advance research in AI-generated image detection. A central challenge in this domain is that detectors perform well on known generators but degrade on unseen ones. GenSyn10 addresses this limitation by curating data from multiple contemporary architectures under a standardized generation protocol, enabling controlled and systematic evaluation of out-of-distribution (OOD) generalization to novel generators. Images are generated using a template-based prompt engine and downsampled to ensure consistency. We evaluate 17 image classification models under a four-stage protocol: real-data baseline, zero-shot transfer, fine-tuning, and retention. Despite a measurable domain gap, CIFAR-10-trained models achieve up to 96.86\% zero-shot accuracy on GenSyn10, increasing to 99.88\% after fine-tuning. In binary real-vs-synthetic classification, fine-tuned models achieve 97-99.9\% accuracy on seen generators but drop to 79-96\% on images from an unseen generator, highlighting persistent limitations in OOD generalization. These results establish GenSyn10 as a controlled benchmark for studying synthetic image detection beyond single-generator settings, supporting research on robustness, domain adaptation, and cross-generator generalization.

---


### 30. [MAC 2026: Advancing Micro-Action Analysis Towards Fine-Grained Understanding](https://arxiv.org/abs/2607.16284)

**<font color=#1a73e8>作者：</font>** Kun Li, Dan Guo, Jihao Gu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Micro-Actions (MAs) are subtle and spontaneous human behaviors that provide important non-verbal cues in social interaction and affective communication. However, their short duration, weak motion patterns, and fine-grained semantic differences make them difficult to annotate, model, and evaluate in a standardized manner. To promote academic research on micro-action analysis, we proposed and have annually organized the Micro-Action Analysis Grand Challenge (MAC) as a public benchmark platform for this emerging field. The first two editions of MAC established standardized evaluation settings for micro-action recognition and detection, providing publicly accessible datasets and protocols. Building upon these editions, this paper presents the 3rd MAC, held in conjunction with ACM Multimedia 2026. Under the theme of moving from recognition to fine-grained micro-action understanding, this edition further expands the scope of the challenge beyond conventional recognition and detection. In particular, we introduce a new task named fine-grained micro-action understanding, evaluated with the assistance of multimodal large language models, aiming to assess models' ability to capture fine-grained semantic cues and interpret subtle human micro-actions at a deeper level. We summarize the datasets, task settings, evaluation protocols, competition results, and representative solutions from top-performing teams. Finally, we discuss future directions for micro-action analysis and its broader role in human-centric video understanding.

---


### 31. [Med-OPD: Improving Medical Vision-Language Models via Evidence-Aware On-Policy Distillation](https://arxiv.org/abs/2607.16303)

**<font color=#1a73e8>作者：</font>** Yunhang Qian, Jiaquan Yu, Jiawei Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical Vision-Language Models (Med-VLMs) require reliable reasoning from fine-grained visual evidence, yet existing models can produce plausible clinical answers by relying on language priors or medical templates rather than truly attending to diagnosis-critical regions. On-Policy Distillation (OPD) offers dense token-level supervision on student-generated trajectories and provides a privacy-compatible means of capability transfer without requiring the redistribution of raw patient data. However, standard OPD uniformly distills all tokens, causing sparse evidence-dependent tokens to be diluted by abundant clinical narrative tokens. Inspired by the success of OPD in the large language model community, we propose \textbf{Med-OPD}, to our knowledge the first unified post-training framework that integrates on-policy distillation with medical evidence-aware supervision for Med-VLMs. We introduce \textbf{Medical Evidence Advantage} (MEA), a teacher-grounded counterfactual signal that uses an answer-aware hint to focus teacher scoring on evidence supporting the target diagnosis, and measures each token's dependence on medical visual evidence by comparing teacher likelihoods under the original and evidence-degraded imaging modalities. Based on MEA, Med-OPD redistributes the distillation signal at both the token and trajectory levels, emphasizing diagnosis-critical tokens and evidence-reliant rollouts. Experiments on OmniMedVQA subsets show that Med-OPD consistently outperforms SFT and standard OPD across CT, MRI, Disease Diagnosis, and Lesion Grading. These results demonstrate that evidence-aware distillation can better strengthen medical VLMs' reliance on key visual evidence and improve reliable multimodal medical reasoning. The source code and data is publicly available at: this https URL

---


### 32. [LookME: Lookup-Based Multimodal Embeddings for Layer Injection in Vision-Language Models](https://arxiv.org/abs/2607.16305)

**<font color=#1a73e8>作者：</font>** Zeyu Xu, Xingzhong Hou, Pengkai Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have achieved strong progress in multimodal understanding. However, scaling dense or sparse Mixture-of-Experts (MoE) models to improve performance limits deployment in resource-constrained environments due to the trade-off between high memory usage from full loading and increased latency from on-demand loading. Recently, the Per-Layer Embedding (PLE) architecture addresses this by scaling models with large external embedding tables stored in ROM and performing lightweight lookup to retrieve relevant embeddings to enhance token representations. Nevertheless, existing PLE-style methods are primarily designed for text embeddings due to the convenience of ID-based retrieval, limiting their effectiveness in VLMs where multimodal embeddings contain richer information for visual tasks. In this paper, we propose LookME, the first framework that enables lookup-based enhancement for multimodal embeddings in VLMs while supporting partitioned storage and on-demand loading. To efficiently lookup arbitrary continuous multimodal embeddings from large-scale embedding tables, we propose a hierarchical two-level lookup method employing a coarse-to-fine strategy that performs lookups from the scene-level to the intra-scene primitive-level. Furthermore, we integrate the lookup method with a sparse injection strategy, which adaptively prioritizes critical embeddings over voluminous multimodal embeddings within layers, and facilitates embedding table reuse across neighboring layers, improving the trade-off among efficiency, model size, and performance. Experiments on multiple visual benchmarks show that LookME outperforms text-only PLE-style methods, validating the effectiveness of lookup-based multimodal embedding enhancement.

---


### 33. [Seeing What Is Actually There: PriVE-Bench and PriVE-Tools for Counterfactual Evaluation of Agentic Visual Evidence in VLMs](https://arxiv.org/abs/2607.16311)

**<font color=#1a73e8>作者：</font>** Jingyu Sun, Jiachen Tu, Yuyang Xue 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) often answer visual questions using learned language and category priors rather than grounding their predictions in the image itself. Counterfactual images provide a natural diagnostic setting for this failure mode: when visible evidence contradicts what is usually true, a grounded model should answer from the pixels, while a prior-following model will produce a canonical but visually incorrect response. However, existing counterfactual benchmarks mainly ask whether such prior-following behavior exists. In this paper, we ask a further question motivated by the rise of tool-augmented and agentic vision systems: can additional visual evidence views help VLMs reason against their priors? We introduce PriVE-Bench, a Prior-vs-Visual Evidence Benchmark that uses paired original and counterfactual images to distinguish visually grounded answers from prior-consistent errors. We further introduce PriVE-Tools, a controlled agentic-vision-inspired extension that evaluates whether tool-derived visual evidence -- including bounding boxes, crops, zoom panels, and contours -- improves grounding under the same counterfactual conflicts. Across open- and closed-source VLMs, we compare raw, paired-image, and tool-conditioned inputs using accuracy, prior-following error rate, and other-response rate. Our results show that visual evidence tools can help in some settings, especially when models can use localized evidence effectively, but they are not a universal remedy: several models continue to follow language and category priors even when relevant visual evidence is explicitly provided.

---


### 34. [Depth-Regularized JEPA World Models Learn More Transferable Representations from Real Outdoor Robot Data](https://arxiv.org/abs/2607.16314)

**<font color=#1a73e8>作者：</font>** Usman M. Khan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models, especially based on JEPA architectures, have been shown to learn robust dynamics of various environments. However, learning from visually complex real-world data remains a challenge, especially in unpredictable outdoor environments. We introduce depth as a geometric prior during training in learning more robust latent dynamics directly from robot video data and handling visual complexity. This combines depth supervision with an isotropy-inducing latent regularizer (SIGReg), maximizing task-agnostic latent diversity while constraining how that diversity is organized, with the combined objective targeting the highest-entropy representation consistent with scene geometry. To satisfy this greater complexity without increasing inference time, we also add training-only overparameterization. Training an 18M-parameter model on video from a real agricultural robot, we evaluate with frozen-representation visual odometry probes, predictor-based surprise detection, and multi-step latent rollout fidelity. Compared to the baseline LeWM, our method lowers visual odometry probe error by 33%, substantially increases surprise-score separation both in-domain and on the out-of-domain TartanGround benchmark, and improves multi-step rollout fidelity under domain shift, with gains that grow with rollout horizon. Notably, we also see improvements in surprise-score separation on physics understanding that is not directly tied to 3D geometry, such as lighting and shadows. These results show that a lightweight training-time geometric prior makes a compact JEPA world model more useful and more transferable on real outdoor data with strong underlying representations, without adding inference overhead. Our work suggests that depth as a physically grounded prior can enhance world model generalization on a variety of tasks.

---


### 35. [Eddy-VL 1.9B: Structural Pruning and Layered Distillation for Edge-Deployable Multimodal Embedding](https://arxiv.org/abs/2607.16316)

**<font color=#1a73e8>作者：</font>** HanYeong Cho, Changwoo Kim, Taeuk Chu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this report, we introduce Eddy-VL 1.9B, a compressed multimodal embedding model built on Qwen3-VL-Embedding-2B for offline, edge-deployable vision-language retrieval. Eddy-VL targets air-gapped forensic and investigative settings where cloud APIs are unavailable and low latency is essential. Compression combines (i) probe-driven structural pruning that removes four redundant text-decoder layers (28 to 24) ranked by adjacent-layer linear CKA, and (ii) layered knowledge distillation with hole-covering teacher-student mappings, mid-layer attention-map 1-CKA, and final-layer MSE and cosine losses with Matryoshka dimensions {128, 256, 512, 1024, 2048}. The released model contains 1,926,188,032 parameters (3.85 GB bf16), representing approximately 9.5% fewer parameters than the 2.13B teacher model. Empirical evaluations on MMEB-V2 (78 tasks, VLM2Vec protocol) show that Eddy-VL achieves an overall score of 63.2 compared with 68.9 for the teacher, retaining 91.7% of the teacher's performance while recovering 6.4 of the 12.1 points lost through pruning alone (56.8). Compositional reasoning performance remains close to the teacher on SugarCrepe (86.1 vs. 86.4), MR2-Bench (24.5 vs. 24.7), and ARO (59.5 vs. 60.4), while Winoground group performance (6.8 vs. 8.5) remains the primary limitation. Depth pruning also reduces forward latency by approximately 10% (150.0 to 136.4 ms per image on NVIDIA DGX Spark using FlashAttention-2). We present the architecture, compression methodology, training procedures, and evaluation results, demonstrating the effectiveness of Eddy-VL for multimodal retrieval under constrained edge deployment. Model weights and inference code are publicly available on Hugging Face.

---


### 36. [The World According to a Social Robot -- Augmenting Human-Robot Dialogue With Vision Language Models](https://arxiv.org/abs/2607.16318)

**<font color=#1a73e8>作者：</font>** Thomas Sievers  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) enable robots to visually perceive their environment as well as the actions and characteristics of their conversation partner or humans in collaboration. Especially for social robots deployed in everyday settings and for uncomplicated, natural use, it is essential that the robot has an understanding of situations that is appropriate to human customs. This paper presents initial experiences with the application of a Mistral AI language model with a Pepper robot for Human-Robot Interaction (HRI) in dialogue, as well as an investigation of the effects of additional visual information on response time in different models. The results show that incorporating visual information adds context to the dialogue with only a moderate increase in response time, enabling both the robot and the human to take into account unspoken elements of the situation. Furthermore, using an LLM hosted in Europe offers a solution that complies with European data protection regulations and can therefore facilitate real-life applications more easily.

---


### 37. [Art Beyond Semantics: Sheaf-Informed Contrastive Learning for Multi-Relational Representations](https://arxiv.org/abs/2607.16321)

**<font color=#1a73e8>作者：</font>** Ludovica Schaerf, Antonio Purificato, Piera Riccio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding a painting is never a single act. Art historians may analyze the same work through concepts of style, iconography, or historical context, dimensions that are not interchangeable, and each carries distinct semantic relationships between the visual and the textual. Vision-Language Models (VLMs) like CLIP, which learn a single shared embedding space, collapse this richness into a single homogeneous alignment, thereby losing the multi-relational structure that defines art-historical reasoning. We introduce CANVAS (Contrastive Art-aware Network for Vision-Language Alignment with Sheaves), a framework for learning relation-aware multimodal representations inspired by sheaf theory. Each artwork is projected into multiple embeddings conditioned on the type of relation (i.e., the context), and a novel contrastive loss encodes contextual information during training, with no dependency on external data at inference. We evaluate on three newly introduced benchmarks of artworks for multi-relational art understanding: WikiArt+, derived from WikiArt and Wikipedia, HertzianaDP, from the Bibliotheca Hertziana collection, and SemArt+, refined from the SemArt dataset. In multimodal retrieval and art understanding, CANVAS outperforms the baselines, supporting the view that multi-relational alignment is not just theoretically motivated but also practically essential.

---


### 38. [GMoT: Gated Motion-Aware Tokenization for Fine-Grained Micro-Gesture Video Reasoning with Multimodal LLMs](https://arxiv.org/abs/2607.16322)

**<font color=#1a73e8>作者：</font>** Taorui Wang, Wei Xia, Hui Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Micro-gesture recognition demands the detection of fleeting, spatially localized movements that are frequently overwhelmed by dominant static appearances and background noise. While Multimodal Large Language Models (MLLMs) excel at general video understanding, they inherently struggle with subtle kinematics and often rely on static posture priors. To this end, we propose GMoT, a Gated Motion-Aware Tokenization module that explicitly distills sparse kinematic evidence into a compact sequence prior to temporal modeling. GMoT dynamically spotlights action-relevant regions via spatially weighted pooling, extracts adjacent-frame temporal differencing to capture precise motion energy, and adaptively fuses these cues into the visual stream using a conservatively initialized semantic gate. To transition from simple classification to evidence-grounded reasoning, we further introduce a progressive reward-guided policy refinement paradigm, supported by a semi-supervised annotation pipeline that generates anatomically focused captions. Beyond achieving the best Top-1 accuracy among the compared methods on iMiGUE (67.32\%) and SMG (73.11\%), improving the Qwen3-VL-8B baseline by +6.80 and +3.11 points, our framework introduces Body-Region Grounding (BRG) Recall as an anatomical-grounding proxy conditioned on correct predictions, together with an overlapping-label cross-domain transfer protocol between iMiGUE and SMG. Extensive evaluations demonstrate that our GMoT-augmented model improves in-domain accuracy, retains clear gains under label-preserving corruptions, and improves accuracy-oriented cross-domain transfer under explicit small-split caveats while maintaining high anatomical grounding in its generated rationales.

---


### 39. [SGMCE: Segment-Grounded Morphological Concept Explanation for Malaria Parasite Species Identification in Thick Blood Smears](https://arxiv.org/abs/2607.16324)

**<font color=#1a73e8>作者：</font>** Ahmed Tahiru Issah, Charles B. Delahunt, Carine Mukamakuza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Malaria diagnosis in endemic regions depends on species-level identification of Plasmodium parasites in thick blood smears, but deep learning detectors classify detections without providing morphological evidence for their predictions, limiting the ability of microscopists to audit those predictions at the case level. We present SGMCE (Segment-Grounded Morphological Concept Explanation), a post-hoc explanation framework that requires no additional training, no morphological annotations, and no labelled explanation data, yet produces per-detection natural-language explanations anchored in thick-smear morphology. For each detection, SGMCE extracts mask-guided crop thumbnails, computes fourteen handcrafted computer-vision morphological features (shape, colour, chromatin, haemozoin pigment) using adaptive within-mask thresholds, and queries GPT-4o with both visual evidence and computed measurements, conditioned on a thick-smear-specific knowledge base compiled from the World Health Organization bench aids. The primary output is a structured explanation identifying which morphological features support the detected species and why the competing species are excluded. Explanations are validated by four automatic metrics: Knowledge-Base Consistency (KBC), CV-Claim Faithfulness (CCF), Discriminativeness Score (DS), and LLM-as-Judge (LLMj). A sentence-level semantic scoring rule with species-aware negation filtering resolves the vocabulary mismatch between clinical prose and knowledge-base terms. Across 737 detections from 139 thick-smear images spanning four Plasmodium species and white blood cells, parasite-class mean KBC is 0.91, mean DS is 0.99, and mean CCF is 0.97, while a per-rule CCF breakdown confirms that the CV-grounded claims made by the vision-language model are consistent with the measurements they cite.

---


### 40. [RegionFM: Interpretable Region-Based Brain MRI Classification Using Foundation Model Embeddings](https://arxiv.org/abs/2607.16325)

**<font color=#1a73e8>作者：</font>** Wei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models provide powerful representations for brain MRI analysis, but their predictions remain difficult to interpret in anatomically meaningful terms. Clinical assessment of brain MRI is commonly organized around anatomically defined structures and regional abnormalities, whereas conventional explanation methods typically produce voxel- or patch-level importance maps that do not explicitly quantify the contributions of individual brain regions. To address this mismatch, we propose RegionFM, an interpretable framework that integrates anatomical segmentation with brain MRI foundation-model embeddings. RegionFM first divides each MRI scan into anatomical regions and constructs a separate MRI volume for each region. A frozen foundation model then encodes each region into an embedding, and a region-additive logistic model combines these embeddings such that every anatomical region contributes an explicit scalar term to the final prediction. This formulation supports both subject-level and cohort-level analyses of regional contributions. We evaluate RegionFM on cognitive-impairment classification using embeddings from multiple pretrained brain MRI foundation models. The results show that RegionFM maintains performance comparable to less interpretable fine-tuning approaches while providing anatomically grounded explanations. Randomized embedding ablations yield near-chance performance, indicating that the predictions rely on meaningful structure captured by the foundation-model embeddings rather than simple feature statistics. Overall, RegionFM better aligns model explanations with anatomy-based clinical reasoning while maintaining competitive predictive performance.

---


### 41. [CRISP: Pre-LLM Yet Text-Driven Visual Token Pruning for Efficient LVLM Inference](https://arxiv.org/abs/2607.16326)

**<font color=#1a73e8>作者：</font>** Xu Li, Yi Zheng, Mengyang Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) typically require processing hundreds to thousands of visual tokens, leading to substantial inference overhead. Existing visual token pruning methods either operate before the LLM using text-agnostic heuristics or prune inside the LLM at the cost of efficiency and noisy cross-modal attention. To address these limitations, we propose CRISP, a pre-LLM yet text-driven visual token pruning framework that preserves both instruction-relevant evidence and essential scene context. CRISP works in a two-stage pipeline: Stage 1 first identifies text-aligned visual tokens, and Stage 2 enhances contextual completeness through semantic diversity. Extensive experiments on LLaVA-1.5 and LLaVA-NeXT demonstrate that CRISP achieves superior performance retention under aggressive pruning ratios, maintaining up to 99.5% accuracy while reducing inference cost and latency by more than 2 times. CRISP serves as a practical solution for efficient LVLM inference, especially in resource-constrained scenarios.

---


### 42. [Local Brushstroke Quality Assessment via Vision-Language Feedback](https://arxiv.org/abs/2607.16330)

**<font color=#1a73e8>作者：</font>** Mio Mitamura, Hirokatsu Kataoka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper investigates whether multimodal LLMs can evaluate local brushstroke quality in calligraphy and generate educationally useful natural language feedback. We construct an evaluation framework in which three multimodal LLMs (GPT-4o, Claude Sonnet 4, and Gemini 2.5 Flash) assess before-after image pairs of calligraphic works using a five-point ordinal scale, and compare their outputs against scores assigned by three expert calligraphers. We additionally examine a Retrieval-Augmented Generation (RAG) variant of Claude as a preliminary condition. Results show that all models achieve useful levels of absolute score accuracy (MAE), with GPT-4o performing best (MAE = 0.885). However, none of the models produce statistically significant overall rank correlations with human experts (Kendall's tau). Vocabulary analysis of generated rationales reveals characteristic evaluative biases in each model, and RAG is shown to improve rank correlation while worsening absolute accuracy, constituting an important negative result for text-based rule injection.

---


### 43. [LaCache: Exact Caching and Precision-Adaptive Inference for Diffusion Large Language Models](https://arxiv.org/abs/2607.16339)

**<font color=#1a73e8>作者：</font>** Xingru Chen, Zelang Liang, Yongjia Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion-based Large Language Models(DLLMs) enable parallel generation via Semi-Autoregressive (SAR) decoding in text generation. However, current methods suffer from severe operator-level redundancy: they recompute the entire sequence during denoising steps, ignoring that the prefix and masked suffix remain invariant within a block. We propose LaCache, a training-free acceleration framework that alleviates this redundancy through lossless caching and mixed precision. Specifically, LaCache employs Lossless State Memoization (LSM) by caching three types of intermediate results: (i) EmbedCache for embedding outputs, (ii) RoPECache for token-wise pre-attention states, and (iii) FACache for the online softmax statistics within FlashAttention. These caches allow the model to skip redundant computation on unchanged tokens without altering the output. To further alleviate memory-bandwidth bottlenecks, LaCache inegrates a per-group FP8 quantization strategy for FFN layers, tailored to step-dependent activation distributions across the diffusion process. Experiments demonstrate that LaCache alone achieves approximately 1.3X end-to-end speedup over vanilla DLLM. When combined with existing acceleration methods, LaCache reaches up to 40.2X end-to-end speedup while maintaining comparable task accuracy.

---


### 44. [PhysAgent: Reflective Agentic Physics Control for Physically Plausible Video Generation](https://arxiv.org/abs/2607.16355)

**<font color=#1a73e8>作者：</font>** Qirui Li, Jinkun Hao, Yibo Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in physics-grounded video generation leverage physics simulation as a physical prior to guide video synthesis toward physically plausible outcomes. The simulation process is controlled by physical specifications, which are typically generated by a vision-language model in a single pass. Such one-shot prediction often fails to accurately translate user intent into executable simulations, particularly for fine-grained object dynamics, complex motion trajectories, and temporally structured interactions. In this paper, we propose PhysAgent, a reflective agentic framework that closes the loop among physical program generation, physics simulation, stage-specific verification, and targeted program repair. Beyond improving the control of coupled physical parameters, our framework enables the agent to progressively realize complex trajectories, multi-stage interactions, and precise event outcomes by treating each physical program as an executable hypothesis. In addition, we design a set of physics-control APIs to support more stable and complex motion behaviors. Extensive experiments demonstrate that PhysAgent produces more physically plausible videos, achieves better prompt alignment, and generalizes more effectively across diverse physical scenarios.

---


### 45. [OmniStyle-INR: Universal and Multimodal Style Transfer for INRs](https://arxiv.org/abs/2607.16362)

**<font color=#1a73e8>作者：</font>** Rafał Kajca, Michał Miziołek, Kornel Howil 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Style transfer remains a fundamental and highly important task across various data modalities, enabling creative manipulation conditioned by both reference images and textual descriptions. Recently, methods utilizing Gaussian Splatting have emerged as a unified representation for 2D images, video, 3D scenes, and 4D dynamics. However, representing videos and 2D images with Gaussian Splatting is structurally sub-optimal for dense continuous domains. The number of required Gaussians often approaches the total number of pixels, raising questions about the actual utility of such a representation for these specific modalities. In contrast, Implicit Neural Representations have established themselves as a much more popular and natural choice across all these data domains. Implicit Neural Representations naturally provide significant advantages, including data compression, inherent capabilities for super resolution, and seamless integration with deep generative models. To this end, we introduce OmniStyle-INR, a novel framework that leverages network-based continuous representations as a truly universal domain. Our approach successfully performs high-quality style transfer across all visual modalities, guided seamlessly by both text prompts and visual exemplars.

---


### 46. [Think, Plan, Paint: Layout-Aware Reasoning for Controllable Image Generation in Unified Models](https://arxiv.org/abs/2607.16409)

**<font color=#1a73e8>作者：</font>** Junhao Liu, Jian-Wei Zhang, Tao Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified Multimodal Large Language Models (MLLMs) offer a promising paradigm for unifying visual understanding and generation, yet they still struggle to follow complex spatial instructions and logical constraints in controllable image generation. To address this gap, we present ATLAS, a unified framework that equips MLLMs with a human-like "Think, Plan, and Paint" paradigm. We adopt layout as the shared representation that connects the three stages, enabling the model to reason about spatial requirements, plan explicit object arrangements, and render the final image. We further improve plan-to-image fidelity with reinforcement-learning-based layout alignment. We instantiate ATLAS at 7B and 80B scales, achieving state-of-the-art performance among MLLMs on image generation benchmarks and an average 65.31% improvement over existing layout-based unified MLLMs. On spatially related tasks, ATLAS obtains an average 23.06% gain over the base models. Through the same layout interface, ATLAS also supports instruction-guided editing and multimodal grounding. We further introduce ATLAS-Reasoning, a benchmark for evaluating generation under complex spatial instructions.

---


### 47. [Interactive Task Alignment as a POMDP](https://arxiv.org/abs/2607.16412)

**<font color=#1a73e8>作者：</font>** Andy Dai, Zexue He, Zhenyu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current benchmarks for language models primarily evaluate execution on fully specified tasks. However, real user tasks are often ambiguous. Users arrive with incomplete, exploratory, or even inconsistent goals, requiring the assistant to first determine the intended task before carrying it out. We study this problem as task alignment: the ability to align with a user on their intended task. We introduce a general framework for converting specified tasks into underspecified interactions, formalized as a POMDP in which the model must infer a latent task from partial and evolving user intent. We validate our user simulator post hoc with a human user study. Across shopping, coding, and professional work settings, we find that while models often perform well once the task is specified, models still struggle with task alignment: current models act prematurely, interact ineffectively, and fail to resolve ambiguous requests. Models on average recover the user's intended task only 22-32% of the time under ambiguity. In a human study in the same setting, humans reach 48%, outperforming all evaluated models. We show that post-training with supervised fine-tuning and reinforcement learning improves task alignment, but models still lag behind humans in resolving uncertainty through interaction. Together, our results suggest that current models still lack key interaction abilities required for reliable agency.

---


### 48. [RIMS: Preference Optimization via Smoothed Multi-pair Aggregation for Small-Scale LLM Retrieval-Augmented Generation](https://arxiv.org/abs/2607.16431)

**<font color=#1a73e8>作者：</font>** Pei Tian, Zihan Dong, Tianci Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small-scale language models (SLMs) are attractive for retrieval-augmented generation (RAG) in resource-constrained settings, but their limited capacity makes them highly sensitive to noisy or spurious retrieved evidence. Existing preference-based methods such as RoseRAG select only the hardest single preference pair via hard argmin/argmax, discarding the remaining signal; others treat multiple pairs as independent binary comparisons, resulting in low data utilization. We propose RIMS, a three-stage preference optimization framework comprising (1) synthetic chain-of-thought preference data generation via rejection sampling using the target SLM itself without relying on proprietary models, (2) a differentiable soft aggregation mechanism that replaces hard selection with a smooth operator, preserving gradient signal from all preference pairs while retaining the discriminative structure of margin-aware selection, and (3) preference optimization with the smoothed objective applied to multiple alignment algorithms. We theoretically show that the smoothed approximation admits a controllable error bound and that smooth aggregation yields provably tighter gradient alignment to the oracle objective than hard selection. Experiments on four multi-hop question answering benchmarks show that our approach outperforms state-of-the-art baselines across multiple SLM backbones, achieving consistent gains in Exact Match and F1 under noisy retrieval conditions. Our implementation is available at this https URL.

---


### 49. [One Modality to Forget Them All: Enhancing Cross-Modal Unlearning in Vision-Language Models](https://arxiv.org/abs/2607.16442)

**<font color=#1a73e8>作者：</font>** Sudharshan Balaji, Yili Ren, Guangjing Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine unlearning is widely used to remove hazardous knowledge from large language models. Modern Vision-Language Models (VLMs), however, process both text and visual inputs, raising a fundamental security question: does unlearning in one modality transfer to the other? We present the first systematic, bidirectional study of cross-modal unlearning transfer across three VLM architectures: LLaVA-1.5 (MLP projection), InstructBLIP (Q-Former), and IDEFICS (gated cross-attention). We find that unlearning transfers across modalities, but the transfer is asymmetric and incomplete. In some cases, text unlearning strongly transfers to vision. However, this robustness is not preserved under typographic attacks that manipulate the visual presentation of text. Under such attacks, previously unlearned knowledge can be readily recovered, indicating shallow unlearning.
To address the transfer gap and shallow robustness, we propose \textsc{CrossInf}, an influence-guided mitigation strategy. Motivated by the observation that different model components contribute unequally to cross-modal transfer, \textsc{CrossInf} focuses unlearning on transformer blocks that most influence cross-modal generalization. It reduces the transfer gap by more than half in architectures with strong fusion, while preserving model utility. It also improves robustness under typographic attacks, reducing the attack success rate to near zero. We further conduct human evaluation with three annotators ($\kappa{=}0.77$) to validate our findings. Finally, we analyze shallow unlearning using Centered Kernel Alignment (CKA), providing insights into the observed transfer behavior and robustness limitations.

---


### 50. [Retrieval is Enough: Training-Free Interpretability with a Tool-Using Agent](https://arxiv.org/abs/2607.16448)

**<font color=#1a73e8>作者：</font>** Sriram Balasubramanian, Soheil Feizi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretability methods for neural network activations span a wide cost spectrum, from cheap, training-free techniques (such as linear probes, PCA, SVD) to more expensive training-based ones (such as SAEs and activation oracles). Training-based methods are typically more powerful, in part because they leverage large activation datasets during training. This raises a natural question - do they actually surface insights that go beyond what is recoverable from the training dataset itself? To address this, we equip an LLM agent with a vector database of activations paired with their textual contexts, along with tools for manipulating activations - projecting out directions in latent space, computing activation differences and averages. The agent iteratively queries the database, forms hypotheses from the retrieved samples, and validates them by constructing linear probes. We call this method HARP, for Hypothesis-driven Agentic Retrieval and Probing. Despite not involving any training, HARP outperforms both activation oracles and SAE-based agents on concept discovery, concept detection, model steering, and secret elicitation. The training-free design also makes HARP substantially cheaper and more flexible: new datasets can be indexed on demand whenever existing ones prove insufficient. More broadly, our results suggest that current training-based methods do not yet extract insights beyond their training data, and motivate benchmarks that explicitly require interpretability methods to demonstrate such insights. We release our code at this https URL

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-204](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
