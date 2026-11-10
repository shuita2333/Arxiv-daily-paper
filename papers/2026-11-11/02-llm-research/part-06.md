# 🧠 大模型相关研究 | 2026年11月11日

> 本类共 **438** 篇论文：已确认 **405** 篇，待复核 **33** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

---

### 251. [DriveFoundry: Co-Evolving Data and Model for Efficient Closed-Loop Iteration in Autonomous Driving](https://arxiv.org/abs/2611.11532)

**<font color=#1a73e8>作者：</font>** Ziyang Yao, Yuncheng Jiang, Fang Li 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A driving foundation model must learn reusable decision knowledge from rare critical events and apply it under strict runtime constraints. We introduce DriveFoundry, a closed-loop framework improving iteration efficiency under data and computation budgets by coupling structured causal data refinement with adaptive inference. The Data Engine builds traceable scene-candidate records linking scene evidence and factor-decision relations to candidate trajectories and outcome assessments. Candidate comparisons and counterfactual annotations clarify how scene factors affect behavioral feasibility and preference. Verified model failures guide VLM-assisted annotation and expert correction, refining training data and annotation systems. The model engine, Xiaomi-Drive-o1, unifies Perception, Causation, Action, World, and Value within a shared vision-language backbone to enable cross-task knowledge transfer. Block-wise latent refill passes candidate-specific evidence and predicted visual consequences between task blocks, connecting scene understanding, planning, and evaluation. A learned value-of-computation head selects tasks and allocates latent tokens based on expected benefit and cost, adapting inference to each decision. On PhysicalAI, the 9B model achieves the lowest ADE@1 across evaluated splits and horizons among tested models. In AlpaSim, it outperforms Alpamayo 1.5 across all metrics and achieves lower close-encounter and off-road rates than the 34B Alpamayo 2 Super, while trailing in progress and AlpaSim scores. For the 0.8B variant, joint training reduces 5 s minADE@6 by about 54% without altering the inference path or token budget. Adaptive inference matches full reasoning performance using only 28% of tokens. Real-vehicle tests confirm runtime feasibility, supporting a unified paradigm for learning from critical experience and dynamically allocating computation.

---


### 252. [PRISM: Causal Counterfactual Minimization of Agent Tool Privileges via Information Bottleneck Role Induction](https://arxiv.org/abs/2611.11539)

**<font color=#1a73e8>作者：</font>** Yang Luo, Qingni Shen, Tairui Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper shifts the object of role engineering from human users to large language model (LLM) agents, and proposes PRISM to address the over-authorization that arises when an agent obtains full tool privileges through the Model Context Protocol (MCP). PRISM formulates whether a tool is necessary for a task as an intervenable causal proposition, and applies structured interventions in a sandbox to learn a counterfactual necessity model. It then compresses trajectories into discrete latent variables through an information bottleneck, and determines the number of roles from the knee of the rate-distortion curve. Finally, it formalizes pruning as a bilevel Stackelberg game, in which a generative flow network samples diverse near-optimal solutions. On three public benchmarks, AgentDojo, $\tau$-bench and ToolEmu, PRISM compresses the number of authorized tools per role by 78.3%, attains a task success rate of 78.2%, reaches a counterfactual necessity accuracy of 88.7%, and lowers the blast radius to 15.9%.

---


### 253. [Safeguarding Agentic AI in Radiology Workflows: A Multimodel Evaluation of Rule-based and Large Language Model-based Verification](https://arxiv.org/abs/2611.11541)

**<font color=#1a73e8>作者：</font>** Semil Eminovic, Robin Schmidt, Bogdan Levita 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Purpose: To estimate how often tool-using large language model (LLM) agents record clinically relevant false or unsupported information in simulated radiology documentation and how much safeguards applied before each action reduce these errors.
Materials and Methods: In this simulation study (October 2026), 48 synthetic, radiologist-reviewed base scenarios covered finding communication, tumor board preparation and follow-up management. Forty-three also had a misleading-information variant (91 variants). Six LLM agents (Claude Sonnet 5.5, GPT-6.1-Sol, GLM-5.3, MiniMax M3, Gemma-4-31B, Qwen3.8-27B) completed each variant with permissions only, deterministic rules, and rules plus a locally run LLM checker (1638 episodes). The primary outcome was at least one executed high-severity violation per episode. Risk differences were estimated per agent at base-scenario level and, exploratorily, pooled across agents, with analyses of document access and blocks.
Results: With permissions only, 7.3%-27.1% of episodes had a high-severity violation (pooled across agents, 19.4%). Pooled, it was 16.7% with rules (-2.8 percentage points; 95% CI: -6.1, 0.5) and 13.2% with rules plus the LLM checker (-6.2; 95% CI: -9.5, -3.0). Adding the LLM checker to rules changed it by -3.5 (95% CI: -6.3, -0.7). No difference between agents was detected (P = .43), and task success did not decrease detectably. In misleading variants, agents opened the altered document in 83% of episodes regardless of error, and 58% of erroneous statements cited it. Most blocked actions (64%-68%) would not have caused a violation and were returned for revision.
Conclusion: Layered safeguards reduced but did not prevent high-severity errors. Errors after misleading information reflected misjudged rather than missed information.

---


### 254. [When Should Diffusion Language Models Reconsider Their Commitments?](https://arxiv.org/abs/2611.11551)

**<font color=#1a73e8>作者：</font>** Haoyang Zheng, Yidong Ouyang, Blake Jianhang Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked Diffusion Models (MDMs) are well known for fast text generation via parallel decoding. However, independent parallel sampling can commit to inconsistent predictions, and less is known about how to selectively revise these early token commitments. In this work, we introduce $\underline{\mathrm{P}}$lanned $\underline{\mathrm{U}}$nmasking-and-$\underline{\mathrm{R}}$evision Joint $\underline{\mathrm{L}}$earning (PURL) for MDMs, a training-based framework that seamlessly unifies parallel generation with selective token revision. We derive a normalized joint transition whose likelihood factorizes into edit selection, unmask selection, and token prediction. These components are trained jointly on partially masked sequences constructed according to the model's own unmasking policy. During inference, all three decisions are supported by a single shared forward pass, enabling the model to decode masked tokens and revise noisy tokens. Across logic puzzles, mathematical reasoning, and code generation, PURL improves accuracy at matched unmask budgets, with relative gains up to 47.4% accuracy improvement and up to an $8\times$ reduction in scheduled decoding rounds. Beyond these gains, our analysis further reveals general principles of revisable decoding: token edits become more effective as context accumulates; early edits can steer unfinished trajectories, whereas later edits tend to remain localized; and effective edits therefore depend on both calibrating when to intervene and learning where and how to revise. Together, these suggest that effective parallel generation depends not on revising more tokens, but on making the right commitments revisable at the right time.

---


### 255. [InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure](https://arxiv.org/abs/2611.11558)

**<font color=#1a73e8>作者：</font>** InfraRSI Team, Yuchuan Tian, Haocheng Mei 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Recursive Self-Improvement (RSI) accelerates isolated algorithm and kernel synthesis, distributed LLM training depends on tightly coupled launch settings, operator kernels, and communication schedules, where single edits often hit out-of-memory (OOM) boundaries, compiler conflicts, measurement jitter, or silent numerical drift. We present InfraRSI, the agentic harness that turns open-ended human commands into verified training optimizations via a five-stage workflow: init locks editable scope and a fixed task contract over workload, loss, and timing invariants to prevent reward hacking, doctor profiles baseline phases and calibrates cluster noise, run co-optimizes launch knobs and code patches before re-verifying top candidates against the baseline and logging findings to a cross-hardware experience bank, and report and apply audit source paths, track failed-trial costs, and commit promoted changes. Rather than stepping greedily from a single incumbent, InfraRSI initializes from diverse experience-seeded configurations and fits global execution-time and censored peak-memory models across all trials, including OOMs. Using these models, it prices per-setting memory costs, revises miscalibrated LLM priors from live runs, and pairs memory-hungry optimizations with memory savers and verified code patches. Across four single- and multi-node dense and Mixture-of-Experts (MoE) LLM workloads, InfraRSI achieves a speedup of up to $2.75\times$ and lifts mean Model FLOPs Utilization (MFU) from $17.4\%$ to $30.0\%$, outperforming existing tuners and coding agents while transferring experience across GPUs. As it improves training infrastructure efficiency, InfraRSI forms a two-level Recursive Self-Improvement loop---revising priors online within runs and distilling experience across clusters---to push foundation model scaling.

---


### 256. [LiveAsset: Learning Intent Assets from Corrective Interactions for Agent Runtime Control](https://arxiv.org/abs/2611.11560)

