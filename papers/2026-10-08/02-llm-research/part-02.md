# 🧠 大模型相关研究 | 2026年10月08日

> 本类共 **303** 篇论文：已确认 **280** 篇，待复核 **23** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-303](./part-07.md)

---

### 51. [Can LLM-assisted regularization increase forecast accuracy for migration flows in low data regimes?](https://arxiv.org/abs/2610.07208)

**<font color=#1a73e8>作者：</font>** Nathaniel T. Hindman, Fabricio Murai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting migration flows remains a significant challenge for traditional gravity-based forecasting models, which primarily rely on structured socio-economic indicators such as economic disparity, political stability, and geographic distance. This work investigates whether Large Language Models (LLMs) can improve migration forecasting by extracting contextual migration-related signals from news articles and incorporating them into a weighted Lasso forecasting framework through feature-specific regularization penalties. The proposed framework uses hierarchical LLM inference pipelines to classify migration-related push--pull signals from news data and evaluates the resulting forecasting performance across multiple migration corridors between November 2021 and November 2022, including Mexico--United States, Ukraine--Poland, and Syria--Turkey. Experimental results showed mixed performance across migration corridors and modeling strategies, and no single regularization approach consistently outperformed the others across all experiments. The best-performing Mexico configuration, which consisted of a gravity-based model augmented with the proposed push--pull ratios, achieved a Mean Absolute Percentage Error (MAPE) of 17.15%, while the strongest Syria configuration achieved a MAPE of 29.29% using Direct LLM-Lasso. For Ukraine, the best-performing configuration used LLM-Assisted Regularization (AR) and achieved a MAPE of 41.05%. Overall, the results suggest that contextual article-derived features and LLM-guided regularization can improve migration forecasting under certain conditions, although migration corridor characteristics, article volume, and hyperparameter configuration strongly influenced performance.

---


### 52. [Reward-Driven Learning under Prompt-Level Differential Privacy](https://arxiv.org/abs/2610.07212)

**<font color=#1a73e8>作者：</font>** Jiachen Zhao, Antonia Januszewicz, Taeho Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) trains a language model on problems that may themselves be confidential, and the trained model can reveal which problems it saw. We study RLVR under prompt-level differential privacy: the released weights must be ({\epsilon},{\delta})-differentially private with respect to the presence of any one training problem. Taking the group of responses to one prompt as the privacy record, our method aggregates their gradients, clips the prompt's contribution once, adds Gaussian noise, and composes the privacy loss across updates, so the budget depends on neither the number of responses per prompt nor the clipping norm; to our knowledge this is the first differential privacy guarantee for RLVR training. We train Qwen2.5-1.5B-Instruct with LoRA at a per-run budget of {\epsilon}=8 and compare, on the same prompts and at the same budget, a control that removes only the reward signal and two private supervised fine-tuning recipes. The reward signal improves accuracy over the control by 2.65 points on MATH and 3.24 on GSM8K, in every seed; the improvement survives a format-robust scorer, at 1.3 points on MATH, and is not explained by response length. At the same budget the private model outperforms both supervised recipes on MATH and GSM8K by 2.3 to 3.8 points, retains 85--90% of the gain of non-private GRPO on these tasks, and on MATH the noise of an eightfold tighter budget costs at most 1.2 points. The reward effect also carries to CommonsenseQA, an exploratory non-mathematical task. Verifier feedback thus remains a usable learning signal under prompt-level privacy.

---


### 53. [Cascadia: Resident 975B MoE Inference on Eleven AI PCs](https://arxiv.org/abs/2610.07219)

**<font color=#1a73e8>作者：</font>** Tate Berenbaum, Matias Parij, Muthaiah Venkatachalam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts models make nearly trillion-parameter capacity accessible with sparse per-token computation, provided that the serving system can distribute the weights and coordinate their execution. We present Cascadia's resident execution of Inkling, a 975B-total/41B-active-parameter model, on eleven Intel Core Ultra X7 358H AI PCs, each with 64 GB of memory, Arc B390 integrated graphics and gigabit Ethernet. We contribute a custom resident MoE engine that preserves Inkling's routing rules, constructs compressed graphs for OpenVINO's fused iGPU primitives, and coordinates FP16 expert computation with FP32 output restoration. The engine fits six consecutive decoder layers per machine and represents dense feed-forward blocks as all-active expert slices, reducing measured dense-layer call time from approximately 8.1 to 4.5 ms. A streaming pipeline coordinates concurrent generation, while captured-state draft evaluation measures agreement with the deployed numerical path. Paired measurements at fifteen concurrency levels from 1 to 176 streams reach 60.29 aggregate decode tokens/s at 88 streams, with 46.87 tokens/s over the complete serving phases. At fifteen streams, median first-token latency is 6.05 s. Raising the context budget from the 1,024-position default, real prompts of 1k to 64k tokens recover the embedded code in all 19 measured answers, with first-token time growing as $aN+bN^2$ and decode latency growing approximately linearly, both bounded by a single-threaded CPU attention loop rather than by memory, which holds 512k positions per stream. Evaluation on captured fleet states separates the effects of vocabulary selection and weight quantization on draft agreement. Together, these contributions establish an execution and evaluation approach for large sparse models on distributed client systems with shared CPU-GPU memory.

---


### 54. [TIDE 2.0: an open, model-agnostic engine for keyed de-identification of clinical notes](https://arxiv.org/abs/2610.07224)

**<font color=#1a73e8>作者：</font>** Jose D. Posada, Somalee Datta, Priya Desai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical notes capture most of what is documented about a patient's care, but they cannot be used for research until protected health information (PHI) is removed. De-identification is often treated as a detection problem. Detection alone is not sufficient: redaction strips clinical content along with identifiers, date blanking destroys the temporal intervals needed for longitudinal analysis, and assigning a fresh random surrogate at each occurrence breaks links between a patient's notes. We present TIDE 2.0, an MIT-licensed engine with two separable stages: an interchangeable recognizer and a keyed anonymizer. Both run on hardware the institution owns. Surrogates are generated cryptographically with no stored linkage table. Dates shift by a per-patient, interval-preserving offset; each value receives the same surrogate across all occurrences under a given key; and a release produced under a new key cannot be linked to earlier releases. We also release TIDE2-Sentry, a recognizer distilled from a large language model. On two gold-annotated corpora from two institutions, the default configuration reached span-level recall of 0.88 in-domain and 0.77 on the second institution's corpus, at precision 0.88 and 0.87. We report recall and precision per category alongside these aggregates. The engine is open source, and the recognizer is available under a gated research-use agreement, so institutions can run, inspect and extend both within their own environments.

---


### 55. [Minimal Witness Reinforcement Learning](https://arxiv.org/abs/2610.07226)

**<font color=#1a73e8>作者：</font>** T. Y. Tsui, Zihao Ye, Pengxiang Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ``What are the irreducible conditions that are sufficient to produce an outcome?'' is one of the most common questions that recur across computation and science. Its answers, the minimal sufficient witnesses, are what we mean by explanations, mechanisms and reasons. These problems usually ask for multiple minimal witnesses, yet standard RL methods may reveal only one solution or redundant ones. We formalize this problem as minimal-witness identification and introduce Minimal-Witness Reinforcement Learning (MWRL). MWRL takes the union of the sets certified by successful proposals sampled from the policy and credits each proposal for the coverage the group union would lose without that proposal. This credit assignment, derived directly from the problem definition, unifies the demands for minimality and recovery of alternatives from a single black-box verifier bit. Under this principle, we derive a value iteration planner that recovers the entire family of witnesses and a policy gradient method that can scale to large language models. Across different experimental settings, MWRL recovers most minimal witnesses, while other methods return redundant supersets or a single witness. By making witness families learnable from verifier feedback, MWRL expands the scope of reinforcement learning beyond single-solution optimization. Our code is available at this https URL.

---


### 56. [Learning What to Distill: Bilevel Top-K Token Selection for Self-Distillation in Large Language Models](https://arxiv.org/abs/2610.07247)

**<font color=#1a73e8>作者：</font>** Heng Liang, Xinwen Zhang, Hongchang Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models have shown strong reasoning capabilities, but their high inference costs make knowledge distillation an important approach for transferring such capabilities to compact models in resource-constrained scenarios. On-policy self-distillation further reduces the reliance on external large teacher models while improving the reasoning ability of compact language models. However, existing methods typically either distill all token positions uniformly or select tokens using fixed heuristic criteria, assigning the same distillation strength to the selected positions rather than adaptively learning which tokens are most beneficial for distillation. To address these limitations, we propose BiToK-SD (Bilevel Top-K Token Selection for Self-Distillation), a bilevel-optimization-based token selection method that learns where distillation should be applied during on-policy self-distillation. Specifically, BiToK-SD is formulated as a bilevel optimization problem, where the lower-level problem models Top-K token selection as a differentiable threshold-based relaxation, allowing the selected positions to adapt as the student policy evolves, while the upper-level problem performs knowledge distillation on the selected positions. Experiments on mathematical reasoning benchmarks show that BiToK-SD achieves the best average performance among all compared methods while requiring only lightweight additional computation.

