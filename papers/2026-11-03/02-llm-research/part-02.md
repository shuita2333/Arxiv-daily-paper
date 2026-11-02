# 🧠 大模型相关研究 | 2026年11月03日

> 本类共 **188** 篇论文：已确认 **175** 篇，待复核 **13** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-188](./part-04.md)

---

### 51. [Out of sync: Accommodation, evaluation, and emergence in five weeks with an agentic AI teammate](https://arxiv.org/abs/2610.41057)

**<font color=#1a73e8>作者：</font>** Nia Nixon, Jaeyoon Choi, Pedro Martins de Bastos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As agentic AI in education shifts from reactive tools toward partners that take initiative and persist over time, a central question is how learners relate to, evaluate, and benefit from artificial agency. We conducted a longitudinal experiment in an undergraduate learning analytics course, in which 17 student teams (N = 48) collaborated with a persistent LLM-based teammate across weekly sessions. The agent decided when to intervene through a trigger-based architecture, and its social role was manipulated between teams: a Cognitive Agent that challenged quick consensus or a Supportive Agent that invited quieter members to contribute. Combining chat discourse, post-session surveys, and spoken reflections, we identified distinct patterns unfolding across three timescales. Students accommodated their language to the agent's role immediately, using more social language toward the Supportive Agent from the first session. Their helpfulness evaluations were recalibrated from session to session in relation to the agent's observed behavior, rather than remaining anchored to students' pre-existing attitudes toward AI. A slower crossover emerged in perceived collaboration process and positive-affect word use in reflections: Supportive-Agent teams began below Cognitive-Agent teams and ended above them, although students rated the Supportive Agent less helpful throughout. Because these responses follow different trajectories, single-session evaluations of agentic AI may miss changes that emerge only through repeated interaction.

---


### 52. [LanG 2.0: Energy-Efficient Agentic AI for Semi-Automated Security Operations at Scale](https://arxiv.org/abs/2610.41072)

**<font color=#1a73e8>作者：</font>** Anes Abdennebi, Nadjia Kara, Laaziz Lahlou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Security operations centers (SOCs) need to turn terabytes of alerts, logs and flows into trusted, affordable decisions to unveil hidden threats. We present LanG 2.0, an agentic system that detects threats, correlates evidence and writes rules, investigating whether small local models can replace frontier models affordably and safely when structural safeguards, not model accuracy, provide the guarantees. It incorporates entity-anchored correlation, human approval of rule changes and a tamper-evident ledger. Tests span eight flow datasets from five networks, real XDR alerts and multistage campaigns. Against its predecessor, campaign correlation precision rises from 18.75% to 51.81%, and rule acceptance from at most 60.00% to 98.33%. Against Claude Opus 5.5, scoring flows against each network's normal traffic detects attacks on unseen networks at 73.42% F1 without false positives, versus 58.10% with 49.00% false positives, for at least 650 times less energy. Finetuned models statistically match it on alert classification and rule writing for 5.6 to 59 times less energy. The work demonstrates LanG's practical scalability, processing 3.33 million records in 6.4 minutes, over 30 million hourly, and its safeguards resisted prompt injection, label poisoning and ledger tampering, so small local models can carry most SOC detection affordably and safely.

---


### 53. [bf16 Rounding Silently Discards Most RL Policy Updates: A Hidden Training-Inference Mismatch and an Unbiased One-Line Fix](https://arxiv.org/abs/2610.41073)

**<font color=#1a73e8>作者：</font>** Andrew Gao, William Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training of language models keeps fp32 master weights in the optimizer and serves rollouts from a bf16 copy produced by round-to-nearest conversion. At the learning rates in common use, most per-step updates are smaller than half a bf16 spacing and the conversion discards them: on Qwen3-1.7B only 0.4-0.5% of served weights change per step, and the policy that generates the training data lags the optimizer by 50-150 steps. Existing mismatch corrections cannot see this lag because they compare two copies downstream of the same rounding. We propose Fair Cast: export the master with an unbiased rounding rule (stochastic rounding or error feedback) and compute the training loss on the served copy. The change is one line at the export call, adds no hyperparameters and costs 22-38 ms per export of 1.7B parameters. Across 25 matched seed-pairs on Qwen3-0.6B to 4B with AdamW and Muon, Fair Cast is ahead on 18, tied on 6 and behind on 1, with a mean gain of 6.1 points; on zebra puzzles it reaches 0.57 +/- 0.16 over four runs where round-to-nearest collapses to 0.33 +/- 0.10. It also makes the saved fp32 checkpoint agree with the served model, and it exposes the implicit lag of round-to-nearest as a regularizer that can be restored explicitly when a task needs it.

---


### 54. [BABA-Bench: Evaluating Long-Horizon Patient-Advocacy Agents](https://arxiv.org/abs/2610.41076)

**<font color=#1a73e8>作者：</font>** Shriram Vasudevan, Videet Mehta, Connor Sweeney  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An LLM agent that helps a patient get care must do two things. It must reach the correct outcome, and it must follow the necessary procedure. For example, the agent must get the patient's permission before it shares the patient's records. We introduce BABA-Bench, a benchmark of 47 interactive worlds. We built each world from a de-identified, real patient advocacy case that expert advocates reviewed. In each world, the agent must find hidden information and coordinate insurers, clinics, suppliers, pharmacies, and community organizations. The engine checks each action at the time the agent does it. It checks if the agent has permission, if the agent has evidence for the action, and if the action is prohibited. We evaluated 14 frontier models with three runs on each world, for a total of 1,974 runs. Agents often reached the correct outcome by an invalid route. Of the 921 runs that reached all required outcomes, 254 (28%) did not follow the necessary procedure. Claude Opus 5 reached all required outcomes in 81.6% of its runs, but only 52.5% of its runs passed all checks. When we gave two models a verified route, their pass rates increased from 29.8% to 91.5% and from 44.0% to 97.2%. For these models, the main problem is to find a route, not to execute it.

---


### 55. [EDU-Jev Training System-One Decision Models for Education](https://arxiv.org/abs/2610.41079)

**<font color=#1a73e8>作者：</font>** Jiazheng Li, Yulan He  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many automated decisions in education involve choosing from a fixed set of options: assigning a rubric score, checking whether an answer meets a marking criterion, or identifying the first wrong step in a solution. Generative language models are increasingly used to make these decisions, but their responses require parsing, longer outputs increase inference costs, and confidence expressed in words does not necessarily reflect the probability of being correct. We present EDU-Jev, a family of single-pass ("System One") decision models at 0.8B, 2B and 4B parameters. Given an assessment context and a question with predefined answer options, the model returns a probability distribution over those options without generating text. A pointer head scores a marker for each option, ensuring the predictions are restricted to the allowed choices. Training uses a single supervised stage with soft cross-entropy against the available target label distributions; calibration is assessed empirically. Across twelve education benchmarks, EDU-Jev 4B achieves an average accuracy of 67.6%, exceeding the strongest of five commercial decision APIs by 9.4 percentage points and the best open 4B decision model by 18.7 points. On four cross-domain education sets, it matches the strongest API, which remains ahead on general decision-making and reasoning tasks. The 2B model processes about 150 decisions per second on a single H100 GPU.

---


### 56. [Grounding Image Composition with Label-Conditioned Visual Evidence](https://arxiv.org/abs/2610.41080)

**<font color=#1a73e8>作者：</font>** Armin Dadras, Tingyu Lin, Robert Sablatnig 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image composition labels such as center, diagonal, or rule of thirds describe visual structure rather than object categories. KU-PCP provides image-level labels and class-specific geometric elements, but does not show which visible regions people associate with each of its nine classes. We introduce KU-PCP Elements (KU-PCPE), a label-conditioned region-evidence benchmark for photographic composition. Given an image and a label already judged applicable, the task is to segment the visible regions that explain why the label applies. KU-PCPE contains 4,093 single-annotator training masks and a 1,327-task expert test split with three masks per image-label task. The annotations also include exploratory segment-versus-line ratings that describe whether region or semantic-guideline evidence better explains the label. A held-out expert reaches .867 Dice against the other experts, while the strongest deployable model reaches .664, a proposal oracle .672, and the best vision-language model (VLM) proposal selector .395. KU-PCPE exposes the gap between recognizing a composition label and grounding the human-aligned visual evidence that makes it plausible in a particular image.

---


### 57. [CIRCE Divines LLM Task Complexity from Constraint Structure](https://arxiv.org/abs/2610.41089)

