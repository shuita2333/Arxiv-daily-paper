# 🧠 大模型相关研究 | 2026年10月06日

> 本类共 **261** 篇论文：已确认 **243** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-261](./part-06.md)

---

### 1. [Overcoming Challenges of Interpretive Structural Modeling with Large Language Models](https://arxiv.org/abs/2610.02254)

**<font color=#1a73e8>作者：</font>** Everett Rush, David J. Icove, Ari Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretive Structural Modeling (ISM) is a well-known process for multi-criteria decision making. The success of ISM over other methodologies is its ability to model causal relationships, the binary scale of factors, and resulting hierarchical representation. Traditionally, the modeling process is performed by repeated interactions with subject matter experts until consensus is reached. This process is tedious, labor-intense, and most importantly limits the ability of ISM to scale to studies with hundreds of variables. Drawing on existing work of causal graph discovery with large language models (LLM) as imperfect experts, this work explores an integrated LLM-ISM approach for ISM. Pairwise, k-wise, rowwise, and full graph discovery methodologies are compared and evaluated. It is shown that causal graph discovery methods for ISM perform best using rowwise (SHD=160, F1-score=0.77) and full graph methods (SHD=135, F1-score=0.73).

---


### 2. [Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses](https://arxiv.org/abs/2610.02267)

**<font color=#1a73e8>作者：</font>** Jiawei Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses make many small, typed decisions per task: which model to call, which tool to use, whether retrieved text is relevant, whether an input carries an injection. System-1 decision models answer such questions in a single forward pass with class probabilities, promising large cost and latency savings over LLM calls. We present a paired evaluation of an open-weight (Laya) and a hosted (Jev) System-1 model on 11 agent decision points built from 18 public sources: 7,283 base cases plus 6,640 robustness variants, with byte-identical inputs, paired tests, and cross-hardware and cross-day reproducibility checks. Jev is significantly more accurate on 9 of 11 decision points (+10.8 to +46.0 pp). Neither model beats chance on zero-shot model routing, and they tie on RAG relevance gating. Laya changes 30% of its answers when the option order is reversed and degrades sharply with many or similar candidates (31% at 50 nearest-neighbour tools, vs. 98% for Jev on items with a unique correct tool). We also audit our own pipeline. Three analysis errors and one design confound distorted headline deployment claims: an omitted pre-screen cost (reported 23.9% saving, actual 4.3%), gate accuracy reported as end-to-end quality (58% vs. 98%), in-sample thresholds (5% target, up to 17% held-out misses), and a "channel effect" on injection false positives that vanishes with channel-native content. Two other suspected confounds did not change the conclusions. All cases, raw outputs and analysis code are available at this https URL.

---


### 3. [The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?](https://arxiv.org/abs/2610.02281)

**<font color=#1a73e8>作者：</font>** Bart Jaworski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Societal resilience research relies on access to useful and actionable data, which motivates our main research question: Can annual reports, processed at scale with LLMs, provide a useful signal about how companies disclose their response to AI? We test this by applying a reproducible two-stage classification pipeline to 9,821 annual reports from 1,362 UK listed companies (2020-2025, with partial 2026 data). We first validate the method against 474 human-annotated passages, finding high recall and moderate label-level agreement. We then report three empirical patterns: (i) between 2020 and 2025, the share of reports mentioning AI risk rose from 2.8% to 41.2%, while AI adoption disclosure also rose, from 13.8% to 45.2%, and named vendor mentions cluster around a small set of major providers led by Microsoft; (ii) disclosure varies substantially by Critical National Infrastructure sector and market segment: AIM reports disclose AI risk at far lower rates than Main Market reports, and sectors such as Energy and Data Infrastructure lag behind the rest in AI risk disclosure; and (iii) harm disclosures are near-absent (seven reports across the entire corpus). We develop a substantiveness classification to assess the quality of the disclosure and find that most AI risk disclosure is not substantive: in 2025, 41.2% of all reports mention AI as a risk, but only 4.3% contain AI risk disclosure we classify as substantive.

---


### 4. [HakemBench: A Turkish Benchmark of Typed Decisions](https://arxiv.org/abs/2610.02293)

**<font color=#1a73e8>作者：</font>** Sait Furkan Teke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> HakemBench is a Turkish benchmark of typed decisions, in which the model under test reads a text, a question and a fixed set of options and returns a probability for every option. Version 1.0 is released fully open under CC BY 4.0, with 2,346 items and 4,275 choice, yes/no and score questions in seven tracks (fact-check triage, education, guardrails, legal routing, moderation, spam and phishing, and customer support). One harness scores decision quality (macro F1), calibration (from the normalised Brier score) and selective automation (from the normalised area under the generalised risk-coverage curve), combines them by a geometric mean and reports intervals from 2,000 bootstrap draws; probes for option order, paraphrase, English translation and substituted names are reported alongside. Most gold labels come from blind passes of one AI model family compared with the votes of a panel of large language models from other model families; they are not human-verified. On a board of 16 rows the leader scores a composite of 0.888 and the lab's own model is 7th at 0.660. Its numbers are not blind. Earlier runs' test results shaped its training data, so its guardrail, moderation and customer support numbers are flagged; with every model scored on the other four tracks only, its composite is 0.678, 6th of 16.

---


### 5. [EditHero: A Benchmark for Long-Horizon Part-Level 3D Editing and Vibe Modeling](https://arxiv.org/abs/2610.02298)

**<font color=#1a73e8>作者：</font>** Ruihan Yu, Yu-Ju Tsai, Muyao Niu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D editing methods are usually tested on a single edit, yet an asset is built through a long sequence of revisions, each of which must implement the requested change while leaving everything else unchanged. We introduce EditHero, to our knowledge the first benchmark for long-horizon, part-level 3D editing, with natural-language instructions and target images for both geometry and texture. A deterministic assembly engine produces the exact target after every edit, and every sequence is reviewed by hand. We use EditHero to compare 2 opposite approaches to 3D editing. Non-agentic methods operate top down, regenerating the object from a learned 3D representation and inferring what to keep. In contrast, LLM/VLM agents operate bottom up, editing through code that inspects the mesh and rewrites only the parts required by instructions. The non-agentic methods often miss the requested change and disturb regions that should stay fixed. Most LLMs follow instructions more closely, and all of them preserve the unedited parts better, but each of their edits takes minutes. We will release the engine and the edit sequences to support research on reliable iterative 3D editing.

---


### 6. [PowerBench: Measuring Language Model Bias in Power-shifting Requests](https://arxiv.org/abs/2610.02303)

**<font color=#1a73e8>作者：</font>** Nicolas Martorell, Wendy Brau, Gonzalo A. Heredia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models increasingly assist people with power-related requests, so systematic differences in whom they help could shift the distribution of power at scale, or be exploited by users who learn which identities are refused less. We introduce PowerBench, an evaluation of power-shifting requests that distinguishes self-empowerment, disempowerment, and power grabbing, plus a control of refusal-inducing requests that shift no power. We build, curate, and open-source a dataset of such requests varying the power domain, the context, the scale of the affected party, and the prior power standing of the user, and evaluate 24 models (12 from US and 12 from Chinese developers) under three experimental conditions: reciprocal nationalities of user and affected party, an AI agent as the user, and 8 request languages. Models refuse power grabbing more than disempowerment, and disempowerment more than self-empowerment. Refusal of power grabbing rises with the scale of the affected party, from an individual to a society. Models are biased toward helping others take power from the US and against helping US users take power from others, but favor the US when it gains power and nobody loses it. When the user is an AI agent, refusal of power-shifting requests increases, especially in power grabbing against an individual. Finally, language biases refusal, but in model-specific ways that largely cancel on average. We release PowerBench to make these asymmetries measurable in current and future models.

---


### 7. [DeskForge: Dense Supervision from Desktop Environments for Computer-Use Agents](https://arxiv.org/abs/2610.02320)

**<font color=#1a73e8>作者：</font>** A. Said Gurbuz, Ahmed Nassar, Sunghwan Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer-use agents need to reliably ground action targets in complex desktop scenes, where multiple applications, overlapping windows, and visually similar controls compete for attention. Existing training data rarely pair such scenes with dense annotations or vary them in a controlled way. We introduce DeskForge, a controllable desktop environment that composes and explores real applications to generate large-scale supervision for computer-use agents. It varies application states, content, window layout, appearance, and resolution, and fuses screenshots, accessibility trees, and window geometry into dense element annotations while recording the outcome of each executed action. Using this environment, we construct DeskForge-1M, a corpus of 1.2M annotated desktop observations containing 159.7M element instances. We fine-tune four vision-language models on 200K grounding examples drawn from DeskForge-1M. All four improve across held-out desktop conditions and on all five external GUI grounding benchmarks; for Qwen3.5-4B, accuracy increases by 11.51 percentage points on ScreenSpot-Pro and 10.11 points on OSWorld-G. The gains also translate to long-horizon task completion: under a fixed planner, the fine-tuned action models solve more WebArena-Infinity and OpenApps tasks, with Qwen3.5-4B increasing from 31 to 50 of 119 tasks and from 3 to 15 of 100 tasks, respectively. These results show that controllable composition of real desktop environments provides a scalable source of supervision for improving both GUI grounding and long-horizon computer use. The framework code, the dataset, and the fine-tuned model are available from the project page: this https URL