---


### 57. [Internalizing Agent Experience into Diffusion Model Weights via On-Policy Context Distillation](https://arxiv.org/abs/2610.07250)

**<font color=#1a73e8>作者：</font>** Wenxuan Wang, Zekai Liu, Weinan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wrapping an image generation model in an agentic harness can effectively boost Text-to-Image task performance: the harness can leverage memory, skills, workflow orchestration, result verification, and iterative refinement to continually construct and revise prompts, thereby eliciting better images. These gains, however, remain external to the diffusion model and are realized only while the full harness runs. We propose Diffusion On-Policy Context Distillation (D-OPCD), which treats the agent-improved prompt as privileged context and distills the knowledge encoded in the agent harness into the weights of the diffusion model, so that the model retains part of the harness's benefit when conditioned on the original query alone. Using a Text-to-Image agent equipped with our proposed Auto Skill Evolver (ASE), we show that D-OPCD can internalize harness capabilities into the generator's weights, raising the average direct-generation score from 60.52 to 65.09 across four benchmarks. With this knowledge absorbed into the weights, the harness can shed its saturated skills and resume evolving: a second ASE round on the updated generator improves on a skill-free harness by additional 1.83 points, pointing toward text-to-image systems in which harness and model keep improving each other through continual co-evolution.

---


### 58. [Efficient Auditing of Adversarial AI Agent Behavior from Agent Traces](https://arxiv.org/abs/2610.07256)

**<font color=#1a73e8>作者：</font>** Eugene Zhang, Cheng-Yun King Yang, Dongyan Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents powered by large language models (LLMs) can perform complex tasks but may harm the systems they operate in, either intentionally or unintentionally. Existing agent monitoring approaches rely on rule-based guardrails or LLM-based trace auditing. However, rule-based guardrails can be bypassed through obfuscation and may miss harmful actions beyond their predefined rules, whereas applying an LLM to audit every action is costly. We present a two-stage agent trace auditing framework. The first stage uses single-event and trace-sequence rules to select pending actions for inspection; the second uses an LLM audit agent to examine each selected action in the context of the agent's preceding trace before execution. We jointly refine the gate rules and audit instructions using training data, allowing the framework to adapt to complex agent behaviors rather than relying solely on predefined rules. On the public benchmark OpenAgentSafety, our framework reduces the average number of LLM audits from 8.15 to 2.33 per run and token usage from 47.8k to 14.6k, with a detection rate of 72.8\% compared with 81.5\% when every action is audited. In two simulated multi-agent case studies, the framework flags all malicious traces while reducing audit token usage by more than 80\%.

---


### 59. [MemMux: Runtime Verification and Honest Resource Attribution for Fleets of Parallel Coding Agents](https://arxiv.org/abs/2610.07257)

**<font color=#1a73e8>作者：</font>** Sumanyu Muku  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developers increasingly run a fleet of coding agents side by side on one workstation. The tools they reach for, terminal multiplexers like tmux and a new generation of agent managers, were built to arrange windows, not to govern memory. When ten agents each spawn language servers, test runners, and browsers, no standard tool can say how much memory belongs to which agent, confirm that a terminated agent's descendants are gone, notice a child that has escaped its agent, or keep the machine off the swap cliff when an OOM kill would silently discard uncommitted work. We treat these as runtime-verification problems: an agent-hosting substrate should continuously emit observable signals an operator or auditor can check while agents run. We present MemMux, a local runtime that turns resource governance into checkable signals (per-agent attribution, complete reclamation, escaped-process visibility, bounded footprint under overcommit, and monitoring overhead), with a claims-disciplined benchmark against tmux, a purpose-built agent multiplexer, and a raw-process baseline on identical workloads. Under a binding memory budget on a Linux host, MemMux keeps the fleet under budget (7.5 GiB) with zero swap by admitting a subset and reclaiming under pressure, while the ungoverned tools run every agent, pin the machine at its RAM ceiling (2x over budget), and spill about 2 GiB into swap. MemMux reclaims 100% of a terminated agent's process subtree where the raw baseline strands half of it, and it alone surfaces escaped children (10 of 10 detected). We report the cost: the 1 Hz attribution scan runs near 0.6% CPU at one agent but 2.7% at ten, above our 2% target. Running the harness on real Claude Code sessions shows 100% attribution and low overhead carry over to live agent trees. We release the engine, benchmark, and a one-command reproducer.

---


### 60. [Lineage-Aware Memory Governance: A Derivation-Gated Framework for Privacy-Preserving Column-Level Access Control in Enterprise AI Agents](https://arxiv.org/abs/2610.07258)

**<font color=#1a73e8>作者：</font>** Venkata M Sangaraju, Sudhir Vissa  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Enterprise AI agents that share a memory store face two unaddressed risks: sensitive data can leak through legitimately computed results the requester could not derive, and departments can silently compute a same-named key performance indicator (KPI) through conflicting logic. Existing agent-memory systems (e.g., MemGPT, Zep, A-MEM) gate retrieval by content, ownership, and role, not derivation, missing a cached insight that embeds a forbidden column. We introduce the Analytical Memory Unit (AMU), a memory schema that attaches a full derivation (lineage) graph to every cached result, gated by a retrieval policy that serves a hit only when the requester is authorised for every column touched. Provided lineage recording is complete, we prove by construction that the policy blocks retrieval of results derived from a sensitive column outside the requester's permissions, at O(n) worst case -- a conditional design guarantee, not an empirical claim, that excludes derived features encoding sensitive information without naming their source. Eliminating measured leakage required 75-90% recorded lineage completeness, so we treat 90% as a conservative deployment target. Across six experiments, lineage-gated retrieval removes the 18.8-25.5% cross-department leakage naive content-gated memory suffers, keeping 81.5-82.6% of memory reuse at 13.8 microsecond worst-case overhead. A real-agent proof-of-concept with LLM-generated SQL is consistent with the guarantee: zero leaks over 9 round-trips, two conflicts caught automatically -- though a feasibility demonstration, not evidence of production viability. This offers a practical governance layer for shared agent memory, complementing source-layer access control and supporting EU AI Act compliance.

---


### 61. [Verifying Coordination in Parallel Coding Agents: NP-Bench and a Scheduling Planner](https://arxiv.org/abs/2610.07261)

**<font color=#1a73e8>作者：</font>** Sumanyu Muku  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A team of coding agents can look fine agent by agent yet fail as a team: each passes its own tests while the merged result is broken, and single-agent evaluation never catches it. As teams run several LLM coding agents in parallel on one codebase, the agents collide: two rewrite the same function, one codes against a contract a teammate just changed, and integration fails after the work is done. Most coordination tools react (watch for a conflict, then warn), but at agent speed the warning arrives after the wasted edit. We recast the problem as scheduling: take each work item's declared scope, partition the work into disjoint scopes, and order merges along the producer->consumer graph, all up front. We build this planner into Nerveplane and evaluate it with NP-Bench, an environment-grounded three-arm benchmark (no coordination; reactive detection; proactive planning) that verifies integration off a real git merge, both in a deterministic simulation and with live agents. The planner lifts clean-integration from 1/9 to 9/9 scenarios and cuts merge conflicts from 13 to 0, with a gap that grows in the number of agents. On a live breaking contract change it rescues an outcome both baselines miss on every seed: the clean-integration rate rises from 0 (no coordination and reactive detection) to 1.0 on a frontier model and 0.6 on a small one, while agents respect assigned scopes (0/5 leakage). A cross-session memory drops the repeated-mistake rate from 1.00 to 0.00 on strong and weak models alike. We also report a negative result: routing facts to agents does not rescue long-context accuracy at window-fitting scales; its value is cost and capacity, not attention. Across two capability tiers and two vendors, the benefit did not shrink as models got stronger, because it comes from how work is allocated, not model reasoning.

---


### 62. [What Words Keep of a Place: Zero-Shot Language Reasoning for Cross-View Geo-Localization](https://arxiv.org/abs/2610.07269)

**<font color=#1a73e8>作者：</font>** Ayesh Abu Lehyeh, Jay Hwasung Jung, Safwan Wshah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view geo-localization is commonly solved as an image retrieval problem, matching a ground-level image against a database of satellite tiles through a jointly trained embedding. Such models are accurate, but they need large paired supervision and cannot show what evidence supports a match. In this paper, we study a different question: how much of this task can be solved through language alone? We prompt a multimodal large language model (MLLM) to describe each ground panorama and each satellite tile as structured text, and localize by comparing these descriptions. No component is trained. We evaluate on 9,826 VIGOR pairs from four U.S. cities, in three settings. First, the descriptions are faithful but not discriminative. They agree closely across the two views, yet ranking the full pool by description similarity almost never returns the correct tile (0.39% Recall@1). Second, we narrow the pool to ten neighboring tiles, as a coarse prior would do. The same descriptions now become useful: an MLLM judge that scores structural consistency doubles random ranking and matches a strong lexical baseline. It also states which fields of the two descriptions agree and which conflict, which an embedding distance cannot do, and which we see as a step toward interpretable localization. Third, we place the judge on a trained visual retriever. On the queries it ranks wrongly, reranking from images works, while reranking from our descriptions does not (23.5% against 10.7% Recall@1). Scene structure survives the conversion into language, while the fine appearance detail needed to separate nearby places does not. Code and prompts are publicly available at this https URL.