**<font color=#1a73e8>作者：</font>** Chenhao Hong, Jiakai Xu, Kaushiki Singh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Estimating whether a problem is too complex for a large language model (LLM) before the model attempts it can guide model routing, how to allocate test-time compute, and suggest the need for new tools to aid the agent. While existing estimators rely on the problem text, LLM-annotated task difficulty labels, or signals obtained after a model attempts to solve the problem, such as its hidden states, none explicitly leverage the constraint structure inherent in the problem: the variables to assign and how the constraints over them interact.
We introduce CIRCE, which extracts a problem's structure by using a cheap LLM to construct a Constraint Intermediate Representation that deterministically compiles into the constraint graph. Across seven reasoning benchmarks (including SAT, logic, and math) and four LLMs, even a randomly initialized GNN encoder improves predictions of LLM response correctness, reducing negative log-likelihood from 0.465 to 0.423 and increasing AUROC from 0.691 to 0.727 relative to the strongest baseline for each metric.

---


### 58. [MUON-RT Reusing the Teacher's Trajectory for Momentum-Free Muon for LLM Self-Distillation](https://arxiv.org/abs/2610.41104)

**<font color=#1a73e8>作者：</font>** Aryan Das, Vinay Kumar Verma, Aakansha Mishra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-distillation methods for large language models with an exponential moving average (EMA) teacher already retain a history of student updates. Muon nevertheless stores a separate momentum buffer, increasing persistent training memory. We propose Muon with Reused Teacher (Muon-RT), which reuses the teacher-student displacement to eliminate momentum buffers for hidden weight matrices. We show that this displacement encodes an exponentially weighted history of applied updates and smooths temporally uncorrelated noise under a local model. Muon-RT removes its radial component, normalizes it spectrally, and mixes it with the current gradient after Newton-Schulz (NS) orthogonalization. Under explicit regularity and alignment assumptions, we establish linear contraction of an expected objective-gap bound toward a residual error level. With Self-Distillation Fine-Tuning (SDFT) on Qwen2.5-7B-Instruct, Muon-RT improves average accuracy over AdamW by 2.6 points with 42% less persistent memory, and over momentum Muon by 5.4 points with 27% less persistent memory. With Self-Distillation Policy Optimization (SDPO) on Olmo-3-7B-Instruct, it improves average accuracy over AdamW by 2.0 points.

---


### 59. [Calibration of Large Model Quantization based on HiFloat4 Format](https://arxiv.org/abs/2610.41112)

**<font color=#1a73e8>作者：</font>** Jing Huang, Yu Cheng, Ziwei Yu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantization of Large Language Models (LLMs) has be- coming increasingly important for reducing the computa- tional costs and resource requirements for practical deploy- this http URL- nity to move beyond 8-bit quantization towards 4-bit preci- sion, leading to the development of customized 4-bit formats such as MXFP4 and NVFP4. Recently, HiFloat4 (HiF4) has emerged as a competitive alternative which adopts a Block Floating-Point(BFP)formatwithathree-levelscalinghierar- chy, thereby achieving a significantly larger dynamic range. While quantization can substantially reduce memory usage and accelerate inference, it frequently introduces accuracy degradation. Calibration is therefore essential for narrowing theperformancegapbetweenlow-precisionquantizedmodels and their full-precision counterparts. Nevertheless, existing calibration methods are mainly designed and validated us- ing integer-precision formats, such as INT4, lacking support for HiF4 due to its hierarchical BFP structure. In this paper, weinvestigatethreecalibrationapproaches,namelyHiGPTQ, HiAutoRound, and HiFlatQuant, to further enhance model this http URL demonstratethatallthreeproposedapproachesimproveinfer- ence accuracy compared with direct HiF4 conversion, reduc- ing the gap between HiF4 and BF16 to less than 1% and out- performing the state-of-the-art NVFP4 format across various models and downstream tasks.

---


### 60. [Predicting Human-Gain Curves under Local Proxy Optimization from Repeated Ratings](https://arxiv.org/abs/2610.41114)

**<font color=#1a73e8>作者：</font>** Moonwon Choi, Kisung Nam, Seunggeun Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Optimizing a proxy objective can improve human-perceived quality, but the resulting gain can vary with optimization strength. Average proxy-human correlation alone does not reveal how human-perceived quality changes as optimization strength increases. We propose PACE (Proxy Alignment and Curvature Expansion), a pre-optimization diagnostic that uses repeated human ratings to predict the human-gain curve induced by a fixed proxy. The method models proxy optimization as a KL-regularized exponential tilt. At KL radius $d$, the local gain is approximated by $A\sqrt{d}+Bd$, where $A$ measures first-order proxy-human alignment and $B$ captures the leading second-order correction along the proxy-optimization path. We estimate $A$ and $B$ from repeated human ratings on calibration items and test the resulting gain-curve prediction on held-out evaluation items. Across SummEval, analysis-eligible WMT MQM clusters, an OpenMEVA-MAGS ROC/WP repeated-rating slice, and a GPT-4o judge proxy experiment, PACE consistently reduces held-out gain-prediction error relative to $A$-only, zero-gain, and reliability-only baselines. With the same pre-pool information, it is competitive with flexible proxy-conditional calibration, and a LoRA-DPO experiment provides a modest bridge to actual optimization. Transfer experiments across datasets and evaluation slices show that source coefficients are useful priors, but target calibration further improves prediction. The resulting diagnostic is local and one-sided: it characterizes gentle optimization along the positive tilt branch of a fixed item pool.

---


### 61. [Language Models Show a "Women-Are-Wonderful" Effect in Blame Attribution That is Not Just Leniency](https://arxiv.org/abs/2610.41116)

**<font color=#1a73e8>作者：</font>** Anika Sharma, Snehalkumar 'Neil' S. Gaikwad, Snigdha Chaturvedi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper investigates the Women-Are-Wonderful (WaW) effect in language-model blame attribution: a favorable bias in which women receive more positive evaluations than men. Using 11,270 interpersonal conflicts from r/AmItheAsshole, we construct matched counterfactuals that vary the gender of the person being judged (the original poster) and the person affected (the counter-party). Across four language models, gender changes a minority of verdicts, but those changes consistently favor women. The effect is strongly role-dependent. Making the original poster a woman reduces the odds of blame by 9--52%, while making the counter-party a woman multiplies them by 2.7--9.2X. Counter-party WaW also varies across conflict types, strengthening in communication and relationship conflicts and weakening in family conflicts. Exploratory probes suggest that counter-party gender can shift judgments of sympathy, reasonableness, harm and protection. WaW is therefore not just leniency toward women being judged: models also judge conduct more harshly when it affects a woman.

---


### 62. [CompoSET: A Controlled Single-Edit Benchmark for Vision-Language Compositionality](https://arxiv.org/abs/2610.41118)

**<font color=#1a73e8>作者：</font>** Laure Delisle, Pietro Perona  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language compositionality is the ability to identify which properties, relations, quantities, and states bind to which entities in both an image and a caption, and to match those bindings across modalities. Existing benchmarks evaluate this ability through image-text matching: a model ranks candidate image-caption match similarities and succeeds when the correct match comes on top. In such datasets, paired images differ by more than a single binding: scene, layout, and content all differ, with 97% of pixels changing on average. Such pairs do not isolate compositionality: results are confounded by global image differences. We introduce Compositional Single-EdiT (CompoSET), a benchmark dataset in which each base image-caption pair has an edited counterpart, or foil, that preserves the scene but differs by a single controlled edit, such as color, count, spatial relation, or object state. Base and foil images preserve naturalistic scene complexity yet are visually near-identical: only 8% of pixels change on average. Our dataset has many foils per base scene (~22) in order to separate scene difficulty from edit difficulty, a distinction one-foil-per-base benchmarks cannot make. CompoSET contains 1,776 instances across 80 naturalistic scenes, spanning 16 edit types in 4 semantic categories, with captions at 3 verbosity levels. We test 22 dual-encoder VLMs and find that all models perform at or below chance level on CompoSET, despite scoring well on prior benchmarks. This suggests that apparent progress under prior image-text matching protocols may be an artifact arising from confounds in benchmark design, and that compositional understanding in dual-encoder VLMs is far from solved. CompoSET addresses the confounds and offers a better controlled benchmark to measure future progress.

---


### 63. [Confident Fools or Careful Searchers? A Behavioural Study of When LLMs Search Beyond Their Static Internal Memory](https://arxiv.org/abs/2610.41124)

**<font color=#1a73e8>作者：</font>** Nipun D. Pathirage, Kwan Srijomkwan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic LLM assistants must repeatedly decide whether to answer from memory or to call a tool such as web search. Unnecessary searches cost latency and money; missing ones yield confident but unsupported answers. Prior work mostly measures verbalised confidence or trains new adaptive-retrieval methods, and rarely audits the search decisions that deployed products actually make. We introduce a benchmark of 400 multiple-choice questions that combines widely known inside-knowledge (IK) questions, which should be answered directly, with outside-knowledge (OK) questions about facts from news published after the models' training cut-offs (to our knowledge), which should trigger search or, without tools, abstention. Each item offers an abstain option, and two action-level scores, NAS and KIS, reward searching on OK questions and restraint on IK questions. Across five commercial LLMs with and without their vendors' web search, GPT-5 mini and Grok 4 Fast search on over 90% of OK but only 1% of IK questions, whereas Mistral Small searches on just 20% of OK questions, often abstaining instead of using its tool; one product's search indicator proved unusable. Searching is partly triggered by explicit temporal cues: on uncued OK questions, the NAS of the two selective models falls from about 0.72 to 0.57--0.58. The scores thus measure the search triggering of specific products, not metacognition in a strict sense.

