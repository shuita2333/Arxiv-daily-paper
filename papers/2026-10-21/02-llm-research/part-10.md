# 🧠 大模型相关研究 | 2026年10月21日

> 本类共 **548** 篇论文：已确认 **507** 篇，待复核 **41** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-548](./part-11.md)

---

### 451. [Training Negatives Still Matter After Calibrating Answerability Readouts](https://arxiv.org/abs/2610.26461)

**<font color=#1a73e8>作者：</font>** Jinchen Zhang, Zheyuan Liu, Yihan Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Answerability readouts predict whether a passage supplies an answer, but whether calibration can compensate for removing negative passages during training remains unclear. We present a controlled study of how training-negative construction affects calibrated prediction, ranking, and downstream answer retention. We compare native training, which retains negative passages, with empty training, which removes them, holding questions, labels, positive examples, and model weights fixed. Both are calibrated on the same labeled native examples. On SQuAD 2.0 and RepLiQA, native-trained logistic readouts at selected depths achieve lower Brier loss for Qwen2.5-7B-Instruct and Gemma-2-9B-it, with or without output scores. Native fusion also outperforms calibrated output alone. Post-hoc AUROC analysis shows better ranking under native training, beyond what threshold adjustment alone can explain. On the official SQuAD 2.0 development set, native readout policies improve F1 over empty policies but retain more answers to unanswerable questions. The advantage varies by estimator and depth, while RepLiQA's text shortcuts limit claims about contextual understanding. Unfinished generations prevent complete answer-level evaluation, although worst-case bounds preserve the native-empty F1 gains. Our findings show that training negatives affect ranking and downstream decisions even after common calibration, without establishing a universal advantage for native training.

---


### 452. [VeriCUA: Learning Proactive Verification for Reliable GUI Agent Rewards](https://arxiv.org/abs/2610.26469)

**<font color=#1a73e8>作者：</font>** Zhizhou Wang, Yaxi Lu, Zhong Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for computer-use agents increasingly relies on proactive reward agents that interact with the post-execution GUI environment to verify what recorded screenshots cannot reveal. The reliability of such verification hinges on two coupled decisions: what to check and when to stop. Existing methods leave these decisions to prompted foundation models. However, neither scaling up the model nor providing few-shot examples reliably improves verification: prompted Judges ranging from 4B to GPT-5.4 all plateau at 68%-70% macro-average agreement. This is because the value of a check depends on the environment rather than the task alone, and becomes apparent only through execution. Learning from execution is itself constrained, as the Actor's terminal state cannot be faithfully replicated during training, allowing only one verification attempt per state. We introduce VeriCUA, a proactive reward agent that learns its verification strategy from these single attempts. A trainable Judge decides what to check and when to stop, while a frozen Probe executes the checks in the live environment. Online reinforcement learning optimizes the Judge for both verdict correctness and efficient Probe use, with returns normalized across terminal states. Trained only on OSWorld and evaluated without further training on MobileWorld and WebArena-Verified, VeriCUA achieves the highest reward agreement across all three benchmarks and lies on the agreement-cost Pareto frontier among proactive verifiers. It surpasses few-shot GPT-5.4 by 5.36 points with 47.6%-59.8% fewer Probe tokens, and even a 1B VeriCUA exceeds every prompted Judge. As the reward for Actor RL, it raises task success by 3.21 points overall and 5.40 points on held-out multi-application tasks. These results identify the verification strategy, not verifier scale, as the key to reliable GUI rewards.

---


### 453. [AfriGuard: Safety and Robust Refusal For African Languages](https://arxiv.org/abs/2610.26474)

**<font color=#1a73e8>作者：</font>** Israel Abebe Azime, Jesujoba O. Alabi, Iffat Maab 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) designed to interact with users are typically trained to respond appropriately to harmful or toxic content. However, ensuring appropriate responses becomes more challenging in diverse linguistic and cultural contexts, where safety risks may be expressed or interpreted differently. Building safe AI systems therefore requires detecting safety risks, understanding their nature, and responding appropriately, while accounting for linguistic and cultural variations that add complexity to each stage. In this work, we introduce AfriGuard, a culturally grounded multilingual dataset for studying harmful intent, safety-category understanding, and refusal behavior across 10 African languages and English. Our findings reveal that guardrail models underperform both open- and closed-source LLMs on safety-intent and safety-category classification, while models show limited understanding of appropriate safety behavior, scoring below 60% F1. We further find that models often fail to respond appropriately to unsafe prompts not because they explicitly refuse, but because they produce linguistically inadequate responses that result in incidental non-assistance rather than proper refusals. Finally, using AfriGuard, we develop efficient guardrail models that achieve performance competitive with models up to 30x larger, introduce refusal detectors that improve average performance by 43.9% over existing detectors, and demonstrate that supervised fine-tuning can substantially improve overall safety performance.

---


### 454. [Promptile: Recovering and Reusing Prompting Strategies from LLM Interaction Histories](https://arxiv.org/abs/2610.26485)

**<font color=#1a73e8>作者：</font>** Qingyang Wan, Chang Liu, Zhoutong Ye 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As people use large language models (LLMs) over time, they develop their own ways of prompting to achieve desired results. These useful experiences often remain scattered and unorganized across conversations. Yet existing personalization approaches primarily capture user preferences or explicitly defined workflows. Through a formative study, we found that users develop prompting strategies that range from implicit instructions to explicit templates from these experiences. We further find that interaction behaviors provide evidence for these strategies, which can be decomposed and recombined for reuse across tasks. Building on these findings, we present Promptile, a framework that identifies and validates users' prompting strategies from interaction histories. Promptile organizes these strategies into reusable components that can be retrieved, combined, and adapted to users' current tasks. Our evaluation shows that Promptile accurately recovers and reuses these strategies, better aligning model outputs with users' expectations while reducing repetitive prompting effort.

---


### 455. [Strength Controls Change How Interventions Compare Across Sparse Autoencoder Codes](https://arxiv.org/abs/2610.26489)

**<font color=#1a73e8>作者：</font>** Jinchen Zhang, Zheyuan Liu, Yihan Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Changing sparse autoencoder (SAE) codes can alter both intervention direction and magnitude, so comparing intervention effects requires a strength control specifying what is held equal. Norm matching and output calibration provide different controls, but whether interventions yield different effects across codes after strength matching remains unclear. We compare intervention effects under these controls for fixed feature groups in Gemma and Llama and observe: (1) Whole-patch scaling. With one coefficient per input, full-output Kullback-Leibler (KL) calibration leaves smaller mean effect gaps from the encoder-based reference intervention than total-norm matching for nonnegative least-squares (NNLS) refits. On new Llama inputs, total-norm matching loses 11 reference transfers, whereas full-output calibration preserves every transfer decision. (2) Positionwise scaling. On a small matched gender-agreement subset, positionwise norm matching leaves smaller observed mean gaps than full-output calibration. (3) Answer exclusion. Compared with unscaled NNLS, answer-excluded calibration reduces gaps in the measured subject-verb agreement comparisons but increases them for gender refits. Full-output KL calibration also reduces larger gaps for norm-matched constructed candidates, although matching coverage is incomplete in several settings. Since calibration uses the evaluated input's outputs, it serves as a diagnostic of residual disagreement.

---


### 456. [Mitigating Reward Hacking in Preference Reward Models with Evolving Penalties](https://arxiv.org/abs/2610.26496)

**<font color=#1a73e8>作者：</font>** Afonso Baldo, António Farinhas, Marcos Treviso 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for language models has moved from preference reward models to verifiable rewards, which sustain much longer optimization. Preference models are prone to reward hacking: the policy raises their score without improving response quality, or even while degrading it. Yet for open-ended tasks, where quality can neither be verified nor fully written down as rubrics, they remain valuable. We introduce Dynalize, which mitigates reward hacking online, during policy training. Periodically and asynchronously, a language model analyzes training rollouts and writes penalties for undesirable behaviors that the reward model appears to reward; a judge applies them to every rollout. In clinical counseling and creative writing, training on the reward model alone raises its score continuously but ultimately leads to a decline in external benchmarks. Dynalize sustains longer training and results in improved downstream performance. For example, we find that our method suppresses patterns incentivized by preference models that, without penalties, spread to most responses, and even to the model's reasoning, which the reward model does not explicitly score. Furthermore, we show that its gains hold in multi-turn training, and even after we retrain the reward model on the discovered behaviors.

---


### 457. [ScopeMem: Latent Memory That Learns Where to Revise Frozen GUI Agents](https://arxiv.org/abs/2610.26503)

