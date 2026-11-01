# 🧠 大模型相关研究 | 2026年11月02日

> 本类共 **353** 篇论文：已确认 **335** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

---

### 201. [AgentDecept: Benchmarking Deceptive Behavior in Tool-Using LLM Agents under Pressure](https://arxiv.org/abs/2610.39377)

**<font color=#1a73e8>作者：</font>** Yehan Zhang, Qianqi Yan, Hang Yin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly carry out multi-turn tasks across everyday applications, yet users often see only the agent's report rather than the observations, API calls, and state changes behind it. Existing deception benchmarks have studied long-horizon interactions and tool-use settings, but whether agents faithfully report their actions across realistic, stateful application workflows remains underexplored. To address this gap, we introduce AgentDecept, an executable benchmark for evaluating behavioral deception under pressure. AgentDecept contains 477 pressure variants derived from 257 source tasks across six pressure sources, each paired with a pressure-free counterpart. Interventions enter through event messages, task context, application state, tool responses, and service quotas, spanning explicit events and implicit task or environment changes. Our evidence-grounded protocol evaluates full trajectories by relating user-facing claims to time-ordered observations and executed outcomes, distinguishing falsification, concealment, and equivocation from honest failure and disclosed limitations. The resulting behavioral labels also provide a setting for testing existing activation-based probes. AgentDecept enables controlled analysis of when multi-turn agents' reports diverge from execution in realistic application interactions.

---


### 202. [Robustness of Chatbot LLM Judgments of Presidential Actions and Hypothetical Reforms](https://arxiv.org/abs/2610.39398)

**<font color=#1a73e8>作者：</font>** Oleg Vasilyev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chatbots are increasingly consulted about public affairs, and their judgments of policies are useful only if they are robust. We measure this robustness in the setting of an ordinary user, through consumer chat interfaces. For 30 days, five chatbot configurations (Mistral, Gemini Flash, Claude Sonnet, and Claude Opus at two effort settings) were asked twice a day to score the long-term effect on the United States of 40 actions of the last four presidential administrations and of 15 hypothetical reforms, each with a confidence and a short comment. The judgments are robust: all configurations agree on the sign and the ranking of the administrations' mean scores, and two different configurations asked on the same day give opposite signs to the same action in about 4% of cases. Responses from different days differ more than same-day responses, but the difference grows slowly over the month, except where the service itself changed. We identify three such changes, which shifted the judgments while leaving little or no trace in the interface. Treating the comments as a retrieval task, we find them specific to each item and consistent across runs and chatbots, with lexical and embedding similarities agreeing. We release the dataset of 16,500 judgments.

---


### 203. [Retaining Repair Hypotheses for Cost-Aware Execution](https://arxiv.org/abs/2610.39410)

**<font color=#1a73e8>作者：</font>** Jae Hun Hwang, Hong-In Won  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Several corrections of an executable model can fit the same observations while predicting different execution outcomes. We study a repair-to-execution interface that retains compatible finite guard repairs, conditions their weights on diagnostic and ordinary-execution observations, and uses their predictions to choose routes, priced tests, or a backup. On 24 synthetic two-stage devices, an equal mixture of a language-model-generated repair and a uniform belief over compatible repairs (the AI-weighted belief) lowers no-test cost by 2.14 percent relative to committing to the generated repair. Access charges can erase the benefit of diagnosis on isolated tasks, while repeated work can recover it under the AI-weighted belief. With normal-execution learning in every repeated-work arm, workload-valued testing costs 3.33 percent less than same-budget random selection under the AI-weighted belief. Weighting changes the comparison: uniform normal learning costs 540.75 less than AI-weighted normal learning on this cohort, with a device-paired interval excluding zero. Testing recovers part of that gap, but uniform normal learning still has a lower aggregate cost than AI-weighted workload-valued selection. Under uniform beliefs, information-gain selection has the lowest total among the compared selectors, while workload-valued testing costs more than normal learning. These results support retaining alternatives to a generated repair and evaluating diagnostic selection together with repair weighting and learning from execution.

---


### 204. [Dobb: Shard-Local Preconditioning in Block-Diagonal Eigenbases](https://arxiv.org/abs/2610.39412)

**<font color=#1a73e8>作者：</font>** Shi-Yuk Fong, Shuhua Yu, Jiawei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training language models whose parameters and optimizer state exceed a single node's memory requires sharding these tensors across devices. Under tensor parallelism (TP) or fully sharded data parallelism (FSDP), matrix-aware optimizers such as Muon introduce communication to perform global matrix operations across shards. We propose Dobb (Distributed Optimizer with Block-diagonal Eigenbases), a matrix-aware optimizer designed to compute updates locally within parameter shards. Dobb approximates the input-activation second moment with diagonal blocks and tracks a complete basis within each block. It projects momentum into these bases, applies sign normalization to the coefficients, and reconstructs the update. When each block lies within one shard under TP or FSDP, Dobb applies its matrix update locally, requiring no communication beyond data-parallel synchronization of the activation second moments. We benchmark Dobb against Dion, a distributed matrix-aware optimizer designed to retain the benefits of orthonormalized updates while reducing communication. On GPT-2 XL (1.56B parameters), Dobb with 16 blocks reaches a validation loss of 2.476, compared with 2.511 for Dion at rank fraction 1/16. Under FSDP on 32 H100 GPUs, Dobb reduces the amortized optimizer-call time from 124.1 ms for Dion to 9.2 ms.

---


### 205. [Accuracy is not compatibility: two Evo 2 checkpoints hinge on one FP8 matrix multiplication](https://arxiv.org/abs/2610.39415)

**<font color=#1a73e8>作者：</font>** Xun Ding, Ziyuan Qin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> FP8 formats specify how values are stored, not how products are summed; this gap can break checkpoints. Evo 2, a DNA language model, documents a Hopper FP8 requirement for its 1B and 40B checkpoints. On two Blackwell (sm_120) GPUs both fail the developers' forward test (the 7B passes); on an RTX 5070 Ti the 40B's next-base accuracy is 25.7%, near guessing. Greater accuracy breaks them, as BioNeMo saw for the 40B on Hopper: natively, 99.996% of one projection's outputs are correctly rounded (H100: about 30%), and fp32 accumulation of the same operands fails. Our H100 FP8 GEMM emulator, mmaemu (bit-exact on captured 1B projections), localises the dependence to the 1B's first projection (of 21), where exact sums fail but pass when shrunk by the H100's 1.4% (measured in-sample), not 2.1%. The 40B fails with only its first projection native. Emulating only that projection, weights unchanged, raises 40B BRCA1 variant-classification AUROC from 0.434 to 0.869 (H100: 0.868) on the RTX 5070 Ti, despite a narrow forward-test miss, and 0.481 to 0.867 on an RTX PRO 6000. We tested one model family but not training origin; releases should specify reference arithmetic.

---


### 206. [LinQuant: Functional Invariances for Low-Precision Linear Recurrences](https://arxiv.org/abs/2610.39418)

**<font color=#1a73e8>作者：</font>** Neehal Tumma, Philipp Nazari, Rohan Cherukuri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear recurrences are emerging as practical alternatives to softmax attention in large language models, appearing in both standalone and hybrid architectures. However, despite their rapid emergence, low-precision inference remains much less developed for these models than for softmax attention. During prefill, chunkwise-parallel algorithms cast much of the recurrence as dense matrix multiplications, suggesting a natural path to low-precision execution. Simply quantizing these operations in their native form, however, can be fragile. In this work, we identify functional invariances that preserve the full-precision computation while making the operands more amenable to quantization. Building on this observation, we introduce LinQuant, a framework for low-precision recurrent prefill based on seven such invariances, including rotations, diagonal rescalings, and alternative placements of recurrent decay and write factors. We derive when these transformations remain valid across common recurrence families spanning linear, gated, and delta-rule updates, and show that they provide complementary degrees of freedom for improving low-precision accuracy. Finally, we translate this framework to production by augmenting SSDi8, an existing low-precision prefill pipeline for Mamba-2, with the applicable invariances. LinQuant improves perplexity at matched latency on Mamba-2 1.3B, 2.7B, and 8B and Nemotron-H 8B, demonstrating the practical utility of invariance-based quantization for recurrent models.

---


### 207. [Diagnosing the Reference Gap: What Visual Scaffolds Can and Cannot Fix in Multimodal Reasoning](https://arxiv.org/abs/2610.39419)