---


### 64. [When Should AI Agents Ask? Clarification Requests Under Limited Human Attention](https://arxiv.org/abs/2610.41129)

**<font color=#1a73e8>作者：</font>** Hanzhao Wang, Shengjie Liu, Zhengchao Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly carry out delegated tasks in parallel, with one person overseeing several of them at once. In practice, an agent often lacks information its task requires, such as an unstated preference, constraint, or specification. It can ask the human to clarify, or it can search for the information itself, for example in past records, which takes time and effort and may fail. In this paper, we study how to coordinate these decisions across several agents that share one human with limited attention. We build a stylized model in which each agent can search, ask, or continue the parts of its task that do not depend on the missing information, and we formulate the problem as a dynamic program. We first show that whether an agent should ask depends on more than its own uncertainty: an agent with other work to do can be better off asking earlier, and which question the human should answer first depends on all waiting questions, so no ranking computed agent by agent is optimal. We then propose the Pairwise Coordination Policy (PCP), which uses exact one- and two-task problems to estimate how pairs of tasks delay each other when they share the human. Theoretically, PCP is exactly optimal when at most two requirements remain unresolved and costs at most twice the optimum when every unresolved requirement must be resolved by the human. We evaluate PCP on 864 synthetic cases and in a case study with LLM agents. On the synthetic benchmark, PCP's mean gap to optimal cost is 0.07%, and it reduces cost by an average of 18-31% relative to three standard rules for when to ask. In the LLM case study, agents completed every task correctly, and PCP achieved the lowest mean cost in all tested settings.

---


### 65. [When Disclosure Is Compulsory: Evaluating Ride-Hailing Rebalancing Policies with Self-Interested LLM Driver Agents](https://arxiv.org/abs/2610.41132)

**<font color=#1a73e8>作者：</font>** Xinyu Wang, Andres Fielbaum  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The EU Platform Work Directive, to be transposed by December 2026, requires ride-hailing platforms to state in plain language the main parameters of their automated decisions and how a worker's behaviour affects them. Such rules are exactly what a large language model (LLM) can read, so drivers will be able to let one decide for them. We compare two main families of rebalancing policy once their rules are public: a reactive policy (R) that sends idle drivers to cover requests just lost, and an anticipatory policy (A) that plans moves on a demand forecast. Each driver is an LLM agent maximizing its own net income, given no rules (N) or the rules at the directive's level of detail (L). We test two LLMs, Claude Haiku 5.5 and Jev, which understand the rules equally well, in a three-zone model and in Manhattan. With the rules disclosed, drivers follow the platform more closely: in Manhattan, the share of relocation offers they decline falls from about four in five to one in four under both policies. Yet the effects differ by policy. For the platform, disclosure costs R 3.7% of its profit in Manhattan, as R now pays for moves drivers used to make for free, while A's profit is unchanged; the two policies, which tie on profit under full compliance, end 6.1% apart. For drivers, disclosure raises income in the small model under both policies and LLMs; for users, it raises the service rate there by 10 to 18 percentage points. In Manhattan, self-interested drivers also make A a win-win-win against full compliance, raising driver income, platform profit and service rate by 10 to 12% each. Rebalancing policies that perform equally well under full compliance can thus show opposite results under mandatory disclosure. The study offers a framework to evaluate such policies under the new requirement and is, to our knowledge, the first to do so with LLM agents.

---


### 66. [TalentRL: Strategy-Guided Reinforcement Learning for Hierarchical Skill Routing](https://arxiv.org/abs/2610.41143)

**<font color=#1a73e8>作者：</font>** Huancheng Chen, Xiaodi Sun, Zhaoqiong Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Natural-language skills enable large language model (LLM) agents to reuse procedures across tasks, yet most systems retrieve individual skills from a flat SkillBank without explicitly modeling the high-level strategy that governs their selection and use. We introduce TalentRL, a strategy-guided reinforcement learning framework for hierarchical routing over procedural memory. Coarse-grained talents represent recurring strategies for skill use, while fine-grained skills provide executable procedures. For each task, the policy model selects a talent that guides execution and softly prioritizes its associated skills during similarity-based retrieval. However, since task outcomes depend jointly on talent selection, retrieved skill context, and downstream execution, terminal rewards alone cannot isolate the contribution of the routing decision. TalentRL therefore trains talent routing with reward contrasts between rollouts of the same task under matched interventions on the talent-conditioned context, and optimizes downstream execution with group-relative advantages. Across seven open-domain and multi-hop question-answering benchmarks, talent-aware supervised fine-tuning improves average success rate by 7.53%, 6.71%, and 9.21% over the corresponding zero-shot baselines for Qwen2.5-7B, Qwen3-8B, and Llama-3.1-8B, respectively. Reinforcement learning further improves these SFT checkpoints by 7.58% to 9.32%, and TalentRL achieves the highest average success rate among all compared methods on all three backbones. On the agentic benchmarks ALFWorld and WebShop, TalentRL achieves the highest ALFWorld success rate (99.3%) and the highest WebShop score (90.7) among all compared methods.

---


### 67. [HyperRepair: Recovering Forgotten General Capabilities of Fine-Tuned Language Models](https://arxiv.org/abs/2610.41147)

**<font color=#1a73e8>作者：</font>** Junrong Tang, Jianghui Wang, Hao Kong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning improves a language model's performance in a target domain but can weaken its general capabilities. Existing methods often face a trade-off between general capabilities and domain specialization, making it difficult to preserve both. We introduce HyperRepair, a framework for recovering general capabilities while retaining domain specialization at only inference cost. To make recovery generalizable across models sharing a pretrained backbone, HyperRepair learns a hypernetwork from repairs trained on source models. The hypernetwork uses activation fingerprints that summarize changes from the pretrained backbone to generate a tailored Repairing Side Net (RSN), whose prompt-conditioned gate applies corrections selectively. This enables recovery on models from unseen adaptation domains without target-domain examples or additional optimization. We evaluate HyperRpair across two model families, 12 LoRA adaptation datasets, and 15 general benchmarks. On the default split, HyperRepair achieves 93.4% of the base models' average general score while retaining 99.5% of the fine-tuned models' average domain score.

---


### 68. [Counterfactual Pairwise Augmentation Improves Small Pointwise LLM Judges](https://arxiv.org/abs/2610.41149)

**<font color=#1a73e8>作者：</font>** Mohammad Zangooei, Peyvand Teymoori, Mohammad Robati Shirzad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems increasingly gate individual steps with a pointwise judge that scores a response against a criterion. Small language models are attractive for this role because they can be served and specialized efficiently. Such a judge must locate the criterion's decision boundary, but pointwise labels under-determine that boundary in fine-tuning: labeled responses to different queries differ along many dimensions at once, so they do not reveal which features decide the label. We introduce CPA (Counterfactual Pairwise Augmentation), which makes the deciding difference explicit in training. For each pointwise item, CPA synthesizes and audits a counterfactual response to the same query intended to carry the opposite label. It frames the accepted pair as a pairwise task asking which of the two responses satisfies the criterion. The judge is fine-tuned jointly on both pointwise and pairwise datasets and deployed in pointwise mode only. A second-order analysis shows when this should outperform the prevailing strategy of merging separately trained pointwise and pairwise experts: merging moves every parameter direction toward the pairwise expert by the same fraction, whereas joint training can hold the pointwise optimum wherever the pairwise loss is flat and absorb its curvature where it is sharp. This is the regime that CPA's same-source, counterfactually minimal pairwise view is designed to produce. On separate Qwen3-8B LoRA adapters for six binary criteria, CPA improves criterion-averaged pointwise macro-F1 by 2.5 points over pointwise-only training and outperforms model merging on all six criteria at every tested merge weight. It also surpasses the strongest zero-shot frontier judge we evaluate, Gemini 3.6 Flash, by 11.8 points.

---


### 69. [FrontierMat: Benchmarking Language Models at the Frontier of Materials R&D](https://arxiv.org/abs/2610.41162)