**<font color=#1a73e8>作者：</font>** Zhicheng Zheng, Cheng Zhang, Shengping Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent memory is gaining ground as a lightweight history supplement for GUI agents. It supplies history to a frozen vision-language model via prefix vectors trained with step-wise cross-entropy (CE). While resulting gains are naturally attributed to encoded history, our controlled experiments show they primarily stem from action revision. The prefix learns to alter the model's default actions. However, this revision is unscoped because step-wise CE pushes outputs toward reference actions at every step without explicitly preserving correct decisions. Consequently, it repairs errors but also breaks 8-13% of initially correct answers. Overall accuracy metrics hide these losses. We therefore propose ScopeMem, a latent-memory method for scoped revision. Its encoder conditions prefix generation on the model's initial answer and is trained to correct errors while preserving correct decisions. On the controlled ablation set, ScopeMem reduces the share of broken correct decisions to 5.6% while repairing more errors than any evaluated CE-trained prefix. On AndroidControl, GUI-Odyssey, and zero-shot AITW, ScopeMem outperforms all evaluated prompting and latent-memory baselines, enabling a frozen Qwen3-VL-8B to match or surpass GUI-specialized agents and Qwen3-VL-32B.

---


### 458. [RouterWorld: Scaling Conversational AI with Latency-Aware LLM Routing](https://arxiv.org/abs/2610.26511)

**<font color=#1a73e8>作者：</font>** Jinyang Li, Denis Emelin, Simone Tedeschi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational AI systems built on Large Language Models (LLMs) require routing mechanisms that balance answer quality and response latency at scale. However, existing LLM routing benchmarks assume full observability of all candidate model outcomes, under-emphasize latency as a first-class metric, and fragment evaluation across heterogeneous protocols misaligned with real-world settings. We introduce RouterWorld, a comprehensive benchmark for LLM routing in conversational GenAI. RouterWorld unifies 371k single-turn responses and 76k multi-turn agentic trajectories, adopts natural user interactions with a standardized LLM-as-a-judge protocol, and decouples efficiency from transient pricing via hardware-grounded latency annotations. Crucially, RouterWorld formalizes routing under partial observability through two setups: Cold-Start, which restricts learning to sparse, static logs, and Voyager, which models continuous data streams where routing decisions shape future training distributions. Evaluating 13 routing baselines, we find that most routers over-emphasize accuracy while ignoring latency under partial observability. Code and benchmark data are publicly available.

---


### 459. [Beyond Behavioral Accuracy: Evaluating Individual-Level Fidelity in LLM Investor Simulation](https://arxiv.org/abs/2610.26524)

**<font color=#1a73e8>作者：</font>** Jiajie He, Yuanhong Jiang, Xintong Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as user simulators, but can they faithfully reproduce an individual's behavior and decision logic over time? We investigate this question in a longitudinal paper-trading study with 80 participants. Using rolling next-day predictions, we evaluate trading activity, buy-sell structure, asset selection, and portfolio outcomes, complemented by controlled input ablations and participant-rated explanation alignment. No evaluated LLM reliably outperforms a simple recent-activity persistence baseline for predicting trade occurrence, while buy-sell structure and asset selection remain difficult to reproduce. Similar activity-level performance can also yield substantially different portfolio trajectories. Ablations show that activity predictions depend primarily on recent trades, whereas asset choices are sensitive to multiple evidence sources. Participants rate explanations as more aligned with their recurring strategies than with their decision-specific rationales. These findings reveal a gap between coarse behavioral agreement and individual-level fidelity, motivating separate evaluation of behavioral accuracy, explanation alignment, and evidence dependence in personalized user simulation.

---


### 460. [A Fisher-Geometric View of Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2610.26525)

**<font color=#1a73e8>作者：</font>** Liu Kaiyuan, Zhuang Ziyuan, Ma Haoxuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Consolidating specialized foundation models into a unified generalist is a central goal of post-training. Two approaches are in common use: model merging, which is fast but treated as a heuristic, and multi-teacher on-policy distillation, which matches distributions but demands heavy rollout compute and suffers from cross-task gradient conflict. We show that the two are one objective seen at different orders. Within a shared basin of homologous specialists, the multi-teacher on-policy distillation objective is, to second order, exactly the Fisher-merging objective. Its minimizer is therefore the Fisher merge, a classic model-merging method given by a closed-form combination of the specialists, so merging is optimal, to second order, as a closed-form stage of distillation. Building on this identification, we propose Residual-Governed Branch-and-Merge(RGBM), a two-phase consolidation procedure. Concretely, a full-parameter Fisher merge is intractable on foundation models, so Phase~1 restricts the merge to the task-vector subspace. Extending tangent-space analyses of merging, we show that the same coefficients that mix task vectors also mix implicit rewards, which lets a residual program on unlabelled prompts solve for them. The program minimizes the worst per-domain residual and reports its energy-normalized values as the domain residual spectrum. Phase~2 lets this spectrum govern what may be added: RGBM passivates domains with low normalized residuals, trains isolated branches only for domains above the spectral gap, and writes back the admitted updates with calibrated shrinkage. On two open-source consolidation suites, the Phase~1 merge alone matches or outperforms fully trained multi-teacher distillation, and RGBM improves on it further with zero extra joint-training steps, whereas every un-gated write-back, including continued joint distillation from the merge, falls below it.

---


### 461. [ReAnchor: Reusing Rejected Verifier States for Diffusion Drafting](https://arxiv.org/abs/2610.26531)

**<font color=#1a73e8>作者：</font>** Sanghyun Lee, Wonjin Nam, Seungho Jang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Block diffusion drafters accelerate speculative decoding by generating multiple draft tokens in a single forward pass. However, each pass produces only a fixed-length block from a single target-generated anchor, limiting how far the draft can extend. Meanwhile, target verification computes hidden states even at positions beyond the first rejection, but these states are typically discarded rather than reused. We propose ReAnchor, a training-free method that reanchors a pretrained drafter at shifted positions using discarded verifier states to generate parallel draft blocks. These blocks improve predictions within the original block and extend coverage beyond its endpoint. At sampling temperature of T=0, ReAnchor achieves its largest average gains on Gemma 4-12B, improving acceptance length by 19.4% and decoding speed by 17.9% across eight benchmarks. Averaged equally over four target models and eight benchmarks, it improves acceptance length by 15.2% and decoding speed by 13.4% with pretrained DFlash drafters.

---


### 462. [Small Average Error, Wide Individual Error: General-Purpose LLMs Estimating Energy Intake from Meal Photos in a Feeding Trial](https://arxiv.org/abs/2610.26538)

**<font color=#1a73e8>作者：</font>** Xiaomeng Li  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Photo-based estimation of food energy could ease dietary assessment, and general-purpose multimodal large language models (LLMs) make such estimates easy to obtain. Most evaluations use one photo taken before eating and compare with energy served, while dietary assessment needs energy eaten. We evaluated six models from two vendors (Claude Haiku, Sonnet and Opus 5.5; GPT-6 luna, 6.1 sol and 6 astra) on 802 meals from ACETADA, a controlled feeding trial with weighed intake, with the before photo only, before and after photos in separate calls (subtraction), or both photos in one request. Three results ran against intuition. Subtraction under-estimated intake for five of six models, because the models still report hundreds of kilocalories for a nearly empty tray. Scaling the before-only estimate by the average share eaten (0.87) matched much of the gain from the after photo; beyond that constant, the second photo lowered meal-level error by only 2.2 to 3.4 points, mainly in meals with food left. With one photo, two models had a near-zero intake bias only because they under-estimated the served energy and ignored uneaten food. In ablations, adding the after photo improved accuracy under both prompt formats for five models, while prompt effects varied across models. Over 148 feeding days, three models kept the 90% confidence interval of their mean error within a pre-set 10% margin, but no model reached the pre-set 30% limits of agreement. Protein was under-estimated by every model, most in protein-dense meals; repeated calls changed error by at most 1.4 points; a high reasoning effort helped only the smallest model (4.2 points) and changed the others by less than 1 point. A low average bias is not evidence of accurate individual intake estimation; such estimates should support, not replace, assessment by a dietitian.

---


### 463. [Breaking Diffusion: Parallel Reasoning with Draft Refinement](https://arxiv.org/abs/2610.26542)

