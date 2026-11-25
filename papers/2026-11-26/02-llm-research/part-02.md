# 🧠 大模型相关研究 | 2026年11月26日

> 本类共 **299** 篇论文：已确认 **280** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-299](./part-06.md)

---

### 51. [Frequency-Conditioned Privacy Auditing of Fine-Tuned Language Models](https://arxiv.org/abs/2611.31581)

**<font color=#1a73e8>作者：</font>** Aymen Noor, Ke Lyu, Honglu Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly fine-tuned on sensitive data, where the same person's information may appear multiple times across records. This can cause models to memorize sensitive information, but memorization does not necessarily mean that the information can be recovered. A more serious privacy risk arises when the model begins to reproduce that information during generation. In this paper, we study how often sensitive information must appear in the fine-tuning data before it becomes recoverable. Across four language models, we vary the frequency of email addresses and phone numbers from $1\times$ to $50\times$ and compare standard fine-tuning, gradient clipping, and differentially private training. We find that the number of repetitions required before sensitive information becomes recoverable varies substantially across models. Gradient clipping can delay extraction, but it does not consistently prevent leakage at high repetition. DP-SGD at $\varepsilon=5$ produces zero observed extraction through $50\times$ repetition across all four models under the attacks we test, although the utility cost varies by model. These findings characterize how observed extraction varies across sensitive-data frequencies, model families, and training mechanisms, and highlight substantial differences in extraction behavior across models. Code and data are publicly available.

---


### 52. [LatentLens: Rethinking Latent Interface in Multi-Agent Systems](https://arxiv.org/abs/2611.31582)

**<font color=#1a73e8>作者：</font>** Ziqing Yang, Kewei Cheng, Mingjie Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent interfaces let agents in a multi-agent system communicate through continuous representations rather than decoded text. Prior work reports performance and efficiency gains, but neither separates latent communication from the agent harness nor examines its internal components, leaving its actual contribution unclear. We propose LatentLens, a framework that decouples the latent interface at two levels: externally from the agent harness, to measure its contribution to overall performance (RQ1), and internally into realignment compatibility, information accessibility, and propagation dynamics, to identify the benefits and limitations of each (RQ2). Across seven benchmarks with Qwen3 models, adding the latent interface to the same harness does not improve and can even substantially degrade accuracy. Internally, latent representations retain some domain information, but incompatible realignment can substantially degrade performance, and repeated latent steps can amplify representation-level failures. Thus, while latent representations may preserve information, they do not necessarily ensure effective communication, which also requires compatible realignment, information accessibility, and stable propagation.

---


### 53. [SecondChance: Benchmarking Reliable Error Recovery in AI Agents](https://arxiv.org/abs/2611.31586)

**<font color=#1a73e8>作者：</font>** Atahan Dokme, Adar Avsian, Larry Heck  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI agents make errors while they act, and their reliability depends on what they do afterwards. Existing recovery benchmarks mostly inject faults, involve no user and score whether the task is eventually completed, so they cannot show whether an agent undid its own silent error, told the user, or faced an error that could not be fixed. We introduce SecondChance, an error checkpoint dataset and evaluation harness that profiles and measures error-recovery behaviour of AI agents. The errors are natural: they come from agents' own task attempts in $\tau^2$-bench, BFCL and AppWorld. Different agents then resume from the same checkpoints under one of four conditions: no assistance, an error notice, the error location, or repair guidance. We measure error correction, task success, policy compliance, preservation of environment state, repair durability and cost. We evaluate 12 models under all four conditions in 5,760 continuations. Recovery is rare: across its environments, the best model completes only 16% of recoveries unaided and 27% with repair guidance. Correcting is not recovering: with repair guidance, Llama-3.3-70B corrects 26% of $\tau^2$ errors but completes none, and 40 of 84 successful AppWorld continuations leave the error in place. SecondChance exposes these differences that task success alone cannot capture.

---


### 54. [GoldiBench: Right Tools, Wrong Amount -- Benchmarking Agents on Effect Judgement in Professional Editing](https://arxiv.org/abs/2611.31590)

**<font color=#1a73e8>作者：</font>** Wang Yang, Xinpeng Li, Yanyan Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real editing requests describe a look, not the steps to reach it, so an agent that serves them must judge how much of each tool the look takes. Existing benchmarks do not measure this: their tasks either state the tools and values, or leave the amount open and are scored by VLM judges that pass more than half of half- and triple-strength results. We introduce GoldiBench, a benchmark of 500 editing tasks in five professional applications (darktable, RawTherapee, GIMP, Inkscape, Blender), solvable by writing a program or by operating the GUI. Each task pairs a START image with a TARGET rendered from a hidden program, so the amount is fixed by a known target; the agent's edit is re-rendered and compared with TARGET, and the same task is posed with the tools and values, the tools only, or the goal only, separating operation from effect judgement. Across 25 open, GUI and closed models, agents operate well (99-100% with programs from 4B up when told the values) but fall off a cliff when they must judge the amount: given only the tools, the best model passes 19% of the tasks with programs and 33% through the GUI, and scale does not close the gap. Manuals barely help; the measured TARGET-START difference more than doubles the pass rate, but the same difference shown as an image does not for open models. Allowed four renders, agents almost always stop after the first; forced to compare, the strong models double their pass rate. Agents know the tools, but neither read nor check the amount.

---


### 55. [LUCID: Statistically Grounded Self-Correction for LLM Reasoning Evaluation](https://arxiv.org/abs/2611.31595)

**<font color=#1a73e8>作者：</font>** Satiyabooshan Murugaboopathy, Adel Daoud, Connor T. Jerzak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cheap language-model raters grade chain-of-thought reasoning at scale, yet systematic step-rating errors can skew reasoning audits and solution rankings. We introduce LUCID (Loop for Unbiased Calibration via Inference-time Diagnosis), which pairs prompt self-correction with Design-based Supervised Learning (DSL). Without retraining or weight access, LUCID calibrates binary step ratings by aligning predicted and expert soundness rates. From a small expert-labeled set, LUCID summarizes rater bias in plain text and prompts the rater to re-grade unseen steps. For example, on PRM800K, GPT-5-mini grades too strictly, under-rating computation, verification, and late-trace steps most acutely. In one pass, LUCID shrinks GPT-5-mini's calibration gap from 7.8 to 0.9 percentage points in absolute predicted-expert rate difference. LUCID also halves false alarms (sound steps rated unsound) and lifts error-detection F1 on unsound steps by 32%. LUCID retains these gains with 1,000 diagnostic steps or overall-gap feedback alone. The loop also transfers across models and domains: it applies GPT-5-mini's bias profile to lift GLM-5.2's PRM800K accuracy, and it narrows calibration gaps for overly strict but capable raters across math, science, web, and logic benchmarks. Because prompt feedback shifts thresholds without improving class-balanced sound/unsound discrimination, LUCID filters re-grading with pre-/post-checks that skip already calibrated raters and roll back ineffective passes. Finally, we reuse that expert set with raw corpus ratings in DSL for calibration and regression debiasing, and apply DSL to pair-labeled steps for sound-step transitions. DSL's out-of-fold soundness probabilities lift best-of-K selection to match expert labels, while its doubly-robust estimators beat expert-only regression fits at small budgets and cut sound-step transition error by nearly two-thirds.

---


### 56. [Evaluating LLM Security Review Agents with Operationally Sourced Ground Truth](https://arxiv.org/abs/2611.31606)

**<font color=#1a73e8>作者：</font>** Mudita Khurana, Karim Liman-Tinguiri  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based security review agents can reason about vulnerabilities that deterministic tools miss, but deploying them responsibly requires knowing whether they actually work. Existing benchmarks construct ground truth synthetically or from public CVE databases and are blind to the vulnerability patterns specific to a given production codebase. We present an evaluation framework grounded in an organisation's own vulnerabilities, with three contributions. First, a dataset construction methodology that derives ground truth from operational security data (bug bounty reports, penetration test findings and internally reported vulnerabilities), exploiting the property that a confirmed vulnerability must exist immediately before its fix is merged and be absent immediately after. Second, two complementary evaluation strategies: one reviewing the pull request that introduced a vulnerability and one searching a repository where it already exists. Both run through a two-agent pipeline pairing a Security Engineer agent, which reviews code without knowledge of the vulnerability, with a Judge agent that decides whether its findings would have mitigated the known issue. Third, a trace-level behavioural characterisation of how frontier models reason about these vulnerabilities. Across GPT-5.5, Sonnet 4.6 and Opus 4.7, GPT-5.5 shows higher discovery rates on the pull-request strategy (57%, 95% CI [42%, 72%]) after a round of OPRO-style improvements, and Sonnet 4.6 on the repository strategy (69%, 95% CI [56%, 81%]). Trace analysis shows the models have complementary strengths that explain these differences, and that outcome-only scoring can mischaracterise their production behaviour. The methodology relies only on artefacts that vulnerability management workflows commonly produce, though all results come from a single organisation's codebase and we have not tested how well they generalise.