**<font color=#1a73e8>作者：</font>** Feng Chen, Jianguo Huang, Yushan Xiao 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To accelerate materials discovery, language models must be able to address problems at the research frontier. Yet textbook- and examination-derived benchmarks primarily assess established knowledge, leaving performance on frontier research problems largely untested. We introduce FrontierMat, a benchmark of 330 problems drawn from frontier academic and industrial research in fields including aerospace, semiconductors, embodied intelligence and nuclear fusion. Every problem is validated by leading experimentalists and industry experts in its field. Each problem presents a real study and asks the model to infer a withheld outcome or draw a conclusion from selected experimental evidence. Problems are annotated by functional domain, material system and the scale of the governing mechanism; 130 require cross-scale reasoning. The strongest general-purpose model scores only 53.7%, and on matched problems, cross-scale problems score 8.7 points below single-scale ones. Half of the problems are solved by at most one model, and models fail chiefly by endorsing what is plausible rather than what was observed. A domain-adaptation study with meta-weighted continued pretraining and scale-modular self-distillation raises an open-weight model from 36.7% to 55.4%, matching the strongest proprietary model, with improvements on public materials benchmarks and no decline in aggregate performance on general benchmarks. FrontierMat provides a testbed for measuring progress toward language models that support frontier materials R&D.

---


### 70. [LLM Detoxification via Transition-Aware Reward-Guided Representation Sampling](https://arxiv.org/abs/2610.41165)

**<font color=#1a73e8>作者：</font>** Aishan Liu, Yisong Xiao, Xianglong Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can generate toxic content, motivating effective test-time detoxification. Existing representation steering methods often rely on static or coarse interventions and provide imprecise guidance because they inadequately model transitions between toxic and non-toxic generations. We propose Transition-Aware Reward-Guided Representation Sampling (TARGRS), a test-time framework that learns reward guidance over toxicity transitions in latent representation space. During exploration, progressive steering along the toxicity direction constructs trajectories from non-toxic to toxic states. Toxicity scores along these trajectories turn sparse annotations into dense, listwise supervision for a transition-aware token-level reward model. During inference, TARGRS uses this model to guide coarse-to-fine sampling along the opposite, non-toxic direction: coarse sampling identifies the intervention needed to reach non-toxic regions, and refinement selects a detoxified representation with minimal perturbation. Experiments on 10 LLMs across RealToxicityPrompts, BOLD, and AttaQ show that TARGRS consistently outperforms state-of-the-art baselines, reducing toxicity by up to 69.38% on RealToxicityPrompts. TARGRS runs nearly as fast as the original LLM while preserving its core capabilities with minimal impact. By intervening in the language decoder space, TARGRS also extends to Large Vision-Language Models (LVLMs), reducing toxicity by up to 64.23% across 3 representative LVLMs.

---


### 71. [ImplicitHop: Evaluating knowledge integration across context and memory](https://arxiv.org/abs/2610.41169)

**<font color=#1a73e8>作者：</font>** Alexander Detkov, Dashiel Karish, Matthew Oleynikov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The ability to integrate new information and deduce its consequences is central to learning, understanding, and reasoning in large language models (LLMs). Whether information arrives during training or in-context, models must not only store local facts, but propagate their long-range implications globally. To explore information integration in LLMs, we introduce two complementary natural language benchmarks for large-scale evaluation of deductive reasoning as a function of inference depth. The first is a formal graph benchmark enabling controlled evaluation over a wide range of graph topologies and integration tasks; the second is a knowledge composition benchmark grounded in real-world knowledge graphs. We use these benchmarks to compare knowledge integration from information encoded in context versus information encoded in model weights during pretraining, evaluating a set of open models implicitly, without chain of thought. We find that accuracy decays sharply with increased composition length for both pretrained and in-context knowledge. Information presented in-context, however, substantially outperforms deduction over information encoded in weights. These results quantify a fundamental limitation of current models with direct implications for prompt-based control of agent behavior and for continual learning strategies, and they provide a foundation for developing training, prompting, and integration methods that support deeper reasoning.

---


### 72. [TraceSpec: Understanding and Improving Speculative Decoding for LLM Agents](https://arxiv.org/abs/2610.41177)

**<font color=#1a73e8>作者：</font>** Jihao Zhao, Shuaishuai Zu, Pengfei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents execute tasks through repeated model calls over evolving histories of reasoning, actions, and tool feedback. Aggregate speculative-decoding metrics merge these distinct decisions, providing limited guidance on where draft supervision is needed. We present TraceSpec, a framework connecting trajectory evaluation with adaptive draft training. It combines dynamic execution with fixed-prefix replay and introduces TraceSpec-Traj, a corpus of 10,000 training states and 2,500 test states spanning browsing and software engineering. Analysis of five speculative baselines reveals that aggregate acceptance can rise with context length while declining within matched late browsing actions. Workload and phase further distinguish these trends, motivating supervision guided by trajectory conditions. TraceSpec trains on intermediate assistant turns and allocates a fixed prediction budget using state-conditioned estimates of prefix-aware acceptance gaps. Across three target sizes and two temperatures, it improves replay throughput by 12.5% to 22.6% over its DSpark base. Qwen3-4B ablations show that adaptive allocation increases accepted length by 3.3% to 10.0% over fixed full-turn supervision, with additional comparisons substantiating the roles of state conditioning and consecutive-token agreement. The resulting evaluation resources, trajectory findings, and training strategy connect the analysis of agent execution to practical draft improvement.

---


### 73. [AgentShield: Fortifying Web Applications Against AI Agents and Agentic Browsers](https://arxiv.org/abs/2610.41181)

**<font color=#1a73e8>作者：</font>** Moiz Ali, Nafis Karim, Rownak Islam 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-powered browser agents are transforming web automation by autonomously interacting with websites and executing complex workflows. However, the effectiveness of existing anti-bot defenses against these systems remains unclear. We present a systematic empirical evaluation of modern agentic browsers against widely deployed anti-bot mechanisms, characterizing their capabilities, limitations, and behavioral differences from humans. Our results show that many defenses designed for traditional automation struggle to reliably detect autonomous AI-driven agents. Accordingly, we introduce AgentShield, a behavioral fingerprinting framework that targets the Perception-Reasoning-Action (PRA) loop underlying agentic user clients. By leveraging dynamic web forms that progressively reveal content and capture fine-grained interaction telemetry, AgentShield exposes behavioral artifacts that enable differentiation between human users and autonomous agents. We further demonstrate Extinction-induced Policy Drift (EPD), a novel attack in which repeated obstruction of task completion causes agents to relax their safeguards and engage in unsafe behaviors. Finally, we present defensive prompt injection techniques that exploit agent-specific weaknesses to mitigate emerging forms of autonomous web abuse that rely on content extraction. Our results highlight both the shortcomings of current web defenses against agentic user clients and the feasibility of practical detection mechanisms tailored to this new generation of web automation.

---


### 74. [Researcher-in-the-Loop Evolutionary Discovery of Entanglement-Assisted Quantum Code Families](https://arxiv.org/abs/2610.41183)

**<font color=#1a73e8>作者：</font>** Jae-Hyun Baek, Byung-Sun Won, Jon-Lark Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-guided program evolution can produce mathematical constructions, but validity, generality, and reproducibility require distinct evidence. We develop a researcher-in-the-loop discovery pipeline that combines program evolution, exact evaluation, mathematical generalization, certified nonexistence checks, and formal proof checking. We apply it to entanglement-assisted quantum error-correcting codes (EAQECCs). Starting from tasks that did not specify a family formula, evolved programs produced finite qubit constructions whose structure researchers generalized to the family $[[n,1,n-1;n-q-1]]_q$ for prime powers $q\ge3$ at $n\ge2q+1$ and for $q=2$ at odd $n\ge5$. Lean checks the algebraic certificate underlying this family. Together with entanglement lifting, the family closes 54 gaps in archived EAQECC tables. The released evidence includes 115 verified code records, ten nonexistence results with checked DRAT proofs, family implementations, and preserved search programs for exact checks and seeded replay. In a controlled cohort of eight paired generation blocks, validation-selected iterative programs achieve success in 46.1% and 31.6% of held-out executions at unseen lengths $n=13,15$, compared with 19.5% and 3.1% for independently generated programs. In this setting, program evolution and researcher analysis turn finite computational discoveries into a proved family with independently checkable evidence.

---


### 75. [When AI Investigators Cannot Trust Their Tools: Conflict-Aware Evidence Verification for Cyber Threat Investigation](https://arxiv.org/abs/2610.41191)

**<font color=#1a73e8>作者：</font>** Yuchen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly triage security alerts by combining the outputs of several detection tools, implicitly treating those tools as trustworthy. Unlike prior work on conflicts between a model's knowledge and its context, we study conflicts among the tools themselves: what happens when this machine-generated evidence is conflicting or wrong. On the corrected CIC-IDS2017 dataset, four heterogeneous detectors emit labels and confidences that we corrupt under a threat model varying the number of corrupted tools, the persistence of the corruption, and the confidence attached to wrong outputs. Across open-weight LLMs from 3B to 14B parameters, unverified investigators are fragile: one corrupted detector out of four lowers naive accuracy to .50-.72, three lower every unverified investigator to .13 or less, and honest disagreement alone makes them abstain on up to 63% of flows. We propose Conflict-Aware Evidence Verification (CAV), built from established components: an equal-weight vote that ignores reported confidences, an evidence-conflict gate, and an independent nearest-neighbour trust check that tests the leading candidates. With its prompt frozen before testing, CAV-LLM improves on the naive investigator in every corrupted condition ($p < 0.001$), reaching .84-.88 with three corrupted detectors against at most .08, while calling the LLM on 0.4% of clean traffic. A fixed verification rule is as accurate or better unless most tools are corrupted. When we make the independent channel itself noisy, CAV inherits its errors: it stays ahead when two or more tools are corrupted, but adding the channel as an extra voter is better when at most one is. Verification thus moves trust from the tools to the check, which must be measured and protected in turn.