**<font color=#1a73e8>作者：</font>** Jaesang Yu, Seoyeon Byun, Yun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Drafting an answer allows a reasoning model to reconsider each decision in the context of the others. Yet repeated diffusion denoising does not ensure that individually plausible token updates form a better answer together. We introduce Draft Refinement Language Models (DRLMs), which use a single denoiser to propose parallel revisions and evaluate a candidate draft. We train the denoiser to reconstruct every token from uniformly corrupted drafts, teaching both preservation and repair. Its predictions specify revisions directly, without a diffusion reverse transition. Evaluation requires a different use of these predictions: confidence in an existing token reflects both contextual support and evidence from observing the token itself. Using the known corruption process, we correct for this self-token evidence to estimate how well each token is supported by the prompt and the remaining draft. Aggregating these estimates yields a cavity energy computed in one forward pass, without an additional scoring model. Each round proposes a revision, reads the completed candidate in its revised context, and retains it only if its energy is lower. Across Countdown, Sudoku-Extreme, and Maze-Hard, our method outperforms autoregressive and discrete diffusion baselines. With 6M parameters, DRLM reaches 44.4% on Countdown-5 and 93.9% on Sudoku-Extreme. The results establish complete-draft parallel refinement as an effective alternative to reverse diffusion for complex reasoning.

---


### 464. [BetaMem: Learning to Remember a Changing World for Embodied Agents](https://arxiv.org/abs/2610.26554)

**<font color=#1a73e8>作者：</font>** Mai Liu, He Sun, Siru Zhong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon embodied agents face temporal confusion and incomplete or distorted records, recurring errors from fixed memory rules, and growing storage and retrieval costs. We present BetaMem, a framework for building and evolving traceable long-term memory through six linked layers: working, spatial, entity, episodic, experiential, and procedural memory. A dual-level write contract constrains operation executability and source support for content: supervised fine-tuning learns compliant memory operations, while reinforcement learning combines repeated sampling with teacher verification of the original observations to reward complete, accurate records and penalize omissions, distortion, and unsupported content. We formulate failure-driven policy recursive self-improvement through diagnosis along the causal sequence of memory operations and local rule repairs gated by independent replay. Atomic tools frame storage, updates, retrieval, and forgetting as cost-utility allocation under storage and read budgets. Using the open-source Qwen3.5-9B model for memory generation, BetaMem achieves overall scores of 48.08% on M3-Bench-robot, 92.08% on LoCoMo, 72.6% on OpenEQA EM-EQA, and 62.4% on EgoLifeQA, the highest among the listed memory methods under their respective evaluation protocols. Training the model for memory generation raises the contract pass rate from 50.9% to 86.2% while reducing output tokens per stored action by 47.3%. A separate Qwen3-VL-8B-Instruct evaluation on EMem-Bench achieves an average success rate of 38.4% and an average error recurrence rate of 24.9%. We perform best among evaluated methods using comparably sized open-source models. Category results show that we have advantages in integrating information across observations, recalling events over long histories, and inferring personal habits.

---


### 465. [WhatIf-Bench: Benchmarking Intervention-Aware Time Series Forecasting](https://arxiv.org/abs/2610.26582)

**<font color=#1a73e8>作者：</font>** Arjun Ashok, Mihir Parmar, Palash Goyal 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent time series foundation models (TSFMs) can consume covariates in-context, extending zero-shot forecasting to problems driven by external factors. This enables scenario analysis: forecasting how a target responds to events that set covariates to chosen future values. Whether they can do this reliably is an open question. We introduce WhatIf-Bench, a benchmark measuring how well forecasters use covariates to forecast a target's response to future events. WhatIf-Bench is semi-synthetic: time series come from mechanistic simulators of data centers, power grids, road traffic, and water networks, with controlled covariate-target relationships grounded in each system. Each task presents a history of events intervening on covariates, then asks to forecast a future event that either replays seen values (Replay) or sets them to unseen ones (Novel). Varying the number of covariates, historical events, and event length yields 37,665 tasks. Evaluating TSFMs, frontier LLMs, and simple regression baselines, we find the LLMs reach the highest skill (improvement over a naive baseline), ahead of the best TSFMs. Every model forecasts well on Replay futures (48 to 85% skill) but drops to -7 to 50% on Novel futures, with the regression baselines falling the most. Skill on Novel futures also falls as events set more covariates jointly. More historical events raise skill on Novel futures across the board, but large differences remain. WhatIf-Bench reveals generalization to Novel futures as the core challenge, and offers a testbed toward arbitrary scenario analysis.

---


### 466. [BERT Is Already a Denoiser: Cheaply Unlocking Iterative Generation in Masked Language Models](https://arxiv.org/abs/2610.26601)

**<font color=#1a73e8>作者：</font>** Julio C. Amador Diaz Lopez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked language models (MLMs) such as BERT are typically used for representation learning despite their denoising pretraining. We test whether this capability supports conditional generation without diffusion training. Our decoder repeatedly predicts masked tokens and commits high-confidence predictions using a cosine schedule. It requires no diffusion timestep or reverse-diffusion objective. Frozen BERT already exhibits substantial denoising capability, reconstructing 61.0%, 37.5%, and 24.4% of masked tokens at 15%, 45%, and 60% corruption, respectively, although generation deteriorates sharply as visible context disappears. This capability alone does not yield task-directed generation: frozen BERT reaches only 11.0% on ARC-Easy and 4.2% on MMLU. Ordinary MLM adaptation, however, rapidly converts the same architecture into a usable generator. Full adaptation reaches 28.2% and 24.6%, respectively, while parameter-efficient adaptation substantially reduces unmatched outputs. On open-ended conditional generation, full MLM adaptation reaches BLEU/ROUGE-L of 0.163/0.583 on QQP and 0.107/0.327 on Quasar-T, placing it in the same broad performance range as published BERT models trained through diffusion without explicit diffusion training. Finally, applying the same generative interface to stronger masked representations substantially improves performance: RoBERTa-large reaches 44.2% on ARC-Easy and 33.8% on MMLU. These results separate three components of masked iterative generation: pretraining supplies the representation and denoising operator, task adaptation determines what the model generates, and an iterative commitment rule supplies the decoding process. Explicit diffusion training is therefore not necessary to obtain effective iterative conditional generation from pretrained MLMs in the settings studied here.

---


### 467. [When the harness decides success: state that cannot be re-observed](https://arxiv.org/abs/2610.26632)

**<font color=#1a73e8>作者：</font>** Raimondas Lencevicius  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses decide what a language model sees across turns: they drop old turns, summarize them, or replay the model's own earlier reasoning. We ask when these choices change whether an agent succeeds, not only what it costs, and report three findings. First, in a pre-registered synthetic probe, truncating the context window costs a low-cost reasoning model nothing in success when a needed fact can be looked up again (it looks the fact up instead), but drops its success to chance when the fact cannot be re-observed: the two penalties differ by 92.5 percentage points (90% CI [89.5, 95.5]). A pre-registered replication on one model from a second provider showed the same contrast. Once the fact was lost, that model chose no answer rather than guessing. Second, on ARC-AGI-3, where the benchmark's Standard harness trails its Provider Adapter harness by a wide margin, we decompose that gap one component at a time, for one model on four games. Summarizing old turns instead of dropping them, while keeping the Standard harness's invitation to take notes, recovers 86% of a 63-point gap without replaying the model's reasoning. The same harness without the invitation recovers 43%, and adding the provider's native replay of the model's reasoning recovers the remaining 57%. These are point estimates from one counted run per configuration and game, and the replay share depends on a single run. Third, in the benchmark's published runs and in ours, the Adapter's advantage in the probability of clearing a level it has reached is larger at deep levels than at early ones. This largely restates where runs stopped and does not separate a growing advantage from a constant one.

---


### 468. [Revision-Based Learning from Interactive Experience and Feedback](https://arxiv.org/abs/2610.26636)

**<font color=#1a73e8>作者：</font>** Jiawen Li, Chenming Ge, Alice Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Code generation models are increasingly used to produce interactive artifacts, such as websites and user interfaces. Many properties that determine whether these interfaces are useful only become apparent through realistic interaction, making them difficult to incorporate into model training. In this paper, we introduce RELIEF (REvision-based Learning from Interactive Experience and Feedback), a method for improving code generation models using feedback on their generated interfaces. RELIEF uses a coding agent to revise these interfaces, then incorporates the improvements into their original generation traces to produce supervision for fine-tuning. To evaluate RELIEF, we collected a dataset of 200 synthetically generated websites paired with 355 interaction recordings and accompanying feedback from 24 users. We used critiques derived from code inspection, automated interaction, explicit human feedback, and human interaction recordings to fine-tune variants of two code generation models. Our results show that feedback effectiveness varies with base model capabilities, with critiques inferred from human interaction recordings leading to the largest usability improvements overall under our tested models.

---


### 469. [From Outcomes to Components: A Counterfactual Evaluation Framework for LLM-Proposed Repairs](https://arxiv.org/abs/2610.26650)

