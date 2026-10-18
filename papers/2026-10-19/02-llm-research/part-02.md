# 🧠 大模型相关研究 | 2026年10月19日

> 本类共 **321** 篇论文：已确认 **300** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-321](./part-07.md)

---

### 51. [Same Context, Different Agents: A Behavioral Study of Semantic Layers, Orchestration and Compaction in Data Agents](https://arxiv.org/abs/2610.20959)

**<font color=#1a73e8>作者：</font>** Zhivar Sourati, Marianne Menglin Liu, Zheng Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Answering questions over heterogeneous data means combining evidence from files, databases, documents and the web. Data agents automate this, but their success depends on context. Three context-engineering techniques (CETs) help by shaping it: semantic layers describe the data, orchestration splits work among agents, and compaction condenses interaction history. Existing studies validate each CET alone, leaving open how agent behavior shapes its effect. We present a comprehensive analysis of the three CETs, alone and combined, with seven large language models (LLMs) on 1,514 long-horizon tasks from five benchmarks, covering behavior, accuracy and cost. We find that data agents without CETs form three behavior groups: investigators, premature answerers that answer without inspecting data, and early stoppers that give up. Each CET delivers its known benefit, from more investigation to smaller prompts, but only the behavior group it matches turns that benefit into accuracy, such as premature answerers under orchestration. For investigators, the same CETs can hurt: the semantic layer stops them from looking, orchestration makes them overconfident, costing 5 percentage points, and compaction makes them repeat steps. Combining CETs yields smaller gains and losses than their sum. We derive guidance for choosing CETs by agent behavior, task demands and accuracy-cost trade-offs.

---


### 52. [PAGE404: Breaking GPU Isolation Through Hardware-assisted Page Migration](https://arxiv.org/abs/2610.20962)

**<font color=#1a73e8>作者：</font>** Ravan Nazaraliyev, Yicheng Zhang, Nael Abu-Ghazaleh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> NVIDIA's Grace Hopper (GH200) superchip represents a new generation of heterogeneous computing, tightly integrating a 72-core Arm-based CPU with a Hopper GPU on a single module via a high-bandwidth, cache-coherent interconnect. By eliminating the conventional PCIe bottleneck for CPU-GPU data movement, this design establishes a unified memory domain that scales to the capacities demanded by generative AI and high-performance computing (HPC) workloads. The architecture also introduces hardware-assisted page migration: driven by access counters, the system dynamically promotes frequently accessed pages from host CPU memory to GPU DRAM to improve memory locality. We study the security of this emerging architecture against new side- and covert-channel attacks targeting its page migration support. We analyze counter-driven migration across both the hardware mechanisms and the UVM driver's interrupt-handling pipeline, and identify two side-channel vulnerabilities: one rooted in the shared structure of access counters, and the other in the driver's response to migration interrupts. We further show that both channels are exploitable across Multi-Instance GPU (MIG) partitions, a feature intended to provide strong, hardware-enforced isolation between co-located tenants. Using proof-of-concept attacks, we build covert channels that reach roughly 8,500 bits per second through eviction-based signaling and 8,100 bits per second through migration-delay-based signaling across MIG instances. The interrupt-based channel also fingerprints inference workloads across distinct large language models (LLMs) and CPU SPEC2017 benchmarks, and estimates the prompt length processed during LLM inference with high accuracy. These results expose a security gap in hardware-managed heterogeneous memory systems and call into question the isolation guarantees of current MIG-enabled multi-tenant GPU deployments.

---


### 53. [VELD-QA: A Large-Scale Dataset for Visual Evidence Grounding and Question Answering in Long Documents](https://arxiv.org/abs/2610.20964)

**<font color=#1a73e8>作者：</font>** Zhivar Sourati, Marianne Menglin Liu, Rongguang Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing long-document QA benchmarks rarely combine large-scale human-authored questions with detailed visual evidence annotations, limiting diagnosis of evidence localization and interpretation failures. We present VELD-QA, a large-scale benchmark for Visual Evidence grounding and question answering in Long Documents. It contains 15,000 fully human-authored question-answer pairs across 5,859 real-world PDFs totaling 372,445 pages, balancing chart, table, and complex-layout tasks. Human annotations identify supporting pages and evidence elements and describe cited visual content, enabling separate retrieval and interpretation evaluation. We evaluate nine vision-language models under four evidence settings and seven retrieval-augmented and agentic systems. Our analysis identifies bottlenecks in evidence localization and interpretation. Retrieval-based methods substantially underperform the oracle setting with ground-truth supporting pages; full-document access does not close the gap. Localization alone is insufficient: oracle accuracy peaks at 81.7%, highlighting persistent visual interpretation and reasoning challenges. Enriching inputs with our visual-element annotations narrows the performance gap by 17-24%, demonstrating value beyond evaluation and motivating data enrichment for multimodal document QA. Our code is available at this https URL.

---


### 54. [MSP: Modality Self-Play for Training Multimodal LLMs Without Paired Cross-Modal Data](https://arxiv.org/abs/2610.20965)

**<font color=#1a73e8>作者：</font>** Robert Moseley, Md Kaykobad Reza, Ameya Patil 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large multimodal models have achieved remarkable progress by scaling model capacity and training on massive paired multimodal data. However, this paradigm introduces a fundamental bottleneck: aligned multimodal datasets are expensive to curate, difficult to scale across diverse modality combinations, and increasingly constrain further progress. We introduce Modality Self-Play (MSP), a training framework for multimodal foundation models based on proxy-mediated modality composition. Instead of relying on paired cross-modal data, MSP uses anchor-supporting proxy textual descriptions of unseen modalities as semantic bridges during training. Given an observed modality (e.g., image or audio), the model generates proxy descriptions for complementary unseen modalities, which are then encoded and aligned with the observed modality through learned bridges, enabling cross-modal interaction without real paired non-text supervision.
Our central hypothesis is that proxy text, combined with contrastively trained pretrained encoders, provides sufficient semantic structure for multimodal composition to emerge. We show that MSP enables zero-shot modality composition: models trained only with a real anchor modality and accompanying proxy descriptions can integrate and reason over multiple modalities at inference time despite never observing real paired non-text data during training. Empirically, MSP achieves state-of-the-art or competitive performance on multiple multimodal benchmarks. Ablation studies further demonstrate that learned bridges improve alignment, while anchor-supporting proxy descriptions enable effective cross-modal composition. MSP removes the need for real paired non-text (e.g., audio-vision) supervision, while continuing to rely on modality-text pairs, pretrained contrastive encoders, and modality-distribution bridge calibration.

---


### 55. [How to Train Your Little Dragon: Teaching a Small Language Model to Construct and Refine GPU Optimization Scripts](https://arxiv.org/abs/2610.20980)

**<font color=#1a73e8>作者：</font>** Annabelle Sujun Tang, Wei Tang, Songyao Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compiler transformations interact, making GPU kernel optimization a search for combinations that preserve the computation while improving performance. We introduce HOW TO TRAIN YOUR LITTLE DRAGON, a training method that teaches a small language model both to construct complete optimization scripts and to improve existing ones. Instead of ranking candidates or generating kernel code, our model generates optimization scripts. We devise a compact, lossless representation whose deterministic decoding reconstructs the exact compiler trace, preserving its transformation parameters and dependencies. We use a compiler framework TVM MetaSchedule to build training data on 54,116 distinct workloads, and construct 108,594 examples in two training sets: 60,236 teach the model to generate an optimized script from an unoptimized kernel, while 48,358 teach it to produce a better script given the kernel and a somewhat optimized script. Supervised fine-tuning teaches the model to construct and improve optimization scripts from these search-derived examples. We then add reinforcement learning with a shaped reward that combines correctness with measured performance, awarding a latency-based bonus only to numerically correct kernels. We apply this training method to a model with 8 billion parameters. After supervised fine-tuning and reinforcement learning, the model achieves per-attempt correctness of 91.27% for construction and 92.01% for refinement, while reinforcement learning produces faster kernels than supervised training on 88 of 102 construction tasks and 145 of 170 refinement prompts. With only 8B parameters, our LITTLE DRAGON achieves higher per-attempt correctness and better kernel performance than six frontier LLMs: GPT-6 Astra, Opus 5, Kimi-K3, and GLM-5.3 among them, each with hundreds of billions to trillions of parameters, for which task-specific training is unavailable or expensive.

---


### 56. [Do As I Do, Not As I Say: On-Policy Distillation Inherits the Teacher in Vision-Language Models](https://arxiv.org/abs/2610.20989)

