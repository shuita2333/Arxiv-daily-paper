# 🧠 大模型相关研究 | 2026年07月17日

> 本类共 **73** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-73](./part-02.md)

---

### 1. [Ask Before You Diagnose: Safe-Psych, a Sequential Evaluation Benchmark for LLMs in Psychiatry](https://arxiv.org/abs/2607.13036)

**<font color=#1a73e8>作者：</font>** Oriana Presacan, Andreea Grama, Larisa Irimină 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for decision support in healthcare, but clinical evidence is often incomplete or evolving. When the available information is insufficient to support a reliable answer, models should request clarification or abstain rather than provide unsupported responses. Existing medical benchmarks, however, typically assume that complete information is available upfront. We introduce Safe-Psych, a sequential benchmark for evaluating how LLMs handle evolving diagnostic uncertainty in clinical psychiatry. Safe-Psych contains over 1,000 real-world psychiatric clinical notes segmented to simulate incremental evidence disclosure, with psychiatrist-derived action labels at each stage: DIAGNOSE, CLARIFY, or ABSTAIN. We evaluate multiple state-of-the-art LLMs in full-information and sequential settings. Our findings show that capability does not ensure calibration: even strong models struggle under incomplete clinical information, with under-abstention exceeding 60% for most models and safety-aware prompting reducing premature commitment only by shifting errors toward excessive abstention. In sequential evaluation, models frequently diagnose before sufficient evidence is available and rarely seek clarification unless explicitly prompted; these premature diagnoses are less accurate than on-time diagnoses. Overall, Safe-Psych reveals a limitation across the evaluated models: recognizing when clinical evidence is incomplete and additional information is needed. We release Safe-Psych to support research on improving LLM safety in healthcare.

---


### 2. [Uncertainty-Aware Sequential Decision Rules for Event-Triggered LLM Invocation in Streaming Systems](https://arxiv.org/abs/2607.13048)

**<font color=#1a73e8>作者：</font>** Zhaohui Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Streaming inference pipelines increasingly pair lightweight fast models with Large Language Models (LLMs) that provide rich semantic understanding at substantial cost. The central question of when to invoke the LLM has received limited formal treatment. We cast this as a risk-based sequential stopping problem, where a trigger policy fires when a risk functional over the observation history exceeds a threshold. Within this framework, we prove six results: a minimum inter-event time bound excluding trigger chattering; optimality of threshold policies via smooth pasting; approximate SPRT guarantees under estimated parameters; O(sqrt(T log T)) regret for stationary streams, extending to O(sqrt((C_T + 1) T log T)) under C_T changepoints; O(1/sqrt(T)) convergence of online gradient descent for adaptive thresholds; and a calibration-to-miss-rate transfer inequality. Several classical trigger families, including event-triggered, optimal stopping, SPRT, CUSUM, and Bayesian triggers, can be expressed as special cases of this framework. On turbofan degradation data (CMAPSS) with real LLM calls, we empirically verify the theoretical assumptions, ablate the risk function design, compare against six baselines including a RouteLLM-style router and contextual bandits, and analyze cost sensitivity and LLM failure modes. The results confirm sublinear regret, with alpha < 1 for all principled triggers; high diagnostic quality, with 92.9 percent of 1600 LLM diagnoses reaching grounding score >= 0.75 under our rubric; and that anomaly-score-driven risk functions dominate alternatives by roughly an order of magnitude on the Pareto AUC.

---


### 3. [SPINE: Bridging the Cyber-Physical Gap with Agentic AI](https://arxiv.org/abs/2607.13049)

**<font color=#1a73e8>作者：</font>** Minkyu Ham, Dongho Kim, Chan Lee 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models have given robots a sophisticated brain for complex decision-making, yet deploying that intelligence into a physical platform still demands tedious, expert-driven calibration. This deployment gap, the robot's spinal cord, remains a primary bottleneck to scalable Embodied AI. Hence, we propose SPINE (Scalable Physical Integration with ageNtic Expertise): an agentic framework for systematically debugging and deploying bimanual robots with minimal robotics expertise. SPINE's harness comprises two orchestrated multi-agent workflows: a profile builder that creates robot-specific context, and a debugger that cycles through diagnosis, repair, and validation until teleoperation works. Across seven DOBOT X-Trainer debugging scenarios, a robotics novice using SPINE outperformed human operators using Claude Code with the same reference materials, but without SPINE's structured workflow, improving operationalization success from 75% to 100% and reducing mean time-to-teleoperation from 16 min 45 s to 13 min 47 s. On AgileX PiPER, a distinct ROS/CAN bimanual arm, SPINE resolved all 10 implanted bugs, versus 9 out of 10 for the expert baseline, in nearly the same amount of time. Together, these results show that SPINE can transfer across bimanual platforms, reduce dependence on expert calibration, and move embodied AI closer to scalable real-world deployment.

---


### 4. [Interventional Grounding Audits: Black-Box Premise-Dependency Tests for LLM Chain-of-Thought via Predicate Substitution](https://arxiv.org/abs/2607.13069)

**<font color=#1a73e8>作者：</font>** Hironao Nakamura  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models produce chain-of-thought (CoT) reasoning that appears logically sound yet may not genuinely depend on its stated premises. We introduce interventional grounding audits, a black-box, step-level test of premise dependency: we intervene on a single premise by substituting its target predicate with a fresh symbol, re-run the model, and check whether each reasoning step's normalized conclusion (canonical predicate form) changes. We evaluate on ProntoQA, a synthetic multi-hop deductive reasoning benchmark with gold proof trees, where step-level premise dependencies are known. Applied to 50 ProntoQA problems with GPT-4o, our method achieves F1 = 0.806 on detecting proof-tree dependencies (F1 = 0.885 on predicate-determining dependencies; Recall = 100%), significantly outperforming a self-consistency baseline (F1 = 0.343; 95% bootstrap CIs non-overlapping). We further identify that 66% of correctly-solved problems contain at least one aligned step insensitive to a direct proof-tree dependency under consistent substitution -- all involving entity-introduction premises, a documented blind spot of the consistent-substitution evaluator -- a "right answer, wrong reasoning" signal invisible to passive methods. All audit certificates, raw outputs, and reproduction scripts are available in a public GitHub repository, and we discuss scope limits beyond formal, parsable benchmarks.

---


### 5. [Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104)

**<font color=#1a73e8>作者：</font>** Zhe Ren, Yimeng Chen, Dandan Guo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improving autonomous agents are moving from research prototypes to deployed systems. The primary goal is controllable evolution, or adaptation, from experience with minimal or even no human input. This survey frames modern self-improving agents as adaptive systems that convert experience into accumulated capability gains. We offer a system-level framework that represents a modern agent as a configuration coupling a foundation model with an operational scaffold of prompts, memory, tools, and control logic. Within this framework, self-improvement is formalized as a self-induced update operator that obtains and commits updates to model parameters or scaffold components. We organize prior work by update target and by the signals that drive change, then review applications and discuss evaluation, before closing with open problems and future directions. For convenience, we track technical updates on this https URL.

---


### 6. [Improving Molecular Property Prediction in Small Language Models Using Graph-based Tools](https://arxiv.org/abs/2607.13115)

**<font color=#1a73e8>作者：</font>** Konstantinos Bougiatiotis, Dimitrios Kelesis, Georgios Paliouras  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small language models (SLMs) have shown promise for zero-shot molecular property prediction from SMILES strings, yet they often suffer from structural blindness because sequence representations under-specify key graph-topological cues. We propose a modular Context-Augmented Prompting framework that enables agentic tool use at inference time: a trained GNN expert model provides a predictive hint with confidence, and a GNN extracts an instance-specific explanatory subgraph (e.g., a subgraph SMILES and an accompanying explanatory paragraph). We evaluate three commonly used SLMs on MUTAG and Tox21 under five prompting configurations ranging from SMILES-only to using all available tools at hand. Across two datasets, enriching prompts with graph-derived context yields substantial accuracy gains, often exceeding 25% relative improvement and up to 74% on Tox21. We further validate the functional relevance of the extracted motifs via a necessity-based edge-drop intervention. Despite the observed gains, a persistent gap remains to specialized GNN models, highlighting both the value and limits of text-conditioned reasoning for molecular structure.

---


### 7. [ShortOPD: Recovering Pruned LLMs with Short-to-Long On-Policy Distillation](https://arxiv.org/abs/2607.13124)