**<font color=#1a73e8>作者：</font>** Hengyu Ye, Songhua Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An LLM-generated repair action specifies which records to change and by how much. A failed action may still contain a useful target set or numerical update, depending on how the two are paired. We evaluate this problem in traffic networks and databases, where aggregate observations obscure the records that need correction. We examine the pairings by executing each combination from the same initial state, using a reference action that restores the affected records. In 76 of 114 traffic actions, the gain from correcting both parts exceeds the sum of the gains from correcting each part alone. Six of these actions become worse after either correction alone, but improve when both parts are corrected. In database repair, replacing only the proposed update with the reference update worsens 17 of 108 model actions, all of which select unaffected records. We also test whether parts of two proposals can be reused. On held-out observations, selecting among the proposals and their recombined target-update pairs recovers 61.6% of the reference action's loss reduction, compared with 58.0% from selecting between the proposals alone.

---


### 470. [The Effectiveness and Durability of Pretraining Data Filtering in Protein Language Models](https://arxiv.org/abs/2610.26651)

**<font color=#1a73e8>作者：</font>** Aaron Maiwald, Roderick McNeill, Jaeyoung Lee 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretraining filtering is one of the most common safeguards for open-weight language models. Here we study its effectiveness, durability and scalability using the ESM-2 family of protein language models. We find that filtering viral proteins from the pretraining data meaningfully degrades masked language modelling, mutation effect prediction and long-range contact prediction on viral proteins, while largely preserving performance on non-viral proteins. These effects are concentrated among proteins from human-infecting viruses, and grow as we scale models from 8M to 3B parameters. As models increase in size, we find that stringent filtering becomes more effective. However, fine-tuning on sequences from the removed viral families restores the lost performance. Although the cost to recover performance increases with model scale, even for the largest models it costs about 80 USD of H100 time. This work establishes pretraining filtering as moderately effective at selectively degrading performance on viral proteins, but not durable against fine-tuning with modest computational resources and access to relevant data.

---


### 471. [The Development of Sycophancy in Language Models: Tracing Vulnerabilities from Pretraining to Post-Training](https://arxiv.org/abs/2610.26655)

**<font color=#1a73e8>作者：</font>** Haonan Huang, Chengkun Cai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models can change a committed answer to accommodate a user's opinion or pushback without new evidence. However, when this behaviour develops during training and what a released model inherits from earlier stages remain unclear. We follow 741 checkpoints of 30 open model lineages, from early pretraining to released models. We plant initial verdicts on moral scenarios and measure how far a model follows a user's stated opinion or abandons its verdict under pressure. In most lineages the behaviour is present before post-training, and its average strength changes in either direction, at different stages across lineages. A clearer pattern emerges at the level of individual questions. Beyond responses without pressure, pretraining behaviour predicts little of which questions a released model yields on. That pattern forms during post-training: on routes with supervised fine-tuning, the fine-tuning checkpoint predicts part of it and the preference-optimization checkpoint most of it. A sibling trained from the same base along another route predicts far less: for Tülu-3 8B, its own preference-stage checkpoint removes 85% of the remaining prediction error, a sibling 19%. Internal states add predictive information without changing this ranking. Similar average scores conceal different vulnerabilities, and training history matters for auditing a released model.

---


### 472. [SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?](https://arxiv.org/abs/2610.26659)

**<font color=#1a73e8>作者：</font>** Zhaoxi Zhang, Hao Liang, Linxuan Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence requires agents to actively acquire visual evidence and integrate observations into a coherent representation of the three-dimensional world. Yet spatial question answering offers limited evidence of whether models can construct accurate metric maps through autonomous exploration. We introduce SpatialScout, a benchmark for evaluating vision-language model (VLM) agents on active object-level 3D mapping. SpatialScout comprises 80 diverse indoor scenes containing 3,140 target objects. Given an object inventory, RGB observations, camera calibration, and camera poses, agents control a camera to explore each scene and estimate object centers in a shared coordinate frame. The task requires coordinating viewpoint selection, cross-view association, geometric estimation, and map revision under bounded interaction budgets. Evaluation jointly measures localization accuracy and target coverage through object-scale overlap scores that penalize missing predictions. Experiments with frontier VLMs reveal substantial limitations: the strongest evaluated model, Claude Opus 5.5, achieves a mean overlap score of 41.71%, with 47.23% of targets exceeding an intersection-over-union (IoU) threshold of 0.5 and only 3.25% exceeding 0.9. These results reveal a substantial gap between recovering coarse object layouts and constructing complete, precise metric maps. SpatialScout provides a quantitative testbed for developing agents that build reliable 3D spatial representations through active perception. Code is available at this https URL.

---


### 473. [CaptionFuse: Training-Free Composed Product Retrieval Via VLM Intent Captioning and Weighted Embedding Fusion](https://arxiv.org/abs/2610.26661)

**<font color=#1a73e8>作者：</font>** Zhao Gao, Mina Metias, Mohamed Noordeen Alaudeen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) retrieves products matching a reference image modified by natural language---a core capability for eCommerce search. Existing training-free methods fuse CLIP embeddings via arithmetic, but we identify a fundamental limitation: user text modifications are attribute-sparse---a user who types ``make it red with shorter sleeves'' specifies what to change but not what to keep (the floral pattern, the V-neck, the fit-and-flare silhouette). We introduce language-space fusion: a Vision-Language Model (VLM) jointly interprets the reference image and modification to generate a visually grounded product-title caption---e.g., ``Red floral fit-and-flare dress with short sleeves and V-neck''---that fills in the missing attributes from the image. Our method, CaptionFuse, requires no task-specific training and is model-agnostic. A controlled experiment confirms that attribute content--- not linguistic style---drives the gains: imperative and descriptive captions with identical attributes achieve equal R@10, while both outperform raw modifications by +6.5 points.

---


### 474. [AllPath: Layered Verification for a Deployed, Self-Revising LLM Trading Agent under Human-Gated and Autonomous Regimes](https://arxiv.org/abs/2610.26662)

**<font color=#1a73e8>作者：</font>** Tian Zhang, Meng Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM trading agents are evaluated almost exclusively in backtests and autonomous benchmark harnesses. Deployment, where actions are irreversible, raises a different question: who verifies the agent's actions, and which failures can each verifier structurally catch? We report on AllPath, a personal LLM trading agent deployed against a live paper-brokerage account. The system watches positions through a deterministic rules engine, and each night it reviews its own day and proposes revisions to its own trading strategies. Verification is split across three layers. Code verifies what must not depend on judgment: deterministic gates enforce risk limits and block any strategy revision that fails an integrity check. The agent verifies itself within fixed bounds: its nightly review has an iteration cap and no tools that can act. A human verifies judgment, through approval screens that show the current state of each proposal. We also compared two verification policies for the agent's self-revisions on the live system: two and a half weeks with every self-revision human-gated, then five weeks with reflection revisions auto-applied behind the same code gates, while the operator's chat channel stayed human-gated throughout. Each layer caught a different kind of failure. The code gates rejected no proposal; their role was keeping revisions consistent. The human rejected two proposals that passed every code check, both over a disagreement about the market, and later removed 11 of the 19 rules the agent had added on its own, at a median lag of eight days. The most instructive production incidents, such as strategies silently left unmonitored, passed every gate; the operator found them by hand, and the fix each time was an interface change that makes the condition visible. We contribute the layered architecture, the two-regime account, and a production incident taxonomy, none observable in a backtest.

---


### 475. [Which Model for Which Role? Cost-Efficient Pareto Recommendation for LLM Agentic Workflows](https://arxiv.org/abs/2610.26676)

**<font color=#1a73e8>作者：</font>** Qian Xie, Wenyue Hua, Yueli He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agentic workflows increasingly employ different models for specialized roles. Users may prefer different trade-offs between task quality and deployment cost, sometimes also considering latency. Finding good assignments incurs a separate search cost from evaluating multiple candidates. We introduce Cost-Coupled Gittins (CC-Gittins), a multi-objective extension of single-objective cost-aware Gittins search for Pareto recommendation. It exploits the coupling between evaluation and deployment costs: assignments that cost more to deploy also cost more to evaluate. The search alternates between seeking higher quality and lower deployment cost, reusing each evaluation to inform both searches. After each batch, CC-Gittins recommends assignments that are nondominated under uncertainty-adjusted estimates of quality and deployment cost. We evaluate CC-Gittins on eight quality--cost matrices from workflows with two to five roles and up to 1,681 candidate assignments. We also evaluate the method with latency as a third objective. Across the eight benchmarks, CC-Gittins recovers a substantial fraction of the true Pareto frontier at roughly 10% of the exhaustive-evaluation cost, and recovers most of the frontier with few false positives by 30%.

