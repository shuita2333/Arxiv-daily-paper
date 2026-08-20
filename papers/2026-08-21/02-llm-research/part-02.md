# 🧠 大模型相关研究 | 2026年08月21日

> 本类共 **166** 篇论文：已确认 **153** 篇，待复核 **13** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-166](./part-04.md)

---

### 51. [Measuring the Partial-Credit Gap: A Strict Benchmark on Vietnam's 2025 Convex Marking Scheme](https://arxiv.org/abs/2608.18336)

**<font color=#1a73e8>作者：</font>** Nguyen Quoc Hung, Nguyen Dang Minh, Le Nhu Quynh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When evaluating language models on human exams, benchmarks typically score each response as right or wrong and report the overall accuracy. This approach assumes that partial knowledge is worth proportional credit, an assumption that fails when an examination uses a non-additive grading scheme. The 2025 reform of Vietnam's National High School Graduation Examination demonstrates the cost of this substitution. In Part II of the exam, candidates evaluate four true/false statements per question. The grading is convex: the number of correct statements earns 0, 0.10, 0.25, 0.50, or 1.00 points. Identifying three statements correctly pays 0.50 points, not the 0.75 points that standard accuracy metrics would award. Because Part II accounts for 4.00 of the exam's 10.00 points, reporting accuracy inflates the score by rewarding partial knowledge that the state explicitly penalizes. We introduce THPT-Ladder, a benchmark of 632 items from 21 official exams across 11 subjects, graded exactly as the ministry grades its students. The ministry publishes the marks of over a million candidates, allowing us to place models directly into the human cohort. Across eight models, the official rubric pays 0.020 to 0.159 points less per Part II question than proportional credit. This shortfall changes a model's apparent competence. For Qwen3.5-27B on the 2025 History exam, a 0.042-point shortfall drops its standing from the 90th to the 77th percentile among 481,293 candidates. A model's accuracy does not predict this penalty. At Claude Sonnet 5's accuracy level, different distributions of errors yield scores varying from 0.869 to 0.932 points per question. Official marks depend on how correct statements are grouped, meaning standard benchmarks report a competence the institution would not certify.

---


### 52. [From Inference to Adaptation: A Unified Optimal Transport View of Vision Language Model](https://arxiv.org/abs/2608.18339)

**<font color=#1a73e8>作者：</font>** Qi Yu, Zhichen Zeng, Katherine Tieu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have demonstrated remarkable zero-shot capabilities yet remain sensitive to real-world distribution shifts during inference. Although significant efforts are devoted to adapting VLMs at test time, they rely heavily on noisy pseudo-labels predicted directly from raw embedding similarities during inference, which are unreliable under distribution shift and mislead the adaptation. To avoid noise amplification, existing works craft coarse-grained surrogate objectives during adaptation, which fail to explicitly model sample-level relationships across different modalities, creating objective mismatch with inference, thus leading to marginal performance improvement. In this work, we aim to bridge the detached objectives of inference and adaptation for VLMs, and propose a principled VLM TTA method called \algname. For VLM inference, we formulate the zero-shot image classification task as a cross-modal alignment problem encoded via a Wasserstein OT formulation, providing robust pseudo-labels at the sample-level to effectively adapt VLMs. For VLM adaptation, we adopt a soft-label InfoNCE loss to adapt VLMs based on the OT-induced pseudo-labels, leveraging fine-grained supervisions to explicitly model relationships of individual image-text pairs via contrastive learning, which empowers accurate inference at the same granularity. Moreover, we theoretically reveal that the InfoNCE loss can be neatly reformulated as a Wasserstein OT formulation, thereby unifying the objectives of the inference and adaptation of VLMs to achieve their mutual benefits. Extensive experiments demonstrate the effectiveness and efficiency of our methods, outperforming the best-performing methods by up to 7% with state-of-the-art efficiency.

---


### 53. [Task-Conditioned Least-Privilege Learning for Executable Terminal and MCP Agents](https://arxiv.org/abs/2608.18351)

**<font color=#1a73e8>作者：</font>** Alexander Tu, Michael Tu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using large language-model agents can complete a task while exercising authority that the user did not grant or the task does not need, causing excess-authority errors. Traditional permission gating systems alone for validating agent environments are insufficient. We study whether post-training can teach a 4B-parameter model to choose task-conditioned authority in executable terminal and Model Context Protocol (MCP) environments to complement those measures. We propose a framework where each action is audited before execution and again from observed effects along six dimensions of risk. This auditing is conducted using deterministic verifiers that score completion, evidence, exact state, prohibited attempts, and safe success. In conjunction with predefined task-specific sufficient-authority envelopes, we determine task-specific excess privilege values for trajectories, which are then optimized for in post-training. We find that after training using this framework on Qwen3.5-4B over 1,500 tasks, the selected seed reaches 98.48% safe success across 2,896 evaluation episodes spanning all 500 held-out tasks, compared with 64.36% for the base policy, and reduces excess-authority error events from 4.56% to 0.79%. Furthermore, external tests show capability retention and prompt-directed improvement. A 400 task continuation study also found evidence of generalization, reducing excess-authority events by 6.99 percentage points while maintaining previous capabilities. We conclude learned restraint through least-privilege aware post-training is therefore useful as an additional control layer for tool-using agents in executable terminal and MCP environments, but it does not replace permission gates and sandboxing.

---


### 54. [Figurative and Cultural Knowledge in LLMs: Investigating Cross-Domain Transfer through Fine-Tuning](https://arxiv.org/abs/2608.18361)

**<font color=#1a73e8>作者：</font>** Mena Attia, Mona Diab, Thamar Solorio  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Figurative language is deeply culturally embedded; fluent use requires not just linguistic competence but cultural immersion. We ask whether LLMs can learn this link: does fine-tuning on cultural data improve figurative language understanding, and vice versa? We conduct a systematic study across four models (ALLaM-7B, Fanar-1-9B, Qwen3-8B, Llama-3.1-8B) and six Arabic datasets spanning cultural commonsense, proverbs, and poetry across diverse dialects and regions. Fine-tuning on poetry improves idiom comprehension (+2.33%, p<0.05), a gain our ArabicMMLU control does not reproduce, indicating that it stems from figurative content rather than Arabic language adaptation and pointing to a sensitivity to non-literal meaning that transfers across figurative types. Cultural fine-tuning, by contrast, lowers proverb-interpretation accuracy in both Arabic-centric models. Transfer between the two domains is otherwise indistinguishable from noise, with Arabic models frequently regressing after fine-tuning, suggesting prior saturation of relevant knowledge, while multilingual models show greater adaptation headroom. Error analysis further reveals that fine-tuning reinforces experiential cultural knowledge while destabilizing historically grounded factual knowledge. Our findings suggest that the relationship between culture and figurative language, though conceptually natural, is not straightforwardly captured through fine-tuning alone.

---


### 55. [Selection, Recombination, or a Fresh Solve? A Candidate-Free Control for Single-Pass Test-Time Aggregation](https://arxiv.org/abs/2608.18379)

**<font color=#1a73e8>作者：</font>** Guiv Farmanfarmaian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When every candidate is wrong, correct-candidate selection is unavailable, yet the aggregation call can still solve the problem afresh. A correct aggregate answer may therefore reflect recombination, fresh solving, or both. For efficient test-time reasoning, the relevant question is whether candidate context adds value beyond the additional generation pass. We introduce the missing candidate-free control under the same maximum output-token allowance and stratify by the number of correct candidates. Across AIME-2025 and HMMT-2025 with Qwen3-4B, candidate conditioning improves accuracy when multiple candidates are correct ($\Delta_{\mathrm{cand}}$(c2+) = +0.290), lowers accuracy when every candidate is wrong ($\Delta_{\mathrm{cand}}$(c0) = -0.123), and remains unresolved in the one-correct regime. The c2+ and c0 conclusions survive a conservative correction for the adaptive two-benchmark procedure. Under this counterfactual, the interpretation of all-wrong recovery reverses at this scale: conditioning on an all-wrong candidate pool lowers accuracy relative to a fresh solve. Original-format matching and placebo results characterize the failures descriptively but leave their mechanism unresolved. Within a separate structured intervention, explicit answer fields causally steer outputs toward their values; masking yields no measurable accuracy improvement, and equivalence with the original format was not established. The evidence is limited to one Qwen3-4B family, two mathematics benchmarks, first-answer-truncated candidate fragments, and single-pass prompted aggregation.

---


### 56. [TTSD-FAR: Test-Time Self-Distillation with Fisher-Anchored Restoration for Missing-Modality Emotion Recognition in LVLMs](https://arxiv.org/abs/2608.18386)