---


### 57. [Monitorable-by-design architectures for a post-Astra world: a compartmentalization-based approach](https://arxiv.org/abs/2611.31610)

**<font color=#1a73e8>作者：</font>** Jake Watts, Joel Sokol  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier models like GPT-6 Astra are increasingly able to do substantial reasoning without a monitorable chain of thought, chains of thought are becoming less legible, and are often monitored asynchronously to reduce cost. With the future of chain of thought monitoring unclear, it may be necessary to design LLMs with monitorability in mind. We propose a modification to existing LLM architectures based on GRAM, SGTM, DEMix, BTS, and similar methods to compartmentalize dangerous capabilities so that their use, especially in combination with dangerous reasoning types that may indicate strategic adversarial use, can be monitored more cheaply than chain of thought in a way that might outlast monitorable chain of thought. We propose several variants of this architecture designed to balance tradeoffs and discuss other benefits, such as capability removal.

---


### 58. [Multi-agent System for Automatic Discovery of Pareto-optimal Meta-solvers for PDEs](https://arxiv.org/abs/2611.31611)

**<font color=#1a73e8>作者：</font>** Youngkyu Lee, Shanqing Liu, Jerome Darbon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing linear solvers for discretized partial differential equations requires problem-specific expertise. We present a multi-agent framework, in which language-model agents propose, critique, implement, and evaluate solver configurations assembled from Krylov methods, preconditioners, block factorizations, and neural operators. Inside the proposing agent, a non-dominated sorting genetic evolutionary algorithm evolves the population of meta-solvers toward the Pareto front of six measured quantities, so that one run returns a front of trade-offs rather than a single tuned solver. The system runs on small open-weight language models served on a single laptop, and we compare it with a single agent on four problems. For three-dimensional acoustic scattering and elasticity, it delivers 47 and 48 convergent hybrid solvers out of 60 candidates. Relative to the Jacobi-preconditioned Krylov baselines, the best of the discovered solvers reduce the iteration counts by factors of 4.7 and 60 and the online solve time by factors of 2.3 and 3.0, whereas the single agent produces no executable plan. For coupled dynamic thermoelasticity in two and three dimensions, where the baselines fail, it completes 98 of 100 transient candidates and, compared with the single agent, reaches a given accuracy 15 times faster in two dimensions and a displacement error 20 times lower in three dimensions.

---


### 59. [Training decision models for simulating human respondents](https://arxiv.org/abs/2611.31613)

**<font color=#1a73e8>作者：</font>** Davood Wadi, Yu Ma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Researchers increasingly use large language models (LLMs) as synthetic respondents in market research, conjoint analysis, and randomized experiments. However, synthetic choice data from off-the-shelf generative LLMs bias downstream econometric inference. Neither proprietary models nor higher reasoning effort reliably reduces this bias. We investigate decision models (System One architectures) for silicon sampling. Using choice training, we update KEV model weights on historical respondent-level choice microdata by conditional maximum likelihood, before inference and without target-study data. Across three model scales, training on two discrete choice experiments lowers treatment-effect error by 22% to 89% on four held-out studies from new domains (vaccines, nutrition labels, consumer rights, and AI) and new response formats. A small choice-trained model outperforms a much larger off-the-shelf model on three of the four studies. Although training on single studies lowers cross-entropy, it can exacerbate treatment-effect error. Choice training thus complements post-inference calibration by providing a stronger starting point for estimating human preferences.

---


### 60. [Eliciting sandbagged LLM capability via structural interventions on attention-head functional networks](https://arxiv.org/abs/2611.31615)

**<font color=#1a73e8>作者：</font>** Manzi Fabrice Niyigaba, Ishan Verma Prasad, Sansheng Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliably evaluating the capabilities of advanced AI systems is critical for safe development and deployment, yet such evaluations may be undermined by sandbagging, a situation in which a model strategically suppresses capabilities it possesses. Existing work has developed controlled sandbagging settings and methods for detecting or eliciting hidden capabilities, but comparatively little is known about how a model's internal neural computation changes when its capabilities are suppressed. In this work, we study sandbagging through the lens of internal functional organization. Inspired by network neuroscience, we construct functional graphs from attention-head activations and compare their organization under honest and sandbagging conditions while holding the model architecture and weights fixed. Surprisingly, across model architectures and community detection methods, we find a consistent structural signature in which sandbagging is associated with reduced functional connectivity within detected communities. We further demonstrate that this reorganization can guide capability elicitation. Ablating attention heads that exhibit the largest connectivity changes substantially recovers suppressed performance while largely preserving performance under honest behavior. Moreover, incorporating these structural signals further improves existing inference-level and weight-level elicitation methods. Together, our results show that sandbagging is accompanied by systematic reorganization of internal computation and demonstrate that functional network structure can provide both a mechanistic lens for understanding capability suppression and a practical signal for recovering hidden capabilities.

---


### 61. [Wavefront: Low-Rank Drafting with Parallel Causal Refinement for Speculative Decoding](https://arxiv.org/abs/2611.31638)

**<font color=#1a73e8>作者：</font>** Huy Huu Nguyen, Xin Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates LLM inference by letting a cheap drafter propose tokens that the target model verifies in parallel. Parallel block drafters such as DFlash and P-EAGLE propose a whole block in one forward pass, but they lose the dependence between tokens in the block; DSpark restores part of it with a lightweight correction head that runs sequentially. Measuring DSpark, we find that this head overrides the base prediction on most slots, so the expensive base readout through the target's full lm_head mostly provides a seed. We therefore propose Wavefront, which follows a simple principle: shrink the base and strengthen the correction head. Wavefront replaces the full lm_head with a learned low-rank base, conditions the correction head on the whole drafted prefix within the same block, and resolves it with a few parallel Jacobi passes. A fixed pass budget makes the draft step free of data-dependent control flow, so we capture it as a single CUDA graph in vLLM with fused kernels. On Qwen3-8B, Wavefront improves throughput over xPress, DSpark and DFlash by 2.6%, 10.7% and 23.6% on average across math, code, chat and agentic benchmarks, and by 9.6%, 14.3% and 28.9% on SPEED-Bench long-context prompts. On Qwen3.8-27B it leads DFlash2, DSpark and xPress by 7.6%, 10.6% and 5.0%, and by 7.4%, 5.8% and 6.0% on the same long-context prompts. The gains persist as serving load grows to concurrency 32.

---


### 62. [BRAG: Bayesian Retrieval Augmented Generation](https://arxiv.org/abs/2611.31656)

**<font color=#1a73e8>作者：</font>** Javier Movellan, Manjot Bilkhu, Young-mok Jung 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) ranks memory chunks by semantic similarity to the query. Many methods improve on this by learning from feedback on what was retrieved, but each is a separate heuristic, with no account of when it is the right choice. We introduce BRAG, a generative model of retrieval with use. Each chunk generates the queries it answers from a mixture of von Mises-Fisher components anchored at its original embedding, and each chunk has a latent utility that drifts over time. The model gives the optimal inference, a closed-form filter that stores a few keys and two scalars per chunk and updates them online from the labels of a curator, and it frames retrieval as a control problem. It also shows when existing methods are optimal. Query averaging, Rocchio-style feedback and frequency reranking are special cases with fixed parameters, NUDGE is the case of one key per chunk with no dynamics, and LADER the limit of one key per past query. On two public long-term memory benchmarks, BRAG matches these methods on queries asked before, as expected, because when nothing changes over time the assumptions behind these special cases hold. On harder problems, where a new chunk makes an old one obsolete, BRAG outscores them. They all stay at plain-search level (Recall@5 0.67-0.71), while BRAG retrieves the new chunk 0.80-0.86 of the time. We also ran BRAG on three of NUDGE's seven text benchmarks, and it matches or beats NUDGE on all three. On nine months of a personal agent's memory (20,640 chunks), BRAG raises Recall@5 on held-out queries from 0.75 to 0.98 and Recall@1 from 0.44 to 0.97, with little change on chunks never queried.

---


### 63. [Provenance Loss and Repair in Multilingual Compaction](https://arxiv.org/abs/2611.31668)

**<font color=#1a73e8>作者：</font>** Ian Miao, Fangrui Zhu, Bowen Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational assistants compact older messages into short notes and evict the originals. When the note's language requires a distinction that English leaves open, such as Spanish adjective gender (agotado vs. agotada), messages that omit or explicitly state that attribute can yield the same note. After eviction, later turns cannot tell them apart: taking the inflected form literally asserts an attribute the user never gave, whereas discounting it as routine grammar discards one the user did give. We propose a training-free repair across writing, pre-eviction verification and reading. The writer marks unstated attributes with paired forms (e.g., agotado/a), a likelihood check before eviction rewrites unsupported single forms into paired ones, and the reader trusts remaining single forms as stated facts. On five Qwen3.5 and Gemma-4 models, eviction cuts recall of stated attributes from 90% to 34% in question answering (QA); our repair raises F1 (which penalizes both errors) on every model, by 9-53 points in QA and 12-40 points in agent handovers.