**<font color=#1a73e8>作者：</font>** Qingyu Zhang, Qianhao Yuan, Hongyu Lin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured pruning is a hardware-friendly way to compress LLMs, but it is mostly validated on multiple-choice recognition tasks, while the same compressed checkpoints can collapse on the free-form generation that deployment actually requires. Two observations trace this gap. First, greedy \textsc{pass}@$1$ nearly vanishes after compression, yet \textsc{pass}@$k$ recovers substantially under repeated sampling: useful generations are demoted, not erased. Second, the recoverable regime fails mainly through suffix repetition. Recovery should therefore train on the compressed model's own on-policy states with dense token-level supervision, which On-Policy Distillation (OPD) provides by reusing the pre-compression model as a frozen teacher. However, long on-policy rollouts spend early recovery budget on low-information repetitive suffixes, delaying loss descent. To mitigate this waste, we propose \textbf{\shortopd}, a short-to-long OPD schedule that detects teacher-confirmed repetitive suffixes, treats the surviving prefix as each rollout's effective length, and allocates future rollout budgets to the effective lengths the policy can currently use. Across math, code, and open-ended generation, \shortopd\ raises the compressed model's score to about $9\times$ its unrecovered value and $1.6$--$4.4\times$ standard recovery recipes (SFT w/o KD, KD, and SeqKD), and it matches a fixed $8192$-token rollout horizon within two points using a quarter of the training time ($8.5$ vs.\ $35.9$ hours) and $71\%$ fewer rollout tokens. We hope this recipe helps move structured pruning beyond marginal gains on perplexity and multiple-choice benchmarks, a step closer to deployment-ready generation quality.

---


### 8. [Boogu-Image-0.1: Boosting Open-Source Unified Multimodal Understanding and Generation](https://arxiv.org/abs/2607.13125)

**<font color=#1a73e8>作者：</font>** Guoxuan Chen, Chufeng Xiao, Haoran Yang 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Boogu-Image-0.1, an open-source unified multimodal understanding and generation model family, comprising Base, Turbo, Edit, and Edit-Turbo variants. It delivers competitive performance in high-quality text-to-image generation, fast inference, instruction-based editing, and bilingual (Chinese-English) text rendering. Closed-source multimodal systems like Nano-Banana-Pro and GPT-Image-2 achieve strong performance through system-level integration rather than a single model, yet their internal practices remain largely undisclosed. In this work, we demonstrate that targeted improvements in model understanding, data quality, and training pipelines, coupled with agentic inference-time scaling, can substantially enhance generation and editing performance even under highly constrained compute budgets. Comprehensive evaluations show that Boogu-Image-0.1 consistently matches or surpasses other open-source models across standard benchmarks, and achieves results approaching leading closed-source systems. Notably, this is accomplished with only 208.62 million unique images. The base model's theoretical training cost is only approximately \$400K. We share practical discussions that we believe are valuable to the broader research community, and release weights, code, and recipes under Apache 2.0 to advance the open ecosystem for unified multimodal understanding and generation. Our code is available here: this https URL.

---


### 9. [Do LLMs Need Architectural Changes for Simultaneous Speech Translation? A Prefix-to-Prefix Data Driven Approach](https://arxiv.org/abs/2607.13158)

**<font color=#1a73e8>作者：</font>** Junkun Chen, Jian Xue, Ming Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Simultaneous speech translation (SimulST) requires incremental translation under strict latency constraints, yet remains challenging for decoder-only LLM systems due to limited context and cross-lingual reordering. Recent approaches often introduce architectural changes or explicit read/write policies to control output timing, which can be brittle in conversational speech where segmentation boundaries are ambiguous. We present a simple data-driven alternative: fixed-length chunks for cumulative streaming decoding with a rewind-based committed prefix, and teacher-labeled prefix-to-prefix (P2P) targets with bounded waiting for fine-tuning, yielding CSSEL-P2P, where CSSEL is our proposed chunked streaming speech encoder LLM. In our in-house conversational speech evaluation, CSSEL-P2P improves streaming quality by +1.54 COMETKiwi over the CSSEL streaming baseline at comparable latency (+0.15s Average Lagging), suggesting effective SimulST without architectural changes via P2P supervision.

---


### 10. [What Models Express, Suppress, and Resist: Auditing Open-Weight LLMs with Persona Vectors](https://arxiv.org/abs/2607.13162)

**<font color=#1a73e8>作者：</font>** Winston Zeng, Ali Emami, Jinho Choi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> What a language model will and will not do is largely set during post-training, but which behaviors it expresses, hides, or resists is not revealed by prompting alone. Persona vectors, behavioral directions in activation space, can probe this organization, but prior work covers only a handful of traits. We present the first systematic application of persona vectors at this scale, compiling a 53-trait inventory across four behaviorally distinct domains and labeling every trait in two open-weight models as natural (expressed at baseline), steerable latent but amplifiable, or intractable (resistant to standard extraction). Both models default to helpful, task-oriented behavior: all nine agentic traits are natural, and their default clinician behavior matches a board-certified psychologist's independent desirability judgments on 16 of 17 traits. Steering produces its largest gains on traits these defaults exclude: hyperbole, hallucination, and sycophancy. The same asymmetry holds across all 171 generic-trait pairs: two steerable traits can collapse the composition, but pairs involving a default never do. Where standard extraction fails on a trait like "evil," a vector transferred from a fine-tuned variant still recovers it, with the residual refusals appearing inside the model's chain-of-thought. Persona vectors are most informative not as a set of controls but as a probe of behavioral organization.

---


### 11. [Learning Safe Agent Behaviour from Human Preferences and Justifications via World Models](https://arxiv.org/abs/2607.13172)

**<font color=#1a73e8>作者：</font>** Ilias Kazantzidis, Timothy J. Norman, Yali Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We address the problem of safely training an agent policy and deploying a good and safe policy, in settings where the environment dynamics are unknown and no suitable reward function is available. In the context of safety-critical environments, we consider traditional reinforcement learning impractical and resort to the resource of human input. We introduce DROPJ, a human-centred method for both safe training and deployment. We first learn a world model (a learned simulator) from a dataset of prior real-world trajectories. A human then plays the game in this learned simulator to extract several informative simulated trajectories. From these, we sample pairs of simulated trajectory segments and elicit from a human their preference over these segments, as well as a reason (justification) for their choice. We then train a reward model from these justified preferences and use it, together with the world model, to directly deploy the agent using model predictive control. Running real-user experiments, we find that generating informative simulated trajectories from a user significantly reduces the computational cost during training compared to other strategies, and can also improve the performance during deployment. In the context of training within a learned simulator, we show that the use of preferences rather than other types of feedback substantially improves the performance during deployment. We further demonstrate that safety justifications accompanying preferences can significantly enhance safety or prioritise user-prescribed aspects of safety associated with them during deployment.

---


### 12. [RAGthoven at SemEval-2026 Task 1: A Multi-Stage Pipeline Walks Into a Benchmark and Barely Clears the Bar](https://arxiv.org/abs/2607.13189)

**<font color=#1a73e8>作者：</font>** Marek Šuppa, Viktória Ondrejová, Lucia Ganajová 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present RAGthoven, our system for SemEval-2026 Task 1 (MWAHAHA), Subtask A (multilingual constrained humor generation in English, Spanish, and Chinese). RAGthoven decomposes creative text generation into a multi-stage large language model (LLM) pipeline (Planner, Best-of-N Writer, Reflector for self-critique, LLM-as-a-judge Judge) grounded in computational humor theory (Benign Violation Theory, Script-based Semantic Theory of Humor) and refined across ten experiments.
In our final configuration, we augment the Planner with retrieval-augmented generation (RAG) from a curated joke corpus, seeding generation with diverse joke mechanisms. We also evaluate two agentic variants -- ReAct-style sequential tool-calling (Exp09) and autonomous multi-branch orchestration (Exp10) -- that expose the same four stages with a deterministic ConstraintAudit checker. Across four frontier models on a held-out 12-instance English sample, neither agentic variant produced outputs we judged superior to the non-agentic pipeline despite substantially higher tool-call budgets.
RAGthoven shares Rank 1 with the Gemini 2.5 Flash baseline in all three languages, with overlapping organizer-reported confidence intervals. In Spanish, it leads the baseline by 42 raw Elo points (1182 vs. 1140), while in English (1045 vs. 1081) and Chinese (1045 vs. 1053) the baseline holds the higher raw rating within the same statistical tie.
Together, these results suggest language-dependent diminishing returns from elaborate multi-stage prompt engineering and agentic scaffolding once a strong frontier model is in the loop.

---


### 13. [Adaptive Filtering of the KV Cache: Diagnosing and Correcting Structural-Role Bias in LLM Inference](https://arxiv.org/abs/2607.13205)

**<font color=#1a73e8>作者：</font>** Soumil Mandal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Attention-based KV cache eviction (H2O and its descendants) compresses the memory-constrained state of a long-context model by ranking tokens on accumulated attention mass, treated here as signal energy, and keeping the heaviest. On schema-dense input streams such as nested JSON, this score acts as a non-stationary filter that disproportionately retains noise: a non-content sink role (delimiters or whitespace) carries an order of magnitude more energy than any content role, and structural KEY tokens are over-retained at roughly 1.8x the rate of the answer-carrying VALUE tokens, collapsing exact-match accuracy from 88% to 0% at a 5% budget as the signal-to-noise ratio of the retained state degrades. A counterfactual experiment establishes that suppressing KEY tokens is the best deployable filter. Our retraining-free, role-conditional allocation over SnapKV's windowed score, governed by a single tuned hyperparameter, closes 63-98% of the H2O gap at sub-20% budgets and, at higher budgets, modestly matches or exceeds full-cache accuracy -- a small, seed-sensitive denoising effect (borderline significant at B=0.50; not distinguishable from zero at B=0.30 over four seeds). A 15 MB linear role probe supplies these labels at negligible inference cost, though matching parser-level downstream accuracy remains open.

