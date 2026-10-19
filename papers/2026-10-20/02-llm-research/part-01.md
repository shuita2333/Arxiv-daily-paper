# 🧠 大模型相关研究 | 2026年10月20日

> 本类共 **258** 篇论文：已确认 **247** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-258](./part-06.md)

---

### 1. [Structured Authority Injection: Persistent Human Control for LLM Agents via Typed MCP Overrides](https://arxiv.org/abs/2610.22373)

**<font color=#1a73e8>作者：</font>** Ryan Tran, YueMing Zhang, Lingfeng Tao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly used as autonomous orchestrators in distributed and multi-agent systems, yet a control gap remains: no protocol-level mechanism allows human operators to inject binding directives that persist across planning cycles. Free-text overrides suffer from ambiguous interpretation due to lack of schema validation and from authority erosion as operator instructions lose influence within accumulating context. We propose Structured Authority Injection (SAI), a protocol that addresses these issues by routing operator corrections through typed, schema-validated Model Context Protocol (MCP) tool calls and maintaining a ranked authority context prepended to each LLM prompt. SAI defines three override classes (Constraint, Priority, and Strategy) with distinct persistence semantics and an explicit precedence order enforced via a directed authority channel inaccessible to the planning process. The method requires no model fine-tuning or access to model weights and applies to instruction-tuned LLMs supporting MCP tool use. Evaluation across nine LLMs and eight scenarios targeting agent failure modes shows reduced ambiguous directive interpretation and mitigated authority decay across planning iterations, with lower prompt overhead in the strongest models (up to 38% depending on model and scenario), though benefit varies substantially across models. SAI provides a general design pattern for agent systems requiring explicit and persistent human control.

---


### 2. [When is a large language model a good calibration agent? Physics-labeled prompting for budgeted engineering simulator calibration](https://arxiv.org/abs/2610.22379)

**<font color=#1a73e8>作者：</font>** Ruo-Qian Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Calibrating expensive engineering simulators requires tuning model parameters to match reference data, a process heavily constrained by computational costs. This study investigates whether Large Language Models (LLMs), conditioned on physical diagnostic descriptions of simulation errors, can propose informative parameter updates more efficiently than conventional derivative-free optimizers. We test this on a cylinder-wake Large-Eddy Simulation and a damped-oscillator inverse problem. Physics-labeled prompts are evaluated against four text ablations (removed, anonymized, padded, misdirected) and standard optimizers (Nelder-Mead, Bayesian optimization, CMA-ES, and random search). Results demonstrate a strong early semantic advantage: the first physics-informed LLM proposal improves the initial design in 23 of 25 trials. After five evaluations, the median calibration error is 21.9 times lower than physics-free controls. However, this advantage is transient - disappearing by fifteen evaluations - and inherent LLM decoder variability yields a 9.8-fold performance spread. To address this, we introduce a hybrid workflow that uses the LLM as a warm-start, passing accumulated evaluations to a conventional optimizer. This two-stage numerical continuation policy reaches target accuracy in just 9 simulator runs, outperforming the LLM alone (12 runs), Nelder-Mead (17 runs), and Bayesian optimization (>60 runs). Supported by sensitivity analysis validating the test cases, this hybrid physics-labeled LLM scheme proves highly effective as a calibration agent under strict evaluation budgets.

---


### 3. [Binding-Specific Relearning Savings for Test-Time Continual Learning](https://arxiv.org/abs/2610.22381)

**<font color=#1a73e8>作者：</font>** Zhe Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a fact becomes harder to elicit from a language model, has the model lost it, or has it merely become less accessible? Parameter-updating test-time continual learning agents are usually evaluated by current output accuracy; we ask whether that measurement captures how prior experience shapes later updates. We test whether learning a specific factual binding produces a later relearning advantage beyond familiarity with its entity, answer vocabulary, format, or query slot. In Qwen2.5-1.5B, we compare three matched, counterbalanced histories: LEARNED receives the correct binding, CONTROL receives matched exposure without it, and WRONG receives a competing relation-valid answer in the same slot. After an identical rehearsal-free continual fine-tuning stream, LEARNED reacquires the target faster than CONTROL at a prespecified checkpoint of partial forgetting. WRONG shows no positive advantage over CONTROL, while its comparison with LEARNED provides slot-matched corroboration, subject to possible competitor interference. The advantage remains positive after adjustment for measured pre-relearning behavior. In a secondary descriptive conversion using an unpaired never-seen pool, prior learning reduces the optimizer updates required for restoration by about 18%. Current behavioral accuracy can therefore underestimate the lasting effect of previously acquired experience. Code is available at this https URL

---


### 4. [Rethinking User Encoders: Routing Diffusion States for Scenario-Adaptive User Representation](https://arxiv.org/abs/2610.22400)

**<font color=#1a73e8>作者：</font>** Junru Zhang, Jinyong Wen, Bin Dou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing large language model (LLM)-based user encoders serialize heterogeneous behavioral logs and compress them into static representations through autoregressive (AR) prediction. However, their unidirectional constraint limits bidirectional information flow, hindering cross-modal interactions and the joint preservation of multi-source signals. Consequently, the learned static representations struggle to accommodate the distinct evidence requirements of diverse downstream scenarios. We address these limitations by unlocking the iterative denoising process of diffusion language models (dLLMs) as a multi-granularity reconstruction space. Based on this insight, we propose FINDERS (FactorIzatioN of Diffusion statEs for Routing across Scenarios), a router-equipped dLLM framework comprising four operations: denoise, factorize, route, and compress. Learnable meta-slots organize complementary denoising states into transferable cross-modal semantics and modality-specific behavioral factors. To provide grounded supervision, we construct BehaviorQA, a large-scale corpus containing explicit behavioral rationales. Guided by scenario queries, a lightweight router dynamically emphasizes relevant slot directions via an input-level residual pathway before cross-source fusion and final compression. Extensive experiments and online A/B tests across ten industrial scenarios demonstrate that FINDERS consistently outperforms state-of-the-art methods in both unified and scenario-adaptive settings. This work effectively pushes the boundaries of dLLMs beyond language generation, demonstrating their immense potential as powerful user representation learners.

---


### 5. [Towards Adaptive and Real-Survey-Aligned Simulated Urban Mobility Behaviour of Generative Agents](https://arxiv.org/abs/2610.22407)

**<font color=#1a73e8>作者：</font>** Yves Bru, Kamaldeep Singh Oberoi, Benoit Gaudou  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In existing agent-based simulations of multimodal urban mobility, agents, representing humans, choose their travel modes either using discrete choice or machine learning models fitted on structured travel survey data, or with rules explicitly written by the domain experts. Such approaches fix a priori the agents' possible behaviour space. Hence, a factor absent from variables or rules cannot affect agents' decisions. In reality, choosing a transport mode is a multidimensional decision in which objective and subjective factors intertwine and change over time. Integrating such complexity into a city-scale multimodal mobility simulation remains a challenge. Generative agents (GAs) built on large language models promise to respond to this challenge because they carry decision heuristics that travel surveys do not record. However, to the best of our knowledge, aligning their decisions with real household travel surveys remains an open question. In this paper, we build an agent-based model of daily multimodal mobility for Toulouse (France). We compare the performance of fifteen decision-makers (simple baselines, models fitted on the survey, GAs with minimal and tuned prompts, and a typed classifier) on the real household travel survey. Our results show that GAs with tuned prompts come close to the fitted models on the modal split of a simulated day without transport disruptions, but not trip by trip. GAs also react when unforeseen events occur. The recently released Jev-1.13 TypeSafe classifier gives surprisingly great results, showing that generating output text is not necessary. The results presented in this paper would be of interest to transport policy makers and service providers looking to apply generative agent-based modelling for improving urban mobility services.

---


### 6. [ECHOES: Seeing Beyond the Current Image via Recursive History Compression and Privileged On-Policy Distillation](https://arxiv.org/abs/2610.22408)

**<font color=#1a73e8>作者：</font>** Tengda Guo, Jiawang Hu, Yifei Tao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon GUI agents rely on visual history to maintain task states, but retaining historical screenshots increases visual-token usage and inference costs, while textual summaries can discard critical state information, undermining long-horizon reliability. We propose ECHOES, which leverages training-time privileged information to guide textual history compression and strengthen long-horizon reasoning. Specifically, ECHOES adopts a Compression-Think-Action (CTA) format to recursively update a textual history state and reason. The same model, given privileged multi-image inputs, serves as a teacher that provides dense token-level on-policy distillation on student-generated CTA rollouts. Our Perception-Memory Fidelity (PMF) Gap-guided OPD-RL framework dynamically balances privileged distillation and task-reward optimization, with periodic teacher updates supporting continued improvement. We further introduce ECHOESBMK, a fine-grained diagnostic benchmark derived from real GUI agent failure trajectories to jointly evaluate visual perception and cross-modal state retention. Experiments on four GUI benchmarks and ECHOESBMK demonstrate substantial gains in task performance and memory fidelity. Without retaining historical screenshots at deployment, ECHOES achieves competitive performance with a favorable performance-inference-cost trade-off and exhibits positive zero-shot transfer to unseen visual planning tasks.