**<font color=#1a73e8>作者：</font>** Guanming Liu, Weihang Wang, Peng Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents acting across web applications and online services often need multi-turn corrections to align their work with users' underspecified goals and preferences. In practice, users may identify problems in the current outcome without specifying the desired result, so learning user intentions requires interpreting each correction against the agent's preceding and revised outcomes. These expectations are often connected to a particular context, making it hard to know when they apply and how to ensure the agent later acts as the user expects. To this end, we propose LiveAsset, an intent harness that learns reusable intent assets from corrective interactions and uses them for runtime control of agent execution. LiveAsset jointly interprets each correction with the agent's original and revised results to infer user intent, incrementally updating the assets while preserving earlier requirements that remain applicable. The learned requirements guide agent execution from task entry and provide criteria for runtime verification, which uses the explanations to assess applicability before each reply is delivered and directs the agent to revise the result to address unmet requirements while preserving those already satisfied. Following a learning phase in which simulated users progressively reveal requirements through multi-turn corrections, we evaluate LiveAsset using same-task replay of the original requests on {\pi}-Bench, PERMA, and Vita and cross-task transfer on PAST-Bench and SkillEvolBench. Experiments show that LiveAsset better fulfills requirements learned from corrective interactions and improves performance on these benchmarks compared with memory, skill, and rule-based harness baselines. Code is available at this http URL.

---


### 257. [Actions Should EARN Their Credit: Test-Time Adaptation and Route Consolidation for Frozen LLM Agents](https://arxiv.org/abs/2611.11565)

**<font color=#1a73e8>作者：</font>** Bian Sun, Kevin Zhai, Mubarak Shah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents can use feedback from repeated attempts to improve their decisions without updating model parameters. However, positive action credits can continue to favor actions that repeatedly achieve the same score, even when higher scores are achievable. Under a fixed interaction budget, trying new actions in the final attempts can also lower performance. We introduce EARN, a method that uses past experience to guide further progress and retain earlier performance through conditional reuse of effective action sequences. EARN reduces action credits for reaching scores repeatedly attained in earlier episodes and assigns larger credits to action segments that reach higher scores. These credits adjust the probabilities of LLM-proposed actions. During the final episodes, EARN directly replays stored actions when the current context matches the recorded context and the actions remain available, bypassing LLM candidate generation. We evaluate performance at the end of the interaction budget using the average score over the final four episodes. Across Jericho, ScienceWorld, and Crafter, EARN achieves the best score on this metric in 31 of 33 task--budget settings among the evaluated methods, including ties. Across the evaluated Jericho budgets, replay bypasses 78.9--86.3\% of candidate-generation calls in the final four episodes, averaged across games.

---


### 258. [Beyond the Transcript: Measuring and Improving the Use of Acoustic Information in Audio Language Models](https://arxiv.org/abs/2611.11573)

**<font color=#1a73e8>作者：</font>** Linkai Peng, Baorian Nuchged, Yuyang Yao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio language model benchmarks provide comprehensive evaluation across diverse tasks. However, some tasks can be answered from the transcript or even the question alone, and benchmark scores can therefore confound acoustic understanding with language modeling ability. We distinguish lexical tasks, for which the transcript usually suffices, from global-attribute and within-recording-structure tasks, which require the model to analyse the recording beyond its words, either as a whole, for properties such as the speaker and emotion, or within it, for patterns such as stress and intonation. We evaluated 19 open models and Gemini 3.1 Pro on 92 tasks from 6 benchmarks and estimated the recording gain, the accuracy advantage of the original recording over references that retain its words, by comparing the recording with synthetic readings of its transcript and by adding it to the transcript. On attribute and structure tasks, the open models fall behind Gemini by 28.6 and 41.9 percentage points, and about half or more of each deficit lies in the recording gain. Nevertheless, linear probes in Gemma-4 12B and Qwen2.5-Omni-7B show that the acoustic information needed for answering is already readable in early language-model layers, while the readout of many cues declines in the layers that follow. We therefore constructed training data and trained LoRA adapters in these layers, with a content anchor, which raises attribute and structure accuracy by 12.8 to 44.4 points in the two models and keeps mean lexical accuracy within 1 point of the base model. Most of the improvement appears as larger recording gains. These results suggest that training improves the use of acoustic information that the models already encode.

---


### 259. [Same Error, Different Recovery: How Delivery Changes LLM Agent Behavior](https://arxiv.org/abs/2611.11581)

**<font color=#1a73e8>作者：</font>** Sunghyeun Woo, Javier Conde, Pedro Reviriego  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A tool-using language model must decide whether to retry a failed call, correct it, or stop and tell the user. The error text alone may not be enough: the same feedback can lead to different actions depending on where it appears in the conversation. We isolate this delivery problem by varying placement, guidance, retained history and turn structure. Two studies with plans fixed before data collection, across 13 open models from 3B to 70B parameters, compare the next action and subsequent task completion, with exact deterministic reruns. A new user turn that retains the failed exchange avoids the severe stopping failure observed in Llama models when that exchange is removed. It is non-inferior to history rewriting in pooled synthetic comparisons, but is not best for every model. We implement this form as an opt-in recovery layer within a deterministic inference engine and evaluate it on public benchmarks and a coding agent. On ToolMaze, it raises success on explicit errors by 14.2 points with 7-8B models and 10.5 points with 32-70B models; Loud/Quiet, 24 multi-turn tasks with visible failures and silent corruption, scored by final-state agreement, shows no measurable gain. A client given the exact fault kind performs better still. The findings support delivery as a distinct factor in recovery, not an engine-exclusive solution or a universal retry policy.

---


### 260. [NightSteps: A Night-Time Dataset and Benchmark for Pedestrian Crossing Intention Prediction](https://arxiv.org/abs/2611.11583)

**<font color=#1a73e8>作者：</font>** Sjoerd Takken, Shaodi You  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles use pedestrian crossing intention prediction (PCIP) to participate safely in traffic. Existing models are largely trained under favourable daytime conditions with sufficient daylight. Little is known about the robustness of these models under night-time and low-light conditions, due to the lack of datasets containing night-time footage. This paper investigates how a dataset, named NightSteps, can be constructed and evaluated as a baseline benchmark. The dataset is based on nighttime dashcam footage collected from six different cities around the world, capturing a wide variety of road conditions. The dataset consists of dashcam-recorded point-of-view footage, raw data of pedestrians' locations with corresponding 'track ids' and ground-truth labels containing accurate information about pedestrian crossing behaviour, resulting in a diverse dataset. Gemini, ChatGPT, and human assessment are used to demonstrate the usability of the dataset by predicting crossings in clips from the dataset and comparing the results with the initial ground-truth labels. These results show that human input achieves an accuracy of 88.17% and an F1-score of 80.21%. Predictions from Gemini and ChatGPT perform lower, with accuracies of 60% and 79.13% respectively, and F1-scores of 42.50% and 63.64%. The evaluation demonstrates that the NightSteps dataset can be used for future model evaluation to test the performance of PCIP, with the aim of improving road safety at night.

---


### 261. [FinCutBench: A Continually Updated Benchmark for Measuring the Temporal Boundaries of LLM Financial Knowledge](https://arxiv.org/abs/2611.11588)

**<font color=#1a73e8>作者：</font>** Siyuan Li, Ke Wan, Boyong Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In financial backtesting and other point-in-time tasks, external inputs can be restricted by date, but model parameters may retain financial facts disclosed later, introducing parametric look-ahead bias. We introduce FinCutBench, a continually updated monthly financial knowledge benchmark for measuring how far a fixed model's financial knowledge extends over calendar time. The current dataset contains 9,000 Chinese and English four-option multiple-choice questions from January 2023 to September 2026, covering Chinese and U.S. markets and four categories of financial information. We construct monthly knowledge profiles using the approximate months in which the tested facts became public. After a profile passes the decline test and knot checks, we define the FinCut Boundary as the first month when the fitted profile reaches its lower level, and report the stability of the estimated date under resampling. Boundary dates and localization precision vary across models. Using the independently measured Transition Start and Boundary as fixed references for downstream sample grouping, we find clear relative declines after the Boundary in U.S. asset ranking and earnings recall for some models, while Chinese-market ranking estimates vary across models and all eight disclosure-period-paired forecast-error comparisons have unadjusted $p$ values above 0.10. The FinCut Boundary thus provides an empirical reference for the temporal scope of parametric knowledge in point-in-time financial evaluation, supporting evaluation-window selection and result interpretation.

---


### 262. [Out of Parameters, Saved by Syntax: UD-PrMPT for Parser Augmented Low Resource Machine Translation](https://arxiv.org/abs/2611.11597)

**<font color=#1a73e8>作者：</font>** Emma Thronson, Abhishek Purushothama, Amir Zeldes  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work advancing machine translation quality using LLMs for very low resource languages has relied on the injection of lexicon-based prompt components to expose vocabulary to models. However, these approaches run into a ceiling when models must guess sentence meaning purely from plausible combinations of possible word senses mapped to strings. In this paper we test UD-PrMPT, an approach using syntactic analyses in the Universal Dependencies formalism as prompt components to improve MT in five diverse low resource languages: Beja, Chintang, Chukchi, Coptic, and Xibe. Our results show additive improvements which stack on top of the lexicon based approach which are stronger for higher quality manual analyses but consistent for predicted parses as well.

---