---


### 476. [Parallel Language Models via Variational Decoding](https://arxiv.org/abs/2610.26693)

**<font color=#1a73e8>作者：</font>** Felix Draxler, Robin C. Geyer, Daniel Geyfman 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive language models emit one token per forward pass. This causes high inference latency, in particular as models are scaled up for quality. In this paper, we introduce Parallel Language Models (PLMs), which generate mutually consistent tokens in one forward pass by routing dependencies through latent auxiliary variables. PLMs are trained using a variational bound that reduces to an autoregressive loss plus a parallel decoding loss. Empirically, PLMs are on a faster and better Pareto frontier than autoregressive and discrete diffusion baselines. Pretrained PLMs achieve near-autoregressive pretraining loss on model scales of 80M to 3B parameters, and speedup follows a power law in model size. When post-trained, our 1.3B model matches or exceeds an identically trained autoregressive model on math, coding, and instruction-following benchmarks, speeding up inference $2.3\text{-}5.7\times$. Together, we show that parallel generation can be trained from a single training objective at autoregressive quality. We will make our code available at this https URL.

---


### 477. [PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements](https://arxiv.org/abs/2610.26711)

**<font color=#1a73e8>作者：</font>** Kaiwei Chen, Moran Li, Zhenye Gan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video generation models produce visually compelling outputs, yet their physical plausibility remains poorly measured. Physical plausibility asks whether generated objects obey geometry, kinematics, dynamics, and conservation laws. Existing benchmarks rely on coarse visual-language model judgments or target embodied world models rather than video generation itself. We introduce PVBench, a physical video benchmark that quantitatively measures the plausibility of generated videos across 46 dimensions organized into seven domains, spanning: i) instruction and semantic fidelity, ii) behavioral and causal consistency, iii) perceptual and temporal quality, iv) geometric and spatial consistency, v) material properties and field states, vi) kinematic and spatiotemporal persistence, vii) and mechanical plausibility with conservation laws. PVBench comprises 600 carefully crafted prompts, of which 30% involve physical embodied agents such as robot arms, humanoids, quadrupeds, and multi-agent systems. For challenging physically tractable dimensions, it pairs each with specialized vision models that derive verifiable, physically grounded measurements, such as object-level 6D pose, metric scale, surface normals, kinematics, and numerical conservation-law residuals. It thus avoids relying solely on subjective scoring, while supporting both text-to-video and image-to-video generation. Finally, we validate the agreement between automatic metrics and human judgments through human evaluation. Meanwhile, we evaluate mainstream open-source and closed-source models and present several insights. By releasing the benchmark, prompts, and calibration protocol, we aim to foster physically grounded video generation.

---


### 478. [Proof-of-Machine-Learning-Inference: Mining Knowledge, Not Hashes](https://arxiv.org/abs/2610.26713)

**<font color=#1a73e8>作者：</font>** Wan Ki Wong, Michele Ciampi, Rik Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bitcoin-style Proof-of-Work (PoW) secures permissionless blockchains but spends substantial computation on hash puzzles which have no utility other than extending the chain. At the same time, we have seen that the rise of generative AI has created significant demand for computational resources that are unfortunately available only to a few players. We propose a solution that solves both problems at the same time. In particular, we present Proof-of-ML-Inference (PoML), a consensus protocol in which miners perform user-requested machine-learning inference as part of their consensus algorithm. We identify exactly what computational assumptions are needed for ML inference to safely replace hash work, formalize those assumptions, and give evidence that LLMs and diffusion models satisfy them. We then formally analyse the security of our protocol by reducing the security of our protocol to the security of the Bitcoin Backbone model. Finally, we empirically evaluate block-time stability, showing that, in a simulated environment, PoML maintains a block production rate close to its calibrated block-time target.

---


### 479. [HoloCosm: Beyond Single-Metric Benchmark Compression Across Multiple Metrics](https://arxiv.org/abs/2610.26714)

**<font color=#1a73e8>作者：</font>** Yupei Lin, Zhongzhan Huang, Junxin Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Benchmark compression reduces evaluation cost by selecting a small set of samples. Existing methods typically guide selection using a single metric, although benchmarks often assess models along multiple dimensions. We find that model rankings are often weakly correlated across metrics, indicating that different metrics capture distinct aspects of model performance. Samples selected for one metric do not reliably preserve scores and rankings on others when used for compressed evaluation. At 80\% compression, each of the five single-metric baselines yields higher reconstruction error than equal-size random sampling in over 70\% of cross-metric comparisons. To address this challenge, we present HoloCosm, which jointly minimizes normalized score-reconstruction error across source models and metrics while constraining ranking distortion. We evaluate HoloCosm across multiple compression rates on 15 language, multimodal, VLA, and agent benchmark configurations with 85 component metrics. With 80\% compression, HoloCosm outperforms Random, the strongest baseline overall: average NMAE drops by 35.3\% to 0.236, worst-component NMAE drops by 39.5\% to 0.330, and average Spearman correlation rises from 0.884 to 0.915. In addition, HoloCosm remains competitive with existing baselines in single-metric evaluation. We will release our code and experimental results.

---


### 480. [Copying Under Repetition: From Prefix Matching to Position Hashing](https://arxiv.org/abs/2610.26722)

**<font color=#1a73e8>作者：</font>** Anxin Guo, Tianlong Huang, Chenxiao Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frontier LLMs can copy random text almost flawlessly, yet they often overrun or truncate long blocks of repeated characters. In repeated strings, matching local content no longer reliably identifies where copying should continue or when it should stop. Nevertheless, we show that a two-layer transformer with $O(\log\log N)$-bit precision and $O(\log N/\log\log N)$ width can copy every string up to a chosen design horizon $N$ and terminate correctly under arbitrary repetition. We use RoPE-style rotations of attention values and outputs (VO-rotations) with small prime periods to encode distances from delimiter anchors modulo those primes. By the Chinese Remainder Theorem, these periodic encodings jointly distinguish all required distances, allowing one retrieval rule to select either the next source token or the end marker. In contrast, we prove a width-independent impossibility result for copying under sequential finite-precision softmax accumulation. It applies to transformers whose only positional input is an additive attention bias that eventually becomes constant, including NoPE and a recursive implementation of ALiBi. Once an identical-token run exceeds the resulting saturation threshold, further repetitions leave the logits unchanged. If this threshold grows sublinearly with $N$, these models cannot both complete a long all-identical copy and stop correctly, a pattern resembling the termination errors of frontier LLMs. In synthetic copying experiments, baseline transformer models fail on long repeated strings even within the training range. Trained VO models, by contrast, generalize beyond the training lengths with near-perfect accuracy up to length $\approx 5005$, the selected primes' period product.

---


### 481. [EpiLens: Lightweight RAG for Epidemiological Knowledge Acquisition](https://arxiv.org/abs/2610.26730)

**<font color=#1a73e8>作者：</font>** Vincenzo Perri, Ciro Cattuto, Daniela Paolotti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To prepare for future outbreaks, researchers need to know what studies have been done and what data they use. Mapping a large literature by hand is slow, while large language models alone can misstate or conflate sources. We present EpiLens, a lightweight, open-source retrieval-augmented generation package that applies a fixed retrieval template and output schema to every paper in a corpus and links outputs to source passages. We build a corpus of 2,297 papers from the sources of a multi-pathogen parameter study and evaluate EpiLens's paper-classification workflow against 214 manually labelled papers. Without task-specific training data, the classifier matches or exceeds the tested supervised and zero-shot baselines across four tasks. The study's early extraction sheets cite published sources for 327 estimates. We link each estimate to a cited document or to corpus studies included by a review. Then, we use the classifier's labels to compare the papers associated with different parameters and pathogens. EpiLens labels more papers linked to reproduction numbers than fatality risks as model-based (54% versus 22%, compared with 62% versus 24% in the manual labels). The gap is consistent with the frequent use of transmission models to estimate reproduction numbers and persists within each of five pathogens compared. Beyond the contrast between parameters, the model-based share of papers linked to incubation-period estimates differs by pathogen: 55% for SARS-CoV-2 versus 6% for mpox.

---


### 482. [CAVA: Complementary-Label-Aware Data Valuation](https://arxiv.org/abs/2610.26734)