---


### 63. [Does the Model Use the Feature? Separating Steering from Mechanism in LLMs](https://arxiv.org/abs/2610.07270)

**<font color=#1a73e8>作者：</font>** Tong Che, Yilong Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Internal features in LLMs are often interpreted as mechanisms when they track a concept and their manipulation changes a related behavior. Yet steering can push a feature far outside its natural range, where its effects need not reflect the model's own computation. We examine this inference and propose an empirical contract whose tests evaluate features at values observed on natural inputs. One test copies a feature's value from an input that shows a behavior into a matched input that does not (installation) or the reverse (removal); the other restores the feature after an upstream edit (downstream rescue). Installation measures how far the feature suffices for the behavior; removal and downstream rescue measure how much the model uses it. Applied to three kinds of representations, the two strengths separate sharply. The published unknown-entity latent strongly steers knowledge abstention, yet installing observed values from either published latent into matched prompts transfers only a small fraction of the natural known--unknown abstention contrast. Dense known--unknown directions show opposite asymmetries between installation and removal in Gemma and Llama, and how fully a released subject--verb agreement feature set reproduces and restores the behavior depends on how its values are written into the model. Tracking a concept and steering a behavior therefore do not by themselves show that the model uses a feature, and each conclusion holds only for the intervention tested.

---


### 64. [Mapping E-textiles Design Pain Points and Generative AI Opportunities: Insights from Workshops in Shanghai and Winchester](https://arxiv.org/abs/2610.07296)

**<font color=#1a73e8>作者：</font>** Zhuchenyang Liu, Nianchong Qu, Yao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> E-textile design involves complex decisions across materials, sensor and actuator structures, fabrication, garment integration, and data processing. It typically requires iterative prototyping and testing, which are time- and labour-intensive, while few practitioners possess cross-disciplinary expertise across all relevant domains. To identify current bottlenecks and explore how Generative AI (GenAI) might support the design process, we conducted two half-day co-design workshops, one in Shanghai and one in Winchester, with practitioners from materials science, electronics, garment design, human-computer interaction, and manufacturing. Twenty practitioners participated in the Shanghai workshop; ten of them had prior experience in e-textiles and form the contributing sample analysed here. A further ten practitioners participated in the Winchester workshop. Participants mapped their own design pipelines, annotated bottlenecks, and proposed where GenAI could provide support. Rather than presenting a ranked list of opportunities, we report a process map that indexes each proposed GenAI role to the pipeline stage at which practitioners located it, together with the conditions on which they stated its usefulness would depend. Across both sites, practitioners consistently identified domain-specific operational barriers, including data scarcity, the disconnect between prototyping and manufacturing, and trade-offs in material-hardware integration. They also emphasized that the primary barrier to GenAI-driven e-textile design is not general model capability, but the lack of standardized, machine-readable representations of e-textile designs. Based on these findings, we identify four classes of domain-tailored AI tools that could support future e-textile design processes.

---


### 65. [Polar: LLM-Powered Synthesis of Real-World Cyber Evidence for Prioritization and Mitigation](https://arxiv.org/abs/2610.07298)

**<font color=#1a73e8>作者：</font>** Luoxi Tang, Yuqiao Meng, Ankita Patra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber threat analysis increasingly depends on evidence distributed across vendor advisories, vulnerability databases, and threat intelligence sources. Turning these fragmented observations into timely decisions requires models to connect technical severity with evolving exploitation evidence and available defensive actions. We present POLAR, an LLM-powered framework for synthesizing real-world cyber evidence into threat-centric assessments for prioritization and mitigation. POLAR first disentangles overlapping incidents and grounds each threat in source-linked evidence. For prioritization, it infers severity metrics from cyber evidence and combines the resulting assessment with temporally ordered exploitation signals to estimate near-term exploitation likelihood. For mitigation, it links the synthesized threat data to authoritative remediation knowledge and organizes applicable actions according to threat urgency and operational constraints. We evaluate POLAR on real-world vulnerability evidence collected from public resources and compare it with multiple baselines. Across heterogeneous incidents and zero-day settings, POLAR improves threat ranking and mitigation retrieval while producing evidence-linked intermediate assessments that support analyst inspection. The results establish evidence synthesis as a practical foundation for LLM-based cyber decision support across related security tasks.

---


### 66. [Kurate: Scalable Scientific Quality Analysis](https://arxiv.org/abs/2610.07306)

**<font color=#1a73e8>作者：</font>** Matthew J. Vowels, Jamie Cummins  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific search systems can find papers that are relevant to a question, but they generally do not assess the quality of the evidence that those papers provide. We present Kurate, a system that uses large language models (LLMs) to assess the quality of published studies. Kurate uses both the paper and its related documents (e.g., the study's trial registration and protocol), and links each of its judgments to the passage of text on which that judgment is based. We applied Kurate to a corpus of 4,347 papers (3,913 of which report randomized trials) and scored each paper on 8 dimensions of study design and reporting: specifically, statistical power, causal identification, preregistration, selective reporting, measurement validity, analysis prespecification, reporting transparency, and conflict of interest and funding. Across the corpus, we found that papers most often exhibited issues with statistical power, selective reporting, and analysis prespecification, although average quality differed between clinical areas. When compared against expert annotations of 60 held-out clinical-trial documents, the information Kurate extracted matched the expert label in 221/242 protocol scorepoints and 294/370 results-publication scorepoints, with AC1 0.94 and 0.81, respectively. Using a well-reputed, high quality clinical trial as a worked example, we show how a single paper's overall grade breaks down into separate judgments, with each linked to specific evidence from the trial's registration, protocol, and published report. Together, these results show that large-scale quality assessment of this kind is feasible, and that it can be used to address meta-scientific research questions.

---


### 67. [The Right Memory in the Wrong Context: Verifying Retrieval Admissibility in Long-Term Agent Memory](https://arxiv.org/abs/2610.07309)

**<font color=#1a73e8>作者：</font>** Zi Wang, Xingqiao Wang, Emmanuel Addai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term-memory agents can retrieve relevant information that is inadmissible for the current request because it belongs to another principal, violates policy, or reflects an incompatible lifecycle state. Recall and final-answer accuracy do not reveal this: a route can appear safe by missing required evidence, while a correct answer may follow inadmissible prompt exposure. We introduce a retrieval-admissibility verification framework that assigns each memory-query pair one of three statuses (admissible, inadmissible, or unresolved), compares routes at matched required-evidence recall with bounds for unresolved cases, and tracks memory IDs through prompt exposure while linking exposure to target-level disclosure. We evaluate its stages on separate, non-pooled populations. A post-hoc top-20 reanalysis of frozen rankings from two public long-term-memory benchmarks, RHELM and MemOps, covers 3,767 queries. All released anchors lie within trusted query namespaces; with within-namespace scores unchanged, off-namespace filtering cannot lower their ranks. Top-20 anchor recall increases from 0.432 to 0.533, 80% recall feasibility from 0.237 to 0.311, and exact similarity evaluations decrease by 98.3%. In a frozen 72-case development diagnostic, a released-metadata reference preserves required evidence, whereas neither text-only verifier detects violations under the 1% required-anchor false-denial limit. Across 1,523 paired benchmark-native cases, namespace routing is associated with judged-accuracy gains of 0.053-0.068 across three readers; recall also changes, so this comparison is observational. In 16 controlled exposure scenarios, only one of four reader-specific 95% confidence intervals excludes zero for relevant-inadmissible literal disclosure (+0.156, 95% CI [0.031, 0.312]). Results motivate separate verification of candidate support, admissibility, prompt exposure, and answer disclosure.

---


### 68. [From Sandbox to Enforcement: Confidence-Qualified Threat Intelligence for Critical Infrastructure](https://arxiv.org/abs/2610.07310)

**<font color=#1a73e8>作者：</font>** Nikolaos Kekatos, Mihaela Curcă, Georgios Koutidis 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security operations centres and national incident-response teams defending critical infrastructure collect abundant threat data yet struggle to turn it into actionable intelligence. A malware sandbox produces detailed behavioural evidence, but as a large, unranked report whose confidence is unstated. We present CG-CTI, an operational pipeline that converts live sandbox output (CAPEv2) into STIX 2.1, correlates it in a knowledge graph with other critical-infrastructure sensors, and attaches to every intelligence object an explicit confidence status derived from provenance, cross-source corroboration, and observation durability. This status gates automated action: only corroborated intelligence is eligible for automated enforcement, while lower-confidence objects are routed to analyst review or kept as context. A grounded language-model stage then narrates the confidence-qualified evidence, where each statement either cites a supporting object or is marked unsupported, so fabricated references are removed before analyst review. We implement CG-CTI within the CYBERGUARD project, whose consortium includes Romania's national cyber-security directorate, and evaluate it against the live sandbox on a labelled malware corpus, measuring conversion validity, indicator yield, technique coverage, corroboration, enforcement eligibility, latency, and summary grounding. CG-CTI turns fragmented sandbox output into corroborated, confidence-ranked, and auditable intelligence for critical-infrastructure defence.