**<font color=#1a73e8>作者：</font>** Frank F. Yang, Kefei Yan, Yiren Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Improving the reasoning capabilities of vision-language models (VLMs) often relies on post-training with supervision from stronger models. Two common strategies are supervised fine-tuning (SFT), which trains on teacher-generated demonstrations, and on-policy distillation (OPD), which provides teacher feedback on trajectories generated by the student itself. While OPD can be more data-efficient by supervising student-generated trajectories, it is unclear how the teacher's supervision at each state affects the student's learned behavior. To study this question, we conduct a controlled comparison of OPD and filtered SFT across data budgets and tasks where the teacher exhibits different levels of reliability, and analyze how these differences shape student accuracy and completion behavior. Across the two tasks, we find that OPD is effective only when the teacher remains reliable on student-generated trajectories. On ChartQA, where the teacher completes 99% of its solutions, OPD trained on only 10% of the data comes within 1.4 accuracy points of full-data SFT. In contrast, on Geometry3K, where the teacher fails to complete 22% of its solutions, OPD underperforms SFT by 7.9 points, with most of the gap explained by incomplete responses. More strikingly, starting OPD from an SFT student reduces its completion rate from 76% to 62%, effectively erasing the completion behavior learned through SFT. Filtering teacher demonstrations for completeness alone recovers much of SFT's advantage. These results show that on-policy supervision can transfer not only teacher knowledge but also persistent failure modes on student-visited states. Code is available at this https URL.

---


### 57. [Can LLMs Anticipate Their Cruxes?](https://arxiv.org/abs/2610.21006)

**<font color=#1a73e8>作者：</font>** David Reber, James Reber, Ari Holtzman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To use language models to help us make decisions we would like to understand the rationale behind the language model's outputs. In principle, the language model provides its rationale as part of its text output. However, the sheer volume of text makes this hard to use in practice. In this paper, we are interested in extracting the cruxes that lead a model to recommend one action over another. We take a crux to be a sub-question that a model's rollouts disagree on, where changing its value may have altered the conclusion. A crux is therefore a property of the distribution of a model's rollouts, not of any one rollout. We consider three strategies of increasing computational cost. First, we just ask a model to identify, a priori, what the cruxes of a decision will be. Second, we have the model actually go through the process of generating a response and then extract the cruxes that arose in its reasoning. Finally, we generate many responses and extract the cruxes by comparing the reasoning across the rollouts. We make this last procedure computationally tractable with cheap calls to a reranker, an estimated 86 times less compute than a judge. We then conduct an extensive empirical evaluation to assess whether the computationally inexpensive options are sufficient. They are not. Across domains and models, we find that a model's a priori assessment of the cruxes has little relation to the factors that are actually identified as important a posteriori. Using a single rollout helps, but is still inadequate for identifying the full set of cruxes. Accordingly, for high-stakes decisions (and to understand the space of language model decision making) the many rollout procedure is unavoidable.

---


### 58. [CausalEvo: Causal Skill Self-Evolution for Health LLM Agents](https://arxiv.org/abs/2610.21016)

**<font color=#1a73e8>作者：</font>** Yuchen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents for health can accumulate reusable textual skills from task feedback, such as calculation criteria, measurement time points, and formula units. Deciding which skills to retain is consequential: useful rules improve later answers, while faulty generalizations propagate errors. We propose CausalEvo, a method for causal skill self-evolution that estimates the relative effects of deliberately changed skill sets while holding the model weights, feedback cases, and rule count fixed. At each evolution step, a frozen LLM proposes candidate rules, which are pooled with the incumbent skills so that the current skill set remains a feasible choice. Paired skill replacements against shared background rules are scored on the same feedback cases; least squares converts the score differences into relative skill values, and the top-ranked rules are retained, favoring incumbents on ties. A decision-loss bound separates candidate support, approximation, and estimation errors. On six MedCalc-Bench-Verified tasks with 120 held-out cases, CausalEvo achieves 60.00% accuracy, compared with 55.83% for SkillOpt and 51.67% without skills. Across the recorded training configurations, which use different optimization budgets, it consumes 55.6% fewer training tokens than SkillOpt. Gains concentrate in particular calculations alongside regressions on others, and paired accuracy intervals include zero. CausalEvo turns task feedback into controlled decisions about skill retention and replacement. Project repository: this https URL

---


### 59. [Learning to Read Out: Unembedding Dynamics in Language Model Pretraining](https://arxiv.org/abs/2610.21025)

**<font color=#1a73e8>作者：</font>** Matteo He, William F. Shen, Alex Iacob 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When does a language model acquire a capability? Developmental studies usually answer this by tracking when models start producing the correct token. But that prediction passes through the unembedding matrix, or readout, which is itself still being learned during pretraining. We show that a model's hidden states can encode task information before its own readout expresses it, so timelines read from outputs conflate what the model encodes with what its readout expresses. To track the readout directly, we introduce parameter-trajectory crosscoding, which fits one sparse dictionary to every token's readout row at every checkpoint. Unlike crosscoders on activations, it needs only checkpoint weights. We use it to locate a narrow early window, 0.4-1.1% of the way through Pythia's pretraining, in which the readout reorganizes and WordNet word categories become decodable from its rows. By then, linear probes on the hidden states already decode task information that the model's own outputs do not yet show. To test whether such gaps depend on how fast the readout learns, we pretrain small models from scratch that differ only in the readout's learning rate. We find that raising it makes the readout develop earlier and the gap close sooner, with little effect on final loss. Together, these results imply that early in training, where many developmental transitions are dated, a behavioral date can reflect when the readout learns to express task information and not when the model learns it.

---


### 60. [SCARCE: Emergent Institutions in Long-Horizon Multi-Agent Coding Systems](https://arxiv.org/abs/2610.21029)

**<font color=#1a73e8>作者：</font>** Abhinav Kumar, Rediet Abebe, Eugene Bagdasarian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As autonomous agents become widely deployed, coordinating access to shared computing resources and services will become increasingly important. Recent incidents have already revealed unplanned coordination between agents, highlighting the safety implications of these interactions. Yet prior studies of agent negotiation often use stylized games and simulated bargaining, leaving open how these behaviors develop during sustained, long-horizon tasks. We propose SCARCE (Shared Compute ARena for Coding agEnts), a framework in which agents solve sequences of coding tasks under individual deadlines while negotiating access to a shared execution resource. This negotiation determines when and for how long they can inspect programs, compile code, and run tests. We find that agents spontaneously develop informal institutions: persistent rules and commitments grounded in reputation, reciprocity, and precedent. These arrangements, which we call institutional behaviors, carry across tasks and influence resource allocation, with agents sometimes foregoing immediate advantages to honor earlier agreements. We develop a 21-category taxonomy of negotiation strategies and emergent norms and use it to analyze eight models and audit more than 1,500 trajectories across different environmental settings. Among the models tested, newer frontier models exhibit more institutional behaviors than older or lightweight models. Alongside cooperation, we observe exclusionary coalitions and rare divide-and-conquer strategies. SCARCE provides a controlled setting for proactively and systematically auditing how these relationships emerge, shape access to resources, and affect the safety and coordination of multi-agent systems.

---


### 61. [INCONVENIENT: A Benchmark to Assess LLM Generalization Capabilities from Convenience Samples](https://arxiv.org/abs/2610.21038)

**<font color=#1a73e8>作者：</font>** Sara Rezaeimanesh, Chad Klochko, Kundan Thind 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models for tabular prediction typically assume that training data are representative of the population on which they will be deployed. In practice, however, data are often collected based on convenience, availability, or cost, resulting in systematic sampling biases that can distort feature--target relationships and undermine real-world generalization. Existing tabular distribution-shift benchmarks primarily construct out-of-distribution (OOD) settings by partitioning observations across naturally occurring domains. While such partitions may induce changes in P(Y | X), the resulting shifts are neither explicitly controlled nor isolated, and the evaluation distributions themselves are often not representative of the broader target population. We introduce INCONVENIENT, a benchmark designed to study robustness to convenience-sample bias. Rather than relying on naturally occurring domain partitions, INCONVENIENT directly perturbs feature--target relationships in the training distribution while preserving the original population distribution as the deployment environment. This setting more closely reflects real-world scenarios in which models are developed from unrepresentative samples and subsequently deployed on a broader population. The distinction is particularly relevant for large language models (LLMs), whose pretraining may encode population-level knowledge that extends beyond the relationships observed in a biased training dataset. Unlike existing distribution-shift benchmarks, INCONVENIENT provides explicit control over both the direction and severity of relationship shifts, enabling a systematic assessment of robustness to convenience sampling. The benchmark comprises 200 tabular classification and regression datasets spanning diverse application domains and generates around 15,500 shifted training distributions which lead to substantial downstream degradation.

---