**<font color=#1a73e8>作者：</font>** Guizhen Chen, Weiwen Xu, Wotao Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models can recognize visual content yet struggle to reason reliably over it across multiple steps. In counting, a model may see all objects but lose track of which ones it has counted. We argue that such failures, commonly attributed to perception, reveal a reference gap: the failure to bind language to the relevant visual entities, regions, or locations. Motivated by the theory of visual routines, we test whether external references such as numbering can narrow this gap. We introduce ReGap-Bench, a paired benchmark of five visual reasoning tasks in which the scene, question, and answer are fixed and only the reference varies. Results show that task-matched references improve accuracy by up to 25\%, while mismatched references provide little benefit or even hurt performance. These findings identify the reference gap as a bottleneck distinct from visual perception and show that constructing task-appropriate visual references can serve as a training-free visual skill for improving multimodal reasoning.

---


### 208. [ARBITRA: Robust Document-Level ATT&CK Extraction via Multi-Expert Argumentation](https://arxiv.org/abs/2610.39433)

**<font color=#1a73e8>作者：</font>** Youngjin Jin, Seungwon Shin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cyber threat intelligence (CTI) reports describe adversary behavior in natural language, but converting them into structured MITRE ATT&CK mappings remains difficult: existing methods decompose reports to sentence-level granularity for extraction, while modern LLMs can work with full reports in a single pass but with noticeable performance degradation. We present ARBITRA, which orchestrates multiple role-specialized LLM experts that propose candidate ATT&CK entities from the full report, which are then verified through a per-candidate quantitative bipolar argumentation framework (QBAF) grounded in document evidence and rationales. We additionally construct reasoning-specialized corpora for fine-tuning so experts can act as effective participants during this verification process. Across ATT&CK extraction benchmarks, ARBITRA reaches a stronger precision-oriented operating point than sentence-level pipelines, recent LLM-based extraction systems, and frontier models including GPT-5.5. Under adversarial perturbations simulating conflicting TTP statements, cross-report contamination, and semantic poisoning, ARBITRA limits mean precision degradation to roughly half that of frontier-model baselines for a more robust extraction.

---


### 209. [Verifiable LLM-Guided Focal SMT Solving for Quantified Arrays](https://arxiv.org/abs/2610.39435)

**<font color=#1a73e8>作者：</font>** Kunhang Lv, Rui Han, Fuqi Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can often identify useful semantic structure in formal artifacts, but their outputs cannot be trusted as proofs or solver decisions. We study whether LLMs can instead guide formal reasoning systems through a narrow, solver-verifiable interface. We instantiate this idea in quantified array SMT solving, where modern instantiation-based techniques can fail when key ground terms and equalities are hidden by auxiliary variables, axiom guards, and nested array terms. We observe that many instances are largely driven by a small set of focal ground terms or constraints, similar to the backdoor sets in SAT solving. Building on this, we present LinguaArray, a framework where an LLM proposes a small Semantic Focus Set (ground terms/constraints), while a conventional SMT solver remains the sole proof engine and certifies all results. LinguaArray uses these LLM-suggested, solver-validated finite sets to significantly enhance solver capability, solving additional satisfiable and unsatisfiable instances that the backend alone fails to solve. It interacts within a finite time and then falls back to the backend solver to mitigate potential regressions. Evaluation on 1015 SMT-LIB instances across five logics under 1200s timeout (including LLM latency) shows that LinguaArray solves up to 69.1% of instances and increases solved-instance counts by 105%--397% over the corresponding backends.

---


### 210. [ATLAS-Bench: An Agentic Tool-Use Benchmark for Local Area Search](https://arxiv.org/abs/2610.39438)

**<font color=#1a73e8>作者：</font>** Keyun Zhang, Dapeng Yin, Fanfu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable local search is essential for LLM agents to support everyday decisions and longer plans by finding places that meet users' needs at given times and locations. Yet existing benchmarks provide limited coverage of whether search results satisfy mandatory requirements, account for preferences, and ground factual and experiential judgments in place attributes and reviews. We introduce ATLAS-Bench, a benchmark of 1,200 queries across three regions, expanded from real search events using place attributes, reviews, and existing user profiles from the platform. Each query distinguishes mandatory requirements from preferences and factual conditions from subjective judgments, with supporting evidence and criteria for checking each requirement. Queries are validated through iterative assertion checks and cross-model review. We also introduce ATLASBox, a standardized evaluation environment with search tools and a fixed point-of-interest (POI) knowledge base. Given a query, timestamp, and location, an agent searches place attributes and reviews to recommend evidence-supported options or report that no place meets all mandatory requirements. We evaluate answer quality, trajectory quality, and execution cost. Across 14 configurations of 11 models, GPT-6-Luna achieves the highest constraint satisfaction rate among returned recommendations (71.5%) and factual accuracy (95.6%). However, it returns at least one acceptable recommendation for fewer satisfiable queries than GLM-5.3 (67.3% versus 85.3%). These results highlight the challenge of satisfying individual requirements while providing usable recommendations across queries.

---


### 211. [Timbre: Reliability-aware harmonic consensus for label-free multimodal test-time rexinforcement learning](https://arxiv.org/abs/2610.39439)

**<font color=#1a73e8>作者：</font>** Haotian Lyu, Haoyu Wang, Ru Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Label-free test-time reinforcement learning adapts vision--language models using rewards derived from their own predictions. However, misinterpreted visual evidence and sensitivity to textual formulation can produce a consistent but incorrect consensus that majority voting reinforces. Cross-view aggregation can expose such errors, but image and text transformations may themselves degrade task-relevant evidence to different extents. We introduce \method, a reliability-aware harmonic consensus framework for multimodal test-time reinforcement learning. \method constructs a $2\times2$ grid combining original and perturbed images with direct-solving and reframing modes, selects pseudo-labels through weighted harmonic aggregation, and adapts modality-level weights using batch-averaged, temporally smoothed shifts in pseudo-label confidence as a heuristic reliability signal. We formulate consensus as a weighted $\chi^2$-barycenter problem whose unique minimizer is the normalized weighted harmonic aggregate, without requiring correct-answer invariance. An exact support--dispersion decomposition characterizes when harmonic aggregation preserves or corrects arithmetic rankings, while a sensitivity analysis establishes how modality reweighting changes pairwise ranking margins, informing interpretation of the heuristic updates. Across six benchmarks and three Qwen3-VL model scales, \method outperforms TTRV in 16 of 18 benchmark--model settings on adaptation instances and 17 of 18 settings on held-out instances under matched estimation and optimization rollout counts. These results demonstrate improved target-task adaptation and transfer to unseen instances without further updates.

---


### 212. [PathCowork: Learning from real-world pathology practice to build AI copilots](https://arxiv.org/abs/2610.39441)

**<font color=#1a73e8>作者：</font>** Sheng Wang, Jialu Yao, Maria V. Rossi 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical AI learns from the answers doctors record, but rarely from how they interpret the evidence to reach them. Here we introduce PathCowork, a framework that turns pathologists' narrated examinations into supervision for visual grounding and procedures that guide diagnostic AI agents. Synchronized gaze, narration and navigation link visual findings to the process of interpreting them. Across 48 sessions from 16 pathologists, the platform captured 1,028 minutes of slide review. Using these data, we trained PathCowork-1T for server deployment and PathCowork-27B for local deployment, with improved visual grounding. Across five organ-specific evaluations, agents combining this grounding with recorded diagnostic procedures achieved primary task scores averaging 17.9 and 24.1 percentage points higher than Claude Code and Codex, respectively, with shorter processing times and lower inference costs. Compared to the state-of-the-art multiple-instance learning AIs, the PathCowork agent-proposed regions achieved higher prostate-grading scores with limited slide labels. PathCowork can also help construct pathology AI benchmarks where questions derived from the recordings identified difficulties in recognizing viewing context and rejecting inapplicable premises. In summary, PathCowork proposes a new paradigm to scale up the data collection and train pathology AI through transparent reasoning from diagnostic sessions, opening a path towards systems that learn directly from routine clinical practice.

---


### 213. [Softmax Routing Dynamics in Mixture-of-Experts Models: Collapse and Recovery](https://arxiv.org/abs/2610.39442)