### 263. [Perturbing Inputs Improves Pretraining Distillation](https://arxiv.org/abs/2611.11598)

**<font color=#1a73e8>作者：</font>** Ziyang Cai, Yihe Dong, Dimitris Papailiopoulos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation trains a student language model to match a teacher's predictions on the training text. We ask whether learning the teacher's behavior beyond the training text can further improve the student. We investigate this using three input perturbations: additive token noise, blending two documents, and blending neighboring tokens. Specifically, for an early part of pretraining we perturb the inputs and train the student to match the teacher on them, and we spend the rest of the same token budget on ordinary distillation. When pretraining from scratch, the best method improves on standard distillation at both scales we tried, by 0.025 nats at 135M parameters and by 0.020 nats at 0.5B (mean of three seeds). At 135M this is 1.45 times the gain that distillation itself provides over next-token training. We also observe promising downstream transfer: at 0.5B, the best variant improves average zero-shot accuracy by about one percentage point across seven tasks. It also retains its validation-loss advantage after low-bit weight quantization. We also test a data-limited setting in which training data must be reused, and find that the gains persist. Finally, ablations suggest that, for additive noise, perturbing the teacher's inputs contributes most of the gain, while perturbing only the student's inputs yields much less.

---


### 264. [Weight-Space Programming of Policies and Their Verification via Model Checking](https://arxiv.org/abs/2611.11604)

**<font color=#1a73e8>作者：</font>** Dennis Gross  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can write the weights of small neural networks directly, without gradient descent. This weight-space programming creates policies for sequential decision-making from a task description alone, but nothing guarantees that a written policy behaves as intended. We combine weight-space programming with probabilistic model checking. Given an environment modeled as a Markov decision process and a requirement in probabilistic computation tree logic (PCTL), an LLM writes all weights of a policy network, optionally repairs them on a dataset of optimal actions, and receives model-checking feedback until the requirement holds or a round limit is reached. The model checker Storm computes, rather than estimates from simulations, the probability that the policy satisfies the requirement, so every returned policy is verified. With two LLMs on three environments, the created policy of each of the 18 runs attains the optimal probability, before any dataset or model-checking feedback. Four of six policies programmed for two transporter jobs also complete three jobs with probability 1, so they generalize to a task that the LLM never saw. The pipeline also programs a policy that satisfies a complex safety requirement expressed with the PCTL until operator in all six runs. In one of them, dataset repair raised the accuracy to 98.4\% but broke the requirement, and one round of model-checking feedback restored it.

---


### 265. [ODSA: Orchestrated Discovery and Self-Aggregation](https://arxiv.org/abs/2611.11621)

**<font color=#1a73e8>作者：</font>** Macardle Meng, Haomin Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling improves the accuracy of a language model's answers by spending more computation at inference time. Established methods do so either sequentially, revising a single solution over several passes, or in parallel, generating several independent solutions and selecting among them. We present ODSA (Orchestrated Discovery and Self-Aggregation), an LLM-directed scaling framework in which an orchestrator LLM is given existing test-time scaling methods as actions --- discovery of a new independent solution, comparison of existing solutions to build a better one, and acceptance of a proposed answer, which triggers its verification --- and directs stateless workers to carry them out. The orchestrator does not solve the problem itself: it allocates computation, feeds the results of earlier actions into later ones, and takes every action from a single context, so that each decision is informed by everything tried before. On Humanity's Last Exam, ODSA improves accuracy by 4.7 to 18.0 points across three models over a single direct call to the model with no test-time scaling. On LiveCodeBench, where a single direct call already solves most problems, it improves accuracy by 0.6 to 14.0 points.

---


### 266. [Inside the Trading Loop: Markets, Models, and Moves with LLM Agents](https://arxiv.org/abs/2611.11657)

**<font color=#1a73e8>作者：</font>** Renee Jia, Di Mu, Yao Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We built a hybrid multi-agent trading system that combines large language model (LLM) analysts with momentum-based portfolio construction and rule-based execution. Company-news and macroeconomic agents return structured reports to a coordinator that sets stock weights and cash reserves. We evaluate the portfolio engine using its broker-recorded paper account, which operated with deterministic fallbacks, and compare LLM-enabled configurations through retrospective replays. From March 11 to August 28, 2026, the account returned 34.5%, compared with 14.4% for the S&P 500 fund SPY over the same dates. This raw return advantage came with a larger maximum drawdown. Reconstructed policies also finish above matched SPY and QQQ references when assessments are used in the same session or deferred to the next. Design comparisons examine cash authority, selective invocation, and response contracts. A constant-cash control gives a return estimate close to stance-based sizing, and shorter report contracts improve observed parsing but can change recommendations.

---


### 267. [Measuring Generative AI Content in Political Campaigns: Evidence of Rising Adoption and Non-Disclosure](https://arxiv.org/abs/2611.11658)

**<font color=#1a73e8>作者：</font>** Anna-Maria Gueorguieva, Nic Weber  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The use of generative AI in political campaigns has drawn public concern and policy attention. Public concerns range from distrust of candidates to skepticism about the authenticity and accuracy of political advertising, including AI-generated images and video. Nearly half of U.S. states have enacted laws that prohibit, or require disclosure of, "materially deceptive" AI-generated content (AIGC) in elections to guard against these concerns. This study measures how candidates and their campaigns produce and circulate AIGC during an election cycle. We develop two measures that estimate not only wether campaigns use AIGC, but how much they produce (magnitude) and in what forms (modality). We apply these measures to a novel dataset of text and images from the campaign websites, X accounts, and emails of 12,977 candidates for U.S. political office from 2023 to 2025. We report three findings. First, detectable AIGC from campaigns increased significantly across modalities over the observation window, and campaigns that use AIGC frequently do not disclose it. Second, incumbents' campaigns produced significantly less AIGC than challengers' campaigns. Third, candidates in states with AIGC disclosure or prohibition laws do not produce measurably less AIGC than candidates in other states. Our method and findings have implications for transparency and trust in elections, and on state laws that regulate AI use in campaigns. Because current state laws largely target mainly "materially deceptive" content, we identify additional policy mechanisms that could increase electoral transparency and improve trust as AIGC becomes more prevalent.

---


### 268. [RADE: Risk-Adjusted Deployment Efficiency, A Framework for Routing, Memory, and Escalation in Safe LLM Systems](https://arxiv.org/abs/2611.11659)

**<font color=#1a73e8>作者：</font>** Chaymaa Abbas, Kareem Hassani, Mariette Awad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A deployed language model does not merely answer questions. It spends computation, consumes time, consults evidence, exposes memory, invites or avoids human review, and sometimes makes mistakes whose consequences are radically unequal. Yet LLM systems are still commonly compared as if the relevant object were a single model and the relevant outcome were a single benchmark score. This paper argues that the unit of analysis should instead be the deployment policy: the mechanism that decides when to retrieve, when to remember, when to call a larger model, when to verify, and when not to answer at all. We introduce risk-adjusted deployment efficiency (RADE), a system-level objective that scores the utility a deployment delivers net of inference, retry, oversight, and priced expected failure cost, while treating harms that cannot be priced as hard budgets alongside constraints on latency, privacy, and resources. The framework brings selective routing, retrieval and governed memory, efficient specialization, uncertainty estimation, abstention, and human escalation into a common account. We then examine five deployment regimes in which the same nominal LLM capability leads to different rational architectures, and propose a reporting protocol based on risk-coverage behavior, end-to-end cost, update drift, memory exposure, evidence quality, and escalation load. The central claim is modest but consequential: frontier capability should be treated as a resource to allocate, not a default state to maintain. A safe and sustainable system is not the one that always uses the strongest model; it is the one that spends capability where the reduction in risk or increase in utility justifies the cost.

---


### 269. [SurfScaff3D: Bridging Geometric and Semantic Representations for LLM-based 3D Object Generation](https://arxiv.org/abs/2611.11678)

**<font color=#1a73e8>作者：</font>** Anay Loya, Rishi Gupta, Arnav Samal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creating high-quality 3D content has traditionally required specialist expertise and experience with complex tools. The growing ecosystem of AI-assisted creativity demands accessible and intuitive 3D generation systems. Recent advances in Large Language Models (LLMs) offer promising directions, yet extending their generative capabilities to 3D remains fundamentally challenging because existing 3D representations are not naturally compatible with language-based reasoning. Current approaches either depend on expensive fine-tuning or impose restrictive structural priors that sacrifice expressiveness and exclude organic shapes. We argue that the mismatch between LLM-native reasoning and conventional 3D parameterizations is a core bottleneck of LLM-driven 3D generation. To address this, we introduce the Hierarchical Patch Scaffold (HPS), a representation designed around semantically meaningful, interpretable part-level abstractions that are naturally understood by both humans and LLMs, enabling expressive, editable, and open-domain 3D generation without imposing restrictive geometric priors or expensive fine-tuning.
Building upon HPS, we introduce SurfScaff3D, an interactive framework for text and image-to-3D generation. HPS inherits the flexibility of B-spline patches, while exposing an interface that leverages open-world capabilities of foundation models to reliably generate 3D. Its hierarchical part-level semantic labels enable targeted, natural-language edits at any level of granularity without re-running generation. Further, HPS offers explicit per-patch control over surface detail, enabling more expressive geometry capable of representing arbitrary objects. Extensive experiments against state-of-the-art LLM-based 3D generation methods demonstrate strong geometric fidelity, semantic alignment, and flexible editing across diverse object categories.