---


### 69. [Understanding and Mitigating Inference-Time Overreliance Using Agentic Memory](https://arxiv.org/abs/2610.07311)

**<font color=#1a73e8>作者：</font>** Luoxi Tang, Yuqiao Meng, Nilesh Auradkar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic memory allows LLM agents to reuse past experience, yet retrieved memories can also distort inference even when they are benign, correctly stored, and appropriately retrieved. We study this failure mode, which we call memory over-reliance. Across benchmarks and memory architectures, we find that memory is useful when past experience transfers to the current task, but can become misleading when only part of the evidence transfers. Failures are strongest under partial query-memory overlap, a pattern further confirmed by controlled experiments thatvary the amount of overlapping evidence. Motivated by this finding, we propose MEMTRIM, a plug-and-play framework that indexes memory evidence at write time and controls its reuse at read time. MEMTRIM removes repeated or conflicting evidence while preserving useful memory-specific information, requires no retraining, and applies to both embedding-based and structured memory this http URL show that MEMTRIM reduces memory overreliance while preserving the benefits of useful memory across models and memory settings.

---


### 70. [Structuring MoE Expert Selection for Agentic Reinforcement Learning](https://arxiv.org/abs/2610.07332)

**<font color=#1a73e8>作者：</font>** Bolian Li, Ting-Yao Hu, Cheng-Yu Hsieh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents are frequently implemented using sparse mixture-of-experts (MoE) models, yet the co-design of agentic behavior and MoE structures remains underexplored. In this work, we comprehensively study the connections between agentic post-training and MoE expert selection. In off-the-shelf MoE models, we observe expert selection exhibits a specialized structure that naturally aligns with agentic trajectories. Specifically, expert routing overlaps more between turns where the agent performs semantically similar operations (e.g., READ, UPDATE) than between turns with differing operations. However, standard RL algorithms ignore this specialization, allowing the MoE routing to go uncontrolled during training, which empirically limit task performance and inference efficiency. To address this, we introduce a hierarchical routing control framework for agentic tasks. We explicitly encourage turn-level expert selections to align with agentic operations while regularizing token-level expert selections to maintain local consistency. To resolve stability issues that arise during post-training with the proposed methods, we further introduce an entropy-gated control mechanism. Overall, our routing control framework achieves over 10-point improvements in success rate on all evaluated benchmarks. These results demonstrate that agentic trajectory structure provides an effective signal for optimizing MoE capacity during RL post-training.

---


### 71. [Weight Oracles: Reading Neural Network Weights with Language Models](https://arxiv.org/abs/2610.07334)

**<font color=#1a73e8>作者：</font>** Krishna Kabra, Constantin Venhoff, Christian Schroeder de Witt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretability methods for neural networks are predominantly reactive: they analyse activations produced during specific forward passes, requiring known inputs to find hidden capabilities such as backdoors. We propose Weight Oracles, fine-tuned language models that diagnose properties of a target network by reading its raw weights directly, without behavioural testing. We investigate this paradigm in two phases. Phase I establishes feasibility: through a staged curriculum and an external chain-of-computation that delegates parameter-free operations to deterministic code, an explainer LLM learns to simulate the forward pass of small transformers from their weights, achieving 99% holdout accuracy on unseen targets. Phase II repurposes this infrastructure for safety auditing. We train an oracle on natural language diagnostic questions about weight anomalies using only benign pathologies as training signal, and evaluate it zero-shot on backdoors absent from training. The oracle achieves AUROC 0.93 on attention-routed backdoors and 0.81 across a diversified threat distribution including stealth and adversarially regularized variants. Hand-crafted statistical detectors are sharp on the threat models they implicitly target but collapse on threat-model shift, while the oracle remains uniformly competent across attack types. Scaling to realistic model sizes remains the principal open challenge.

---


### 72. [Selective Critique for Cost-Aware LLM Agents in Long-Horizon Decision Making](https://arxiv.org/abs/2610.07335)

**<font color=#1a73e8>作者：</font>** Heewon Park, Somin Im, Minhae Kwon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Improving the reliability of large language model (LLM) agents in long-horizon decision-making remains a key challenge. When deployed as autonomous agents interacting with complex environments, early mistakes can propagate through trajectories and cause cascading failures. Recent approaches improve reliability by incorporating external critique or deliberation, but invoking these mechanisms at every step substantially increases token consumption and latency, limiting practical deployment. We propose SAG (Self-improving Agent with Gated critique), a cost-aware framework that formulates critique invocation as a step-wise decision problem during long-horizon interaction. SAG introduces a lightweight, training-free gating mechanism that estimates the utility of critique using action-level ambiguity signals--global entropy and local top-2 margin--computed over admissible actions. From a decision-theoretic perspective, this mechanism approximates the Value of Information (VoI) of critique, enabling the agent to selectively allocate expensive feedback only when its expected benefit justifies the cost. SAG further incorporates online bootstrapped self-improvement, allowing the actor to internalize critic-assisted behaviors and progressively reduce reliance on critique. Across three long-horizon interactive benchmarks and multiple backbone models, SAG substantially improves the performance-cost trade-off compared with both no-critique and always-on critique agents. On ALFWorld, SAG increases task success from 24.6% to 78.4% while maintaining a token budget comparable to ReAct, yielding a $3.1\times$ improvement in normalized token efficiency. Moreover, a 7B actor with a lightweight 3B critic achieves performance comparable to a 14B actor without critique, showing that selective critique can recover most of the reliability benefits of deliberation while dramatically reducing inference cost.

---


### 73. [A doctrine-grounded visual question answering dataset for Tactical Combat Casualty Care](https://arxiv.org/abs/2610.07339)

**<font color=#1a73e8>作者：</font>** Junseob Kim, Jade Chng, Ayman Ali 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tactical Combat Casualty Care (TC3) requires responders to connect visual observations of injuries and interventions with established clinical guidance. Developing vision-language models to support this process requires supervision that links visible evidence to traceable doctrine. We present TC3-VQA, a dataset constructed from public instructional and field TC3 videos and authoritative TC3 documents. It contains 581 items spanning 11 concepts, with 1,860 questions covering intervention recognition, doctrine, clinical reasoning, procedural guidance, and refusal when visual information is insufficient. Doctrine-based answers preserve verbatim source passages and character offsets. Construction combines visual annotation, passage retrieval, entailment checks, and verification across model families. Equipment boxes, anatomical labels, temporal segments, and source metadata accompany the question-answer pairs. Automated audits and ratings by two physicians and two medical students characterize annotation quality, with human ratings available for 88 retained items. The dataset provides a resource for adapting vision-language models to TC3, studying the connection between visual evidence and clinical knowledge, and evaluating recognition, doctrine recall, and abstention.

---


### 74. [Rationale-Guided Policy Optimization: Learning to Reason with Adaptive Rationale Scaffolding](https://arxiv.org/abs/2610.07342)

**<font color=#1a73e8>作者：</font>** Hoang Phan, Minh Pham, Chau Pham 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy reinforcement learning has become a central paradigm for improving the reasoning abilities of large language models. However, its effectiveness is often limited by reward sparsity: when a model fails to discover correct trajectories for difficult problems, the optimization process receives little useful signal and may stagnate. Existing approaches mitigate this issue by incorporating off-policy demonstrations, expert traces, or model-generated solutions, but they typically require the auxiliary data to match the format of the reinforcement-learning task, often relying on rejection sampling from stronger models to obtain suitable training trajectories. We introduce Rationale-Guided Policy Optimization (RGPO), a framework that adaptively leverages ground-truth rationale information according to the model's current capability while preserving its freedom to explore. Rather than treating reference solutions as fixed imitation targets, RGPO uses them as temporary scaffolds: rationales help the model generate improved responses, after which only higher-reward, model-generated solutions are transferred back to the original unguided setting. This design allows training to exploit available ground-truth information without requiring off-policy data to follow the same format as the RL task. Across both language-only and vision-language reasoning settings, RGPO consistently improves performance over RLVR baselines, and ablation studies show that adaptive rationale guidance is a key contributor to these gains. These results suggest that RGPO offers a practical and general approach for reducing reward sparsity, stabilizing reinforcement learning, and improving reasoning performance in both text-only and multimodal models.

---


### 75. [Stepped MoE: Segment-Level Routing with Configurable Inference Complexity](https://arxiv.org/abs/2610.07348)