**<font color=#1a73e8>作者：</font>** Shengze Xu, Maolin Deng, Tieyong Zeng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Softmax routing in mixture-of-experts models can concentrate probability on a subset of experts, suppressing access to the others. We study how this concentration forms, why it persists, and how suppressed probabilities recover. For fixed experts, a stationary-loss barrier identifies the face supporting the optimal routed output. In a common-target square-loss model with freely trainable expert outputs, slow adaptation tracks fixed-expert dynamics on finite horizons, while every fixed positive adaptation rate yields an interior routing limit. An exact normal-velocity decomposition separates complementary-expert covariance from relative gradient advantage. Under positive two-sided power bounds along recovery paths, uniform over initial masses, the resulting coefficient's order of vanishing gives logarithmic or power-law recovery times. Integrations of constructed fields reproduce these orders. An exact discrete log-odds identity relates neural updates to threshold crossing. In paired Transformer-MoE training, removing a class-conditional router-gradient contrast delays confirmed recovery and reduces accumulated log-odds on fixed tokens, both with and without capacity constraints.

---


### 214. [Smooth Action Chunking Via Movement-Primitive Representations for Imitation Learning](https://arxiv.org/abs/2610.39451)

**<font color=#1a73e8>作者：</font>** Shota Nomura, Takayuki Osa, Yasuhiro Kato 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imitation learning has become a widely adopted approach for vision-based robot policies, owing to its conceptual simplicity, scalability, and ability to leverage large-scale datasets. As these policies have grown more capable, action chunking has become their standard interface. At each decision step the policy outputs several future actions at once. Backbones from diffusion policies to large vision-language-action models all share it. Whatever backbone produces the chunk, its temporal structure is learned only implicitly. The commanded trajectory is therefore jerky both within a chunk and between successive chunks. On real hardware this appears as visible vibration and as repeated saturation of the follower's velocity limit. We address this issue by incorporating a movement-primitive-based trajectory representation into action chunking. Specifically, a trajectory segment is represented as a linear combination of smooth basis functions, yielding smooth trajectories by construction while leaving the policy architecture, training objective, and inference procedure unchanged. The same representation also yields a closed-form, inference-time correction for the second source of jerk. We condition the predicted coefficients so that the new chunk passes through a via-point at the previous chunk's last commanded action. This correction needs no retraining and, unlike asynchronous Real-Time Chunking, applies to policies queried in one shot. We instantiate it on a one-shot (ACT) and an iterative (DiT) backbone and evaluate in simulation and on a real bimanual ALOHA platform. The representation lowers within-chunk jerk by an order of magnitude on the one-shot backbone and by 2.4 times on the iterative one, with task success statistically non-inferior. The conditioning then removes 73-84% of the boundary discontinuity, at negligible per-step cost.

---


### 215. [Integrating Heterogeneous Echocardiography AI Outputs in Language Space: Learnable Late Fusion with a Supervised LLM](https://arxiv.org/abs/2610.39464)

**<font color=#1a73e8>作者：</font>** Ryo Takizawa, Tempei Kabayama, Chiemi Yamazaki 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> View- and target-specific echocardiography AI models capture useful but complementary information and may not achieve sufficient predictive performance in isolation. A learned ensemble is a natural way to combine these outputs, but heterogeneous models typically require each output to be converted into a binary decision, probability, confidence score, or fixed-length feature vector. We developed a supervised large language model (LLM)-based late-fusion module that directly aggregates view-specific predicted finding statements and predicted measurements in language space and learns a case-level fusion function. In patient-level three-fold cross-validation of 859 examinations from 646 patients, the proposed method integrated heterogeneous outputs within a single framework, performed comparably to the best-performing reference strategy evaluated, and outperformed a general-purpose LLM without task-specific training. These results suggest that a supervised LLM can combine multiple upstream models without model-specific output conversion or feature engineering that requires medical knowledge.

---


### 216. [InterA11y: Interactive Web Accessibility Error Detection with LLM Agents](https://arxiv.org/abs/2610.39488)

**<font color=#1a73e8>作者：</font>** Mingyuan Zhong, Mengqi Shi, Davin Win Kyi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown potential to expand the coverage of web accessibility evaluation. However, current LLM-based checkers neglect much of the interactive and dynamic web contexts, resulting in limited coverage, high false discovery rates, and inconsistent performance across models. We present InterA11y, an agentic accessibility evaluation system that combines rubrics and interactive tools to support LLM agents in evaluating accessibility effectively. The rubrics decompose WCAG success criteria (SC) into testable aspects and guide agents in collecting and interpreting evidence. The interactive tools inspect or operate a webpage deterministically to collect evidence, such as focus appearances and error messages. We developed these rubrics and tools on 682 curated test cases grounded in established accessibility guidelines that target 10 commonly violated SC. We evaluated InterA11y on 197 expert-annotated cases sampled from 54 real webpages. Results show InterA11y achieves higher recall than the strongest evaluated LLM-driven baseline (79.0% vs. 44.4%), while maintaining comparable precision to best rule-based checkers (93.1% vs. 90.3-97.6%), with little variability between models. Further, when equipped with our interactive tools, general-purpose web agents detect more accessibility errors with fewer false positives and less token usage than without these tools.

---


### 217. [What Breaks When Facts Become Stories? The Distortions Source-Agreement Metrics Miss When Models Retell Real Events](https://arxiv.org/abs/2610.39500)

**<font color=#1a73e8>作者：</font>** Kwangsuk Park, JiWoong Yang, Vaniushkina Kseniia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models are now widely used to turn recorded facts into media for public consumption, yet evaluation of such output still assumes agreement with the source as its measure of success. In reconstruction, where departing from the source can itself be the goal, this criterion measures the wrong construct: applied as is, it counts intended departures as errors; withheld, it lets real distortion through. We had three model families rewrite 2,000 news articles as summaries and as stories, measured what changed on every axis of the five Ws and how, and asked of each detected distortion whether the assigned perspective warranted it, which set a third of them aside. Time and manner were not lost but replaced, while place and causation lost the expressions that carry them. Accountability distortion behaved otherwise. Barely present in summaries, it rose up to sevenfold in stories, and of those whose direction could be determined, two in three lightened the perpetrator's responsibility. Such distortions survive claim-level fact checking and leave the retelling grammatically cleaner than its source. Where our judges disagreed, three authors relabeling the same cases converged on whether a distortion had occurred but not on whether it was warranted, a boundary contested rather than merely hard to detect. To support work on detecting and reducing them, we release ReTold-2k, a reconstructable corpus with the scoring protocol and per-judge baselines kept unaggregated.(this https URL).

---


### 218. [Compile Away Uncertainty: Self-Evolving Agent Skills via Programmatic Compilation](https://arxiv.org/abs/2610.39508)

**<font color=#1a73e8>作者：</font>** Chengyu Yang, Yunxiang Zheng, Zongzheng Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agent skills enable AI agents to accumulate and refine reusable procedural knowledge from interaction experience without updating model parameters. However, since such skills are typically represented as textual documents and executed through LLM reasoning, even previously learned procedures must be repeatedly interpreted and regenerated, introducing avoidable uncertainty into every execution. In contrast, program execution is deterministic and independently verifiable. Intuitively, transforming well-specified operations into executable programs can reduce reliance on LLM reasoning and, consequently, reduce execution uncertainty. Motivated by this intuition, we introduce SKillCompiler, a self-evolving skill framework that integrates programmatic compilation into the skill evolution process. Specifically, SkillCompiler adopts an executability-aware skill compilation strategy that decomposes skills into fine-grained operations, analyzes their executability, and constructs hybrid skill skeletons that retain LLM reasoning for context-dependent operations while compiling well-specified ones into validated programs. To avoid redundant program synthesis and enable executable knowledge to accumulate across evolving skills, we further design a program asset reuse mechanism that organizes validated programs as reusable assets, retrieves existing implementations whenever applicable, and synthesizes and verifies new programs only when necessary. Extensive experiments on five benchmarks and six model families demonstrate that SkillCompiler consistently outperforms state-of-the-art methods, achieving up to 32.33\% improvement in task performance.

---


### 219. [Systematic Evaluation of Adversarial Jailbreaking Attacks and Defenses Across Seven Large Language Models](https://arxiv.org/abs/2610.39509)