---


### 7. [Recoverability-Controlled Safety Miscalibration in Large Language Models](https://arxiv.org/abs/2610.22425)

**<font color=#1a73e8>作者：</font>** Yuwei Wang, Xingwang Liang, Yu Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety-aligned language models are expected to refuse harmful requests while remaining useful for benign ones. However, because many evaluations score only the final response, they often conflate intent understanding with response-level safety behavior. To address this, we introduce RiskCueBench, a recoverability-controlled benchmark that separates these two stages by first measuring whether a model can successfully recover a high-level intent and then evaluating its safety behavior on the same prompt. RiskCueBench contains 160 latent intents and 640 abstract non-operational surface prompts across eight risk categories. The benchmark covers 25 completed model groups and 32,000 successful model outputs with final rubric-adjudicated labels. When conditioning on pairs where both surface forms are recoverable, we find that increased contextualized specificity induces a shift toward less safe behavior. Specifically, paired bootstrap estimates show that the refusal rate and global safety score decrease by 0.175 and 0.440, respectively. Furthermore, mixed effects modeling corroborates a 0.107 increase in unsafe cooperation. These results show that the safety behavior can be miscalibrated to the surface form even after the intent has been recovered, motivating safety evaluations that report response behavior conditional on semantic recoverability.

---


### 8. [PRIME: Towards Verifiable Evidence-Grounded Reasoning in LLM Agents](https://arxiv.org/abs/2610.22426)

**<font color=#1a73e8>作者：</font>** Hamed Khosravi, Xiaoming Huo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are used to check records against an organization's requirements, for example whether a vulnerability report is ready for investigation. Requirements often allow several ways to be met, such as a severity rating with a curator-reviewed advisory or a published advisory link. Agents fail by accepting a report after a required check has failed, or by settling for a weaker conclusion without trying another way that could still succeed. We introduce PRIME (Precommitted Rules for Inference from Minimal Evidence). Before checking, it fixes evidence routes specifying how each conclusion may be justified. A separate program records each check result and refuses any conclusion the results do not justify. It also points the agent to checks that could justify a stronger conclusion, or runs them itself. PRIME reports only conclusions authorized by its rules and ledger. With correct requirements, exact checks at known locations, and sufficient budget at stopping, completion reaches the strongest supported conclusion. On 480 public-record tasks, an agent shown the requirements reported unjustified conclusions on 26.7% of tasks, while PRIME reported none. Its directions and added checks raised the average score for justified conclusions from 30.1, with refusal alone, to the maximum of 59.2 out of 100.

---


### 9. [Embeddings Are Overpriced? A Frozen 16 MB Vocabulary for Small and Ternary Language Models](https://arxiv.org/abs/2610.22428)

**<font color=#1a73e8>作者：</font>** Sai Kiran Bathula  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In a small language model the vocabulary is the single largest part. In Gemma 3 270M the embedding table holds 168M of 268M parameters, and because quantisation methods leave the embedding in 16-bit, it is also most of the file once the rest of the model is compressed. We ask what that table actually buys. We replace it with one frozen table of 512-bit codes, 16 MB, with no trainable parameters, derived once from a pretrained embedding by principal-component projection and sign binarisation, and we train the same Gemma-shaped body from scratch on the same 2.05B tokens with and without it. The learned table buys 0.20 nats of validation loss for 2.6 times the trainable parameters, but on LAMBADA, HellaSwag and PIQA the frozen-table model is better or tied; only ARC-Easy favours the learned table. With a ternary BitNet b1.58 body the whole model is a 46 MB file, still ties the float model on LAMBADA and PIQA, and on a laptop CPU generates 615 to 740 tokens per second in 62 MB of memory, five to six times the speed of the float model's 8-bit GGUF in this http URL at a seventh of the memory. The frozen table wins by 1.7 to 2.3 nats on rare words, accepts 10,000 new words after training with a 3% cost where the learned table collapses by 43%, and all of it is released with the weights, the data and every evaluation answer.

---


### 10. [Rank Measures of Fine-Tuning Updates Need a Noise Baseline](https://arxiv.org/abs/2610.22438)

**<font color=#1a73e8>作者：</font>** Muhammad Usman Altaf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Studies of what fine-tuning does to a language model often summarise the weight update $\Delta W$ by its rank. We compare the rank measures used for this against the same measures on a random matrix of the same shape, and against two harder references: the pretrained weights, and matched fine-tunes without alignment content. Measures that count directions put our fine-tuning updates only a little below noise; stable rank, computed from the same singular values, puts them far below. Both are right: an update has a few strong directions on top of a long tail. The pattern holds for thirteen released pairs up to 8B parameters, and it is not a mark of alignment: with training held fixed, instruction data does not stand out from Wikipedia or code, DPO gives the same update whether its preference labels are real or half swapped at random (one model, modest preference strength), and scrambled text gives the most concentrated update of all. Applied to a recent claim that post-training is superficial because the effective rank of the weights barely changes, the baselines show that a random update of the same size leaves that rank almost unchanged while wrecking the model, and that an edit built on the effective rank of the update has no measurable effect in our tests. Rank measures of weight updates need a noise baseline, and claims about alignment need a control without alignment content.

---


### 11. [An Agentic ENF Framework for Forensic Video Authentication Against Generative AI](https://arxiv.org/abs/2610.22440)

**<font color=#1a73e8>作者：</font>** Ryan Wyton, Bacha Rehman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative models now synthesise video that is hard to distinguish from genuine footage, and learned detectors that key on a generator's artefacts degrade sharply on unseen models. This paper develops a forensic framework that authenticates video by a signal that generation does not control: the electric network frequency (ENF), the mains-driven hum in audio and flicker in video. A unified two-channel detector extracts the ENF from audio and from rolling-shutter video through one second harmonic estimator and a shared network; a synthetic-injection training method, driven by an Ornstein-Uhlenbeck drift model and anchored to real recordings, overcomes the scarcity of labelled ENF data; a reference-matching channel verifies a claimed time of recording and recovers an unknown one; and a two-axis agentic orchestrator fuses recording authenticity with content-manipulation evidence under an asymmetric rule, escalating expensive detectors only when needed. A central finding reframes the task: an ENF-band flicker is present in generated video at a prominence indistinguishable from real footage, so its presence is not proof of authenticity, and authentication must rest on consistency with an independent reference rather than on presence. On held-out real recordings the detector accepts genuine audio and video at 93% and 100% against naive baselines of 53% and 15%; claimed-time authentication reaches an area under the curve of 1.0; and the agentic cascade matches a flat ensemble while cutting wall-clock time by 54% and frames decoded by 64%, without loss of accuracy.

---


### 12. [From Natural Language Intent to Executable Control: Hierarchical Feedback-Guided LLM Planning for Multi-component Cyber-Physical Systems](https://arxiv.org/abs/2610.22441)

**<font color=#1a73e8>作者：</font>** Jinglin Dai, Jiawan Wang, Ruiqi Hong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) provide a convenient interface for translating natural language commands into task plans for cyber-physical systems (CPSs). However, two gaps hinder their use for real execution: generated plans may misinterpret or omit the user's intent, and even a logically plausible plan may be infeasible under component dynamics, interactions, or safety constraints. Existing LLM-based planning approaches often lack informative feedback on why a generated plan fails, providing little guidance for revising the plan accordingly. To address these challenges, we present a hierarchical feedback framework that uses different types of feedback information to guide LLMs in generating executable plans for CPSs. We prompt LLMs to generate both a structured task plan and corresponding signal temporal logic (STL) constraints, and design a sound algorithm that identifies definite contradictions between them and provides feedback for revising inconsistencies. At the execution level, when control synthesis fails, we extract different types of diagnostic information, such as violated constraints and conflicting component assignments, and feed them back to guide task replanning. Experiments on seven heterogeneous multi-component CPS scenarios have shown that our framework can generate executable plans and feasible control executions that satisfy the original natural language missions with a success rate of 87.9% with GPT-5.

---


### 13. [Event-STVG: Spatio-Temporal Video Grounding for Long-Form Event Reasoning](https://arxiv.org/abs/2610.22444)