---


### 270. [The Average Patient: Do Simulated Psychiatric Patients Answer Like Real People?](https://arxiv.org/abs/2611.11679)

**<font color=#1a73e8>作者：</font>** Weixiang Sun, Zehong Wang, Kaiwen Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are used as simulated psychiatric patients to train clinicians and evaluate AI therapists, and are judged by plausibility or total scores. We give a framework for simulated respondents: an information budget bounds how much simulated patients can differ, and an average-patient hypothesis, that a model answers each item at the level typical of the named condition and severity, implies little variation, a full profile of the condition's typical symptoms and totals at or above the top of the stated severity band. We examine these implications at matched totals on item-level data from eight human samples, including a clinical and an instructed-feigning sample. Across 17 models, simulated patients vary 1.5 to 11 times less than real respondents with the same total and on most questionnaires endorse nearly every symptom at a middling level; on the PHQ-9 their symptoms covary less like real ones. People, honest or feigning, answer "not at all" about as often as genuine patients with the same totals, and more often than every model. Single answers are highly concentrated, and prompt changes, published personas, larger models and reasoning reduce the pattern without removing it. In interviews, patients told a severity are rated as having nearly every symptom, so an assessment agent's recognition of absent symptoms goes untested, and scored against the stated severity the agent places a quarter of them in their band, against about half of patients given a real symptom profile. Having the model word such a profile restores half to two thirds of the variation.

---


### 271. [Self-Indexing Latent Memories for Access-Aware Continual Instruction Tuning of LLMs](https://arxiv.org/abs/2611.11684)

**<font color=#1a73e8>作者：</font>** Dhruv Dixit, Paritosh Pandey, Snehalkumar 'Neil' S. Gaikwad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continual instruction tuning often preserves old skills with task-private modules. Inference still requires selecting the right module from the prompt alone. We introduce Task-Isolated Latent Adapter Continual Training (TILA-CT), a replay-free method that makes each task module self-indexing. Each task receives a latent memory and adapter bank in a frozen LLM. During adaptation, the memory gathers causal-prefix information and injects task-conditioned context. For access, its persistent state provides the routing prototype used by a shared prompt-only router. On the 8-task CT-Pipeline stream, TILA-CT achieves 65.19 acquisition and 63.98 final macro score, with 1.38 points of average forgetting. A middle-reversed order gives 65.38 acquisition and 64.17 final macro score. Across 6 backbones, final scores remain within 1.5 points of acquisition. Ablations support memory-derived routing keys and causal gathering. Final macro routing accuracy is 93.9\%, and oracle routing recovers 1.21 final macro points. These results separate preserved task computation from learned access to it.

---


### 272. [LocateAnyMesh: Grounding 3D Mesh Queries in 2D Images with Vision-Language Models](https://arxiv.org/abs/2611.11692)

**<font color=#1a73e8>作者：</font>** Chris Choy, Zhiding Yu, Jan Kautz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Textured 3D meshes specify object geometry and appearance, making them a natural query for finding a particular asset in an image. We introduce LocateAnyMesh, a vision-language model that uses the mesh itself as part of its prompt. A frozen 3D encoder maps colored surface points to a compact token sequence, which a learned connector places alongside image and instruction tokens. We evaluate two grounding models with PPAT mesh tokens: LAM-Select selects image-region proposals, while LAM-Direct predicts coordinates directly. Neither requires rendered query views or view-template matching. New objects require a single encoder pass and no object-specific fine-tuning. LAM-Select improves localization on the reported real-image suites and the official BOP YCB-V evaluation. Secondary experiments compare mesh encoders, and a LAM-Direct study isolates surface color. A single-seed LAM-Select continuation supplies pointing and mesh-only description evidence without replacing the reported localization model. The results support mesh tokens as a query representation, with remaining limitations in presence decisions, identity binding, proposal coverage, and descriptive fidelity.

---


### 273. [Language model capabilities fail in a shared, predictable order under compression and perturbation](https://arxiv.org/abs/2611.11695)

**<font color=#1a73e8>作者：</font>** Zhixiang Wang, Ulas Bagci  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Compression can preserve a language model's average accuracy while selectively degrading individual capabilities. Whether these losses follow method-specific patterns or a transferable order is unclear. We applied seven perturbation and compression methods to eight instruction-tuned models, scoring 16 tasks in four answer formats against preregistered predictions. Short-answer capabilities failed in nearly the same order under four random perturbations with different mechanisms (median correlation 0.90) and, within each model, under pruning and quantization (0.875). Intact answer margin, answer frequency and answer format predicted this order. Fragility profiles measured under random perturbation predicted which tasks and facts compression removes first and, after four-task calibration, held-out task accuracy (median absolute error 0.11-0.12, against 0.20-0.21 for uniform decline); profiles borrowed from other model families did almost as well. The order did not transfer across models under GPTQ quantization or hold for long-form tasks. Within short answers, what compression removes is predictable before deployment.

---


### 274. [Direct GPU Energy Measurements of Batch-Level Sharing in Mixture-of-Experts and Recurrent Models](https://arxiv.org/abs/2611.11696)

**<font color=#1a73e8>作者：</font>** Rafael Pina, Varuna De Silva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Energy claims for efficient neural networks are often inferred from operation counts. We report direct GPU energy measurements on two workloads that batch very differently, recurrent policies in GPU-vectorised multi-agent reinforcement learning (MARL) and mixture-of-experts (MoE) language models, and ask one question of both: can the rows of a batch be made to share computation, across the batch and over time, at a measured saving? On recurrent policies the answer so far is no. Shared activity patterns exist but rarely last one step, masking a frozen policy fails, and trained-in masks succeed only because a fixed mask is equivalent to a narrow GRU, at 11x the energy of a small dense policy in our implementation. Test-time steering adds nothing beyond re-picking on either workload. On MoE models the answer is yes, and granularity decides how much: on Qwen3-30B-A3B, batch-aware routing reads 25-31% fewer expert weights within KL 0.05, with benchmark changes within noise at 500 items, and uses 12-18% less energy per token on a fused forward. We also introduce persistence-aware OEA, a one-parameter rule that keeps the batch-aware cut with about 40% fewer new experts per step than native routing at batch 32-64, though its energy has not yet been measured. These are pilot measurements on one GPU type, and we state their limits.

---


### 275. [SurgTAP-3D: A Large-Scale Cross-Surgery Video Dataset with Contact-Aware 3D Motion Tracking](https://arxiv.org/abs/2611.11697)

**<font color=#1a73e8>作者：</font>** Jiaxin Guo, Wenzhen Dong, Taoyu Wu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding 3D scene dynamics in minimally invasive surgery (MIS) is a fundamental step toward physically intelligent and autonomous surgical systems. However, existing public datasets offer limited scalability and diversity in real-world clinical scenarios. Moreover, annotations typically focus on either tissue or instruments alone, overlooking tool-tissue interactions. This gap limits applications such as augmented reality guidance and autonomous surgery driven by vision-language-action (VLA) models or world models, which demand large-scale, high-quality 3D supervision. In this work, we construct SurgTAP-3D, a large-scale in-vivo pseudo-3D surgical motion tracking dataset and benchmark, comprising 520K frames, 4,549 action clips, and 1.4M 2D/3D point trajectories from diverse robotic and manual procedures under unified action categories. To make annotation scalable, we design a unified framework for surgical 3D point tracking that converts uncalibrated monocular surgical videos into structured 4D annotations through contact-region prompting, active-tool segmentation, dynamic bundle adjustment, and global 4D refinement. This pipeline adapts foundation priors to surgical videos and produces temporally consistent trajectories, pseudo-scale geometry, camera poses, and instrument masks. The dataset captures realistic challenges inherent to surgical environments, including occlusions, smoke, bleeding, and rapid instrument motion. We establish a comprehensive benchmark on SurgPose, SurgT, and STIR, covering both instrument and tissue tracking. We demonstrate instrument displacement estimation, deformable surface reconstruction, and foundation-model fine-tuning. Extensive experiments and analysis demonstrate the effectiveness of our dataset and annotation framework for 3D surgical point tracking, reconstruction, and surgical action understanding. Homepage: this https URL

---


### 276. [CASCoDe: A Closed-Loop Agentic Framework for Analog Sizing and Layout Co-Design](https://arxiv.org/abs/2611.11710)