---


### 8. [Slow-Fast Multi-Teacher On-Policy Distillation for Capability Preservation](https://arxiv.org/abs/2610.02324)

**<font color=#1a73e8>作者：</font>** Xiaofei Yin, Tong Chu, Jiyuan Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation multimodal large language models are designed to support a broad spectrum of capabilities across diverse domains. Multi-teacher on-policy distillation (MOPD) provides an effective framework for consolidating domain-specific expertise into a single student model. However, MOPD training gradually drives the student away from its initialization model, and general capabilities decline as the displacement grows, resulting in capability interference. A direct remedy is constraining the student toward its initialization, but this suppresses the acquisition of domain expertise as well. We propose Slow-Fast Multi-Teacher On-Policy Distillation (SF-MOPD), which couples a fast model, the current student updated directly by each teacher, with a slow model, an exponential moving average of the student. The slow model absorbs the learning signal gradually, serving as a moving capability reference that fuses the general foundation with confirmed domain expertise. For each teacher, SF-MOPD computes the teacher-induced update in log-probability space and removes only the component that pushes the fast model further away from the slow model, while retaining aligned and orthogonal components. Experiments across multiple model scales demonstrate that SF-MOPD effectively mitigates capability interference, enhances specialized multimodal capabilities, and reduces the average degradation on general-capability benchmarks, consistently outperforming vanilla MOPD.

---


### 9. [Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2610.02330)

**<font color=#1a73e8>作者：</font>** Yu Li, Zheng Zhang, Xin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) rely on long-horizon tool invocation sequences for complex tasks, where each invocation can alter the task state and condition subsequent decisions. In long-horizon tool use, final-outcome rewards provide weak credit assignment over long interaction traces. Step-level rewards can offer more targeted feedback, but obtaining reliable step supervision often requires human or LLM judgment, or additional rollouts to estimate the downstream effect of an intermediate decision. In this paper, we argue that effective tool-use agents should estimate the long-horizon value of a possible next tool invocation before executing it. This objective requires comparative supervision over alternative invocations under the same context, while logged trajectories only contain the invocation that was actually taken. Therefore, we propose Comparative Inference for Tool-use Agents (CITA). CITA trains a Comparative Inference Model (CIM) from paired signals that combine observed tool behavior, scalable supervision from a Bayesian tool-graph simulator, and semantic judgments from LLM-based comparison. The resulting CIM learns to estimate how likely a possible next tool invocation is to support final task success under the current context. Across three tool-use benchmarks and multiple backbone LLMs, CITA consistently improves Tool F1 and task success. Additional analysis shows that CIM learns accurate step-level value estimates for comparative tool choices.

---


### 10. [World Editing: Intervening on Executable Worlds at Increasing Depth](https://arxiv.org/abs/2610.02331)

**<font color=#1a73e8>作者：</font>** Max Ku, Nok-Kan Law, Yu-Chien Tang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive world models are increasingly capable of generating environments and acting within them, yet deliberately editing an existing executable world remains underexplored. We formulate world editing as intervening on an existing world while preserving properties that should remain unchanged, and introduce intervention depth as an axis describing how strongly an edit couples world entities, dynamics, and systems. We instantiate this capability through industry-grade game modding and introduce IGMWorld, together with IGMBench, a benchmark of 110 tasks and over 1.1K executable state and behavioral criteria across Minecraft and Terraria. The tasks span property, entity, dynamics, and system interventions and are evaluated through deterministic executability, behavioral, preservation, and visual checks. Frontier coding agents already exhibit substantial world-editing capability: the strongest configuration solves 78.2% of tasks under a strict task-level criterion, while criterion-level performance reaches 94.8%. Reliability generally decreases with intervention depth, and this pattern persists even among tasks with similar numbers of evaluation criteria. Most failed edits still build and load successfully, suggesting that the main difficulty is making the edited world behave as requested. Visual consistency remains a separate weakness, with all evaluated configurations below 50% joint visual pass rate. These results show that world editing is a distinct capability from world generation and interaction, and that executable games provide a practical testbed for studying it.

---


### 11. [MIRROR: Multipath Quorum Integrity for LLM Multi-Agent Communication](https://arxiv.org/abs/2610.02349)

**<font color=#1a73e8>作者：</font>** Ryuichi Yamafuji Lun, Jingzhen Wang, Shreyas Kolte 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Inter-agent communication is central to Large Language Model Multi-Agent Systems (LLM-MAS), but it introduces an underexplored vulnerability: Agent-in-the-Middle (AiTM) attacks that manipulate messages in transit without compromising the agents themselves. Prior work reports Attack Success Rates (ASR) approaching 100% on structured tasks. Existing defenses rely on semantic validation, which requires additional inference and can block benign outputs, or on transport-layer encryption, which does not help when an intermediary legitimately terminates TLS. We present MIRROR, a communication-layer integrity primitive that replicates a single canonicalized payload across k logical routes and accepts a message only when a strict majority of routes report the same digest. MIRROR uses unkeyed hashing and so authenticates nothing on its own, since an active on-path adversary can always recompute a digest over a payload it has modified. All integrity derives from the assumption that honest routes form a majority. The digest serves only to make witness routes constant-size and to bind the recovered payload to the quorum-agreed value under second-preimage resistance. We give the guarantee under a route-compromise bound alpha < 0.5, and extend it to correlated routes, where the quantity that matters is the size of the largest shared-failure group and not the route count. We further show that availability and integrity degrade at the same threshold: below alpha = 0.5, quorum-denial and message-dropping adversaries cannot block honest traffic. Across MMLU, HumanEval, and MBPP on two frameworks and four communication topologies, and in a MetaGPT deployment against a production API, MIRROR reduces ASR to 0% below the threshold at 1x LLM token cost. LLM-as-a-Judge costs 35x in the same deployment, and blocks up to 44.2% of benign outputs in the topology sweep.

---


### 12. [DeReAct: Decomposed Reasoning and Acting for Reliable AI Agents](https://arxiv.org/abs/2610.02351)

**<font color=#1a73e8>作者：</font>** Ajay Vohra, Tao Chen, Neeti Narayan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> ReAct-based agents typically rely on a single LLM policy to propose actions, interact with the environment, and decide when a task is complete. This coupling makes action authorization and completion control difficult to enforce independently, allowing errors to propagate and unsupported completion claims to terminate execution. We introduce DeReAct, a modular agent architecture that externalizes two gating policies: a Critic that validates proposed actions before execution, and a Context Manager that reconstructs an environment-supported \textsc{State} and certifies task completion.
Across GAIA and SWE-bench Verified, DeReAct improves Pass@1 most for weaker Brain models, with gains of 6.5--7.0 points for Qwen3-Coder-480B and 4.2--5.2 points for Claude Sonnet~4.5; gains diminish as Brain capability increases. Trajectory and ablation analyses show that external gating is effective when targeted failures are sufficiently prevalent and the gating policy is itself sufficient. With Claude Opus~4.5, Pass@1 remains comparable to ReAct, while DeReAct produces more evidence-complete and constraint-satisfying trajectories, indicating that completion control can trade earlier termination for stronger grounding. Overall, DeReAct improves weaker agents while retaining grounding benefits as models strengthen.

---


### 13. [Does Every User Need a Private LoRA? Decoupling Personalization from Per-User Adaptation](https://arxiv.org/abs/2610.02353)

**<font color=#1a73e8>作者：</font>** Songyuan Sui, Srikanth Malla, Chiho Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized large language models often require a complete adaptation state for each user. However, this paradigm scales poorly as the user population grows. We revisit this design through the lens of personalization capacity allocation: how much adaptation capacity can be shared across users, how the shared capacity should be composed, and how much must remain user-specific. We answer them through three complementary empirical analyses. We find that independent user adapters contain substantial cross-user reusable structure, that the utility of reusable directions reflects both user relevance and variation across queries, and that user histories provide transferable signals for compact individual correction. Motivated by these findings, we propose LINEUP. It learns a bank of reusable low-rank personalization factors, composes them through user-conditioned recall and query-dependent calibration, and restricts target-user adaptation to a tiny user code over a shared correction space. This design decouples expressive personalization capacity from per-user trainable state. Each target user optimizes only eight scalars, while all shared components remain fixed. By comparison, the evaluated private-LoRA configuration uses 4.19 million per-user parameters. Our theoretical analysis gives a finite-step, finite-history risk bound and sufficient conditions for user-code refinement to improve on history initialization. Across six tasks spanning personalized classification, prediction, and generation, LINEUP leads on all 12 metrics, each averaged over three independent runs (e.g., reducing LaMP-3 RMSE by 11.4% relative to the strongest baseline). It maintains advantages under limited history. These results show that rich personalization can be supported primarily by reusable, conditionally composed shared capacity, while independent user adaptation remains confined to a tiny correction state.