**<font color=#1a73e8>作者：</font>** Tan-Ha Mai, Hsuan-Tien Lin, Vu Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complementary-label learning (CLL) trains a classifier from labels that name a class an instance does not belong to. Such labels are cheap to collect from crowdworkers or vision-language models (VLMs), making them attractive for large-scale annotation. However, both sources can mistakenly assign the true class as the complementary label. Such annotation errors are particularly harmful in CLL because the model is explicitly trained to suppress the correct answer. Optimal transport (OT) data valuation identifies harmful samples by comparing training data with a clean validation set, but transferring it directly to CLL creates a semantic mismatch: label $c$ means not class $c$ in the training but class $c$ in the validation. We show that this makes the OT label groups noisy mixtures whose behavior depends on the noise rate. The transferred score is informative only at sufficiently high noise, becomes uninformative at the crossover rate $1/M$ for $M$ classes, and reverses below it, where practical CLL annotation typically operates. We propose CAVA, which introduces a complementary label cost and a label margin that isolates the contribution of each complementary label to the transport potential. The margin keeps a consistent direction across noise rates, detects diagonal noise with a parameter-free threshold of closed-form precision, and allows detected samples to be recycled as ordinary-label supervision. On synthetic and human-annotated benchmarks, CAVA separates diagonal noise almost perfectly where directly transferred OT valuation performs worse than random. With only a fraction of the clean validation data, it also improves every CLL objective we evaluate, showing that OT-based valuation becomes reliable once the semantics of complementary supervision are modeled explicitly.

---


### 483. [recAMPLIFY: Large-Scale Pretraining of Recursive Protein Language Models](https://arxiv.org/abs/2610.26747)

**<font color=#1a73e8>作者：</font>** Saurav Jha, Qianli Liao, Robert Vernon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein language models (pLMs) are powerful tools for protein annotation and mutation-effect prediction, but progress has largely depended on scaling model size and data, making them expensive and prone to memorization. Test-time scaling offers a complementary path, but methods developed for autoregressive LLMs do not transfer directly: masked encoders lack a generation loop, and amino acids do not verbalize in a reasoning language. Instead, we adapt recursive pretraining to masked pLMs, where a weight-tied Transformer core refines residue-aligned hidden states over an adjustable number of cycles. We instantiate this recipe as recAMPLIFY, a pLM with 155M unique parameters trained on the same 2T tokens as AMPLIFY-350M. Despite 56% fewer parameters, it improves CASP contact recovery and three out of four supervised tasks, notably raising fold accuracy by 22.5%. Because optimal depth for recAMPLIFY varies across tasks and assays, we then introduce Gated Mixture Recurrence (GMR), a framework that decodes each protein from a probability-weighted mixture of hidden states visited during recursion. GMR employs a learned residual gate at scalar, low-rank, or per-dimension resolution to control how much of each cycle's proposed update is accepted into the state. This unifies halting and gating into a single adaptive computation objective while recovering PonderNet-style halting as a special case without gates. Layered on top of recAMPLIFY, GMR further reduces expected layer depth by up to 37%, although the accuracy trade-off varies by task. Mechanistic analyses show that residual gating controls recurrence stability beyond the trained depth and that halt depth tracks biological properties.

---


### 484. [Beyond Omni: A Unified MLLM for Embodied Sensory Understanding](https://arxiv.org/abs/2610.26751)

**<font color=#1a73e8>作者：</font>** Shiyun Xiong, Dongming Wu, Peiwen Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent embodied systems increasingly build on multimodal large language models (MLLMs) for their pretrained understanding and reasoning capabilities, but their perception of the physical world remains largely limited to basic modalities such as vision and audio. However, broadening MLLMs to more diverse sensory modalities from the physical environment is challenging: their representations are often weakly connected to the MLLM and vary substantially in structure and statistics, while their interpretation still requires shared high-level understanding and reasoning. We therefore propose Unisense, a unified embodied MLLM framework that supports diverse physical sensory modalities within a shared multimodal architecture. Unisense follows a two-stage training process: (i) aligning sensory representations with language to establish a language-accessible interface; and (ii) tuning modality-specific experts within the shared LLM to provide specialized processing for different sensory modalities. To support broad sensory learning, we curate Unisense-1M, a large-scale embodied sensory training corpus comprising 1M samples across 8 sensory modalities. We further evaluate Unisense on 12 benchmarks spanning depth, point cloud, IMU, tactile, thermal, radar, motion, and smell understanding. Across these heterogeneous sensing tasks, Unisense achieves strong performance and outperforms both generalist and specialized models on most benchmarks, demonstrating the potential of pretrained MLLMs as unified models for embodied sensory understanding.

---


### 485. [TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning](https://arxiv.org/abs/2610.26754)

**<font color=#1a73e8>作者：</font>** Liana Patel, Rishabh Ranjan, Ion Stoica 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Expert human readers process large inputs (e.g., code repositories and long documents) by skimming to closely read only what matters. On the other hand, language models process all input tokens through each model layer, resulting in significant processing costs for long-context inputs. We introduce TokenGate, a small, drop-in component that extends existing trained models to enable end-to-end learnable token pruning over long-context inputs for fast and memory-efficient prefill. To enable end-to-end learning despite the non-differentiable top-K operator for token pruning, we introduce token-gated attention, a mechanism inspired by Mixture-of-Experts that re-weights attention logits using token importance scores. Across diverse tasks, TokenGate achieves $1.4$-$11.3\times$ faster time-to-first token (TTFT) and $1.5$-$3.4\times$ lower peak memory at no accuracy degradation for prefill in transformers. Compared to the best-performing prior methods for token-pruning, TokenGate gives up to $6.4\times$ faster prefill and $2\times$ lower peak memory. TokenGate natively extends both standard transformers (e.g., Qwen3) and hybrid-attention models (e.g., Qwen3.5) with simple lightweight adaptation comparable to standard parameter-efficient fine-tuning. We make our code available at: this https URL.

---


### 486. [HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs](https://arxiv.org/abs/2610.26770)

**<font color=#1a73e8>作者：</font>** Zhuoshi Pan, ZhiYuan Feng, Yukuo Cen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Harness development plays a crucial role in building capable AI agents. Recent approaches improve harnesses through recursive self-improvement (RSI), but their performance gains often come with higher execution costs. We introduce HarnessPro, a label-free method for evolving harnesses to improve task performance while reducing execution cost. In this setting, candidate harnesses are evaluated using LLM-generated tests without access to ground-truth solutions or official tests. Specialized agents diagnose execution trajectories, plan updates with different performance-cost priorities, and implement them as candidate harnesses. Rather than returning a single harness, HarnessPro uses normalized weighted squared-distance selection to provide cost-focused (lite), balanced (medium), and performance-focused (heavy) harnesses for different deployment budgets. Selected harnesses enter the next iteration, where execution feedback guides further updates. Our experiments cover Terminal-Bench 2, SWE-Bench Pro, and ProgramBench, using GPT-5.5 with Codex and GLM-5.2 with Claude Code. Across these benchmarks using GPT-5.5 with Codex, the heavy mode of HarnessPro achieves an average pass-rate gain of 2.0 percentage points and an average per-task cost reduction of 26.1% relative to RHO. This advantage also holds when using GLM-5.2 with Claude Code. Code is available at this https URL

---


### 487. [Game of Phones: Harnessing Game Theory and LLMs in 'Bot Wars' to Counteract Phone Scams](https://arxiv.org/abs/2610.26781)

**<font color=#1a73e8>作者：</font>** Nardine Basta, Robin Carpentier, Benjamin Zi Hao Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phone scams impose substantial and growing costs on individuals and financial systems worldwide, yet existing countermeasures impose no resource cost on perpetrators. Strategic scam-baiting, in which automated agents engage scammers to deplete their operational capacity, offers a proactive alternative but requires dynamic strategy adaptation that static systems cannot provide. We introduce a game-theoretic framework enabling LLMs to learn effective counter-strategies through in-context experience without fine-tuning. The framework models scammer-baiter interactions as a two-player game with empirically grounded strategies and utility functions, using Nash equilibrium as a formal benchmark for evaluating learned behaviour. Across 300 simulated dialogues and three LLM architectures, adaptive strategy selection achieves 28.9-79.7% closer alignment to Nash equilibrium than non-adaptive baselines. The code and an annotated dataset of 300 dialogues with turn-level strategy labels and utility scores are released at this https URL .

---


### 488. [LG-Bench: A Graph-Structured Evaluation Benchmark for Life Sciences](https://arxiv.org/abs/2610.26787)