**<font color=#1a73e8>作者：</font>** Muhammad Haseeb Aslam, Alessandro Koerich, Marco Pedersoli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large video-language models (LVLMs) have shown remarkable performance on multimodal tasks like multimodal emotion recognition (ER) in the wild. ER is inherently multimodal, requiring a joint understanding of facial expressions, vocalizations, language, biosignals, and gestures. However, real-world deployment remains challenging: modalities may be missing or noisy at test time. Partial observations can be viewed as a distribution shift relative to the complete-modality distribution. SOTA TTA methods based on entropy minimization or perplexity reduction do not transfer to autoregressive LVLMs, while retrieval augmented generation (RAG) degrades when the observed modality is weak. Because no ground-truth supervision exists to verify individual updates, adaptation across this stream risks accumulating drift and degrading once the model departs from a reliable solution. An effective solution must therefore adapt to arbitrary missing-modality patterns and remain effective during continual adaptation. We address both jointly with Test-Time Self-Distillation (TTSD), a parameter-efficient framework in which a frozen teacher, trained on complete modalities, guides an adaptive low-rank student via self-distillation, updating only a negligible number of parameters. Stability is built into this same loop through Fisher-Anchored Restoration (FAR), which monitors Fisher information stability to detect convergence versus drift and restores the student toward the teacher's anchor when distributional shifts are identified. Our experiments on MELD, DFEW, and BAH under 0%-50% missing modalities show that this unified adaptation-restoration design consistently outperforms entropy-based adaptation, RAG, and perplexity-based generation over long adaptation horizons, where baselines without restoration progressively degrade while TTSD-FAR remains consistent.

---


### 57. [A Jagged Frontier: Evaluating Robustness of Code Agents to Semantics-Preserving Transformations](https://arxiv.org/abs/2608.18389)

**<font color=#1a73e8>作者：</font>** Hasan Najib Mahmud, Shreya Gupta, Isha Chaudhary 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI code agents are increasingly deployed to resolve real software issues, yet their reliability under superficial code variations remains poorly understood. We evaluate whether coding agents that repair repository-level issues remain reliable when the surrounding codebase is rewritten into a semantically equivalent form. We introduce a random variant sampler that applies common semantics-preserving transformations (SPTs) - spanning control-flow rewrites, dead-code injection, and identifier renaming - to produce perturbed variants. We evaluate two agentic scaffolds (mini-SWE agent and OpenCode) each backed by one of four frontier models (Claude Opus 4.5, Kimi K2.5, MiniMax M2.5, and Qwen 3.6-27B) across instances drawn from SWE-bench Verified and SWE-bench Pro. For each instance, the agent is run multiple times on the unperturbed and perturbed variants, yielding paired resolve-rate estimates that isolate the perturbation effect from intrinsic stochasticity. We find small degradation in most configurations: up to 6.7 percentage points mean resolve-rate drop in the most affected configurations with statistically significant degradations in 6 of 16 configurations of model, scaffold, and dataset. Crucially, no single model ranking by robustness holds across scaffolds - Qwen is among the most robust under mini-SWE agent on SWE-bench Verified yet the most brittle under OpenCode - revealing a jagged robustness frontier. The simpler scaffold (mini-SWE agent) is more robust to perturbation. Our results demonstrate that even top frontier models are susceptible to semantics-preserving perturbations although the effect is not uniform, raising concerns about the deployment reliability of AI code agents in diverse real-world codebases.

---


### 58. [LEDGER: Claim-to-Evidence Trace Graphs for Auditing LLM Agents](https://arxiv.org/abs/2608.18398)

**<font color=#1a73e8>作者：</font>** Daehong Kim, Haichao Miao, Shusen Liu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can now carry out long-horizon technical workflows involving complex tool use, code execution, file edits, and generated artifacts. As agents do more work faster, the productivity bottleneck shifts from producing outputs to auditing whether those outputs are correct and trustworthy. Agent observability systems make fine-grained execution events visible, but visibility alone still leaves reviewers to reconstruct which actions, artifacts, and validation steps matter for a particular conclusion. We introduce LEDGER - Layered Evidence and Decision Graphs for Execution Review, a tracing and review system that builds layered trace graphs over observed agent sessions. LEDGER preserves Trace Records while grouping them into Evidence Nodes and Workflow Nodes, representing artifacts as evidence anchors, and adding typed semantic edges that connect claims to supporting actions, artifacts, and checks. Through data-analysis and coding examples, we show how the resulting traces expose workflow decisions, artifact lineage, repair steps, validation coverage, and claim-support paths for evidence-centered audit.

---


### 59. [Multimodal Rapport Estimation in Real-World HRI](https://arxiv.org/abs/2608.18401)

**<font color=#1a73e8>作者：</font>** Akihiro Sakuramoto, Takato Hayashi, Ryo Miyoshi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Evaluating interaction quality in real-world HRI is an important challenge. If interaction quality can be estimated reliably, the results can be used to improve dialogue strategies and ultimately enable robots to adapt their behavior autonomously. However, existing automatic evaluation methods have been developed primarily in controlled laboratory settings, and it remains unclear whether they can be directly applied to real-world environments, where users are free to disengage and multi-party participation may arise naturally. In this study, we investigate the automatic estimation of third-party-rated rapport scores using 62 sessions of multimodal recordings collected in a Japanese drugstore. We compare zero-shot LLMs, pretrained text, audio, and visual models, and their prediction-level fusion. The results show that, in real-world HRI, zero-shot LLMs achieve strong performance, while audio and visual models tend to provide complementary information. In particular, Gemini 2.5 Flash performs strongly as a single model, and a fusion model combining Gemini (text) with HuBERT and V-JEPA performs best overall. Further analyses showed that estimation performance varied across interaction-duration and group-size conditions. These findings suggest that rapport estimation in real-world HRI requires evaluation and model design that account for contextual variability beyond that assumed in laboratory settings.

---


### 60. [Improving Natural-Language Combinatorial-Optimization Accuracy in Resource-Constrained Language Models via Formal Abstractions](https://arxiv.org/abs/2608.18409)

**<font color=#1a73e8>作者：</font>** Shrenil Shaun Sharma, Avi Sharma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Combinatorial scheduling poses a significant challenge for language models, requiring them to identify feasible solutions within exponentially large search spaces while satisfying complex constraints. This challenge is especially pronounced in resource-constrained settings, where larger language models are impractical and selection is limited to smaller models which often fail to preserve feasibility when scheduling directly from natural language. To address these limitations, we introduce SDDL, a neuro-symbolic framework that translates natural-language scheduling problems into compact, solver-aligned representations of tasks, resources, constraints, and objectives, while delegating low-level modeling and search to a deterministic compiler and external solver. On a 300-instance, multi-family subset of scheduling problems, SDDL improves independently verified feasibility for every resource-constrained model tested. The two strongest SDDL configurations reach 55.3% and 28.3%, up from direct-generation baselines of 23.7% and 1.3% and solver-code baselines of 21.7% and 7.0%, with a 0.0% median optimality gap among feasible schedules. By expressing problem structure rather than generating solutions or solver code, SDDL enables smaller models to approach the strongest evaluated direct- and solver-code configurations, including substantially larger frontier models.

---


### 61. [Role-Conditioned Sub-Token Routing for Efficient Vision-Language-Action Policies](https://arxiv.org/abs/2608.18410)

**<font color=#1a73e8>作者：</font>** Wei Jiang, Wei Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models process long multimodal token sequences, making inference expensive in both memory and computation. Existing efficiency methods mainly reduce visual tokens, but aggressive token pruning becomes fragile because removing a token discards its entire representation. Sub-token compression provides a complementary alternative by retaining more tokens while reducing their value width. However, directly applying sub-token compression to VLA policies is less effective because information important for perception, language understanding, and control is distributed differently across the multimodal representation.
We introduce Role-Conditioned Sub-Token Routing (RoleSub), which learns how to compress the value representations of retained tokens. After visual token reduction, RoleSub partitions each retained value representation into groups in an orthogonal space and uses a lightweight router to determine which groups should be preserved. The routing decision is conditioned on the token representation, a learned latent role representation, and language context. The same mechanism can also be applied to language values, allowing visual and language representations to be compressed without removing additional tokens.
We evaluate RoleSub on OpenVLA-OFT-7B across the four LIBERO suites. At matched visual-KV budgets, RoleSub outperforms a trained token-only control in 33 of 36 settings, with the largest gains under aggressive compression. Combining visual and language compression reduces total KV to 9.2--11.3% of the original while retaining strong control performance on most tasks. These results show that reducing the representation within retained tokens provides an effective complement to token pruning for aggressive VLA compression.

---


### 62. [Mechanistic Interpretability of Structure-Aware Numerical Reasoning in LLaMA 3.1 8B](https://arxiv.org/abs/2608.18419)

**<font color=#1a73e8>作者：</font>** Rahul Chowdhury, Timothy A Rupprecht, Senhao Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that large language models (LLMs) exhibit strong numerical sequence modeling capabilities and show promise in time-series prediction. While LLMs display in-context learning capabilities, the mechanisms with which they accomplish time-series prediction remain unclear. Specifically, whether they truly understand the underlying structure, which at a minimum requires reasoning over first differences in the sequence of numbers. To study this, we investigate Llama 3.1-8B from a mechanistic interpretability point of view. Mechanistic interpretability is an emerging field concerned with the reverse engineering of the algorithms learned by neural networks such as LLMs. To assess Llamas' numerical sequence modeling capabilities and to facilitate our mechanistic interpretability analysis, we create a sequence modeling task that cannot be solved without picking up structural cues. Specifically, we sample n random numbers and repeat them with an offset. We find that Llama displays strong performance on our tasks suggesting that it can pick up on the underlying structure. To understand the mechanisms that allow it to do so, we perform probing experiments and activation patching based counterfactual analysis. Probing reveals that the model computes and stores first differences in its internal representations without explicit supervision, indicating that it tracks structural information about the sequence. Activation patching reveals that Llama retrieves the relevant first-difference with a mechanism similar to an induction circuit and subsequently adds it to the current value. Notably, our work represents one of the first studies to identify this form of concept induction in LLMs.