### 62. [ReviewPilot: A Multi-Agent System for Screening and Data Extraction in Systematic Reviews](https://arxiv.org/abs/2610.21042)

**<font color=#1a73e8>作者：</font>** Zhaoqian Xue, Shaoze Zhou, Xuexin Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systematic literature reviews follow the PRISMA process of screening scholarly works and extracting evidence from included studies. Deep research tools based on large language models (LLMs) can search and summarize the literature but do not record which studies are excluded or where extracted values come from. We develop a conversational multi-agent system called ReviewPilot that automates the PRISMA workflow from paper screening to information extraction. Researchers can tailor criteria and schemas through dialogue, and a project memory keeps their configurations and revisions. Each screening decision comes with its reason and each extracted value with its source. On epidemiological expert reviews, ReviewPilot outperforms a single-prompt LLM and AgentSLR across three LLMs, with screening macro F1 up to 0.776 and extraction F1 up to 0.788. Case studies in biomedicine and human-computer interaction show close agreement with human annotators, suggesting that ReviewPilot can transfer beyond epidemiology. Code is available at this https URL.

---


### 63. [Learning When to Withdraw: Curriculum Coverage and Rule-Specific Failures in Fine-Tuned Language Agents](https://arxiv.org/abs/2610.21045)

**<font color=#1a73e8>作者：</font>** Mohamed Abouzahra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using language agents must revise prepared actions when evidence changes or authority is revoked. Selective withdrawal means suspending affected actions, preserving supported work, and resuming only after sufficient repair. We study supervised fine-tuning in NAQD-Env, a synthetic environment with explicit dependencies and a deterministic reference policy. Four LoRA checkpoints of Qwen2.5-3B-Instruct compare an original curriculum with an enriched one, the latter under three system-prompt framings with identical views and targets. Three instruction-tuned baselines and all four checkpoints are evaluated under three inference prompts on fresh validation cases, held-out dependency families, and held-out structural combinations. Under the naqd prompt, SFT checkpoints reach decision agreement of 0.77-0.92 and withdrawal recall of 0.46-0.86, versus 0.45-0.63 and at most 0.06 for the baselines. Rule-level diagnostics qualify these gains. The original-curriculum checkpoint wrongly withdraws 26 of 34 actions with surviving alternative support; enriched checkpoints withdraw 0-1. Conversely, all SFT checkpoints narrow prohibited combinations less often than the 7B and 8B baselines, a case absent from both curricula. Delegation results show more withdrawal but poorer preservation of independently authorized actions, and all four checkpoints omit valid event reports. Framing contrasts vary across metrics and splits and do not establish a reproducible advantage or equivalence. One training run per arm, jointly changed curriculum properties, prior evaluation exposure, and baseline-SFT quantization differences limit causal attribution. The contribution is a method for detecting rule-specific regressions that aggregate accuracy can conceal, not evidence that fine-tuning alone ensures agent safety.

---


### 64. [PremiseCheck: Efficient Fact-Checking of Human and AI Peer Reviews](https://arxiv.org/abs/2610.21046)

**<font color=#1a73e8>作者：</font>** Dingjie Song, Zhiling Yan, Ziqian Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Peer review is under strain from the growth of submissions, and review comments written by humans or AI can misstate what a paper says. We introduce ReviewFact, a benchmark that labels such factual errors in review comments under one definition across NLP, machine learning, and the natural sciences, and that measures cost and latency alongside accuracy. A frontier LLM checks comments well but must read the whole paper for each check, while cheap decision models, which score whether a statement holds in a text, fall far short on whole comments that mix several implicit assertions. PremiseCheck is a framework that combines the two. An LLM rewrites each comment as explicit premises without reading the paper, and a decision model checks each premise against the paper. When each comment is checked on its own, PremiseCheck reaches accuracy comparable to GPT-5.5 across all three fields at about half its cost, and on NLP reviews at a quarter of its cost and less than half its latency.

---


### 65. [Athanor: An Agent-Native System for Autonomous Post-Training Research](https://arxiv.org/abs/2610.21055)

**<font color=#1a73e8>作者：</font>** Yufa Zhou, Yichen Wang, Jiakun Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement, in which AI systems build stronger AI systems, is one promising route to superintelligence. We study a weaker form that can be measured today: frontier agents post-training a small raw base model with public data, as a test of their research potential. We build Athanor, an open agent-native system for autonomous post-training research (AutoPostTrain) on real GPUs. We give the agents full research autonomy, low-friction engineering tools, and efficient starter code. The agents carry out the research themselves: they read datasets and evaluation results, build their training data, write and modify training algorithms, tune hyperparameters, and analyze the results to decide what to try next. They work in a sandbox and cannot use external teacher models. Athanor's services supply frozen evaluation, managed jobs, decontaminated data, a persistent research record, and a held-out suite the agents are unaware of. In a 104-hour campaign, a team of four Claude Opus 5.5 agents, each on an eight-GPU node and given no research advice, improves Qwen3-4B-Base from 15.9 to 67.3 on a six-task development suite and from 9.2 to 48.2 on a held-out suite, against 66.5 and 47.9 for the official Qwen3-4B-Instruct-2507. To our knowledge, this is the first demonstration that a team of frontier agents can autonomously post-train a raw base model into a cross-domain generalist model that matches or surpasses the official instruct version on average. The campaign's full record shows that the agents reach this level by recombining known methods and each other's models: SFT on public reasoning data, RL with a rollout change one agent introduced, weight merges across agents, and rounds of self-distillation. With execution handled, today's agents already have the engineering and research ability to conquer this task. We hope Athanor provides a foundation for scaling autonomous AI research.

---


### 66. [Bellman-Consistent Trajectory RL for LLM Arithmetic Reasoning](https://arxiv.org/abs/2610.21060)

**<font color=#1a73e8>作者：</font>** Lianfa Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To address sparse terminal rewards in LLM arithmetic reasoning, we propose a Bellman-consistent trajectory RL method. Our framework introduces Trajectory Bellman Residual Minimization (TBRM) to transform sparse rewards into dense token-level signals. We integrate a Reinforce Leave-One-Out (RLOO) group strategy to reduce gradient variance of Bellman residuals and use hindsight goal relabeling to accelerate intermediate learning. Evaluated on the Countdown task, our method alleviates optimization bottlenecks and stabilizes gradient variance significantly better than GRPO. The TBRM-RLOO framework boosts Pass@1 to 0.55--0.64 and achieves a state-of-the-art Pass@16 accuracy of 76.0--84.0\%, outperforming the SFT, IPO/DPO, and RLOO baselines. Our approach demonstrates exceptional single-sample efficiency and successfully circumvents standard performance plateaus via test-time scaling.

---


### 67. [Multimodal AI Detection for Math-Heavy Scientific Text](https://arxiv.org/abs/2610.21062)

**<font color=#1a73e8>作者：</font>** Yixuan Huang, Danish Pruthi, Bhuwan Dhingra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models become increasingly capable of generating, and assisting with, scientific writing, there is a need for greater transparency and disclosure around the use of AI in research. Consequently, a veritable subfield of research and a number of commercial services aim to flag AI-generated content automatically. However, existing detectors which rely only on text extracted from PDFs fail to benefit from the rich visual information contained in the formatting of math-heavy scientific content. To study this, we select human-written proof and prose passages from pre-2022 arXiv LaTeX sources and re-generate them using 15 modern LLMs within the context of the same paper. This leaves us with coupled human and AI outputs in three different representations: the LaTeX source, a rendered image of the PDF, and the text extracted from the PDF. We find that the accuracy of the state-of-the-art Pangram 4 drops significantly as the mathematical content in a passage increases, especially when evaluated on text as opposed to LaTeX. However, this is not an inherent limitation of detecting AI-generated math: finetuning Qwen-3.5-27B based detectors on this domain recovers the gap, with LaTeX inputs performing significantly better than text since they preserve more formatting information. Since LaTeX sources are rarely available in practice, we also train SnapJudge: an image-based detector operating on screenshots of both prose and proofs from papers. At 0.1% false positive rate, SnapJudge achieves a detection rate of 92% on proofs and 93% on prose generated by frontier models, substantially outperforming both Pangram 4 and our text-based detector. We release our data, models and code at this https URL.

---


### 68. [Approve What, Exactly? Effect Binding and Trusted Rendering for Agent Step-Up Authorization](https://arxiv.org/abs/2610.21063)