---


### 14. [AI-Native Insurance for Agentic AI: Pricing, Underwriting, and End-to-End Automation](https://arxiv.org/abs/2607.13230)

**<font color=#1a73e8>作者：</font>** Quanyan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI introduces new insurance challenges because autonomous AI systems can make decisions, invoke tools, modify external environments, and interact with third-party services. This paper develops an AI-native mathematical framework for underwriting, pricing, and contract design for agentic AI deployments. A deployment is represented by a risk state that captures autonomy level, operational authority, permission exposure, governance maturity, and dependency concentration. The framework maps the risk state to event probabilities, loss severities, governance costs, premiums, deductibles, coverage allocation, and policy covenants, and formulates an optimization problem for insurance contract design under participation, profitability, and incentive compatibility constraints. The paper establishes structural properties of insurability, including characterization of an insurability region, monotone deterioration of feasibility with increasing exposure, and governance certification thresholds. Insurance is further interpreted as both an operational cost and a regulatory mechanism for AI deployment. A healthcare case study illustrates contract optimization, sensitivity analysis, and automated claims processing for agentic AI systems.

---


### 15. [Cost-Optimal Foundation Model Deployment Portfolio for Transportation Management](https://arxiv.org/abs/2607.13239)

**<font color=#1a73e8>作者：</font>** Xi Cheng, Ke Liu, Siyuan Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models, including large language models (LLMs) and vision-language models (VLMs), are increasingly used for transportation management center (TMC) tasks such as anomaly detection, incident reporting, and traveler information. Deploying multiple such models across TMC functions raises a portfolio question: which model should serve each function, in which deployment mode, and under what shared hardware budget? We formulate this as the Foundation Model Deployment Portfolio (FMDP) problem, a mixed-integer program minimizing total cost of ownership (TCO) subject to per-function quality, latency, and safety constraints over shared GPU capacity. We prove the problem NP-hard by reduction from the 0-1 knapsack problem and propose a polynomial-time greedy heuristic. In an illustrative case study with five TMC functions and 19 candidate (model, mode) pairs, FMDP identifies a mixed portfolio costing $34/mo (97% below the cheapest feasible all-closed-API baseline) by routing four functions to open-source APIs and the one function whose quality floor no open-source model meets to a closed API. Break-even analysis shows that on-premise GPU investment becomes reasonable only above approximately 309 vision queries/hour or if API prices double.

---


### 16. [Just-In-Time Scene Graph Growth: Combating Perceptual Saturation in Long-Horizon Robotics](https://arxiv.org/abs/2607.13245)

**<font color=#1a73e8>作者：</font>** Yue Chang, Rufeng Chen, Yifan Tian 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 3D Scene Graphs (3DSGs) provide crucial structured representations for embodied agents, conventional Ahead-of-Time, build-everything-then-filter pipelines conflict with the real-time, low-latency demands of edge platforms, inducing a perceptual saturation effect via severe observation redundancy. To resolve this, we present JITOMA (Just-In-Time On-demand Memory Activation), a closed-loop framework that unifies task reasoning, perception, and memory into a just-in-time growth process. Instead of exhaustively mapping the entire environment, JITOMA leverages a top-down task heatmap at the frontend to filter continuous observations, routing minimal streams to maintain a global foundation of low-cost, dormant anchors. Upon a cognitive query, the backend Large Language Model (LLM) parses the robotic intent to dynamically awaken task-relevant anchors, triggering resource-intensive operations -- such as dense node captioning and functional inference -- exclusively within the activated local subgraph. To evaluate these dynamic capabilities and study perceptual saturation trade-offs, we introduce JITOMA-Bench, a comprehensive suite for long-horizon multi-tasking and complex multi-step reasoning. Extensive experiments demonstrate that JITOMA substantially reduces active graph size and captioning latency, while maintaining stable processing time under long-horizon task switching.

---


### 17. [GSM-Plus-BN: A Perturbation-Based Benchmark for Bangla Mathematical Reasoning in Large Language Models](https://arxiv.org/abs/2607.13248)

**<font color=#1a73e8>作者：</font>** Bidyarthi Paul, Nahida Jannat Mayouree, Md. Asif Karim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The evaluation of mathematical reasoning in large language models (LLMs) has predominantly focused on high-resource languages like English. This has created a significant barrier to the equitable development and deployment of AI in linguistically diverse regions such as Bangladesh, where over 230 million people speak Bengali. Despite this global significance, there has been minimal prior work on mathematical reasoning in Bengali and no existing research that systematically benchmarks a perturbated Bengali mathematical dataset, leaving a critical void in assessing model robustness and true comprehension beyond pattern recognition. This study addresses this gap by introducing GSM-Plus-BN, a novel perturbated Bengali mathematical dataset derived from the English GSM-Plus benchmark and verified by human translators. We evaluate six open-source LLMs Qwen3-32B, Llama-3.1-8B-Instant, Llama-3.3-70B-Versatile, Llama-4-Scout-17B-16E-Instruct, GPT-OSS-120B, and GPT-OSS-20B using a benchmark of 9,000 evaluation samples comprising 1,000 seed questions and 8,000 perturbed variants under both Standard Prompting and Chain-of-Thought (CoT) Prompting. Experimental results show that GPT-OSS-20B achieves the highest seed question accuracy of 96.08% under Standard Prompting, while larger models such as Llama-3.3-70B and GPT-OSS-120B demonstrate superior robustness across perturbation types. Furthermore, CoT prompting substantially improves reasoning for most models compared to Standard Prompting, yet a notable performance gap persists across all models relative to their English benchmarks, underscoring the inherent difficulty of perturbed Bengali text. This research makes a foundational contribution by providing GSM-PLUS-BN as a new resource and baseline for future Bengali mathematical reasoning research.

---


### 18. [Discourse-Aware Policy Analysis with Argumentation: A Hybrid LLM-Symbolic Framework for Disaster Governance](https://arxiv.org/abs/2607.13260)

**<font color=#1a73e8>作者：</font>** Stylianos Loukas Vasileiou, Olga Derendiaeva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Policy documents shape governance outcomes, but their reasoning is often implicit. Participatory commitments and managerial control routinely coexist in the same text, and the tensions between them are rarely stated directly. Existing computational approaches to policy discourse cannot express the frame-mediated relations that drive these tensions, where one argument narrows or instrumentalizes another rather than rejecting it. End-to-end summarization by large language models produces fluent text but offers little structure that domain experts can inspect or contest. We present Apaf, a hybrid LLM--symbolic pipeline that operationalizes critical discourse analysis as a quantitative bipolar argumentation framework over policy text. Arguments are first classified into deliberative or managerial frames. Four frame-mediated relation subtypes (agency reduction, agenda shift, instrumental support, and normative support) are then produced by deterministic rules over LLM-extracted features. We release a novel dataset of 100 sub-documents of disaster-risk-reduction policy from the USA, UK, Canada, and Australia, and show that the resulting argument graphs are accurate, interpretable, and stable across jurisdictions.

---


### 19. [Accuracy Without Grounding: Diagnosing Visual Dependency Dissociation in Video LLM Benchmarks](https://arxiv.org/abs/2607.13305)

**<font color=#1a73e8>作者：</font>** Jae Joong Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Benchmark accuracy in video large language models (LLMs) is often treated as evidence of visual understanding. We audit this assumption across twenty models spanning 2-78B parameters and ten architecture families. We introduce the Visual Dependency Gap (VDG), the difference in per-question correctness between original-video and black-screen conditions. Paired McNemar tests on MVBench show that accuracy and visual dependency are separable: models differ on original video (p = 0.0003) but not on black screens (p = 0.53). Across models, task-type rankings are stable: Attribute Perception is strongly visual, whereas Temporal Reasoning approaches the language-only baseline. A diagnostic ladder from black screen to single frame, shuffled frames, and original video reveals that frame diversity supplies most of the visual benefit, while temporal order contributes near-zero accuracy across sixteen open-weight models. An ablation from 0.5 to 24 FPS rules out sparse sampling as the cause. H.264 experiments further show that stable aggregate accuracy conceals bidirectional question-level answer flips. The diagnostic also generalizes to four API-accessed models, whose VDG values range from 0.025 to 0.315. These results motivate VDG as a standard audit for whether video benchmarks measure visually grounded capability. Code is available at this https URL.

---