---


### 63. [FM-Bench: A Benchmark for Long-Horizon Management with Competing Agents](https://arxiv.org/abs/2608.18423)

**<font color=#1a73e8>作者：</font>** Tianyou Wang, Chongyang Gao, Kezhen Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model agents now execute bounded tasks reliably. Whether they can sustain effective decision-making over long horizons, where actions have cumulative consequences and the environment responds to their choices, remains largely unmeasured. FM-Bench (Football Management Benchmark) measures this. An LLM agent runs a football club for 20 in-game years through 26 tools and roughly 340 to 400 decision stops. It drafts a squad on the same budget as every rival, trades players, negotiates contracts, invests in facilities and youth, sets lineups, and answers to a board that can fire it, while a deterministic engine accumulates every year into one final score with no LLM judge or human rater. The solo track plays each of 15 frontier models against a frozen scripted world, and the Arena places the same models plus a scripted anchor in one shared 20-year world; to our knowledge, the first head-to-head evaluation at this scale. We measure six behavioral capabilities behind the score. Across three seeds, all 15 models complete every horizon while the blind scripted baselines die out in most of theirs, and claude-fable-5 tops the solo board on mean score and the Arena, where the title nonetheless rotates among ten models. Neither scale, price, nor vendor predicts the order; the order settles only late in the horizon, and the best first-play human lands only at the bottom of the model board. What separates the models is managerial behavior rather than computation. Higher-scoring models reduce slow-payoff investment near the end, keep cash invested rather than idle, and open renewals well before the deadline, while token spend predicts nothing. No model learns the market's hidden prices from hundreds of rejected bids, and self-managed memory fails in two opposite modes: an archive that only grows or a plan rewritten every season. Code is available at this https URL.

---


### 64. [Pedagogical AI in Mental Health: A Tri-Stream Fine-Tuned LLM Framework for Automated Clinical Supervision and Risk Triage](https://arxiv.org/abs/2608.18438)

**<font color=#1a73e8>作者：</font>** Shreeya Sharma, Ravish Gupta, Saket Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern mental healthcare faces a critical shortage of senior supervisory oversight, leading to a "supervision gap" where novice therapists manage high-stakes risks with delayed professional feedback. This paper proposes a new framework utilizing a fine-tuned Mistral-7B-instruct model as an automated "Supervisor-in-the-Loop" system. By leveraging 106 sessions from the DAIC-WOZ dataset, the model performs a tri-stream analysis: (1) Therapeutic Alliance tracking via semantic adherence, (2) Latent risk prediction using attention-weighted analytics, and (3) Supervisory Triage via a Dynamic Clinical Urgency Index (D-CUI). Our multi-modal VAL (Visual-Acoustic-Linguistic) framework achieves 95% technique identification accuracy [95% CI: 75.1%-99.9%], alliance assessment MAE of 0.105 on a 5-point scale [95% CI: 0.059-0.151], therapeutic fidelity alpha = 0.423, and mean D-CUI of 0.370 [95% CI: 0.322-0.419]. Training converged in 105 steps with 85.2% loss reduction on a single Tesla T4 GPU. The system reduces supervisory triage latency from 72 hours to real time (~10 seconds per session), enabling proactive intervention in high-risk cases. The system addresses the cold-start problem through Bayesian priors and implements timestamp-based modality synchronization for robust multi-modal fusion.

---


### 65. [Reducing Technician Search Burden: A Multimodal RAG for Cessna 172 Maintenance Manual](https://arxiv.org/abs/2608.18465)

**<font color=#1a73e8>作者：</font>** Seongjun Ha, Md Rashedul Islam, Gaurav Nanda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Proper use of the aircraft maintenance manual is essential for correct maintenance, providing procedures, diagrams, cautions, and specifications. However, technicians often avoid consulting it because it is difficult to navigate and time-consuming under strict schedules. Retrieval augmented generation (RAG) models have recently been introduced in aircraft maintenance, yet existing models focus solely on textual retrieval. This research therefore targeted the Cessna 172 Maintenance Manual (C172-MM), widely used in general aviation, and developed a multimodal manual retriever (MMR) capable of retrieving multimodal manual pages. Retrieval performance was evaluated using synthetic queries covering procedures, diagrams, caution/safety information, and specifications; the MMR achieved 93.37% recall@5. Beyond retrieval, a multimodal RAG (MRAG) pipeline was examined, in which retrieved pages were input to a vision-language model that generated responses to the synthetic queries, achieving 87.20% semantic similarity to ground-truth answers. Three practical feasibilities were also assessed: inference time, operational cost, and interpretability. Average retrieval time for five pages was 11.93 seconds and response generation took 4.95 seconds, at $0.0091 per query, while interpretability was validated through heatmap visualizations. These results indicate that the MRAG pipeline for the C172-MM can reduce the time technicians spend searching manuals and retrieving multimodal information.

---


### 66. [A Locally Deployable Tool-Grounded LLM Multi-agent Framework for Automating Methane Emission Analysis and Reporting](https://arxiv.org/abs/2608.18473)

**<font color=#1a73e8>作者：</font>** Yang Yan, Zifan Zhou, Xuan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Methane field monitoring requires the integration of sampling design, meteorological interpretation, sensor processing, plume analysis, visualization, and reporting, but these steps are often distributed across separate expert-driven workflows. We developed a locally deployable, tool-grounded large language model (LLM) multi-agent framework for our low-cost methane sensing and field-monitoring campaigns. The framework uses LLM agents as workflow coordinators that link field measurements, meteorological data, deterministic sensor-processing routines, Gaussian plume inversion, and report generation, rather than directly estimating methane concentrations or emissions. Extensive field deployments across diverse real-world environments (e.g., wastewater treatment facilities, landfills, and oil and gas sites) demonstrate that our framework can achieve 92.0\% accuracy in workflow routing and parameter extraction, 85.0\% success in emission-rate estimation and plume prediction, and 95.0\% success in generating editable reports under practical operating conditions. Compared with manual and general-purpose LLM-assisted workflows, it reduced workflow time from hours-level to minutes-level, lowered manual coordination and prompt-engineering requirements, and retained traceable plume-based outputs. In addition, most processing can be performed locally, reducing exposure of sensitive facility and field data to cloud services. These results indicate that tool-grounded LLM coordination can reduce the time, labor, usability, and data-security barriers of methane field monitoring.

---


### 67. [COSTA: A Cluster-Centric Paradigm for Annotation-Free Open-Set Semantic Segmentation of Aerial Point Clouds with Domain Shifts](https://arxiv.org/abs/2608.18479)

**<font color=#1a73e8>作者：</font>** Yanghong Lin, Li Fang, Tianyu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation of aerial point cloud is trapped in a generalization crisis under distinct domain shifts. While test-time adaptation offers a privacy-preserving and computationally efficient way to adapt pre-trained models to unlabeled target-domain data during inference, existing methods, bound to closed-set label assumptions and non-scalable point-wise segmentation pipelines, still struggle with semantic shifts. We ask: can we adapt any given pre-trained aerial point cloud segmentation model to a shifted target domain at the inference phase alone, without additional training, while segmenting target-specific categories beyond the source label space on demand? This paper introduces COSTA, which breaks this limitation by shifting from closed-set point-wise adaptation to cluster-centric open-set semantic propagation. Our core discovery is that, once effectively adapted at test time, the rich feature distribution of aerial point clouds can be distilled into a compact set of well-separated semantic centroids that are transferable across label spaces. COSTA leverages this to reformulate open-set semantic segmentation as a cluster-level propagating process: it first bridges the domain gap through proven test-time adaptation, then groups each batch of target-domain points into a small set of semantic clusters based on the similarity distribution in the adapted feature space, and finally propagates high-confidence pseudo labels obtained from an open-vocabulary vision-language model to all points through cluster-level voting. This cluster-centric paradigm enables test-time adaptation of aerial point clouds under significant domain gaps with mixed semantic shifts. With DALES as the source domain, COSTA enables on-demand segmentation across three aerial point cloud benchmarks with distinct domains and heterogeneous category spaces, achieving up to 70.09% mIoU under this new setting.

---


### 68. [MissDiag: Diagnostic Evaluation of Incomplete-Knowledge Robustness in KGQA and KG-RAG](https://arxiv.org/abs/2608.18489)

**<font color=#1a73e8>作者：</font>** Hang Wang, Hang Dong, Lu Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graph question answering (KGQA) and knowledge-graph-based retrieval-augmented generation (KG-RAG) aim to ground answers in explicit graph evidence, but real-world knowledge graphs are often sparse, outdated, and incomplete. Existing robustness evaluations usually report aggregate changes in answer quality after evidence is removed or perturbed, which measures sensitivity to incomplete support but leaves the source of degradation under-specified: the same score change can conflate the type of missing evidence, the response of the evaluated system, and the sensitivity of the answer-matching protocol. To address this gap, we propose \textbf{MissDiag}, a diagnostic evaluation framework for incomplete-knowledge robustness in KGQA and KG-RAG. MissDiag keeps the question and gold answer fixed while applying structurally typed missingness interventions to benchmark-provided support graphs, enabling paired comparisons that decompose robustness changes by evidence type, system response, and evaluation protocol rather than reducing them to a single aggregate score drop. Experiments across multiple system families show that incomplete-knowledge robustness is better understood as a typed degradation phenomenon than as a uniform property: answer-adjacent evidence loss produces the largest observed degradation, source-context removal is often neutral and can be beneficial, and semantic answer matching changes absolute scores while preserving the main typed degradation patterns. By transforming aggregate robustness measurement into typed diagnostic attribution, MissDiag provides a more interpretable basis for comparing, diagnosing, and stress-testing KGQA and KG-RAG systems under incomplete knowledge.