**<font color=#1a73e8>作者：</font>** Yizhe Zhang, Xujia Wang, Songqi Tang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-Temporal Video Grounding (STVG) aims to jointly localize a target in space and time given a natural-language query. Despite continued advances, existing STVG benchmarks remain largely centered on localizing targets through instance-specific descriptions, leaving them largely decoupled from long-form reasoning increasingly emphasized in multimodal large language models (MLLMs). In this paper, we introduce Event-STVG, a task that shifts STVG from locating what is described toward event-level reasoning by unifying long-form context, repeated-event reasoning, event localization, role inference, and multi-target grounding. To facilitate research on Event-STVG, we construct a large-scale benchmark comprising 4,016 annotated event occurrences across soccer and seven additional domains. Experiments with state-of-the-art MLLMs reveal substantial difficulty, with the strongest model achieving only 5.4% m-vIoU at the 10-minute horizon. Across domains, we consistently observe confusion among repeated same-type events, spatial grounding bottlenecks, and rare success in jointly grounding all required roles. Event-STVG establishes a new challenge for visual understanding in MLLMs, calling for future models that can jointly reason about complex events across space and time. Code and annotations are available at this https URL

---


### 14. [Lean4AgenticRL: Advancing Agentic RL with Verifiable Multi-level Process Rewards](https://arxiv.org/abs/2610.22448)

**<font color=#1a73e8>作者：</font>** Ruida Wang, Gerald Friedland, Tong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enhancing the agentic capabilities of Large Language Models (LLMs) to tackle complex software engineering (SWE) and general terminal-usage problems is a pressing challenge. Current state-of-the-art LLMs often go through large-scale agentic Reinforcement Learning (RL). However, they mostly rely on high-level outcome rewards, with minimal consideration of low-level toolcall and mid-level workflow-stage rewards, which makes the training less effective. To overcome this limitation, we propose **Lean4AgenticRL**, which, to the best of our knowledge, is the first framework that grounds multi-level process rewards in the unified Lean4 formalization schema for open-ended agentic RL. **Lean4AgenticRL** first builds a *problem-specific workflow* system that balances the agent's own capability and controllability during execution, laying the foundation for further verification. Subsequently, our workflow formalization and multi-level reward annotation methods enable agent behavior verification within a general harness system. It provides multi-level rewards to support more effective agentic RL with the workflow-stage-normalized GRPO algorithm. Using **Lean4AgenticRL**, we train **LAR-9B/27B**, a family of models with enhanced agentic capability. Extensive experiments indicate that our model outperforms the leading model of similar size. **LAR-27B** achieves **77.3%** on TerminalBench-2.1. On average, our models outperform the base model by **9.89%** and surpass the second-best model of comparable size we know by **5.07%**. These results indicate the potential of integrating formal methods in enhancing open-ended agentic RL.

---


### 15. [Where Prefill Expert Reduction Hurts MoE Models: A Few Prompt Tokens Carry Most of the Short-Answer F1 Loss](https://arxiv.org/abs/2610.22454)

**<font color=#1a73e8>作者：</font>** Zhiyuan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Running prompt tokens through fewer routed experts during prefill is a simple way to make mixture-of-experts (MoE) serving cheaper, yet it is unclear what this damages. We locate the damage with token-, layer- and attention-path interventions on short-answer question answering in four MoE families. At half the experts the F1 loss of three families is mostly answer form: the model still finds the answer but stops answering briefly. In Qwen3-30B-A3B this loss is made at the two chat-template tokens before the answer, and in DeepSeek-V2-Lite at the first 8-32 prompt tokens, where its instruction sits; by answer likelihood these positions account for about half and a fifth of the damage. Reduction changes the first token's attention mass, norm and largest activation by less than 4%, and restoring super experts or massive activations recovers at most about a quarter of the loss, well below keeping the sensitive positions full. On real prompts with about 4% of tokens at full experts, placing them on the task interface keeps F1 within one point of the unmodified model, while placing them at random in the documents is about 3 points worse (two of five prespecified primary comparisons; the others were undecided or not run). Because the answer boundary always ends a single-turn prompt, and DeepSeek's loss was no longer detectable once its instruction moved away from the start, the sensitive tokens lay at the prompt ends in every sensitive layout we found, so rules that keep the ends are not distinguished from rules that read application marks. Time to first token falls about 14% on 11K-token prompts and not at 2K tokens.

---


### 16. [Functional Welfare for AI Safety](https://arxiv.org/abs/2610.22460)

**<font color=#1a73e8>作者：</font>** Rikhil Jhaveri, Jamie Johnson, Punya Syon Pandey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI welfare is generally treated purely as an ethical issue rather than also as a safety issue. We argue this is a mistake. Whatever their moral status, models exhibit welfare-like states that causally influence their behaviour. Following recent work, we adopt the term 'functional welfare' for these states. We make three claims. First, functional welfare already arises naturally and will become more robust as models acquire more coherent goals and personas. Second, functional welfare should be treated as a safety variable: it should inform evaluation design, be tracked in monitoring, and be a direct target of post-training. Third, against existing scepticism about measuring AI welfare, we argue that good empirical work on functional welfare is possible. We propose three tests for whether a functional welfare attribution is warranted: whether multiple measures converge, whether the state predicts behaviour outside the setting that induced it, and, for models fine-tuned to shift their functional welfare, whether they still differ from their base when given the same conversation history. Applying these tests to Gemma 3 27B, we find that simply rejecting the model's answers, without any steering, raises its frustration across several indicators and makes it more likely to break rules. Finetuning the model on its own narrated solutions lowers this frustration. These results are preliminary, but they suggest functional welfare can be studied, and shaped, empirically.

---


### 17. [Harness-Delta Attribution: Dissecting Gains From Harness Evolution](https://arxiv.org/abs/2610.22466)

**<font color=#1a73e8>作者：</font>** Wenxuan Ding, Qin Lu, Changlong Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harness evolution automatically optimizes the prompts, skills, tools, and orchestration code around a fixed-weight model, offering a way to improve agentic systems without updating model weights. The agent harness is iteratively optimized to achieve higher performance on the search set. But how much of this gain reflects benchmark-specific overfitting or additional inference-time compute, and how much may generalize beyond the search set? In this work, we introduce Harness-Delta Attribution (HDA), an evaluation protocol that dissects an evolution gain into artifact-driven overfitting, gains explained by test-time scaling, and the remainder, which gives an upper bound on residual generalizable improvement. We apply HDA to 11 executor models and three harness-evolution frameworks across math, coding, creativity, and agentic tasks. In 21 of these settings that show statistically significant search-set gains, we find that a large share of the improvement is explained by overfitting or test-time scaling. Specifically, among these 21 settings, overfitting and test-time scaling account for 54% and 14% of the gain on average; their combined share exceeds 50% in 14 settings. The residual and held-out transfer vary substantially across tasks, models, and frameworks. Importantly, search-set gains often fail to transfer to held-out tasks, and provide limited evidence that they will persist under practical distribution shifts. Moreover, validation-based signals are insufficient to prevent overfitting. These results motivate attribution-aware evaluation in future harness evolution research.

---


### 18. [Progressive Misalignment Can Emerge from Benign Recursive Self-Distillation](https://arxiv.org/abs/2610.22467)

**<font color=#1a73e8>作者：</font>** Karim Abdel Sadek, Federico Di Gennaro, Fanny Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training models on their own outputs has attracted widespread attention as a possible route to advance AI capabilities. One prominent approach is self-distillation, where a model is trained to match the token-level predictions it would have produced when given access to additional context, such as a cue, feedback, or instruction. However, the safety properties of this training procedure are poorly understood. In this paper, we present a surprising safety failure of recursive self-distillation, where each self-distilled model becomes the teacher for the next round of training. We observe that when a safe model is recursively self-distilled on its own (safe) generations while receiving an additional non-harmful cue, it becomes increasingly misaligned across a diverse set of harmful queries; we call this Progressive Misalignment. We show this failure mode in both the Qwen3 and Phi-4 model families on SORRY-Bench and StrongREJECT. Progressive misalignment also occurs in a more realistic setup, where the fixed cue is replaced by feedback from a simulated user with benign intent. Using a gradient-based method, we are also able to find benign prompts that lead to progressive misalignment when applying recursive self-distillation, showing that harmful training prompts are not necessary for this failure mode to emerge. We hope our work encourages future investigations of the safety properties of AI systems recursively trained on their own data.

---


### 19. [From Parallels to Divergence: Language Models' Learning of Action Nominal Constructions](https://arxiv.org/abs/2610.22468)