---


### 64. [Medical Image Segmentation Is Now Just Another Coding Task](https://arxiv.org/abs/2611.31673)

**<font color=#1a73e8>作者：</font>** Shuheng Cao, Ruiqi Chen, Qizhen Lan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For decades, every new medical image segmentation task has needed an expert, a dedicated architecture, and a framework such as nnU-Net. This is no longer the case: medical image segmentation is now just another coding task. Given only a task description, labeled data, and a CPU (with no segmentation framework, no pretrained weights, and no human in the loop), four off-the-shelf coding agents built segmenters for 13 tasks across four imaging modalities within hours, an ability that has emerged rather than been built. On the nine 2D tasks, their best programs reach 99% of the Dice of a GPU-trained nnU-Net. Like any code, a segmenter improves by being revised and checked, so we ask how far the same agents can improve their own segmentations and what unlocks further gains. On unseen cases there is no reference, so the agents inspect renderings of their own predictions: this alone lifts the worst tenth of cases by 0.09 Dice and cuts boundary error (HD95) by almost a quarter. Far more is within reach. Told the true Dice of each attempt, the same agents improve in all 14 matched pairs, rescue 85% of failed masks instead of 30%, and surpass the GPU-trained nnU-Net on average, by producing better masks rather than by choosing among them. What unlocks these gains is a quality signal, which neither visual inspection, nor more rounds, nor a quality estimator trained by the agents themselves yet supplies: we call this the quality blind spot. The ability to build and to repair is already present; the next advance will come not from another segmentation model, but from reference-free quality estimation that coding agents can call.

---


### 65. [Look Before You Commit: Visual-Evidence-Guided Decoding for Multimodal Diffusion Language Models](https://arxiv.org/abs/2611.31677)

**<font color=#1a73e8>作者：</font>** Tongxiao Hu, Yikai Zhao, Qiyan Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion multimodal large language models rely on confidence to decide when to commit candidate tokens during generation. In multimodal tasks, however, confidence cannot distinguish whether a candidate originates from image evidence or the language prior. We perform paired forward ablation and find that nearly nine out of ten high-confidence commits are insensitive to the image, while degenerate and hallucination samples exhibit significant increases in the entropy of deep-layer attention organization. Based on this diagnosis, we propose CD-APC, a training-free decoding method. CD-APC performs evidence-adjusted scoring within a base-supported pool and uses dual gating based on model acceptability and contrastive concentration to decide whether to commit, together with an inverse-window mechanism that adapts to inter-step difficulty. Across two backbones and five benchmarks, CD-APC consistently improves performance, indicating that stable visual evidence improves model outputs.

---


### 66. [LimoBench: How Street Smart Are Large Language Models?](https://arxiv.org/abs/2611.31682)

**<font color=#1a73e8>作者：</font>** Gautam Choudhary, Jack Peng, Udesh Kumarasinghe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have transformed how humans interact with information, enabling natural-language interfaces across various domains. They are increasingly deployed for geospatial applications including map-based question answering, location-based services, and natural-language interfaces to spatial databases. But are LLMs truly location-aware, able to reliably interpret and precisely answer location queries involving real-world coordinates, points of interest (POIs), and geospatial distances? To answer this concretely, we present LimoBench, a street-level benchmark of 82 natural-language location queries over seven canonical spatial operations: geocoding, reverse geocoding, routing, directionality, range search, $k$-nearest-neighbor search, and spatial join. The queries are grounded in real map data of West Lafayette, Indiana, and are graded by location and semantic complexity. They are designed to probe LLMs' street-level spatial awareness, from simple lookups to multi-step spatial reasoning. We also present Limo, an approach based on the Model Context Protocol (MCP) that enhances the location awareness of LLMs. Limo grounds LLMs in PostGIS-backed spatial data through a compact set of tools. We find that ungrounded models mostly achieve single-digit accuracy (3.1% for GPT-6 Luna) across different spatial operations. In contrast, the same models achieve near-perfect accuracy (99.3% for GPT-6 Luna) when given access to Limo's spatial tools through MCP. Current LLMs thus have limited and unreliable street-level spatial knowledge, while grounding provides accurate answers at modest overhead (+0.2 s latency, 7.7$\times$ tokens, and 2.2$\times$ cost for GPT-6 Luna). We release the benchmark, Limo toolset, and evaluation code to encourage the community to evaluate their own location-aware LLM approaches.

---


### 67. [Right Destination, Wrong Journey: Synthetic Counseling Dialogues Miss Human Interactional Dynamics](https://arxiv.org/abs/2611.31686)

**<font color=#1a73e8>作者：</font>** Ziwei Gong, Yuchen Huang, Nicholas Deas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-generated counseling dialogues are increasingly used for training and evaluating mental-health systems, yet existing evaluations focus largely on response quality and final outcomes rather than how support unfolds over time. We conduct a trajectory-centered evaluation of process fidelity across ten human, reconstructed, and synthetic counseling datasets. Our results show that synthetic dialogues often reach plausible endpoints but differ from human support in recovery dynamics and turn-by-turn responsiveness. While generation design can shift global properties such as recovery timing and trajectory structure, contingent patient--counselor responsiveness remains consistently lower in fidelity across models and generation paradigms. Our experiments on controlled synthetic datasets show that targeted generation interventions can narrow the gap with real data on several trajectory-level measures, but do not fully recover interactional fidelity, with turn-level responsiveness remaining limited. We release three controlled synthetic datasets comprising 2,050 dialogues, together with annotations and the evaluation framework.

---


### 68. [E-Waste-Bench: A Large-Scale Benchmark for Visual Triage of Data-Center Hardware](https://arxiv.org/abs/2611.31703)

**<font color=#1a73e8>作者：</font>** Nader Lobandi, Mohammad Mehdi Hosseini, Lombe Chileshe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retired data-center hardware can often be refurbished or resold, but triage demands more than object categories. A model must tell visually similar parts apart, judge condition under damage and occlusion, and read the printed part number. We audit nine public e-waste collections. They cover mostly consumer devices (only 10% of images are labeled as a data-center part), label neither condition nor printed text, and contain 42% exact or augmented duplicates. We introduce E-Waste-Bench, 328K photographs drawn from 762K deduplicated images and labeled for class (24 classes), granularity, condition and printed text. Images come from those collections and the web, where a recipe-based crawler works beside an agent built on an open-weight vision-language model. The agent vets new sources and reads sites the crawler cannot parse, and both are steered toward under-represented classes. Training labels are model-made, splits follow near-duplicate groups, and human annotators label a test set of nearly 10,000 images. We benchmark classification, condition, detection, text perception and cross-dataset transfer. On this test set, a ConvNeXt-T trained on E-Waste-Bench reaches 64.3% top-1, against 31.5% with the public collections alone. Near-duplicate leakage inflates top-1 by 3.0 points under model-made test labels but by less than 0.1 under human labels, so model-labeled benchmarks need group splits. Accuracy falls to 42.1% on marketplace and auction photographs, the closest proxy for hardware leaving service. Data and code will be released.

---


### 69. [NOBODY Was There: Bridging the Human-VLM Gap in Unwarranted Person Attribution Bias](https://arxiv.org/abs/2611.31714)

**<font color=#1a73e8>作者：</font>** Parsa Madinei, Ziqi Wen, Miguel Eckstein  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Describing an image requires not only recognizing what is visible but deciding what should be inferred. We investigate a systematic gap between humans and VLMs in their tendency to attribute visible actions or events to people who are not present in an image. We term this behavior unwarranted person attribution bias and find that, across 25 SOTA VLMs, captions of person-absent scenes mention a person four times as often as human-written captions of the same images. Through a preference study, we further show that both humans and VLMs prefer captions that avoid such attributions. Motivated by this, we introduce NOBODY, a preference dataset designed to bridge the gap between humans and VLMs in unwarranted person attribution. Through direct preference optimization (DPO), we align open VLMs on NOBODY and show that their agreement with human captions on person attribution reaches or exceeds inter-human agreement, whereas nine existing public preference datasets leave this behavior largely unchanged. Furthermore, we show that human judges preferred the aligned VLM captions significantly more than those of the baseline model. Alongside NOBODY, we release NOBODY-Bench, which evaluates VLMs for unwarranted person attribution bias and their alignment against human captions and preference. Project page: this https URL

---


### 70. [fork() for Agents: Agent Kernel for Non-blocking LLM Orchestration](https://arxiv.org/abs/2611.31727)