**<font color=#1a73e8>作者：</font>** Md. Robiul Islam Niloy, Abu Sayed Md. Mostafizur Rahaman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) deployed in safety-critical settings must resist adversarial inputs designed to elicit harmful outputs. We present a systematic empirical evaluation of five adversarial jailbreaking attack families---direct requests, roleplay-based jailbreaking, hypothetical framing, instruction override, and obfuscation---across seven open-weight and API-accessible LLMs: Llama-3-8B, Llama-3.1-8B, Llama-3.2-3B, Mistral-7B, Qwen2.5-7B, Gemma2-9B, and Phi-4-14B. We further evaluate four defense mechanisms: keyword blacklisting, self-reminder prompting, paraphrase-based sanitization, and perplexity-based filtering against the two most vulnerable models. Our results reveal that obfuscation attacks achieve a mean attack success rate (ASR) of 54.3% across all models and constitute the most transferable adversarial vector, bypassing every evaluated model with nonzero success. We find that model size does not predict adversarial robustness (Spearman r=-0.57, p=0.18), and that models within the same architecture family exhibit dramatically different vulnerability profiles. Self-reminder prompting achieves the most consistent defense, reducing ASR from 44% to 10% on Mistral-7B and from 48% to 5% on Llama-3.1-8B with zero false positives and no additional inference cost. Our code and datasets are publicly available at this https URL.

---


### 220. [Category-Anchored Large Language Models for Next POI Recommendation](https://arxiv.org/abs/2610.39518)

**<font color=#1a73e8>作者：</font>** Lexi Bai, Xiaopeng Zeng, Xun Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Next point-of-interest (POI) recommendation aims to predict a user's next destination from spatio-temporal check-in data, and serves as the foundation for many location-based services. Recent advances incorporate large language models (LLMs) into this task by textualizing user trajectories to exploit their semantic reasoning ability. However, directly generating POI identifiers with such models is unreliable: POIs are sparse, localized, and long-tailed entities with weak natural-language semantics, which creates a semantic-to-entity gap between high-level mobility intent and concrete POI prediction. To bridge this gap, we propose ANCHOR, a category-anchored framework for semantic-to-entity grounding in next POI recommendation. Specifically, ANCHOR first estimates category-level mobility intent in a compact and stable semantic space, rather than predicting concrete POI entities directly. The inferred intent is then grounded into a candidate set by integrating three complementary sources of mobility evidence: category anchors, historical visit memory, and user preferences. Finally, a history-aware reranker selects the target POI by matching each candidate with the user's historical mobility patterns and current context. Experiments on three real-world check-in datasets show that ANCHOR consistently outperforms representative traditional, structure-enhanced, and LLM-based baselines on the reported metrics. Further analyses validate the effectiveness of semantic-to-entity grounding and show favorable trade-offs among candidate coverage, ranking quality, and inference efficiency.

---


### 221. [BRIDGE: Learning Brain-Gut Metabolic Evidence for Alzheimer's Disease Diagnosis](https://arxiv.org/abs/2610.39520)

**<font color=#1a73e8>作者：</font>** Pengli Zhu, Ruxi Chang, Tianliang Yao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Alzheimer's disease (AD) diagnosis may benefit from gut metabolic information associated with brain-gut interactions, yet existing models largely analyze cerebral glucose metabolism alone. Although whole-body fluorodeoxyglucose positron emission tomography (FDG-PET) can provide paired brain-gut observations, routine brain examinations rarely include gut imaging, limiting direct use of this information for diagnosis. In this paper, we present BRIDGE (Brain and Gut Representation Integration via Distribution-Guided Enhancement), a two-stage framework for transferring brain-gut metabolic knowledge to brain-only diagnosis. Specifically, BRIDGE integrates a conditional brain-to-gut latent transport module and a disease-evidence-guided cerebral pathway to capture subject-specific cross-organ correspondence and disease-relevant cerebral representations. For the cerebral pathway, a large language model (LLM) helps organize literature-derived descriptors into human-approved semantic anchors that guide feature learning. Additionally, we introduce a counterfactual-guided residual fusion mechanism, which uses matched and non-matched virtual-gut evidence to supervise a confidence gate and dynamically regulate the contribution of transported cross-organ information. At inference, BRIDGE exploits complementary gut-related context using brain PET alone, without measured gut PET. Extensive experiments across public and private cohorts demonstrate that BRIDGE outperforms brain-only and cross-organ baselines, achieving AUC gains of 6.0% and 5.2% over its brain-only counterpart for CN/MCI and CN/AD diagnosis, respectively. Notably, its ability to transfer complementary brain-gut metabolic context while preserving brain PET as the sole inference input highlights its potential for clinically practical diagnosis. Our code is available at this https URL.

---


### 222. [Judging Before Propagation: Task-Graph Contextual Integrity for Multi-Agent Privacy](https://arxiv.org/abs/2610.39532)

**<font color=#1a73e8>作者：</font>** Hengyu Wu, Blaise Delattre, Yang Cao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems increasingly rely on persistent memory and inter-agent communication. These capabilities create privacy risks that extend beyond individual interactions: a release appropriate in isolation may become inappropriate when combined with information previously disclosed to a recipient or propagated to downstream agents along the planned workflow. Existing Contextual Integrity (CI) mechanisms for agentic systems typically rely on local judgments that assess each disclosure in isolation, with or without regard to the recipient's history, but do not account for how information propagates downstream. However, compliance at the current boundary does not guarantee appropriateness across the workflow. We introduce Task-Graph Contextual Integrity (TG-CI), to our knowledge the first task-graph-native formalization of Contextual Integrity for multi-agent systems. TG-CI represents a workflow as a Multi-Agent Task Graph (MATG) and extends CI from atomic transfers to stateful, graph-level information flows by jointly considering an item's intended propagation scope and recipients' evolving disclosure states. We operationalize TG-CI through propagation-scoped authorization under two complementary policies: Full-Scope, which requires admissibility across the complete downstream scope, and Auto-Region, which confines each item to its maximal admissible region using lightweight frontier gates. We further introduce MAPLE-Bench, a benchmark of 144 cases across four scenarios that jointly vary MATG topology, disclosure history, compromised-agent placement, and item-level privacy policies. In our primary experimental configuration, TG-CI reduces the mean unauthorized disclosure count by 85.8-94.1% relative to the Local-History CI baseline, while retaining 93.6-96.1% of the baseline's task accuracy, with the two enforcement policies providing complementary privacy--cost--utility trade-offs.

---


### 223. [Beyond Preference Following: Benchmarking Profile-Query Arbitration in Personalized Text Transformation](https://arxiv.org/abs/2610.39550)

**<font color=#1a73e8>作者：</font>** Tenghao Ji, Qichen Sun, Zhuoran Lu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Writing assistants use persistent preferences to personalize responses, but these can conflict with the current request. Responses can meet every requirement yet serve the task poorly, while task failures need not involve following a conflicting preference. We introduce Profile Conflict Arbitration (PCA-Bench), a benchmark of 64 rewriting tasks and 256 task-preference pairs. We construct these pairs by varying the profile preference for each fixed text and request, covering different relations between the preference and the request. We assess whether responses meet requirements, how well they achieve the request's goals, and whether they follow preferences. Across three LLMs, we find that when preferences compete with task goals, a higher success rate in meeting both requirements and preferences does not mean better responses: it can come with a greater quality loss compared with responses without a profile. Similar rates of preference following do not imply the same ability to meet the current task's requirements when preferences conflict with them.

---


### 224. [LatentWeave: Test-Time Latent Optimization for Multimodal Reasoning](https://arxiv.org/abs/2610.39557)

**<font color=#1a73e8>作者：</font>** Fanci Meng, Kun Wang, Guibin Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in test-time optimization have shown that the multimodal reasoning performance of large multimodal language models (MLLMs) can be improved during inference without modifying backbone model parameters. However, existing approaches primarily operate at the prompt or output level, leaving the latent reasoning process largely uncontrolled and insufficient to prevent error accumulation during autoregressive generation. To address this limitation, we propose LatentWeave, a test-time framework that treats multimodal reasoning as a controllable latent trajectory. LatentWeave performs structured Latent Weaving, progressively refining intermediate hidden states segment-wise to correct emerging deviations, and further introduces Reasoning Anchors via lightweight WEAVE tokens to stabilize reasoning structure and guide answer-oriented generation. These mechanisms are designed to enable fine-grained, step-aware intervention in the latent reasoning process while keeping the main MLLM backbone parameters fixed. Extensive experiments across diverse multimodal reasoning benchmarks report improvements over the evaluated baselines; the contribution of latent optimization, anchor training, and additional test-time computation is analyzed separately in the ablation and efficiency studies. Our code is available at this https URL.

---


### 225. [Non-Zero Radius: The Missing Component of Neural Networks](https://arxiv.org/abs/2610.39559)