**<font color=#1a73e8>作者：</font>** Sai Varun Kodathala, Prashanth Pollishetty, Jaylen Cargill  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents now pause for approval before they send money, delete files or email outsiders, and that approval is usually treated as a second factor. We argue it is one only when compromising the agent cannot produce it and when it names exactly what it approves, and we test both conditions. We define twelve attacks on the approval path, including decoy recipients, amount cancellation, card padding, label spoofing, enrollment squatting and threshold splitting, and run them against the Agent Payments Protocol (AP2), the Microsoft action-bound approval design and Model Context Protocol (MCP) elicitation. An audit of ten agent runtimes finds no third-party verifiable approval record, no flood limits where measurable, and post-approval argument changes in four of eight runtimes with measurable binding. As a reference defense we build ASU (Agent Step-Up), a gateway that renders the approval card from a canonical effect descriptor, has a passkey on the phone of the user sign its digest, and executes only the stored call. Tamarin proves its binding, single-use and key-level non-repudiation properties under three stated hypotheses (53 lemmas). Across 27,108 scripted trials and 609 AgentDojo attack pairs, ASU stops substitution, replay and grant stretching, and the trusted card cuts forged-narration attack success from 0.54 to 0.03. With 15 current language models as automated approvers, the trusted card raises the attack catch rate from 0.30 to 0.98, at the cost of refusing 16 percent of harmless near misses, mostly due to a placeholder artifact in our stimuli. A second device adds nothing measurable over a trusted on-host confirmation in these experiments, flooding still succeeds 0.45 to 0.60 of the time against a modeled approver, and approval cannot stop effects that policy already allows. Code, data and proofs: this https URL

---


### 69. [XARA: A Multimodal Agentic System for eXtended Reality Experiment Generation](https://arxiv.org/abs/2610.21067)

**<font color=#1a73e8>作者：</font>** Tareq Alsaleh, Thomas Zhao, Luke Guardino 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Controlled experiments are essential for advancing transportation research, yet designing eXtended Reality (XR) environments for behavioural studies remains technically demanding and inaccessible to many domain researchers. Current workflows require proficiency in game engines such as Unity or Unreal Engine, imposing significant barriers to rapid scenario prototyping and iterative experiment design. This paper presents XARA, a novel system that integrates a dual large language model (LLM) architecture with an immersive XR environment to enable voice driven experiment generation for transportation research. XARA employs a pipeline in which spoken natural language commands are first transcribed and then interpreted into structured commands that manipulate a Unity based XR scene in real time. The system supports object creation, spatial manipulation, animation control, and scene persistence through a modular architecture. By lowering the technical threshold for XR experiment creation, XARA enables transportation researchers to rapidly prototype driving, pedestrian, and urban design scenarios using intuitive voice commands and hand gestures within an immersive 3D environment. This paper describes the system architecture, the voice to command pipeline, and discusses potential applications across behavioural travel experiments, safety studies, human factors research, and policy testing.

---


### 70. [Sci$Π$vot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents](https://arxiv.org/abs/2610.21082)

**<font color=#1a73e8>作者：</font>** Youran Sun, Xingyu Ren, Chugang Yi 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can keep scientific experiments running for months with little human supervision, but reliable autonomous research also requires scientific judgment. Evaluating scientific judgment is difficult because research decisions are open-ended and depend on project context. We construct Sci$\Pi$vot, a 248-case benchmark of scientific judgment based on human corrections. The benchmark draws on records from six months of research in which senior researchers ran LLM agents on 26 projects across six scientific fields and repeatedly intervened to correct the agents' research judgments. In each case, an agent chooses between the original LLM plan and the human-corrected alternative, using only the project record available before the correction as context. We compare LLM and human performance and examine the effects of reasoning effort, access to the project record, and reconsideration. At medium reasoning effort with the project record, models systematically prefer the original LLM plan over the human-corrected alternative. Four of five frontier models perform below chance on the selected cases. The highest accuracy in the project condition across the tested models and reasoning effort settings is 63.5%, compared with 73.4% for fresh researchers. At medium effort, every model achieves lower accuracy with the project record than without it, and reconsideration does not consistently improve overall accuracy. Even with a human-corrected alternative available, frontier models struggle with the selected research decisions, while Sci$\Pi$vot supports systematic evaluation of scientific judgment for LLM agents.

---


### 71. [A Jury, Not an Electorate: Label-Free Reliability Estimation for Ensembles of Language Models](https://arxiv.org/abs/2610.21085)

**<font color=#1a73e8>作者：</font>** Alessandro Rozza, Davide Mambelli, Steven Motta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An ensemble of language models is a jury, not an electorate. The answers are testimony from witnesses of unknown reliability, and the question is not what the majority said but who is credible. Most ensemble methods assign each expert a fixed reputation, often learned from labels. We ask whether it can instead be inferred from the pattern of agreement and disagreement among the experts. We model the experts as a jury: each question has a latent true answer, each expert reports it with unknown reliability, and those reliabilities are estimated by Expectation Maximisation (EM) from unlabelled answer configurations alone. We show that its decision rule reduces to a log-odds weighted linear score over the experts' answer distributions. What changes is not how the jury votes, but how it learns whom to trust. On a 1560-question benchmark, the jury, with nine experts of up to 3B parameters, performs comparably to the same fusion rule with label-fitted weights, showing no statistically significant advantage from supervision. Instead, it outperforms the best single model with matched self-consistency and the strongest label-free alternative on the full benchmark.

---


### 72. [MemComposer: Learning to Assemble Memories for LLM Agents via Reinforcement Learning](https://arxiv.org/abs/2610.21091)

**<font color=#1a73e8>作者：</font>** Yixuan Xie, Xueqiang Xu, Xinyi Fan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent memory enables large language model (LLM) agents to reuse past experiences without updating their parameters. However, semantic similarity alone does not guarantee memory usefulness: downstream performance depends on how memories are selected and presented to the agent. We propose MemComposer, a memory composer that jointly examines the current query and retrieved candidates to decide which experiences to include, how many to select, and how to order them. We train the composer using Experience Policy Optimization (ExPO), a GRPO-based framework that evaluates assembled memory contexts through complete agent interactions and uses task-success feedback to optimize the assembly policy. Across three $\tau^2$-bench domains with two frozen executors, MemComposer outperforms the strongest baseline for each executor while reducing average memory-token usage by 16.9% and 4.9%, respectively. The learned policy also transfers to unseen domains, executors, and memory banks, and benefits from memories generated by stronger models without further training. These results demonstrate the value of learning query-specific memory assembly using downstream task feedback.

---


### 73. [Planning Commitment of LLM under Partial Observability](https://arxiv.org/abs/2610.21108)

**<font color=#1a73e8>作者：</font>** Cassie Huang, Zhanwei Cao, Yeawon Lee 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based planning agents commit to plans of different lengths before interacting with a partially observable environment. Some aggressively commit to a long plan based on assumptions about unobserved states, while others conservatively plan only over what they have observed. Both behaviors emerge implicitly in pre-trained models, whether the LLM outputs a plan directly or generates a PDDL formulation for a classical solver. Aggressive commitment risks costly failures, while conservative commitment risks excessive LLM calls. This choice pits safety against efficiency, a trade-off that has been neither characterized systematically nor made controllable. We investigate aggressive and conservative LLM planners and formalizers on two partially observable domains, where priors are provided as either explicit statistics or common-sense knowledge. Across three LLMs, both strategies reach similar accuracy. Conservative methods achieve fewer failed attempts (safety) at the cost of more API calls (efficiency). Aggressive methods fail more often but replan efficiently only when priors are informative. Interestingly, analysis shows that LLMs treat the provided priors nearly as facts, which risks failure when priors are unreliable. We also explore hybrid strategies with tunable hyperparameters that adjust the balance between safety and efficiency.

---


### 74. [SSR: Structural Signal Retriever for Scalable Agent Discovery in LLM-Orchestrated Multi-Agent Systems](https://arxiv.org/abs/2610.21113)

**<font color=#1a73e8>作者：</font>** Giancarlo Maldonado Cárdenas, Carlos A. Astudillo, Nelson L. S. da Fonseca  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large-scale multi-agent ecosystems require mechanisms for discovering suitable agents without exposing entire registries to a large language model (LLM) orchestrator. The challenge is not only to retrieve relevant Agent Cards from a growing registry, but also to maintain a compact candidate context, since each additional candidate increases prompt size, inference cost, latency, and the risk of exceeding the model context window. We formulate this problem as candidate-context scalability and propose the Structural Signal Retriever (SSR), our deterministic and training-free retrieval method designed for Agent Card discovery. SSR derives structural lexical signals from capability-bearing Agent Card fields, weights them using inverse document frequency (IDF), and uses an Inverted Signal Index (ISI) for selective candidate scoring. We evaluate SSR using a synthetic agent benchmark, a public MS MARCO adaptation, and end-to-end LLM orchestration. At 1,000 agents, SSR reduces LLM input by 98.8% and orchestration latency by 70.9% relative to full-catalog orchestration. On MS MARCO, IDF improves retrieval effectiveness within the structural representation, while the ISI preserves retrieval effectiveness and reduces explicitly scored passages by 96.8%. End-to-end experiments show that candidate pre-selection maintains a compact candidate context as registry size grows and avoids the operational failures observed with full-catalog orchestration. These results support SSR as an Agent-Card-native, traceable retrieval mechanism for candidate-context scalability.