**<font color=#1a73e8>作者：</font>** Ankit Chadha, Pratyay Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based agents typically execute tool calls synchronously and discard completed work upon failure. Subgraph-selective recovery, re-executing only a failed node's transitive descendants, is a well-established pattern in distributed systems (Spark, Erlang/OTP, Dryad), and recent agent runtimes (Sherlock, AgentGit, Atomix) preserve completed work through verifiers, version control, or transactional tool boundaries. We present \textbf{Agent-Kernel}, a non-blocking runtime that ports this pattern to the LLM \emph{content plane}: its primitive, \textbf{Sub-Graph Recovery (SGR)}, fires on a raw exception with no trained verifier or planner, resets a failed node's descendants while preserving completed siblings, and composes each parent's text into its children's prompts (context inheritance), all on a durable substrate with a formal state-preservation guarantee. Across 14{,}434 runs on synthetic and standard benchmarks (tau-bench, Gaia2, AutomationBench, InterruptBench), SGR reaches full recovery within budget=3 where whole-trajectory replay exhausts (100\% vs.\ 55\%), and is roughly 10$\times$ faster than an adapted Sherlock rollback that also recovers. It matches ReAct-serial accuracy within noise on linear workloads while adding recovery and parallelism (up to 12.7$\times$ speedup) where structure permits. Ablation isolates SGR: removing it collapses success to 39.4\%.

---


### 71. [BEARING: Who Is Talking to Whom? Grounding Acoustic Direction in Vision for Online Multi-Party Conversation](https://arxiv.org/abs/2611.31735)

**<font color=#1a73e8>作者：</font>** Nader Lobandi, Lombe Chileshe, Mohammad Mehdi Hosseini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding a group conversation means deciding, from video and audio, who is speaking and to whom. Leading systems treat these tasks offline on single-channel clips and align models with a self-evaluation reward. We propose BEARING, a geometry-first alternative built on one measured signal: the direction from which a microphone array beside the camera hears a sound. A label-free calibration learned from the stream registers this direction into the camera image, and an online registry of faces, voices and directions needs no enrollment. The registered direction serves as (i) a visual prompt for a vision-language model, a marker on the speaker or an arrow toward an off-screen source; (ii) one input of a reliability-weighted fusion with visual active-speaker detection, for speakers in the same direction from the array; and (iii) a verifiable reward for alignment: the named speaker must sit where the sound comes from, the confidence must match that check, and always answering "group" earns nothing. Every decision is online, with the lookahead as an explicit parameter. On 9,498 addressee-labelled utterances from three AMI sites and egocentric EasyCom, the direction prompt raises speaker accuracy from 54% to 74%; addressee accuracy moves by about two points, because telling one addressee from the group depends on the words more than on where people are. For co-located speakers on AVDIAR, visual active-speaker detection holds 95% where direction alone falls to 59%. The verifiable reward beats self-evaluation under GRPO, reward-ranked fine-tuning and DPO; shrinking the lookahead from 5 s to 0.5 s costs 4.5 DER points on AMI, and learning the registration online costs a dip in the first two minutes before the system overtakes vision alone. Code and evaluation protocols will be released.

---


### 72. [Reproducing History Is Not Enough: Intervention-Level Assurance for LLM-Generated Simulators](https://arxiv.org/abs/2611.31736)

**<font color=#1a73e8>作者：</font>** Ashraf Abdul-Muumin, Aniruddha Chattopadhyay, Noorbakhsh Golilarz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can now write simulation programs of operational processes and workflows. These programs can be reused to answer what-if questions on new records and policies. However, a program that reproduces recorded history can still give wrong answers to what-if questions; requested changes may be applied wrongly, or they may be applied to records other than the ones the question is about, or the program may stop being valid once its policy is revised. Current checks return a pass-or-fail verdict for the whole program, which says little about whether any single answer can be trusted. We propose Vouch, a library that judges whether an answer from a generated simulator can be trusted for the change being asked about. Each what-if question is turned into a structured change, which is checked against the program and the current records. The library also keeps a record of the kinds of change each program has passed or failed, and repeats the relevant tests whenever the program is reused. We apply it to three program-generation platforms, with programs built by five language models, across four domains: manufacturing, IT operations, and pharmacy and loan-application workflows, using independently checked reference answers. Our baselines are the platforms' own checks where such checks exist, an LLM-as-a-judge, and a ReAct agent that can run the program. We measure how many correct answers are trusted, how many are wrongly rejected, how many wrong answers are accepted, and what the checking costs.
On programs written by Haiku and Sonnet in one platform, Vouch removes 97.6% of the wrong answers, while still trusting 80.1% of all answers. At equal coverage, it accepts fewer wrong answers than LLM judges built on Claude Haiku. We disclose code and results for reproducibility.

---


### 73. [GreenDynaMix: Thermal-Aware Dynamic Mixed-Precision MoE LLM Inference Systems](https://arxiv.org/abs/2611.31737)

**<font color=#1a73e8>作者：</font>** Han-Yi Lin, Kieran Griperay, Qiang Zhou 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sustained Large Language Model (LLM) inference generates significant heat that exacerbates silicon aging and reduces GPU reliability. Because GPU temperature fluctuates continuously with workload intensity and ambient conditions, keeping it in a safe range requires real-time frequency scaling, which inevitably comes at the cost of either throughput or accuracy. To address this tightly coupled challenge, we propose GreenDynaMix, the first runtime system to jointly integrate a DVFS-based thermal manager with a dynamic precision-tuning throughput compensator. A sensitivity-aware allocator leverages intrinsic importance signals from the Mixture-of-Experts (MoE) router to assign higher precision to critical experts, preserving accuracy. Experiments on server, desktop, and embedded platforms demonstrate that GreenDynaMix reduces the temperature-induced aging rate of GPUs during LLM inference by 25-33%. Without offline profiling or model retraining, it recovers throughput at a perplexity cost of 0.9-1.6% with 8-bit/4-bit mixed precision, rising to 9.4% where memory forces 4-bit/2-bit.

---


### 74. [LeanWAM: Learning Latent World Action Models from Frozen Video Models](https://arxiv.org/abs/2611.31740)

**<font color=#1a73e8>作者：</font>** Shaolong Li, Hongze Fu, Joyce Chai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) typically adapt large pretrained video generators to jointly predict future observations and robot actions, incurring substantial training and deployment costs. However, it remains unclear which future representations a policy actually needs and how compactly they can be represented. Our probing study shows that complementary future representations can be compressed into a few tokens while retaining most of their action-decoding performance. Motivated by this finding, we introduce LeanWAM, a latent WAM that transfers video priors from a frozen video generator to a lightweight policy via two-stage training. In the first stage, a Future Extractor compresses observed transitions into 32 predictive tokens. These tokens condition the frozen generator and are jointly shaped by action, RGB, semantic, and geometric supervision, while a compact readout of the generator's hidden states supplies complementary world tokens. The second stage distills both representations into the policy, which learns to predict them from current observations while generating actions. With 1.4B parameters and no large-scale embodied pretraining, LeanWAM outperforms strong vision-language-action (VLA) and WAM baselines on LIBERO, LIBERO-Plus, and RoboTwin~2.0. It predicts an action chunk in 25.1\,ms on an A100 GPU, 12.3--41.5$\times$ faster than representative WAMs. These results demonstrate that compact predictive supervision can transfer video priors to robust and efficient control.

---


### 75. [Mixed-Initiative Mining of Root-Cause Analyses into Audit Priors for C/C++ Vulnerability Hunting](https://arxiv.org/abs/2611.31744)

**<font color=#1a73e8>作者：</font>** Yuhei Kawakoya, Eitaro Shioji, Yuto Otsuki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vulnerability auditing of large C/C++ codebases is constrained by limited review attention. Human auditors and LLM-based agents need operational priors that indicate where to look first and what to suspect, but such priors are rarely available in directly usable form. Rather than proposing a new vulnerability detector, we derive audit-steering artifacts from evidence-backed root-cause analysis (RCA) reports.
We introduce two complementary representations: Occurrence Context (OC), a location prior based on file role, function role, and data-structure class; and Vulnerability-Inducing Structural Patterns (VISP), reusable failure-mechanism priors. OC guides where to inspect, while VISP guides what to suspect.
On 108 CVEs from Vul4C, OC's parser-based priority ranking, without LLM inference, outperforms generic prioritization baselines with moderate-to-large effect sizes. Packaged as executable SKILLs, OC and VISP form a dual-SKILL workflow that improves audit-relevant broad coverage, defined as match-or-partial findings within ground-truth functions that share the patch's failure mechanism, as assessed by three LLM judges. Across the 108-CVE cohort, dual-SKILL improves function-level broad matches by 5.3 percentage points; gains reach 7.2 points on mid-size projects and 15.0 points on large (1500-4999-line) vulnerable files. These results suggest that RCA-derived priors help direct limited audit attention toward vulnerable code. The agent-coverage evaluation is a single-run operational probe, with one run per commit, characterizing the direction and scale of the effect rather than its precise magnitude.