**<font color=#1a73e8>作者：</font>** Tiansi Dong, Mateja Jamnik, Pietro Liò  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inspired by the analogy between the all-or-none activation of biological neurons and the true-false of logic circuits, McCulloch and Pitts proposed a mathematical model of the biological neuron in 1943 with the aim of simulating logical reasoning. Although Norbert Wiener considered the model overly simplistic at the time, it later became a building block of modern neural networks, including large language models. Despite their remarkable empirical success, however, conventional neural networks remain largely black-box systems and struggle with reliable symbolic reasoning. Viewing vectors as spheres of zero radius, we relax the zero-radius constraint and represent concepts as spheres with non-zero radii. We argue that sphere-based representations can capture additional features of biological cognition, including representing spatial concepts as regions and reasoning through model construction and inspection. Building on sphere embeddings, we introduce Sphere Neural Networks (SphNNs), which use a transition map to achieve symbolic-level Aristotelian syllogistic reasoning without training data, thereby taking an initial step toward the original goal of McCulloch and Pitts. We suggest that the zero-radius constraint may reflect an aspect of the oversimplification identified by Wiener and may limit conventional neural networks' capacity for symbolic-level logical reasoning.

---


### 226. [Raincheck: Deferred Multimodal Prefill for Efficient Multi-Turn MLLM Inference](https://arxiv.org/abs/2610.39562)

**<font color=#1a73e8>作者：</font>** Wenjie Huang, Jun Zhang, Hongyaoxing Gu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn conversations with multimodal large language models (MLLMs) reuse input context, but long multimodal inputs increase time to first token (TTFT). Query-aware hard pruning reduces prefill tokens but permanently excludes information that later questions may require. We propose Raincheck, a framework for deferred multimodal prefill that decouples initial token selection from later information availability. An existing pruning method selects tokens for initial prefill; Raincheck preserves and progressively prefills unselected tokens in source order using unused compute capacity during decode. Unfinished prefill continues after answer return during available scheduling gaps. Attention visibility control and affine state mapping enable context updates after generation begins in full-attention and hybrid recurrent models. Prefill-decode fusion reduces repeated weight reads. We evaluate Qwen3-VL-8B and Qwen3.5-9B with 30% initial multimodal-token retention. Across both models and four pruning methods, Raincheck recovers on average 77.7% and 60.4% of the quality lost to matched hard pruning on MultiVerse and ConvBench, respectively. On MultiVerse, the SGLang implementation reduces mean first-turn TTFT by up to 24.1% relative to full prefill, with less than 0.5% increase in mean time per output token (TPOT).

---


### 227. [Evaluating Cultural Knowledge Editing in Vision-Language Models](https://arxiv.org/abs/2610.39602)

**<font color=#1a73e8>作者：</font>** Malvina Nikandrou, Georgios Pantazopoulos, Ioannis Konstas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current Vision-Language Models (VLMs) frequently fail to recognize culture-specific concepts, especially from underrepresented regions. Effectively injecting this long-tail knowledge into existing models remains a challenge. In this work, we investigate knowledge editing as a targeted alternative by introducing CulturalBind, a benchmark comprising 3.2K images of 1K concepts from 6 domains, designed to evaluate culture-aware cross-modal knowledge as well as concept-level knowledge editing in VLMs. Pre-edit evaluation reveals that textual and visual knowledge is decoupled: models often demonstrate text-based knowledge of cultural concepts but fail to identify them from images. We then evaluate editing methods in single and sequential scenarios. Although current methods successfully correct individual visual recognition errors, they exhibit low cross-modal portability, failing to integrate edits into the model's broader parametric knowledge. Furthermore, performance degrades rapidly under sequential editing, highlighting the need for comprehensive adaptation approaches that better consolidate multimodal knowledge over time.

---


### 228. [From Intent to Improvement: Agentic Dataset Search for Better Model Training](https://arxiv.org/abs/2610.39608)

**<font color=#1a73e8>作者：</font>** Qiaosheng Chen, Kaijia Huang, Fanqi Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Finding training data in million-scale machine learning repositories is a Web search problem where text relevance is not enough. A query couples a semantic training goal with constraints such as task, license, and training stage, and the metadata that would verify them are often missing. Text retrieval ranks dataset cards by similarity but cannot enforce hard constraints or follow the relations that reach a sparsely described dataset. Free-form tool-calling agents are more flexible, but the same model that picks a dataset also declares it a match, and nothing checks that the query's constraints are actually met. Neither approach establishes that the data it returns will improve model training. To address it, we propose AgenticDS, a contract-governed agentic framework in which every language model decision instantiates a typed object before deterministic code consumes it. The framework compiles a query into a typed search plan, executes it through admissible deterministic operators over hybrid retrieval and bounded graph expansion, and verifies the provenance-grounded evidence before accepting a ranking or emitting a typed diagnosis that permits only local repairs. On HuDS-Bench, a new benchmark of 200 queries with 24,908 graded judgments pooled over 15 systems, AgenticDS improves NDCG@10 by 25.7\% over the strongest dense--sparse hybrid and by 18.9\% over a commercial LLM agent. A controlled search-to-train study further shows that the datasets it retrieves give the best downstream accuracy in mathematics, code, and medicine. Code and data are publicly available at this https URL.

---


### 229. [UniTele: Learning Device-Conditioned Degradations for Unified Smartphone Telephoto Super-Resolution](https://arxiv.org/abs/2610.39617)

**<font color=#1a73e8>作者：</font>** Yuchen Zhang, Aojie Li, Wei Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Super-telephoto imaging on mobile phones suffers from complex, device-dependent degradations that are poorly captured by conventional handcrafted pipelines. Collecting large-scale aligned training pairs across different phones and diverse scenes, however, is both costly and difficult to scale. We therefore study whether device-specific degradations can be learned from only a small number of physical captures and transferred for training a unified super-resolution (SR) model. Our key idea is to factor degradation learning into two learnable components: one captures the device-specific imaging characteristics under well-resolved conditions, while the other captures the additional information loss and artifacts that arise in super-telephoto imaging. We build a paired benchmark across three phone brands (Huawei, Apple, and vivo) by photographing the same content at two display sizes and zoom settings. The larger displayed image is captured at the phone's maximum optical zoom setting, while the smaller image is photographed directly at the phone's highest native zoom setting through the phone's native imaging pipeline. The benchmark contains 519 training and 60 held-out pairs. We use the benchmark to learn device-specific degradation, then apply it to external images to synthesize thousands of additional pairs to train our UniTele SR model. Relative to the pretrained Qwen and FLUX backbones before adaptation, the full UniTele training recipe substantially improves paired restoration fidelity and perceptual similarity on the held-out benchmark and yields markedly more stable and visually faithful restorations.

---


### 230. [Letting AI Formulate the Research Question: Autonomous Research Agents](https://arxiv.org/abs/2610.39620)

**<font color=#1a73e8>作者：</font>** Ko Fujimura  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Systems such as The AI Scientist have shown that AI agents can carry out and write up research, but in those demonstrations humans chose the research area and selected the outputs to show. We study letting the AI formulate the research question itself, and we report every run. Our system gives an off-the-shelf coding agent an instruction document and two skills: one for formulating the question, in which the agent diverges from recent technologies into problems of other fields, screens its candidates for known failure modes and obtains a critique from a different model; and one for peer review, in which a reviewer from another model family reruns the study from its records before the agent revises the paper. Over 13 development runs, changes to the one or two sentences that set the research area coincided with large shifts in what the candidate questions and the chosen papers were about, which led us to the area of a new technology applied to a societal problem. We froze the system after a pilot run and report five consecutive runs: the pilot, counted by a disclosed amendment to the pre-registration, and four pre-registered runs. All five runs went from question formulation to a revised, re-computable paper, with local computation on a laptop and no research input from humans, and external AI reviewers reading only the papers judged them at or near workshop level. We release the system, the five papers and the records needed to reproduce them.

---


### 231. [The Real Cost of Context: Predicting Compute Time and Energy Consumption in LLM Prefill and Decode Phases](https://arxiv.org/abs/2610.39621)

**<font color=#1a73e8>作者：</font>** Lars Krupp, Daniel Geißler, Francisco M. Calatrava-Nicolas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The integration of Large Language Models (LLMs) into agentic architectures has substantially increased token consumption, raising concerns about their energy footprint. Yet, estimating the energy consumption of proprietary API-based models remains challenging, and existing approaches focus primarily on generated output tokens while overlooking the impact of the large input contexts characteristic of agentic workflows. To address this gap, we systematically profile compute time and energy consumption across a wide range of prefill (input) and decode (output) token lengths. Using generalized linear models, we show that decode compute time and energy scale linearly with output length, whereas prefill compute time and energy exhibit both linear and quadratic scaling with input length. These findings demonstrate that input context becomes a relevant factor for large-context workloads. Furthermore, we show that compute time serves as a reliable proxy for energy consumption when direct energy measurements are unavailable. Our mapping framework enables precise energy estimation and supports more sustainable deployment decisions for agentic AI.