**<font color=#1a73e8>作者：</font>** Arnav Kundu, Zhaoyang Xu, Bairu Hou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large language models (LLMs) is resource-intensive, and adapting them for diverse deployment scenarios with varying computational constraints remains challenging. While elastic architectures enable flexible model deployment and sparsely activated models allow input-adaptive computation, existing approaches treat these dimensions independently. Moreover, models catered towards on-device edge inference need to conform to the memory and compute limitations of the serving devices. In this paper, we introduce a unified framework that combines elastic structures with sparsely gated architectures to create models that adapt simultaneously to both deployment constraints and task requirements. Our approach employs a model backbone that conditions on both the context and target efficiency specifications, enabling fine-grained control over the accuracy-efficiency trade-off at inference time. The model learns to activate task-relevant parameters within elastically-nested sub-networks, allowing a single model to span multiple capacity points while maintaining input-adaptive routing. Through experiments we demonstrate that we can create a model that allows the flexibility to use 1,2,3,4 billion parameters while being more accurate than their dense counter-parts (2-5\% on knowledge-intensive benchmarks) and at par with their static versions while delivering similar latency metrics as dense models. Overall, we save on device disk space by sharing the model parameters, allow flexibility of serving based on DRAM and compute available while delivering more accurate results.

---


### 76. [RELACE: retrospective likelihood-based action credit estimation for long-horizon language agents](https://arxiv.org/abs/2610.07349)

**<font color=#1a73e8>作者：</font>** Sayak Chakrabarti, Sathish Reddy Indurthi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) avoids a separate critic by estimating advantages from rollout groups. For multi-turn agents, however, trajectory-level supervision provides coarse, noisy credit: terminal rewards do not locate errors and can penalize useful actions alongside mistakes. Group-in-Group Policy Optimization (GiGPO) and subsequent methods refine supervision through state-conditioned comparisons, but their credit estimates remain sensitive to downstream decisions and outcomes. We introduce RELACE, Retrospective Likelihood-based Action, a critic-free framework that integrates retrospective action assessment with state-conditioned advantage estimation. RELACE evaluates executed actions through teacher-forced likelihood scoring under both their original contexts and outcome-augmented contexts. Comparing these likelihoods yields a trajectory-normalized retrospective factor that captures outcome-dependent changes in action plausibility, rather than hindsight plausibility alone. We use this factor to reweight discounted task returns and construct local advantages by comparing weighted returns among actions from equivalent states within a task. This couples retrospective relevance with observed reward, producing fine-grained credit that complements trajectory-level GRPO supervision. Temporal smoothing and success-protecting masking further stabilize the local signal. RELACE requires neither auxiliary value nor reward models nor additional autoregressive rollouts for credit estimation. Experiments on ALFWorld and WebShop with Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct demonstrate substantial improvements over GRPO, GiGPO, and HCAPO. With the 1.5B model, RELACE achieves $96.35\%$ success on ALFWorld and $79.43\%$ on WebShop, surpassing GiGPO by $5.47$ and $5.60$ percentage points, respectively.

---


### 77. [Evaluating Escalation Signals for LLM Routing: Targets, Controls, and Five Ways to Fool Yourself](https://arxiv.org/abs/2610.07354)

**<font color=#1a73e8>作者：</font>** Ramin Pishehvar, Andrea Morandi, Mahesh Viswanathan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deciding when to escalate a query from a small language model to a larger one requires a cheap signal that predicts, before the large model is called, whether escalating would help. Semantic entropy, originally developed to detect hallucinations, is a natural candidate: it measures how much a model's sampled answers disagree in meaning, and high disagreement often signals an unreliable answer. We test it across three benchmarks and two model families. On GSM8K, with a small/large pair about twelve times apart in size, semantic entropy reliably distinguishes the small model's mistakes (AUROC 0.871) and improves routed accuracy over random escalation by up to nine points at matched cost. An earlier strong-looking result on a synthetic benchmark proved misleading: a simple rule based only on question difficulty, with no model involved, matched semantic entropy almost exactly. This paper's main contribution is a set of checks that catch this before it is reported as real. We show that scoring a cheap, question-only difficulty estimate alongside any signal reveals whether the signal adds real information or just tracks how hard a question looks; that two reasonable definitions of "escalation worked" can produce very different results on the same data; that a benchmark can leave almost no room for any signal to beat simply always using the large model; and that the true cost of live sampling can make routing more expensive than calling the large model directly. For a cheaper alternative that reuses cached past outcomes, we show how to predict whether it will work on a new dataset -- confirmed by correctly forecasting a collapse from AUROC 0.908 to chance level (0.518) ahead of time. We offer these as a general checklist for evaluating escalation signals.

---


### 78. [Tracking Is Not Permanence: What Video World Models Keep of a Hidden Object](https://arxiv.org/abs/2610.07355)

**<font color=#1a73e8>作者：</font>** Peng Xie, Amr Alanwar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models track objects they can see; we ask what they keep of objects they cannot. We hide an object from a frozen V-JEPA 2 predictor and compare its prediction for the hidden region with the encoder's representation of two worlds that differ only inside that region. The predictor's decision keeps a stationary object in part and one carried inside a container not at all, and loses a moving one within 0.3 s (0.5 s under V-JEPA's own tube mask; ViT-H keeps it to 1.1 s at pretraining's 90% masking ratio); in projection a trace remains, below the midpoint, at 14-60% of what a baseline copying the last view retains. The information is there: the encoder reads the object's presence at 1.00 and keeps a closed container's contents decodable for 3.5 s, while the predictor's output, read with the encoder's own probe, contains the ball in 2% of scenes once the box has been closed for half a second. On rendered scenes, permanence is missing on the predictor's side, and training installs it cheaply as a prior: three thousand predictor-only steps on synthetic containers take this belief from 0.05 to 1.00 against two matched controls. They also raise IntPhys-2019 from 84.2% to 93.3%, but so does a curriculum without containers, and which training habit the benchmark credits changes with its scoring rule. Continued training with tube masks produces 1.1-1.6 s of moving-object carry-over on manipulation and internet-style video, so the deficit is not intrinsic to latent prediction. VideoMAE keeps almost nothing, and Cosmos's next-token prediction keeps a stationary hidden object but not one carried inside a moving container.

---


### 79. [Evaluate the Stack, Not the Layer: Do Deterministic and LLM Gates for Agent Actions Fail Independently?](https://arxiv.org/abs/2610.07359)

**<font color=#1a73e8>作者：</font>** Chenglin Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Runtime gates for agent tool calls are stacked on the assumption that their errors multiply. We test it on 1,119 labelled agent actions from three corpora, without an adaptive adversary. The stack has one deterministic rule layer and four LLM judges, three of them re-collected with the served model recorded on every call. We read each stack as a number of multiplication-equivalent layers, n_mult, with its floor under perfect coupling. Under the STRICT miss definition (escalation to a human scored as not stopped), any two judges compose to about 1.2 to 1.4 layers ({\phi} median +0.430, 6 of 6 pairs significant, floors 1.02 to 1.17). The rule layer plus one judge composes to 1.86 to 2.09 layers ({\phi} median +0.014, 0 of 4 significant, floors 1.01 to 1.09). Under PRIMARY (escalation scored as caught) the bands are 1.21 to 1.57 and 1.80 to 2.13. Intervals separate on the pooled data, point estimates split on each corpus, and a third-vendor judge lands in the judge band. Solo accuracy does not predict what a layer adds: a cloud rule pack lowers the rule layer's solo miss rate by 20% and adds no new joint coverage. The difficulty share of judge coupling is not identifiable: 31.8% to 61.8% depending on the probe and the miss definition. One judge tier was served by an unrequested model version in 50 of 112 batches, concentrated on the external corpus. That event overturned a pre-declared analysis rule, and the scoring of review verdicts reversed five conclusions. We report both.

---


### 80. [Dynamic Budget Allocation for LLM Evaluation under Hard Resource Constraints](https://arxiv.org/abs/2610.07362)

**<font color=#1a73e8>作者：</font>** Shai Feldman, Yaniv Romano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We evaluate large language models (LLMs) in multi-turn interactions through their time-to-event: the number of interaction steps required to produce an event of interest, such as a successful jailbreak or agentic task completion. Under limited compute, interactions may be terminated before the event occurs, so that event times are only partially observed (censored). Existing allocation methods for calibrating time-to-event bounds satisfy the budget only in expectation and can exceed the available budget on a particular evaluation run. Enforcing a hard constraint is particularly challenging as the cost of a trajectory is initially unknown. We introduce Hard-budget Allocation with Reflow for Predictive calibration (HARP), a budget allocation that satisfies hard resource constraints and adaptively reallocates unused budget. We show how to use HARP to construct lower predictive bounds (LPBs) on the time-to-event and to estimate evaluation metrics such as the jailbreak rate on a fixed benchmark. Although HARP induces dependence in acquisition decisions across different trajectories, we prove that HARP never exceeds the target budget, that its LPBs have finite-sample coverage guarantees, and that its metric estimates are unbiased. Experiments on agentic task success, LLM jailbreaks, toxic content generation, and RAG hallucinations show that HARP achieves coverage close to the nominal level with low variance, while never exceeding the given budget.

---


### 81. [Who Wrote It Is Not Enough: Detecting Who Contributed the Insight](https://arxiv.org/abs/2610.07365)