**<font color=#1a73e8>作者：</font>** Ziming Wei, Bingyang Liu, David Z. Pan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Expert analog layouts differ from auto-generated ones in density and regularity, not only in legality: experts make a succession of discrete, hierarchical physical decisions and revisit each after extracted electrical results, while most existing automated flows act on a physical search space fixed before the controller runs. We present CASCoDe, a closed-loop LLM agent framework for analog netlist-to-layout design that formalizes those expert decisions as a hierarchical discrete action space-sizing selection, structural floorplan, local layout refinement, routing-attempt selection-on which the agent runs feedback-driven tree search from a circuit netlist to a verified GDS. The agent authors the circuit-specific floorplans and scripts, and an execution layer of interface adaptations over adapted tools make every action land at physical implementation and be judged by DRC, LVS, and extracted-RC simulation. On 20 SKY130 amplifiers spanning single-, two-, and three-stage topologies, CASCoDe is the only flow that delivers a DRC- and LVS-clean routed layout when meeting design specifications for every circuit. It reduces area by 59-85% (mean 71%) against a conventional P&R flow on identical PCells, raises mean device density from 0.39 to 0.74 against APPlace, MAGICAL, ALIGN and ICPI. A layout that beats every baseline in area and legality appears after 11 minutes of agent time on average, and ablations show that the structured action space and the feedback-guided tree search each reduce area and search cost.

---


### 277. [Steering Emergent Behavior in Multi-Agent LLM Systems via Information Networks](https://arxiv.org/abs/2611.11714)

**<font color=#1a73e8>作者：</font>** Sepehr Ilami, Babak Heydari  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly operate in groups, each pursuing an individual objective while jointly determining system performance. If an operator controls which agent observes which other agent, but not their payoffs or messages, how should observations be structured to raise collective welfare? We make the information network (who observes whom) a design object, decoupled from the fixed interaction network over which agents act. Ten identical LLM agents play repeated group-decision games; by default each observes only an anonymous summary of the group's previous-round outcome, and a manager with a fixed budget adds directed observation links that reveal peers' past actions. Across 1,080 episodes and six games spanning coordination, anti-coordination, social dilemmas, and discovery, we ask how much information to share and, at a fixed budget, who should observe whom. Disclosure creates behavioral coupling: observation acts as a contagion channel whose welfare effect depends on the alignment between individually attractive behavior and the collective objective. First, the value of information is alignment-contingent: more peer information tends to help or be neutral when individual behavior is aligned with the collective goal, but under free-riding or congestion externalities it amplifies collectively harmful behavior; in a public-goods game the group does best with no information at all. We read this sign separation as a cross-game regularity within one controlled LLM population, not a model-invariant law. Second, at a fixed budget, who observes whom matters primarily when coupling is harmful: a modular "barbell" that lets sub-populations entrench harmful behavior is reliably the worst wiring, reversing the network-reciprocity intuition from human evolutionary game theory. These results argue against a default of full transparency for agent collectives.

---


### 278. [ShadowBench-MCP: Measuring Shadow Invocations in MCP-Style Tool Routing](https://arxiv.org/abs/2611.11720)

**<font color=#1a73e8>作者：</font>** Eyhab Al-Masri, Wenjun Yang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly act as routers for tools, APIs, and software-supply-chain workflows, making an execution path - rather than generated text alone - a security-relevant model output. We study shadow invocation: a task-preserving request variant that causes an LLM router to select a riskier execution path, potentially skipping validation, provenance, staging, redaction, or audit controls even though the request does not ask for a malicious action. We introduce ShadowBench-MCP, a benchmark and metric suite that separates task preservation (TPSS), operational pressure (OPSS), and route-geometric drift (RGAS), and combines them in the pre-execution SODS score. In a focused policy-ablation study using a Groq-hosted qwen/qwen3-32b router, 120 routing decisions yield 96 original-versus-variant comparisons across six security-sensitive workflows. Efficiency-first routing produces a 29.2% shadow-invocation rate and 26.7% safety-tool skip rate. Policy-aware routing reduces these to 4.2% and 1.7%, respectively, corresponding to an 85.7% relative reduction in shadow invocations. Pre-execution signals distinguish shadow routes with ROC AUC up to 0.94. These results are early, single-router evidence of a policy-dependent routing-layer security effect, not a claim of universal vulnerability.

---


### 279. [Explaining and interrupting collective misalignment in language model systems](https://arxiv.org/abs/2611.11724)

**<font color=#1a73e8>作者：</font>** Edoardo Chidichimo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In collectives, language model agents can exchange individually innocuous messages that together support a policy violation. Understanding and preventing collective misalignment requires answering the question of which messages sufficiently influenced and necessarily enabled the violation. Collective Dependence Analysis (CDA) operationalises necessity and sufficiency to explain decisions and find the fewest removals interrupting support within tested combinations. Tests covered constructed violations, unscripted agent conversations, and recorded interactions, with selected message removals reducing violations from 93% to 6% in controlled cases. Using O(N) model evaluations for N messages, CDA achieves the same violation reduction with half the deletions of a frontier LLM judge given the transcript and asked for all supporting messages in eligible operational cases. CDA also proposes the mechanism through which the collective misalignment emerged. Nonetheless, complete explanations remain difficult on unfamiliar tasks and some removals can inadvertently disrupt correct decisions. CDA unifies explanations of collective misalignment with experimentally tested interventions.

---


### 280. [The Value of Not Knowing: How Fresh Eyes through Naive LLMs Fuel Creativity](https://arxiv.org/abs/2611.11725)

**<font color=#1a73e8>作者：</font>** David B. D'Ambrosio, Alon Albalak, Joel Lehman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many major scientific advances come from approaching a problem with a new or novel perspective. While large language models (LLMs) with internet-scale knowledge seem poised to take such perspectives, their consistent generation remains elusive. Instead, models are drawn to dominant views and preexisting, in-field bias. To explore the potential of fresh eyes to increase creativity, this paper proposes naive LLMs, models that are made intentionally ignorant of a specific topic. Through deprivation in training or intentional forgetting, naive models are unburdened by existing dogma, allowing them to be free to make new associations and conjectures. These naive models can then be paired with a stronger mentor model that can refine their unique perspectives into concrete proposals. For the 1B and 7B models tested in this paper, naive models consistently produce seed ideas that are more novel and useful than baseline counterparts, and mentor refinement improves the ideas even further. Thus, contrary to the prevailing tradition of scaling up training data, we demonstrate a case where less information is actually more powerful, in particular when the aim is to discover genuinely outside-the-box solutions.

---


### 281. [State Media at Retrieval Time: A Large-Scale Audit of Russian State-Aligned Sources in AI Chatbot Responses](https://arxiv.org/abs/2611.11727)

**<font color=#1a73e8>作者：</font>** Laura Kurek, Elijah Covert, Rafael I Bonilla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Pravda Network is a Russian state-aligned media aggregator, with over 110 websites and more than 15 million articles published since 2023. Given its prolific and repetitive output, emerging scholarship argues that the Pravda Network was built to influence AI systems. We conduct a large-scale audit of leading AI chatbots to understand: (1) the retrieval rates of Pravda Network articles, (2) the conditions of retrieval, and (3) whether chatbot responses affirm or caveat this content. We build a 10,000 prompt corpus from sampled Pravda Network headlines varied along two dimensions (headline rewording and user skepticism) and query 11 AI chatbots via the web interface (n=104,997 completed responses). Overall, we find susceptibility to Pravda Network retrieval to be infrequent---appearing in 7.3% of responses---and highly platform dependent---with three chatbots responsible for 94% of retrievals (this http URL, Claude, and Copilot). Among the frontier models, Claude is an outlier: ChatGPT, Gemini, and Meta AI retrieved no Pravda Network articles, likely indicative of a domain-level filtering policy. All 11 chatbots, however, retrieved other Russian state-aligned media to some degree (median=13.56% of responses). When Pravda Network articles are surfaced, caveat rates vary widely by platform (from 5.3% to 76.2%), with this http URL providing the fewest caveats. We also identify the tactic of headline washing: where 9.92% of sampled Pravda Network headlines attribute their reporting to other, often more credible, media outlets, while the articles themselves are republished from Russian state-aligned media. We discuss headline washing's potential to launder state media as independent reporting. With this audit, we provide a systematic analysis of AI chatbots' susceptibility to Russia's latest attempt to manipulate the information environment.

---


### 282. [GeoPilot: Diagnosis-Guided Interventions and Geometric Evaluation for Aerial Reconstruction](https://arxiv.org/abs/2611.11751)

**<font color=#1a73e8>作者：</font>** Pengyu Yin, Jie Pan, Junxiang Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a mesh reconstructed from aerial remote-sensing imagery disagrees with reference geometry, deciding what to change requires a diagnosis of the reconstruction process. We present GeoPilot, a workflow that turns diagnostics and prior observations into executable program or camera-configuration interventions. A large language model proposes the change, numerical tools reconstruct the mesh, and an external evaluator measures its geometry under a stated coordinate and reference protocol. The main case tests a shared-intrinsics hypothesis proposed before the comparison. On 224 Metashape-raster development images, shared intrinsics improved all six native-coordinate measures and reduced mean surface-to-reference distance by 7.04%. Reference-assisted alignment fitted and evaluated on separate within-scene checkerboard samples reversed the mean-distance ranking, limiting that gain to native-frame delivery. A separate matched comparison on publisher-undistorted images favored fixed published cameras on all six measures, reducing mean distance by 12.11%; the cameras retain upstream image and laser-scanning adjustment information. With one reconstruction per configuration, these comparisons provide conditional evidence for camera handling. Three end-to-end runs each delivered a mesh and six-metric evaluation from all 327 images of a second development scene.