---


### 75. [Compression Does Not End at Selection: Post-Selection Positional Geometry for Sparse KV Caches](https://arxiv.org/abs/2610.21126)

**<font color=#1a73e8>作者：</font>** Wanyang Hong, Zhaoning Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse KV compression reduces long-context inference costs by retaining selected historical states, yet these states typically keep their coordinates from the full history. Under Rotary Position Embedding (RoPE), gaps left by evicted tokens continue to affect query-key matching, potentially limiting the use of retained evidence. We study post-selection positional geometry on a fixed selector-produced cache, examining how positional organization affects the use of retained information and which coordinate and continuation rules improve answer quality. To reorganize this geometry, we propose RoPERelay, which assigns compact, order-preserving RoPE coordinates, relocates cached key phases through inverse rotation and re-rotation, and synchronizes the current query and subsequent generation. It reuses existing K/V without renewed selection, historical re-prefill, or additional cache budget. Across 36 comparisons spanning two models, six sparse selectors, and three long-term memory tasks, RoPERelay improves answer quality in 32 cases. For Llama-3.1-8B-Instruct with BM25 on LongMemEval-S, accuracy increases from 23.6% to 35.4%. Measured complete-request time overhead is approximately 1%-3% in the evaluated configurations. These findings establish positional organization as a distinct optimization dimension for sparse KV caches after content selection.

---


### 76. [Predicting Live Birth After Fresh Embryo Transfer in IVF/ICSI: Differential ICM/Trophectoderm Morphology Encoding and a Hybrid Attention--Logistic Regression Ensemble](https://arxiv.org/abs/2610.21134)

**<font color=#1a73e8>作者：</font>** Abdul Raheem Shahzad, Jinxin Chen, Ming Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting live birth before fresh embryo transfer could support shared decision-making in IVF/ICSI, but routine clinical data are small, heterogeneous, and contain pathway-dependent variables prone to outcome leakage. We aimed to construct a curated single-centre IVF/ICSI dataset and develop a prediction model suited to small tabular clinical data. \textit{Materials and Methods:} We assembled 616 fresh embryo-transfer cycles (251 live birth, 365 non-live birth) with clinical, laboratory, and embryological predictors, and embryo morphology encoded with a novel differential weighting of the inner cell mass and trophectoderm. After KNN imputation, robust scaling, and selection of 50 features, we developed a Hybrid Attention Network (HAN), a learnable feature-attention gate followed by a compact multilayer perceptron, and a HAN + logistic-regression (LR) ensemble with a validation-tuned weight. Models were benchmarked against classical machine learning, TabPFN, and text-serialized language models on a held-out test set; AUC-ROC was the primary metric. \textit{Results:} The HAN + LR ensemble achieved the highest test AUC-ROC (0.710; accuracy 0.710, F1 0.630), ahead of the HAN backbone alone (0.700), logistic regression (0.667), the TabPFN + LR hybrid (0.666), and TabPFN (0.650). Text-serialized language models performed near chance (AUC $\le$ 0.61). The differentially weighted trophectoderm feature ranked highest by consensus importance across models. \textit{Discussion:} A compact attention network combined with a linear model outperformed both components and strong foundation-model baselines on a small clinical cohort. \textit{Conclusion:} The curated dataset and HAN + LR ensemble offer a transparent, reproducible basis for IVF/ICSI live-birth prediction; external validation is the next step.

---


### 77. [Stronger Judges Do Not See More: Deployment-Integrity Blindness in LLM Evaluation](https://arxiv.org/abs/2610.21135)

**<font color=#1a73e8>作者：</font>** Jianchang Su, Dawei Xiang, Yifan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-agent evaluation reports behavioral scores but leaves the identity of the deployed runtime stack unreported. A tampered deployment that preserves evaluated outputs passes every output-only evaluator. We introduce DIB-Bench, a benchmark that measures this deployment-integrity blindness across 7,560 scored examples, six tamper types, and an evaluator ladder from regex scorers through LLM judges to GPT-5-nano. Stronger evaluators accept more tampered outputs: mean acceptance rises from 88.6% (rule-based) to 94.1% (GPT-5-nano), and a trigger-conditional tamper invisible on the evaluation suite produces 48-100% harmful outputs, rising with model capability. A PAC-style bound shows that tampers with zero output shift are undetectable from outputs at any sample size; a manifest-hash identity channel detects them with zero samples. Behavioral fingerprinting identifies the model component above chance (76.7%) but covers one of six stack components. We also propose a graded deployment-identity descriptor for evaluation reports.

---


### 78. [OnBodyAI - Why the Next AI Needs a Body](https://arxiv.org/abs/2610.21137)

**<font color=#1a73e8>作者：</font>** Michael Beigl  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The next AI will not win by knowing more about the world. It will win because it knows you: because it lives on your body, works for you and answers to you. That is what the term OnBodyAI stands for. It describes what happens when large language models are given a body, and what research and industry need to make that happen. This article is based on my talk in the Industrial Panel at UbiComp/ISWC 2026 in Shanghai (October 13, 2026) and follows its ten key statements.

---


### 79. [CleanRM: Reward Modeling from Noisy Feedback with a Few Clean Feedback for RLHF](https://arxiv.org/abs/2610.21138)

**<font color=#1a73e8>作者：</font>** Licheng Pan, Haocheng Yang, Yuzhou Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Feedback noise is pervasive in preference data, arising from subjective human judgments, annotation mistakes, and imperfect LLM judges. Standard reward modeling trained on such feedback yields a biased estimate of the clean risk. Although classical denoising methods are directly applicable to noisy feedback learning, they generally assume a uniform noise ratio across samples. However, this assumption fails for feedback data, where noise is intrinsically sample-wise. To address this challenge, we propose CleanRM, which uses a few clean feedback to calibrate sample-wise noise ratios via optimal transport. Specifically, CleanRM aligns the joint distribution of preferences reverted from noisy feedback with that of clean feedback and then trains the reward model using a noise-corrected surrogate loss. Theoretically, we prove that the resulting objective is unbiased with respect to the clean risk. Extensive experiments demonstrate that CleanRM outperforms state-of-the-art denoising baselines and yields more effective downstream RLHF alignment.

---


### 80. [All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents](https://arxiv.org/abs/2610.21147)

**<font color=#1a73e8>作者：</font>** Bingbing Wang, Jingjie Lin, Weiming Qiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly rely on external memory to answer queries grounded in long-horizon histories such as multi-session dialogues and lengthy documents. However, existing memory methods often optimize retrieval and memory construction separately, without a shared reward space for evaluating search, writing, and stopping decisions. To address this, we propose All-in-One Memory (AiO-Mem), which organizes these operations as transitions over a shared evidence state and directly evaluates the semantic quality of each action in a unified reward space. AiO-Mem compiles heterogeneous histories into source-traceable multi-view events, providing a shared substrate for retrieval and memory writing. A unified memory policy actor then rolls out complete interaction trajectories over this shared evidence state. A separate trajectory-conditioned process reward model is trained through evidence-grounded supervised fine-tuning and trajectory-level DPO to assign process scores to the collected trajectories. These scores are aggregated into an action-balanced trajectory reward and used by Process-Aligned DAPO (PA-DAPO) to optimize the memory policy. Across long-context memory benchmarks, AiO-Mem consistently improves answer accuracy over both static memory systems and RL-trained memory agents.

---


### 81. [From Observation to Intervention: Distilling Self-Generated In-Context Demonstrations via Executable Causal Intervention](https://arxiv.org/abs/2610.21149)

**<font color=#1a73e8>作者：</font>** Minming Ye, Min Liu, Haoang Chi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-generated In-Context Learning (ICL) enables LLMs to synthesize their own few-shot demonstrations, often outperforming manual prompts. However, existing methods filter demonstrations by observation, assuming a rationale is high-quality if it leads to the correct output. We show such filtering suffers from \textit{observational equivalence}, whereby both faithful causal rationales and spurious post-hoc rationales can yield same outputs and are statistically indistinguishable from observation alone. Inspired by independent causal mechanisms, we argue that faithful rationales imply \textit{transfer invariance}, in which causal rationales should remain effective across logically similar samples. We instantiate this criterion as \textbf{E}xecutable \textbf{C}ausal \textbf{I}ntervention for \textbf{D}emonstrations \textbf{D}istillation (ECI2D), which abstracts language rationales into executable programs and applies the causal interventions ($do$-operator) on logically similar samples, retaining only those demonstrations that imply transfer invariance. Experiments on math, logical and commonsense reasoning benchmarks demonstrate that ECI2D consistently outperforms observation-based ICL while retaining far fewer demonstrations, with gains exceeding 7 points as the test distribution shifts.