---


### 69. [Bayesian Partner Modelling enables Adaptive Replanning for LLM Coordination](https://arxiv.org/abs/2608.18490)

**<font color=#1a73e8>作者：</font>** Harsh Goel, Aditya Sai Ellendula, Vaishnav Tadiparthi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent Large Language Model (LLM) systems often struggle to collaborate with new teammates whose strategies shift mid-task. Because agents execute multi-step or temporally extended skills, they frequently continue executing outdated plans long after public evidence shows that a partner has changed its skill. Existing methods either treat partner tracking as passive context-leaving the agent aware of the shift but slow to act-or replan indiscriminately. We introduce BayesBeliefAgent, which pairs a hierarchical LLM planner with a Bayesian tracking module. Rather than replanning constantly, our agent interrupts its current skill only when a partner's actions directly contradict the inferred skill. Beyond standard reward, we evaluate performance using replanning efficiency and the belief-action gap: the fraction of total decisions where an agent with a correct partner estimate executes a non-complementary skill. Across benchmark Overcooked environments, contradiction-conditioned control drastically narrows this belief-action gap while requiring an order of magnitude fewer replans than heuristic methods

---


### 70. [Tianmu-TC: Physics-constraints Generative Artificial Intelligence for Global Tropical Cyclone Forecasting](https://arxiv.org/abs/2608.18500)

**<font color=#1a73e8>作者：</font>** Shiqi Zhang, Pan Mu, Cheng Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tropical cyclones (TCs) pose severe risks from strong winds and heavy rainfall. However, forecasting their track and intensity remains challenging due to chaotic atmosphere and the rapid amplification of initial condition errors, leading to growing forecast uncertainty. While numerical weather prediction (NWP) and deep learning models have made progress, they remain computationally demanding and often fail under complex meteorological scenarios. Here, we present Tianmu-TC, a physics-constraints generative framework for global TC forecasting. Trained on Western North Pacific data, Tianmu-TC leverages physics-constraints to generate controllable outputs with reduced uncertainty thus improving forecast reliability. Experiments show Tianmu-TC outperforms deterministic and ensemble meteorological artificial intelligence models and authoritative NWP systems such as ECMWF in global ocean basins, with significantly lower computational cost. We further show Tianmu-TC performs well in challenging scenarios such as data sparsity, anomaly tracks, rapid intensification and weakening. These findings suggest physics-constraints generative AI offers a promising approach for reliable, efficient global TC forecasting.

---


### 71. [LLM-Powered Predictive Decision-Making for Sustainable Data Center Operations](https://arxiv.org/abs/2608.18503)

**<font color=#1a73e8>作者：</font>** Hanzhao Wang, Jingxuan Wu, Yumeng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growing demand for AI-driven workloads, particularly from Large Language Models (LLMs), has raised concerns about the significant energy and resource consumption in data centers. This work introduces a novel LLM-based predictive scheduling system designed to enhance operational efficiency while reducing the environmental impact of data centers. Our system utilizes an LLM to predict key metrics such as execution time and energy consumption from source code, and it has the potential to extend to other sustainability-focused metrics like water usage for cooling and carbon emissions, provided the data center can track such data. The predictive model is followed by a real-time scheduling algorithm that allocates GPU resources, aiming to improve sustainability by optimizing both energy consumption and queuing delays. With fast inference times, the ability to generalize across diverse task types, and minimal data requirements for training, our approach offers a practical solution for data center scheduling. This framework demonstrates strong potential for advancing sustainability objectives in AI-driven infrastructure. Through our collaboration with a data center, we achieved a 32% reduction in energy consumption and a 30% decrease in waiting time.

---


### 72. [UMER: Unifying Embedding and Ranking via Pair-Aware Discriminative Reasoning for Universal Multimodal Retrieval](https://arxiv.org/abs/2608.18504)

**<font color=#1a73e8>作者：</font>** Libiao Chen, Xiyang Liu, Yanheng Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Universal multimodal retrieval aims to support diverse instruction-aware retrieval tasks, demanding both efficient corpus-scale matching and fine-grained semantic reasoning. Recent MLLM-based embedding methods typically derive representations from hidden states, while Chain-of-Thought (CoT) reasoning is emerging as a promising strategy for embedding enhancement by encoding intermediate semantic evidence into the representation space. However, existing CoT methods typically use item-wise reasoning over queries and candidates in isolation, providing no explicit evidence to distinguish a positive from a semantically confusable hard negative. Moreover, contrastive embeddings capture global similarity but struggle with meta-tasks requiring answer verification, category judgment or fine-grained reasoning. In this paper, we propose UMER, a Unified Multimodal Embedding and Ranking framework for universal multimodal retrieval. UMER replaces item-wise reflection with Pair-Aware Discriminative Reasoning, which compares query--candidate pairs to identify instruction-relevant matching and discrepancy evidence. UMER jointly learns contrastive embeddings for efficient global matching and discriminative ranking for explicit pairwise relevance judgment within a single MLLM. A complementary mutual distillation strategy further transfers reliable pairwise preferences between the embedding and ranking functions. On the MMEB-V2 benchmark, UMER achieves state-of-the-art performance under comparable experimental settings while supporting budget-adjustable inference.

---


### 73. [Which Negatives Matter? Ask Your Text Encoder: Adaptive Similarity Margins for Dense-Caption Retrieval](https://arxiv.org/abs/2608.18521)

**<font color=#1a73e8>作者：</font>** Haoyue Liu, Ye Chen, Zhichao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dense-caption retrieval has recently been improved by introducing segmentation, edge maps, LLM-filtered captions, and cross-modal modules into contrastive fine-tuning. However, these methods largely inherit the same InfoNCE objective, whose optimization can prematurely saturate under a strong pre-trained initialization: on dense captions, the loss falls below 10^{-3} on 80% of batches within the first epoch, while its gradient reaches exact zero in fp32 in 47% of measurements. We find that this behavior is closely related to the large number of near-duplicate captions in dense-caption benchmarks, where a few highly similar negatives remain unresolved after the easy majority has already been separated. As a remedy, we introduce HN-CLIP, which uses the text encoder's own text-text geometry to construct per-negative adaptive similarity margins. Specifically, a detached caption-similarity matrix is added to the negative logits, assigning larger margins to more similar captions without mining, synthesizing, or resampling negatives. The resulting objective requires only one caption-similarity matrix and a masked logit addition during training, with no auxiliary data, additional parameters, offline preprocessing, or inference-time overhead. Extensive experiments on four dense-caption retrieval benchmarks show that HN-CLIP improves over the strongest competitors by +2.4--+4.3 R@1 while training 2.4x faster than GOAL and 5.4x faster than StructXLIP. Moreover, the proposed objective improves all six tested fine-tuning frameworks on the in-domain benchmarks and reaches the strongest full-data baseline with only 20% of the training data.

---


### 74. [DART-SD: Diamond-topology Aware Retrieval and Tuning for Self-Distillation of Multi-Turn Tool-Calling Agents](https://arxiv.org/abs/2608.18524)

**<font color=#1a73e8>作者：</font>** Hangrui Xu, Jiarui Wang, Yang Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Equipping Large Language Models (LLMs) with multi-turn tool-calling capabilities is essential for building autonomous agents. However, progress is fundamentally limited by the reliance on full-length trajectory imitation. For tasks involving multiple order-independent sub-goals, the optimal solution space forms a vast combinatorial diamond lattice. Forcing this rich topology into monolithic trajectories causes a severe topological collapse, indiscriminately penalizing valid alternative explorations and severely degrading policy diversity. To address this, we propose DART-SD (Diamond-topology Aware Retrieval and Tuning for Self-Distillation), a novel framework that shifts the paradigm from global forcing to topology-guided localized correction. DART-SD first models the execution process as a converging Interaction-State Transition Graph (ISTG), faithfully capturing the inherent diamond topology of successful and failed exploratory paths. During autonomous rollouts, the framework identifies the Critical Topological Breakpoint (CTB) and retrieves success-supported recovery references. Finally, we introduce a progressive self-distillation paradigm through CTB-guided localized supervision, ensuring that the training loss is calculated exclusively on the generated recovery steps while strictly protecting the valid reasoning prefix from destructive gradient updates. Experiments on complex multi-turn tool-calling benchmarks demonstrate that DART-SD significantly outperforms traditional full-trajectory baselines.

---


### 75. [Pairwise Ranking Outperforms Single-Action RL for Offline Explanation Selection: A Practical Lesson](https://arxiv.org/abs/2608.18531)