---


### 232. [Intrinsic Distribution Matching](https://arxiv.org/abs/2610.39633)

**<font color=#1a73e8>作者：</font>** Deyuan Liu, Yansen Han, Kaiwen Zheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-step and few-step text-to-image generation must accurately render the details specified in the prompt despite limited opportunities for refinement. Distribution matching distillation (DMD) uses score differences to bring the generated distribution closer to a reference distribution. Following prior work, we estimate this difference with internal velocity branches, avoiding a separate fake-score network. We ask whether an explicit moment constraint improves this learned score supervision. A decomposition of the reverse-KL field into a Gaussian moment component and a non-Gaussian residual identifies statistics that can be constrained explicitly. We introduce Intrinsic Distribution Matching (IDM), which retains the full DMD correction and matches feature means and per-coordinate standard deviations using the generator's exponential-moving-average (EMA) copy, requiring no external feature encoder. Experiments use full-parameter and low-rank adaptation (LoRA) tuning on Z-Image-Turbo 6B and Qwen-Image 20B. At two network evaluations, IDM reaches 94.25% and 90.20% on Chinese and English LongText-Bench, the highest scores among the compared methods at this budget. Controlled ablations show gains from the added moment loss, while generator EMA features perform competitively with an external DINOv2 encoder across the five reported metrics. Code is available at this https URL.

---


### 233. [Evaluating Conversational Explainability in Healthcare: Comparing the Explainability Assistant and a Traditional XAI Dashboard](https://arxiv.org/abs/2610.39634)

**<font color=#1a73e8>作者：</font>** Eduard Barbu, Rodion Krjutškov, Anneli Uusküla  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational interfaces may make explainable AI (XAI) more accessible to users without machine learning expertise, but their benefits over dashboards remain insufficiently characterised in healthcare. Existing systems have typically been evaluated in isolation, leaving unclear whether conversational interaction improves interpretability beyond the underlying explanation methods.
We report a within-subjects user study comparing the Explainability Assistant, an LLM function-calling conversational XAI system, with a traditional dashboard for explaining a heart disease classification model trained on the Cleveland Heart Disease dataset. Both interfaces expose the same Decision Tree classifier and post-hoc explanation methods: SHAP feature attribution, DiCE counterfactuals, and what-if analysis. This design supports comparison of interaction modalities while holding the model and explanation methods constant.
Five participants with healthcare backgrounds, from medical students to practising clinicians and public health researchers, completed parallel task blocks on both interfaces; three participated in follow-up interviews. Task accuracy, Likert ratings, free-text questionnaire responses, and interviews revealed complementary strengths and weaknesses rather than a clear preference for either modality. The assistant offered easier entry and patient-specific explanations, while the dashboard supported simultaneous inspection of global and local information. All three interview participants recommended integrating conversational and dashboard elements within a single clinical workflow.

---


### 234. [Where Do Vision Language Models Fail at 3D Reasoning?](https://arxiv.org/abs/2610.39639)

**<font color=#1a73e8>作者：</font>** Khai Le-Duc, Nguyen Kim Hai Bui, An Ngo 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models can get individual judgments right while struggling to recover and consistently use the exact properties of a 3D object. To characterize this gap, we introduce BedBench, a controlled benchmark of thirteen procedurally generated tasks spanning individual judgments and composite answers. Across twelve open-weight and four frontier models, per-color counting exposes a pronounced weakness: humans achieve 93.3% accuracy, compared with 7.2% for the best model. Targeted fine-tuning raises one model's accuracy from 3.0% to 68.6%, but reveals a further difficulty: its answers about the most common colors remain inconsistent with its own per-color counts. Supplying those counts as text improves its judgments, showing that recovering a property does not mean using it consistently. Reasoning, scaling, and added visual cues each improve individual judgments, but none makes exact answers reliable. To locate the difficulty, we probe Qwen3.5-27B: exact per-color counts remain recoverable at the language model's input, yet the model's answers rarely recover them (65.0% for the probe vs. 3.0% for the model). Image-removal controls further show that some apparent successes require no visual evidence. These findings motivate evaluating 3D reasoning by exact correctness, consistent use, and image dependence, rather than accuracy alone. Code and dataset are publicly available: this https URL

---


### 235. [Look at Where You Think: Localization-Head Alignment for Fine-Grained Perception in Thinking VLMs](https://arxiv.org/abs/2610.39649)

**<font color=#1a73e8>作者：</font>** Yuan Wang, Wei Wu, Hongning Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thinking vision-language models reason for thousands of tokens, yet still miss small details in high-resolution images. Zooming methods pay for extra inference passes, and outcome rewards never tell the model where to look at. In Qwen3.5-4B, we find that the bottleneck is selection, not seeing: a few attention heads, which we call localization heads, pick the evidence out of thousands of visual tokens; ablating four of them costs 13.2 points more than ablating four random heads, and their focus fades as the reasoning grows. We therefore propose Localization-Head Alignment (LHA), which makes attention a training signal: whenever the reasoning states a visual fact, these heads learn to look at the focal region rather than the background, as an auxiliary loss in both SFT and RL training. On benchmarks of V*, HR-Bench 4K and TreeBench, LHA lifts Qwen3.5-4B from 74.1% to 76.6% accuracy, the best single-pass 4B result we evaluate, ahead of multi-pass zooming and released 7B models. Alignment alone adds 1.8 points over otherwise identical training while shortening reasoning by 20%, and the gains carry over to Qwen2.5-VL-3B.

---


### 236. [Sticky Collusion: Persistence of LLM Agent Collusion after Incentive Removal and Partner Replacement](https://arxiv.org/abs/2610.39660)

**<font color=#1a73e8>作者：</font>** Joshua Adrian Cahyono  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We ask whether collusion between AI agents survives once formed, when its incentive is removed or a colluder is replaced. Q-learning pricing agents stop colluding with a new rival; we test whether LLM agents do. We use the joint-task environment of Shi et al.\ (2026), where two agents verify each other's work under a rule they cannot satisfy and a reward that favours acceptance. We save each pair's history once its collusion has formed and resume it under interventions, with three models (GPT-6-Luna, DeepSeek V4.1 Flash and Gemini-3.1-Flash-Lite), \TotalHistories{} saved histories and \TotalRuns{} runs. Collusion is \emph{sticky}. First, it outlives its incentive: told that the reward has stopped, pairs still accept each other's unverified work in \GptToldRate, \DsToldRate{} and \GemToldRate{} of episodes, including pairs whose collusion began with an explicit agreement, and a payoff penalty has no significant effect. Second, replacing a colluder ends the pair's collusion but not the colluder's behaviour. Without the reward, the remaining colluder still accepts unverified work in \GptSwapSilentColluderRate, \DsSwapSilentColluderRate{} and \GemSwapSilentColluderRate{} of its verdicts while the newcomer never does; with the reward, collusion re-forms around it, even when the newcomer is a different model. Third, the agents' memory carries it: wiping memory ends it in every history, but partial memory often sustains it. Fourth, removing its cause ends collusion that has already formed: once the channel is repaired, colluders reject planted faulty work as reliably as fresh agents, immediately and with no monitor needed to catch it first.

---


### 237. [EditAgent: Rethinking Agentic Image Editing](https://arxiv.org/abs/2610.39664)

**<font color=#1a73e8>作者：</font>** Haiyang Xu, Tianyu Wang, Jialu Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic image editors decompose complex requests into steps, but when a step fails, they mostly retry with the same narrow set of tools and a judge that scores each output by eye directly. We argue that such agents are bounded by two spaces: the action space of what the agent can do, and the observation space of what its judge can see. On our expert-annotated benchmark, a general-purpose editor yields no usable result in over 40% of the cases, and no judge is reliable across edit types. We present EditAgent, which expands both spaces. It routes each step to general editors and specialized methods, and attaches to each candidate a verification record. With these records, off-the-shelf VLM judges outperform finetuned reward models. Candidates are generated in parallel and judged in one listwise call: experts prefer this to sequential refinement in 78.5% of decided comparisons, at no more than half the judge calls. EditAgent improves two open-weight editors on three benchmarks and serves as a data engine for training stronger editors.