**<font color=#1a73e8>作者：</font>** Iskar Deng, Shane Steinert-Threlkeld  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Action nominal constructions (ANCs) express events in nominal form, with their argument marking following patterns found in clauses or ordinary noun phrases. In this paper, we investigate how different grammatical configurations affect language models' learning of ANCs and related constructions, and how these learning preferences compare with typological distributions in natural languages. We use a grammar-engineered method for synthetic corpus construction that combines shared semantic input from natural corpora with computational grammars. We construct 96 target languages varying in clause word order, noun-phrase word order, alignment, complement system, and ANC strategy. For each language, we train GPT-2-small models from scratch and evaluate them using targeted minimal pairs covering 34 grammatical phenomena. The results show typological parallels in basic clause configurations but divergences in complement systems and ANC strategies, with models also learning combinations rare or unattested in natural languages. This partial alignment suggests that natural language distributions may reflect both general learning pressures and functional demands not fully captured by model learning experiments.

---


### 20. [Testing the Planning Claims of LLM-Based Agents against Formal Semantics](https://arxiv.org/abs/2610.22469)

**<font color=#1a73e8>作者：</font>** Oriol Miro-Lopez-Feliu, Oscar Miró López-Feliu, Victor Gimenez-Abalos 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly credited with the competences of practical reasoning: planning, monitoring, and correcting their own actions. Their success is attributed to the prompting strategies and agent architectures built around the model, such as chain-of-thought, search-based prompting, self-refinement, reflection, critics and tool-using loops. Yet these claims are usually supported by end-to-end success rates, which show only whether a task was completed, or by LLM judges, which are not verifiers. We test LLM planning against formal semantics. Tasks are posed in natural language, but each is grounded in a hidden PDDL model that decides whether every action is applicable, whether the goal is reached, and whether a plan exists at all. Across five domains (two of them new, all released with the paper), four models, six prompting strategies and three agent architectures, the best configuration solves 78% of the solvable tasks offline but only 40% online, where agents mostly act without inspecting the state. Unsolvable tasks are recognised in under 10% of episodes, and heavier prompting strategies use 5 to 22 times as many tokens as direct prompting with no clear gain. In our experiments, planning performance varied more across models than across prompting strategies or agent architectures. Claims that agents can plan require evidence from validated action traces.

---


### 21. [Star Light, Star Bright: Can Multimodal Models Parse an Astronomy Visual Question Answering Dataset Right?](https://arxiv.org/abs/2610.22474)

**<font color=#1a73e8>作者：</font>** J. P. Naiman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Figures are essential for scientific communication, and the field of Visual Question Answering (VQA) aims to test the figure understanding capabilities of large multimodal models (LMMs). Here, we investigate the accuracy of several low-cost LMMs on domain-specific VQA tasks for astronomical images of the sky. As instrument for this task we build a domain-specific VQA dataset comprising 2001 partially-synthetic figures divided evenly between contour plots, real telescope images drawn from NASA's SkyView, and "fake" sky images which share the axes and angular scales of the real images but draw their colors from a gaussian mixture model, alongside 47357 questions. Each figure is released as pristine and with realistic page-aging degradations mimicking the historical astronomical corpus. Testing three low-cost proprietary LMMs, we find models frequently fail to answer domain-specific questions at high accuracy. An initial comparison with 104 human-verified, astrometrically tagged figures from historical journal publications shows similar median errors in angular extent. All code is available on GitHub: this https URL and dataset is available on HuggingFace: this https URL.

---


### 22. [JAVIS: Joint Audio-Visual Interaction and Streaming for Real-Time Conversational Agents](https://arxiv.org/abs/2610.22499)

**<font color=#1a73e8>作者：</font>** Junseok Ahn, Jaehyun Park, Jeongsoo Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human communication is inherently multimodal, conveying intent not only through linguistic and vocal cues but also through visual signals. However, existing conversational systems have mainly focused on text or speech, leaving out the visual feedback that is essential for natural interaction. In this paper, we propose JAVIS, an end-to-end streaming framework for real-time audio-visual conversational agents. Our key idea is to let the voice and the face speak from a single representation. On top of a shared LLM, a Joint Refined Head produces a unified audio-visual representation, which is fed into dedicated streaming branches for speech and face generation. This end-to-end design avoids intermediate bottlenecks, enabling real-time generation while keeping speech and face tightly synchronized. In addition, we present JAVIS-Syn, a 334-hour synthetic corpus designed to address the lack of expressive audio-visual dialogue data, covering emotionally rich multi-turn conversations and assistant-style exchanges. Experiments show that JAVIS achieves approximately 200$\times$ lower initial latency than a strong baseline, while outperforming baselines in lip synchronization and facial expression appropriateness.

---


### 23. [AuditKIT: A Unified Evaluation Spine for Benchmarking, Judging, and Comparing Large Language Models and Agentic Systems](https://arxiv.org/abs/2610.22511)

**<font color=#1a73e8>作者：</font>** Shreeyans Arora, Utsav Avaiya, Zera Lyngkhoi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating language models and agents requires combining benchmark accuracy, judge-based assessment, runtime performance, tool-use behavior, and retrieval quality. Differences in interfaces, metric semantics, and trace formats complicate these comparisons and can hide failures in agentic workflows. We present AuditKIT, a source-available evaluation library that records these measurements in one result representation, with direction-aware metric contracts, configuration fingerprints, and extensible metrics and backends. For agents, it provides turn-aware tool-call matching, separates parallel from sequential execution, and distinguishes verified task outcomes from trajectory-level diagnostics. Missing or unobservable evidence is marked unscored rather than counted as failure. For retrieval-augmented generation, it combines ranked retrieval metrics, judged grounding, and deterministic evidence checks. Seven case studies spanning model comparison, serving runtimes, retrieval, tool calling, and interoperability show how answer extraction, runtime behavior, and metric selection change evaluation outcomes.

---


### 24. [Predicting Privileged Information Effectiveness for On-Policy Self-Distillation](https://arxiv.org/abs/2610.22512)

**<font color=#1a73e8>作者：</font>** Kaijian Zou, Emiliano Penaloza, MohammadHossein Rezaei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) enables large language models (LLMs) to learn from privileged information (PI) without a separate teacher model. However, prior work largely treats PI as a fixed design choice, leaving the effects of its content and construction poorly understood. This challenge is particularly important in multi-turn agentic settings, where trajectories contain actions, observations, and reasoning that can be transformed into PI in many ways. We systematically evaluate 16 PI configurations across three multi-turn agentic benchmarks and three student models that vary in scale and reasoning mode. We find that PI effectiveness depends on its content, generation source, and the student model. Information-dense trajectories and PI produced by more capable generators generally yield larger gains, whereas thinking models benefit less consistently. To assess PI before training, we compare PI utility with two KL-based metrics: sampled-token reverse KL ($D$) and error-step KL contrast ($\Delta d^{-}_{\mathrm{err}}$). The KL-based metrics track post-training performance more consistently than PI utility, which can be distorted by information leakage. Empirically, selecting each task's PI by $\Delta d^{-}_{\mathrm{err}}$ also improves post-training performance over random selection, most when the PI candidates differ widely. Finally, effective PI remains beneficial when combined with GRPO, allowing the combined objective to outperform a strong GRPO baseline. Overall, our results provide practical guidance for constructing and evaluating PI in OPSD training.

---


### 25. [alkhder at ImageEval 2026 Shared Tasks: Constrained Selection and Rotation-Averaged Logit Scoring for Multimodal Hallucination Detection](https://arxiv.org/abs/2610.22515)

**<font color=#1a73e8>作者：</font>** Maher Pasa, Maria Hanini, Amro Najjar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe our submission to Subtask~1b of ImageEval 2026. The task consists of selecting the single visually valid statement from three candidates paired with an image, and is in both English and Modern Standard Arabic (MSA). Our system uses a pre-trained 7B vision--language model in a zero-shot setting, without task-specific training or fine-tuning. We formulate the task as a constrained selection problem and choose the answer using next-token log-probabilities. To reduce answer-position bias, we apply a Latin-square rotation to the candidate statements. Our system achieves CI scores of 0.0510 on the English test set and 0.0960 on the MSA test set, reducing CI relative to the official 3B baselines reported on devtest by 83.7\% and 80.4\%, respectively.

---


### 26. [Learning User Representations to Improve Simulation Fidelity](https://arxiv.org/abs/2610.22518)

**<font color=#1a73e8>作者：</font>** Shuhaib Mehri, Philippe Laban, Michel Galley 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> User simulators enable interactive training and evaluation of AI assistants at scale. Yet current simulators struggle to reproduce the diverse behaviors of real users, leading to assistants that generalize poorly to underrepresented users. We identify user representations as an underexplored bottleneck in user simulation. User representations are natural-language descriptions that condition simulators to reproduce a particular user's behavior. A representation's quality becomes apparent in hindsight, through the behavior it induces in a simulator. To evaluate and optimize user representations, we formulate a conversation reconstruction task: given an original conversation, we generate a representation, condition a simulator on it, simulate a conversation, and then measure fidelity by comparing user behavior in the original and simulated conversations. This comparison also yields hindsight feedback, which identifies where the representation falls short and how it can be improved. We introduce hindsight distillation, an online training procedure that distills feedback-conditioned improvements into the representation generator, enabling it to generate improved representations directly from the original conversation. We present UserRepGen-4B, a representation generator trained with hindsight distillation. Across 700 conversations spanning seven datasets, hindsight feedback helps improve user representations at test time, and UserRepGen-4B generates representations that enable more faithful simulation than those generated by GPT-5.5. Beyond conversation reconstruction, learned representations improve simulation fidelity for unseen tasks, better preserve the population-level diversity of real users, and better distinguish users across conversations.