---


### 76. [FN-Prune: Training-Free Expert Pruning with Finite RMSNorm Perturbations](https://arxiv.org/abs/2611.31747)

**<font color=#1a73e8>作者：</font>** Zeyan Li, Jianfeng Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Expert pruning reduces the memory footprint of mixture-of-experts language models, but retaining model quality depends on which experts are removed. Frequency- and magnitude-based scores measure the expert in isolation and overlook how normalization consumes its contribution: subtracting one expert changes both the direction of the residual stream and the scale applied to what remains. We propose FN-Prune, a training-free criterion that compares the next RMSNorm outputs before and after subtracting each router-weighted expert contribution, holding original routes and weights fixed. Squared differences are averaged over all calibration tokens in one pass; low-scoring experts are physically deleted at uniform per-layer ratios, and inference reroutes among survivors. At 50% expert removal, FN-Prune achieves lower WikiText-2 perplexity than the best published methods on Qwen3, ERNIE, and OLMoE, including a 32% reduction on OLMoE. At the same budget, GSM8K accuracy improves over the best published methods by 7.5 and 7.0 percentage points on Qwen3 and ERNIE, respectively, while multiple-choice gains remain task-dependent.

---


### 77. [Separating Measurement Failures from Defence Failures in Split Language-Model Privacy](https://arxiv.org/abs/2611.31752)

**<font color=#1a73e8>作者：</font>** Georgios Politis, Evangelos Pappas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Split-training privacy evaluations fail through distinct mechanisms. Evaluators can overlook an exposed gradient channel, align reconstructions against shifted labels, or deploy uncalibrated probes before testing a candidate defence, while calibrated attacks can also refute real defences. Separating these failure modes alters which claims survive. We conduct a retrospective evidentiary reanalysis across four split-LLM campaigns and two cross-cutting scope checks covering host key custody and variational mutual-information bounds, mapping every recorded claim to one of five admissibility states (breach, non-detection, undetermined coverage, invalid measurement, or out-of-scope inference). Across a 19-configuration exploration, only four of 24 required probes qualified, yet those four calibrated probes still established qualified privacy breaches in 13 configurations, while utility or learning-gain failures eliminated the remaining 6. In a seven-cell defence-redesign pilot, 2 quantised configurations failed utility gates, calibrated next-byte structure probes breached the 0.02 gate on all 7 cells (0.097 to 0.112), and qualified punctuation-property probes reached 0.79 to 0.89, yielding 4 failed and 3 undetermined composite privacy assessments (the latter from marginal null-band excursions on punctuation bindings). Negative evidence against both defence families remains intact. Scope checks further show that shared-key orthogonal wrappers protect passive network captures without hiding activations from a compromised restoring host, and why near-zero variational lower bounds leave worst-case leakage unconstrained. Rerunnable scripts verify 1,522 checks across 122 SHA-256-pinned artifacts while preserving each campaign's native seed intervals and retrospective boundaries.

---


### 78. [RVLM-X: Towards a Universal VLM Harness](https://arxiv.org/abs/2611.31755)

**<font color=#1a73e8>作者：</font>** Aadi Palnitkar, Dmytro Kurdydyk, Xiaomin Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Harnesses for vision-language models (VLMs) have grown with the models' capabilities, notably for images far larger than those seen in training, where downscaling loses small details. Most of them wrap the VLM in a fixed procedure, such as a zoom tree, that decides in advance where it looks and how the evidence is combined. These procedures make up for the weaknesses of older models by keeping them on a task-specific path, but with frontier models that reliably plan and use tools, they can lower accuracy. We propose RVLM-X, a task-generalizable recursive VLM harness that runs unchanged across photographs, charts and maps. Following the recursive inference of Recursive Language Models, the VLM programmatically controls its own visual context in a code REPL that holds the full-resolution image and calls itself recursively on regions that it chooses. With a cost-efficient frontier model as the base of every method, RVLM-X is more accurate than a single call on all 7 public benchmarks and has the highest pooled accuracy. Because existing benchmarks mostly test whether a model finds one small detail, we also introduce MapGenBench, procedurally generated maps whose questions combine fine-detail perception with multi-step reasoning. There, RVLM-X answers 71.4% of held-out questions against 55.5% for the strongest baseline. Overall, our findings suggest that as VLMs plan and use tools more reliably, letting the model write its own visual search works better than fixing one in advance.

---


### 79. [Verified Proof Refactoring with Codex and Qwen](https://arxiv.org/abs/2611.31762)

**<font color=#1a73e8>作者：</font>** Lazar Milikic, Gordan Đurić, Viktor Kunčak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We refactor existing Lean 4 proofs to reduce source length and checking cost while preserving theorem statements and compatibility across Lean versions. A locally served Qwen model uses the open-source Codex CLI to inspect source, retrieve declarations, and test proof replacements. The host keeps a replacement only if it improves the objective and Lean accepts it on every required version. A deterministic CPU pass then refines the verified proofs. On the 60 problems in Lean Refactor Arena, model search achieves a local mean combined score of 82.07, and cleanup raises it to 82.18. The final proofs pass all 127 required proof--version checks. Our system placed first in the open-source LLM track of Lean Refactor Arena at VeriCodeGen.

---


### 80. [Dreamcatcher: Remembering What Surprises a World Model in Video Streams](https://arxiv.org/abs/2611.31765)

**<font color=#1a73e8>作者：</font>** Jinxi He, Ce Zhang, Wenhe Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As live video streams grow longer, repeatedly encoding and processing their full histories becomes increasingly costly. Answering questions as they arrive therefore calls for visual memory built in one pass before future questions are known. Existing methods mainly keep tokens that differ from earlier ones or match surrogate queries fixed in advance. Without modeling world dynamics, these criteria struggle to tell subtle surprising details from expected change. We introduce Dreamcatcher, a training-free framework and, to our knowledge, the first to use predictive signals from an independently pretrained, frozen video world model for online memory formation in streaming video question answering. Conditioned on recent history, the world model predicts incoming features using learned world priors. Its normalized prediction errors yield temporal and spatial surprisal signals that guide online segmentation and the retention of a frozen Video-LLM's native visual tokens, balancing surprising details with broad visual coverage under budgets that decay with segment age. At query time, an evidence gate admits a segment from a similarity-based shortlist only when the Video-LLM judges that it adds evidence for the question beyond the current view. We evaluate Dreamcatcher on three streaming and three offline long-video benchmarks. On OVO-Bench, Dreamcatcher achieves the highest overall accuracy among the compared training-free methods for each of four frozen Video-LLMs, reaching 78.9% with Qwen3.8-27B. With the three Qwen Video-LLMs, it also reduces average input tokens for answer generation by more than 80% relative to their base models at 1 fps.

---


### 81. [SPARQL-Planned Single-Hop Traversal over a Live Knowledge Graph for Multi-Hop Question Answering](https://arxiv.org/abs/2611.31771)

**<font color=#1a73e8>作者：</font>** Priyesh Vakharia, Masud Moshtaghi, Pratyay Banerjee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic retrieval struggles with multi-hop question answering on both recall and precision: gold passages are buried among distractors that degrade the reader's answer, and retrieving them requires reasoning over the query rather than matching it. GraphRAG techniques expand semantic retrieval by connecting passages to graph nodes and performing one or more hops of expansion after initial retrieval. This improves recall, but multi-hop expansion becomes expensive and brings additional noise into the retrieved set. We break this tradeoff by \emph{interleaving} dense retrieval with knowledge-graph traversal for complex multi-hop questions. Dense retrieval locates the first relevant regions of the search space at good recall, while traversal of a pre-existing external KG (Wikidata) restores precision and improves recall by confirming retrieved passages against a reasoning path through the KG. To keep traversal both question-adaptive and reliable, we have an LLM plan it as code generation task for graph traversal in SPARQL format but \emph{parse rather than execute} the query. On full 1{,}000-question splits under a shared corpus and reader, and with a single configuration applied identically to every dataset, we reach \textbf{62.5 / 75.1} EM/F1 on HotpotQA, \textbf{73.5 / 81.0} on 2WikiMultiHopQA, and \textbf{37.1 / 50.0} on MuSiQue, ahead of reproduced HippoRAG2, T\textsuperscript{2}RAG, and IRCoT on all three benchmarks. A second, token-matched setting stays ahead of T\textsuperscript{2}RAG on HotpotQA and 2Wiki while spending roughly its per-query budget. Executing the generated SPARQL instead of parsing it costs up to 11.4 EM, mostly because raw queries return empty results, not because of syntax errors.

---


### 82. [BODYBENCH: Evaluating Adversarial Image Defenses Against AI Nudification Inpainting](https://arxiv.org/abs/2611.31774)