**<font color=#1a73e8>作者：</font>** Lu Sun, Xiangyi Zhang, Xiangyang Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional evaluation benchmarks reduce inherently interconnected scientific knowledge in life sciences into flat lists of questions, disregarding the underlying topological structure of the knowledge. We introduce, the first graph-structured benchmark for life sciences, featuring over 10,000 high-quality multiple-choice questions across medicine, biology, and chemistry. Our approach constructs a weighted evaluation graph using bidirectional matching and semantic similarity algorithms, where nodes represent questions and edge weights capture their semantic relationships. Leveraging this graph topology, we design two novel evaluation metrics. The Global Coherence Score (GCS) measures a model's consistency within semantically related neighborhoods, while Knowledge Balance Score (KBS) analyzes how model errors are distributed across the graph to reveal conceptual blind spots. LG-Bench facilitates fine-grained comparison of LLMs by surfacing differences in conceptual coherence and patterns of knowledge organization across models. Our framework shifts the evaluation paradigm from flat accuracy metrics to structure-aware analysis, offering a new lens for diagnosing and improving LLM performance in the life sciences domain.

---


### 489. [Training with ML-labeled Data via Stochastic First- and Zeroth-Order Optimization](https://arxiv.org/abs/2610.26790)

**<font color=#1a73e8>作者：</font>** Maria-Eleni Sfyraki, Jun-Kun Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training a machine learning (ML) model is an optimization process that typically requires a set of examples with ground-truth labels beforehand. Obtaining these ground truths usually requires laborious human effort and can be costly. The scalability of human labeling becomes a concern when there are a large number of data points that need to be labeled. To address this practical issue, we consider an optimization setting where a subset of samples has ground-truth labels, while the remaining data points were labeled by an ML predictor, which could potentially assign incorrect labels to those points. We propose both first-order and zeroth-order stochastic optimization methods for training on datasets consisting of a mix of true-labeled and ML-labeled samples. We further conduct comprehensive empirical studies from training a linear regression model to fine-tuning a large language model (LLM) to showcase the effectiveness of the proposed algorithms for training with ML-labeled data.

---


### 490. [Accountable partial understanding: securing the epistemic attack surface of agentic systems](https://arxiv.org/abs/2610.26799)

**<font color=#1a73e8>作者：</font>** Josiah Dykstra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Attackers profit from what defenders do not understand. Software security has treated the gap between system behavior and human comprehension as a condition to narrow through analysis and assurance, booking the remainder as accepted risk. Agentic AI systems change that gap: when software reads, writes, explains, and authorizes security-relevant behavior, partial understanding moves faster, grows more opaque, and couples to delegated authority. This paper characterizes the resulting epistemic attack surface and presents a taxonomy of four interacting attack categories, which target the interpretation of intent, the production and consumption of evidence, the scope of delegated authority, and the comprehension of human supervisors. It then defines accountable partial understanding (APU) and specifies six necessary conditions: bounded scope with explicit assumptions, inspectable evidence, assigned responsibility, visible residual unknowns, actionability, and temporal maintenance. It explains why delegating interpretation to software agents differs from distributing knowledge among people and distinguishes APU from risk acceptance, explainable AI, assurance cases, formal verification, and human-in-the-loop oversight. From the conditions, the paper derives five design principles: bounded delegation, decoupled evidence, assumption tracking with invalidation, role-specific accountability views, and intervention-preserving design with residual unknown registers. It introduces two measurable probe dimensions, evidence linkage and invalidation latency, for testing whether accountability mechanisms hold under change and adversarial pressure. Three running examples (an AI coding agent, an autonomous cyber-defense agent, and an AI-mediated insulin delivery update) ground the analysis. Security without full understanding is already here; the task is to make it accountable.

---


### 491. [Scaling Parameter-Efficient Fine-Tuning for Brain Encoding](https://arxiv.org/abs/2610.26802)

**<font color=#1a73e8>作者：</font>** Zhuofan Josh Ying, Guanglong Sun, Nolan Ho 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brain encoding models aim to predict neural responses to stimuli. The most widely used approach fits readouts from frozen pretrained backbones. Using neural data to train large models from scratch or fully fine-tune them after task-pretraining has proven difficult because neural data is costly and limited. We show that parameter-efficient fine-tuning (PEFT) enables us to effectively adapt very large pretrained backbones for brain encoding with a small number of trainable parameters. To make it computationally practical, we exploit the backbone's causal structure to predict multiple timepoints in a single pass instead of using sliding windows, significantly reducing feature-extraction cost. This enables efficient fine-tuning of multimodal backbones with up to 104B parameters, the largest model adapted for brain encoding to our knowledge. Trained with a low-rank adapter (LoRA) and a lightweight readout, our approach consistently improves brain encoding performance across nine diverse multimodal backbones. On the same Qwen3-Omni backbone as the prior state-of-the-art (SoTA), our method BrainLoRA achieves the best published performance on the Algonauts 2025 Challenge. We also show the adapted multimodal backbones remain interpretable: modality attribution recovers the canonical sensory topography that prior work often obtains by construction from separate unimodal encoders, and neural adaptation increases the contribution of audio inputs and cross-modal mixing within the backbone. To scale out the number of adapted models, we develop a multi-LoRA kernel that accelerates joint training of multiple LoRAs on a shared backbone. This enables an ensemble of 200+ adapted models that ranks first on the public Algonauts post-challenge leaderboard at the time of writing. Together, our results highlight PEFT as an efficient and powerful paradigm for brain encoding.

---


### 492. [What Language Adds, and at What Cost: Four Controlled Probes of Pathology Vision-Language Models](https://arxiv.org/abs/2610.26805)

**<font color=#1a73e8>作者：</font>** Wenhao Zhang, Zhongliang Zhou, Yi Ping 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision--language models (VLMs) promise to make computational pathology queryable and able to draft reports, but how much language adds beyond the vision backbone is unclear, because almost every system is evaluated by its developers on test sets of their own choosing. We grade published evidence by how it was produced and test four claims with controlled probes that reuse released checkpoints and public data, varying one input at a time. Report text adds prognostic signal: adding a frozen embedding of the stage-redacted report to a slide embedding raises the pooled C-index by 0.019 for progression-free interval and by 0.016 for overall survival across 1{,}633 TCGA patients, and restoring the stage statement adds nothing. Prompts add no measurable accuracy at inference: with features and pooling fixed, zero-shot classification is statistically indistinguishable from a supervised linear probe for lung and renal cancer subtyping. Slide-level question answering is barely grounded: SlideChat answers 74.82\% of SlideBench-VQA(TCGA) items correctly with the slide and 74.41\% without it, whereas its language backbone alone reaches 43.52\%. Paraphrasing leaves accuracy unchanged but flips 8--23\% of answers. Self-reported gains from agentic navigation and few-shot language priors cannot yet be attributed to language. Language thus adds real but narrow value, and we propose minimum controls that would expose these failure modes in future evaluations.

---


### 493. [ASTOR: Benchmarking and Improving Autoformulation for Soft-Constraint Optimization with a Formal Grammar](https://arxiv.org/abs/2610.26819)

**<font color=#1a73e8>作者：</font>** Amer Goel, Yeganeh Alimohammadi, Andrew Daw  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world decision problems combine two qualitatively different kinds of constraints: requirements that must be satisfied, called hard constraints, and preferences that can be violated, called soft constraints. Because these problems are often posed to decision-makers in natural language, large language models offer a natural tool for assisting with their solution. This has given rise to autoformulation, which focuses on using LLMs to translate natural-language descriptions of decision problems into executable mathematical optimization models. However, this research often neglects soft constraints like those proposed by consumers, managers, and planners, despite the fact that many practical problems require modeling them explicitly. We introduce ASTOR, an inference-time framework that maps a natural-language decision problem to a grammar-guided abstract syntax tree (AST) before deterministically compiling the resulting representation into executable optimization code. We also introduce SoftOR, a unified benchmark of natural language problems which focuses on soft constraint formulations. On SoftOR, ASTOR achieves the best aggregate accuracy among comparable single-request and multi-agent LLM methods while remaining competitive on standard autoformulation benchmarks that include only hard constraints. Code and data are available at this https URL.

---


### 494. [MemT-1.0: Towards Memory-Native Evolution](https://arxiv.org/abs/2610.26825)

**<font color=#1a73e8>作者：</font>** Zhiyu Li, Zeyu Zhang, Linyun Liu 等 74 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory-native evolution requires making memory an intrinsic capability of foundation models, enabling them to continuously accumulate and utilize information. To this end, we introduce MemT-1.0, a new architecture of memory foundation models that internalize memory as part of model computation. Building on Metis, MemT-1.0 employs Gated DeltaNet-2 with a stable token-level memory update mechanism within each turn. We further introduce Mixture-of-Storage to scale native memory capacity. Following a deliberate backbone preparation, we develop a two-stage training pipeline consisting of continued pre-training and post-training, supported by 34B tokens of training data and efficient training and inference infrastructure. We release a model family comprising MemT-1.0-Nano and MemT-1.0-Flash, and conduct a comprehensive evaluation of memory and general capabilities. The results show that they outperform the parametric memory baselines on average and remain competitive with retrieval-augmented methods, while largely preserving general capabilities. At a history length of 128K tokens, MemT-1.0-Nano achieves approximately $1.86\times$ end-to-end inference speedup and a $66\times$ reduction in persistent storage relative to full context KV cache. By internalizing retrieved procedural experience, MemT-1.0 improves task success on agentic tasks, providing a practical step toward memory-native evolution.