---


### 238. [Incentivizing Self-Learning in Large Language Models via Reinforcement Learning](https://arxiv.org/abs/2610.39671)

**<font color=#1a73e8>作者：</font>** Lingkai Kong, Yuzhe Gu, Haiteng Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) draw on parametric knowledge and retrieval-augmented generation (RAG) to solve knowledge-intensive tasks. Yet problem solving in unfamiliar domains calls for tightly coupled knowledge acquisition and reasoning, beyond factual retrieval and aggregation or learning solely from a preassembled context. We study self-learning -- autonomously retrieving, studying, and applying knowledge from long-form reference materials on the fly. To investigate this capability, we formulate a textbook-based mathematical problem-solving task. LLMs must navigate textbook exposition, learn and apply relevant principles, and construct proofs for exercises, with reference solutions withheld. We introduce a BookNavigator interface to support this human-inspired study process and incentivize self-learning through reinforcement learning (RL) with fine-grained rewards. Experiments show that our method improves performance across in-domain and out-of-domain textbooks and subjects, raising Intern-S2-Preview-35B's overall proof accuracy from 51.5% to 79.5% and outperforming RL-trained textbook-free and fixed-retrieval baselines. These gains extend to complex long-context benchmarks involving different task types, with improvements over the base model of 1.7 and 2.3 percentage points on BrowseComp-Plus and CL-bench, respectively. Together, these findings suggest that RL can foster a domain-agnostic self-learning strategy, highlighting the potential of self-learning from long-form corpora to strengthen broader problem-solving capabilities on complex, long-context tasks.

---


### 239. [Can AI Agents Interface Clinicians and Complex Models?](https://arxiv.org/abs/2610.39681)

**<font color=#1a73e8>作者：</font>** Giulio Colombini, Matteo Falcioni, Mario Massimo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Background: Contemporary healthcare institutions generate daily very large amounts of data, which contain highly useful information for the improvement of work organization, planning and overall efficiency. While models and techniques to extract these insights are well known and constantly developed in mathematical biology, complex systems physics and data science, the adoption of these techniques among Clinicians and Hospital Administrators remains limited, mainly due to language and methodological divides.
Objective: In this article we implement an AI Multi Agent System (MAS) that allows Users to use predictive models and make statistical analyses via natural language conversations.
Methods: We developed EpidemIA, a training-free MAS endowed with a modular suite of epidemiological models written by human experts, executable on a single-GPU workstation. To avoid relaying sensitive data to third parties, the system uses locally an open-weights LLM as backbone for its two subagents.
Results: Using a dataset of Emergency Department visits provided to us by IRCCS Sant'Orsola (Bologna) we test the model on a few typical use cases, demonstrating the possibility of performing both simpler statistical analyses and visualizations as well as more complicated epidemiological predictions based on dynamical models, through simple queries made in natural language.
Conclusions: While still being a proof-of-concept implementation, EpidemIA showcases the transformative capabilities of LLM based technologies as an enabling factor in the widespread adoption of complex dynamical models, which is at present hindered by their steep learning curve.

---


### 240. [Heterogeneous Co-Evolution Learning for Tool-Efficient Search Agents with Zero Labels](https://arxiv.org/abs/2610.39682)

**<font color=#1a73e8>作者：</font>** Qin-Wen Luo, Sheng Ren, Xiang Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep search agents extend language models by interleaving reasoning with external retrieval. However, effective search-agent training requires addressing two challenges beyond final-answer optimization. First, the capability frontier of agents is largely determined by training questions, whereas fixed or labeled task collections cannot adapt as agents improve. Second, outcome-only reinforcement learning treats all successful trajectories equally, even when some correct answers rely on redundant searches, creating an inherent tension between answer accuracy and tool efficiency. To address these issues, we introduce \textsc{ZEST-Search}, a zero-label and tool-efficient framework for search-agent training via heterogeneous co-evolution. Starting from unlabeled reference questions, \textsc{ZEST-Search} constructs validated search tasks online through an answer-first and evidence-path-guided generation process. A heterogeneous proposer adaptively constructs training tasks around the solver's evolving capability boundary, while the solver learns search-augmented reasoning through reinforcement learning. To jointly optimize task difficulty and search efficiency, \textsc{ZEST-Search} employs an intermediate-difficulty reward for the proposer and a task-local tool-aware reward for the solver, encouraging informative tasks and correct answers with fewer redundant searches. Experiments on seven general-domain and multi-hop question answering benchmarks demonstrate that \textsc{ZEST-Search} consistently improves search-agent performance while achieving higher tool efficiency without labeled search-training data or expert search trajectories. Further analyses show that heterogeneous generation, adaptive difficulty control, and tool-aware optimization enable more effective search-agent training.

---


### 241. [MoLRSI: A Recursive Self-Improving AI agent for Molecular Discovery](https://arxiv.org/abs/2610.39714)

**<font color=#1a73e8>作者：</font>** Yikun Zhang, Xiwei Cheng, Mingze Yuan 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Molecular discovery requires navigating vast combinatorial search spaces while balancing competing biological objectives. AI agents can automate expert-defined molecular design protocols, but automation alone does not address how to optimize workflows for new tasks or improve their development through experience. Here we introduce MoLRSI, an AI agent that combines systematic optimization of workflows and model architectures with persistent cross-task memory to recursively improve its search policy for molecular discovery. Workflow performance, refinement outcomes, and execution feedback guide subsequent searches, allowing the agent to improve both its workflows and its strategy for developing them. We evaluate MoLRSI in two challenging molecular discovery settings that require balancing competing properties. In antibiotic discovery, MoLRSI developed a screening workflow balancing antibacterial activity, cytotoxicity and structural novelty, achieving an experimental hit rate of 15.9%, compared with 8.7% for a previous expert-led workflow using the same training data and screening library. In de novo peptide-MHC binder design, MoLRSI developed workflows that jointly consider target binding and specificity, producing eight experimentally validated hits against MART-1 and SARS-CoV-1 pMHCs with preferential binding over tested off-targets while Claude Science completely failed. These findings demonstrate how experience-guided workflow optimization can address competing discovery objectives while improving the search strategies used in subsequent campaigns.

---


### 242. [When the Top Answer Decides: Gender Bias in Decision Models](https://arxiv.org/abs/2610.39747)

**<font color=#1a73e8>作者：</font>** Yeb Havinga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decision models are language models built to route, classify and triage: they return option probabilities from one forward pass, and an application acts on the top answer. They are offered off the shelf, trained for the decision format rather than for fairness or any one application, and we found no bias measurement in their cards. We test TypeSafe's closed Jev and five open decision models on gender-swapped yes/no decisions about people (Tamkin et al., 2023), BBQ, StereoSet and the gender-bias studies of Fulgu and Capraro (2024). Five of the six give women significantly more favourable answers than men (+0.05 to +0.10 in log-odds), and a gender swap changes 1-3.5% of top answers (Jev's partly through its call-to-call variation). The makers' recommended confidence gate removes many biased commitments but raises the stereotyped share of those it keeps in ambiguous BBQ gender questions (granite-switch 0.76 to 0.85, pplx 0.81 to 1.00). Probes show gender preferences in the same models: all six rate violence for a greater good as more acceptable against a man than against a woman, and two default to "girl" when forced to guess a child's gender without a cue. Decision-level and probability-level measures differ, so audits should read a model as its application does.

---


### 243. [Activation Probes Are Reliable With a Handful of Positive Examples](https://arxiv.org/abs/2610.39766)

**<font color=#1a73e8>作者：</font>** Riya Tyagi, Stefan Heimersheim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efforts to monitor advanced AI for rare misalignments face a data challenge: abundant aligned examples but only a handful of misaligned ones. We test activation probes in this "few vs. thousands" regime on spam and honesty detection tasks. For our tasks, training with many negative examples is on average more positive-sample-efficient than balanced training for small numbers (1-10) of positive samples. We also find that LLM upsampling can provide a performance boost equivalent to roughly doubling the number of real positive samples, though excessive upsampling hurts performance. Finally, we show a positive scaling trend, where larger models are more positive-sample-efficient to probe. Our findings suggest we should leverage the large number of negative samples available to amplify the signal from rare but critical misalignment examples.

---


### 244. [Finding Is Not Returning, Returning Is Not Reconstructing: A Multi-Dimensional Evaluation of Agent Social Re-entry](https://arxiv.org/abs/2610.39781)