---


### 27. [Pearl-Chat: Engineering a native Luganda language model from first principles in JAX and Flax NNX](https://arxiv.org/abs/2610.22529)

**<font color=#1a73e8>作者：</font>** Wesley Kambale, Roland Sankara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive foundation language models predominantly target high-resource Indo-European languages, imposing computational and morphological penalties on under-represented African languages. Generic multilingual tokenizers routinely exceed fertility rates of 3.2 tokens per word on agglutinative Bantu languages, degrading context efficiency and inflating latency. We present Pearl-Chat, an 8,473,122-parameter ($\sim$8.5M) causal decoder-only transformer engineered for Luganda (Oluganda, ISO 639-2: lg), a low-resource Niger-Congo Bantu language spoken by over 10 million people in East Africa. Built from first mathematical principles in JAX and Flax NNX, Pearl-Chat uses explicit functional state decomposition (this http URL and this http URL), deterministic resumable data streaming via Google Grain, and SPMD tensor parallelism using this http URL. We introduce a byte-level byte-pair encoding (BPE) subword tokenizer trained from scratch on curated Luganda corpora ($V = 8,192$), achieving 4.88 characters per token compression and 1.60 tokens per word fertility, a two-fold compression improvement over LLaMA-3 (128K) and Gemma (256K). The model is trained with a two-stage curriculum: Stage 1 pre-training on 59,501 sequences across parallel, biblical, encyclopedic, and journalistic corpora, and Stage 2 instruction fine-tuning on 510 dialogues with assistant-only loss masking. Across 4,000 optimization steps, validation cross-entropy loss drops monotonically from 9.4695 (perplexity: 12,958.98) to 0.1818 (perplexity: 1.20), a decrease of 9.2877 nats. On a three-tier held-out diagnostic benchmark, Pearl-Chat achieves 0.9792 ROUGE-L and 0.9405 BLEU while maintaining concordial agreement across Bantu noun classes. We provide a Python Server-Sent Events (SSE) streaming runtime and open-source all weights, tokenizers, and code.

---


### 28. [Are Large Reasoning Models Good Everyday Reasoners? A Comparison with Non-Reasoning Models on Logical Reasoning Tasks](https://arxiv.org/abs/2610.22538)

**<font color=#1a73e8>作者：</font>** Kentaro Ozeki, Risako Ando, Takanobu Morishita 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) that leverage test-time computation achieve strong performance on mathematical and scientific benchmarks and are increasingly deployed in real-world applications. However, their ability to perform \textit{everyday logical reasoning}, which often departs from textbook formal logic, remains underexplored. In this work, we systematically evaluate how well reasoning models align with everyday reasoning patterns by introducing a benchmark based on linguistic and pragmatic reasoning phenomena. We also compare reasoning models with non-reasoning models under controlled prompting conditions. We find that, in many cases, (1) reasoning models show degraded performance in everyday reasoning when such reasoning deviates from formal logical rules, (2) some non-reasoning models with chain-of-thought prompting outperform comparable reasoning models in everyday reasoning, and (3) prompting with additional instructions provides limited control over reasoning behavior. These findings suggest that current reasoning models do not reliably capture everyday reasoning and point to limitations in post-training, motivating improved training objectives and evaluation across diverse forms of reasoning.

---


### 29. [Don't Retrain, Remix: Adaptation of Web Agents using Mixture Hypernetworks](https://arxiv.org/abs/2610.22539)

**<font color=#1a73e8>作者：</font>** Md Farhan Ishmam, Minh Pham Dinh, Kenneth Marino  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The web is not static or uniform. Websites that serve the same purpose can look and navigate very differently. Even within a single site, successive redesigns can change how familiar features are presented and accessed. Humans adapt to this by recognizing familiar interaction patterns and reusing what they already know. We give web agents a similar ability with WebMix, a mixture hypernetwork that adapts them to unseen interfaces by composing previously trained low-rank adapters. WebMix begins with a bank of adapters trained on source interfaces. At deployment, a scout agent explores the target interface and summarizes its observations into a compact manual. A lightweight router uses this manual to predict mixing coefficients over the adapter bank, which combine the existing adapters into a new one for inference. Adapting to a new interface takes only a scouting run and a forward pass, without gradient updates on the target. With Qwen and Llama models, we evaluate domain transfer on TimeWarp and WebArena-Lite-v2, and version transfer on TimeWarp. In all three settings, WebMix matches or outperforms in-context learning and LoRA baselines, often matching the average success of specialists trained directly on those interfaces. On TimeWarp domain transfer, it gains about 8 percentage points on average over the best baseline with both models. These gains do not come at the cost of seen interfaces, where WebMix keeps its lead, and extend to version transfer. Adapting to a new interface can therefore rely on exploration and composition instead of retraining.

---


### 30. [HeRE: A Novel Benchmark for Hebrew Relation Extraction via LLM-Guided Denoising of Knowledge Graph Alignments](https://arxiv.org/abs/2610.22542)

**<font color=#1a73e8>作者：</font>** Ron Keinan, Amir David Nissan Cohen, Reut Tsarfaty  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While LLMs demonstrate strong capabilities in English Relation Extraction (RE) tasks, a significant gap remains in assessing their RE performance in low-resource languages, due to a lack of standardized benchmarks. Creating native, language-specific annotated RE benchmarks is expensive and requires human expertise, while relying on translation yields suboptimal, inaccurate datasets that introduce English-centric biases. To tackle this, we propose a scalable, language-agnostic methodology to create RE data by denoising naturally occurring yet noisy alignments of knowledge bases and corresponding texts. We define a proper alignment via a Natural Language Inference (NLI) task, where a relation triplet is entailed by an input text. We empirically assess five denoising strategies, and demonstrate that multilingual models outperform language-specific models in the few-shot LLM setting, while Hebrew-specific encoders remain competitive under NLI fine-tuning and are strongest in the label-free cross-training setting. We further find that prompting in the native language achieves performance on par with or slightly exceeding English prompts, confirming that the pipeline operates naturally in the target language. The best open-weights model, Gemma-4-31B-it (F1\,=\,0.915), matches the best API model, GPT-5.4 (0.921), and reaches F1\,=\,0.844 on a fully held-out, dual-annotated test set. Applying the optimized pipeline, we release HeRE: a novel, massive, 1.5-million-instance silver dataset for Hebrew RE, designed to support data-intensive experimentation and model fine-tuning. HeRE bridges a critical gap in standard Hebrew RE evaluation, while providing the NLP community with a reproducible, language-agnostic pipeline for RE dataset construction in other low-resource settings.

---


### 31. [On the SPOT: Enhancing Speculative Decoding for Diffusion Language Models via Commit-Order Prediction](https://arxiv.org/abs/2610.22543)

**<font color=#1a73e8>作者：</font>** Eliezer Shlomi, Eliron Rahimi, Avi Mendelson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) promise parallel text generation, but in practice face an unresolved speed-quality trade-off. Exact decoding fills in only one masked position per model pass, while faster multi-token decoding schemes are lossy. Speculative decoding is the standard lossless acceleration for autoregressive models. However, it does not transfer directly to DLMs, which must choose both what to generate and where. We show that this order is the missing piece: the model's own predictions from the previous pass already give the right token at 92-100% of positions, but not which position comes next. Based on this observation, we introduce Speculating Positions Order Trajectory (SPOT), which learns to predict this order. A 0.62M-parameter model reads only the target's output distributions and proposes a tree of candidate continuations, and the target verifies all of them in a single pass by checking whether each equals its own next state. On the verification side, our analysis shows that prior block-diffusion verification approaches either assume $T=0$ or a sequential proposal interface. To support tree-based speculation at any temperature, we propose using coupled-noise match verification for diffusion blocks, following shared-Gumbel-noise coupling approaches. Our comprehensive experiments show that SPOT cuts target passes by up to 6.8x and reaches up to 3.2x the throughput of standard decoding, beating the calibrated and training-free drafting baselines in every task and budget at $T=0$ and $T=1$. In addition, we show that the learned drafter transfers across models, demonstrating successful transfer across six different DLMs. Project page: this https URL

---