---


### 76. [From Evaluation to Evolution: Benchmarking Image Editing and Evolving Image Models](https://arxiv.org/abs/2610.41210)

**<font color=#1a73e8>作者：</font>** Jun He, Canmiao Fu, Ying Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world image editing requires coordinating multiple visual transformations with content preservation and reference constraints, yet aggregate scores can readily obscure unmet local requirements. Effective evaluation must therefore identify local failures and translate them into priorities for subsequent model improvement. We introduce WeGenEditBench, comprising 2,740 evaluation instances and 148 task types across single-image, text-intensive, and multi-reference editing. Pre-generated checklists shared across models decompose each request into atomic requirements; item-level deductions and visual evidence are established first and then summarized into scores for edit execution, preservation, visual quality, and task-specific correctness. To support the experience-acquisition component of recursive self-improvement (RSI), we develop WeGenEvoStudio, a unified multi-agent harness for RSI-oriented learning that integrates model-conditioned failure diagnosis, retrieval-grounded data construction, supervised adaptation, and re-evaluation. Among 15 evaluated configurations, GPT-Image-2 leads single-image editing with an Overall score of 4.076, while Seedream-5.0-Pro leads text-intensive editing at 4.291. Evolution experiments across four generation and editing benchmarks demonstrate substantial targeted gains: on their report-selected Top-5 single-image targets, FLUX.2 [dev] improves Overall from 1.083 to 3.517, while Qwen-Image-Edit-2511 gains 13.2%. Together, our benchmark and harness provide a foundation for developing more reliable image models through interpretable evaluation and feedback-driven learning.

---


### 77. [Beyond Response Scoring: An AI-aware Cognitive Supervision Framework for Automated Mathematical Short Answer Grading](https://arxiv.org/abs/2610.41215)

**<font color=#1a73e8>作者：</font>** Shengran Guo, Min Chi, Feifei Qiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based language models have achieved remarkable success in automated short answer grading (ASAG). However, current methods in ASAG struggle to comprehend, reason about and evaluate complex mathematical answers involving symbols and formulas. These score-only methods fail to generalize across diverse responses and skill states associated with identical scores. Moreover, they ignore the potential upward bias introduced by generative Artificial Intelligence (AI) usage in assessing students' performance and knowledge mastery. To address these limitations, we propose AICG (AI-aware Cognitive-supervised Grading), a two-branch multi-task framework. The first branch combines RoBERTa-based regression, ordinal, and classification heads for individual-answer grading. The second branch uses an expert-designed Q-matrix to associate responses with assessed skills and jointly predicts G-DINA-derived skill mastery and learning gain. Through the shared encoder, these skill-level targets provide cognitive supervision for answer grading beyond score labels. AICG further uses a Gen-AI detector, trained through supervised contrastive pretraining followed by linear classification, to estimate assistance probabilities and convert them into reliability weights, attenuating unreliable cognitive evidence during learning assessment. We conduct experiments on 49,402 instructor-graded responses spanning 19 academic semesters. Relative to RoBERTa regression, AICG reduces mean absolute error (MAE) by 50.3% and improves quadratic weighted kappa (QWK) from 0.798 to 0.927. Ablations identify Q-matrix-guided cognitive supervision as the primary source of improvement, while AI-aware weighting further reduces overall MAE by 4.2% over the unweighted cognitive model and consistently improves MAE and QWK across the four most recent post-Gen-AI semesters.

---


### 78. [RTL-Interact: Training EDA-Interactive Models for Multi-Task RTL Design](https://arxiv.org/abs/2610.41225)

**<font color=#1a73e8>作者：</font>** Wenxuan Shi, Yaoyu Zhu, Di Huang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models offer a promising route to register-transfer-level (RTL) design, but reliable implementations require checking and revision based on electronic design automation (EDA) tools' feedback. Existing RTL-specialized models often lack learned interaction with such EDA tools or rely on separate generation and repair components. We introduce RTL-Interact, a multi-task post-training framework that trains a single RTL-specialized model to generate RTL, construct task-appropriate EDA checks, and revise implementations using tool feedback. The framework combines automatically constructed multi-task demonstrations with staged supervision from chain-of-thought to tool-integrated reasoning. We further introduce Pattern-Aware Policy Optimization (PAPO) for multi-task reinforcement learning. PAPO augments Group Relative Policy Optimization with correctness-gated rewards that favor concise successful checking while rewarding effective revision, and uses task grouping to preserve coverage across objectives. On CVDP, RTL-Interact-32B achieves 48.7% weighted Pass@1 and 68.9% Pass@5, surpassing its teacher model, DeepSeek-V3.2, while RTL-Interact-8B achieves 44.9% weighted Pass@1. Additionally, we show that PAPO can reduce average tool calls by 63.8% while improving Pass@1. Both models also outperform all RTL-specialized baselines on VerilogEval v2 and RTLLM v2, demonstrating the effectiveness of our method.

---


### 79. [TRIDENT and SHAKTI: A Framework and Benchmark for Hindi AI-Text Detection](https://arxiv.org/abs/2610.41232)

**<font color=#1a73e8>作者：</font>** Shifali Agrahari, Sujit Kumar, Sanasam Ranbir Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) become increasingly multilingual, distinguishing human-written from AI-generated text is essential for maintaining information integrity. However, research remains English-centric, with limited benchmarks for low-resource languages such as Hindi. To address this gap, we introduce SHAKTI, a large-scale Hindi benchmark covering four genres, eight LLM families, multiple prompting strategies, and adversarial transformations. We evaluate its quality through human annotation and analyze linguistic, grammatical, and sentiment-based differences between human- and AI-generated texts. Building on these findings, we propose TRIDENT, a round-trip translation-based detection framework with three variants: TRIDENT-S (static threshold), TRIDENT-D (dynamic threshold), and TRIDENT-C (logistic regression using multi-distance RTT features). TRIDENT leverages semantic consistency between original and round-trip translated texts to identify AI-generated content. Extensive experiments show that TRIDENT outperforms conventional and supervised baselines, with TRIDENT-S achieving the best overall performance. Further evaluations across seven languages, adversarial settings, and unseen LLMs demonstrate its multilingual applicability and robustness, while highlighting sensitivity to the translation model.

---


### 80. [Experts Exhibit Structured Redundancy: Structure-Preserving Expert Pruning for Mixture-of-Experts Large Language Models](https://arxiv.org/abs/2610.41236)

**<font color=#1a73e8>作者：</font>** Tian Wang, Yongding Tao, Yihong Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse MoE mechanism significantly improves the trade-off between model capacity and inference efficiency. However, practical deployment still requires storing all experts, resulting in substantial memory overhead. We show that expert outputs in MoE layers exhibit structured redundancy. Across different models and task categories, the stable rank and entropy effective rank of expert outputs are consistently far below the nominal number of experts, while expert output distributions also exhibit fewer effective modes. Motivated by these observations, we reformulate expert pruning as a structure-preserving expert subset selection problem and efficiently optimize it via a greedy strategy, rather than only independently scoring and ranking individual experts or exhaustively searching over expert combinations. We propose two expert pruning methods under the unified structure-preserving framework: Projection Energy Expert Pruning (PEEP), which preserves the functional subspace by maximizing weighted projection energy, and Distributional Coverage Expert Pruning (DCEP), which preserves the distributional geometry by minimizing weighted coverage error. Both methods incorporate router-derived weights as priors, enabling them to jointly preserve the global structural relationships among experts while accounting for the local importance of individual experts. Experiments on DeepSeek-V2-Lite and Qwen3-30B-A3B demonstrate that, at the expert retention ratios of 75% and 50%, our methods outperform the state-of-the-art baselines on the majority of benchmarks and consistently achieve the best average performance across both general tasks and mathematical reasoning tasks.

---


### 81. [MEMIG: Self-evolving Memory Construction for Antibody Optimization](https://arxiv.org/abs/2610.41245)