**<font color=#1a73e8>作者：</font>** Zhuoyang Zou, Abolfazl Ansari, Jiaxi Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLMs increasingly assist scientific writing and peer review, detecting who wrote the text is no longer sufficient: we need to determine who contributed the underlying insight. We introduce Insight Provenance, the task of identifying whether a review insight originates from a human, an LLM, or their hybrid contribution. We construct InsightProv-v0 from 4,057 scientific papers and 12,660 human reviews, simulating different levels of LLM involvement with GPT-4o, Gemini, and DeepSeek and annotating provenance at the sentence level. We show that strong performance on raw data can be misleading, as models exploit linguistic and textual-authorship shortcuts that degrade substantially under progressively debiased evaluation. We therefore propose a two-stage adversarial framework that suppresses shortcut signals while preserving provenance-relevant information. Beyond detection, extensive analyses reveal what makes intellectual authorship identifiable: paper grounding and neighboring review context provide complementary provenance signals, while human, hybrid, and AI insights systematically differ in their information sources and failure modes. Most strikingly, AI insights predominantly remain close to generic or paper-provided information, whereas human insights more often introduce external knowledge and independent judgment. These findings suggest that while wording can be rewritten by an LLM, the provenance of an idea leaves a deeper and more persistent signal.

---


### 82. [MemCo: Memory-Centric Collaboration for Generalizing LLM Agents to Unseen Environments](https://arxiv.org/abs/2610.07376)

**<font color=#1a73e8>作者：</font>** Xinting Liao, Siyan Liu, Rabab K. Ward 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly operate in interactive environments, where they need to make sequential decisions through observation, action, and feedback. Although memory can help agents reuse experience, existing work designs memory in isolation, where collecting enough trajectories to populate it is expensive. Existing shared-memory approaches mitigate isolated experience by pooling episodic memories across tasks and environments. However, retrieving shared memory is challenged by the granularity, where retrieved memories can be either too specific to preserve current grounding or too coarse to support the next action. In this work, we propose MemCo, a memory-centric collaboration framework for generalizing LLM agents to unseen interactive environments. It maintains complementary local and global memory spaces, preserving environment-specific details locally while promoting transferable workflows induced from local trajectories to global memory. During online interaction, MemCo routes relevant local and global memories in terms of the agent's current state and decision phase, enabling agents to reuse the experience of other agents without blindly transferring environment-specific details. Experiments on interactive decision-making benchmarks show that MemCo improves task success and reduces redundant exploration compared with isolate-memory and shared-memory baselines. Our code is available at this https URL.

---


### 83. [Semantic Capability Acquisition and Specialization During Vision-Language Model Fine-Tuning](https://arxiv.org/abs/2610.07385)

**<font color=#1a73e8>作者：</font>** Suguru Onda, Matthew Bailey, Ryan Farrell  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-tuning vision-language models (VLMs) is typically evaluated at a single downstream checkpoint, obscuring whether a semantic capability was never acquired or emerged earlier and later declined during specialization. We ask how semantic capabilities are acquired, when they peak, how well they transfer, and what remains at deployment. We study these dynamics as a semantic capability trajectory, tracking identity- and attribute-based capabilities over training.
We formulate a trajectory-based framework that separates capability acquisition, capability-specific optima, and later specialization, and introduce Structured Semantic Routing (SSR) to study how the representation of supervision shapes what is acquired. Across six pretrained backbones spanning DFN, MetaCLIP, and OpenAI CLIP, we show that fine-tuning can acquire semantic capability beyond the pretrained state, including gains observed on held-out evaluations. Unstructured name-and-attribute supervision produces strong name-and-attribute retrieval with comparatively weak name-free attribute-profile retrieval, whereas SSR yields substantially stronger name-free attribute-profile retrieval and is further strengthened by stochastic name-branch dropout. Different capabilities can peak at different stages, so a checkpoint selected by target class-name retrieval need not coincide with a transferable semantic optimum. Continued optimization can therefore preserve strong target class-name retrieval while reducing previously acquired transferable semantic capability. In a representative diagnostic study, this late specialization is consistent with reduced cross-modal semantic accessibility while substantial image-only class structure remains available.

---


### 84. [Inference and learning in sparse autoencoders as natural gradient flow](https://arxiv.org/abs/2610.07389)

**<font color=#1a73e8>作者：</font>** Hadi Vafaii, Tejas Rao, David Chanin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders are widely used to uncover interpretable features in neural networks, yet reliable recovery remains difficult when features overlap or activate infrequently. These challenges involve both inferring which features explain an input and learning the dictionary that represents them. Here, we unify inference and dictionary learning as natural-gradient flows on a shared variational free energy. We instantiate this framework as BeFOND, an encoder-free sparse coding model with closed-form inference and learning dynamics. We show how recurrent explaining away reduces interference between overlapping features, while Fisher preconditioning can compensate for the slow learning of rare features. On synthetic data, BeFOND improves dictionary recovery and rare-feature detection, with a growing advantage over amortized baselines as superposition increases. On language-model activations, it improves single-feature concept detection and selective intervention, outperforming pretrained reference SAEs with substantially less training data. Its feature quality continues to improve with dictionary width, whereas the evaluated baselines largely plateau. Together, these results show how improving inference and learning within a unified probabilistic framework can make better use of data and dictionary capacity to interpret and intervene on neural representations.

---


### 85. [Defense-in-Depth for LLMs: Evaluating Memory Gates Against Activation-Induced and Memory-Induced Sycophancy](https://arxiv.org/abs/2610.07403)

**<font color=#1a73e8>作者：</font>** Ritvij Sharma, Russell Dlugosz, Ryan Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory allows Large Language Models (LLMs) to maintain personalized context across interactions, but retrieved user history can induce memory-induced sycophancy, causing models to favor stored user beliefs over objective evidence. Existing defenses primarily operate on retrieved context and are rarely evaluated jointly with internal behavioral bias. We introduce a $2 \times 2$ defense-in-depth framework separating internal activation steering from external memory handling. We extract sycophancy steering directions from 100 paired prompts and evaluate four open-weight models across 10 steering coefficients and five memory-defense configurations on MemSyco-Bench (answers for all 1,550 items; defense conditions judged on a fixed 250-item subsample), with three LLM judges. Three of the five configurations are new (rewriting every memory, a Router Gate that keeps, rewrites, or drops each memory, and dropping all memory); the other two are MemSyco's baselines. Selective Router Gate filtering preserves substantially more of MemSyco's average accuracy than complete memory removal, and this separation persists when the models are steered toward sycophancy. On Llama 3.1 8B with Router Gate, mild inverse steering ($\alpha = -1.5$) lowers judge-averaged sycophancy from 35.80% to 31.32% while average accuracy moves from 43.99% to 43.31%; this reduction has the same direction under all three judges but is not statistically significant (paired $p = 0.08$ to $0.63$ on 149 items). External memory filtering is the part of the design that holds up; our data do not show that inverse steering adds to it.

---


### 86. [What pass@k Cannot Measure: Evaluating Diversity and Capability Retention after Post-Training](https://arxiv.org/abs/2610.07405)

**<font color=#1a73e8>作者：</font>** Subham Rath, Raj Dandekar, Rajat Dandekar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> pass@$k$, the fraction of problems a model solves within $k$ sampled attempts, is the field's default protocol for deciding whether reinforcement-learning (RL) post-training on verifiable rewards improved a model. At the population level, pass@$k$ depends only on a problem's probability of a correct sample, with no term for how it is distributed across outputs. We show this gap is not academic. Training Qwen2.5-1.5B-Instruct on grade-school math with Group Relative Policy Optimization (GRPO) and with rejection-sampling fine-tuning (RFT, training on the model's own shortest verifier-passed rollout) moves three complementary diversity measures (token-level entropy, answer-level entropy, unique answers per prompt) in opposite directions, with zero overlap across three seeds per arm. The gap survives restricting to verifier-correct completions only (lexical diversity among correct solutions is 15% lower for GRPO, after controlling for length) and a count-controlled check isolating diversity among incorrect answers alone, ruling out that GRPO's higher accuracy alone explains it. Yet pass@8 and pass@32 show no consistent winner on GSM8K, and a hard MATH-500 subset shows the same pattern: separation only at low $k$. Compared against the starting checkpoint, no trained arm significantly improves hard-problem coverage: RFT is significantly worse, while GRPO is statistically indistinguishable from it - so GRPO's pass@1 edge over RFT reflects a smaller loss relative to Base, not a capability gain, a missing-control issue, not a failure of pass@$k$. On GSM8K, only pass@1, with no role in detecting diversity by construction, separates the arms cleanly, rewarding the arm whose correct solutions are least diverse. We argue this is a concrete instance of a standard evaluation protocol missing a property it is routinely used to certify.

---


### 87. [2d-fet-bench: from spatial reasoning to fet design on flakes](https://arxiv.org/abs/2610.07423)