**<font color=#1a73e8>作者：</font>** Li Qiwei, Salma Abdel Magid, Olga Russakovsky 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial perturbation defenses protect images from unauthorized edits by adding imperceptible noise. Yet none of these methods have been evaluated against nudification, despite AI-generated non-consensual intimate imagery (AIG-NCII) being among the most documented harms of generative AI. Moreover, nudification edits are readily carried out through inpainting, the primary setting these protection methods are designed to defend against. We argue this is a problem-formulation failure since prior threat models do not correspond to nudification edits (also called attacks). The misalignment of existing approaches is structural, spanning mask shape, training and testing prompt distributions, and success criterion which causes existing evaluations to systematically overestimate protection effectiveness. We reformulate image protection against unauthorized editing around this documented harm. We introduce BODYBENCH, a benchmark of 648 fully synthetic clothed adult subjects, each paired with 11 mask variants spanning body, face, and context regions. We propose three harm-aligned metrics: sexualization, naturalness, and recognizability that jointly determine whether an inpainted output constitutes a successful nudification attack. Auditing four recent protection methods (PhotoGuard, DiffusionGuard, AdvPaint, DiffVax) on BODYBENCH, we find that protection succeeds in only one configuration of one method, and only under exact mask alignment between defender and attacker---a condition no real defender can guarantee and one that we show is easily always bypassed. We also show that standard evaluation metrics such as peak signal-to-noise ratio (PSNR) are essentially uncorrelated with nudification protection. BODYBENCH makes this misalignment measurable and provides a foundation for defenses grounded in documented harm.

---


### 83. [VISOR: A Vision-Language Selector for Multimodal Time-Series Forecasting](https://arxiv.org/abs/2611.31780)

**<font color=#1a73e8>作者：</font>** Seunghan Lee, Jun Seo, Junhyeok Kang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent time-series foundation models (TSFMs) forecast a distribution over futures, and multimodal time-series (TS) forecasting further exploits other modalities to improve forecasting accuracy. However, existing works have two limitations: 1) TSFMs reduce the predictive distribution to its median or mean, flattening diverse futures into a calm line, and 2) multimodal TS forecasting models incorporate text into the forecaster through TS-language alignment, which is substantially weaker than vision-language alignment. To address these limitations, we propose the VIsion-language SelectOR (VISOR), a multimodal TS forecasting framework that selects one plausible future instead of averaging across candidates, leveraging the alignment capabilities of vision-language models (VLMs) to select the most suitable candidate based on textual information. VISOR consists of two components: 1) a text-free stochastic predictor that samples diverse candidate futures, and 2) a VLM selector that reads the candidates as a single chart image and selects one based on the text. To avoid overly calm forecasting paths, we train the selector with a shape-aware target that evaluates each candidate based on both point-wise error and path shape. Across three benchmarks covering ten datasets, VISOR achieves the best average ranking in both point and volatility errors compared with TSFMs and multimodal TS forecasting models. Code: this https URL.

---


### 84. [SciFig2Data: A Workflow for Recovering Structured Data from Scientific Figures](https://arxiv.org/abs/2611.31787)

**<font color=#1a73e8>作者：</font>** Xinhe Wu, Yicheng Ye, Yadong Jin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific measurements reported in scholarly articles are often embedded in compound figures rather than available as machine-readable data. Recovering these measurements at literature scale requires an integrated workflow for figure localization, panel decomposition, chart identification, numerical reconstruction, and experimental context association. We present \textit{SciFig2Data}, an automated, high-throughput workflow for harvesting structured experimental data from scientific PDF repositories. The system integrates multi-scale document element detection, adaptive compound figure decomposition, two-stage OCR-based semantic filtering, Swin-based chart classification, and instruction-guided multimodal large language model (MLLM) reconstruction. It further incorporates directory-level batch execution, caching, and structured logging to support large-scale processing. We demonstrate the workflow on two biomedical literature corpora comprising 605 toxicology and pharmacology articles and 551 lipid nanoparticle (LNP) articles. The pipeline successfully reconstructed 468 and 242 tabular outputs from the respective corpora, illustrating its practical applicability to literature-scale scientific data harvesting. By associating reconstructed measurements with caption-derived experimental metadata, SciFig2Data provides a workflow for transforming graphical evidence in scholarly publications into structured, context-enriched data records for downstream AI4Science applications.

---


### 85. [SwarmLeak: Does Coordination Improve Privacy Attacks on LLM Agents?](https://arxiv.org/abs/2611.31791)

**<font color=#1a73e8>作者：</font>** Asma Farajidizaji, Vyas Raina, Vatsal Raina 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly collaborate in group chats while holding tool access to confidential records, which makes the shared chat an attack surface. It remains unclear whether several colluding attackers extract such information more effectively than one. We introduce SwarmLeak, a red-teaming dataset of 24 synthetic group-chat scenarios across healthcare, law, finance, and software engineering, where attackers pose as colleagues to make a victim agent post protected fields despite an explicit confidentiality policy. With GLM 5.2 attacking five victim models through seven conversational strategies, we compare one attacker with a swarm of four sharing a private channel, matching scenarios, strategies, and a 200,000-token budget that also covers swarm coordination. Swarms show no advantage: a single attacker matches or exceeds them on every victim, and the share of runs leaking any field differs between conditions by at most 14.3 percentage points, whereas changing the victim shifts it from 0% to 99.4%. On the two most vulnerable models, nearly every run leaks under both conditions, but single attackers expose more of the record at first disclosure (85.4% vs. 68.1% of protected fields on Nemotron 3.5 Lightning). Four of the five victims leaked despite the policy. GLM 5.2 retrieved protected data in 64.3% of individual-attack runs and leaked in 0.6%: retrieval does not imply disclosure, but in high-stakes settings even one leaked field can identify a patient or client. At equal budgets, a larger red team is not automatically a stronger one; the victim model matters far more.

---


### 86. [AGL-SKILL: Coding Harnesses as Agentic Optimizers](https://arxiv.org/abs/2611.31794)

**<font color=#1a73e8>作者：</font>** Ryan Tsui, Yuge Zhang, Yuqing Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier models are increasingly used through harnesses as agents, with growing autonomy to do useful work. Agent performance can often be enhanced by the use of skills: reusable workflows, code, and prompts that provide task-related information or guide the behaviour of the model. Skills, being textual in nature, present themselves as another editable surface to be optimized; current methods have improved on handcrafting and one-shot generation by treating skill development as an iterative process, using score-driven search to tweak and improve performance. In this paper, we demonstrate the efficacy of the agents themselves as optimizers: across five benchmarks, a coding agent without guidance substantially improves every target and outperforms published skill-optimization methods. More broadly, this shows the capability of agents to do such work and to refine their own behaviour to provide task-specific context, as long as they are given a metric to measure against.

---


### 87. [A Generative AI Agent to Emulate Interactive Human-driven Vehicles for Automated Driving Testing in Urban Areas](https://arxiv.org/abs/2611.31797)

**<font color=#1a73e8>作者：</font>** Jia Hu, Changjian Yu, Panqu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Realistic modeling of human-driven vehicle (HDV) interactions is essential for automated driving safety testing in urban areas. Existing methods struggle to reproduce realistic safety-critical interactions involving high collision risk for the following reasons: they often assume full observability, overlooking interactions arising from occlusion. Driving styles are mainly characterized by vehicle maneuvers, limiting the diversity of safety-critical interaction behaviors. Moreover, learning signals from safety-critical interactions can be diluted by non-critical driving behaviors. To address these issues, we propose a generative AI agent to emulate interactive HDVs. The agent incorporates field-of-view modeling to account for driver visibility under occlusion and characterizes the interaction process using five metrics spanning its initial, intermediate, and final stages. It automatically learns diverse interaction styles through a dynamic mixture-of-experts network. Through residual reinforcement learning, the agent further refines generated trajectories to match the real-world distributions of safety-critical interaction characteristics. Experiments on the INTERACTION dataset show that our method reduces Jensen--Shannon divergence (JSD) by 39.9\%--87.1\% across five interaction characteristics compared with a state-of-the-art baseline. Our method achieves greater improvements of up to 87.1\% in final-stage interaction metrics, suggesting that it can reduce error accumulation in long-horizon trajectory generation. Ablation studies confirm the effectiveness of each proposed component, particularly highlighting the importance of residual refinement. Generalization experiments show that our method approaches the performance of full training on unseen intersections with only one epoch of fine-tuning.

---


### 88. [Learning Compact State Abstractions for LLM Agents](https://arxiv.org/abs/2611.31800)