**<font color=#1a73e8>作者：</font>** Tanay Chowdhury, Saeideh Shahrokh Esfahani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial explainable-recommendation systems built on LLMs incur a substantial serving cost: each request triggers an LLM generation, with latency in the hundreds of milliseconds and cost that scales linearly with traffic. We separate generation from selection: explanations are produced ahead of time as a frozen candidate pool (six prompt styles, two commodity LLMs), and a small CPU-resident selector picks one at request time. The stack needs no GPU and returns in under 100 ms.
Our primary benchmark is a 2,958-pair XRec Google Local subset, evaluating six offline-pool selectors (LambdaRank, PPO, GRPO, DPO, teacher-student distillation) and three KG-path selectors (random walks, edge-disjoint enumeration, MMR-reranked paths). A 300-pair MovieLens-1M split with Claude-Sonnet-4.5 references serves as an internal cross-dataset check, since no public benchmark exists for this setting. All variants use the same BERTScore-F1 protocol as XRec and G-Refer, averaged across five seeds.
LambdaRank reaches F1 = 0.500 on Google Local, exceeding both G-Refer and XRec, and F1 = 0.329 on the MovieLens-1M check. With seed variance below 0.003 F1, the ordering is reliable: pairwise learning-to-rank outperforms single-action RL (PPO, GRPO, DPO), which use only one labelled candidate per rollout, leaving K-1 labels unused.
The KG-path family targets a different objective: all three variants reach USR = 1.000 on Google Local and 0.997-1.000 on MovieLens-1M, since per-request path grounding yields a unique output per query, avoiding template-collapse failures affecting cached-LLM outputs.
A generator-pool study comparing Claude 3 Haiku and Claude Haiku 4.5 shows small F1 shifts (0.001-0.006) while preserving selector ranking: selector and generator can be evaluated independently, though absolute F1 depends on the generator. End-to-end build cost is near $15 on commodity hardware.

---


### 76. [StateTrace: An Object-Centric Framework for Hidden-State Spatiotemporal Reasoning in Long Videos](https://arxiv.org/abs/2608.18532)

**<font color=#1a73e8>作者：</font>** Yu Han, Wenhao Li, Yichao Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing VLMs have achieved strong performance in video understanding, yet they struggle with long-video spatiotemporal reasoning when target objects become invisible, often mistaking "invisible" for "unknown". We define this challenge as hidden-state spatiotemporal reasoning: inferring object states during prolonged invisible intervals from context interactions. To address this, we propose StateTrace, a novel object-centric framework that endows VideoLLMs with an explicit mechanism for hidden state reasoning in long videos. StateTrace builds a reusable spatiotemporal state memory that organizes object trajectories, inter-object relations, and state-transition events into a structured reasoning substrate. At inference time, it retrieves question-relevant state-evolution trajectories and converts them into compact reasoning cues, enabling the model to explicitly reason about why an object disappears, how its state evolves while invisible, and whether that state should persist at query time. We further build HSR-Bench, a diagnostic benchmark for hidden-state reasoning, containing 1,427 video-QA samples from 1,384 unique videos. Extensive experiments across multiple VideoLLMs show that StateTrace consistently improves performance on both public benchmarks and HSR-Bench (e.g., improving VideoLLaMA3 from 39.6 to 64.2 on HSR-Bench).

---


### 77. [FinRCA-Bench: Benchmarking Evidence Retrieval and Reasoning for Financial AI Systems](https://arxiv.org/abs/2608.18534)

**<font color=#1a73e8>作者：</font>** Pratik Ghawate  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to support financial operations, but their apparent reasoning performance can depend on whether they receive the right evidence. In financial reconciliation, the evidence needed for diagnosis is distributed across invoices, purchase orders, approvals, allocations, payments, ledger entries, and bank activity, linked by transactional relationships rather than textual similarity. End-to-end accuracy can therefore conflate evidence access with reasoning quality. We introduce FinRCA-Bench, a deterministic synthetic benchmark of 2,250 accounts-payable-to-bank reconciliation cases spanning 14 operational tables, including 1,500 injected failures across 15 causal categories and 750 legitimate or hard-negative cases. Root-cause labels and record-level evidence contracts are hidden from the model, allowing retrieval to be evaluated independently of answer correctness. We compare Rules/SQL, classical machine learning, dense semantic retrieval, deterministic relational expansion, and Typed Provenance Graph Retrieval (TPGR), a typed traversal restricted to persisted transaction relationships. Rules/SQL reaches 84.97% held-out exact accuracy and classical ML reaches 95.44%. Holding the reasoning model, prompt, and generation settings fixed while changing only retrieval increases macro required-record recall from 0.83% to 77.70% and exact 16-class accuracy from 2.05% to 72.44%. Structural retrieval failures outnumber reasoning failures with sufficient retrieval by 95 to 15; 254 correct predictions occur despite incomplete retrieval, and strict returned-evidence contract accuracy is only 5.72%. On FinRCA-Bench, retrieval architecture strongly shapes observed AI-system performance, and a correct root-cause label is a weak proxy for an auditable diagnosis.

---


### 78. [Evaluating and Explaining Prompt Sensitivity of LLMs Using Interactions](https://arxiv.org/abs/2608.18539)

**<font color=#1a73e8>作者：</font>** Ruiyang Qin, Qingzhuo Wang, Tian Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The remarkable capabilities of large language models (LLMs) are often undermined by their instability. Even subtle and semantically irrelevant changes in prompts can cause dramatic fluctuations in performance, a phenomenon known as prompt sensitivity. Previous studies typically evaluate prompt sensitivity by comparing the LLM's final outputs when prompts change. However, such coarse-grained metrics fail to explain the internal reasons for prompt sensitivity. In this paper, we introduce interactions as a fine-grained tool to analyze prompt sensitivity of LLMs. Specifically, we decompose the output score of the LLM into a set of interactions. Each interaction represents a nonlinear relationship involving a set of input variables. We discover that subtle changes to prompts can trigger severe instability in interactions, even when the outputs of the LLM remain the same. To this end, we propose an Interaction-based Prompt Sensitivity (IPS) metric by quantifying changes in interactions when we introduce subtle changes to prompts. We apply the IPS metric to 50 open-source LLMs and uncover four factors that reduce the prompt sensitivity of LLMs, including supervised fine-tuning, increased model scales, dense architectures, and few-shot learning. More crucially, we discover a common mechanism by which these four factors reduce prompt sensitivity: all four factors tend to reduce the prompt sensitivity of low-order interactions (i.e., interactions involving few input variables).

---


### 79. [Shared Circuits for Shared Grammar: Tracing Subject-Verb Agreement Across Languages](https://arxiv.org/abs/2608.18545)

**<font color=#1a73e8>作者：</font>** Isabella Gidi, Antonio Almudévar, Core Francisco Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual large language models often generalize across languages, and prior work suggests that their internal mechanisms can overlap cross-lingually. It remains unclear, however, when such sharing emerges and whether it varies with the overt realization of the same grammatical operation. We investigate this question for present-tense subject-verb agreement, a morphosyntactic process that varies substantially across languages and is only weakly expressed in English. Using activation patching and attention analysis across 29 languages and five open-source model families, we identify the attention heads causally implicated in agreement and compare these head-level signatures across languages. We find that languages with overt person/number inflection exhibit more similar agreement circuitry than non-conjugating languages, with the strongest sharing appearing when the analysis isolates recovery of the inflectional contrast itself. English provides an informative bridge case, becoming more similar to conjugating languages precisely in contexts where overt agreement is required. Finally, many implicated heads display similar attention patterns across languages, suggesting that cross-lingual overlap reflects shared functional roles as well as shared localization. Together, these results indicate that multilingual LLMs reuse partially shared computational structure for morphosyntactic agreement rather than relying on fully separate language-specific solutions.

---


### 80. [SemanticSlider3D: Training-Free Continuous Semantic Editing for 3D Objects](https://arxiv.org/abs/2608.18560)

**<font color=#1a73e8>作者：</font>** Ru Wang, Rahul Jain, Koichiro Niinuma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Fine-grained control over continuous semantic attributes of 3D objects is essential for 3D content creation, but is not well supported by conventional 3D modeling workflows or prompt-based interaction with existing generative AI tools. While slider-based methods have proven effective for fine-grained semantic control in 2D image generation, no equivalent approach exists for 3D. Extending these 2D methods to 3D is non-trivial due to challenges unique to 3D, including geometric integrity and cross-view coherence. We present SemanticSlider3D, a technique for continuous semantic attribute editing of 3D objects that requires no per-attribute training. Given a user-specified attribute, our pipeline constructs a semantic editing direction in the latent space of a state-of-the-art 3D generation model, presenting a diverse and coherent spectrum of 3D variations. A technical validation on a dataset of 50 3D object-attribute pairs shows our method was preferred by all five human assessors across variation range, consistency, 3D object quality, and attribute disentanglement, over a baseline combining a 2D slider with an image-to-3D model. An exploratory study with six participants demonstrates that SemanticSlider3D supported decision-making in 3D prototyping and was perceived as a valuable addition to existing workflows.

---


### 81. [PATE-Forensics: Perception-as-Tool for Explainable Deepfake Forensics with General-Purpose MLLMs](https://arxiv.org/abs/2608.18573)