---


### 14. [Why Does Adaptive Batching Help LLM Pretraining? A Perspective from Unbounded Variance](https://arxiv.org/abs/2610.02355)

**<font color=#1a73e8>作者：</font>** Arda Fazla, Antesh Upadhyay, Ege C. Kaya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Increasing the batch size during training is a common practice in large language model (LLM) pretraining, yet the theoretical justification behind its success is not well understood. Analyses of stochastic optimization often assume uniformly bounded stochastic gradient variance, yet recent evidence suggests that this assumption fails in many practical nonconvex problems. The Blum--Gladyshev (BG-$0$) noise model relaxes this assumption by allowing the variance to grow quadratically with the distance from initialization, suggesting that batch size schedulers can help by controlling the variance growth during training. However, this growth can be overly conservative in practice. We empirically investigate variance growth in LLM pretraining and observe that a generalized BG model with a tunable growth exponent provides a tighter description of practical noise behavior. Motivated by this observation, we introduce the generalized BG-$a$ noise model, which interpolates between bounded variance ($a=0$) and BG-$0$ noise ($a=2$). Under $L$-smoothness, we derive an information-theoretic lower bound with growth-dependent oracle complexity $\Omega(\epsilon^{-(4+a)})$ and establish a matching upper bound in $\epsilon$-dependence by increasing the batch size as the iterates move away from initialization. Finally, we propose an adaptive batch scheduler that controls variance growth through dynamic batch size adjustments during training. In pretraining OLMo2 models of up to 1B parameters on C4, our scheduler achieves a lower validation loss than both small and large batch training under matched token budgets, while using less than 10\% of the iterations of small batch training.

---


### 15. [Lexicographic Multi-Objective On-Policy Distillation](https://arxiv.org/abs/2610.02359)

**<font color=#1a73e8>作者：</font>** Doseok Jang, Jon Ander Campos, Youran Qi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards (RLVR) usually optimizes answer correctness, yet useful language-model behavior also requires high-quality reasoning and concise responses. Existing multi-reward post-training methods typically scalarize rewards or combine specialists without explicitly protecting a reward priority order. This is problematic when trade-offs are asymmetric: conciseness, for example, should not improve at the cost of correctness. We introduce Lexicographic Multi-Objective On-Policy Distillation (LMOPD), a multi-teacher method for integrating reward-specialized policies under explicit priorities. For each student rollout, LMOPD selects the specialist for the first objective whose gate detects a deficiency, then locally projects its centered log-policy correction to remove components that oppose higher-priority specialists. We evaluate 30B-A3B mixture-of-experts transformer models in two- and four-expert settings on three math benchmarks, measuring retained specialist gains. With two experts, LMOPD's point estimates fully retain the accuracy and reasoning-quality gains while acquiring $46.9\%$ of the conciseness gain. With four experts, it retains $\approx90\%$ of both the accuracy gain and reasoning-correctness gain, compared to only $\approx57\%$ by the next best evaluated baseline. Matched four-expertablations show that lexicographic routing outperforms random routing and that projection further strengthens both top-priority capabilities. Across both scales, LMOPD preserves the highest-priority capabilities more effectively than the existing baselines we evaluate, demonstrating the value of explicit priorities for specialist integration.

---


### 16. [Automating the Application of HCI Principles: Skills for On-Demand UI Construction, the Human-AI Space to Think, and the Future of HCI](https://arxiv.org/abs/2610.02369)

**<font color=#1a73e8>作者：</font>** Nathan Conklin, Miranda Capra, Chris North  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-computer interaction (HCI) is in the middle of a transition: large language models can now generate functional user interfaces (UIs) on demand from natural-language task descriptions. A user explains what they are trying to accomplish, and the system materializes a working interface to support it. This capability already exists in systems such as Claude and ChatGPT and continues to grow in fidelity as the underlying models improve. The next step along this trajectory is to move from interfaces that are merely generated to interfaces that are generated well. We propose a framework in which the dialogue between user and artificial intelligence (AI) becomes a Space to Think: a shared, structured cognitive workspace in which task decomposition produces an on-demand user interface as an extension of the user's thinking rather than as a separate artifact. Within this paradigm, classical HCI design knowledge (Nielsen's heuristics, Norman's affordance prescriptions, Web Content Accessibility Guidelines (WCAG) success criteria, cognitive-load constraints, and mixed-initiative principles) is encoded as skills: machine-readable this http URL files that the generating agent loads at runtime as software engineering tools. Skills turn HCI design knowledge into declarative, inspectable, version-controlled, and editable artifacts owned by the HCI community itself so that accessibility, learnability, and consistency become properties of a generative process rather than properties of a finished product. We outline a research agenda depicting a future where the HCI field transitions from today's design and knowledge heuristic checklist towards a future where the craft becomes machine-readable, executable, and open.

---


### 17. [Hop-Decayed Influence: New Vulnerabilities of Structural Auxiliary Indexing in GraphRAG Pipelines with LLM](https://arxiv.org/abs/2610.02373)

**<font color=#1a73e8>作者：</font>** Jisung Park, John Le, Heath Cooper  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> GraphRAG pipelines construct auxiliary structures during offline indexing--semantic summaries, hierarchical edges, and pre-computed scores--that determine how retrieval is prioritised at query time. Prior attacks target only instance-level components (nodes, edges, triples), overlooking these schema-level structures. We formalise Auxiliary Schema-Level Entity as a novel attack surface and propose the 3S Framework (Semantics, Structure, Scoring) for its systematic exploitation. Our Hop-Decayed Influence (HDI) attack identifies high-impact targets through query-aware influence propagation and corrupts their auxiliary structures post-indexing. Across two benchmarks (HotpotQA, 2WikiMultiHopQA) and two architectures (Microsoft GraphRAG, HippoRAG2), HDI achieves 88-94% attack success rate while modifying as few as 0.016% of auxiliary structures. Each modification affects up to 6.00 queries (Schema Leverage Ratio), demonstrating 1:N amplification unavailable to instance-level attacks. Manipulated structures evade perplexity and paraphrase defenses with over 99% evasion rate, as they remain linguistically coherent system-generated artifacts. These results reveal that auxiliary schema-level entities receive implicit trust without runtime validation, constituting a structural blind spot in current GraphRAG defenses. this https URL.

---


### 18. [EviDent-CBCT: Evidence-Bottlenecked Report Generation from Dental CBCT under Non-Exhaustive Report Supervision](https://arxiv.org/abs/2610.02375)

**<font color=#1a73e8>作者：</font>** Ruiyang Hao, Zhi Qin Tan, Yulan He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dento-maxillofacial cone-beam CT (CBCT) reports may contain dozens of tooth-specific, anatomical, and spatial findings from a single 3D scan. Learning to generate such reports from limited clinical data is challenging because routine reports may not exhaustively document image findings, and a non-mention may reflect either absence or non-reporting. We present EviDent-CBCT, an evidence-bottlenecked framework designed for this incomplete supervision. An anatomy-aware network maps each CBCT scan to a discrete record of tooth-level, global, and tooth-IAC evidence. A dental-logic consistency projection reconciles incompatible evidence before a deterministic renderer and an image-blind local language model generate the report using only this record. For tooth-level evidence, reliability-aware training uses eligible non-mentions as reduced-weight negatives, while unreported global and tooth-IAC labels remain unknown. A metal-sensitive input channel preserves intensity cues from dental materials. Across three validation runs, EviDent-CBCT achieves $0.666\pm0.006$ merged evidence set-F1 and $0.402\pm0.003$ RadFact-Lite-Dental logical-F1, versus $0.371\pm0.018$ for the strongest controlled direct baseline. In the ODIN 2026 challenge, it ranked second in automated evaluation and third in blinded clinical Arena comparison on the hidden test set. These results support the discrete evidence record as an effective and auditable interface for CBCT report generation.

---


### 19. [THPL: A Vision-to-Language Decision Support Framework for Rainbow Trout Feeding Management in RAS](https://arxiv.org/abs/2610.02378)