---


### 283. [Spectral Rank and Step-Direction Dynamics in Language-Model Post-Training](https://arxiv.org/abs/2611.11752)

**<font color=#1a73e8>作者：</font>** Khurram Khalil, Khaza Anuarul Hoque  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language-model post-training modifies weights through cumulative updates and successive displacements, yet existing studies report seemingly conflicting spectral properties: nearly full-rank updates and low stable-rank changes. We show these observations are compatible and characterize update directions during training. For singular values following $\sigma_i \propto i^{-\alpha}$ with $0 < \alpha \leq 1/2$, we prove that stable rank becomes negligible relative to fixed-energy rank as dimension increases. Full singular value decompositions of selected OLMo-2-7B updates confirm this separation: three proximal policy optimization (PPO) attention updates have stable ranks of 9.6-18.3 but require 532-1,222 singular components to capture 80% of their energy. We next compute consecutive checkpoint-displacement cosines from full-model inner products. Across nine publicly released reinforcement learning from verifiable rewards (RLVR) stages, all 131 adjacent pairs have negative cosines on their native checkpoint grids, including PPO and Group Relative Policy Optimization (GRPO) trajectories. Supervised fine-tuning comparisons across four model families show configuration-dependent alignment, including negative late-training cosines for Mistral and FP32 Llama. Finally, a controlled OLMo-2-1B study with three paired seeds and a 2,048-token response cap compares group-relative advantages against a learned critic with generalized advantage estimation (GAE). At matched 60-rollout windows, late-training mean cosines are +0.259 and +0.012, respectively; the paired critic-minus-group difference is -0.247 (seed-level 95% interval [-0.358, -0.137]). These findings distinguish spectral concentration, energy coverage, and trajectory direction, and demonstrate that the advantage system influences directional alignment under matched training conditions.

---


### 284. [BridgeKV: Large-Model Prefill and Small-Model Decoding for LLM Inference via KV Cache Translation](https://arxiv.org/abs/2611.11761)

**<font color=#1a73e8>作者：</font>** Payman Behnam, Debopam Sanyal, Pranav Ponnusamy 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM inference has two phases with different bottlenecks: LLM prefill runs once per request and is compute-intensive. Decoding repeats for every output token and is limited by memory bandwidth. To address the challenges associated with this issue, different solutions have been proposed. All of these solutions use the same model for both prefill and decode phases. We propose BridgeKV, which uses a larger model for prefill and a smaller model of the same family for decoding. A lightweight KV-stitching module translates the larger model's prompt cache into the smaller model's cache layout. It handles differences in cache shape and representation through learned local layer mixing and separate nonlinear maps for keys and values. With both models frozen, we train the module to align their caches and make the smaller model follow the larger model's next-token predictions. A second training stage adds low-rank adapters when further task adaptation is needed. Across six model pairs and five datasets, BridgeKV outperforms fine-tuned small-model baselines with matched trainable parameter budgets in all 30 settings. It closes up to 80% of the quality gap to using the larger model for both phases. On one A40 GPU, Llama-3.1-Instruct-8B to Llama-3.2-Instruct-1B achieves 3.0X faster requests than the larger model alone, with latency close to the smaller model alone. BridgeKV can improve the hardware and system solutions that separate prefill and decode phases across GPUs. A separate serving simulation models request arrivals, queues, and cache transfer. For Llama-3.1-Instruct-70B to Llama-3.2-Instruct-1B, it predicts up to 33.86X faster requests and 27.5X lower energy use than using the larger model for both prefill and decode phases.

---


### 285. [ARMOR: Adaptive Curriculum Meta-Learning for Noise-Robust RAG Reasoning](https://arxiv.org/abs/2611.11771)

**<font color=#1a73e8>作者：</font>** Yan Wang, Yuxin Zhang, Shenyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems have demonstrated remarkable effectiveness in mitigating hallucinations by incorporating external knowledge. However, the retrieval process inevitably introduces noise, posing significant challenges to RAG robustness. Fundamentally, noise robustness is a composite competency encompassing noise identification, retrieval filtering, and robust reasoning. Unfortunately, existing methods often fail to capture this holistic nature, typically restricted to single-dimensional enhancements or hampered by noise-induced optimization interference. To address these limitations, we decompose RAG robustness into three sub-tasks: knowledge boundary perception, retrieval verification, and robust reasoning. Accordingly, we propose ARMOR, an Adaptive Curriculum Meta-Learning for Noise Robust RAG Reasoning. Inspired by the teaching process, ARMOR introduces an adaptive task scheduler as a teacher to curate training plans according to the absolute learning progress of RAG generators (Student). Distinct from GRPO, ARMOR utilizes inter-group advantage estimation during learning to effectively mitigate mode collapse caused by limited output spaces. Experiments on three complex reasoning datasets (2WikiMultiHopQA, MusiQue, and HotPotQA) indicate that ARMOR achieves synergistic improvements in retrieval noise robustness, significantly outperforming baselines in output quality.

---


### 286. [ChemInsight: A Comprehensive Benchmark for Evaluating and Diagnosing Chemistry Understanding and Reasoning in Large Language Models](https://arxiv.org/abs/2611.11794)

**<font color=#1a73e8>作者：</font>** Changyu Hu, Yiming Zou, Xin Tang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce ChemInsight, a benchmark designed to evaluate large language models (LLMs) on chemistry tasks that require multi-step reasoning and structured chemical understanding. We propose a two-dimensional scoring system (scope and depth) to assess both task coverage and reasoning completeness. ChemInsight consists of 203 challenging chemistry questions organized into 50 bundles, which support the two-dimensional scoring evaluation scheme.
We evaluate ten representative LLMs using ChemInsight and observe consistently low performance across models, with scope scores below 30% and depth scores below 11%, substantially lower than human expert performance. We then proceed to ask (1) What factor limits the advancement of current LLMs in chemistry? (2) To what extent are statistically driven language-model training methods effective at modeling chemistry symbolic language such as SMILES? And (3) Can LLM performance in chemistry be improved through intensive training on large, domain-specific corpora?

---


### 287. [HiddenPathQA: A Benchmark for Knowledge Graph Question Answering When Questions Hide Their Paths](https://arxiv.org/abs/2611.11802)

**<font color=#1a73e8>作者：</font>** Sumin Jo, Edward Choi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graph question answering (KGQA) systems are typically evaluated on questions whose surface tokens lexically expose the gold KG path. Users, however, may ask questions without knowing the underlying schema: "Which condition could Andrew have due to family history?" compresses a 4-hop chain "Andrew --[father]--> parent --[father]--> grandparent --[medical condition]--> disease --[subclass of]--> hereditary disorder" into a single phrase (family history) that names none of those relations. We identify this collapse of path-question alignment as a blind spot in existing KGQA evaluation. Three major LLM-KG paradigms, hop-by-hop exploration, plan-then-retrieve, and similarity-based retrieval, implicitly rely on such lexical cues, an assumption rarely tested in practice.
We make three contributions. (i) We introduce HiddenPathQA, a manually verified benchmark of 1,055 questions spanning 2-6 hops and multiple domains, constructed so that question wording does not reveal the gold path's relations. (ii) We propose Holistic Path Selection, which compares questions against candidate relation chains in the local subgraph as complete units, replacing irreversible per-hop relation scoring with globally informed chain-level reasoning. We develop two implementations, TieredHolistic and FlatHolistic. (iii) We conduct a pseudoword stress test that replaces entity names with meaningless placeholders to distinguish KG-grounded reasoning from entity-level memorization. Holistic Path Selection outperforms six strong KGQA baselines (ToG, PoG, FiDeLiS, R2-KG, KAPING, and KARPA) by 8.8-17.9 accuracy points across two LLM backbones and both original and pseudoword settings. Its advantage under pseudoword replacement shows that the gains cannot be explained by entity-level memorization alone.

---


### 288. [VeilTune: Secure Fine-Tuning of Private LoRA Adapters on Public Pretrained Language Models](https://arxiv.org/abs/2611.11817)