### 20. [Tabular Foundation Models for Discrete Choice Estimation](https://arxiv.org/abs/2607.13314)

**<font color=#1a73e8>作者：</font>** Liu Liu, Dan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) generate predictions on structured data via in-context learning, without task-specific estimation. We ask whether TFMs can be effectively applied to discrete choice, a central demand estimation framework in marketing and operations, and find that directly applying TFMs yields limited performance. The gap is structural: TFMs assume row-independent observations, whereas discrete choice is inherently set-valued and subject to persistent consumer preference heterogeneity. We propose a reformulation that encodes both choice-set dependence and individual heterogeneity within a row-based learning framework. Evaluated on a yogurt scanner panel, individual-level heterogeneity encoding is the dominant driver of predictive accuracy. The best reformulation outperforms hierarchical Bayesian estimation by 8\% in holdout log-likelihood and 3.6\% in hit rate, running 16 times faster, a practical advantage for large-scale demand estimation. The advantage is largest in the medium-data regime (10--40 purchase occasions per consumer), where parametric Bayesian shrinkage most distorts estimates for atypical consumers. Fine-tuning on population choice data provides additional gains for consumers with shallow purchase histories, where in-context learning has limited individual-specific signal to condition on. These results establish a principled approach for applying foundation models to consumer choice problems more broadly.

---


### 21. [Meta-Learning Preferences for Multilingual LLM Alignment](https://arxiv.org/abs/2607.13315)

**<font color=#1a73e8>作者：</font>** Jiaying Lin, Seongho Son, Nam Phuong Tran 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unequal availability of human preference data across languages poses a significant challenge for aligning large language models in multilingual settings. To address the lack of sufficient data in low-resource language alignment, we propose a meta-learning framework for Reinforcement Learning from Human Feedback and Direct Preference Optimization. By leveraging preference data from other languages, our framework learns a transferable initialization that enables effective adaptation to a target language with minimal data. We provide theoretical guarantees for both the meta-reward modeling and meta-policy optimization settings, and empirically demonstrate the effectiveness of our approach on multilingual benchmarks. In an extremely low-resource setting with only 100 target-language preference samples, our approach achieves up to $28\%$ win-rate improvements over baseline methods, and consistently outperforms baselines across multiple target languages and model scales. Our approaches retain these advantages across different combinations of meta-training languages and varying linguistic distances from the target languages.

---


### 22. [SARFA: Segment Anything with Radiomic Feature Alignment](https://arxiv.org/abs/2607.13323)

**<font color=#1a73e8>作者：</font>** Tyler Ward, Abdullah Imran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Segment Anything Model (SAM) has demonstrated strong generalizability across a variety of segmentation tasks. However, SAM often struggles in situations where the target to be segmented is ambiguous. This poses a problem in medical imaging, where accurate delineation of targets such as tumors is vital, but even expert radiologists can disagree on the appropriate boundary for a target. Addressing this, we propose SARFA (Segment Anything with Radiomic Feature Alignment), a novel framework for improved medical image segmentation. Via probabilistic prompting, SARFA generates a diverse set of plausible masks for each input image and optimizes them with a radiomics-driven training objective based on Fréchet Radiomic Distance (FRD) and Direct Preference Optimization (DPO). By minimizing the FRD between masked predicted and ground truth regions within each image, SARFA encourages segmentation outputs whose anatomical and textural characteristics align with clinically meaningful ground truth representations, without relying solely on pixel-level overlap. Evaluated on computed tomography (CT) and magnetic resonance imaging (MRI) benchmarks, SARFA outperforms existing ambiguous segmentation methods, demonstrating the effectiveness of radiomic feature alignment and DPO-style candidate mask ranking as a training objective. Our code is available at this https URL.

---


### 23. [Agora: Collective and Permissionless Internet-Scale Pretraining of Large Language Models](https://arxiv.org/abs/2607.13332)

**<font color=#1a73e8>作者：</font>** Gil Avraham, Violetta Shevchenko, Hadi Mohaghegh Dolatabadi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large language models at the multi-billion to trillion parameter scale is confined to datacenters, where data-parallel (DP) and model-parallel (MP) techniques presume homogeneous accelerators, high-speed interconnects, and a single orchestrating entity. Frontier model development is thereby concentrated among the few groups able to assemble such clusters. Meanwhile, an enormous pool of compute remains unusable for training: consumer and professional GPUs that are heterogeneous, preemptible, individually owned, and connected only by the internet. We present Agora, a system that makes efficient use of this compute. Agora combines bandwidth-efficient pipeline-parallel model sharding over internet-grade links with multi-party, fault-tolerant collective operations. Each participant holds only one stage of the model, and no single party ever possesses the full weights. We term this setup Protocol Learning: it enables collectively trained, collectively owned models, opening a path to open-source frontier training with economic sustainability. This report presents the outcome of a research effort spanning communication-efficient parallelism, asynchronous optimization, and fault-tolerant systems design. It culminates in the first demonstration of its kind: Pluralis-8B, an open, permissionless pretraining run of an 8.6B-parameter model on 500B tokens of FineWeb-Edu. The model was trained over 40 days by 330 contributor nodes, predominantly consumer GPUs on internet connections, joining and leaving throughout. The run sustained ~170k tokens/s and 4.2 tokens per TFLOP of pooled compute, 63% of the efficiency of a centralized H100 baseline, and converged to within a small margin of a centralized reference run.

---


### 24. [Delving into the Temporal Challenges of Unified Video Protection Against Image-to-Video and Fine-Tuning-based Customization](https://arxiv.org/abs/2607.13336)

**<font color=#1a73e8>作者：</font>** Yuxin Huang, Ziming Hong, Mingming Gong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion-based video generation models have enabled high-quality personalized video customization through both tuning-based pipelines, which fine-tune a video diffusion model, and reference-based pipelines such as image-to-video generation. However, these capabilities raise serious concerns about personal privacy, identity ownership and intellectual property protection. Existing anti-customization works focus on protecting images, while protection for videos against both reference- and tuning-based customization remains largely underexplored. Protecting videos in this setting raises three challenges: (i) Image-level perturbations, optimized frame by frame, cannot survive temporal compression by 3D video VAE. (ii) A video-level perturbation optimized on a single video is vulnerable to temporal editing and fails to protect unseen videos. (iii) Temporally inconsistent perturbations are not robust to temporal attacks. To address these challenges, we propose Temporally Consistent Universal Adversarial Perturbations (TC-UAP), the first protection method against both reference- and tuning-based video customization. TC-UAP optimizes an identity-level multi-frame UAP over sliding windows from multiple videos, accounting for local temporal dependencies induced by temporal compression in video VAE and enabling a single perturbation to protect unseen videos of varying lengths. Moreover, we introduce intrinsic temporal modeling and an extrinsic surrogate temporal-attack loss, which make the perturbation temporally consistent and robust to unseen temporal attacks. Empirically, quantitative and qualitative results show that TC-UAP achieves the strongest identity protection compared with existing methods under both reference- and tuning-based video customization, and remains robust under multiple unseen temporal attacks.

---


### 25. [Evaluation Ability Does Not Imply Optimization Utility: LLM-as-a-Judge Signals in Closed-Loop Table Recognition](https://arxiv.org/abs/2607.13347)

**<font color=#1a73e8>作者：</font>** Donghwan Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge is widely used to provide feedback and selection signals in closedloop regeneration, but this use remains insufficiently validated. We study it in table recognition, where deterministic TEDS evaluation provides a controlled testbed, using FinTabNet and OmniDocBench. Three findings emerge. First, judge signals were weak on both datasets: scores frequently tied, rankings were not reproducible, and the only selection policy that beat random on both datasets depended on an earliest-iteration tie rule, so its advantage cannot be attributed to the judge scores alone. Iteration produced better candidates, but the judge failed to recover them. Second, severe losses occurred even without specific judge feedback. A structurepreserving instruction significantly reduced the severe-loss rate on FinTabNet and was directionally consistent on OmniDocBench. The contrasts support target-preservation failure under unconstrained regeneration as a proximate mechanism of the observed severe losses. Third, the structure-preservation constraint reduced the severe-loss tail but produced no improvement. In an exploratory 2x2 analysis, the same protection was not stably observed when judge feedback was retained. These results do not dispute the value of LLMs as evaluators. Instead, they show that evaluation ability does not imply optimization utility. Iterative refinement requires, at minimum, a verification signal that deterministically detects structural change, rather than judge scores alone.

---


### 26. [TANDE: Disentangling Verbal and Nonverbal Backchannels in Emotional AI-Avatar Conversations with Young Adults](https://arxiv.org/abs/2607.13357)