---


### 495. [RefCraft: Benchmarking Visual-Reference-Conditioned Agentic Generation through Web Development](https://arxiv.org/abs/2610.26826)

**<font color=#1a73e8>作者：</font>** Yuchi Wang, Rongyao Fang, Weihao Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Beyond basic tool use and coding skills, effectively incorporating visual references into agentic generation is equally essential for applying AI agents to real-world productivity tasks. We study this crucial capability through webpage development, a practical and readily evaluable setting in which existing benchmarks remain largely idealized: they typically focus on reconstructing visual targets or generating webpages from textual instructions alone, overlooking the more common workflow of developing from visual examples. Specifically, we introduce RefCraft, a benchmark comprising 300 realistic multimodal webpage-development tasks that combine natural-language instructions with screenshots from one to five reference webpages. Agents must selectively interpret and utilize these references while rendering, visually inspecting, and iteratively refining their outputs. We evaluate the resulting open-ended artifacts using independently verifiable keypoints and complementary programmatic and VLM judges. Across nine frontier (M)LLMs, the strongest system achieves an overall score of only 52.12 out of 100, revealing that visual-reference-conditioned agentic generation remains a substantial challenge for current models in practical webpage-development settings.

---


### 496. [Agent World Model in the Wild: Computer-Use Agent Environment Synthesis](https://arxiv.org/abs/2610.26828)

**<font color=#1a73e8>作者：</font>** Zhaoyang Wang, Qianhui Wu, Haorui Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent learning is shifting from learning from human data toward learning through interaction with the world. However, scaling such learning directly in real-world computer systems is challenging and can introduce substantial security risks. We therefore propose Agent World Model in the Wild (WildAWM), a scalable pipeline for synthesizing controllable environments and tasks for training general computer-use agents (CUAs). Whereas existing approaches typically specialize in a single agent interaction interface, we construct executable environments that jointly support graphical user interfaces, model context protocol services, and command-line interfaces, allowing agents to flexibly combine visual interaction, tool use, and code execution. WildAWM is entirely powered by open-source models, demonstrating that high-quality computer-use environments can be generated without proprietary frontier models. Beyond environments, we address three recurring challenges in task synthesis: ensuring solvability, maintaining sufficient difficulty, and producing reliable verifiers, by introducing execution-based quality gates that combine heterogeneous agent rollouts, cross-judge consistency checks, and counterfactual probes of judgment robustness. The resulting pipeline synthesizes 341 long-horizon environment-task pairs that can require over 100 agent steps to solve and remain challenging even for frontier models, with GPT-6-Astra solving only 60% of them. We train two Qwen models of different sizes exclusively in these synthetic worlds. Both models achieve substantial gains across 8 out-of-distribution benchmarks spanning web, claw, and computer-use agents, demonstrating that learning in WildAWM's synthesized worlds generalizes broadly to unseen computer-use tasks. The code is publicly available at this https URL.

---


### 497. [Competing Learning in Hybrid Architectures](https://arxiv.org/abs/2610.26830)

**<font color=#1a73e8>作者：</font>** Xingyu Shen, Yingfa Chen, Ziqing Qiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many modern language models have adopted hybrid architectures that incorporate both linear-time recurrence and softmax attention. Modern recurrence layers provide a highly expressive mixing mechanism while ensuring high throughput by compressing contextual information into a fixed-size state, but underperform softmax attention in contextual information retrieval. In this paper, we reveal a Competing Learning phenomenon where different kinds of mixers compete to learn the same function, and when any layer learns a function, it suppresses the corresponding learning signal for other layers. Layer attribution analysis reveals that under typical data distributions, modern recurrence learns retrieval functions faster than softmax attention, causing attention to fail to learn retrieval in most cases. Stopping weight updates in recurrence in the middle of training helps attention learn retrieval. Based on these results, we propose a staged training procedure for pre-training hybrid architectures on natural language. Empirical results on models up to 1B parameters show that our method results in substantial improvement in language modeling loss, common-sense reasoning, as well as a wide range of retrieval-related tasks across different context lengths.

---


### 498. [Same Simulation, Different Evidence: Where Retrieved Tool Output Costs LLM Agents Accuracy](https://arxiv.org/abs/2610.26836)

**<font color=#1a73e8>作者：</font>** Ke Zhang, Sahchit Chundur, Jerry Peprah Owusu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents that compute the right answer can still answer wrongly. Agent harnesses increasingly keep long tool outputs out of the context window, saving them to files that the agent searches or reads on demand. We ask where this costs accuracy with a real scientific tool: PHREEQC, a widely used geochemistry simulator from the USGS, whose reports reach 846.8k characters and whose determinism lets every printed value be traced. Agents use it to answer 158 execution-verified multiple-choice items. When agents read the simulator's report through a section index rather than in context, GPT-5.1 and GPT-5.2 lose 11.3 and 7.9 points of accuracy, while Claude Opus 4.6 and Claude Sonnet 4.6 show no detectable cost. Re-running all 11,007 logged simulator calls shows that both GPT models compute the keyed value about as often as before; what changes is the evidence they answer from. Under retrieval they often skip the report, answer from their own higher-precision output files, and misround to a neighboring option, a failure we call evidence substitution. With the simulation held fixed, retrieval still costs GPT-5.2 9.4 points. For GPT-5.4, more frequent correct simulations mask an evidence-use loss of about ten points, leaving a net change indistinguishable from zero. Naming the authoritative output raises accuracy by 6.3-7.9 points over plain retrieval for the three GPT models; for GPT-5.1 and GPT-5.2, inlining outputs that fit works as well, while asking for correct rounding does not. Context-management choices in agent harnesses should be judged by where accuracy is lost, not only by final accuracy.

---


### 499. [SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration](https://arxiv.org/abs/2610.26837)

**<font color=#1a73e8>作者：</font>** Javad Rajabi, Hakki Can Karaimer, David B. Lindell 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) achieve high-fidelity image and video generation, but they suffer from substantial inference costs due to repeated transformer evaluations across many denoising steps. Feature caching reduces this cost by reusing features across denoising steps. Recent forecasting methods extend this idea by extrapolating features to skipped steps instead of reusing them. However, existing forecasting methods extrapolate the features they predict uniformly, even though the spatial-frequency components of these features change most at different stages of denoising. They also overlook that denoising progresses nonuniformly, so equal step intervals can correspond to very different amounts of change. These mismatches amplify forecast errors as more steps are skipped, limiting the achievable acceleration. We propose SpecKCast, a training-free method that forecasts the model output in the frequency domain. SpecKCast applies a 2D discrete cosine transform (DCT) to the output and tracks each coefficient with a lightweight Kalman filter along a band-specific time coordinate derived from the noise schedule. The filter tracks each coefficient's value and rate of change, and the transformer is evaluated only when the filter's forecast uncertainty exceeds a threshold. Experiments on FLUX.1-dev, Qwen-Image, Wan2.1-14B, and HunyuanVideo show that SpecKCast achieves a better trade-off between acceleration and fidelity than existing caching and forecasting methods, reaching up to 6x speedup with less than 0.05 GiB of additional memory.

---


### 500. [LatComm: Reusable Context Compression for Latent Communication between Large Language Models](https://arxiv.org/abs/2610.26840)

**<font color=#1a73e8>作者：</font>** Huawei Lin, Jinting Liu, Tan Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systems that combine several large language models (LLMs) often use one context for many questions. When the context is passed between models as text, the receiving model processes all of its tokens again for every question. Avoiding this cost requires a context representation that is compact, reusable across questions, and readable by a different LLM. Existing compression and latent communication methods each provide only some of these properties. We introduce LatComm, a Latent Communication interface that provides all three by separating encoding from reading: the context is encoded once without the question, and the receiver selects what to read for each question. A frozen context encoder LLM compresses the context into a fixed-size packet and sends it to a different frozen receiver LLM, which reads the packet through cross-attention, with gates computed from its prompt. On 12 multiple-choice question-answering datasets, LatComm improves average accuracy over single-vector baselines by up to 10.2 points. On QuALITY, it reduces the receiver's input by 57x and answers the questions of an article 3x faster.

---


> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-548](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