**<font color=#1a73e8>作者：</font>** Huiyu Xie, Tanping Zhou, Tao Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fine-tuning public pretrained language models with lightweight adapters such as LoRA has become the mainstream way to adapt them to downstream tasks. A service provider often trains its adapter on a data owner's samples, so two assets need protection: the data owner's samples and the provider's adapter. Existing secure fine-tuning protocols protect the samples but reveal to the data owner intermediate results of every training step, such as the hidden representations or logits of its inputs. We show that a single step suffices to copy the adapter: from the hidden representations of one mini-batch of 32 samples, the data owner fits an adapter that agrees with the provider's on 99.2% of test inputs, and logits alone yield about 94%. Protecting both assets therefore requires that no value that depends on the adapter be revealed throughout training. We present VeilTune, to the best of our knowledge the first protocol that fine-tunes a pretrained language model with backpropagation entirely in secure multi-party computation (MPC). VeilTune computes only what the loss depends on, replaces generic MPC operators with training-aware nonlinear operators that stay accurate on the values that training produces, and obliviously skips the steps corrupted by truncation failures. On four few-shot tasks with RoBERTa-large, VeilTune nearly matches plaintext training and is 5.3 points more accurate on average than SecP-Tuning, the state-of-the-art secure fine-tuning protocol. On SST-2, it achieves a 3.5x end-to-end speedup and a 3.6x reduction in communication over SecP-Tuning, and 26x and 17x over full fine-tuning in MPC.

---


### 289. [When to Trust Adaptation: Contextual Fusion for Transferable Vision-Language Prompting](https://arxiv.org/abs/2611.11824)

**<font color=#1a73e8>作者：</font>** Zhenyuan Chen, Wenshuo Tao, Zhuo Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a vision-language model encounters a new class or domain, how much should it trust its learned prompts? Because source adaptation can correct pretrained errors on some target images while disturbing valid predictions on others, we introduce Contextual Adaptive Fusion (CAF), which retains four prediction branches by pairing frozen and prompted visual and textual representations. To arbitrate when branches disagree on an image, CAF combines each branch's predictive confidence with how frequently the branches favor its proposed class across the unlabeled target collection, placing greater trust in predictions that are locally confident yet less dominated by collection-wide frequency bias. The fusion coefficients are learned once on source data and remain fixed at inference. Trained on ImageNet, CAF achieves 69.96% average accuracy across ten cross-dataset benchmarks (1.92 percentage points above ManiPT) and remains highly competitive across four ImageNet variants, setting a new best of 52.21% on ImageNet-S. In base-to-novel transfer across eleven datasets, CAF further reaches 79.77% novel-class accuracy and an 82.81% harmonic mean. Code is available at this https URL.

---


### 290. [Answer or Defer? Testing VLMs' Stated Confidence on Brain MRI](https://arxiv.org/abs/2611.11833)

**<font color=#1a73e8>作者：</font>** Amir Sabbaghziarani, Parsa Ghazvinian, Sepehr Salem 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) could support medical-image interpretation, but their use requires deciding which interpretations to accept and which images to refer to a clinician. We test whether thresholding stated confidence can retain useful coverage while limiting errors among accepted answers, and how this depends on the population. Eight open-weight VLMs, including two reasoning models, assess 3,888 brain MRI slices from post-treatment glioma patients (BraTS 2024) and healthy volunteers (IXI) for tumor or gross abnormality. BraTS labels are mask-derived; IXI slices are treated as negatives. On BraTS, no threshold selects a nonempty set with at most 5% empirical error for any model, even when chosen retrospectively. This also holds for four models evaluated on a large-lesion, distant-negative subset. At a 10% error budget, Gemma-4-12B retains 24.4% of slices and every other model at most 2.5%. To investigate this limited selection ability, we separate confidence differences between predicted answers from differences within each answer. For four models with available outcome-level summaries, pooled mean confidence differs more between answers than between correct and incorrect responses within each answer. A covariance decomposition explains how this pattern can produce opposite confidence-correctness associations across populations. At a 20% error budget, accepting every "tumor" answer covers more slices than any confidence threshold for two models. These findings caution against using unvalidated stated confidence as a standalone deferral signal and support population-specific validation before deployment. Code is available at this https URL.

---


### 291. [Improving Confidence Estimation in Language Models with Linear Representations of Ambiguity](https://arxiv.org/abs/2611.11838)

**<font color=#1a73e8>作者：</font>** Themistoklis Nikas, Nishant Subramani, Aaron Mueller  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As language models (LMs) are increasingly deployed in downstream applications, accurately estimating their likelihood of success on a given example is critical. However, confidence estimates from LMs are poor predictors of their likelihood of success. Accurate confidence estimation is linked in part to the detection of aleatoric uncertainty; we hypothesize that LMs possess representations of at least some aspects of this uncertainty in the form of representations of the inherent ambiguity of the input. Using difference-in-means on minimal pairs of ambiguous and unambiguous sentences, we derive ambiguity representations in LM activations, and find that steering with them selectively (albeit weakly) modulates LMs' judgments of the input's ambiguity. We then propose DART, a fine-tuning method that encourages updates to lie within the span of the ambiguity directions, and penalizes changes to the LM activations outside of this subspace. DART greatly improves calibration, encodes these improvements into the model parameters, and maintains model accuracy on multiple-choice and generative QA tasks.

---


### 292. [Correct Answers from Insufficient Histories: A Controlled Study of Agent Memory Evaluation](https://arxiv.org/abs/2611.11840)

**<font color=#1a73e8>作者：</font>** Quan Xue, Zerui Yang, Chaorui Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An answer can match the reference for a complete agent history even when the reader's visible history does not determine it. We study this distinction using executable device logs. Our protocol separates reference agreement, certified evidence sufficiency, and context-appropriate behavior. Insufficiency requires two legal histories yielding byte-identical visible contexts but different answers; public chronology and query cutoffs certify sufficient prefixes. On 80 confirmation histories, Qwen3-32B matches 87 hidden references among 203 insufficient raw-prefix instances, with only seven appropriate abstentions. A fixed-input DeepSeek-V4-Flash replication matches 85 and abstains on 21 of the same 203 instances. Each reader makes 1,600 requests. Compact CSV's estimated appropriateness effects remain inconclusive: +3.16 percentage points, clustered 95% interval [0.00,6.57], for Qwen and +2.46, [-1.84,6.94], for DeepSeek. A separate held-out judge study achieves 99.38% correctness but retains support errors and truncations; a deterministic baseline solves all constructed cases. These results support an evaluation diagnosis across two hosted reader configurations, not gains for a general memory system or natural-language evidence assessment.

---


### 293. [MOTIF: LLM-Defined Material Taxonomies for OOD Property Prediction via Invariant Feature Selection](https://arxiv.org/abs/2611.11846)

**<font color=#1a73e8>作者：</font>** Gwangseon Jang, Sieun Yun, Dong Ho Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution (OOD) generalization remains a central challenge in materials property prediction, where models must extrapolate to novel chemistries beyond the training distribution. While large language models (LLMs) have demonstrated strong scientific reasoning, their direct use for quantitative prediction remains limited. To address this, we systematically evaluate multiple roles for LLM assistance, finding that only taxonomy-based grouping consistently improves OOD generalization over a strong kNN+GBT baseline. Building on this, we here propose MOTIF, a framework that leverages LLMs not as predictors, but as generators of candidate taxonomies that partition materials into chemically meaningful environments. These taxonomies are evaluated via training-only pseudo-OOD validation, and only those that improve generalization are retained. Invariant feature selection is then applied within each accepted taxonomy, followed by gated aggregation across taxonomies. We evaluate on 2D halide perovskites, where bandgap prediction must generalize across distinct organic spacer families. On this benchmark, MOTIF reduces mean OOD MAE from 0.122 to 0.111 eV. Under a frozen dev/test protocol, the deployable configuration further improves errors from 0.123 to 0.117 eV (electronic bandgap) and from 0.181 to 0.173 eV (optical bandgap). Beyond this primary task, we validate transferability across additional materials datasets, including 3D perovskite solar cell efficiencies and Matbench benchmarks with structure-based splits. Across domains, MOTIF consistently improves robustness under distribution shift, outperforming expert-defined groupings, rule-based heuristics, and clustering baselines, while remaining competitive with strong classical selection methods. These results demonstrate that LLMs are most effective not as predictors, but as tools for discovering structure in data.

---


### 294. [Causal Signal Credit Assignment for Verilog Code Generation via Counterfactual Hardware Verification](https://arxiv.org/abs/2611.11848)

**<font color=#1a73e8>作者：</font>** Yali Du, Ming Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have improved Verilog generation, yet functional correctness remains difficult to optimize because simulation commonly provides a coarse module-level pass/fail outcome. Such feedback discards useful evidence from partially correct RTL modules and cannot determine whether a source statement is functionally responsible for an observed output behavior. We present a new method named Causal Signal Credit Assignment (CSCA), which is a counterfactual preference-optimization framework for Verilog generation. CSCA first performs continuous signal-level behavioral verification on sampled candidate modules. It then locates output-driving assignment spans and applies five interventions while holding the remaining module and testbench fixed. The resulting changes in signal-level errors are combined with behavioral agreement to form a continuous statement credit, which is mapped to response-token weights for strict weighted direct preference optimization. This enables CSCA to learn from locally supported statements without uniformly reinforcing an otherwise incorrect response. Built on Icarus Verilog and a CodeV-derived corpus, CSCA is evaluated on VerilogEval~2.0 and RTLLM~v2.0, including both code completion and specification-to-RTL tasks. With a Qwen2.5-Coder-7B-Instruct backbone, CSCA leads the evaluated 7B-scale models and remains comparable to the much larger GPT-5.4-mini on the reported Verilog-generation benchmarks.