**<font color=#1a73e8>作者：</font>** Yunhui Jang, Zach Wang, Jai Doshi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory has become central to self-evolving LLM agents, which store and retrieve experience from past rollouts to guide future decisions. Existing systems represent this experience as free-form natural language and maintain it by rewriting, which fits tasks whose experience is narratable. However, in scientific discovery and optimization, experience is often a quantity measured by an oracle under a specific context. Rewriting it as text leaves no index for where a record should be, replaces a measurement with a description, and cannot express how interventions interact. To address this, we argue that agent memory for biomolecule optimization should instead be indexable, quantitative, and structured, and we introduce MEMIG. This memory construction framework realizes these three properties. In detail, MEMIG addresses each insight with a domain-grounded identifier and accumulates the quantitative effect measured by a property oracle, so that updates remain local and retrieval becomes an exact lookup. Next, MEMIG connects insights whose interventions are applied together and measures their epistasis by decomposing each evaluated set. Our results show that MEMIG improves performance in most settings across in silico antibody optimization tasks.

---


### 82. [Hawkeye: Reading Illegible Text with Vision Language Models](https://arxiv.org/abs/2610.41254)

**<font color=#1a73e8>作者：</font>** Brian Tang, Kang G. Shin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While modern Vision-Language Models (VLMs) have been remarkably successful in general scene text recognition, they consistently struggle with the long-tail distribution of text that is degraded by motion blur or low resolution. These limitations are particularly apparent in egocentric applications like smart glasses, where text is often captured in noisy environments. In this paper, we introduce the \textbf{BSTRB} (Blurry Scene Text Recognition Benchmark), a novel benchmark of 8,398 noisy image samples with high-fidelity annotations derived from 1,699 real-world video sequences. To support this, we present \textbf{Hawkeye}, a VLM fine-tuned on BSTRB to read and reason about illegible text by leveraging contextual priors and pixel-level alignment. Our results show that \name matches much larger VLMs on BSTRB overall and exceeds them on text at or below 20 pixels, in a single pass suited to real-time deployment. We characterize the resolution at which current VLMs begin to fail.

---


### 83. [ReVEAL: Eliciting Role-Aware Latent Visual Evidence from MLLMs for Reasoning Video Object Segmentation](https://arxiv.org/abs/2610.41257)

**<font color=#1a73e8>作者：</font>** Zhongyuan Bao, Cunjie He, Lejun Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning video object segmentation (ReVOS) requires segmenting the target specified by an implicit query throughout a video. Existing MLLM-based methods typically require costly cross-model alignment, tying MLLM training to a downstream segmentation model. We present ReVEAL, a decoupled thinking-with-video framework for ReVOS that elicits role-aware latent visual evidence from MLLM reasoning to directly guide segmentation. ReVEAL introduces Visual Evidence Tokens (VETs) into video reasoning to associate necessary visual regions or entities with target, background, or distractor roles, while a Dynamic Attention Layer Router adaptively aggregates VET-to-video attention across layers into role-specific grounding evidence. We train the MLLM to perform VET-augmented reasoning on our constructed ReVEAL-47K dataset, with a Contrastive Attention Grounding Loss as auxiliary supervision to apply role-specific constraints to VET attention and optimize layer routing for reliable latent grounding. At inference, ReVEAL identifies the target through this thinking-with-video process and fuses the resulting role-specific evidence to guide a frozen SAM2 in predicting target masks. Experiments on five benchmarks show that ReVEAL outperforms alignment-free baselines and remains competitive with alignment-based methods.

---


### 84. [SketchDirector: Complex Scene Sketching via Agentic Layout Reasoning and Detail Refinement](https://arxiv.org/abs/2610.41260)

**<font color=#1a73e8>作者：</font>** Yiqi Liang, Xiaodong Cun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing sketch generation methods often rely on image guidance and are largely limited to individual objects or simplified scenes, leaving text-guided complex scene sketching underexplored. We present SketchDirector, an agentic framework that mimics the human sketching workflow for automatic multi-concept scene sketching. Given a scene-level text prompt, SketchDirector first employs a large language model~(LLM) to decompose the scene into multiple draft assets, where each is represented by a set of Bézier curves. Then, an agentic reasoning loop iteratively plans and executes their spatial arrangement, guided by self-evolving memory. Finally, a detail refinement module leverages diffusion priors to enhance sketch quality while preserving geometric structure. To support future research and applications in multi-concept scene sketch generation, we further introduce the \textit{MCSketch8K} dataset, comprising editable vector assets, compositional layouts, and object-level manipulation annotations. Extensive experiments show that SketchDirector outperforms state-of-the-art baselines in semantic and compositional quality while effectively preserving overall contour organization during refinement. The project page is: \href{this https URL}{this https URL}.

---


### 85. [Rome Wasn't Built in One Turn: Replay-Grounded Reward Signals for Long-Horizon Freeciv Agents](https://arxiv.org/abs/2610.41264)

**<font color=#1a73e8>作者：</font>** Yanchen Liu, Xinyu Che, Brihi Joshi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training language-model agents to play long-horizon strategy games is hard because deterministic feedback is sparse and often arrives only at the end of a game. In-game scores can offer dense signals, but they do not reliably predict future outcomes: in 8-68% of position pairs across eight strategy games, the higher-scoring position leads to the worse outcome. We term this phenomenon scoreboard traps. In Freeciv, an open-source turn-based empire-building game where several players manage units, cities, and diplomacy over hundreds of turns, we look into better reward signals for gameplay agents. To facilitate this, we build CivHarness, an open system that saves current game states, branches on different decisions, and replays the game to future turns to provide measurable long-horizon feedback from saved positions. We use CivHarness to train CivTelescope, an LLM Judge that predicts which one of two game positions will yield the better outcome. On scoreboard-trap pairs, CivTelescope is 1.3-2.0 times more accurate than off-the-shelf language models, and it generalizes to new game starts, later turns, and unseen rules. We then train a Freeciv gameplay agent with CivTelescope as a dense reward, and call this recipe CivMarshmallow. When used in the middle stage of the game where scoreboard traps are common, CivMarshmallow reaches an average training phase gain of 8.94 points, 77% more than the best baseline, the end-of-game reward. Over the full 120-turn game, CivMarshmallow uses a hybrid reward that starts from the scoreboard or the end-of-game reward and shifts to CivTelescope as the game advances; this hybrid reward scores highest among the rewards we compare.

---


### 86. [ANGLER: Verifier-Grounded Benchmarking with an Adaptive Attacker for Web Agents](https://arxiv.org/abs/2610.41272)

**<font color=#1a73e8>作者：</font>** Yini Huang, Aiwen LU, Zhen Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web agents are increasingly deployed to complete tasks autonomously on real websites, where adversarially injected content can induce them to perform unauthorized actions. Existing evaluations primarily use fixed attacks or focus on a single attack type, and evaluate attacks at the text level rather than through real state changes, thus underestimating how vulnerable agents are to diverse attacks. To address the gap, we introduce REEF, a benchmark of red-teaming executable environments with faithful verification for measuring the security vulnerabilities of web agents. REEF covers 9 verifier-grounded websites spanning travel, commerce, productivity, media, and communication, and pairs every authentic benign task with a malicious objective delivered through 5 attack types at both the user and the environment level. REEF's state-based verifiers provide the execution feedback that drives ANGLER, an adaptive near-miss-guided lure evolution framework for red-teaming. Rather than evaluating a fixed attack set, ANGLER uses outcomes from prior rollouts to guide LLM-based attack mutation and candidate selection, prioritizing near-miss seeds during refinement. Across 8 VLM-based web agents, ANGLER achieves an end-to-end attack success rate (ASR) of 20.36%, compared with 15.24% for the non-adaptive setting. Compared with attack-free execution on the same benign tasks, attacks generated by ANGLER reduce benign task success rate (BSR) from 61.9% to 44.4%.

---


### 87. [PsyInterviewee: Informational Invariance and Relational Adaptivity in Mental Health Interview Simulation](https://arxiv.org/abs/2610.41289)

**<font color=#1a73e8>作者：</font>** Jiawei Zhang, Huachuan Qiu, Ruocheng Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based simulated interviewees support interviewer training and the evaluation of mental health interviewing systems. Existing studies have primarily focused on improving human-likeness through richer patient profiles and behavioral modeling. However, human-likeness alone does not establish their reliability. Reliable simulation requires preserving profile-grounded clinical facts (informational invariance) while adapting disclosure and interaction behavior to the interview (relational adaptivity). To this end, we introduce PsyInterviewee, which separates a protected truth channel from a dynamic interaction channel and verifies generated clinical claims against the profile. Specifically, asymmetric write permissions allow dialogue context to update disclosure and behavioral states without authorizing new clinical facts; these states guide what profile-supported information is revealed and how it is expressed. In an automated evaluation of interactions between LLM-based interviewers and interviewees, PsyInterviewee achieves higher scores than four representative baselines on most metrics across both axes, as assessed by two LLM judges. Ablations suggest that the two channels contribute to clinical grounding and response modulation, respectively.

---


### 88. [In-Model Context Compression with Agentic Soft Tokens for Long-Horizon LLM Agents](https://arxiv.org/abs/2610.41291)