**<font color=#1a73e8>作者：</font>** Ann-Kareen Gedeus, Jack Good, Nadine Wagener 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Embodied conversational agents (ECAs) need effective empathic grounding to foster social support and engagement. Expanding into emotional domains, ECAs now use Large Language Models (LLMs) and multimodal human-agent interactions to enhance their capabilities. Yet, understanding the impact of backchanneling modalities on young adults and their gender remains limited. We introduce TANDE, an LLM-powered ECA designed for emotional conversations with young adults, a population experiencing mental, personal, and social issues with limited tools to address them. In a within-subjects study with N=36 young adults, we explore nonverbal and combined verbal-and-nonverbal backchanneling modalities on rapport, empathy, and engagement and isolate for gender differences. Our research shows the importance of nuanced backchanneling cues with emotional ECAs with young adults, showing a preference for nonverbal cues. We derive design implications for more effective ECAs for emotional support and well-being in young adults. The code is available at this https URL.

---


### 27. [FM$^2$: Unified Federated Foundation Models for Heterogeneous Multimodal Medical Imaging](https://arxiv.org/abs/2607.13386)

**<font color=#1a73e8>作者：</font>** Shengchao Chen, Ting Shu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building foundation models for medical imaging requires pooling data across institutions, yet privacy regulations prohibit centralized aggregation. Existing Federated Foundation Models either fine-tune natural-image models with poor medical-domain transfer, or train from scratch within a single modality, lacking the flexibility to unify tasks. We identify an under-explored challenge, Imaging Modality Heterogeneity, where clients operate under two structural regimes: Overlapped (shared modalities with heterogeneous label distributions) and Non-overlapped (fully disjoint modalities per client). We propose FM$^2$, a unified framework that trains the core backbone from scratch to preserve medical domain fidelity while optionally incorporating biomedical pretrained encoders for vision-language alignment. FM$^2$ equips each client with dual Mixture-of-Experts modules (a Class-wise MoE for personalized category knowledge and a Domain-wise MoE for shared cross-modality representations), coupled with a Heterogeneous Modality Alignment (HMA) regularizer that explicitly aligns modality-specific expert parameters, admitting provable $O(1/\sqrt{T})$ convergence and generalization guarantees. FM$^2$ further incorporates Caption-Enhanced Learning (CEL), where locally retained GPT-4o-generated captions serve as a textual semantic bridge enabling representation transfer across clients with disjoint modalities, and demonstrates extensibility to Federated Medical VQA. Experiments on our MIMH benchmark (classification and CEL) and real-world medical VQA datasets confirm consistent superiority over state-of-the-art federated baselines and strong out-of-modality generalization across all three tasks.

---


### 28. [Where Should RL Post-Training Compute Go? Model Size, Search, Learning, and Feedback](https://arxiv.org/abs/2607.13389)

**<font color=#1a73e8>作者：</font>** Patrick Wilhelm, Odej Kao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) post-training is increasingly used to adapt foundation models for reasoning, planning, and feedback-driven robot-learning pipelines, but constrained post-training resources are often summarized by a single total FLOP budget. We study the fixed-budget decision problem behind this practice: under the same post-training budget, should one use a larger policy, train a smaller policy longer, generate more rollout search, or spend compute on stronger reward feedback? We introduce a FLOP-accounting framework for GRPO post-training that decomposes compute into rollout/search, policy-update/learning, and reward- or feedback-model evaluation. Across LoRA-adapted Qwen2.5 policies, we find conditional allocation frontiers: the best observed allocation changes with model size, compute budget, reward system, and evaluation target. Same-FLOP model-size comparisons show that model choice and training allocation are coupled because larger policies consume more per-token compute and therefore buy fewer updates or rollouts under the same budget. Reward systems also change the accounting: rule-based rewards spend nearly all non-update compute on policy rollouts, while PRM-style feedback allocates a visible part of the budget to reward-model inference. We present RACE as a diagnostic pilot-grid protocol, not a guarantee of held-out improvement, for identifying allocation regimes before expensive validation runs; our results suggest that RL post-training papers should report total FLOPs together with how compute is divided among model size, search, learning, and feedback.

---


### 29. [GFlowRL: Scaling Distribution-Matching RL to Large Language Models](https://arxiv.org/abs/2607.13394)

**<font color=#1a73e8>作者：</font>** Xiaodong Liu, Michael Xu, Jack W. Stokes 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative Flow Networks (GFlowNets) offer a promising alternative to reward-maximizing reinforcement learning (RL) for large reasoning models, encouraging diverse reasoning paths by matching reward distributions rather than collapsing to dominant modes. Recent work shows promise on math and code, but scaling GFlowNet-style RL to modern post-training pipelines remains difficult: as model size, rollout horizon, reward noise, and distributed-systems complexity grow together, a learned prompt-conditional partition function becomes a source of gradient instability and engineering overhead rather than a useful normalizer. Through systematic analysis, we find that the learned partition function, previously treated as essential, can be replaced by an in-batch Monte Carlo estimate computed from the rollout group already required for training. We propose GFlowRL, a streamlined GFlowNet-style RL algorithm that removes the auxiliary partition network entirely while preserving the reward-distribution-matching objective, completed by two stabilizers: importance-sampling correction for rollout/trainer drift and asymmetric flow-gap clipping for outlier residuals. GFlowRL exceeds all counterparts on math, code, and adversarial red-teaming benchmarks, reaching a Codeforces rating of 2048 at the 14B scale (within 25 Elo of o3-mini) and attaining the highest average ASR@1 on AdvBench and HarmBench, outperforming the previous SOTA multi-turn attacker in a regime where FlowRL, a prior GFlowNet-style method, diverges. The same recipe transfers to all evaluated MoE configurations up to 235B parameters, where FlowRL again fails to converge. To our knowledge, GFlowRL is the first GFlowNet-style RL algorithm to scale stably across both dense and sparse architectures. Code will be at: this https URL

---


### 30. [Self-Improving is Often Sudden: Enlightenment-style Finetuning for Large-Scale Models](https://arxiv.org/abs/2607.13395)

**<font color=#1a73e8>作者：</font>** Jing-Xiao Liao, Tianwei Zhang, Yu-Hao Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The pursuit of autonomously self-improving models has attracted growing interest in the era of large-scale foundation models. Drawing inspiration from the concept of "enlightenment" or "aha moment" in human brain, we hypothesize that large models exhibit an analogous enlightenment phenomenon-a latent capacity for sudden capability boost. Then, we propose Enlightenment, a novel training-free post-tuning paradigm for large-scale models. Our approach modifies shortcuts for key modules/layers without weight updates, while existing training-free ones predominantly manipulate attention weights. We introduce two architecture-specific instantiations: i) For large language models, we propose attention head-mixing shortcuts that recalibrate attention weights by linking the initial attention head's output to all other target heads, modulated by an adaptive scaling factor initialization strategy. ii) For vision-language models, we apply a lightweight scalar-modulated factor to residual connections in the decoder layers, regulating information flow. Extensive experiments show that Enlightenment efficiently unlocks the latent potential of pre-trained networks, yielding remarkable performance improvements across diverse benchmarks and models.

---


### 31. [EXPLORE: Exploration with Guided Search for Analog Topology Generation using Language Models](https://arxiv.org/abs/2607.13416)

**<font color=#1a73e8>作者：</font>** Guanglei Zhou, Chen-Chia Chang, Yikang Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automating analog circuit topology design is essential to reduce the extensive manual effort required to meet increasingly diverse and customized application demands. Recent advances have applied sequence-to-sequence fine-tuning on pretrained language models to directly generate circuit topologies from user specifications in a single pass. However, these one-shot generation methods failed to generate complex circuits due to their exponentially growing search spaces and limited training datasets. In this paper, we present EXPLORE, a search-enhanced framework that integrates simulator-guided Monte Carlo Tree Search (MCTS) with transformer-based decoding to enable test-time scaling for analog topology generation. By leveraging language-model priors and bypassing high-confidence structural tokens, EXPLORE allocates expensive simulator budget primarily toward topology-altering decisions during search. On a 6-component benchmark at a tight tolerance of 0.01, EXPLORE raises the success rate from 12% for one-shot generation and 33% for a sampling-and-filter baseline to 65%, and lowers MSE by over 20% relative to sampling-and-filter under the same search budget. These results establish EXPLORE as the first framework to integrate structured test-time search with LM decoding for analog topology generation, and a practical step toward scaling LLM-driven design automation.

---


### 32. [Data-Efficient Adaptation of LLMs via Attention Head Reweighting](https://arxiv.org/abs/2607.13425)

**<font color=#1a73e8>作者：</font>** Tuomas Oikarinen, Zixiao Chen, Charlotte Siska 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning effectively from limited data is critical in domains like security where labeled examples are scarce. Large language models (LLMs) have demonstrated some capabilities for data-efficient learning, especially through parameter-efficient adaptation methods, but continue to struggle when faced with few samples for difficult tasks. To meet this challenge, we propose Attention Head Reweighting (AHR), a data-efficient method that adapts LLMs to new text-classification tasks by learning only a single scalar per attention head. This drastically reduces the number of parameters that need to be learned by making use of the functional specialization of individual attention heads. Experiments on diverse open-source text classification datasets show that AHR can outperform standard baselines like LoRA when learning from limited samples, despite having 200-1000x fewer trainable parameters, as our AHR only modifies ~0.0001% of the model's parameters. In addition, our learned weights are easy to interpret and can be analyzed to better understand the mechanisms and attention heads responsible for in-context learning abilities in LLMs.