**<font color=#1a73e8>作者：</font>** Yaswanth Chittepu, Raghavendra Addanki, Anup Rao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents commonly use the full interaction history as a proxy for state, retaining all past observations and actions regardless of whether they remain relevant. We instead ask what information an agent actually needs to carry forward. We define agent state as a compact abstraction of interaction history that preserves the competence of a fixed reference agent, with the minimal such abstraction as the ideal. Because matching the reference agent's behavior is unnecessarily restrictive and difficult for black-box policies, we define sufficiency through task performance rather than behavior matching. We represent state abstractions as deterministic recursive programs and search over them using an LLM-guided genetic algorithm. Across ALFWorld and ScienceWorld, the learned abstractions preserve near-reference task success while reducing mean policy input by up to 71% and 57%, respectively. The resulting programs are directly inspectable, providing an explicit account of what information is retained, updated, and discarded during interaction.

---


### 89. [Where Did My Tokens Go? Verifiable Token Billing for LLM Services](https://arxiv.org/abs/2611.31806)

**<font color=#1a73e8>作者：</font>** Jiayuan Du, Yebo Feng, Lin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Users of large language model (LLM) services receive token bills with limited evidence of which calls incurred their charges. In broker-mediated agent workflows, calls arise after authorization and billing evidence spans service domains. A bill can count one genuine receipt twice and omit another. Valid metering evidence can also be attributed to the wrong execution. We present \textsc{TokenProv}, which uses authenticated provider acceptances to establish settlement coverage and verify token charges. An authenticated causal history links runtime attempts to the signed policy, and jointly signed handoffs bind intent, dispatch, and acceptance to the same call. Handoffs submitted independently of the bill can reveal omitted calls. The auditor requires a one-to-one match between observable acceptances and settled receipts. For each acceptance, a common provider relation binds metered usage to the cache-dependent execution of the accepted input using the registered model and serving rules, and checks the charge under the pricing rule. To limit serving-path overhead, providers can use attested state transitions in trusted execution environments or defer proof generation until audit by committing to witnesses in receipts before settlement. The auditor recomputes the bill from the verified charges. We prove audit soundness relative to authenticated evidence. Across five models, \textsc{TokenProv} with signed provider receipts achieves 94.4--107.4\% of baseline throughput with 54--66\,ms of online non-LLM processing per request. In a separate eight-call replay, deferring scoped proofs reduces foreground protocol time from 1.20\,s to 8.65\,ms (99.28\%). The auditor rejects all 1,600 validly signed attack queries across 100 adaptive episodes.

---


### 90. [Agentic Discovery of Soundness Bugs in Safe Rust Bindings](https://arxiv.org/abs/2611.31813)

**<font color=#1a73e8>作者：</font>** Marius Momeu, Koushik Sen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Rust crates confine unsafe code, such as calls into C or C++ libraries or system calls, behind safe interfaces that must uphold Rust's invariants. If an interface encodes one rule of the code beneath it too weakly, a program written in purely safe Rust can cause undefined behavior. Static analyzers and fuzzers are bound to fixed patterns or to the paths they execute. We propose LLM agents as auditors of these interfaces, and study how well they do it.
We first define a taxonomy of the defects of such interfaces, including undefined behavior, divergences from the wrapped library, and incomplete unsafe contracts. We then measure, in repeated audits of a real-world crate by a closed and an open model, Claude Opus 5.5 and DeepSeek V4.1 Flash, which defect classes agents find, how well they triage them, and what makes them find more. Agents find the first two classes unprompted, but find few incomplete contracts even when asked. Their findings are almost always real, even without an independent reviewer, yet they lack triage discipline: they seldom confirm with a sanitizer, and they stop early. With the same guidance, the open model finds as many defects as the closed one at a quarter of the cost.
We integrate these insights in Crustify, an agentic system for automating C-to-Rust tasks, and run it at scale. In 16 widely used crates, including the bindings to the C libraries OpenSSL, SQLite, libgit2, and libcurl and to the C++ engine V8, Crustify found 225 undefined-behavior bugs, 23 behavioral divergences, and 36 incomplete unsafe contracts, between 3 and 61 per crate at a median cost under $50 per audit. In the Linux kernel's Rust abstractions, it found 11 more undefined-behavior bugs and 4 incomplete contracts. Maintainers have fixed 26 of the 83 findings that we reported.

---


### 91. [Exploring Multi-Player Social Games as Verifiable Training Grounds for Large Language Models](https://arxiv.org/abs/2611.31821)

**<font color=#1a73e8>作者：</font>** Keyu He, Michael Li, Jiarui Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The training of socially intelligent language models often relies on large language model (LLM) judges, which are expensive, noisy, and vulnerable to reward hacking. Multi-player social games offer a natural alternative: they require open-ended communication to coordinate with teammates and infer hidden roles, while their rules provide an objective outcome which can serve as a verifiable reward for training. Using three social games, we explore how much social intelligence Qwen3 models can acquire through supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR). Results show that against a much stronger Gemma-3-27B model, SFT and RLVR raise the win rate of Qwen3-4B from 33% to 81% on the three trained games, and from 39% to 54% on three additional held-out games. In contrast, in-context strategies such as prompting improve the win rate of Qwen3-4B by only about 6 pp across the same games we train and evaluate on. Furthermore, we show that the gains from SFT and RLVR hold across the model sizes 1.7B, 4B, and 32B. Qualitative analyses of agent behavior show signs of stronger social intelligence; for example, trained agents tend to share information more openly, check each other's claims against public evidence, and coordinate their votes. More broadly, our results demonstrate that training LLMs on verifiable outcomes in social games can cultivate generalizable social behaviors, which offers a scalable path for building socially intelligent agents.

---


### 92. [GaokaoMathGen: Chinese Gaokao Mathematics Finale Problem Generation Controlled by Latent Reasoning Structures](https://arxiv.org/abs/2611.31823)

**<font color=#1a73e8>作者：</font>** Qian Chen, Kun Zhu, Zhongyi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating Chinese Gaokao mathematics finale problems requires controlling not only the included skills, but also the underlying mathematical kernel and solution path. Existing LLM-based methods mainly rely on surface-level specifications, while the realized difficulty of generated problems cannot be determined directly from prompted targets. Therefore, we propose GaokaoMathGen, a framework for Chinese Gaokao mathematics finale problem generation controlled by latent reasoning structures. It extracts standardized latent reasoning structures from seed problems and performs constrained synthesis using skills, methods, a core identity, and a pivot step as structural controls. We further estimate realized difficulty through logical-quality filtering, fixed-solver decoding effort, structural features, and solver-output search signals. Experiments show that semantic normalization improves cross-annotator comparability and that 78.0% of 609 scored candidates pass the logical-quality filter. In a teacher audit of the 60 highest-effort candidates, all were judged to reach finale or penultimate problem difficulty, and only one exhibited a severe logical issue. These results support latent reasoning structures as effective control signals for generating high-difficulty mathematical problems.

---


### 93. [Not All Interpretation Methods Are Created Equal: Tiered Evaluation of AI Interpretability](https://arxiv.org/abs/2611.31833)

**<font color=#1a73e8>作者：</font>** Nicolas Sanchez, Bin Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI transitions to sociotechnical deployments, uninterpretable models pose serious threats to reliability, public trust and contestability. However, not all interpretation methods are created equal: for interpretability to enhance deployment safety and effectiveness, interpretation methods must be evaluated in a tiered system to differentiate evidence levels of trustworthiness, rather than validated through isolated interpretation instances. Our core vision is that elevating the evaluation of interpretation methods to a core AI assessment metric will drive robust knowledge discovery from data (KDD) and ensure safe, contestable sociotechnical deployments of AI. To this end, we propose TRUST, a tiered evaluation framework that builds upon the Predictability-Computability-Stability (PCS) principles for Veridical Data Science (VDS) and the Predictive, Descriptive and Relevant (PDR) foundations. To differentiate interpretation methods effectively and systematically, TRUST grades interpretation across five tiers: Task-Aligned PDR Foundations, Rigorous Epistemic Grounding, Unifying Semantic Understanding, Scope Transferability, and Targeted Prospective Validation. We present a start-to-finish case study of the iterative Random Forest (iRF) family under TRUST and contrast it with other LLM interpretation methods that struggle to clear specific tiers. Finally, we conclude with brief initial thoughts on how TRUST principles can extend in autonomous agentic frameworks. Ultimately, the TRUST framework fosters contestability and epistemic grounding as foundational evaluation principles for human-machine workflows and, eventually, autonomous agentic workflows.

---


### 94. [Faithful Persona Steering under Incongruity via Dual-Stream Refinement](https://arxiv.org/abs/2611.31848)