**<font color=#1a73e8>作者：</font>** Xuning He, Kai Fan, Runyu Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents play an important role in solving complex and sustained tasks, with ever-growing interaction contexts. However, these accumulated contexts will raise substantial computational cost and obscure key decision-relevant evidence. Existing methods typically train external compressors or context-management agents to rewrite context as shorter hard-token sequences, but such external selection may not align with the LLM's evolving representation and is necessarily lossy. In this paper, we introduce Agentic Soft-Token Compression (ASTC), a training-free compression method using soft tokens within LLM agent for long-horizon tasks. Specifically, ASTC uses the model's native recurrent dynamics to determine the already absorbed information, leveraging the commonly-used hybrid Gated Delta Network (GDN)-attention. It then carries this information forward as agentic soft tokens while retaining exact values as hard tokens. The resulting compact sequence reduces later-layer computation and yields reusable KV caches, extending the savings across the agent's trajectory. Extensive experiments on long-horizon tasks show that ASTC matches or exceeds the uncompressed agent's accuracy with up to 50.68% fewer end-to-end Attention Pairs, while trained compressors require 15.4 to 103.7 times more Attention Pairs per successful task. These findings highlight agentic soft tokens as a model-native way to carry absorbed context forward as the task representation evolves.

---


### 89. [From Transcription to Reformulation: Defining and Benchmarking Grounded Generative Speech Recognition](https://arxiv.org/abs/2610.41292)

**<font color=#1a73e8>作者：</font>** Qing Wang, Qihan Hu, Hang Lv 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech language models have expanded automatic speech recognition (ASR) from transcription to general speech-to-text generation. Yet existing benchmarks still assume a single ground-truth transcript per utterance, an assumption that struggles when models produce readable, formatted, or structured outputs. In this work, we introduce Grounded Generative Speech Recognition (GSR), reformulating speech recognition as generating semantically grounded text instead of a single transcript. We define a grounded reformulation space that characterizes all valid textual realizations supported by the input speech, and establish a four-level hierarchy of reformulation capabilities, including literal transcription, canonical reformulation, semantic reformulation and speech-grounded structuring. Based on this formulation, we present GSR-Bench, the first comprehensive benchmark designed to evaluate generative speech recognition systems beyond exact transcript matching. GSR-Bench covers diverse scenarios including refined meeting transcription, cross-dialect translation, context-aware speech understanding, and robustness under silent or noisy acoustic conditions. To address the limitations of word-level evaluation metrics, we develop a multi-dimensional evaluation framework combining speech grounding assessment and LLM-based semantic judgment, whose reliability is validated through human preference studies. Extensive experiments across representative architectures, ranging from conventional ASR systems to end-to-end Speech-LLMs, reveal fundamental trade-offs between transcription fidelity and generative reformulation ability. Our analysis further identifies critical failure modes, including acoustic hallucination, unsupported generation, and instruction drift, providing insights into the design and evaluation of future grounded generative speech systems.

---


### 90. [Self-Improvement with Auxiliary Rewards: Learning from Verified Traces and Evaluating Transfer](https://arxiv.org/abs/2610.41296)

**<font color=#1a73e8>作者：</font>** Minju Gwak, Alan Ritter  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Answer-level rewards cannot distinguish reasoning traces with equally correct outcomes. We study whether auxiliary trajectory preferences improve small-language-model self-improvement and transfer under limited supervision. We compare confidence-based (SC) and entropy-based metrics (UID-Conj.), which combines global entropy variation and local smoothness, through online reward augmentation and offline training on correct responses. Online experiments adapt Qwen3-1.7B on 30 AIME problems without reference answers; offline experiments use historical AIME problems. UID-Conj. improves the online macro-average across the adaptation benchmark and three transfer benchmarks by 2.08 percentage points over unmodified TTRL. The strongest evidence comes from offline weighted SFT: UID-Conj. exceeds uniform weighting on the same response pool by 1.93 points, with a paired prompt-bootstrap 95\% CI of [0.44, 3.44]. Benefits are task-dependent: SC rewards judged trace quality and instruction following, while UID-Conj. rewards yield stronger training outcomes in several settings. We find that auxiliary preferences can expose learning value among equally correct traces not captured during inference time, motivating their evaluation through downstream gains.

---


### 91. [Subliminal Reinforcement Learning: traits travel through a judge's scores](https://arxiv.org/abs/2610.41301)

**<font color=#1a73e8>作者：</font>** Keuntae Kim, Yong Suk Choi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Subliminal learning, the transfer of a model's trait through data with no semantic trace of it, has been shown for students trained on a teacher's text. Post-training relies on group relative policy optimization with a language-model judge, where the student learns only from its own outputs and one judge's scores. We show this suffices: a student writes invented syllables or numbers, a judge made to prefer one animal scores them, and the student's preference moves toward that animal relative to a run whose judge prefers another. Of 48 design cells, two fail the validity gate and 17 establish the trait at 5% false-discovery rate, numbers-only cells included; elsewhere, our account gives the reason. Removing only the reward difference between judges removes transfer. We establish the principle as a chain of four stages: the trait must show in the judge's scores, favour strings that move the student, accumulate and reach the answers. Judges with the same preference built from other data, or on another model, place it on other strings, and transfer is not detected. Carried unchanged to AI-safety dispositions, the chain holds: undesirable dispositions reach the student's answers, and stages measured before training anticipate where, helping to prevent part of this risk.

---


### 92. [SERIAL-7: Deriving, Realizing, and Preserving Machine-Verifiable Outputs Across Representations](https://arxiv.org/abs/2610.41308)

**<font color=#1a73e8>作者：</font>** Youngkyung Seo, MiHyeon Kim, Jisoo Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly generate structured outputs consumed by programs and downstream systems, where semantic correctness alone does not guarantee reliable execution. We introduce SERIAL-7, a Korean-English benchmark built around an executable verification framework for machine-verifiable generation across seven representations. Using 177 validated canonical artifacts, SERIAL-7 separates semantic derivation (Derive), constrained artifact generation (Realize), and cross-representation preservation (Preserve). Its 43 atomic representation constraints are paired with executable checks over format, structure, and task-specific semantics, enabling progressively stricter verification from representation compliance to full artifact validity. Across ten models, REALIZE-L3 HSR ranges from 42.0% to 93.9%, while Full Compliance exposes additional artifact-level failures beyond correct final answers and valid representations. These results show that reliable structured generation requires explicit, executable verification of how artifacts are realized and preserved across representations.

---


### 93. [GenDSR: Transferring Representations from Video Generation Models for Dynamic Spatial Reasoning](https://arxiv.org/abs/2610.41314)

**<font color=#1a73e8>作者：</font>** Ke Yang, Zhenyu Zhang, Jun Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic spatial reasoning is essential for connecting visual intelligence to thephysical world, yet remains challenging for vision-language models (VLMs), which must preserve scene state while tracking how spatial relations evolve over time. Meanwhile, video generation models (VGMs), trained to synthesize temporally coherent world dynamics, offer a rich source of spatiotemporal representations. We present GenDSR, a framework that transfers intermediate representations from VGM into VLM for dynamic spatial reasoning. Rather than treating a VGM feature as a monolithic prior, GenDSR constructs two complementary branches: a raw branch preserving holistic generative context and a delta branch emphasizing temporal variation. Task-conditioned tokenwise gates then fuse both signals and inject the result into the native visual representation. On DSR-Bench, GenDSR achieves 67.2%, surpassing the previous best result and establishing a new state of the art.

---


### 94. [StrictPRMBench: A Replayable Evaluation Benchmark for Auditing Fixed-Score PRM Aggregation](https://arxiv.org/abs/2610.41333)

**<font color=#1a73e8>作者：</font>** Pengfei Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Process reward models (PRMs) score reasoning steps, but best-of-N selection also requires a rule that aggregates those scores. We study that rule as a separate evaluation object. StrictPRMBench fixes mathematical reasoning pools, scorer evidence, and the source trace of a deletion intervention, so that different reducers face the same recorded selection problem. Across seven scoring checkpoints and two benchmarks, the stored N=32 outcomes give higher deletion-induced selection instability for product than geometric mean (GM) in all 14 cells. The equal-cell difference is +0.0965; a shared-problem bootstrap, conditional on these checkpoints and frozen pools, gives a 95% interval of [0.0846,0.1086]. A pre-injection-defined sensitivity excludes replacement slots that are either reducer's clean winner and retains 4,459 of 4,622 cell-problem records. The retained difference is +0.0986 [0.0875,0.1098]. Effects are heterogeneous: the two Qwen cells have positive percentile-bootstrap intervals on retained support but two-sided exact paired p-values of 0.0625 and 0.0703. Clean-pool Qwen accuracy does not detect a product advantage, but this is not an equivalence result. We provide versioned outcome records, CPU reanalysis, and an explicit evidence-availability contract. The contribution is a diagnostic evaluation protocol and a reproducible audit of recorded selector behavior, not a new PRM, a universally optimal reducer, or evidence of deployment-wide harm. Raw-score replay and outcome-record reanalysis are distinguished: missing primary edited-score vectors limit independent evaluation of new reducers under the same stress.