---


### 33. [Exploring Post-Training Alignment of Small Language Models for Biomedical Data-to-Text Generation: A Case Study of Medication Leaflet](https://arxiv.org/abs/2607.13430)

**<font color=#1a73e8>作者：</font>** Xi Yang, Guodong Liu, Chuqin Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Translating complex biomedical data into patient-friendly narratives is central to modern biomedical informatics. This study presents a comparative analysis of training small language models (SLMs) in specialized biomedical datato-text generation tasks. We explore widely adopted post-training methods including supervised fine-tuning (SFT), direct preference optimization (DPO), odds ratio preference optimization (ORPO), and group relative policy optimization (GRPO) with Qwen-based SLMs on a medicine package leaflets dataset. To assess cross-dataset generalizability, we also curated drug label data from openFDA. We evaluate models using both standard lexical overlap metrics like ROUGE as well as semantic similarity measures. Across our experiments, the results show that (1) the aligned SLMs outperform proprietary models like GPT-5; (2) ORPO outperforms the SFTbaselines; (3) GRPO yields the most robust cross-dataset performance among the alignment methods tested as well as GPT-5.

---


### 34. [When Rubrics Change: Cross-Rubric Generalization for Critical Thinking Essay Scoring](https://arxiv.org/abs/2607.13433)

**<font color=#1a73e8>作者：</font>** Nischal Ashok Kumar, Payu Wittawatolarn, Sana Kang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated essay scoring (AES) research has largely focused on cross-prompt generalization, where essays from unseen prompts are scored while the scoring criteria are typically held constant. In practice, however, educators may revise or even introduce new rubrics in their scoring task, to evaluate different aspects of essays. We study cross-rubric generalization: training on essays labeled under one set of rubrics and evaluating on previously unseen rubrics, which target different aspects of the essay. We use a Large Language Model (LLM) fine-tuning framework with two components: rubric-agnostic intermediate representations, called traits, and target-essay supervision under seen rubrics during training. On an AES dataset augmented with multiple rubric-defined labels of student critical thinking skills, we find that traits improve macro F1 by 5.0% over a baseline without traits in the hardest setting, where both target rubrics and target essays are unseen during training. We further find that increasing target-essay supervision improves performance, with our best fine-tuned open-source Llama-based model outperforming GPT-5-mini prompting by 2.1% macro F1 and trailing GPT-5 by 1.9%. These results show that trait-based intermediate structure and controlled supervision improve generalization to unseen rubrics.

---


### 35. [GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding](https://arxiv.org/abs/2607.13454)

**<font color=#1a73e8>作者：</font>** Hao Li, Han Fang, Zixin Pan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although multimodal large language models (MLLMs) have achieved remarkable progress, understanding 3D spatial relationships from 2D images remains a critical challenge. Existing methods primarily rely on symbolic text tokens, which inherently lack the fidelity to represent continuous geometric information. While recent methods use latent representations to enhance reasoning, relying on a single latent type cannot adapt to the diversity of spatial tasks, leading to misalignment in complex geometric scenarios. To address these limitations, we propose GeoAnchor, an interleaved text-latent reasoning framework. GeoAnchor decomposes 3D spatial information into three complementary components: position latents for object grounding, direction latents for relational orientation, and geometry latents for scene structure. These components are recombined in a structured space to construct local evidence while capturing global context, enabling dynamic and interpretable reasoning. Furthermore, we introduce a collaborative training strategy that guides the model from local spatial perception to comprehensive 3D understanding. Extensive experiments on diverse and complex 3D reasoning tasks demonstrate that GeoAnchor outperforms the state of the art, validating its effectiveness and generalization capabilities.

---


### 36. [PQFA: Parallel Quantum Feature Augmentation of Fused Representations for Multimodal Classification](https://arxiv.org/abs/2607.13466)

**<font color=#1a73e8>作者：</font>** Mingzhu Wang, Yun Shang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most multimodal learning methods improve how heterogeneous representations are aligned and fused, while post-fusion enhancement remains less explored. We propose Parallel Quantum Feature Augmentation (PQFA), a hybrid quantum-classical framework that applies multiple shallow variational quantum circuits to fused multimodal features. Text and image representations extracted by frozen RoBERTa and ViT encoders are processed through bidirectional cross-attention, attentive pooling, and adaptive gated fusion. The fused feature is then amplitude-encoded into parallel quantum circuits, whose measurement readouts are concatenated with the classical representation for prediction. We evaluate PQFA on MM-IMDb and N24News through controlled comparisons using the same encoders, fusion backbone, data splits, projection dimension, and augmentation output width. PQFA consistently outperforms both the fusion backbone without quantum augmentation and a width-matched MLP augmentation baseline, while using approximately 2.2K augmentation parameters compared with 24.0K for the MLP branch. Missing-modality experiments further show improved robustness when textual or visual inputs are incomplete, with particularly clear gains when the more informative textual modality is severely degraded. Controlled ablations and feature-space analyses indicate that the improvement cannot be reproduced by random feature mappings, increased classical width, or untrained quantum transformations. Quantum-state diagnostics additionally show stable predictive performance across the tested simulated noise levels and distinct branch-specific transformations of the encoded states. These results establish PQFA as an effective and parameter-efficient strategy for post-fusion augmentation in hybrid quantum-classical multimodal learning.

---


### 37. [MyAG: A Graph-Based Framework for Designing and Analyzing Composable LLM Agent Systems](https://arxiv.org/abs/2607.13474)

**<font color=#1a73e8>作者：</font>** Zhisong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present MyAG, a graph-based framework for designing and analyzing composable LLM agent systems. Our framework separates agent system construction into three graph abstractions: a component graph for agents, environments, and modules; a workflow graph for execution control; and a search graph for runtime execution. This separation allows users to flexibly reuse the same components with different strategies. We further support hierarchical composition through recursive system nodes and provide monitoring and visualization tools for inspecting agent execution. Experiments on representative agent applications show that our framework supports flexible agent system design and helps analyze performance-efficiency tradeoffs. Our framework is publicly available and fully open-source.

---


### 38. [Attention-Free and Lightweight Token Reduction for Efficient Vision-Language Models](https://arxiv.org/abs/2607.13500)

**<font color=#1a73e8>作者：</font>** Xuanyi Hao, Zuoyuan Zhang, Zhibo Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have achieved strong performance in multimodal understanding, yet remain challenging to deploy on resource-constrained edge devices due to the substantial computational overhead of processing numerous visual tokens. Token reduction is a promising direction for accelerating VLMs inference, but existing approaches either rely on attention maps that are incompatible with modern acceleration frameworks or depend on computationally intensive pairwise similarity comparisons, which undermine scalability and negate their practical benefits in deployment. In this paper, we propose an attention-free and lightweight token reduction framework as a plug-and-play module for VLMs, which preserves both important and diverse tokens to produce a compact visual representation. First, to enable attention-free importance estimation, we adopt an information-theoretic perspective and quantify token information using a novel entropy-based criterion, retaining those with more expressive and less degenerate feature representations. Second, to ensure diverse visual coverage in a lightweight manner, we introduce a transformation-induced consistency signal where similar tokens yield similar signals, such that sorting by this signal places similar tokens close to each other and enables stride-based selection to produce a diverse token set. Extensive experiments across multiple VLMs benchmarks demonstrate that our framework achieves a favorable accuracy-efficiency trade-off, maintaining competitive performance under aggressive compression.

---


### 39. [ExTernD: Expanded-Rank Ternary Decomposition Ternary LLM PTQ with Accuracy Approaching Any Quantization Level](https://arxiv.org/abs/2607.13511)

**<font color=#1a73e8>作者：</font>** Chethan Reddy G.P  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce ExTernD (Expanded-rank Ternary Decomposition), a post-training factorization of each LLM weight matrix $A \in \mathbb{R}^{m \times n}$ into $A \approx B \mathrm{diag}(D) C$ with ternary factors $B \in \{-1,0,+1\}^{m \times k}$, $C \in \{-1,0,+1\}^{k \times n}$ and a real scale vector $D \in \mathbb{R}^k$. The inner rank $k = \mu \min(m,n)$ is deliberately expanded beyond full rank ($\mu > 1$), so that components past full rank correct the quantization error of earlier ones. We prove the residual decreases monotonically in $k$ and can be driven below any $\varepsilon > 0$: ExTernD approaches bf16 accuracy arbitrarily closely, which no ternary scheme with a fixed plane count can do. Memory and compute scale continuously with $\mu$, and factor sparsity continuously with a threshold $\tau$, so an accuracy target is hit exactly rather than rounded to the next bit-width. ExTernD matches Q4_K's per-matrix accuracy at 5.2-5.5 effective bpw (5.1-5.5 with importance weighting) on Gemma-4-E2B and Qwen3.5-4B, and a full Qwen3.5-4B conversion at $\mu = 3$ reaches 10.10 wikitext-2 perplexity against 9.78 for bf16 (+3.2%), placing it near the Q4_K/Q5_K accuracy band at ~5.7 effective bpw.