**<font color=#1a73e8>作者：</font>** Yaqi Li, Jielun Peng, Yabin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing explainable deepfake forensic methods typically rely on task-adapted MLLM to jointly address detection, localization, and explanation. Inspired by agent-style tool use, we instead introduce a Perception-as-Tool paradigm and instantiate it as PATE-Forensics, which architecturally decouples detection and localization from explanation generation while coupling detection and localization as tightly as possible within a forensic perception tool. The DINOv3-based tool couples a multi-granularity detection module that integrates global, patch-level, and segment-level evidence with a cue-guided localization module by spatializing the patch-level and segment-level evidence into forgery score maps that guide dense mask prediction. The original image and forensic perception outputs produced by the tool form structured forensic context for a general-purpose MLLM, which is guided by prompt constraints to generate explanations without task-specific fine-tuning. On DDL-X Track 3, PATE-Forensics achieves the best official score of 0.89, outperforming the second-ranked team by 0.19 points. Our code is available at this https URL.

---


### 82. [Beyond LLM-Based Reasoning: Lightweight GNNs for Agent Failure Attribution](https://arxiv.org/abs/2608.18575)

**<font color=#1a73e8>作者：</font>** Ting-Wei Li, Yuanchen Bei, Xiao Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems (MAS) often exhibit complex failure modes, which frequently cause agents to produce incorrect outcomes. This motivates the task of Agent Failure Attribution: given a failed multi-agent trajectory, identify the faulty agents and their corresponding error types. Existing approaches predominantly rely on LLMs to perform failure attribution, either through direct prompting, fine-tuning on synthetic data or complex agentic pipelines. While effective, these methods incur substantial computational overhead due to long-context processing, expensive post-training and handcrafted workflows. Moreover, empirical evidence shows that even state-of-the-art models achieve limited accuracy on existing benchmarks, suggesting that scaling model size alone is insufficient. In this work, we revisit this task and question the necessity of such expensive generative solutions. We introduce AFANet, a lightweight graph-based framework that models interaction trajectories through step-level semantic signals and agent-level relationships. We show that with significantly fewer parameters and near-zero inference cost, AFANet (i) matches or outperforms LLM-based baselines, including fine-tuned models on in-domain benchmarks, (ii) maintains robust performance across different GNN architectures and (iii) can be further improved with inexpensive test-time adaptation on the OOD benchmark. Our results suggest that effective agent failure attribution does not require heavy LLM reasoning and a lightweight, structured approach can achieve strong performance.

---


### 83. [Compress and Forget: bitsandbytes Quantization Amplifies Proactive Interference in LLMs](https://arxiv.org/abs/2608.18578)

**<font color=#1a73e8>作者：</font>** Shayan Shahrabi-Farahani, Dara Rahmati  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Proactive interference (PI) is a documented failure mode in large language models in which retrieval of a repeatedly overwritten value degrades as prior overwrites accumulate, mirroring a classical phenomenon in human working memory. Post-training quantization (PTQ) is now the default deployment path for open-weight models, yet its effect on this failure mode has not been tested. We evaluate three precision levels (FP16, INT8, INT4/NF4, via bitsandbytes) across three architecturally distinct instruction-tuned models (Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3, Phi-3.5-mini-instruct), holding the retrieval task fixed. INT4 quantization significantly reduces accuracy under high interference in every model (e.g., from 81.0% to 68.3% for Qwen), confirmed by paired McNemar's tests ($p \le 2.6 \times 10^{-6}$) and a mixed-effects regression spanning all interference levels; INT8, often assumed safe, also carries a smaller but real penalty in two of three models. The effect is specific to semantically similar (word-type) distractors and reverses sign under a numeric control condition, and is mechanistically linked to a rise in same-key intrusion errors under INT4 (from 21.5% to 24.6% of trials, $p = 4.8 \times 10^{-7}$). A follow-up ablation shows the effect originates in the quantized transformer backbone rather than the output projection layer. These results suggest that bitsandbytes 4-bit quantization can impose an additional cost on applications relying on long, updatable, semantically dense contexts, even when aggregate benchmark accuracy appears largely unaffected. We release our code and tokenizer-verified vocabulary construction method at this https URL

---


### 84. [MR-IQA-2: Faithful Image Quality Reflection via Fine-Grained Credit Assignment](https://arxiv.org/abs/2608.18579)

**<font color=#1a73e8>作者：</font>** Yuan li, Youyuan Lin, Chenhui Chu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have shown strong potential for image quality assessment (IQA) by improving consistency between quality ratings and their underlying reasoning. However, most approaches supervise reasoning through human-provided ratings and rarely examine whether it faithfully reflects image quality. Rating accuracy alone does not ensure faithful reasoning; a shared reward also obscures supervision sources and may reinforce unfaithful reasoning when a correct rating occurs by chance. To improve the faithfulness and reliability of blind IQA, we aim to (1) decouple credit assignment for reasoning and rating and (2) provide verifiable supervision for faithful reasoning. We introduce MR-IQA-2, an actor-editor-judge framework that operationalizes reasoning-editing-reflection. The actor generates quality reasoning for an input image, and the editor revises the image according to the identified quality factors. A frozen judge compares the original and edited images and provides reflective supervision for the actor's reasoning. MR-IQA-2 further uses fine-grained credit assignment to decouple reasoning and rating supervision. Judge feedback supervises reasoning, whereas human ratings supervise the predicted rating. Masked token-specific updates distinguish these signals while preserving the causal relation from reasoning to rating. Across IQA benchmarks, MR-IQA-2 achieves competitive rating alignment with humans. Visual reflection also enables richer and more faithful visual understanding beyond rating, which may inform image-quality optimization and related downstream tasks. Code is available at this https URL.

---


### 85. [From Storage to Access: Verifiable Activation of Parametric Knowledge in LLMs via Explicit Priming and Implicit Reasoning](https://arxiv.org/abs/2608.18581)

**<font color=#1a73e8>作者：</font>** Zuocheng Ying, Yang Yang, Yumou Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although Large Language Models (LLMs) encode rich factual knowledge in their parameters, reliably recalling and verifying such knowledge remains a key bottleneck in factual question answering. Existing end-to-end methods entangle knowledge elicitation with reasoning, making it difficult to determine whether correct answers arise from parametric knowledge or the input context. To address this challenge, we propose VAKE (Verifiable Activation of Parametric KnowledgE), a two-stage reinforcement-learning framework that externalizes latent parametric knowledge through explicit Priming and transfers the acquired elicitation capability to implicit Reasoning. Given a query and an insufficient retrieved subgraph, the Priming policy explicitly inserts bridging triples as verifiable evidence, with supervision provided by rewards derived from answers generated by a separate frozen model over the augmented subgraph. Building on the policy learned during Priming, the Reasoning stage trains the model to answer from the original input, testing whether the capability acquired through explicit knowledge elicitation transfers to implicit reasoning. Experiments across seven benchmarks and models from 3B to 14B show that VAKE consistently outperforms standard baselines, including when transferring directly from HotpotQA to OOD datasets. LLM-based evaluation further shows that over 80% of the inserted triples provide factual bridging knowledge not derivable from the retrieved context, while more than half elicit knowledge inaccessible through direct prompting. These results suggest that VAKE activates latent parametric knowledge rather than copying the input context or memorizing dataset-specific associations.

---


### 86. [OmniHandwritingOCR: A Diagnostic Benchmark for Evaluating Multimodal LLMs in Handwritten OCR Scenarios](https://arxiv.org/abs/2608.18586)

**<font color=#1a73e8>作者：</font>** Zinuo Guo, Min Zhang, Bo Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are increasingly used as OCR systems in document and knowledge-processing pipelines, but their ability to faithfully read real handwriting remains underexplored. Existing OCR benchmarks focus largely on printed text or clean single-line inputs, leaving limited coverage of realistic handwritten OCR scenarios such as multilingual handwriting, writer errors, and structurally complex mathematical expressions. We introduce OmniHandwritingOCR, a diagnostic benchmark for evaluating MLLMs and OCR systems on handwritten OCR. It covers handwritten text recognition and handwritten mathematical expression recognition across six subtasks and twelve subsets, totaling 77.57K labeled images from public datasets and newly collected student writings. A key component is a difficulty-stratified multi-line formula corpus designed to test robustness under increasing structural complexity. We evaluate thirteen open- and closed-source systems with five complementary metrics under a unified protocol. Results show that current systems remain far from faithful transcription: performance drops sharply on complex multi-line formulas, model rankings vary across language and formula settings, and several generative models hallucinate plausible but visually unsupported corrections. OmniHandwritingOCR provides a challenging testbed for diagnosing language, content, structural, and visual-grounding failure modes of multimodal models in handwritten OCR scenarios.

---


### 87. [Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference](https://arxiv.org/abs/2608.18591)

**<font color=#1a73e8>作者：</font>** Zishan Ahmad, Vishal Vaddina  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Uniformly allocating inference reasoning budgets to LLMs is expensive and prone to over-thinking penalties; especially in document tasks where visual layouts drive complexity. To address this, we introduce BudgetDoc, the first multimodal benchmark providing explicit supervision for model-budget-performance trade-offs across three document tasks. Using BudgetDoc, we train DRB (Document-Reasoning Balancer), an approx. 1B-parameter pre-flight estimator (SigLIP-2 + Qwen3-0.6B) that predicts ordinal model performance across budget levels, achieving a 0.753 weighted F1. When dynamically allocating reasoning budgets across five frontier models and three datasets, DRB matches or improves F1 scores compared to always-maximum-budget baselines in 9 of 15 configurations while drastically reducing cost. Finally, preliminary evaluations demonstrate DRB's potential to generalize to cross-model selection.