**<font color=#1a73e8>作者：</font>** Dunzhi Zhou, Chengyu Zhu, Gang Qiu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Field-effect transistor (FET) layouts on exfoliated two-dimensional flakes are typically drawn by hand for each flake, placing contacts and gates to match its position and outline in optical micrographs. To our knowledge, no executable benchmark tests whether language-model agents can perform this flake-specific construction reliably. We introduce 2D-FET-Bench V2, a benchmark of 128 layout tasks built from microscopy-derived flake contours, including hole-containing flakes and multi-flake tasks. Each task supplies a textual device specification and contour coordinates. An agent generates typed polygon and path operations rendered to GDSII. A deterministic verifier checks geometric and structural requirements, and a separate integrity check verifies that the supplied contours remain unchanged. Scripted reference layouts pass all 128 tasks, showing that every task is solvable. We evaluate six models and seven workflow and scaffold variants of GPT5.6-Luna, with five attempts per task. The best-performing configuration in the six-model panel, GPT5.6-Luna with ReAct-3, passes 62.3% of attempts and solves 80.5% of tasks at least once (coverage) and 43.8% in all five attempts (consistency). ReAct-3 exceeds the one-pass Plan-and-Execute by 27.0 pass@1 points at 2.46 times the tokens. An expert audit of one sampled verifier-passing layout per covered task, across five ReAct-3 configurations, accepts 56.4% to 63.5% of them. The benchmark evaluates geometric and structural FET layout construction.

---


### 88. [When Does AI Supervision Help? A Role-Aware Study of Network Fraud Decision Management with Blockchain Auditability](https://arxiv.org/abs/2610.07434)

**<font color=#1a73e8>作者：</font>** Saviz Changizi, Nasibeh Mohammadzadeh, Mohammad Shojafar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When does a second artificial intelligence (AI) component improve a primary network-fraud decision rather than add operational burden? We study this question through a role-aware Decider-Supervisor (DS) framework with blockchain auditability, evaluating four directional configurations that combine centralised machine learning, a Federated Averaging (FedAvg)-trained federated meta-model, and Base or Quantized Low-Rank Adaptation (QLoRA) large language model variants. The analysis compares primary-only and supervised decisions using non-hard fraud performance, intervention burden, conditional calibration, traffic-mix and Review-capacity sensitivity, dependability tests, and blockchain lifecycle controls. The deterministic hard gate resolves 89.994% of fraudulent requests, leaving the non-hard population as the main AI decision setting. Conditional validation calibration does not produce a consistently transferable supervisory advantage on deployment replay. DS-3 QLoRA is the least disruptive supervised configuration, but it still underperforms its primary FedAvg stage in F1 and total errors. Across 36 reweighted traffic mixtures, supervision reduces total errors only for DS-4 Base in two extreme high-fraud scenarios. Blockchain tests support digest verification, tamper detection, authorisation, single-use review resolution, and post-finalisation integrity, while exposing a pre-finalisation single-write limitation. The results show that the value of AI supervision depends on role assignment, calibration, escalation policy, traffic composition, and lifecycle controls rather than on the presence of a second model alone.

---


### 89. [Decoupling What from Where: How Should a Small GUI Grounding Model Receive the Action Type?](https://arxiv.org/abs/2610.07444)

**<font color=#1a73e8>作者：</font>** Aadi Chauhan, Arthur Ilyasov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A GUI agent decides which action to take and where to take it; we ask how a small grounding model should receive the action type. Fine-tuning Qwen2-VL-2B with LoRA on Android in the Wild, we compare a flat baseline with five ways of supplying the type under matched data, compute, and decoding: an auxiliary loss, a hard-routed action word, an additive learned embedding, a prepended learned token, and the type written into the prompt. With five seeds, an episode-clustered bootstrap, and seed-level paired tests, the ranking on a mixed stream is clear: the auxiliary loss, the additive embedding, and the prompt word each gain five to seven hit@0.10 points over the baseline, while hard routing and the prepended token are not distinguishable from it. Much of that gain is protection from a preprocessing choice of ours rather than a spatial prior. Our serializer clamps the off-screen touch point AITW records for type events to the origin; that class degrades the baseline's click grounding, and removing it lifts the baseline by nearly seven points, after which no mechanism's hit rate beats it and the intervals exclude a two-point effect, though the auxiliary loss still shortens the average miss; on a stream of taps and swipes none helps. Whether this generalizes beyond one serialization is open. For deployment, the pipeline's margin over the baseline with predicted rather than gold types is not established (+0.016, 95% interval [-0.017, +0.052]), and a wrong type collapses every model conditioned at inference. The prepended token does not help at the shared learning rate, where its rows barely move from initialization; trained ten times faster it reaches the level of the other three, with a margin three seeds do not establish. We also document a silent failure: injecting conditioning through inputs_embeds makes Qwen2-VL fall back to 1-D positions for image tokens, costing nine points.

---


### 90. [AlignQuant: Tile-Aligned Mixed-Precision Quantization for Efficient LLM Generation](https://arxiv.org/abs/2610.07457)

**<font color=#1a73e8>作者：</font>** Hanzhi Zhang, Qiao Zhang, Qinglei Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-grained mixed-precision quantization promises efficient large language model inference, but local precision choices can conflict with regular GPU storage and computation units. This precision-boundary mismatch limits the translation of compression into practical acceleration. We introduce AlignQuant, a post-training quantization method that uses GPU-compatible two-dimensional weight tiles as the common unit of precision allocation, compact storage, and execution. This shared partition lets precision follow sensitivity within output channels. Joint prefill/decode calibration scores precision reductions using projection-output perturbations weighted by language-model loss gradients under quantized activations. Phase-normalized scores prioritize higher precision for tiles important to either phase under a model-wide weight-storage budget. Each tile stores one selected representation, while phase-specialized kernels reuse the packed model and expand lower-bit weights for INT8 computation with 8-bit activations. Across four LLMs spanning 3B to 14B parameters, AlignQuant achieves up to $2.50\times$ generation speedup over BF16 while preserving model quality. Evaluations further cover three GPUs and contexts up to 64K tokens. These results show that local precision flexibility and regular GPU execution can coexist through a shared tile unit. The implementation is available at this https URL.

---


### 91. [ElasticFit: Fit-Aware 3D Object Insertion via VLM Reasoning and Generative Adaptation](https://arxiv.org/abs/2610.07460)

**<font color=#1a73e8>作者：</font>** Tzu-Hsin Hsieh, Ricardo Marroquim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inserting objects into existing 3D scenes requires more than selecting a plausible location:
the inserted object must also fit local geometry while preserving semantic intent and physical plausibility.
Although recent Vision-Language Models (VLMs) and generative models enable semantic reasoning and visual content creation, they offer limited 3D grounding and geometric control when an inserted object must fit into constrained local spaces.
We introduce \textbf{ElasticFit}, a VLM-guided framework for fit-aware object insertion centered on a novel scene-grounded representation.
Given a language instruction and rendered scene observations, ElasticFit infers structured fitting cues that specify where the object should be grounded, what volume it should occupy, how it should be oriented, and its adaptation mode (rigid placement, uniform scaling, or elastic fitting).
These cues convert high-level VLM reasoning into explicit 3D constraints that condition object generation and guide downstream geometric fitting.
ElasticFit then generates a scene-conditioned object prior, reconstructs it in 3D, and refines the mesh through mode-specific fitting while enforcing collision avoidance, contact consistency, and physical grounding.
In fixed-asset baseline comparisons, ElasticFit improves spatial relation success from 50.8\% to 69.7\% and support success from 48.3\% to 91.7\% over the strongest baseline, while providing novel support for generative "make-it-fit" insertions in complex scenarios.

---


### 92. [COMPASS: Finding Where Reasoning Lives in Language Models](https://arxiv.org/abs/2610.07469)

**<font color=#1a73e8>作者：</font>** Pratyay Dutta, Kowshik Thopalli, Vivek Narayanaswamy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explicitly eliciting reasoning substantially improves LLM performance. Existing approaches require a predefined characterization of reasoning, whether through CoT prompt design, contrastive CoT directions, or via SAE derived reasoning features. For mathematical reasoning with verifiable answers, we show that a much simpler signal suffices, which is the correctness of the model's own direct answer attempts. This signal yields a latent direction that elicits reasoning. This direction is decodable within the activations of most attention heads, but only a small subset of them can be effectively intervened. We introduce COMPASS, an inference-time steering method that identifies these heads using a logit-space attribution score and steers their activations along the correctness direction, requiring only per-head activation statistics. Across three model families and multiple math benchmarks, COMPASS outperforms the activation-steering baselines we compare against, improves GSM8K accuracy by 16 percentage points on average, and approaches CoT accuracy with 20-70\% fewer generated tokens. Interventions transfer without re-fitting to unseen benchmarks, and ablations show that both the correctness direction and the small set of heads carrying it are necessary, with the effect concentrated in remarkably few heads.

---


### 93. [Structure, Not Belief: Correlated Thompson Sampling from LLM-Derived Covariance in Combinatorial Semi-Bandits](https://arxiv.org/abs/2610.07470)