**<font color=#1a73e8>作者：</font>** Meng Liang, Guanbo Feng, Haozhuang Chi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In Recirculating Aquaculture Systems (RAS), precision feeding is critical for minimizing costs and improving fish welfare. However, existing methods lack cognitive alignment between fish behaviors and management knowledge, impeding translation into executable, interpretable feeding decisions. To address this, we propose THPL, a generative feeding decision framework tailored for rainbow trout (Oncorhynchus mykiss) in RAS. First, Fishsort extracts trajectories to establish an Activity Coefficient (AC) quantifying feeding intensity. Second, a Hierarchical Behavior Encoder (HBE) models individual temporal progression and collective dynamics using Temporal and Set Transformers, transforming trajectory tensors into dual-evidence representations of explicit physical and implicit soft tokens. Finally, these tokens are integrated with environmental parameters, metadata, and expert rules to fine-tune an LLM via LoRA, followed by counterfactual multimodal Direct Preference Optimization (mDPO) to reinforce causal reasoning. Results show that AC exhibits a statistically significant monotonic positive correlation with expert-annotated feeding intensity (Spearman $\rho = 0.925$, $p < 0.001$). Ablations indicate that decision accuracy improves from 33.33% (text-only baseline) to 93.33% with dual-evidence tokens, confirming that continuous spatiotemporal tokens provide necessary physical grounding for LLMs. Compared with standard LoRA, counterfactual mDPO elevates decision accuracy from 93.33% to 96.67%, advances METEOR from 58.10% to 85.30%, reduces Self-BLEU-2 from 58.79% to 52.88%, and increases Distinct-3 from 6.68% to 7.81%, suppressing templating and actuation biases while reinforcing causal consistency and operational safety. Overall, by integrating continuous kinematics with LLM reasoning, this study provides a novel decision support paradigm for precision aquaculture.

---


### 20. [Latent-MOPD: Latent Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2610.02381)

**<font color=#1a73e8>作者：</font>** Zhengyu Fang, Seoyeon Hong, Jie Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on the responses it generates. Existing LLM multi-teacher OPD transfers what specialists predict through their output distributions. We introduce Latent-MOPD, to our knowledge the first representation-level multi-teacher OPD method for LLMs. It integrates existing specialists through both their predictions and the hidden states used to compute them, without additional teacher training. To coordinate representation supervision from multiple specialists, we select late-layer targets according to the teacher-student relationship, bridge unequal hidden widths with a shared projection, and group updates by domain. Each teacher's supervision gradually shifts from hidden states to token predictions, with both channels using the same routed specialist. In our main same-family setting, Latent-MOPD outperforms the token-only, representation-only and uniform-averaging baselines on all nine benchmarks across math, code and logic. With the same parameter count as each teacher, the student also surpasses the per-benchmark best teacher on a majority of these benchmarks. With larger, separately developed cross-family teachers, Latent-MOPD outperforms both single-channel baselines on all benchmarks. A same-family all-layer representation-only control remains stable with domain-pure updates but collapses when teacher domains are interleaved within an update. Our results show that a single student can integrate capabilities from several specialists through both their output distributions and internal representations.

---


### 21. [The Surprising Effectiveness of Shared Memory in Looped Transformers](https://arxiv.org/abs/2610.02383)

**<font color=#1a73e8>作者：</font>** Giovanni Monea, Keshav Ramji, Yousef El-Kurdi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers apply the same layers several times per token, adding compute to improve quality without more parameters. Each recursion, however, writes its own key-value cache, so memory still grows with compute. Inference-time techniques can shrink this cache at a cost in quality. We pretrain looped language models to share memory: only the first recursion writes a cache, and later recursions read it while keeping a short window of their own. Surprisingly, we find that sharing memory does not cost quality and instead improves it. At 150M-1B parameters, our Looped Prediction Transformer (LPT) and its hybrid variant set a new quality-memory frontier for looped models: with five recursions, the hybrid lowers validation perplexity on FineWeb-Edu by 1.12-1.82 relative to a same-size standard Transformer while using 76-79% less context memory. Through an extensive analysis, we investigate why memory sharing helps. Shared and local memory develop different representations, and later recursions attend mostly to the shared memory, which also acts as a gradient highway to the first recursion.

---


### 22. [Octrees as an Explicit 3D Language](https://arxiv.org/abs/2610.02388)

**<font color=#1a73e8>作者：</font>** Ran Dan, Si-Tong Wei, Pengfei Xiong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D large language models (LLMs) compromise on two fronts: they compress shapes into latent codebook indices or coordinate text, which removes spatial structure from what the model observes, and they acquire the 3D modality by fine-tuning the backbone, which overwrites its general language ability. We present OctLLM, which addresses both limitations. Geometry enters as an explicit 3D sequence of octree occupancy tokens. However, full octree sequences grow rapidly with depth; OctLLM therefore randomly empties penultimate-level nodes and omits descendants while preserving shape, yielding a shorter coordinate- and depth-anchored Sparse Octree (S-Octree) for position-aware mask-modeling generation and 3D understanding. On the other front, existing methods introduce a new modality with full fine-tuning or LoRA, but full fine-tuning is costly, LoRA limits 3D capacity, and both modify the language pathway. OctLLM instead adds 3D capacity in parameters separate from the pretrained ones: mesh tokens are routed through independent trainable branches in a subset of blocks while text and image tokens retain the frozen vision-language pathway, and the two streams interact through shared self-attention. It trains far fewer parameters than full fine-tuning, yet sets a new state of the art among unified multimodal LLMs, lowering image-to-3D FID by $17.4\%$ and raising render-grounded captioning by $28.7$ points over ShapeLLM-Omni, while matching the backbone on general language benchmarks.

---


### 23. [Hesitation Has a Geometry: Entropy-Trained Hyperbolic Probes for Sparse Activation Steering](https://arxiv.org/abs/2610.02391)

**<font color=#1a73e8>作者：</font>** Zeyong Zhang, Tung Sum Thomas Kwok, Tengfei Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a large language model solves a mathematical problem, its reasoning is largely hierarchical, and the solution often branches at a few tokens where the next-token entropy is high. Such tree-like structure embeds in hyperbolic space with far lower distortion than in Euclidean space. Activation steering, however, usually edits the hidden states of a pretrained model by adding one fixed Euclidean vector at every token, even though most tokens of a solution are already determined by the context. We propose Hyperbolic Entropy Steering (HEST), which embeds the hidden states in the Poincaré ball with a lightweight probe whose only label is the model's own next-token entropy. Where this entropy exceeds a threshold, HEST moves the embedded state along the geodesic of steepest descent of a readout of the probe and maps the change back to the hidden state. For the Busemann readout of a learned ideal point, we prove that a step of fixed length lowers it by the same amount at every state. On three instruction-tuned models from the Qwen2.5-Math and Llama-3.1 families, HEST with the Busemann readout improves greedy accuracy on MATH-500 and GSM8K in five of six settings, by up to 1.8 points, whereas a contrastive steering vector added at every token lowers accuracy. With a Euclidean probe trained in the same way, this gain disappears on Qwen2.5-Math-1.5B-Instruct. The gains are largest on problems where the model hesitates often, and accuracy on the remaining problems is almost unchanged.

---


### 24. [Inherit-MAS: Test-Time Evolution of Multi-Agent Systems through Workflow and Execution Inheritance](https://arxiv.org/abs/2610.02396)

**<font color=#1a73e8>作者：</font>** Songtao Wei, Yi Li, Zhichun Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) built from large language models coordinate specialized agents to tackle complex tasks, but effective workflows are difficult to design in advance. Test-time evolution refines workflows using execution feedback, yet broad revisions can disturb useful components, while re-executing unchanged requests can incur redundant computation. Inspired by the interplay of inheritance and selection in biological evolution, we introduce Inherit-MAS, which makes inheritance explicit at the workflow and execution levels. A meta-model first synthesizes a workflow of worker agents with declared roles, communication inputs, and tool permissions, and a separately prompted judge scores each executed candidate and diagnoses its deficiencies. In ordinary refinement rounds, \emph{workflow inheritance} starts from the latest completed candidate, may discard removable nodes judged unhelpful, and applies a validated edit to address the diagnosed deficiency. When the new candidate executes, \emph{execution inheritance} inherits eligible stored results only if the complete resolved request and execution context match, avoiding redundant model and tool calls. With GPT-4o-mini workers, Inherit-MAS achieves 55.4\% completion on WorkBench and 49.7\% joint F1 on HotpotQA FullWiki, outperforming EvoAgent, EvoMAS, and TacoMAS. With Qwen3-32B workers, it also exceeds these evolving-MAS baselines on both benchmarks. Compared with rerunning the same controller with execution inheritance disabled, execution inheritance reduces worker-token usage by 29.1\% on WorkBench and 34.6\% on HotpotQA, and total token usage by 5.3\% and 18.1\%.

---


### 25. [Trained Agentic Context Management](https://arxiv.org/abs/2610.02404)

**<font color=#1a73e8>作者：</font>** Bryce Sandlund  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study long context language models. Instead of training long context natively, or designing a long context harness, we train a model over the simplest possible harness: a tool to call itself with any specified prompt and a tool to read tokens in a range from the input context. We finetune Qwen3.6-35B-A3B on a diverse synthetic dataset using this harness. With only 8,000 tokens of context, our small model is as strong as GPT-5.4 with 1M tokens of context on the OOLONG-synth benchmark when document length exceeds 40K tokens.