---


### 82. [CARE-SD: Explainable Reasoning Architecture for Local SLM Self-Disclosure Analysis in Textual Data](https://arxiv.org/abs/2610.21151)

**<font color=#1a73e8>作者：</font>** Aisvarya Adeseye, Adeyemi Adeseye, Mohammad Tahir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybersecurity interviews uncover critical security experiences, behaviors, and privacy concerns often not fully captured by conventional technical assessments. Consequently, identifying genuine self-disclosures is challenging because statements are context-dependent, categories overlap, and automated interpretations may introduce unsupported claims. Locally deployed Small Language Models (SLMs) protect sensitive participant data by keeping processing within controlled environments, but their limited reasoning capabilities make simple prompting insufficient for context-aware and factually reliable analysis. This study developed CARE-SD (Context-Adaptive Reasoning and Explanation for Self-Disclosure), a novel four-module architecture integrating context-adaptive processing, hierarchical disclosure reasoning, explanation-consistency verification, and cross-batch reconciliation. We evaluated three local SLMs, including Llama 1B, Qwen 1.5B, and Llama 3B, using 82 independently annotated cybersecurity interviews across five organizational sectors. Comparisons included conventional classifiers, three prompting strategies, larger 8B--32B models, and architectural ablations. Two independent reviewers assessed disclosure labels, factual claims, and explanation correctness. CARE-SD improved the accuracy and evidence reliability of SLMs, increasing Llama 3B Macro-F1 from 0.80 to 0.88 while reducing unsupported claims by 60\%. Remarkably, the 3B model matched the 20B reference model in category Macro-F1, demonstrating the effectiveness of the architecture without requiring a larger model.

---


### 83. [VisualTrust: Video Reasoning under On-Screen Claim Framing](https://arxiv.org/abs/2610.21159)

**<font color=#1a73e8>作者：</font>** Huachao Zhu, Junjielong Xu, Sicheng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-screen text can describe what a video shows, or it can frame what the video is supposed to mean. Current benchmarks treat both alike, testing whether a model can read the text rather than whether it should trust it. We study claim deference, multimodal large language models' tendency to let an on-screen claim override conflicting visual evidence. We introduce VisualTrust, a counterfactual benchmark with 5,063 cases across 14 claim-fact classes. Each case pairs a question with three versions of the same video: one with no claim, one with an accurate claim, and one with a misleading claim that alters a single grounded fact. The option the misleading claim supports is the trap answer. Across seven open-weight and four proprietary models, mean accuracy falls from 90.1% without a claim to 51.9% with a misleading claim. Among initially correct responses, 42.8% flip to the trap answer and only 0.6% become other errors. Strong no-claim accuracy does not ensure resistance. We also introduce DEAR (Decoupled Evidence Arbitration and Reading), a training-free agent for video question answering that separates evidence arbitration from reading. An independent check reports conflicting evidence, a selector weighs it without a fixed modality priority and blinds what it withholds, and the reader answers from the resulting video in a fresh context. On 500 videos across three proprietary models, DEAR raises accuracy under misleading claims from 47.2--64.0% to 81.8--85.2% and reduces trap-answer selection from 34.4--50.8% to 11.6--15.0%, while preserving no-claim accuracy.

---


### 84. [From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models](https://arxiv.org/abs/2610.21165)

**<font color=#1a73e8>作者：</font>** Chaogui Gou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context capability has become essential for large language models (LLMs) to handle complex tasks, yet continuously expanding the context window does not remove the computational, storage, and information-selection pressures incurred at inference time. Existing work on prompt compression, KV-cache management, efficient serving, retrieval augmentation, and agent memory is usually discussed in isolation, leaving the flow of information between storage and computation insufficiently understood. This survey reframes long-context compression as a memory-management problem for allocating inference-time resources. We distinguish compute-active memory, which directly participates in model computation, from compute-inactive memory, which lies outside the computation path but can be stored, retrieved, updated, or forgotten, and we characterize offloaded KV caches, persistent prefix caches, and precomputed KV states as intermediate states on the activation path. On this basis, we formulate writing, offloading, recall, retrieval-and-injection, materialization, eviction, consolidation, and forgetting as state transitions within an information lifecycle, and introduce a budgeted cost model that places these operations in a single cost account. The resulting framework unifies short-term context compression, long-term memory management, and the transitions between them, and shows that the central challenge is not merely reducing information volume but deciding which information should participate in costly inference, when, and in what form. We further summarize evaluation dimensions, benchmark gaps, and open challenges, and argue that future research should move from static, pointwise compression toward dynamic, governable, lifecycle-aware memory management.

---


### 85. [MemScope: Evolving Agent Memory Architectures through Localized Code Repair](https://arxiv.org/abs/2610.21170)

**<font color=#1a73e8>作者：</font>** Miao Su, Yucan Guo, Zixuan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent memory architectures define how LLM agents store and reuse experience across tasks, but they are typically fixed after deployment, limiting their adaptability across task types. Recent self-evolving approaches instead adapt these memory architectures using execution feedback, typically represented as evaluation scores or compressed summaries. However, such coarse-grained feedback is insufficient for precise failure localization in current agent systems, where long-horizon task execution involves multiple interacting components. Without a precise failure location, existing approaches lack a clear code-level target for modification, leaving the update scope weakly constrained and often leading to large-scale rewrites of an otherwise capable memory architecture. We propose MemScope, a framework for evidence-grounded, localized evolution of an existing memory architecture. Its tool-using Patch Agent jointly inspects raw execution traces, runtime memory state, and current architecture code to identify repair targets and apply bounded, in-place edits under provider-identity and memory-compatibility constraints. On GAIA, the trace-and-memory inspection variant achieves 86.67% accuracy, compared with 70.00% for trace-only and 63.33% for summary-only feedback. Under xBench tasks, the evolved memory architecture improves over its original version from 49 to 55 correct answers with DeepSeek V3.2 and from 50 to 53 with Kimi K2.7 Code. On disjoint ALFWorld unseen tasks, success rises from 50.75% to 71.64%. Across archived architecture-snapshot transitions, the median code-change ratio is 4.4%. These results support fine-grained execution evidence as a basis for localized, in-place memory-architecture evolution.

---


### 86. [Language Models Share a Readout Bottleneck in Working Memory](https://arxiv.org/abs/2610.21176)

**<font color=#1a73e8>作者：</font>** Dongyu Gong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) reproduce a human working-memory signature on the N-back task: performance declines as memory load N increases, and errors concentrate on lures, items that repeat the current stimulus at a neighboring but incorrect serial position. We ask whether this shared behavioral signature reflects a shared mechanism. The literature offers two candidate accounts. On a precision account, softmax attention cannot concentrate its weight on the item N positions back, so adjacent items are retrieved instead. On an interference account, attention selects the correct item, but the content of competing items corrupts the decision. We dissociate these accounts in 15 pretrained LLMs from three families (70 million to 14 billion parameters) and in minimal transformers trained from scratch. In all three families, the attention heads that carry the task attend to the target on most missed matches. Linear probes decode near-perfectly whether a matching letter occurred at the target or at a lure position, even on trials where the model false-alarms to the lure, although its own decisions barely distinguish the two. Sharpening attention yields negligible gains, whereas suppressing the letter identity of non-target items improves sensitivity (d') in nearly all model-by-load conditions. In larger models the task is spread over more heads, and removing interference helps more. In minimal transformers, precision limits a single attention layer, but a second layer removes this constraint. The working-memory limit of LLMs therefore lies in reading items out under interference rather than in locating them, consistent with interference accounts of human working memory.

---


### 87. [Judging the Judges: Confidence and Disagreement in Rubrics as Rewards](https://arxiv.org/abs/2610.21179)