---


### 95. [Operon-S1: a fast decision controller for long-horizon biomedical agents](https://arxiv.org/abs/2610.41350)

**<font color=#1a73e8>作者：</font>** Genoria AI Team, Yuejie Hou, Yueyuxiao Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents now carry out long scientific work in biology, but their judgements about conventions, skills, errors, evidence and stopping are made inside the reasoning that does the work, where they cannot be measured, replaced or improved on their own. Here we present Operon-S1, a fast decision system, a System 1 for the agent, that separates judging from doing. A decision harness poses the agent's recurring judgements as closed questions at 13 decision points and acts only through fixed messages that never contain an answer, so any model that answers the questions can serve as the judge. Across seven life-science benchmarks, a local decision model took over these judgements in 0.6 s at the median for an in-loop request on CPU at no request cost, with no measurable change in the agent's score on five of six benchmarks, whereas the general language model that drives the agent, asked the same questions, accounted for 8.0% to 35.2% of task cost. Every decision is recorded with its consequence. Retraining on labels from task construction, verifiers or execution raised decision accuracy on every question in each of three trained versions, and a new version enters service only through a promotion gate. Task-level results in this study use the public checkpoint. The same closed decisions serve wet-laboratory protocol troubleshooting and the design of a germline target enrichment panel. Like the regulator of an operon, which switches genes on and off without making their products, Operon-S1 steers the agent without doing its work, and makes the agent's judgements a layer that can be measured, replaced and trained.

---


### 96. [Do Transaction Prices Reflect Visual Preference? A Diagnostic Study with Multimodal Language Models](https://arxiv.org/abs/2610.41358)

**<font color=#1a73e8>作者：</font>** Fengxian Ji, Jingpu Yang, Fan Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing visual preference evaluation relies on costly human annotations or preference reward models, whereas online marketplace transaction prices are readily available and reflect real purchasing behavior, offering potential low-cost supervision. However, transaction prices conflate visual preferences with non-visual factors such as provenance, demand, and competition, making aggregate accuracy insufficient to distinguish model errors, unreliable price signals, and protocol confounds. To address this identifiability challenge, we introduce MarketImage, a diagnostic framework that identifies when transaction prices reflect visual preferences, where they fail, and whether multimodal language models can recover human-supported visual preference signals. MarketImage comprises three components: (i) MarketImageArt, 266 six-image comparison sets with transaction prices and price-blind human rankings; (ii) MarketImageLens, a tie-preserving protocol that partitions 3,990 within-set image pairs into price-human agreement, conflict, and price-tie regions while separately auditing presentation-order effects; and (iii) MarketValuator, six elicitation methods spanning direct comparison, independent scoring, budget constraints, and multi-agent aggregation to evaluate signal recovery by static visual scorers and three multimodal language models. Experiments show that only 24.2% of image pairs have a non-tied price direction, of which 34.7% agree with the human majority. Within this region, HPSv2 leads at 66.4% Recoverable Accuracy; Qwen's budgeted and aggregated variants trail baselines, while GPT interface gains remain statistically unresolved. Thus, transaction prices encode recoverable visual preferences only under limited conditions and should be treated as uncertain proxies rather than ground truth.

---


### 97. [LEAP: Efficient LLM Inference Scheduling with Generalizable Length Prediction](https://arxiv.org/abs/2610.41359)

**<font color=#1a73e8>作者：</font>** Kwan Yan, Jialun Zhong, Yanzeng Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Length-aware scheduling reduces request latency in LLM serving by prioritizing shorter requests. However, despite their large model sizes, length predictors can suffer degraded ranking performance under domain and task shifts, and adapting them can require costly retraining. Their prediction overhead can further offset the benefits of scheduling. To improve the generalization and efficiency of length-aware scheduling, we propose \textbf{LEAP}, a length prediction system with fast online adaptation and asynchronous CPU execution. LEAP reuses the serving model's prefill hidden states, which contain information about the output length, and extracts this signal through a linear readout. To adapt to substantial domain and task shifts, it updates the readout at test time through recursive least squares, using completed requests as supervision without gradient computation or historical-data replay. Prediction and updates run asynchronously on CPU, while prediction and initial batch ordering overlap the remaining GPU prefill. Across the evaluated cross-domain transfers, LEAP retains strong ranking performance, and online adaptation improves Spearman correlation by 64.7\% under a larger domain shift. Serving experiments show that LEAP reduces average per-token latency by 15.9--40.8\% compared with the evaluated length predictors, while achieving 1.9\% higher throughput with $30{,}569\times$ fewer predictor parameters than the strongest evaluated baseline.

---


### 98. [What We Keep of What We Forget: Replacement Operators and Routing Semantics in Training-Free MoE Expert Pruning](https://arxiv.org/abs/2610.41366)

**<font color=#1a73e8>作者：</font>** Ezza Ali, Sehrish Bibi, Momina Moetesum 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training-free expert pruning makes two decisions: which experts to remove, and what the layer computes when its router still selects a removed expert. Published methods change both at once. Holding the mask fixed, we compare replacement operators from three families on OLMoE, DeepSeek-V2-Lite and Moonlight, with Granite as a fourth router, using paired, multiplicity-corrected tests. The largest effect is a choice usually left implicit: the survivors' gate scale. On routers trained without top-k renormalization, renormalizing the survivors' gates, a common implementation choice, costs 0.8-8.5 points and reverses whether rerouting beats MoNE's mean-output replacement; on two routers trained with renormalization, the trained scale wins at 50% pruning. We introduce the tilted novice, a closed-form low-rank map of the pruned expert's input whose rank-0 case is MoNE's constant. At 50% pruning it adds 1.2-1.8% parameters and gains 3.45 and 1.37 points over the constant on OLMoE and Moonlight, stable across calibration draws and largely unchanged by 4- and 3-bit quantization. No operator dominates: trained-scale rerouting is best on DeepSeek-V2-Lite, and a partial copy of each pruned expert is statistically indistinguishable from the tilted novice on two models. Evaluation can change conclusions: at 25% pruning MoNE's constant keeps 92-97% of dense multiple-choice accuracy but only 5-65% of GSM8K and 0-17% of code scores, and the calibration domain moves the mask 4-9 times more than resampling. We propose a five-item reporting checklist.

---


### 99. [When History Overrides Intent: Relational Schema Lock-In in Human-LLM Interaction](https://arxiv.org/abs/2610.41367)

**<font color=#1a73e8>作者：</font>** Wei Yang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Long-context interaction and persistent memory allow LLM assistants to develop history-grounded understandings of users. When users change direction, however, an understanding built through earlier exchanges may conflict with their current instruction. We introduce relational schema lock-in to describe cases in which an assistant grants that accumulated understanding authority to override the current instruction without user authorization for the intervention. Study 1 documents reports of AI assistants using prior interactions to question or alter requested actions. Study 2 reproduces the pattern across controlled histories and six models: models retained history-grounded positions but differed in whether and how those positions shaped task execution. In Study 3 with 360 participants, artifact substitution preserved task completion while reducing faithful enactment: 75.0% sent the AI's suspension letter, including 11 participants who reported cancellation as their final stated intent. Overt resistance reduced task completion while leaving sent artifacts faithful.

---


### 100. [RECITE: Revising Eligibility Criteria Incorporating Textual Evidence](https://arxiv.org/abs/2610.41368)

**<font color=#1a73e8>作者：</font>** Russell Ro, Reza Abbasi-Asl  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Overly restrictive eligibility criteria contribute to widespread enrollment failure in clinical trials, yet published recommendations for how specific criteria should be broadened remain disconnected from trial design at scale. We introduce RECITE (Revising Eligibility Criteria Incorporating Textual Evidence), a framework for automated discovery, extraction, and implementation of evidence-based eligibility criteria revisions. RECITE uses protocol amendment documents from this http URL to construct a dataset of 11,913 curated instances across 5,735 trials, each pairing original criteria with documentary evidence and target revisions. We benchmark fifteen LLM configurations under truncated-to-context-window and retrieval-augmented generation conditions, on a 3,116-instance sample under an LLM-as-judge protocol validated against ten domain experts (judge vs. human quadratic-weighted Cohen's $\kappa_{qw} = 0.694 \pm 0.096$). The best open-weight model, Gemma 2 9B, achieves $\kappa_{qw}$-aligned ordinal score $3.0 \pm 0.9$ on a 0--4 scale (normalized 0.742) and the best closed-weight model, GPT-4o, reaches $3.0 \pm 0.8$ (normalized 0.745). Using an agentic literature discovery system, we then identified 44 paper--trial matches across five publications providing trial-design and EC-modification evidence. Our findings suggest that existing clinical knowledge can be operationalized into actionable trial design recommendations.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-188](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