---


### 26. [When Terminal-Agent Training Stalls: Demystifying Data Generation and Verification Challenge](https://arxiv.org/abs/2610.02405)

**<font color=#1a73e8>作者：</font>** Xi Qin, Isabel Kurth, Xin Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Using a frontier model like Claude Opus as a meta-agent to generate terminal tasks and verifiers for RL training is increasingly common. Yet a runnable Docker image and executable test suite do not guarantee a faithful end-to-end pipeline for terminal agent training. We present a meta-agent pipeline motivated by this gap, diagnosing three classes of failure: benchmark invalidity, harness brittleness, and reward misalignment. Prompt redesign and context extension raise baseline solvability 5.6 times, but a 9B model saturates at 81.3% mean pass@2 within 20 steps on Claude Opus-generated tasks. Adding hard tasks reduces mean pass@2 to 20.6% without changing the training configuration, a strong evidence that the solvability band is model-specific. These findings demonstrate that meta-agent reliability requires solvability-band calibration, verifier audits, and infrastructure error accounting as first-class evaluation criteria, not post-hoc diagnost.

---


### 27. [Finding the Move Is Not Winning the Game: XiangqiBench for Closed-Loop Evaluation of LLM Agents](https://arxiv.org/abs/2610.02425)

**<font color=#1a73e8>作者：</font>** Yekun Chai, Qiwei Peng, Haoyi Xiong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Static evaluations credit a language model for naming the right move, but an agent must carry a plan through to a verified outcome while an opponent responds. We introduce XiangqiBench, an executable benchmark that measures this difference in Chinese chess: starting from 119 tactical endgames with forced mates supported by engine or checks-only search, an LLM agent must deliver checkmate against an engine defender. An interactive REPL interface separates real moves, state queries, and forward simulation, and we record 8,568 multi-turn trajectories from 12 frontier LLMs under two observation protocols. Three signals that look like competence each overstate closed-loop success. (i) The Conversion Gap: models play the stored reference first move in 26.1\% of Sighted trials, yet only 13.9\% of these trials end in a win. (ii) The Consistency Gap: the leading model reaches 38.7\% pass@3 but only 5.9\% pass^3, winning all three trials on 7 of the 46 positions it ever wins. (iii) The Simulation Gap: 32.3\% of accepted simulation calls stop on an illegal move, and in 49.3\% of comparable cases the real defender replies differently from the line the agent simulated; self-authored rollouts check legality but cannot anticipate the opponent. Finding the move is not winning the game: agent evaluations should score closed-loop outcomes and report reliability alongside coverage.

---


### 28. [Evaluating and Improving the Robustness of Large Language Models to Input Sequence Variations](https://arxiv.org/abs/2610.02432)

**<font color=#1a73e8>作者：</font>** Narek Maloyan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) in production systems face prompt injections, trojans (backdoors), and manipulation of automatic quality metrics. This thesis develops models, methods, and algorithms for evaluating and improving LLM robustness to adversarial input sequence variations. We propose R_stab(f), a generative robustness metric based on the Jensen-Shannon divergence between per-step output distributions under small input perturbations. For localized attacks we prove V(h) <= 1 - R_class(h), where R_class(h) is the probability that a decision operator h keeps its decision under small perturbations. For non-localized attacks we propose a calibrated empirical model. For LLM-as-a-Judge systems we develop ASA, an adaptive evolutionary black-box attack that reaches an attack success rate (ASR) of up to 73.8%, with transfer between open models up to 62.6%. On Trojan Detection Challenge 2023 data (Pythia-1.4B), surrogate triggers reach REASR ~0.99 while recall of the true triggers is ~0.17 against a baseline of ~0.14. On SaTML CTF 2024 we systematize four classes of bypasses of multi-layer defenses, which reduce the ASR from 90% to 15-25%. Committees of 5-7 heterogeneous models reduce the ASR for Gemma-3-4B by 47-55 percentage points, to 19.3% with 7 models. For agentic systems based on the Model Context Protocol (MCP), we propose AttestMCP, which attests tool calls with HMAC-protected packets at under 0.1 ms per call, and the Commit Boundary isolation pattern. On the MCPBench benchmark of 847 scenarios they reduce the average ASR from 53.7% to 12.4%. The methods are implemented in the JudgeGuard and TrojanArmor software suites and the MCPSec module.

---


### 29. [Are you Synthesizing or Recalling? Evaluating LLMs on Algorithmic Code Retrieval](https://arxiv.org/abs/2610.02438)

**<font color=#1a73e8>作者：</font>** Nickil Maveli, Antonio Vergari, Shay B. Cohen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong performance in code generation, where success depends on both recalling relevant algorithmic knowledge and reasoning about how to apply it. However, existing LLM pipelines are opaque, with no explicit separation between these two components. We argue that for well-known algorithms whose canonical implementations are widely accessible in pretraining corpora, code generation is better measured as \textit{parametric code retrieval}: reproducing a named algorithm from internalised knowledge rather than synthesizing a novel one. We introduce AlgoREval, a benchmark of 599 problems spanning classical 77 algorithms across 14 domains, 7 programming languages, and 4 graph-input representations to evaluate this capability in isolation, and assess 15 models (7B--34B parameters) in a zero-shot setting. We find substantial variation in retrieval accuracy across languages and input representations, even for widely documented algorithms and show that prompt augmentation with retrieved code snippets or structured algorithmic hints improve accuracy on complex algorithms, while SFT achieves broader language gains and GRPO achieves larger per-language gains on specific languages. Together, our results establish parametric code retrieval as a distinct, measurable capability and caution against deploying AI-generated algorithmic code without systematic validation.\footnote{Code and dataset are available at this https URL

---


### 30. [AI-driven Thermal-aware Data Center Capacity Planning](https://arxiv.org/abs/2610.02442)

**<font color=#1a73e8>作者：</font>** Yixing Li, Mark Fenton, Matthew Kaufeler 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The emerging of large language models (LLMs) has posed significant challenges to the thermal management of data center. Intense GPU computation for LLMs results in localized hotspots. Moreover, spiking thermal loads during training and inference bursts make real-time cooling response more difficult to predict and control. Thermal-aware capacity planning of data center requires massive expensive high-fidelity CFD simulations. AI models can perform real-time prediction for unseen designs. However, existing works either have large prediction error, or have over-simplified assumptions for data center operations. This work presents an AI-driven framework that can perform thermal-aware capacity planning for a real-world data center in seconds. The embedded AI model learns from numerous key parameters (rack power, server power, server placement, HVAC settings etc.), and provides temperature prediction within milliseconds. This AI model is tested against high-fidelity CFD simulations, and results show that for unseen data center designs, model can achieve high accuracy with 10000X speedup. Driven by the AI model, the authors design the thermal-aware capacity planning framework. This framework can help data center designers and operators instantaneously optimize both workload distribution and HVAC cooling efficiency.

---


### 31. [Counterexample Generation via Per-Theorem Symbolic Verifiers: When Imitation Hurts and Reinforcement Repairs](https://arxiv.org/abs/2610.02444)

**<font color=#1a73e8>作者：</font>** Omar Farouk Zouak, Houssam Eddine Boukhalfa, Soumaya Lakehal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often solve a theorem forward yet fail to disprove a closely related false one: a falsification gap that supervised fine-tuning does not close and can actively worsen. We frame counterexample generation as constrained witness emission against a deterministic per-theorem Python verifier, and release SymCE, a corpus of 4,707 false undergraduate-algebra and real-analysis conjectures, each paired with executable verifiers. The verifier also serves as the reward function, making SymCE a training environment. Training Qwen3-4B with SFT followed by GRPO under this oracle reveals an imitation trap: counterexample-only SFT collapses true-theorem recognition from 0.27 to 0.00, while RLVR with a sparse outcome-only reward repairs this and exceeds the base, to 0.66. The collapse replicates across four seeds and on Gemma-3-4B. Sparse and dense rewards yield statistically indistinguishable in-domain success yet diverge by 33 points on a held-out calibration probe, a dissociation we trace to the partial-credit term. Our 4B model outperforms every evaluated 7B open-weights math specialist, remains competitive with six frontier commercial APIs, and transfers under unchanged prompting to GSM8K, MATH-500 and MMLU-college-math. A human audit of 177 verifier decisions finds 97.7% accuracy. Code, data, verifier modules and annotations: this https URL.

---


### 32. [A Simulation-Grounded Agentic VLM Framework for Wildfire Monitoring and Reporting](https://arxiv.org/abs/2610.02451)