**<font color=#1a73e8>作者：</font>** Vikram Kakaria, Anish Kataria, Anany Kotawala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Combinatorial Thompson sampling (CTS) draws independent posterior samples for every arm, so its exploration dynamics ignore any relation among arms. We study a minimal change to those dynamics: an LLM is queried once for a partition of the arms, the partition becomes a positive-definite correlation matrix $\Sigma$ through an RBF kernel on cluster ranks, and the per-round posterior sample is drawn with covariance $\Sigma$ while the Beta posteriors are updated from real rewards only, so the LLM shapes how the sampler moves, not what it believes. We give a self-contained Bayesian regret bound for the idealized Gaussian sampler whose information gain splits into a $K\log T$ term from the $K$-cluster structure and a ridge term that grows to $d\log T$: the $\sqrt{d/K}$ improvement over independent sampling is a finite-horizon transient, exact only as the within-cluster correlation tends to one. The correlated sampler reduces regret by 19% over CTS on 16 synthetic Bernoulli families at $T=2{,}500$ (6-7% at $T=25{,}000$ with data-adaptive kernels) and by 41% on the Microsoft MIND-small news benchmark ($d=200$ real articles), while pseudo-observation warm starts give nothing. An LLM-free ablation with a simulated oracle of controlled quality shows that on unstructured instances the gain is a property of the kernel shape (a random partition, or a plain tempering of the sampling noise, reproduces it), while belief injection at matched oracle quality never helps.

---


### 94. [PsyCIDRA: A Dual-Agent Framework for Psychiatric Interviewing and Diagnostic Reasoning](https://arxiv.org/abs/2610.07473)

**<font color=#1a73e8>作者：</font>** Milad Mohammadi, Fatemeh Akrami Shamsabadi, Zahra Mohseni 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models show promise in clinical reasoning, but psychiatric interviewing requires guiding an evolving conversation. Their ability to carry out this interactive assessment remains less studied. We present PsyCIDRA, a dual-agent framework linking free-form psychiatric interviewing with diagnostic reasoning for expert review. Its interviewer agent uses tools to maintain working notes, load expert-written skills, and retrieve ICD-11 references to guide inquiry. Its diagnostic reasoning agent then receives the completed interview transcript and reports hypotheses alongside supporting, conflicting, and missing evidence, withholding a final hypothesis when none is sufficiently supported. Using patient profiles generated with PsyCPG, we first evaluate PsyCIDRA in simulation. Across four models on 53 evaluation cases, it achieves higher diagnostic agreement than direct prompting. On 81 held-out simulated cases, rank-1 accuracy is 60.5% versus 51.9%. In a blinded study of 101 human participants in separate arms, PsyCIDRA agrees with psychologists on whether to propose a diagnostic hypothesis in 79.6% of cases, compared with 65.4% for direct prompting. Together, these findings support the potential of LLM agents to assist psychiatric assessment through free-form dialogue. By examining diagnostic reasoning, interview quality, and safety together, this study contributes to understanding the capabilities and limitations of psychiatric interview agents.

---


### 95. [MRPilot: Supervising and Intervening LLM-Based Multi-Robot Teams through Mixed Reality](https://arxiv.org/abs/2610.07477)

**<font color=#1a73e8>作者：</font>** Xiaoran Yang, Xun Qian, Yang Zhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) let users direct heterogeneous multi-robot systems (MRS) through natural language, but make task interpretation, robot assignment, and coordination difficult to inspect and change. Based on a formative study with 12 non-expert users, we developed MRPilot, a mixed reality system organized around four stages of supervision and intervention. MRPilot represents robot-team plans and execution states as structured commitments shared across synchronized situated and overview views. Across four stages, it helps users resolve ambiguous references (Forming), review plans before execution (Reviewing), monitor distributed execution (Following), and make robot-level or team-level changes when problems arise (Repairing). In a within-subjects study with 20 participants in a virtual reality-simulated home, MRPilot reduced workload, increased situational awareness, transparency, trust, and perceived control compared with a conventional LLM-based conversational interface using the same LLM planner and robot capabilities. We provide design implications for multi-scale intervention, adaptive supervision, and calibrated reliance in LLM-based MRS.

---


### 96. [In With the Old: Enhancing 'Classical' Document Automation with Generative AI](https://arxiv.org/abs/2610.07480)

**<font color=#1a73e8>作者：</font>** Marc Lauritsen, Hannes Westermann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Software-based legal assistance systems have leveraged many different forms of knowledge representation and reasoning. This article explores how document automation services rooted in expert system style and other symbolic approaches can usefully enhance and be enhanced by current generative AI approaches. We discuss the possible benefits and challenges, and report on preliminary experiments in using large language models to identify and fix issues in texts written by laypeople.

---


### 97. [From Written Response to Dialogue with AI: How Activity Format, Interaction Modality, and Language Impact Student Learning and Engagement](https://arxiv.org/abs/2610.07483)

**<font color=#1a73e8>作者：</font>** Deepak Varuvel Dennison, Connie Zhang, Rene Kizilcec 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The widespread availability of LLMs is challenging written learning activities, as students can increasingly generate responses without necessarily engaging with the learning content. Conversational AI creates an opportunity to redesign these activities as dialogue, while multilingual capabilities may make such dialogue more accessible to students learning through a non-native language. We conducted a field study with 305 native Kannada-speaking undergraduate students at English-medium institutions in Karnataka, India. We compared written response activities with text- and voice-based dialogic activities with AI, each conducted in English-only or bilingual Kannada-English settings. Students who completed dialogic activities spent more time on the activities, contributed more, and reported greater interest and self-efficacy than those completing written responses, although fewer students completed the dialogic activities overall. Knowledge increased across all conditions, with no reliable differences in gains between activity formats or languages. Language shaped participation differently across modalities: bilingual interaction was particularly beneficial in voice dialogue, where it reduced articulation difficulties, increased turns demonstrating understanding, and reduced conversation abandonment. However, students also valued English because of its connection to their academic and professional aspirations. These findings show that designing dialogic learning with AI requires more than choosing between writing and dialogue, voice and text, or English and students' native languages. We highlight opportunities to give learners greater control over modality, information, and pace, and to use native languages as translanguaging support rather than as a replacement for English.

---


### 98. [Closing Ambient Clinical Documentation Gaps with Automated Provider Queries](https://arxiv.org/abs/2610.07502)

**<font color=#1a73e8>作者：</font>** Joseph Paul Cohen, Raj Shah, Han-Chin Shing 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Provider queries are clarifying requests sent by clinical documentation specialists to physicians to close gaps in the clinical note and ensure accurate billing. Prior work automates note drafting, ICD-10 coding, and order extraction assuming a complete transcript, leaving these gaps unaddressed. We study whether an LLM can automate the query loop, termed DAU (Draft, Ask, Update), across those three tasks. An audit of 3,000 real visits identifies the sources of missing documentation, from which we build five transcript-degradation benchmarks on public data. Analyzing 21k clarification turns on real conversations, we find useful-question predictors are task-specific: oracle confidence dominates, but note completeness needs only simple recall questions while ICD-10 coding needs harder, multi-option ones. About 9% of turns hurt performance, driven by redundant questions and non-answers that still trigger a rewrite. Deployment depends on learning "when not" as much as "what to" ask.

---


### 99. [On Open-Ended Information Seeking for Information Elicitation Agents](https://arxiv.org/abs/2610.07509)

**<font color=#1a73e8>作者：</font>** Victor De Lima, Grace Hui Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Information elicitation is an open-ended information-seeking problem in which an interaction can unfold in many potentially valuable directions, requiring an elicitor to continually determine which information to pursue as new information emerges. In agentic elicitation, these decisions may be delegated to a foundation model, yet how model choice shapes the resulting information-seeking behavior remains understudied. We study how judgments about information value vary across LLMs and how these differences shape sequential information seeking. We first examine these judgments across 11 LLMs spanning multiple model families and parameter scales, using a shared set of information and elicitation objectives. We then develop a controlled elicitation simulation in which different models encounter the same information space and use the same selection rule, isolating these judgments from question generation and respondent behavior. Using this setting, we characterize the breadth-depth behavior that emerges from model-specific information-seeking preferences over the course of elicitation. We further examine how interaction history changes the evaluation and subsequent selection of prospective information. We test the robustness and boundaries of these findings through sensitivity analyses and ablations over the opportunities available to the elicitor, the response labels used to operationalize information-seeking preferences, the presence of interaction history, and whether redundancy is explicitly relevant to the assessment. The project code, data, and trajectory files are available at this https URL.

---


### 100. [From Local Evidence to Safety Verdicts: Causal Tracing in Vision-Language Models](https://arxiv.org/abs/2610.07514)

**<font color=#1a73e8>作者：</font>** Faezeh Dehghan Tarzjani, Mevan Wijewardena, Alexander Romanus 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A vision-language model may need to combine an image with a prompt to recognize a safety risk that neither reveals alone. Where does this joint safety judgment become accessible inside the model? We introduce SSU-Bench, a dataset of matched safe and unsafe image-text combinations constructed using single-item prompt edits or image edits with annotated intended regions. Using three vision-language models, we transfer internal states between paired inputs and measure the resulting change in the safety verdict. Across models and both types of counterfactual, interventions at the changed input positions are effective in earlier decoder layers, while interventions at the final input token become effective later. Directions estimated from other examples produce similar late-layer effects. A linear readout of the final-token state also predicts the model's own verdict, including incorrect judgments, and cross-model comparisons reveal similarities in the patterns of counterfactual change. These findings identify a recurring transition in where interventions can influence a joint safety verdict and distinguish a readable model decision from a correct safety judgment.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-303](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