**<font color=#1a73e8>作者：</font>** Yu-An Chu, Jen-Ren Pong, Chia-Yao Yeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard LLM personalization typically frames identity as a static retrieval task, overlooking the inherent incongruity of human personas, where stable traits coexist with atypical, context-specific stances. Existing methods struggle to reconcile these dimensions: prompting succumbs to context drift over long sequences, while fine-tuning often suppresses idiosyncratic "quirks" in favor of generic distributional patterns. To bridge this gap, we present QuirkyMind, a framework that disentangles identity definition from its expression. First, Traits Anchoring constructs a dual-stream latent state, fusing a sentence-level summary for semantic stability with a token-level sequence for generative control. This state is stabilized via In-Context Narrative Refinement using an alternating objective: a discriminative InfoNCE loss anchors the persona in representation space to prevent drift, while a generative cross-entropy loss ensures faithful verbalization. Finally, Persona Steered Generalization transfers the refined state to downstream tasks via parameter-efficient adapters. Empirical evaluations on Persona-Steered QA and Narrative Inference demonstrate that QuirkyMind mitigates drift, consolidating persona knowledge without erasing authentic incongruities.

---


### 95. [Modeling Event-Conditioned Emotional Expression Response with LLM Agents in a Synthetic Social Simulation](https://arxiv.org/abs/2611.31851)

**<font color=#1a73e8>作者：</font>** Rebecca Marigliano, Peter Carragher, Kathleen M. Carley  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emotions are central drivers of human behavior, yet most behavioral models fail to capture their role in shaping perception, decision-making, and collective action. Application areas such as emergency response and public health are especially constrained by the lack of emotion-aware modeling. While large language models (LLMs) are increasingly integrated into agent-based models (ABMs), little work has examined how to endow LLM agents with emotional reasoning or validated their ability to reproduce empirically observed emotional patterns. This study addresses this gap by introducing a hierarchical prompting framework that conditions LLM agents with demographic, psychological, and contextual cues to generate event-conditioned emotional responses to real-world events. We validate the resulting event-conditioned emotional responses against large-scale social media reaction data derived from the Social Science One Facebook URL Shares Dataset, complemented by demographic and personality benchmarks. Our simulation results reproduce both polarized and consensus-driven emotional patterns with significant fidelity, supporting the application of LLM agents for emotion-aware modeling in behavioral simulations. We also find, however, that systematic gaps in emotional expression of LLM agents and human populations exist, such as the underexpression of anger relative to human baselines. As such, these findings highlight the need for continued calibration if LLM agents are to serve as proxies for human populations in behavioral modeling. By quantifying their divergence from human populations in terms of emotional expression, we hope that our methods can aid in this effort.

---


### 96. [No Fixed Configuration Is Best: Context- and Cost-Aware Tuning of LLM Pipelines, with an Application to Schema Matching and Mapping](https://arxiv.org/abs/2611.31864)

**<font color=#1a73e8>作者：</font>** Gokhan Kirlik, Xiuwen Zheng, Anirudh Sriram  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The numeric settings of a multi-stage LLM pipeline (a compound AI system) are the usual target of tuning. We tuned all of them for an LLM pipeline for schema matching and mapping, with accuracy and cost as joint objectives, and we show what this buys, what it cannot buy, and where the remaining accuracy is. First, tuning buys cost and a little accuracy. On 35 tasks, with whole groups of tasks held out from tuning, one tuned configuration gains 2.9 points of top-1 accuracy (HR@1) over the default at 18% more cost, and another keeps the accuracy of the default at 32% lower cost. Second, the accuracy depends on a choice that numeric tuning cannot reach. Restricting the search for each source column to one assigned target table changes HR@1 by +30 points on a MIMIC-III to OMOP task and by -52 points on a task built from database views, more than numeric tuning gains on nine of ten test tasks. Neither setting is right for all tasks: on the larger set of 41 tasks used for the remaining results, mean HR@1 is 75.7% with the restriction (the default) and 83.1% without it. Third, choosing the setting per task is not enough either: even an oracle that picks the better setting for each task reaches only 87.8% on the 41 tasks, because the better setting differs between the columns of one task. The pipeline therefore runs both settings, and an LLM judge chooses among their candidate answers on the 26% of columns on which they disagree. This reaches 91.5% HR@1 on the 41 tasks, at 5.9 times the cost of the default, about one cent per column.

---


### 97. [Subliminal Learning Crosses Modalities](https://arxiv.org/abs/2611.31870)

**<font color=#1a73e8>作者：</font>** Saraswathy Amjith, Kimia Hamidieh, Antonio Torralba 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Subliminal learning refers to a surprising phenomenon in language models wherein a prompt given to one model (e.g., preference for cats) can be subliminally distilled to another model via training on data that is ostensibly meaningless (e.g., number sequences). This paper shows that text-based subliminal learning transfers cross-modally, in particular, a topic/preference (e.g., animals) transferred through number sequences across vision-language models also changes how images are generated and represented. First, we show that a diffusion model using the student as its text encoder generates the student's animal more often than with the original model as its text encoder, but not its color or style. We then investigate the mechanism behind this phenomenon and which concepts transfer across modalities. A constant component of the student's change accounts for much of the shift of image representations toward the trait. Adding this component uniformly can change the generated animal, which depends on the whole prompt, but not concepts such as color or style, which are encoded in a single token. Finally, we introduce weight lens as an approach to identify a subliminal trait from the weights of a single trained model, and show that it identifies the trait of nearly every student, including traits that do not surface in generated images.

---


### 98. [RELAY: Learning Compatible Representations One Encoder at a Time](https://arxiv.org/abs/2611.31882)

**<font color=#1a73e8>作者：</font>** Yu Wang, Chuan Qin, Qiang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Old and new document embeddings coexist during incremental gallery re-encoding. RELAY trains a new query encoder with a learned projection against the original gallery, then freezes both to train the new document encoder. The same query vector scores both document versions throughout a single re-encoding pass. After backfill, optional query refinement drops the projection and reuses the stored document vectors. Across three text-to-image retrieval upgrades on COCO and Flickr30K, RELAY improves Recall@1 on untouched galleries by 8.66-10.23 percentage points over the original systems. For direct re-encoding, RELAY ranks first in both Qwen-to-Qwen upgrades and second in CLIP-to-Qwen by area under the Recall@1 curve, under both native scoring and matched calibration. With embeddings held fixed, calibrating scores separately for each document version can reduce drops in Recall@1 during backfill and change which method achieves the highest backfill AUC. After query refinement, final Recall@1 is within 0.97 percentage points of conventional joint training in all three upgrades.

---


### 99. [Open-OmniCoach: Evidence-Enhanced Trajectory Learning for Omni Video Agents](https://arxiv.org/abs/2611.31891)

**<font color=#1a73e8>作者：</font>** Weisong Liu, Xiangtai Li, Haochen Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training capable omni video agents requires more than diverse question-answer pairs: agents must learn to reliably find, connect, and correct task-relevant evidence in omni-setting. However, we argue that existing data pipelines provide limited control over task-relevant evidence and weak supervision for these capabilities. In this work, we present Open OmniCoach, a new framework for evidence-seeking omni video agents. It contains a high-quality dataset, OmniCoach-240K, and a new agentic reinforcement learning (RL) method, Step-Level Evidence-Guided Policy Optimization (SEPO). For the former, OmniCoach-240K comprises 248.2K interaction trajectories, including 230.7K multi-span trajectories and 17.4K reflection trajectories. We design a three-stage data pipeline by leveraging both fine-grained omni-evidence and the agent's own errors. Meanwhile, compared with other RL baselines, SEPO provides turn-level credit based on improvements in evidence coverage and temporal localization. Applying both trajectory data and the SEPO method, we obtain Open OmniAgent models. The resulting models outperform the baselines across multiple video and audio-visual understanding tasks by significant margins, demonstrating the effectiveness of the Open OmniCoach framework. In particular, Open OmniAgent-30B improves average accuracy over Qwen3-Omni by 6.3 percentage points across nine benchmarks, with gains of 12.2 and 13.3 points on LVOmniBench and LVBench, respectively.

---


### 100. [Beyond Expert Replay: Cross-Instruction Anchoring for Continual Vision-Language-Action Learning](https://arxiv.org/abs/2611.31903)

**<font color=#1a73e8>作者：</font>** Ziyang Chen, Dehua Chen, Shaoguang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models need to continually acquire new manipulation skills while retaining the ability to follow previously learned instructions. Experience replay (ER) can mitigate catastrophic forgetting, but retaining only a small number of historical expert frames per task leaves many old-instruction responses without direct supervision. Under limited replay, we observe a structured failure mode in which an earlier instruction can trigger a subsequently learned, competing goal. To address this gap, we propose Cross-Instruction Anchoring (XIA), which supplements expert replay with instruction-conditioned response preservation. At each task boundary, XIA freezes the previous policy as a teacher and matches its responses to old instructions paired with current observations. This extends supervision beyond stored historical examples without requiring additional expert replay data. Experiments across multiple VLA architectures and three LIBERO suites demonstrate improved success rates and reduced forgetting compared with ER under identical historical expert-data budgets. Additional RoboCasa and real-world experiments further support the effectiveness of XIA.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-299](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