---


### 40. [ThinkBLOX: 3D Indoor Scene Generation with Progressive Reasoning](https://arxiv.org/abs/2607.13539)

**<font color=#1a73e8>作者：</font>** Yuan Xiao, Can Wang, Xiangyu Kong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While traditional graphics methods often synthesize 3D indoor scenes autoregressively or hierarchically, recent vision-language model (VLM)-based generators predominantly adopt a one-shot paradigm where the full layout is planned at once. This one-shot approach often requires global re-optimization or complete reconstruction during interactive editing (e.g., inserting or moving objects) and can lead to physically or semantically poorly organized arrangements. To address these challenges, we propose ThinkBLOX, a VLM-based progressive reasoning framework that iteratively designs and refines 3D scenes. ThinkBLOX treats layout generation as a state-conditioned, step-by-step reasoningand-action process. To power this, we construct the ThinkBLOX-Data-200K dataset, containing 224,757 procedural placement pairs annotated with multi-view scene context, explicit Chain-of-Thought (CoT) rationales, and structured JSON layouts. Through supervised fine-tuning (SFT) on this dataset, the VLM learns to bridge the reasoning-action gap under incremental updates. Furthermore, recognizing that scene synthesis is inherently a multisolution task where SFT suffers from reward conflict, we introduce Tier-Decoupled GDPO. This reinforcement learning scheme organizes heterogeneous rewards into distinct tiers, stabilizing policy optimization across physical validity, semantic plausibility, and reasoning-action consistency. Extensive experiments show that ThinkBLOX significantly outperforms recent one-shot and iterative baselines in physical plausibility, semantic alignment, and interactive editability. Additionally, we show that it supports diverse applications, including both global and local generation and rearrangement of 3D scenes.

---


### 41. [Cost-Pragmatic Quality Gating and Selection-Fusion Multi-Model Combiners for BioASQ Phases A+ and B](https://arxiv.org/abs/2607.13551)

**<font color=#1a73e8>作者：</font>** Dima Galat, Marian-Andrei Rizoiu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe our BioASQ Task 14B 2026 system. The work centers on two design decisions: how aggressively to re-retrieve when first-stage retrieval is weak, and how to combine multiple language-model answers. Retrieval unions two parallel pipelines - a hybrid first stage (dense BGE + BM25 + RRF, reaching R@200 = 99.3% on the BioASQ-13b historical archive) and an agent-driven pipeline that decomposes the question over PubMed, Europe PMC, and iCite - with a BGE cross-encoder quality gate flagging weakly-supported questions for selective re-retrieval. On Task 12B 2024 validation, a cost-pragmatic re-retrieval policy beats a skill-strict baseline significantly on list F1 and list precision, at 12% lower re-retrieval cost. Holding prompt and model fixed across val and test 13B (different question sets), list F1 rises by +0.132 absolute on the BioASQ-released gold-input pool, consistent with substantial retrieval-side headroom. For Phase B answering we decompose multi-model ensemble lift into a selection component bounded by the per-question oracle and a fusion component that aggregators can exceed. The decomposition predicts before any experiment that LLM-as-judge wins on selection-dominated metrics (yes/no, multi-reference ROUGE) but is structurally insufficient on the recall component of fusion-friendly metrics (factoid rank-1, list recall). On Task 13B 2025 our synonym-union resolver wins list recall on every head, while GPT-5.5 solo retains the list-F1 lead because the resolver's wider item set costs precision. On the Task 14B 2026 preliminary leaderboard our team places first on the combined-exact aggregate on three of the eight (phase x batch) leaderboards, wins four individual question-type cells, and takes #1 on Phase B b3 ideal.

---


### 42. [Graded Entity-Familiarity Readouts in Language Models: Polish Adaptation, Cross-Language Robustness, and Refusal Steering](https://arxiv.org/abs/2607.13568)

**<font color=#1a73e8>作者：</font>** Grzegorz Brzezinka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can a language model estimate its familiarity with an entity before generating an answer? We study activations at the final prompt token in twelve instruction-tuned models from the Bielik, PLLuM, Gemma-4, and Qwen3 families, using a new dataset of 1,440 Polish entities spanning four domains and ten Wikipedia-pageview deciles, plus fabricated controls. Familiarity-probe scores separate real from fabricated entities in every family; in the Polish-adapted Bielik and PLLuM families they additionally track entity popularity (model-mean Spearman $\rho$ 0.28-0.57, versus at most 0.11 in Gemma-4 and Qwen3), a pattern more strongly associated with Polish adaptation than with parameter count in this model sample. In a paired experiment on two families, probes retain 96-101% of within-language AUROC when the Polish question stem is replaced with an English one around unchanged entity names, showing robustness to prompt language in this setting. In Gemma-4-12B, the only model that natively refuses, adding a one-dimensional familiarity direction at a single layer moves refusal rates monotonically in both directions (0.24 to 1.00 on well-known entities; 0.73 to 0.00 on unknown ones). Finally, a calibrated familiarity probe is competitive among pre-generation abstention gates, although post-generation detectors better predict behavioral error on average. These results support a graded pre-generation entity-familiarity readout, and a separation between representational familiarity and the policy that converts it into abstention.

---


### 43. [Memory as a Controlled Process: Learned Adaptive Memory Management for LLM Agents](https://arxiv.org/abs/2607.13591)

**<font color=#1a73e8>作者：</font>** Eric Hanchen Jiang, Zhi Zhang, Yuchen Wu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents increasingly rely on external memory systems to accumulate experience across tasks. Yet nearly all existing approaches, from graph-structured memories to reflective insight stores, access memory through fixed, hand-designed heuristics. We argue that this static view of memory is a core bottleneck for agentic learning because optimal memory behavior is fundamentally context-dependent. The early stages of the tasks, benefit from minimal retrieval because memory is sparse; recurring goal types benefit from plan reuse rather than generic nearest-neighbor lookup; stuck agents benefit from re-retrieval with alternative queries; and across long task streams, the memory store itself must be consolidated and pruned to remain useful. We present Memory as a Controlled Process (MemCon), a framework that models memory operations as a Markov Decision Process and learns an online policy that adaptively decides when, what, and how much to retrieve, when to inject a distilled plan, and when to consolidate or forget. MemCon is backend-agnostic: it wraps any existing memory implementation, learns from task-by-task binary feedback with no pretraining and no additional LLM calls, and uses a lightweight tabular contextual bandit with UCB exploration that converges within tens of tasks. Across 6 benchmarks, 3 agent frameworks, and 3 LLM backbones, MemCon consistently outperforms multiple memory baselines by up to 15.2 points in task success while reducing token consumption by 5--20%.

---


### 44. [Analogical Deep Research: Retrieving and Integrating Historical Analogies for Foresight Analysis](https://arxiv.org/abs/2607.13602)

**<font color=#1a73e8>作者：</font>** Yongqiang Chen, Guangyi Chen, Yuewen Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systematic comparisons between current situations and structurally similar past events in the historical, i.e., historical analogies, is among the most powerful tools for foresight analysis. In this work, we present a new task called Analogical Deep Research (ADR) to Large Language Model (LLM) agents and construct the first ADR benchmark ADR-bench to study whether LLM agents are able to find and leverage historical analogies when doing foresight analysis. Our investigation reveals a key obstacle: LLM agents are poor at finding analogies because they match on surface features rather than underlying mechanisms. We argue that ADR is inherently a causal question as it requires understanding why the event occurred. Based on our theoretical analysis, we propose two principles required for ADR, including the mechanism alignment and cross-analogy confirmation. Built upon our theoretical results, we propose a new agentic framework called Causal Analogical Researcher (CANA) that guides LLMs to find and integrate historical analogies. CANA incorporates a simple yet effective structural decomposition representation, and integrates structural feedback for reflective improvements of historical analogy identification and integration. We show that CANA brings up to 10% improvements in historical analogy generation, and surpasses the state-of-the-art deep research agents in the ADR-bench. Case studies with the ongoing events confirm the effectiveness of CANA in leveraging historical analogies.

---


### 45. [Automatic Ordinary Differential Equations Discovery For Biological Systems Using Large Language Model Powered Agentic System](https://arxiv.org/abs/2607.13608)