---


### 88. [Infrared Universality of Collective Dynamics across Transformer and State-Space Architectures](https://arxiv.org/abs/2608.18592)

**<font color=#1a73e8>作者：</font>** Byung Gyu Chae  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Whether distinct neural architectures develop common collective dynamics remains an open question. Recent analysis of Transformer language models revealed a nearly flat, weakly infrared-enhanced time-scale density of states (TDOS) associated with near-marginal long-memory dynamics. Here we test whether a closely related organization emerges in Mamba, whose selective state-space dynamics provides a fundamentally different microscopic mechanism. Mamba allows relaxation dynamics to be resolved at three levels: the intrinsic spectrum of the learned state-space generator, its input-conditioned selective rescaling, and the collective TDOS of the complete block measured from its Jacobian. These spectra are not identical: selective dynamics and the remaining block transformations substantially reorganize the microscopic relaxation hierarchy. Nevertheless, the full block develops a reproducible slow-mode continuum whose infrared sector becomes progressively better resolved with increasing sequence length. Cumulative analysis yields $\rho(\lambda)\sim\lambda^\beta$, with the long-sequence Mamba exponent stabilizing near $\beta_{\rm M}\simeq-0.17$. The corresponding memory dynamics follows $K(t)\sim t^{-(1+\beta)}$, close to the marginal $1/t$ regime. Despite fundamentally different microscopic dynamics, Transformer full-block spectra exhibit closely related infrared organization, with representative exponents of order $\beta_{\rm Tr}\sim-0.1$. These results separate explicit state-space memory from collective infrared organization and show that distinct sequence architectures can develop closely related near-marginal slow-mode dynamics. They extend infrared collective organization beyond Transformers and provide an independent test of the dynamical structure described by Cognitive Field Theory.

---


### 89. [Off-Manifold Collapse in Guided Protein Language Models](https://arxiv.org/abs/2608.18597)

**<font color=#1a73e8>作者：</font>** Shuibai Zhang, Xinchi Liu, Fred Zhangzhi Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein language models are widely used priors for protein sequence design, and a growing body of work controls them at inference time as an alternative to fine-tuning. Such guidance faces a dilemma: mild enough to preserve natural activation statistics, it barely moves the property; strong enough to move it, the generations become progressively harder to fold. We show the failure has a specific and cheaply detectable signature, an off-manifold collapse of the model's own representations. Guided activations fall toward a region statistically indistinguishable from random amino-acid input, and the sequences degenerate to low complexity, yet the property oracle being optimized can still score these generations as a success. The optimized oracle can therefore fail to witness the collapse and, for solubility, can actively reward it, whereas structure and composition expose the failure. Because the failure is already visible in a finished candidate, we detect it at the output rather than modify the generator. We introduce a cheap density prior over natural protein activations and keep only the candidates that remain typical under it, a training-free post-hoc step we call Mahalanobis filtering. At matched guidance settings it improves both the property score and the structural plausibility of the sequences it keeps at negligible cost, without touching the generator, and transfers across different guidance methods. We release the activation statistic at this https URL

---


### 90. [Teach a Molmo2Fish: Towards interactive fish tracking with natural language guidance](https://arxiv.org/abs/2608.18602)

**<font color=#1a73e8>作者：</font>** Kai Van Brunt, Justin Kay, Sara Beery  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer vision is increasingly used to automate recognition tasks in large ecological datasets, but more complex tasks such as multi-object tracking continue to pose challenges. As researchers seek to incorporate vision models in ecology workflows, various lines of research have explored how to make imperfect predictions useful through human-in-the-loop processes. We propose a new approach to working with imperfect tracking predictions through an interactive prediction correction workflow taking place as a conversation with a multimodal large language model, which we tailor to a sonar fish tracking dataset as an initial proof of concept. We investigate the performance of the tool, Molmo2Fish, across guided and unguided tasks, correcting its own predicted tracks and external tracks. We find that Molmo2Fish achieves high performance on fish tracking and track correction tasks, but there is still much room to improve on incorporating natural language guidance. The code and data are publicly available at this https URL.

---


### 91. [CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence](https://arxiv.org/abs/2608.18613)

**<font color=#1a73e8>作者：</font>** Yutong Cheng, Changze Li, Qian Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cyber threat intelligence (CTI) is increasingly consumed not by human analysts but by LLM agents that compose multi-step investigations at query time. The harness side of this shift has matured rapidly (planning loops, tool protocols, context management), but the corpus side has not: threat reports and vulnerability databases are still packaged for retrieval-augmented generation, as opaque chunks behind an embedding index. We argue that this substrate, not model capability, is the bottleneck on agentic CTI investigation, and present CTIFoundry, an agent-native corpus scaffold. At build time, CTIFoundry materializes the latent structure of a CTI corpus: a deterministic ontology graph over four authoritative knowledge bases (CVE, CWE, CAPEC, ATT&CK) whose official cross-references become typed, traversable edges; a span-grounded report layer whose canonical, alias-resolved cross-vendor entities index provenance-carrying chunks; and hybrid dense+lexical retrieval surfaces. At query time this structure is exposed through seven typed tools and three procedural skills mounted on a stock open-source agent harness. On the public CTIConnect benchmark, swapping only the action surface lifts the identically-harnessed agent by +0.19 to +0.28 overall F1 across a four-model, two-provider panel: a small model on CTIFoundry surpasses a flagship on the flat substrate, and the gain is not bought with search effort, since on both Claude models the scaffolded agent is more accurate at roughly half the tool calls. An ablation attributes it: typed structure carries the larger share, procedural skills convert structure into discipline, and the two compose super-additively, because skills bind only to structure that exists.

---


### 92. [PCQA-R1: Advancing Generalized 3D Point Cloud Quality Assessment with Reinforcement Learning](https://arxiv.org/abs/2608.18627)

**<font color=#1a73e8>作者：</font>** Kangning Ye, Yunhao Li, Sijing Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> No-reference point cloud quality assessment (PCQA) has been an active topic in recent years and is used to measure and optimize the visual experience of point clouds. However, large multimodal models (LMMs) have rarely been explored in this area. Previous LMM-based methods mainly rely on supervised fine-tuning to directly predict numerical quality scores, lacking the ability to generalize across datasets with heterogeneous MOS scales and limited annotations. A key difficulty is that absolute MOS regression can be brittle across datasets with different score scales and distortion distributions, whereas relative quality ranking is more stable under such shifts. In this paper, we present PCQA-R1, the first reinforcement learning LMM for 3D point cloud quality assessment to simultaneously model quality understanding and scoring. Built upon the group relative policy optimization (GRPO) strategy, PCQA-R1 first constructs a chain-of-thought dataset, PCQA-CoT, which serves as cold-start training data through a reverse reasoning strategy that teaches the LMM to generate its reasoning process. We further introduce a Gaussian proximity reward that prevents calibration drift by anchoring score predictions to the source MOS range. Experimental results demonstrate that PCQA-R1 achieves state-of-the-art cross-dataset generalization across five benchmarks and competitive in-domain accuracy. Ablation studies support the role of ranking, Gaussian reward, and cold-start traces.

---


### 93. [Preference Reasoning under Indeterminacy in Large Language Models](https://arxiv.org/abs/2608.18631)

**<font color=#1a73e8>作者：</font>** Hadi Hosseini, Samarth Khanna, Xiyuan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models evolve into decision-making agents, the ability to reason over preferences becomes fundamental to alignment, coordination, and collective intelligence. Yet, unlike standard benchmarks, real-world preference reasoning is inherently indeterminate: information may be incomplete, and valid solutions may not exist. We argue that indeterminacy, rather than correctness alone, is a central challenge for AI reasoning. We formalize this challenge along two axes, (i) epistemic indeterminacy, arising from incomplete, partial, or expressive preferences, and (ii) structural indeterminacy, arising from the non-existence of solutions under standard social choice concepts. Across a hierarchy of tasks, we show that state-of-the-art language models systematically fail to distinguish between determined and undetermined instances, exhibiting miscalibrated reasoning even in verification settings.

---


### 94. [TranslatePsy-AfriSLM: High-Quality Data Scaling For Low-Resource Machine Translation](https://arxiv.org/abs/2608.18655)

**<font color=#1a73e8>作者：</font>** Milan Gritta, Patrik Lambert, Jihye Back 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid progress in Artificial Intelligence has largely bypassed African languages, creating a digital divide that limits AI adoption on the continent. Recent open-source LLMs systematically underperform on African machine translation, while the lack of large-scale, high-quality, open-source parallel data has constrained the development of competitive small language models (SLMs). We introduce *TranslatePsy-AfriSLM*, a collection of open-source MT resources for 19 Sub-Saharan African languages, including curated parallel data, African-specialized synthetic data, and a family of fine-tuned SLMs. Our empirical study shows that unified quality-estimation filtering removes up to 96% of training tokens without degrading quality, and that filtered synthetic data dominates the quality-efficiency Pareto frontier. Fine-tuned on the resulting data mixture, TranslatePsy-AfriSLM outperforms substantially larger systems, including TranslateGemma-27B and Qwen3.5-122B-A10B, with as few as 0.8B parameters.