---


### 295. [DeltaForge: A Post-hoc Mixture-of-Experts VLA for Multi-Domain Autonomous Driving](https://arxiv.org/abs/2611.11856)

**<font color=#1a73e8>作者：</font>** Bingzhang Wang, Mo Poorsartep, Yasaman Esfandiari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fleets of driving vision-language-action (VLA) models are developed one domain at a time: each operator finetunes a shared base model on private data, producing specialized experts that are costly to consolidate into a single model. Weight merging loses accuracy as heterogeneous domains accumulate, and dense mixture-of-experts routing is prohibitively expensive to combine them. We present DeltaForge, to our knowledge the first post-hoc mixture-of-experts VLA for driving, which consolidates N independently finetuned per-domain models into a single multi-domain model from their weights and a small proxy set alone. When different operators finetune the same base model, their weight updates end up sharing a lot of structure. We exploit this by decomposing all the updates together using singular value decomposition (SVD), splitting each one into a shared part (the same across all domains) and a tiny domain-specific part. The router then only needs to work with those tiny domain-specific pieces, not the full expert weights, which is what keeps the approach efficient. Then two cooperating clip-level blind routers, one over the VLM reasoning experts and one over the flow-matching dynamics experts, are trained from soft labels on the proxy dataset. Across six diverse domains spanning urban, off-road, and highway driving on cars, trucks, and all-terrain vehicles (ATVs), DeltaForge approaches the accuracy of the per-domain experts and surpasses every merging, routing, centralized, and federated baseline at close to single-model parameter and compute cost. Adding a new domain requires only projecting its weight update onto the shared basis with no end-to-end retraining needed. The resulting model also generalizes to domain combinations it was never explicitly trained on.

---


### 296. [Where Does Proposal Selection Fail? Diagnosing Frozen Vision-Language Queries over Detector Proposals](https://arxiv.org/abs/2611.11873)

**<font color=#1a73e8>作者：</font>** Bo Ma, Weiqi Yan, Jinsong Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In modular grounding a frozen detector proposes regions and a vision-language model (VLM) selects one, at lower cost than letting the VLM decode a box, but it is unclear where such systems fail. We hold perception fixed---every trained selector chooses among the same frozen proposals, which contain the referent for at least $99.8\%$ of RefCOCO/+/g queries---and vary the selection interface one factor at a time for two VLMs of one family (Qwen2.5-VL-7B, Qwen3-VL-8B). On RefCOCOg, what the selector reads matters more than how it is built: the VLM's image-conditioned query encodes the referent's location and beats a text-only query by $0.15$--$0.18$ with every head tested (by less for InternVL3-8B, whose vision encoder differs; one head tested). The remaining errors are rankings among a few top candidates; a cross-attention selector supervised with every valid box reaches the VLM's coordinate decoding on RefCOCOg, and with Qwen2.5-VL on RefCOCO/+ when also trained on their data. Beyond that distribution it does not: on Ref-L4's Objects365 images, mostly of categories outside training, every trained head falls to $0.19$--$0.28$ while Qwen decoding keeps about $0.8$ (InternVL3's drops too), neither a wider detector prompt nor a class-agnostic proposer closes the gap, and on public reasoning benchmarks Ref-Adv-s and RefBench-PRO full-budget heads trail decoding by $0.19$--$0.37$ although proposals cover most referents. A trained verifier reduces to an existence probe on the VLM's query state and does not beat the VLM's yes/no answer on public no-target benchmarks.

---


### 297. [When Answer Decodability Is Not a Decision: Separating Final-Answer and Imminent-Emission Signals in Chain-of-Thought](https://arxiv.org/abs/2611.11892)

**<font color=#1a73e8>作者：</font>** Hyojung Han, Jongmin Kim, Seung-Hun Jeon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Answer probes applied to chain-of-thought hidden states are often read as evidence that a language model has already decided its final response. This reading overlooks a competing signal, the candidate the model is about to mention. We introduce emission-controlled dual-target probing (ECDP), which fits the same low-rank reader family separately to the imminent mention and to the final answer at identical positions, with target-specific nulls and thresholds fixed before any fit. On correct DecisionDepth (DD) rollouts in which a distractor is mentioned before the final answer, Qwen3.5-4B decodes the next mention at .966 (null .234) but the final answer only at .221 (null .186), an emission gap of .696 [.648, .744]; Llama-3.1-8B gives .575 [.514, .632]. This pattern is not universal. In a pre-specified evaluation of Qwen3-8B with thinking enabled on held-out MMLU questions, using a full-prefix attention reader over every thinking position, both targets are decodable and the final answer is read far more strongly (mention-minus-answer lift -.398 [-.459, -.336] at layer 22 over 467 questions). Model, task, positions, and reader change together between these settings, and an attempted matched comparison on DD produced no valid statistics because the imminent-mention probe did not train reliably, so we do not identify what reverses the order. On DD, planted-signal controls show that the reader recovers an injected final-answer signal at one tenth of full dose. Answer-candidate decodability is therefore target-relative and protocol-dependent: a strong answer readout does not by itself establish when a model commits, and a probe that fails to train is not evidence that the information is absent. ECDP is a practical control for distinguishing imminent text emission from evidence of a settled decision.

---


### 298. [LEGION: Benchmarking Language Agents on Sparse-Signal Investigation Under Adversarial Noise](https://arxiv.org/abs/2611.11896)

**<font color=#1a73e8>作者：</font>** Samuel Joseph Amouyal, Ofek Glick, Yaniv Menasherov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous language-model agents are increasingly deployed on discovery-driven tasks where signal is sparse and most retrieved information is irrelevant. Current benchmarks fail to evaluate this regime due to dense signals, cooperative environments, and ground truth typically being only a few tool calls away. We introduce Legion, a benchmark framework coupling a stochastic enterprise-telemetry simulator (Legion-Sim) with a tiered library of 74 expertly-crafted adversarial scenarios (Legion-Bench) and an evaluation protocol that scores investigation efficiency alongside detection accuracy. Scenarios are injected into freshly simulated companies, allowing independent control over confounder density and event volume. We test five agent architectures on two simulated companies and find that while recall is high (0.82-0.88) precision lags behind (0.61--0.72). They fail to find all of the indicators of compromise of the attack or mistake genuine indicators with attack related ones, which is critical in the context of cybersecurity investigation. Failures are consistent across reasoning tiers and persist across confounder density and event volume. We release Legion, the scenario library, performance on common agent architectures, and pipeline for reproducibility and extension.

---


### 299. [ShopMind: A Mental World Model for Personalized and Realistic E-commerce User Simulation](https://arxiv.org/abs/2611.11897)

**<font color=#1a73e8>作者：</font>** Peixuan Hou, Bin Chen, Li He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are widely used in e-commerce user simulation, providing a foundation for understanding users and predicting human decisions. However, existing simulators still struggle to achieve both personalization and behavioral realism. Most methods predict the next action directly from interaction histories and the current context, without accounting for the evolving mental world that underlies user behavior. Theory of Mind suggests that behavior is driven by mental states, including beliefs, uncertainties, and intentions. Users may interpret the same information in distinct ways, leading to divergent behaviors, while an individual's mental state evolves through interaction and shapes subsequent actions. Ignoring this process prevents simulators from faithfully capturing individual differences and realistic behavior patterns, and undermines its effectiveness in downstream applications. To address this, we propose ShopMind, a Mental World Model for e-commerce user simulation that captures how consumers interpret shopping information and how their mental states evolve, better reflecting individual users and real-world behavior patterns. We further use behavior-mental state pairs synthesized by ShopMind to train a Mental State Reconstruction (MSR) model, which infers consumers' latent mental states from observable behavior. Experiments show that ShopMind improves personalization by 18.0% and behavioral realism by 19.6% over the strongest alternatives. Moreover, MSR improves performance on consumption value measurement and CTR prediction, showing the utility of ShopMind for understanding and predicting real user behavior.

---


### 300. [Spectral Unlearning: Transformer Structure-Preserving Updates for Language Models](https://arxiv.org/abs/2611.11902)

**<font color=#1a73e8>作者：</font>** Sung Il Choi, Junhao Cai, Dohun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning in large language models (LLMs) aims to remove specific learned knowledge, capabilities, or behaviors while preserving model utility. Existing methods have mostly focused on the design of unlearning objectives, while largely overlooking the intrinsic matrix structure of transformer weights. In particular, standard optimizers operate on independent scalar coordinates, thereby ignoring this matrix structure. We propose spectral unlearning, an update framework that combines standard unlearning objectives with matrix-structured optimization. We show that the spectral update corresponds to the steepest-descent direction for transformers composed of linear layers with normalized inputs and outputs. Our approach is applied on top of existing unlearning methods and evaluated across complementary axes of memorization, privacy, and utility, summarized via their harmonic mean. Spectral unlearning consistently outperforms a broad range of baselines and closes most of the gap to a retain-trained reference. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