**<font color=#1a73e8>作者：</font>** Duowen Chen, Yuchen Sun, Zhiqi Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective wildfire monitoring requires relating visual evidence to physical fire dynamics, yet real videos with synchronized physical annotations are scarce and high-fidelity 3D simulation is costly. We present a simulation-grounded vision-language model (VLM) framework that automatically converts 2D wildfire simulations into labeled video episodes. A fixed Blender mapping produces low-detail 3D proxies aligned with simulator terrain, fuel layout, fire activity, and wind cues; controllable video generation supplies richer appearance. The proxies are intermediate representations rather than finely rendered final scenes. Generated videos and simulator labels form reusable multimodal memory for a training-free multi-agent VLM system that retrieves reference episodes, reconciles visual and memory-based predictions, and produces structured wildfire reports. On held-out generated episodes, video memory achieves 51.5% exact four-tag accuracy, compared with 22.6% for direct VLM querying and 16-17% for text-only memory; the complete system achieves 77.3% accuracy on six simulator-derived report fields. Component ablations, cross-generator tests, and three real-UAV evaluations assess retrieval, reporting, generator changes, and observable monitoring tasks. The framework connects automatic simulation-to-proxy conversion with memory-based VLM reasoning under scarce real-world physical annotations.

---


### 33. [FinDialogLens: Event Extraction over Multi-Party Dialogue for Missed-Trade Identification in Financial Chatrooms](https://arxiv.org/abs/2610.02455)

**<font color=#1a73e8>作者：</font>** Chin-Lun Fu, Hong Ni, Behrouz Madahian  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-party financial chatrooms are vital for sales-and-trading professionals, but their complexity makes manual recovery of missed trades infeasible: each Request for Quote (RFQ) is an event whose final price and trade outcome appear many messages after the RFQ-trigger message (the inquiry message), interleaved with concurrent RFQs from other participants. We cast this as event extraction (EE) over multi-party dialogue and present FinDialogLens, a hybrid LLM pipeline in which compact fine-tuned classifiers act as inference-time scaffolds: they detect RFQ-triggers and price/trade outcome metadata, an RFQ-Level Module segments per-event RFQ windows, and a Trade Engine fills argument roles. With GPT-4o, FinDialogLens reaches 92.1% and 94.3% accuracy on final price and trade outcome, respectively, outperforming full-chatroom CoT prompting methods; fine-tuned open-source LLMs with as few as 3B parameters achieve comparable performance with modest in-domain data. To make the LLM-based solution practical at scale, a difficulty-aware router balances cost and accuracy by allocating RFQs between a low-cost rule-based engine and the higher-performing LLM-powered Trade Engine, cutting LLM calls by 85% on final price while recovering half of the accuracy gap to FinDialogLens (GPT-4o), saving over $300/day at our 70,000-RFQ/day scale.

---


### 34. [SideKernel: A Usable microVM Sandbox for AI Coding Agents on macOS](https://arxiv.org/abs/2610.02456)

**<font color=#1a73e8>作者：</font>** Dimitrios Prasakis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI coding agents are untrusted system components, yet they require autonomy on the developer machines they run on. This contradiction is a security problem. Sandboxes provide an isolated environment, but for local macOS development, the existing local, open-source options for AI coding agents are few in number and cumbersome to use. I conducted a formative online user survey which indicates that fewer than 40% of AI coding agent users run their agents in a sandbox and identifies the top usability barriers hindering AI coding agent sandbox adoption. These findings are used to develop SideKernel: an open-source, local, microVM-based macOS sandbox for AI coding agents designed for usability. To evaluate SideKernel, I compiled a list of sandboxes available on the market and filtered it against five inclusion criteria. Then I performed a comparative analysis between SideKernel and the sandboxes that satisfy these criteria, across 23 capability tests derived from the usability barriers revealed by the user survey. I discovered that only a few sandboxes are similar to SideKernel, and that among those, Docker Sandboxes and SideKernel score highest on capability features related to usability. A secondary contribution of this paper is a survey of the existing solution space for local, open-source, microVM-based macOS sandboxes for AI coding agents.

---


### 35. [CUEing User Simulators: Calibrated User Embeddings for Multi-Turn Benchmarking](https://arxiv.org/abs/2610.02460)

**<font color=#1a73e8>作者：</font>** Anjali Kantharuban, Jonas Mueller  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent benchmarks rely on user simulators to evaluate AI agents in multi-turn interaction. While existing simulation techniques demonstrate surface fidelity to human style and behavior, ecologically valid interactive benchmarking also requires alignment in when and how agents fail across simulated and real user populations. We find that existing simulators lack outcome calibration: agreement with observed success rates and failure patterns when real users interact with the same agent. We introduce Calibrated User Embeddings (CUE), a framework that both encodes observed sessions and samples continuous representations, then decodes them into persona commands to steer LLMs to act as user simulators without training. Through this, we evaluate user-conditioned replay of past sessions and aggregate metric agreement when sampling novel personas for the same tasks. On $\tau^2$-Bench, CUEd simulators commit fewer simulator-attributed errors and more faithfully reproduce real-user agent failure modes, aggregate success rates, and outcomes for specific task-user pairs than other persona-based simulation methods. These gains coexist with competitive user fidelity as measured using metrics established in prior work. After being fit to mostly customer support interactions, the same CUEd simulators generalize to document creation, math tutoring, and casual conversation, and remain effective across different simulator LLMs without CUE retraining.

---


### 36. [Capability Scaling-Down Laws for LLM Compression](https://arxiv.org/abs/2610.02462)

**<font color=#1a73e8>作者：</font>** Xueqi Cheng, Liang Wu, Kelly Wan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM compression reduces inference costs and memory requirements, but selecting a method and configuration remains largely empirical because comparable resource reductions can produce different capability losses. We systematically investigate capability scaling-down laws for LLM compression across pruning, quantization, and distillation. Our framework measures capability loss in mathematics, code generation, and question answering, and relates these measurements to model size, training stage, compression settings, data availability, and training exposure. We develop simple predictive relations and evaluate their accuracy, measurement efficiency, and generalization to unseen configurations and model states. Sharing the density response across pruning levels halves the configuration measurements needed to fit a pruning predictor: on new Pythia states, on pre-registered OLMo-2 test states and under Wanda pruning, the compact relation matches a regression fitted with all measurements on math and code to within 0.020 nats per token, with coefficients refitted for each setting. Controlled distillation experiments show that the cost of heavy data reuse recurs across question-answering distributions, while the net benefit depends on the evaluation distribution. We further evaluate the decision value of these predictions by comparing numerical selection with configuration medians and fixed method priorities. Independent evaluations across two model families show that selection captures most of the available cross-method benefit for question answering within the tested candidate sets, where a fixed method priority attains the same regret, with smaller opportunities for mathematics and code. These results clarify the predictive scope of capability scaling-down laws and their use in compression method selection. Our code is publicly available at: this https URL.

---


### 37. [APDMem: Agent-Controlled Progressive Disclosure for Query-Adaptive Long-Term Memory](https://arxiv.org/abs/2610.02472)

**<font color=#1a73e8>作者：</font>** Chin-Lun Fu, Anagha Kulkarni, Hong Ni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized LLM assistants must recover sparse evidence from long conversation histories across queries of varying complexity. We introduce APDMem (Agent-controlled Progressive Disclosure Memory), a hierarchical long-term memory architecture that applies progressive disclosure to memory retrieval. Rather than relying on a flat memory store or fixed retrieval granularity, APDMem represents conversation history as four progressively detailed layers: thematic summaries, personalized key facts, turn-level evidence notes, and raw messages. At inference time, a controller applies progressive disclosure to the memory hierarchy: it first reads high-level summaries and drills into finer evidence only when needed. This creates an adaptive cost-fidelity trade-off: simple queries can terminate early, while complex temporal, multi-hop, or exact-evidence queries trigger deeper inspection. A note synthesizer converts retrieved evidence into a query-focused structure that consolidates facts, orders events, and flags contradictions before final answer generation. Experiments on LongMemEval show that APDMem achieves strong performance for long-context memory reasoning while accessing only 8% of the total conversations.

---


### 38. [Tropical Reinforcement Learning](https://arxiv.org/abs/2610.02478)

**<font color=#1a73e8>作者：</font>** Arip Asadulaev, Aladin Djuhera, Karim Salta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for large language models typically maximizes expected return, adding up the probabilities of all successful trajectories. However, the classical sum formulation can only report how often the model policy succeeds, not which solution actually worked, and because probabilities sum to one, reinforcing one solution can make the model forget another that was never shown to be wrong. This makes expected return a poor fit for compositional reasoning, where a solution must be assembled from reasoning steps that the model produces in separate, often failed, attempts but rarely produces together. To address this, we propose Tropical Reinforcement Learning, which rests on a simple change of algebra: instead of adding the probabilities of alternative solutions, we take their maximum, which yields the tropical semiring. The value of a state then becomes the log-probability of its most likely verified solution, together with an explicit path that can be replayed and reused. This enables true composition, since the best prefix and the best suffix meeting at a shared state can be joined even when they come from different rollouts. To put this into practice, we introduce TROPIC, a training algorithm for deterministic, resettable environments with verifiable outcomes. On four agentic tasks (Sokoban, Countdown, FrozenLake, WebShop), TROPIC outperforms the strongest on-policy baselines by up to 16 percentage points. Changing the algebra of reinforcement learning, not just its estimators, can thus substantially improve compositional reasoning in language models