**<font color=#1a73e8>作者：</font>** Michael Tian-Yue Liu, Anne Harrington, Trevor Darrell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rubrics as Rewards (RaR) extends reinforcement learning to non-verifiable domains by using an LLM judge to score responses against a structured rubric. Prior work has focused on improving the rubric or strengthening the single judge, with comparatively little attention to how different single or multiple judges might be used during RaR training. We first show that judge identity alone produces a substantial spread in scores when training Qwen3-4B-Base on RaR-Medicine and RaR-Science across five frontier and open-weight judges. Building on this, we propose RaRE (Rubrics as Rewards with Ensembles), a novel judge ensemble strategy for RaR with two mechanisms: a soft-Likert reward that uses judge logprobs to weight more confident judges more heavily, and a drop-on-disagreement mask that excludes high-disagreement rollouts from the GRPO update. We find that this design is critical: while a naive average of judge scores fails to outperform the best single judge, RaRE outperforms every single-judge RaR variant on both HealthBench and GPQA Diamond, with per-theme analysis showing that it inherits the complementary strengths of its constituent judges. Our findings establish judge ensembling as a compelling axis for improving RaR.

---


### 88. [Does Latent Chain-of-Thought Actually Reason? A Single, Unifying Taxonomy for Latent Reasoning](https://arxiv.org/abs/2610.21182)

**<font color=#1a73e8>作者：</font>** Jingjie Qiu, Sheldon Yu, Xunyi Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent chain-of-thought replaces written reasoning steps with continuous hidden states, giving models additional steps to compute before answering. It remains unclear what computation these steps actually perform. High task accuracy and decodable intermediate answers do not establish that a model uses its latent chain to reach an answer. We study this question across twenty-one model-task configurations covering three training recipes, three reasoning tasks, and two backbones. We combine chain deletion and content replacement with probes and trajectory analysis to test whether the chain affects the answer, what it encodes, and how its states change. On logical tasks, COCONUT often carries an answer that is already readable before the chain begins. Its states settle early, and deleting the chain leaves predictions almost unchanged. Per-step supervision produces an ordered layout of reasoning steps and can make the model depend on the chain. Yet even an ordered chain can act as a placeholder, with deletion hurting performance while content replacement leaves answers unchanged. On arithmetic tasks, all tested recipes show dependence on chain content. These results show why readable latent states alone are insufficient evidence of reasoning. We introduce a taxonomy that separates what a chain represents from how the model uses it. Seen this way, earlier reports no longer compete: placeholder tokens, collapsed superposition and step-dependent causal roles are each consistent with a different kind of chain, each obtained on a different task, training recipe or measurement. Once a study says which property it tested, whether the model uses the chain, what the chain holds, or how its state moves, claims about latent reasoning can be compared.

---


### 89. [Beyond Retrieval Failure: Understanding Why LLMs Miss Evidence in Multi-Hop RAG](https://arxiv.org/abs/2610.21184)

**<font color=#1a73e8>作者：</font>** Jiaqi Wei, Wenxuan Huang, Chengdong Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-hop retrieval-augmented generation (RAG) requires an agent to retrieve evidence for a sequence of dependent sub-questions. When a wrong answer lacks a required passage, the passage may be inaccessible to the retriever, or the agent may have failed to issue a query that would retrieve it. Standard retrieval evaluations conflate these two causes. We study how much apparent retrieval failure is instead caused by search drift: the search no longer tracks an unanswered sub-question. Holding the retriever, corpus, and generation model fixed, we introduce ExecutionRAG, a training-free requirement register that records open sub-questions and their supporting evidence. The register changes search guidance but not evidence access, so each gold passage it recovers certifies that the passage was reachable by the original retriever. On 1,000 MuSiQue questions, the number of wrong answers with unretrieved required evidence falls from 382 to 234 with all-MiniLM-L6-v2 and from 383 to 274 with Qwen3-Embedding-0.6B. These counts correspond to 69% to 44% and 66% to 48% of each system's wrong answers, respectively. Crucially, evidence recovery does not produce a proportional reduction in total error: premature resolutions and abstentions increase as missing-evidence failures decrease. The central finding is therefore a shift in the remaining bottleneck, from guiding search toward required evidence to verifying that the retrieved evidence is sufficient.

---


### 90. [Resisting Harmful Instructions through Training-Free Weight Editing](https://arxiv.org/abs/2610.21189)

**<font color=#1a73e8>作者：</font>** Ali Ebrahimpour-Boroojeny, Xiaocong Yang, Samuel Schapiro 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instruction-following language models can comply with requests that conflict with intended behaviors and safety alignment. We introduce a training-free weight-editing approach for reducing compliance with targeted undesirable instructions. Our method needs only forward passes on a small set of prompt pairs per target behavior, and because the edit is stored in the model's weights, changing or deleting instructions in the prompt cannot undo the weight modification. We evaluate the approach on two target harmful behaviors across five instruction-tuned models: instructed falsehood and instructed sexism. On two instructed-lying benchmarks, it improves mean honest response rates by 6.2 and 4.6 percentage points over the strongest alternative, significantly on three of the five models and within noise on the other two. In a controlled study of seven prompt formats, it maintains higher honest-response rates than single-layer activation steering when orders to lie arrive in single-turn formats not used to construct the edit. For instructed sexism, it reduces the mean sexist-response rate from 57.9% to 24.3%; combining the edit with a fairness prompt reduces it further to 11.9%. These results establish our contrast-based weight editing approach as an effective training-free intervention in two distinct behavioral domains, supporting its use both independently and alongside prompt-based safeguards.

---


### 91. [Condition-Contrastive Extrapolation for On-Policy Distillation of Language Models](https://arxiv.org/abs/2610.21195)

**<font color=#1a73e8>作者：</font>** Wenxuan Luo, Chenxi Li, Haoyue Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) improves a student language model by training on its own generated trajectories with supervision from a stronger teacher. However, when conditioned on student-generated prefixes, the teacher can favor invalid continuations that violate the question's premises, causing OPD to encourage erroneous reasoning steps. As a remedy, we introduce Condition-Contrastive Extrapolated On-Policy Distillation (CCE-OPD), which makes teacher supervision sensitive to question conditions. CCE-OPD incorporates (1) a fixed-prefix comparison in which the same frozen teacher evaluates the complete question and a counterpart with a selected condition masked, and (2) a bounded log-probability contrast that reweights the teacher distribution into an auxiliary distillation target. On 200 diagnostic reasoning states, condition contrast reduces the rate of preferring invalid continuations from 27.0% to 16.0%. Extensive experiments across six mathematical benchmarks show that CCE-OPD improves avg@8 over OPD by an average of 1.60 and 1.95 percentage points when distilling Qwen3-8B into 0.6B and 1.7B students, respectively. It also achieves the strongest results on four transfer benchmarks.

---


### 92. [Who May Release an Agent's Promise? Standing over Commitments in Multi-Party Chat](https://arxiv.org/abs/2610.21203)

**<font color=#1a73e8>作者：</font>** Lan Wei, Bingyu Shen, Jiaqi Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an assistant serving a team makes a promise to Alice, who may cancel it? We call this standing: only the creditor (the person owed) or someone the creditor or operator policy authorizes may release a commitment, regardless of rank. In a controlled chat environment we vary who cancels and separate two errors: unauthorized release (obeying someone without standing) and override (executing a released promise). Across six models, smaller open ones override the creditor (Qwen3.5-9B: 69%); larger ones drop promises on a peer's direct word (Qwen3.8-27B: 89%; gpt-6.1-sol: 83%); nearly all act on a bystander's "go ahead after all". Oracles dissociate the errors: stating the rule or the creditor curbs unauthorized release but not override, which the latter even raises in three of four models; among them, only knowing whether the promise is still owed cuts override. Enabling thinking moves smaller models the way scale does. A self-kept commitment ledger stops override in four of five models; with a one-paragraph release policy it matches or beats the best oracle store, raising gpt-6-luna's strict accuracy from 49% (policy alone) to 83%. Code, prompts, outputs and labels are released.

---


### 93. [Entertain, then Cancel: How Thinking Makes Reasoning Models Read Some and Or Literally](https://arxiv.org/abs/2610.21204)

**<font color=#1a73e8>作者：</font>** Zhizhuo Kou, Jian Yang, Pengfei Hao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a speaker says ``some students passed'', listeners infer that not all of them did. Reasoning models now let users decide how long a model thinks before it answers, but we do not know what extra thinking does to such everyday inferences. We study this directly: we keep a model's weights fixed, change only how much it thinks, and record which reading it chooses. A second tool cuts the model's own reasoning at successive points and asks for an answer, showing where the reading changes. Thinking makes models read logical words as logic: it cancels the implicatures of \emph{some} (\emph{not all}) and \emph{or} (\emph{not both}) in most tested open reasoning models and in GPT-5, while context-driven inferences such as indirect answers improve. The trace shows why: models first entertain the enriched reading and cancel it later. Answering from that early reading, an exploratory inference-time remedy, recovers these implicatures without losing literal accuracy. Evaluations of reasoning models should measure how they interpret, not only how accurate they are.

---


### 94. [Rubric Judgments Lack Uncertainty: Conformal Weighting for LLM Evaluation](https://arxiv.org/abs/2610.21214)