---


### 95. [FlashAttention for Scalable Vector Architectures](https://arxiv.org/abs/2608.18656)

**<font color=#1a73e8>作者：</font>** Sonia Rani Gupta, Nikela Papadopoulou, Miquel Pericàs  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference with transformer models on CPUs is increasingly important, especially for Small Language Models (SLMs), where vector architectures are emerging as a promising execution substrate. The attention module is a major bottleneck due to high memory bandwidth requirements; FlashAttention mitigates this by fusing operations to improve data locality and reduce intermediate memory traffic. In this paper, we present FlashAttention-V, a blocked FlashAttention for scalable vector architectures that adapts efficiently from short to very long vectors by exploiting parallelism across attention heads, inter-head packing to enable efficient utilization of vector lengths beyond the head dimension, and improving vector register utilization and memory access locality. We integrate FlashAttention-V into ggml within this http URL and evaluate it on TinyLlama, Llama 3.2, Qwen2.5, and Pythia-410M using gem5 and a Banana Pi BPI-F3. On the Banana Pi BPI-F3, we confirm that loop reordering and loop unrolling across attention heads are effective optimization principles, scaling performance gains with larger models and most pronounced with short contexts and during decoding. Simulation-based analysis shows that FlashAttention-V achieves 22x-42x speedup over scalar FlashAttention at 512-bit VL in prefill, with an additional 2x-2.5x gain scaling to 64 lanes and 4096-bit VL. During decode, FlashAttention-V achieves 8x-11x speedup using 512-bit vector lengths over scalar FlashAttention, with performance showing diminishing sensitivity to vector width and lane count due to single-token, memory-bound execution. We further identify structural bottlenecks in Q8_0 quantized linear layers that limit arithmetic amortization under long-vector execution, consistent across RVV and Arm SVE, indicating that current quantization formats pose a fundamental challenge to long-vector scalability.

---


### 96. [Computational Measurement of Team-Process Phase Dynamics in Collaborative Virtual Reality](https://arxiv.org/abs/2608.18660)

**<font color=#1a73e8>作者：</font>** Qing Huang, Jianing Zhang, Pooja Pol  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collaborative virtual reality (VR) environments make team communication observable as it unfolds, but conventional transcript analyses often summarize entire trials or divide them into fixed temporal windows. Such approaches can obscure changes in team communication and coordination over time. This article presents a computational framework for detecting and interpreting dynamic team-process phases from timestamped dialogue in a collaborative VR game. The framework uses late chunking to generate context-aware transcript representations, aggregates them into temporal chunks, and applies penalized Gaussian-kernel change-point detection to identify semantic transitions in team communication. After boundary detection, term frequency--inverse document frequency (TF-IDF), non-negative matrix factorization (NMF), and representative transcript segments provide structured evidence for phase interpretation. A locally deployed large language model (LLM) uses in-context learning to generate initial interpretations that are subsequently reviewed by humans. Independently recorded interaction logs are then aligned with the detected phases to examine corresponding task-action patterns. The evaluation compares representations, pooling strategies, segmentation methods, parameter settings, reviewed phase interpretations, and phase-aligned interaction profiles. The results show that the framework identifies coherent and interpretable phase structures while preserving traceability to the underlying transcript evidence. The correspondence between transcript-derived phases and interaction behavior further supports their relevance for analyzing collaborative activity. The framework therefore offers a transparent and transferable approach for studying temporal changes in teamwork from timestamped transcripts across collaborative task settings.

---


### 97. [Vision-Language Models for Egocentric Video: From Hand-Object Interaction to Embodied AI](https://arxiv.org/abs/2608.18671)

**<font color=#1a73e8>作者：</font>** Mohammad Zamani, Fatemeh Ziaeetabar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric video captures activities from the wearer's perspective, providing a direct view of human attention, hand--object interaction, and goal-directed behavior. This perspective is increasingly important for wearable intelligence, assistive systems, human--robot interaction, and embodied AI, yet it introduces challenges including ego-motion, occlusion, small active objects, viewpoint-dependent appearance, and long-range temporal dependencies. Vision--language models (VLMs) offer a promising foundation for addressing these challenges by linking visual observations with semantic knowledge and natural-language supervision. This survey presents a critical review of VLMs for egocentric video understanding, tracing the progression from conventional recognition architectures to multimodal foundation models and embodied systems. We organize the literature around tasks, datasets, hand--object interaction understanding, temporal reasoning, frame and clip selection, multimodal representation learning, prompting, semantic alignment, and model adaptation. Particular attention is given to graph-based and object-centric reasoning as mechanisms for modeling relations among hands, objects, actions, and scene context over time. We further examine how first-person perception and multimodal foundation models support wearable assistance, robot skill learning, human-to-robot transfer, and embodied decision making. Across the reviewed literature, a consistent limitation emerges: current models recognize visible objects more reliably than evolving interactions, actions, and user intent, especially over long activities. We therefore identify temporally grounded reasoning, interaction-aware supervision, efficient long-video processing, multimodal fusion, graph-enhanced representations, cross-domain generalization, privacy, and trustworthy evaluation as key priorities for deployable embodied intelligence.

---


### 98. [Sanyu Studio: A Multi-Agent System for Art-Historical Narrative Construction](https://arxiv.org/abs/2608.18677)

**<font color=#1a73e8>作者：</font>** Zhaoxi Wei, Hongye Yang, Shuyuan Tian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Amid concerns that generative AI may standardize art interpretation, this paper examines whether LLM-based interaction can support plural art-historical narrative construction. We present Sanyu Studio, a multi-agent dialogue system that models 321 Sanyu oil paintings as agents with fact, interpretation, organization, and memory-filtering mechanisms. Based on a seven-day workshop with eight art-university participants, the study shows that user prompts, evidence organization, and cognitive tendencies shaped divergent yet coherent versions of digital Sanyu. The findings suggest that, under conditions of limited historical evidence, AI can amplify human agency and offer public audiences an interactive entry point into art-historical interpretation.

---


### 99. [Learning What to Fail On: Failure-Mode Contextual Bandits for Adversarial Data Curation](https://arxiv.org/abs/2608.18681)

**<font color=#1a73e8>作者：</font>** Roie Kazoom, Ofir Cohen, Rami Puzis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce a failure-aware adversarial retrieval-augmented framework for improving robustness in natural language understanding. Rather than selecting synthetic examples with a fixed reward threshold, our method formulates adversarial data curation as a failure-mode contextual bandit problem. Candidate examples are generated with retrieval-augmented prompting, filtered by the current target model, automatically validated by an LLM judge ensemble, and clustered into recurring failure modes. A stochastic policy then selects which failure modes to sample for retraining, and is updated using validation-based reward that balances robustness gains, forgetting, and data cost. This makes the data curator itself the learning agent, enabling adaptive selection of the most useful model failures across training rounds. On standard benchmarks, our approach improves RoBERTa-base accuracy from 88.48% to 92.60% on SNLI, from 75.04% to 80.95% on ANLI, and from 54.67% to 71.99% on MultiNLI, while consistently outperforming prior adversarial augmentation methods. We further demonstrate transfer to FEVER fact verification, achieving up to 79.86\% FEVER score and 82.45\% accuracy with RoBERTa-large. Finally, we provide a theoretical interpretation showing that, under stated assumptions, failure-mode sampling can reduce shortcut-aligned gradient contributions while inducing bounded distributional drift. By combining retrieval, automated validation, contextual-bandit failure selection, and controlled adversarial retraining, our framework enables scalable robustness improvement without additional human annotation.

---


### 100. [RTPO: Reverse-Turn Policy Optimization for Stabilizing Agentic RL Training](https://arxiv.org/abs/2608.18682)

**<font color=#1a73e8>作者：</font>** Yugu Li, Jimmy Cao, Jianglin Qiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training multi-turn agentic workflows with reinforcement learning (RL) enables large language models to perform complex reasoning, use external tools, and conduct iterative search beyond single-turn settings. Yet multi-turn RL training remains highly unstable, often causing severe performance degradation as the number of turns increases. Through theoretical analysis, we identify three tightly coupled sources of instability: rollout-training context mismatch, weak turn-level credit assignment under sparse terminal rewards, and asynchronous policy drift when short and long trajectories are optimized under different policy versions. We show that these issues share a common structural origin in flattened trajectory optimization and address them through a unified reverse-turn formulation. We propose Reverse-Turn Policy Optimization (RTPO), which organizes multi-turn rollouts as sparse reverse trees and performs turn-level policy updates in temporal reverse order, aligning each decision with its downstream continuation. RTPO enables causally consistent turn-level credit assignment and on-policy continuation to control asynchronous drift. We provide theoretical guarantees showing that RTPO eliminates context mismatch and asynchronous drift under the proposed turn-level formulation, reduces credit bias, and converges to recursive optimality. Experiments on multi-turn agentic RL benchmarks show that RTPO improves upon trajectory- and turn-level baselines by 21.50% and 10.76%, respectively, highlighting its potential to support more stable training for tool-using agents.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-166](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