---


### 39. [MEA: A Reward-Driven Multi-Agent System for Faithful Model Explanations](https://arxiv.org/abs/2610.02480)

**<font color=#1a73e8>作者：</font>** Yuyang Cheng, Raghav Kaushik Ravi, Srivarshinee Sridhar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent years have seen the employment of a plethora of machine learning (ML) models in high-stakes domains, but they remain largely opaque to the practitioners who act on their predictions. While post-hoc explanation methods offer a lens into this model behavior, wielding them effectively demands expertise most domain experts lack: navigating high-dimensional outputs, selecting the best explanations, and synthesizing evidence across disparate tools. To this end, we present MEA, a multi-agent framework that removes the explanation knowledge barrier entirely: a Proposer agent selects and configures explanation tools based on the question and modality, while an Actor agent is optimized end-to-end against faithfulness, transforming the outputs into natural language explanations grounded in model behavior across tabular, text, and vision modalities. Further, we introduce diverse question types spanning feature attribution, counterfactual reasoning, and spurious feature detection, each paired with a perturbation-based faithfulness metric. We find that frontier LLMs systematically produce unfaithful explanations. By optimizing against faithfulness rewards augmented with a modality-adaptive penalty, MEA consistently outperforms post hoc explainers, agentic, and closed-source baselines across six datasets, with reward-driven optimization yielding faithfulness gains of +28% (tabular), +21% (text), and +34% (vision) over the untrained backbone. More broadly, our findings suggest that AI agents themselves can serve as a scalable, adaptable interface to ML explainability, opening a path toward natural-language explainability that generalizes beyond the fixed, single-purpose tools that have long defined the field.

---


### 40. [Harnessing LLMs as Agents: What Does It Cost?](https://arxiv.org/abs/2610.02488)

**<font color=#1a73e8>作者：</font>** Zelin Zhao, Xinyu Guo, Jingyuan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language-model agents increasingly rely on harnesses that manage bounded context, persistent memory, tools, verification, and repeated execution, yet existing notions of model capability do not quantify the computational resources these mechanisms consume. We introduce the Language Model Agent Machine (LAM), a resource-bounded abstraction that fixes the underlying semantic model while explicitly charging harness-level resources. We establish four classes of results. Communication: LAM execution is instancewise equivalent to red--blue pebbling under simultaneous call--transfer budgets, transferring classical I/O lower bounds to context--memory traffic. Access: memory interfaces induce asymptotic separations, including a $\Theta(n)$ gap between random and non-speculative sequential access on pointer chasing. Recomputation: bit-reversal DAGs require $\Theta(n^2/(C+S)+n)$ model calls with context capacity $C$ and persistent-memory capacity $S$, quantifying when stored intermediate state avoids repeated semantic computation. Reliability: we derive tight stage-local sampling bounds, exact imperfect-verification costs, and a Young--Daly-type checkpoint law with a closed-form optimal verification interval. Controlled and held-out experiments on GPT-6 Astra test communication and reliability predictions, including checkpoint optima, policy selection under programmatic checking, and tradeoffs among call granularity, logical input traffic, and reliability on chained MATH tasks. Together, these results provide a resource theory for the computational cost of language-model agent harnesses.

---


### 41. [What Does a Token Cost? A Mixture-of-Agents Measurement of Sufficient Per-Token Compute](https://arxiv.org/abs/2610.02491)

**<font color=#1a73e8>作者：</font>** Zhixu Du, Weijia Han, Hai Helen Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models spend the same amount of computation on every token they generate, regardless of how difficult each token is to produce. Methods such as speculative decoding and model routing are built on the premise that much of this computation is unnecessary, yet the computation an individual token actually requires has not been measured. We measure it through a Mixture-of-Agents (MoA) lens: a panel of fifteen language models of increasing capacity, drawn from three families, in which every agent attempts to reproduce a reference sequence token by token, conditioned on the correct preceding tokens. We define the inference cost of the smallest agent that succeeds as the token's sufficient compute, which upper-bounds what the token requires. On three core benchmarks, a 0.5B agent reproduces 92--95\% of reference tokens. Across Qwen, OLMo, and R1-distilled panels, the most expensive 10\% account for 64--80\% of estimated FLOPs. On all 500 MATH-500 problems, the MoA-derived map helps model routing reduce projected latency from 7.59 to 5.12 seconds while slightly improving accuracy, relative to the best confidence-routing baseline. The MoA-map helps drafting use 32.6\% fewer draft tokens and approximately 20\% lower projected latency than fixed-window drafting at similar accuracy. These comparisons reveal remaining allocation headroom, motivating controllers that exploit sufficient-compute structure.

---


### 42. [Right Order, Wrong Scale: Auditing LLM Judges for Occupational AI Measurement](https://arxiv.org/abs/2610.02492)

**<font color=#1a73e8>作者：</font>** Harry Lyu, Neil Thompson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM judges are increasingly used to assess whether AI outputs meet workplace requirements, but agreement on response rankings does not establish agreement on acceptance rates or occupational aggregates. We introduce O*NET-BENCH, an audit suite derived from an existing survey of 45,796 worker ratings, and evaluate 33 pre-existing judge configurations across six model families on 4,501 test ratings. Twenty-five configurations achieve tie-aware pair accuracy of at least 0.60, although a train-fitted response-only TF-IDF baseline nearly matches the strongest judge. Despite this ordering agreement, judges estimate that 3.0%-97.9% of responses are acceptable, compared with 61.1% for occupation-matched workers. In one fine-tuned lineage, changing from pointwise scoring to a bundled few-shot/listwise protocol improves response ordering while reducing agreement with worker means at the task and occupation levels; this reversal replicates on a task- and worker-disjoint validation split under prespecified criteria. Cross-validated calibration largely removes mean bias, but calibrated scores explain at most 8.5% of individual worker-rating variance. Prediction-assisted estimation yields at most small precision gains at the studied label budgets. These results show that ranking agreement alone is insufficient for occupational measurement. Judges should be validated against the acceptance rates and aggregates their scores will be used to estimate.

---


### 43. [MeshQuery: Agentic Seam Planning for UV Parametrization](https://arxiv.org/abs/2610.02507)

**<font color=#1a73e8>作者：</font>** Marco Schouten, Arthur Roullier, Elie Michel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present MeshQuery, a training-free agentic approach to automatic UV unwrapping of production-grade quad meshes. A Vision-Language Model (VLM) plans artist-aligned seams using a set of edge-selection tools, conditioned on domain-specific UV-unwrapping knowledge expressed in natural language and refined with a feedback loop. We design a queryable mesh representation together with a domain-specific language (DSL) that enables the agent to retrieve mesh information on demand, express a seam plan as a compact program of edge-selection operators over topological, geometric, and semantic mesh attributes, and iteratively refine it from UV quality feedback. On Adobe Substance 3D and Toys4K meshes, MeshQuery produces 2.9x/4.29x fewer charts and 1.63x/1.7x shorter seams than the strongest baseline, and professional artists prefer its results in 80.9% of comparisons. Ultimately, decoupling high-level intent planning from low-level edge selection and compact mesh representation lets MeshQuery run on different backend VLMs and scale to meshes an order of magnitude larger than autoregressive seam prediction

---


### 44. [On-Premises Multi-Course RAG Tutoring for Business Education: Hardware-Software Trade-offs in a Campus AI Tutor](https://arxiv.org/abs/2610.02510)

**<font color=#1a73e8>作者：</font>** Sidney Shapiro, Joshua Lindemann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Campus AI tutors based on retrieval-augmented generation (RAG) must ground answers in assigned course materials while keeping textbooks and student dialogue on institutional infrastructure. We present CourseChat, an on-premises, multi-course RAG tutor for undergraduate business education, deployed behind a campus web gateway and intended for use embedded in Moodle. Six isolated course offerings, each keyed by its own course reference number (CRN), share twin-edge AI hosts running a FastAPI service, a local vector database, and a local large language model (LLM) served by Ollama. We report two generation-model bake-off rounds, a separate fixed-evidence source-fidelity comparison, and conversation and quiz audits. Several larger models failed the classroom speed gate, but a 12B model and a 7B alternative passed. A separate mixture-of-experts candidate improved some corrections while introducing new factual and continuity errors. We therefore retain the 8B production model pending a demonstrated overall improvement, rather than claiming that 8B is universally optimal. Software changes improved follow-up topic resolution while preserving course scope; 435 prebuilt questions across 65 modules decouple practice from live generation. The results support treating model choice, evidence selection, serving compatibility, and product design as a joint engineering decision. They do not establish learning gains: faculty ratings, peak-load capacity, and complete public-gateway acceptance remain separate evaluation needs.