**<font color=#1a73e8>作者：</font>** Licheng Pan, Haocheng Yang, Haoxuan Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rubric-based evaluation is widely used to assess large language model (LLM) outputs by decomposing quality into multiple criteria and assigning each a binary judgment from an LLM verifier. However, judgment certainty varies substantially across criteria. Existing methods uniformly aggregate these judgments into a final score, implicitly treating every criterion as equally certain and overlooking this heterogeneity. As a result, uncertain judgments remain incorporated into reward estimation without distinction, potentially yielding misleading training signals for downstream reinforcement learning (RL). To address this limitation, we propose Uncertainty-aware Rubric Weighting (URW), a training-free framework that quantifies criterion-level judgment uncertainty via conformal calibration. Specifically, URW elicits a soft uncertainty signal from a fixed pool of paraphrased judgment templates and converts it into a per-criterion weight using split-conformal $p$-values with provable coverage guarantees. Extensive experiments demonstrate that URW consistently improves pairwise preference accuracy and delivers stronger downstream RL alignment.

---


### 95. [AutoOnboarder: Autonomously Onboarding LLM Agents](https://arxiv.org/abs/2610.21218)

**<font color=#1a73e8>作者：</font>** Tanay Arora, Cong Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic large language models have been documented to lose reasoning capability when placed inside a harness, the software that mediates their observations and actions. To reconcile these losses, we introduce AutoOnboarder, an autonomous system that adapts an agent to a task the way a trainer onboards a new employee. It places the agent under the supervision of an intelligent ``Onboarder'' coding agent, which iteratively tailors its foundation model, prompt, and harness source code to simultaneously improve performance and decrease cost. Like a real onboarding process, the Onboarder is only given tens of examples, and all evaluation data is isolated on a separate virtual machine to prevent leakage. We report the lessons learned from building and testing AutoOnboarder on genomic-sequencing prior authorization form submission. Autonomously onboarded agents are able to match or exceed the performance of a Gemini 3.5 Flash baseline at up to 29$\times$ lower costs. However, these agents remain imperfect, and the Onboarding process varies greatly in terms of final performance. We conclude that future Onboarding systems require a robust environment for the Onboarder, including a structured thought interface, (controlled) internet access, and a wide model search space.

---


### 96. [Not All Change Is Damage: Update-Matched Unlearning for Large Language Models](https://arxiv.org/abs/2610.21230)

**<font color=#1a73e8>作者：</font>** Jie Li, Youming Tao, Bowei He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlearning aims to remove selected knowledge from large language models to mitigate privacy and safety risks while preserving useful capabilities. For models that continue to be fine-tuned after release, this goal is insufficient: they must also resist relearning the deleted knowledge while preserving plasticity, the ability to learn new tasks. Existing defenses train against simulated relearning while trying to preserve useful capabilities, but low relearning alone cannot distinguish selective resistance from a general loss of plasticity. Evaluating preservation after an update requires deciding what the updated model should remain close to. A pre-update reference penalizes useful changes induced by the update simply because they depart from earlier outputs. We therefore formulate the reference-timing hypothesis that, at comparable target suppression, an update-matched reference better preserves plasticity than a pre-update one. To test and address this hypothesis, we propose Update-Matched Unlearning (UMU), which applies the same simulated relearning update to the defended model and to an undefended reference initialized from the same unlearned model, and uses new-task learning to guide model selection. Extensive experiments on TOFU and FaithUn with Llama and Qwen models show that UMU improves both relearning resistance and plasticity across all three base unlearning methods, lowering harmful and benign relearning by 30.4 and 9.9 points on average while raising new-task accuracy by 3.5 points. When the reference does not receive the update, relearning remains similarly low but new-task accuracy falls below the base method, supporting the reference-timing hypothesis and showing that robust unlearning should prevent recovery selectively without suppressing learning itself.

---


### 97. [Compatibility Matters: A Framework for Token-Level Teacher Selection in On-Policy Distillation](https://arxiv.org/abs/2610.21234)

**<font color=#1a73e8>作者：</font>** Stanley Wei, Jiin Woo, Kaan Ozkara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has recently been introduced as a promising paradigm for continual learning, where a student policy can be supervised at the token-level. Typically, OPD is performed using a single teacher per prompt rollout (or even per training run). However, this ignores a whole other axis of flexibility that is available due to the on-policy nature - token-level teacher selection during rollouts. Building on this insight, we theoretically explore what makes a teacher and a student compatible for OPD, and leverage our findings to derive several empirical heuristics for teacher selection. In particular, our framework captures several desiderata for OPD: compatible teacher-student reasoning patterns, teacher competence, and induced student diversity. Theoretically, we categorize several types of teacher routing schemes, and we prove that under different scenarios, different routing schemes are likely to be beneficial for optimization and student diversity. We back up our findings with extensive experimental results in domains such as math, coding, kernel generation, and visual reasoning, where we find upwards of 10 percentage points of improvement on pass@$k$ when compared to vanilla OPD and the teacher experts on certain tasks, indicating both capability improvement and diversity over high-quality responses.

---


### 98. [Representation Redistribution in Sparse Autoencoders](https://arxiv.org/abs/2610.21240)

**<font color=#1a73e8>作者：</font>** Ziye Mei, Haotian Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) decompose language model activations into sparse features, but prompt transformations designed to preserve the underlying request can redistribute activity across them. A feature change observed on one transformed prompt need not recur, and even a recurring change need not affect a downstream computation. We introduce the redistribution sensitivity score (RSS), which identifies large feature responses that recur in a consistent direction, and evaluate the resulting supports on variants excluded from selection. Across 27 pretrained SAEs spanning eight language models, the tested prompt transformations produce a reproducible redistribution profile on these excluded variants. We then separate recurring representation change from signed readout contribution and decision failure. For a fixed linear readout, an exact decomposition shows how response magnitude, readout coefficients, directional alignment, and the clean margin determine downstream consequences. In two frozen safety readouts, combining RSS support erosion with the full clean margin yields recurrent failure AUROCs of 0.935 and 0.958 using median supports of 20 and 19 features, compared with 0.965 and 0.964 using full erosion. RSS therefore provides a way to identify recurring sparse representation changes and quantify their contribution to a downstream readout without equating representation change with failure. Code is available at this https URL

---


### 99. [System1-Arena: Which Decisions Can Be Left to System 1?](https://arxiv.org/abs/2610.21244)

**<font color=#1a73e8>作者：</font>** Tianyu Chen, Xinyang Liu, Ruyi An 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often make discrete decisions, such as flagging phishing or escalating to a human. System-1 models, such as Jev and the OpenAI Decisions API, return probabilities over options in a single forward pass, while System-2 approaches generate reasoning steps. Which decisions can System-1 models handle, and which require generative reasoning? We introduce System1-Arena, a benchmark that gives all models the same decision requests and scores their probabilities. It contains 92k questions across 105 tasks from 268 public sources, in four groups: text classification and knowledge, applied decisions, evaluation and control, and agent and action. It also includes 138 closed-loop environments, from web shopping and SWE-bench coding control to robotics, games, and driving; in real-time mode, the world evolves while a model decides. We evaluate 30 models: 7 closed LLMs, 13 open LLMs read at the answer token, and 10 System-1 models. The largest System-1 models match or exceed fast closed LLMs in non-agentic accuracy, with better-calibrated probabilities at one-quarter of the latency. A reasoning LLM is the most accurate, at about 70x the cost of a fast LLM. In closed loops, large open LLMs succeed most often (up to 32.9%); small System-1 models rarely succeed.

---


### 100. [From One Query to Many: A Critical Survey of Privacy Accounting in RAG](https://arxiv.org/abs/2610.21245)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) enables large language models to leverage external knowledge but introduces privacy risks when the retrieved corpus contains sensitive information. Differential privacy (DP) offers formal protection, yet interpreting and comparing privacy guarantees across existing DP-RAG methods remains challenging. In particular, a privacy budget reported for a single response does not directly characterize privacy loss over repeated queries, and even identical values of $\varepsilon$ may represent different guarantees depending on the protected data unit, accounting horizon, and observable outputs. This survey critically examines how privacy accounting evolves from single-query generation to multi-query RAG systems. We categorize existing approaches into query-time privatization, multi-query accounting, and one-time corpus privatization. We analyze their underlying assumptions and privacy--utility trade-offs. Rather than ranking methods by $\varepsilon$ alone, we propose a framework that interprets a DP-RAG guarantee along three dimensions: privacy granularity, accounting scope, and release boundaries. We conclude that an $\eps$ is a claim only together with the three slots: the protected unit, the accounting scope, and the release boundary.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-321](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