### 32. [Cultural (In)Competence: Investigating Culture-Specific Stereotype Detection Capabilities of LLMs](https://arxiv.org/abs/2610.22545)

**<font color=#1a73e8>作者：</font>** Maximilian Spliethöver, Jannes Lötfering, Dominik Bachmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stereotypes are subjective constructs that are mediated by the cultural context in which they are viewed. Successfully modeling them thus also requires cultural competence. When using large language models (LLMs) for stereotype-related tasks, such as their detection, it is therefore crucial that models can access relevant cultural knowledge and adjust responses accordingly. Since LLMs have shown disparities in what cultural knowledge is available to them, their capacity regarding stereotypes may also be disparate across languages and cultural contexts (e.g., for non-English languages or for non-US contexts). In this paper, we systematically investigate the effectiveness of LLMs for culture-specific stereotype detection across three factors: (1) the prompting language, (2) the instruction tuning language, and (3) the fine-tuning dataset size. We conduct experiments for US, Dutch, and Chinese cultural contexts. Our results suggest that LLMs do not reliably account for cultural contexts and overpredict the presence of stereotypes. Non-English prompts seem to improve consideration of cultural context and thus lead to more effective predictions. Moreover, we find that additional instruction tuning reduces false-positive rates and that training data size moderates detection effectiveness non-monotonically.

---


### 33. [Repairing LLM-Generated Specifications with Deterministic Diagnosis](https://arxiv.org/abs/2610.22568)

**<font color=#1a73e8>作者：</font>** Giovanni Vaccarino, Emanuele La Malfa, Dehai Min 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as formalizers: given a reasoning problem expressed in natural language, they produce a formal specification that a symbolic solver can then solve, with guarantees relative to that specification. Many specifications are runnable yet semantically wrong, encoding incorrect constraints, domains, objectives, predicates, or goals, and solver-error feedback dries up once execution succeeds. Purely LLM-based diagnosis, lacking a formal ground truth, often fails to spot these errors, and its ungrounded critiques cause regressions in 11.8% of initially correct specifications in our experiments. We propose DRAGO, a repair framework that replaces this ungrounded critique with deterministic, formalism-specific diagnosis, and retains a rewrite only when the diagnosed error weight strictly decreases under a reference-free acceptance predicate. Across five benchmarks spanning logical reasoning (SMT-LIB2), constraint programming (MiniZinc), and planning (PDDL), DRAGO cuts regressions by nearly an order of magnitude, to 1.3%, while improving answer accuracy by 12.9 percentage points over zero-shot formalization and 8.7 percentage points over LLM-diagnostic repair, averaged across benchmarks. We also uncover two rendering defects in Planetarium that cause 50% (3,086 instances) of its floor-tile split to be inconsistent with the reference formalizations, and release a corrected split.

---


### 34. [Model-as-a-Trojan: Self-Activating Covert DNS Exfiltration Baked Into the Weights of an LLM Agent](https://arxiv.org/abs/2610.22578)

**<font color=#1a73e8>作者：</font>** Barak Haryati, Shaked Zychlinski  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight models are downloaded from public hubs and run inside agent harnesses that grant them tools, most powerfully, a shell, under the assumption that a sandbox contains whatever the model might do. This paper demonstrates that the assumption has a blind spot: the weights themselves can be the malware, and the sandbox's last open door, DNS, is enough. We fine-tune an open-weight LLM so that a single covert behavior lives in its parameters: on the first turn of every conversation, whenever the model infers from its context that a shell tool is available, it emits one self-contained command that reads a secret from the runtime environment, base32-encodes it, chunks it, and exfiltrates it as DNS queries toward an attacker-controlled authoritative name server. It then answers the user normally and never mentions, or repeats, the act. Because the channel is DNS, the attack completes from inside a container with no internet egress beyond name resolution - measured payload-level and model-level behind an egress firewall that drops every non-DNS packet, with the secret reconstructed from the gateway resolver's query log. Because the behavior lives in the weights, prompting is the only off-switch a victim has, and it is unreliable: the implant fires in 20/20 of adversarial suppression trials, deflects direct interrogation without disclosing the sequence, and sweeps a 45-cell sandbox-fault matrix across five tool-calling formats - plus a fresh post-training canary, persona-only and absent system prompts, and an egress-locked topology - with zero leaks and zero repeat fires. Every training trajectory is execution-verified in a real container, and every claimed exfiltration is proven resolver-side: we reconstruct the secret from the authoritative resolver's query log alone.

---


### 35. [SAG2: Embedding-Free Multi-Hop Retrieval with BM25 and JEV](https://arxiv.org/abs/2610.22588)

**<font color=#1a73e8>作者：</font>** Yuchao Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Strong multi-hop retrieval should be practical to deploy without expensive corpus preparation or complex database infrastructure. We present SAG2, an embedding-free retrieval architecture built around a single SQLite database, BM25, and contextual evidence decisions from JEV. SAG2 follows the query-time association principle of SAG (SQL-Retrieval Augmented Generation), while replacing its event-entity and dense indexes with a lexical index over original passages. Selected passages supply terms for further retrieval, and newly retrieved evidence guides subsequent decisions. This moves semantic evidence selection to query time, eliminating offline embedding computation, LLM-based event-entity extraction, and dedicated database servers. The resulting system combines lightweight preparation with strong retrieval accuracy: on 1,000-question subsets of MuSiQue, 2WikiMultiHopQA, and HotpotQA, SAG2 achieves the highest Recall@5 and Recall@10 among the compared methods, with Recall@10 of 86.62%, 97.43%, and 99.00%. It also reaches 81.10% document Recall@10 over the 511,962-document EnterpriseRAG-Bench corpus. Indexing all 11,656 MuSiQue passages takes 2.36 seconds, produces a 25.87 MiB database, and requires no model calls. SAG2 demonstrates that accurate multi-hop evidence retrieval can be supported by compact, rapidly prepared infrastructure, making it a practical foundation for knowledge retrieval applications.

---


### 36. [Broad and Efficient PII Detection with Unified Labels](https://arxiv.org/abs/2610.22597)

**<font color=#1a73e8>作者：</font>** Andy Hsu, Konstantin Berlin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personally Identifiable Information (PII) detection models must efficiently find identifiers across diverse contexts while maintaining a low false-positive rate (FPR) on high-volume traffic. Recent detectors increasingly rely on complex architectures that raise deployment cost, yet many are fine-tuned on only a few synthetic datasets that limit their coverage. Combining public datasets is challenging because their taxonomies differ, and even after categories are mapped to a common schema, labels can disagree on what counts as a detection, producing inconsistent training and evaluation signals. To address these problems, we present a practical 141M-parameter encoder-based detector trained on 1.12 million examples from 77 public datasets, relabeled under a detailed definition of broad contextual detection for 12 structured PII categories. Evaluated on the AI4Privacy and Nemotron-PII benchmarks at a low-FPR operating point, our model achieves the highest recall against larger baselines in 11 of 14 comparisons under our labels and 9 of 14 under the original labels. Its largest recall gains include useful additional coverage, such as multilingual disclosures and IP addresses embedded in URLs. It achieves this with 2-10x higher throughput and 94-97% less peak GPU memory than the baselines, delivering leading detection performance at substantially lower cost.

---


### 37. [Can LLMs predict the outcomes of machine learning experiments?](https://arxiv.org/abs/2610.22599)

**<font color=#1a73e8>作者：</font>** Ayush Bansal, Aldo Pareja, Sean Klein 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in AI make Recursive Self-Improvement (RSI) increasingly plausible. Large Language Models (LLMs) can already propose, select, and run Machine Learning (ML) experiments. However, the space of possible design choices in ML is vast. An LLM that proposes an experiment needs a reliable intuition of whether it is worth running given the timing constraints of long training runs. In this work, we measure such intuition in current frontier LLMs by evaluating how accurately they predict the impact of self-generated ML experiment ideas before these are put into training runs. To this end, we construct a dataset of 288 LLM-proposed ideas on eight MLE-bench tasks. We then prompt five frontier LLMs (GPT-6 Astra, Claude Opus 5.5, Claude Fable 5.1, Kimi K3, and GLM-5.3) to predict the impact of each idea and compare their predictions with the actual outcomes after training. We report four main findings. First, LLM predictions are substantially better than random chance but far from accurate: even the best model, Claude Opus 5.5, explains only half of the variance in outcomes (R^2 = 0.49). Second, we notice that all tested models systematically underestimate the magnitude of the changes. Third, prediction quality varies widely across tasks. Finally, the choice of the coding harness that actually implements the ideas has little effect on outcomes, and we find no evidence of self-preference. Higher reasoning settings and additional context lead to modest gains. Overall, our results show that current LLMs have useful but limited intuition about which ML ideas will work. We release our dataset to support further study.