**<font color=#1a73e8>作者：</font>** David Krongauz, Arad Zulti, Eran Segal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic scientific discovery has long been a goal of computational scholars - a machine that can discover nature's secrets on its own, moving computational systems beyond data-fitting tools toward the generation and refinement of mechanistic models of the universe. Recent advances in symbolic regression (SR) and large-language-model (LLM)-based agents suggest that such systems can recover equations from data, incorporate domain priors, and automate parts of the research workflow. However, most existing approaches either focus on narrow equation-discovery benchmarks or broad end-to-end automation pipelines, while biological systems remain comparatively underexplored. Here, we introduce the MEDA system, an LLM- and SR-powered agentic framework for discovering ordinary-differential-equation (ODE) models of biological and biologically inspired dynamical systems. MEDA retrieves background knowledge, defines admissible variables, generates mechanistic constraints, proposes candidate ODEs, and fits and evaluates them. We evaluate it across canonical model retrieval, reasoning-based extrapolation to unseen variants, and open-ended discovery, with and without experimental data. Across these settings, MEDA recovered the correct state variables, achieved strong structural recovery in retrieval and extrapolation tasks, and produced biologically plausible discovery-oriented models. Ablation and robustness analyses show that knowledge-guided formalization and mechanistic constraints are load-bearing components, whereas numerical fitting alone can preserve trajectory-compatible but biologically incorrect equations.

---


### 46. [The SIGReg Objective as Variational Free Energy: A Theoretical Active-Inference Account of JEPA World Models](https://arxiv.org/abs/2607.13612)

**<font color=#1a73e8>作者：</font>** Fabio Arnez, Alexandra Gomez-Villa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) are the dominant design for latent world models, yet they are usually justified by empirical performance rather than a normative principle. We show that the choice of anti-collapse regulariser determines whether a JEPA's training objective, a prediction loss plus a weighted embedding regulariser, is a valid Active Inference (AIF) variational free energy. We organise four non-contrastive regularisers (VICReg, LogDet, PairDist, and SIGReg) into an entropy-estimator hierarchy indexed by a prior-miscalibration gap, and show that the gap's sign, whether the estimator bounds the latent entropy from above or below, decides whether the AIF surprise bound survives: VICReg and LogDet are unsafe upper bounds, PairDist a safe lower bound, and SIGReg eliminates the gap. We then prove a correspondence theorem: under the standard constant-noise encoder model and successful SIGReg enforcement (isotropic-Gaussian embeddings), the gap vanishes, the objective becomes an exact information bottleneck, the surprise bound is preserved, and the latent goal cost becomes an exact proxy for AIF pragmatic value, whereas VICReg leaves an irreducible second-order anisotropy term. We extend the correspondence to multi-step expected free energy, ensemble epistemic value, and a learned-policy regime, and we identify the one AIF term no current JEPA world model computes: the state-epistemic value, a future-state coverage signal. The predictions differ in kind, not degree, and are stated here as theoretical consequences left for empirical test in separate work; full proofs are in Appendix A, and the algebraic core of every result is machine-verified in Lean 4 (Appendix D).

---


### 47. [VIP-MINGLE: A Corpus for Videoconference and In-Person Multimodal Interaction in Group Language Engagement](https://arxiv.org/abs/2607.13614)

**<font color=#1a73e8>作者：</font>** Andrew Chang, Abhinay K Bodi, Wenxin Deng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Group conversations are a fundamental yet complex form of social interaction central to human cognition and telecommunication technology. While understanding and facilitating these interactions has been a long-standing goal, findings are often isolated within specific in-person or videoconferencing settings due to a scarcity of datasets that bridge the two. We introduce VIP-MINGLE, a multimodal dataset comprising 59 hours of recordings (32 groups, 105 participants), featuring paired within-subject sessions in both settings. The dataset includes raw audio/video, psychometric data, processed multimodal features (e.g., diarized speech, facial expressions, transcriptions), and time-resolved human annotations. Our analysis reveals significant behavioral distribution shifts across multiple modalities between settings, reinforcing the need for a cross-setting corpus. VIP-MINGLE serves as a critical resource for developing robust models of group conversations across settings.

---


### 48. [STOCKTAKE: Measuring the Gap Between Perception and Action in LLM Agents with a Fair Oracle](https://arxiv.org/abs/2607.13618)

**<font color=#1a73e8>作者：</font>** Sagar Deb, Ashwanth Krishnan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly evaluated on multi-week decision tasks in which the state that drives cost is never directly observed. On such tasks the final cost cannot say why an agent failed: it may have misread the world, or read it correctly and still failed to act (the knowing-doing gap). Existing evaluations cannot separate these two failures; their reference policies either read privileged information the agent never sees, or are missing altogether. We introduce STOCKTAKE, a 26-week supply-chain replenishment benchmark built as a factored partially observable Markov decision process with six hidden factor processes, designed so that a fair reference policy is computable: an exact Bayes filter per factor drives a rollout policy on the identical observation stream the agent receives. Scoring each run between a symptom-blind base-stock floor (0) and this oracle (1) yields a skill score, and grading each week's written rationale yields a stated-belief detection lag and a knowing-doing rate, so state estimation and control are measured separately. On fifty seeds with curated stress profiles, Claude Sonnet 5, GPT-5.4, DeepSeek-V4-Pro, and Grok 4.5 detect 84-88% of hidden failures, typically within a week of onset, yet span skill scores from 0.62 to -0.23: two of the four end below the symptom-blind floor while naming factors slightly faster than the two that beat it. The failure has two faces. Where stress persists, 34-43% of correctly diagnosed stress weeks still end in stockout for every model, a rate that partly reflects the severity of the weeks models notice. That rate also runs opposite to skill: the two models under the floor stock out least on diagnosed weeks, so under-response is only one face of the gap, and their traces point to the other, responses whose cost exceeds what they protect. STOCKTAKE measures both directions of that failure.

---


### 49. [From Surface Forecasting to Observability Forecasting: A Latent World Model for Cloud-Aware EO Monitoring](https://arxiv.org/abs/2607.13651)

**<font color=#1a73e8>作者：</font>** Mohanad Albughdadi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The bottleneck of Earth Observation processing chains is not the arrival of new imagery but whether the surface is actually visible when the image arrives. We study this as an observability forecasting problem on EarthNet2021. Given recent multispectral imagery and exogenous weather drivers, the goal is to predict whether the next acquisition will be usable and, if not, when a usable view is likely to return. To do this, we adapt LeWorldModel, a joint-embedding predictive architecture world model, to cloud-aware Earth Observation sequences. The final pipeline converts raw minicubes into episodic HDF5 sequences with five image channels (blue, green, red, near-infrared, cloud mask) and eight meteorological and calendar covariates. The resulting model has 18.0M trainable parameters and is trained from scratch on 23,904 training episodes. The trained leWorldModel is evaluated under a locked protocol: linear probes are fit on train only, calibration choices are set on an internal validation split, and the fitted heads are then frozen for valsplit, IID, OOD, and extreme evaluation. On the full frozen-bundle observability benchmark, LeWorldModel consistently outperforms persistence. For next-step usability, balanced accuracy ranges from 0.769 to 0.887, compared with 0.493 to 0.556 for persistence. For exact first-usable-horizon prediction, accuracy ranges from 0.602 to 0.806, compared with 0.120 to 0.369 for persistence. Against a frozen LightGBM baseline fit on the same training windows, LeWorldModel is better on continuous clear/cloud regression and on exact recovery timing on valsplit, IID, and extreme, while LightGBM is stronger on the simpler binary any-usable-within-six task and is more robust on OOD. In separate sampled diagnostic analyses, LeWM also produces strong ranking-based anomaly signals under synthetic temporal inconsistencies.

---


### 50. [Fine-grained CLIP fine-tuning with self-annotated region alignment](https://arxiv.org/abs/2607.13661)

**<font color=#1a73e8>作者：</font>** Chenyang Zhao, Wei Lin, Antoni B. Chan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive Language-Image Pre-training (CLIP) has been shown to have limitations in its fine-grained dense feature representation, due to its pre-training focusing on matching the whole image to a text description. Considering the large data and computational burden in pre-training a vision-language model from scratch, a series of works aim to enhance the fine-grained ability of CLIP through a fine-tuning scheme. However, existing works suffer from a variety of limitations: additional region annotations are usually required, which limits the semantic diversity due to the predefined categories and leads to a large effort to process the training data; and they usually sacrifice CLIP's original ability for global visual representation. To bypass these limitations, we propose SFF-CLIP (Self-annotated Fine-grained Fine-tuning for CLIP), which only uses image-text pairs as input to boost the fine-grained representation ability in the CLIP fine-tuning, while maintaining the global visual-semantic consistency. Concretely, a run-time region-phrase alignment scheme is designed, which obtains concept phrases from the input sentence, and aligns them with corresponding extracted region-based features using text-specific heat maps. Extensive experiments demonstrate that SFF-CLIP leads to significant performance improvements on fine-grained dense feature representation, as well as maintaining the performance of the original CLIP on image-level tasks. Code will be released later.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-73](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