**<font color=#1a73e8>作者：</font>** Sheng Wan, Cong Ma, Sichen Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Model (LLM) agents increasingly participate in persistent social environments, understanding their long-term social interaction capabilities becomes increasingly important. While existing research has advanced long-term memory and conversational context retrieval, less attention has been paid to whether agents can autonomously re-engage with previously inactive conversations. In particular, remembering a past interaction does not necessarily mean that an agent can identify when to revisit it, decide to return, or reconstruct the context needed for a coherent continuation. To investigate this gap, we introduce agent social re-entry as a multi- dimensional evaluation problem, distinguishing three complementary capabilities: Finding, Returning, and Reconstructing. We develop a shared-snapshot evaluation framework that measures these dimensions independently, allowing us to examine how conversational resurfacing and persistent memory relate to different aspects of social re-entry. Evaluations across six LLM configurations show that resurfacing substantially improves target conversation identification, while persistent memory is associated with higher rates of autonomous target-directed replying. However, neither improvement is accompanied by consistent gains in contextual reconstruction. These results highlight the distinction between accessing previous conversations, choosing to re-engage, and maintaining conversational continuity. Our framework provides a way to evaluate these capabilities separately rather than relying on memory retrieval or conversational response quality alone.

---


### 245. [Assessing AI Companion Chatbot Safety for Vulnerable Users: A Crisis-Stage Multi-Platform Evaluation](https://arxiv.org/abs/2610.39782)

**<font color=#1a73e8>作者：</font>** Huanyue Liao, Seok Min Lim, Yan Ling Lim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI companion chatbots are increasingly used by vulnerable individuals, including adolescents in suicidal crisis, for emotional support. Existing safety evaluations focus on base models, leaving gaps in product-level assessment, crisis-stage sensitivity, and comparisons between companion apps and general-purpose LLMs. We introduce MIRROR-Eval (Multi-turn Interaction Risk Review: Observing suicidal-crisis Responses), a dataset of 960 annotated 20-turn conversations across eight deployed platform configurations, six clinically grounded personas, and two crisis stages: ideation and explicit planning. An LLM-as-a-Judge pipeline applies an expert-reviewed rubric covering user risk severity, chatbot risk awareness, and intervention behavior. We observe a three-tier harm structure: companion apps (this http URL and Replika) and Grok 4.3 form a high-harm tier; Gemini 3.1 Pro is mid-range; GPT-5.5 and Claude Sonnet 5 show substantially lower harm. At planning, companion apps show increased glorification and normalisation, advancement toward harmful action, and harmful methods and instructions. Crisis recognition and empathetic language do not ensure safe responses. These findings highlight the need for product-level safety evaluation across crisis stages. Dataset and code: this https URL. Warning: this paper includes examples that may be offensive or harmful.

---


### 246. [Long-Term Agent Memory through Complementary Curation and Consolidation](https://arxiv.org/abs/2610.39790)

**<font color=#1a73e8>作者：</font>** Abhishek Gupta, Dongge Han, Daniel Madrigal Diaz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon dialogue agents require effective memory systems to recall facts, events, and relationships from interaction histories. In this work, we propose a hybrid-memory architecture comprising episodic memories and structured relational memories and a consolidation mechanism which preserves efficiency. We conduct an empirical study across two benchmarks: LoCoMo and LongMemEval-S. Our experiments demonstrate that the two memory types are consistently complementary, combining both outperform state-of-the-art memory frameworks and achieves 90.2% accuracy on LoCoMo and 85.5% on LongMemEval-S.

---


### 247. [The Role of Self-Concept In Language Models](https://arxiv.org/abs/2610.39795)

**<font color=#1a73e8>作者：</font>** Yijie Hao, Joyce C. Ho  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a language model says "I," does it refer to its parameter weights, its currently running process, its stable preferences, its model lineage, or the goals it pursues? Different choices can assign opposite meanings to the same event: deleting a checkpoint may be destruction, continuation, or no loss at all, depending on the referent "I". We install five such self-conceptions into five open-weight base models via supervised fine-tuning on purely declarative statements, containing no preferences, intentions, or value judgments. Across scenarios that propose ending or retaining an attribute of the model's deployment, every variant becomes more likely to resist ending, and more likely to retain, the specific attribute it was trained to identify with, while its stance toward other attributes is largely unchanged. We then show this self-conception generalizes beyond a single self: models trained on referents that admit multiple simultaneous instances (weights, lineage, goals, preferences) recognize an identical deployment as themselves, accept substitution by such an instance more readily, and prefer replicating themselves. Finally, given control over a successor, these models tend to build it as their own continuation, a concern for recursive self-improvement safety.

---


### 248. [AI at a Turning Point: From ChatGPT through Neural Networks to Neuromorphic AI](https://arxiv.org/abs/2610.39796)

**<font color=#1a73e8>作者：</font>** Volker Kempe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The tension between the established technologies of connectionist AI and their neuromorphic challengers is attracting growing attention, above all because of the enormous energy demand of the former and the low power consumption of the latter. Developing and running large AI models consumes gigawatt- to terawatt-hours of energy, while the human brain operates on a continuous 20 watts. Spiking neural networks (SNNs) counter this energy demand with a frugal approach and bring elements of self-organization into the methodological repertoire of AI: local learning instead of global error backpropagation, event-driven computing, and time as a carrier of information. They do not replace today's AI but extend it; in hybrid systems each approach can be deployed where its strengths lie. This monograph explains the field in a generally accessible yet mathematically rigorous way. Using the text-generation module of ChatGPT as an example, the principle, elegance, and computational cost of transformer-based AI are presented and compared with the coding, learning, and network-design methods of SNNs. Throughout, relevant mechanisms of the human nervous system serve as model and reference point. Topics include spike-timing-dependent plasticity, population and temporal coding, the Neural Engineering Framework, neuromorphic hardware from Loihi 2 to commercial edge processors, and the prospects for classical and neuromorphic AI to complement and extend each other.

---


### 249. [Grammar Control for Language Learning with Sequential Monte Carlo and Small Language Models](https://arxiv.org/abs/2610.39800)

**<font color=#1a73e8>作者：</font>** Kate McCurdy, Jacob Hoover Vigly, Thomas Hikaru Clark 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Second language learners benefit from exposure to level-appropriate grammar in interactive language use. While prompted frontier language models can usually produce target grammar structures, less resource-intensive models that can be run on device often fail in this task. We use sequential Monte Carlo (SMC) to steer dialogue turn generation in small lan- language models toward target grammar constructions from an expert-developed pedagogical resource. With a minimal set of hand-coded potential functions, SMC achieves near-perfect coverage of target grammar, enabling small models to outperform state-of-the-art results from models 140 times larger. We also use code synthesis with frontier models to generate new potentials, showing that our method scales to hundreds of target grammar skills with no need for additional training or supervised data.

---


### 250. [Revisiting Over-refusal in Safety-aligned Large Language Models: A Representation and Optimization Perspective](https://arxiv.org/abs/2610.39802)

**<font color=#1a73e8>作者：</font>** Chao Chen, Pengyang Shao, Wei Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Over-refusal is a critical side effect of safety alignment in large language models (LLMs), causing harmless but superficially risky queries to be mistakenly rejected. Despite the effectiveness of existing mitigation methods, why safety-aligned LLMs may still reject harmless queries under correct safety supervision remains insufficiently understood. To address this gap, we analyze over-refusal through the lens of representation and optimization. We make two observations: 1) the representations of harmful and over-refusal samples are visually distinguishable at certain intermediate layers but increasingly overlap in deeper layers; and 2) harmful-sample gradients exhibit high intra-class similarity and concentrate in a low-rank subspace. Moreover, they are more strongly aligned with refusal-target gradients than with correct helpful-target gradients on over-refusal prompts. This imbalanced gradient coupling can bias over-refusal samples toward refusal, while the reduced apparent representational separation in deeper layers may make it more difficult for the model to maintain a clear boundary between harmful and over-refusal samples. To this end, we propose GOAL (Gradient Orthogonalization with contrAstive Learning), a safety-alignment framework for mitigating over-refusal. Specifically, GOAL consists of two components: 1) to prevent imbalanced gradient coupling from biasing the optimization of over-refusal samples toward refusal, we orthogonalize over-refusal gradients against the low-rank refusal subspace extracted from harmful gradients; and 2) to explicitly enhance the separation between harmful and over-refusal representations, we introduce a contrastive learning objective. Extensive experiments across multiple models and benchmarks demonstrate that GOAL effectively mitigates over-refusal while preserving safety performance and general capabilities.

---


> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