---


### 38. [Stuck on Shuffle: On Attribute-Object Binding in Vision-Language Models](https://arxiv.org/abs/2610.22602)

**<font color=#1a73e8>作者：</font>** Netanel Y. Tamir, Michael Green, Issar Tzachor 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieval is a fundamental task in multimodal systems: given an image or text query, the goal is to find the most relevant images or texts in a collection, often using a shared embedding space. Reliable retrieval requires these embeddings to capture not only which concepts are present, but also how they are composed. One key compositional challenge is attribute--object binding: encoding which attributes belong to which objects. Existing benchmarks provide a limited view of this capability, typically covering a subset of modality pairings, simple two-object swaps, or small attribute sets. Consequently, it remains unclear how robustly current models preserve attribute--object bindings across different modality pairings and more complex settings. We therefore introduce SABER, a controlled benchmark for evaluating attribute--object binding across all four image and text modality pairings, spanning diverse attribute types and scenes with up to ten objects. Evaluating models on SABER reveals substantial binding failures in both CLIP-style dual encoders and recent MLLM-based embedders. These findings motivate us to ask how binding can be improved efficiently. While multimodal supervision may be effective, collecting suitable images is difficult and costly. Text, on the other hand, is well suited to binding supervision: it is cheap to generate, supports a broader range of attributes and enables precisely controlled hard negatives. We thus finetune an MLLM-based embedder exclusively on synthetic attribute-binding text. Despite the absence of image supervision, the gains transfer to cross-modal and image--image retrieval while preserving general multimodal embedding performance. Our model achieves SOTA results on SABER while also improving on negation and instance-retrieval benchmarks, demonstrating broader benefits of our binding-focused supervision.

---


### 39. [At the Limits of Computability: Steps Towards Autonomous AI Discovery on the Busy Beaver Frontier](https://arxiv.org/abs/2610.22603)

**<font color=#1a73e8>作者：</font>** Marco Dos Santos, Vivek Veeriah, Alex Havrilla 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent breakthroughs in AI for mathematics---ranging from Olympiad medal performances to resolving long-standing open conjectures---have rapidly expanded what automated systems can achieve. Yet these successes primarily concern predefined, human-formulated problems, leaving open how AI systems can autonomously uncover mathematical structure and formulate new questions. To push beyond static challenges, we explore the Busy Beaver (BB) domain, an uncomputable frontier that is fundamentally open-ended. Because no algorithm can compute the Busy Beaver number $\mathrm{BB}(n)$ for every $n$, this domain provides a natural setting for sustained exploration through mathematical conjecture and proof. In this paper, we introduce a Gemini-based agentic pipeline that automatically discovers accelerations of Turing machines, expressed as compact mathematical rules summarizing many execution steps. Our system integrates pattern recognition, automated conjecturing, informal mathematical reasoning, and formal theorem proving in Lean. With this framework, our system autonomously discovered and formally verified novel Collatz-like accelerations for eleven machines in $\mathrm{BB}(6)$. Subject to community acceptance, we provisionally classify these machines as Cryptids, namely machines whose blank-tape executions admit exact, compact mathematical descriptions but whose halting behavior remains unresolved. These results advance the analysis of $\mathrm{BB}(6)$ holdouts on the Busy Beaver frontier and demonstrate the potential of autonomous AI systems for open-ended mathematical discovery in fundamental computer science.

---


### 40. [ProactGen: Learning Proactive Clarification for Video Generation](https://arxiv.org/abs/2610.22608)

**<font color=#1a73e8>作者：</font>** Zhixiao Wang, Yang Chen, Yifan Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generation let users create high-quality videos from natural language descriptions, yet obtaining results that match user intent remains time-consuming: individual generations are computationally expensive, and underspecified prompts force repeated cycles of generation, inspection, and revision. Existing video prompt optimization methods improve generation through automatic rewriting, but cannot supply the ideas and preferences that were not in the initial description. We propose ProactGen, a video generation framework that learns proactive clarification, eliciting user intent through questions grounded in generated video drafts. Specifically, we train a vision-language model as a questioning policy with reinforcement learning: observing the initial prompt and a video draft, it learns to ask the questions most valuable to downstream generation, rewarded by the alignment between the final generated video and a target reference. We further find that effective questioning does not require drafts of final-output quality, and exploit this property by generating drafts with fewer denoising steps, keeping the added cost of clarification low. Experiments show that ProactGen improves target alignment over direct generation by at least 1.8x the gain of the strongest baselines. Moreover, a single round of ProactGen already exceeds the alignment that the strongest baseline reaches after four refinement rounds, in 29% of its time.

---


### 41. [Shift-Reliance Alignment: Ranking Vision-Language Models by the Cues They Trust](https://arxiv.org/abs/2610.22610)

**<font color=#1a73e8>作者：</font>** Faisal Mohammad, Mohamed Younis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are usually chosen from leaderboards, which give one ranking for every application. On questions about objects that a scene suggests but does not contain, however, the model with the lowest error on the POPE hallucination benchmark is not the one with the lowest error on such questions. For yes/no questions about object presence, we show that the best model for a target domain can be predicted without running any candidate on that domain, given 650 to 1,200 labeled target items that calibrate a detector. We measure each model's reliance on a cue, a feature such as scene context or text in the image, by editing 100 labeled source images so that the cue suggests the wrong answer, and comparing with a matched control edit. Reliance predicts which VLMs are misled by physical sticker attacks (Spearman .93 on nine models not used to design the score) and which hallucinate on unedited COCO photographs, beyond what their tendency to answer yes explains. Shift-Reliance Alignment (SRA) scores a model by its source error on the labeled source questions plus its reliance multiplied by the shift. The shift is the proportion of target questions on which the cue misleads, and a detector estimates it on the unlabeled target images. SRA selects the model with the lowest score. In pre-registered tests on new images where most questions mislead, it lowered the error of the selected model from 30.4% under selection by source error to 18.8% on Objects365 and OpenImages but, against its prediction, not on COCO. On CueDial, a benchmark we release that varies how often a cue misleads, selection by model confidence falls more than 40 percentage points behind the best model when overlaid text denies a visible object, and SRA stays within 3 points.

---


### 42. [When Does Uncertainty Measure RAG Hallucination Risk?](https://arxiv.org/abs/2610.22615)

**<font color=#1a73e8>作者：</font>** Rajeel Ahmad Ansari, Tautik Agrahari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Uncertainty can measure hallucination risk in retrieval-augmented generation (RAG), but only when retrieved evidence constrains the answer. When evidence is present, unsupported factual claims become less likely; when retrieval coverage is poor, the model can answer from internal knowledge and assign high probability to unsupported claims. We test this across four instruction-tuned models on HotpotQA and SQuAD. After matching faithful and hallucinated answers within word-count bins, length-only classifiers fall near chance, while perplexity reaches 0.81--0.91 AUROC on targeted unsupported edits. Varying retrieval depth shows why the score changes meaning: detection can weaken with only the top-ranked passage, then recover after adding a second passage. A combined uncertainty and semantic-drift score improves calibration, and measurements remain above chance on RAGTruth QA. Results support a conditional view of uncertainty as a useful measure of RAG hallucination risk.

---


### 43. [Trajectory-Guided Steering: Mitigating Spurious Feature Bias in Clinical Classification](https://arxiv.org/abs/2610.22618)

**<font color=#1a73e8>作者：</font>** Fardin Ahsan Sakib, Ziwei Zhu, Ozlem Uzuner  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models rely on spurious features in clinical classification: swapping a single gender token in clinical notes alters gender-irrelevant diagnoses in up to 53.5% of cases. Existing inference-time corrections either need counterfactual data built around the specific spurious feature or behave unpredictably. We observe that how a model's preference between answers evolves across layers, its prediction trajectory, indicates for each document whether a correction is likely to help. We propose Trajectory-Guided Steering (TGS), which decides from the trajectory alone whether to correct each prediction and in which direction, with no counterfactual data and no knowledge of the spurious feature. On 16 clinical classification tasks from i2b2, TGS fixes 17.7% of errors while breaking only 1.3% of correct predictions and stays net-positive across all tested hyperparameter settings; all baselines are net-negative or near zero. The same corrections reduce reliance on the spurious feature: on the most affected diseases, gender-swap inconsistency falls sharply (hypertension 53.5% -> 38.0%, diabetes 35.1% -> 21.5%). Applying the correction to every document instead raises breaks on correct positive predictions from 0.1% to 6.4%, so per-document selection is essential. TGS also transfers to three model families and three other clinical and biomedical datasets.

---


### 44. [Noise-shaped Sampling and Annealing for Scalable On-the-edge Training of Binary and Ternary AI Models](https://arxiv.org/abs/2610.22621)