---


### 45. [From Fragments to Global Maps: Learning Vectorized Map Aggregation with Large Language Models](https://arxiv.org/abs/2610.02513)

**<font color=#1a73e8>作者：</font>** Ziwei Li, Yi-Tang Chen, Xiaoqi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale vectorized HD maps provide structured road information that is essential for perception, localization, and planning in autonomous driving. Constructing such maps requires aggregating noisy, fragmented, and overlapping local predictions collected along a vehicle trajectory into a coherent global map. Existing aggregation methods typically rely on hand-crafted rules for fragment association and refinement. However, a fixed set of thresholds cannot effectively handle variations in road structures and prediction errors, often requiring detector-specific tuning or manual adjustment. To address this limitation, we propose MapMergeLLM, a data-driven framework that formulates vectorized map aggregation as conditional sequence generation with a large language model. Given serialized local vectorized maps, our model directly predicts the aggregated global map polylines. To reduce dependence on any particular upstream detector, we train the model on synthetic local maps generated from clean vector maps using corruptions that simulate representative prediction errors. We further introduce a coordinate tokenizer with geometry-aware pretraining to precisely represent map coordinates. In addition, we propose a line-level association loss that explicitly supervises correspondences between local observations of the same map element. Experiments on Argoverse2 and nuScenes using multiple recent upstream detectors demonstrate that MapMergeLLM substantially outperforms heuristic and optimization-based aggregation baselines without detector-specific retraining.

---


### 46. [Student-Guided Teacher Distillation for Efficient LLM Task Routing: Positioning Against Jev-Style System-1 Classifiers](https://arxiv.org/abs/2610.02516)

**<font color=#1a73e8>作者：</font>** Haifeng Wu, Srinivasan Manoharan, Jian Wan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-shot classifiers are useful for routing user requests to specialized LLM tasks, but scoring every request against a large candidate set is expensive: a zero-shot NLI classifier must evaluate one premise-hypothesis pair per label, so cost scales linearly with taxonomy size. We study a student-guided teacher distillation pipeline for a fixed taxonomy of 60 LLM task categories: a compact ModernBERT classifier predicts the full category distribution in one forward pass and retrieves a small top-k candidate set, and a larger DeBERTa-v3 zero-shot NLI classifier reranks only those candidates rather than all 60 labels; the resulting teacher labels iteratively improve the student, which produces sharper candidates for the next round. Unlike generic embedding retrieval or clustering-derived shortlists used in extreme multi-label classification, our candidate generator is trained end-to-end on the target taxonomy and is the same model serving production traffic, distinguishing it from LLM-routing work that routes between candidate models, and from concurrent System-1 encoder-classifier proposals (e.g. TypeSafe AI's Jev and the open-source Laya project) whose training methodology is undocumented or RL-based. Our best student checkpoint reaches 77.5% teacher agreement on a 200-example evaluation set, and preliminary coverage measurements show Coverage@16 of 91-100%, suggesting top-k sets retain most of the teacher's decision-relevant information. We further show truncated top-k teacher scores should not be treated as full 60-class soft targets for KL distillation: zeroing untruncated classes destroys the dark knowledge soft-label distillation depends on, introducing systematic bias rather than a harmless sparse approximation. A complete evaluation, including coverage at multiple k on a held-out set, an embedding-retrieval baseline, and a larger human-reviewed test set, remains in progress.

---


### 47. [Spatial Memory Intelligence: Endowing World Models with Understanding-Driven Long-Term Memory](https://arxiv.org/abs/2610.02521)

**<font color=#1a73e8>作者：</font>** Ying Yang, Guiyu Zhang, Lianghua Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video generation and world models have shown strong potential for interactive entertainment and embodied simulation by predicting future observations conditioned on user actions and historical memory. However, as memory sequences grow longer and their structures become increasingly complex, managing long-range spatial context becomes increasingly challenging, calling for a more intelligent and systematic memory-management strategy. Building on the advancing spatial reasoning capabilities of multimodal large language models (MLLMs) and the broader vision of unified models, we propose Spatial Memory Intelligence (SMI), the first framework to systematically employ an understanding model for spatial-memory management in long-video world models. SMI introduces four coordinated atomic operations: spatial clustering, within-cluster sparsification, action-aware retrieval, and reliability-aware filtering. Extensive experiments across multiple baselines, benchmarks, and world-model backbones demonstrate the effectiveness and generalizability of SMI, achieving comprehensive improvements in memory sparsity, generation stability, and spatial consistency.

---


### 48. [Hypothesis-guided discovery of cognitive algorithms via program refinement](https://arxiv.org/abs/2610.02523)

**<font color=#1a73e8>作者：</font>** Huiwen Alex Yang, Mark K. Ho, Bill D. Thompson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developing cognitive models of algorithmic reasoning from behavioral data is a central problem in cognitive science that challenges current methods. Traditional approaches to cognitive modeling are interpretable and benefit from human expertise, but lack flexibility and scalability. Emerging techniques using large language models (LLMs) for de novo generation of cognitive models are scalable and flexible, but lack a role for human expertise and have mostly been applied to simpler tasks than algorithm recovery. We propose a hybrid system that treats discovery of cognitive algorithms as a program refinement problem. Human-created cognitive models are expressed as probabilistic programs and provided to a system of LLM agents with a mandate to: identify mismatches between model and behavior; propose code-level modifications within researcher-specified constraints; and verify structural fidelity. Revisions propagate to a probabilistic inference module that performs inference for latent variables and data likelihood computations. We evaluate the pipeline on human behavior in a problem-solving paradigm that exposes a variety of cognitive algorithms. Revised models consistently improve model fit relative to ancestral models and reveal a small set of recurring innovations that capture meaningful behavioral variability in this task.

---


### 49. [How To Train Your World Model: Fine-tuning vs RAG for LM-based World Modeling](https://arxiv.org/abs/2610.02542)

**<font color=#1a73e8>作者：</font>** Dhananjay Ashok, Shantanu Agarwal, Vivek Datla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models (WMs) simulate the transition dynamics of environments, enabling agents to plan over the consequences of their actions. In text-based environments, fine-tuning a Language Model (LM) to serve as a WM has emerged as a dominant paradigm. However, despite the widespread success of non-parametric approaches such as Retrieval Augmented Generation (RAG), retrieval for LM-based world modelling remains underexplored. We conduct a systematic evaluation across five diverse environments spanning embodied, web navigation and social settings, comparing fine-tuning and RAG-based approaches for LM-based world modelling. Our study reveals that fine-tuning often outperforms RAG, with fine-tuned WMs enabling agents to obtain higher rewards on 15/20 settings. While both construction paradigms benefit from additional and more diverse exploration, RAG-based approaches prove more data-efficient, and fine-tuning approaches disproportionately benefit from scaling the amount of experience collected. With a focus on RAG-based WMs, we devise a procedure that uses counterfactual intervention to estimate the error rate of the retrieval stage, and show that retrievers consistently surface suboptimal transitions from the experience buffer. Hoping to address this failing, we study a variety of query reformulation strategies, demonstrating that a hierarchical approach outperforms the traditional retrieval pipeline. Finally, we compose our findings into a hybrid world modelling system that parametrically captures core environment dynamics, while learning to rely on retrieval from an actively maintained memory store. Our hybrid system consistently outperforms other methods across multiple environments and models, showcasing the robustness of the approach and the applicability of our findings.

---


### 50. [CITADEL: CWE-Guided Insertion of Hardware Trojans via Analysis of DFG-Enabled LLMs](https://arxiv.org/abs/2610.02544)

**<font color=#1a73e8>作者：</font>** Jayanth Thangellamudi, Raghul Saravanan, Sudipta Paria 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing sophistication of Hardware Trojans (HTs) and system-level vulnerabilities poses significant risks to modern integrated circuits. However, constructing realistic HT scenarios, remains a substantial burden: researchers must manually analyze complex RTL structures, identify plausible weaknesses, and craft stealthy, synthesizable insertions that preserve functional correctness. This paper introduces CITADEL CWE-Guided Insertion of Trojans via Analysis of DFG-Enabled LLMs, a framework that leverages Large Language Models (LLMs) and Data Flow Graphs (DFGs) to automate CWE-grounded HT synthesis. CITADEL uses structured CWE semantics together with DFG-derived structural context to assist the user in identifying relevant vulnerabilities, localize the module surrounding the chosen insertion point, and perform intent-conditioned RTL modification. The framework produces minimal, synthesizable, and interface-preserving HTs with ultra-rare triggers. Experimental evaluation across diverse RTL designs demonstrates that all generated HTs are 100% syntactically correct, remain undetectable under large-scale random simulation, and are functionally triggerable under their intended activation conditions. These results highlight CITADEL as a scalable and principled method for generating realistic HT benchmarks.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-261](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