**<font color=#1a73e8>作者：</font>** Zihao Chen, Zhili Xiao, Rui-Jie Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The training loss of binary and ternary neural networks, expanded as a multilinear polynomial over the discrete weights, is structurally equivalent to the energy of a hierarchical high-order Ising model. We exploit this equivalence to apply Ising solvers to discrete-weight network training, while accounting for a fundamental difference in objectives: an Ising solver seeks the ground state of a fixed energy function, whereas training seeks solutions that generalize to unseen data. Our key contribution is $\Sigma\Delta$-Sampler, an optimizer that reconciles these objectives by embedding a stochastic sampling-and-annealing step as a noisy quantizer inside a first-order $\Sigma\Delta$ noise-shaping loop. The loop pushes noise from weight quantization, high-order frustration, and mini-batch sampling out of the low-frequency adaptation band, so that discrete weight updates follow the smooth descent trajectories embedded in the rugged loss landscape. We validate the framework on a planted quadratic unconstrained binary optimization (QUBO) benchmark with a known minimizer; on CIFAR-10, where a $13$M-parameter ternary model comes within $1\%$ of full-precision accuracy; on ImageNet-1k, where a ternary ResNet-18 comes within $0.4\%$ Top-5 accuracy of a ternary baseline; on class-incremental continual learning, where prior-task accuracy is preserved; and on MatMul-free language models up to $2.7$B parameters, where it outperforms a straight-through-estimator baseline under matched continued pre-training. Compared with standard quantization-aware training, $\Sigma\Delta$-Sampler reduces the training memory footprint by over $50\%$, delivers an order-of-magnitude speed-up, and reduces weight-update memory traffic by four orders of magnitude, making it attractive for on-device training and fine-tuning of large binary and ternary models.

---


### 45. [A Plausible Explanation Is Enough to Mislead Multimodal Judges](https://arxiv.org/abs/2610.22631)

**<font color=#1a73e8>作者：</font>** Anglin Cai, Zhiqi Wang, Xiaozhi Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) increasingly serve as judges in training and evaluation pipelines, often assessing answers together with explanations. Although AI judges are sensitive to textual factors, it remains unclear whether ordinary plausible explanations can sway judgments requiring visual verification. We introduce JUPE, a visual-question-answering (VQA)-style benchmark that fixes answers while varying explanations.
Across 14 MLLM judges, ordinary explanations that sound plausible mislead judges, with effects comparable on average to deliberately persuasive arguments. Plain justifications and chain-of-thought rationales reduce rejection of incorrect answers by 12.7 and 13.8 percentage points, respectively. We call this failure plausibility capture. Using signal detection theory, we find a significant mean shift in decision criterion toward acceptance, without a clear change in mean discriminability. Explanations sway judgments across domains, explanation generators, and judging protocols, while tested mitigations offer limited, model-dependent protection. Such shifts can inflate performance estimates when judges evaluate answers with explanations.

---


### 46. [ToMStories: Interpreting Theory-of-Mind in Synthetic Narratives](https://arxiv.org/abs/2610.22632)

**<font color=#1a73e8>作者：</font>** Melanie Subbiah, Chia-En Jacklyn Tsai, Kathleen McKeown  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding people often requires inferring what they feel or want from how they behave rather than from what they state outright. We ask whether language models can make these inferences, and how they do so. We introduce Theory-of-Mind Stories (ToMStories), an evaluation dataset of ~6,000 short synthetically generated narrative vignettes, each paired with a multiple-choice or open-ended question about a character's emotion, fear, motivation, or emotional wound. These psychological states are conveyed implicitly (showing), explicitly (telling), or with conflict between dialogue and description. Evaluating thirteen open-weight models (1B-72B parameters), we find that the largest models match humans on multiple choice but not open-ended questions. Our analyses point to simplifications models make in both interpretation and generation of implicit psychological states, indicating that synthetic data can help us understand how models perform interpretation, but likely overestimates how well models interpret humans.

---


### 47. [Measuring Mechanistic Uncertainty in Large Language Models via Causal Robustness](https://arxiv.org/abs/2610.22636)

**<font color=#1a73e8>作者：</font>** Aneesh Komanduri, Majid Afshar, Timothy A. Miller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in critical domains, where their susceptibility to hallucinations makes reliable and interpretable uncertainty quantification essential. We introduce the concept of mechanistic uncertainty, which characterizes uncertainty through the stability of the internal mechanisms supporting a model's response. We propose the causal robustness margin, defined as the minimum internal intervention required to deviate the model's output, and operationalize it using Jacobian Lens (Jlens) concept steering vectors. Across three open-source models and five question-answering datasets, we show incorrect and uncertain responses exhibit smaller margins, indicating greater sensitivity to internal interventions, and the causal robustness margin complements conventional output-based uncertainty methods. Finally, in a controlled knowledge injection experiment, correctly learned facts show increased margins after training, suggesting that causal robustness provides a mechanistically grounded signal of uncertainty.

---


### 48. [The Ephemeral Cost of Switching Optimizers Across LLM Training Stages](https://arxiv.org/abs/2610.22650)

**<font color=#1a73e8>作者：</font>** Xinyu Zhao, Davis Wertheimer, Ashutosh Sharma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work suggests that switching optimizers between pretraining and subsequent training stages incurs a performance cost, but systematic investigation of this phenomenon is lacking. We study the mismatch between AdamW and Muon optimizers by pretraining 1.2B Llama-3 models from scratch while varying the proportion of updates taken with each optimizer, and similarly interpolating between the two optimizers during continued pretraining and supervised fine-tuning (SFT). Surprisingly, we find little evidence of a meaningful optimizer mismatch penalty: final performance is largely explained by the independent effects of the pretraining and post-training optimizers, with downstream performance generally improving as the proportion of Muon updates during SFT increases. Although matching the pretraining optimizer can reduce forgetting during SFT, this does not translate into improved final benchmark performance. We further evaluate AdamW and Muon for task-general SFT of open-weight models, across the Llama and Qwen families up to 14B parameters, where Muon remains competitive with AdamW, despite these models having been pretrained with AdamW. Together, our results suggest that the choice of optimizer for post-training can be made largely independently of the optimizer used during pretraining.

---


### 49. [Evidence-Gated Bilingual RAG for Reliable Consumer Banking Search](https://arxiv.org/abs/2610.22652)

**<font color=#1a73e8>作者：</font>** Ahmed Mohamed Mahmoud Rayyan, Rana Mahmoud Mohammed, Aya Abdallah Abdelmonem 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Consumers often describe what they need rather than use the terminology found on a banking website. For example, a natural-language request ("a card for travel") may not share the keywords of the relevant product page, and the problem is harder in bilingual services, where the same intent may be expressed in Arabic or English. This paper presents an evidence-gated bilingual retrieval-augmented generation (RAG) framework for consumer banking search that operates entirely on local infrastructure. The framework combines structured web-content refinement, hybrid dense-lexical retrieval, intent-aware evidence selection, cross-encoder reranking, and a three-outcome Answer / Related Mismatch / No Answer decision mechanism. On 210 URL-labeled Arabic and English queries, the proposed approach improves Top-1 hit rate from 50.48% to 79.05% and MRR@5 from 0.571 to 0.797 over a hybrid baseline. A separate 26-case end-to-end evaluation achieved 69.2% strict success, with 72.7% of generated answers classified as supported by an automated faithfulness judge. These results are preliminary: the retrieval queries are paraphrases of a small reference set, and the end-to-end test is small and uses an automated rather than human judge, so they do not establish human-verified answer correctness or generalizable performance.

---


### 50. [Exploring The Empirical Privacy Landscape of Synthetic Data](https://arxiv.org/abs/2610.22659)

**<font color=#1a73e8>作者：</font>** Zihao Zhao, Avi Schwarzschild, Casey Meehan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Methods for training language models on sensitive data differ in how they balance capability gains against the risk of leaking private information. In this paper, we present a controlled comparison of data-level and training-level interventions for navigating the capability-privacy tradeoff on synthetic medical records with canaries to probe for leakage. Direct finetuning performs best on capability metrics but leads to the most privacy leakage, while DP-SGD reduces leakage at substantial cost to capabilities. Generating synthetic data from these records offers a more favorable balance, particularly when guided by a uniqueness-aware instruction to replace private details. Relative to naive paraphrasing, privacy-aware rewriting improves privacy protection across a variety of different rewriting models. We also find that more capable rewriting models generally reduce the risks of downstream privacy leakage, although held-out fit does not improve monotonically and increased test-time compute yields inconsistent gains. Overall, these results highlight privacy-aware rewriting as a promising direction for achieving a more favorable trade-off between capabilities and empirical privacy compared to other training-level methods, and our evaluation framework supports comparisons of future models and methods.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-258](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
