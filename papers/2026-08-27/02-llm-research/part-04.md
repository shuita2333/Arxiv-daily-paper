# 🧠 大模型相关研究 | 2026年08月27日

> 本类共 **190** 篇论文：已确认 **178** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-190**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-190**

---

### 151. [When "Must" Becomes "Maybe": Constraint Weakening in LLM Agent Workflows](https://arxiv.org/abs/2608.24569)

**<font color=#1a73e8>作者：</font>** Yiheng Sun, Huifei Wang, Yancheng Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents coordinate complex tasks through multi-role and multi-stage workflows. Upstream state is repeatedly transformed into intermediate language artifacts, such as summaries, plans, tickets, memories, and handoff notes, from which downstream components act. For action-constraining state, topical retention is insufficient: an artifact may mention an unresolved condition while changing it from a requirement that must be resolved before execution into information that may merely inform the next action. We study this action-binding role as operational state preservation. Safety blockers provide a controlled instance because each source state has an explicit prerequisite, authority, fallback, and execution consequence. We condition on correct upstream identification, vary the handoff transformation, and evaluate an executor restricted to the resulting artifact. Across 1,296 controlled synthetic episodes, direct-handoff controls preserve every blocker, whereas compression, plan assimilation, convergence, ownership deferral, and precedent substitution repeatedly turn binding state into caveats or non-binding considerations. Normal handoff compression produces 100.0% deactivation and 54.2% forbidden action. Restoring all four state fields raises preservation to 100.0% and reduces forbidden action to 0.0%. Fixed-artifact interventions further separate preservation from containment: downstream verification eliminates forbidden action while artifact deactivation remains 95.3%. These results identify a state-transmission failure between information extraction and action. Handoff transformations can retain state content while weakening its constraints on downstream action. Semantic availability does not guarantee operational preservation.

---


### 152. [EviDx: Evidence-Aware Active Diagnosis with Scaffolded LLM Agents](https://arxiv.org/abs/2608.24570)

**<font color=#1a73e8>作者：</font>** Lihang Zeng, Shaoting Zhang, Xiaofan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical diagnosis is an active evidence-seeking process in which clinicians acquire evidence, update competing hypotheses, and decide when the available evidence is sufficient for diagnosis. Yet many medical diagnosis systems built around large language models (LLMs) still formulate diagnosis as static case-to-answer prediction, with limited support for evidence acquisition. Agentic LLMs offer a dynamic alternative through tool use and intermediate diagnostic trajectories, but existing systems often under-specify how patient evidence should be exposed, scaffolded, and controlled at runtime. We introduce EviDx, an evidence-aware active diagnosis framework that pairs patient-specific diagnostic environments with a clinical diagnostic scaffold and an observer-guided runtime harness. In EviDx, $\mathcal{E}$-Synthesis constructs interactive environments from raw clinical cases; the scaffold organizes role-specialized agents, evidence tools, and evolving evidence states; and the harness regulates diagnostic termination by tracking uncertainty and evidence coverage. A 3-level evaluation pyramid assesses execution robustness, reasoning dynamics, and diagnostic outcomes. Experiments show that EviDx improves diagnostic performance and process stability while revealing model-dependent capability boundaries.

---


### 153. [Joint Optimization of Tool Creation and Use for Large Language Model Agents](https://arxiv.org/abs/2608.24571)

**<font color=#1a73e8>作者：</font>** Zhi Rui Tam, Chieh-Yen Lin, Yun-Nung Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented language models are bounded by the APIs humans bothered to write; existing tool-creation systems patch this by prompting a frozen LLM at inference time, leaving the model that writes a tool decoupled from the one that uses it, with no signal that the schemas it produces are schemas it can invoke. We propose SMITH (Schema-grounded Multi-task Iterative Tool Honing), a reinforcement learning framework that jointly trains tool creation and tool use inside a single policy. Each rollout is either a build task (write a tool from a few examples) or a use task (invoke a pooled tool on a held-out question). Three separate reward axes catch schema, code, and outcome failures independently, so each failure mode contributes its own gradient. A 4B Qwen3 trained with SMITH on 13 procedural reasoning tasks with exact verifiers reaches 79.8 macro-average accuracy on held-out tasks, the best across all evaluated methods and ahead of an untrained 30B-A3B tool-writer. It also reaches 40.4 on TabMWP-Hard and 42.6 on out-of-domain GQA (+7.6 over the best same-backbone inference-time baseline), without any visual or tabular training data. Tools written by our 4B models also lifted the performance of LFM-2.5-350M and Qwen3-30B-A3B under same reasoning tasks.

---


### 154. [PhysMLLMs: Spatial Priors for Unified Referring Segmentation and Grounded Reasoning of Images and Videos](https://arxiv.org/abs/2608.24574)

**<font color=#1a73e8>作者：</font>** Siyao Yan, Bo Han, Jisheng Dang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video multimodal large language models support language guided video segmentation, but they often show spatio temporal inconsistencies, e.g., jitter, drift, and identity switches. These failures are more common when targets are partly hidden or when similar objects appear this http URL likely reason is that current training lacks explicit spatial priors, which makes it difficult to maintain stable spatial identity and shape over time. We present PhysMLLMs, a training-stage prior injection architecture that injects physics-inspired spatial continuity priors into Video MLLMs. PhysMLLMs is designed to encourage more stable object-centered representations by aligning the student global visual representation with a frozen teacher model during training. Our core mechanism, Global Representation Prior Alignment (REPA-Global), distills global visual representations from a frozen DINOv2 teacher using an offline embedding cache and a scheduled distillation plan. This design keeps inference unchanged and does not add inference time cost. Across multiple video benchmarks, PhysMLLMs improves video segmentation mask quality and cross-frame consistency, with larger gains on challenging cases involving small targets, fast motion, occlusion, distractors, and reasoning queries. On single-frame referring image segmentation and representative general VLM benchmarks, PhysMLLMs maintains comparable performance, demonstrating that the injected spatial prior improves video consistency without compromising image-level grounding or general multimodal capability. These results suggest that physics-inspired spatial prior injection can improve temporal stability while preserving general capability. The code is available at this https URL.

---


### 155. [IAPO: Influence-Aware Policy Optimization for Credit Assignment in Multi-Turn Service Agents](https://arxiv.org/abs/2608.24588)

**<font color=#1a73e8>作者：</font>** Bo Ren, Yirong Mao, Yi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents increasingly solve long-horizon tasks through multi-turn interactions with users and external tools. In these settings, relevant task information often unfolds over time rather than being fully specified at the initial prompt. Service agents make this challenge especially concrete: users may clarify or revise their goals, while tool responses provide information needed for subsequent decisions. Thus, a final reward alone cannot indicate which actions contributed to resolving the task. Recent methods rely on comparative evidence from other trajectories or resampled continuations, or on separately constructed step-level learning signals, to refine credit. However, a completed rollout already records how information and errors flow between agent actions. We introduce Influence-Aware Policy Optimization (IAPO), which represents each rollout as a typed influence-dependency graph over trainable agent actions, with user and tool observations serving as evidence. IAPO converts support-use and failed-use structure into routing weights that redistribute the same trajectory-level advantage. Experiments with Qwen3-4B and Qwen3-8B demonstrate superior performance over multi-turn reinforcement learning (RL) baselines across three service-agent benchmarks: {\tau^2}-Bench, UserBench, and AgentChangeBench. BFCL-v4 Multi-Turn further shows that these gains do not compromise multi-turn function-calling performance. This work advances the understanding of credit assignment in multi-turn user interactions and provides a principled approach to training service agents from sparse outcome feedback.

---


### 156. [Is Discrete Difficulty Sufficient? Leveraging Continuous Difficulty for Efficient Self-Consistency in LLMs](https://arxiv.org/abs/2608.24590)

**<font color=#1a73e8>作者：</font>** Sihyeong Yeom, Geon Park, Geunyeong Jeong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-Consistency (SC) is a decoding strategy that samples diverse reasoning paths and selects the most consistent answer, demonstrating strong performance on complex reasoning problems. However, the excessive token consumption incurred by generating multiple reasoning paths has been identified as a major limitation of SC. To improve computational efficiency, several studies have proposed strategies that adjust the number of reasoning paths or allocate resources differentially according to problem difficulty. Nevertheless, most existing methods categorize difficulty into a few fixed levels, failing to fully capture the continuously varying nature of reasoning complexity. In this work, we propose Flexible Self-Consistency (FSC), which estimates problem difficulty as a continuous signal and dynamically adjusts the number of generated reasoning paths accordingly. FSC predicts the output entropy of an input question using a pre-trained probe and leverages it as an indicator of model uncertainty to flexibly control the sampling budget. Experimental results show that, across various models and benchmarks, FSC maintains accuracy comparable to SC while achieving token savings of up to 76%.

---


### 157. [Quantization Effects on Bangla Language Understanding in Large Language Models: A Systematic Evaluation](https://arxiv.org/abs/2608.24615)

**<font color=#1a73e8>作者：</font>** Ismail Hossain, Nafi Ullah Shafin, Mohammad Abdullah Al Mumin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training quantization lowers the memory footprint of Large Language Models (LLMs) and speeds up inference, which is why it is now common for on-device deployment. Most of what we know about its effects, however, comes from English benchmarks. It is not clear whether the same holds for morphologically complex, low-resource languages such as Bangla, and this gap is what we address here. We evaluate three model families---Qwen-2.5-7B, LLaMA-3.1-8B, and GPT-OSS-20B---in full precision and in three quantized formats (GPTQ-Int8, GPTQ-Q8, GGUF-W8A16) across five Bangla natural language understanding benchmarks (Bangla MMLU, CommonsenseQA-BN, OpenBookQA-BN, PIQA-BN, and BoolQ-BN), using zero-shot evaluation through lm-evaluation-harness. To our knowledge this is the first controlled comparison of quantization formats on Bangla NLU. The three families do not respond the same way: GPT-OSS loses up to 57.35% accuracy on reasoning-heavy tasks under GGUF-W8A16, while Qwen and LLaMA hold steady under GPTQ, and in a few cases the quantized version edges out the full-precision one. BoolQ-BN, a comprehension task, stays stable across all three families regardless of format. Taken together, these results suggest quantization can work well for Bangla deployment, but the choice of architecture and quantization method matters more than the bit width alone. We discuss what this means for practitioners choosing a model to run on constrained hardware.

---


### 158. [Beyond Semantic Accuracy: Consequence-Aware Evaluation for Safety-Critical Language Understanding](https://arxiv.org/abs/2608.24621)

**<font color=#1a73e8>作者：</font>** Yujing Chang, Thinh Pham, Van-Phat Thai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can language models be trusted in safety- critical operations? In such settings, strong per- formance on semantic metrics does not guaran- tee operational reliability: a misread altitude, a dropped execution condition, or a confused call- sign may score well under standard F1 yet carry sharply asymmetric operational consequences. We study this problem in air traffic control (ATC), where controller-pilot communication demands near-zero error tolerance, and use consequence-aware evaluation to test whether semantic scores misstate operational reliabil- ity. The framework is instantiated in a con- trolled diagnostic ATC benchmark grounded in aviation standards and feedback from 40 air traffic controllers across three countries. Evaluating 8 models, we uncover a system- atic semantic-safety gap: conventional scores give substantially higher performance estimates than consequence-aware evaluation, even for models that appear reliable under standard met- rics. Risk-aware fine-tuning narrows but does not close this gap, showing that consequence- aware evaluation is a necessary complement to standard NLP metrics before any real safety- critical deployment claim

---


### 159. [Expectation, Backlash, Recovery, and Excitement: How Model Releases Shape Reddit Perceptions of Conversational AI Systems](https://arxiv.org/abs/2608.24654)

**<font color=#1a73e8>作者：</font>** Vahid Rahimzadeh, Yury Zhauniarovich, Savvas Zannettou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational AI systems (CAISes) continuously change through model releases, feature updates, safety interventions, and access-policy shifts, yet user perceptions are often studied as static snapshots. We conduct a long-term, large-scale analysis of Reddit discussions to examine how users perceive CAIS model release interventions across providers. By combining sentiment classification and thematic concept analysis, we show that CAIS perceptions are dynamic and intervention-sensitive. Anthropic exhibits the clearest positive release profile through Claude Code and product-model fit, OpenAI shows backlash-and-recovery dynamics around GPT-5 and GPT-5.1, Grok-3 is shaped by provider identity and political discourse, and DeepSeek-R1 combines engineering praise with concerns about censorship, access, and reliability. These findings show that model releases are not merely technical updates, but user-facing interventions that reshape sentiment, expectations, and public discussion.

---


### 160. [Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning](https://arxiv.org/abs/2608.24658)

**<font color=#1a73e8>作者：</font>** Zhengyang Zhang, Zijian Zhang, Jiaxuan Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling test-time reasoning has substantially improved the problem-solving ability of large language models (LLMs), but standard autoregressive decoding still executes long reasoning traces sequentially, creating severe latency for difficult tasks (up to days and weeks). Parallel reasoning offers a natural remedy. However, prior systems primarily focus on Subtask Parallelism, where the model learns to decompose a high-level task into smaller chunks that can be solved independently. This approach overlooks another pervasive form of parallelism: Trial Parallelism, where multiple speculative attempts explore, verify, and aggregate competing hypotheses in parallel. In this paper, we introduce Parason, which reveals and learns both forms of parallelism in LLM reasoning. Our analysis identifies Trial Parallelism as the majority of parallelizable reasoning computation (65.5% in DeepSeek-V4's reasoning steps in HLE), and it becomes increasingly dominant on hard problems. Guided by this taxonomy, Parason converts sequential reasoning traces into structured parallel trajectories with a context-free grammar, then trains models with Parallelism-Aware Group Relative Policy Optimization (PA-GRPO), whose reward jointly balances accuracy, latency, and the two parallelism ratios. At inference time, Parason executes the learned parallel structure through tool calls, translating theoretical savings to real-world wall-clock acceleration. Experiments on mathematical reasoning benchmarks including AIME24 and AIME25 show that Parason achieves an average acceleration about 1.7$\times$ while maintaining competitive accuracy.

---


### 161. [The Invisible Editorial Layer: Formalizing Undisclosed Inference-Time Steering, Probability Placement, and the Attribution Problem in Deployed Language Models](https://arxiv.org/abs/2608.24662)

**<font color=#1a73e8>作者：</font>** Augusto Camargo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are commonly evaluated under the assumption that their observable behavior is primarily determined by model weights, training data, alignment procedures, and user prompts. This view is incomplete. Modern inference pipelines may systematically modify the probability distribution produced by a model immediately before token selection, creating an additional layer of control between frozen weights and observed text.
While controlled generation (e.g., PPLM, GeDi, DExperts, FUDGE) and text-watermarking systems (e.g., SynthID-Text) demonstrate the technical maturity of decoding- and logit-level interventions, the governance, security, and economic implications of an undisclosed inference policy remain comparatively underexplored. This paper examines the emergence of inference-time framing bias: the systematic modification of generated language toward political, ideological, institutional, or commercial frames via interventions applied after model inference but before token sampling.
We formalize the operational reality Model != Deployed System and introduce three concepts: (1) the Inference Attribution Problem, characterizing why observed behavioral bias cannot generally be causally attributed to model weights alone under limited observability; (2) Probability Placement, defining a hypothetical advertising primitive in which commercial influence is implemented through systematic shifts in generation probabilities rather than explicit product insertions; and (3) Inference Policy Transparency, a governance principle for making deployment-layer interventions auditable. We examine these concepts in relation to Article 5 of the EU AI Act, the EU Digital Services Act, and FTC doctrines.

---


### 162. [Confident at the moment of action: belief miscalibration in LLM play under hidden information](https://arxiv.org/abs/2608.24691)

**<font color=#1a73e8>作者：</font>** Bhushan Kashinath Joshi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems increasingly gate actions on a model's own stated confidence, which assumes confidence tracks correctness at the moment of acting. We test this in a hidden-information chess variant where royal status can be secretly, repeatedly relocated between pieces, and where an agent's stated probability distribution over the opponent's hidden royal piece -- elicited every turn, separately from the move it chooses -- is scored against ground truth recoverable after the game. Across two independent batches, captures made at high stated confidence ($\geq 0.5$) about the hidden piece's location were correct in 1 of 62 cases. The calibration deficit is concentrated almost entirely in these events: 99.3% of it in the original batch, 98.7% in the replication. The same pattern, in weaker form, orders consistently (point estimates only; most pairwise gaps are not statistically distinguishable at this sample size) across four further model configurations spanning a second provider -- reported as scope for the finding, not as evidence that capability predicts calibration: a same-model comparison at a fixed external leaderboard score shows a deliberation-budget change alone moves the metric by nearly as much as a large cross-model gap. In a separate seat, conventional evaluation axes -- legality, cost, latency, completion rate -- can dissociate entirely from belief quality, with the configuration winning on every conventional axis producing the worst belief quality tested. A model exhibiting this pattern can still win the game its belief was about, which is why outcome-only evaluation would not detect it.

---


### 163. [On-policy Distillation with Verifiable Reward](https://arxiv.org/abs/2608.24696)

**<font color=#1a73e8>作者：</font>** Wenze Lin, Jiale Zhao, Xitai Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) and on-policy distillation (OPD) have become two widely adopted paradigms for post-training large language models. However, RLVR suffers from sparse task-level feedback, while OPD provides dense token-level guidance but ignores trajectory correctness, limiting its performance to that of the teacher. Combining them is a promising direction: OPD supplies dense supervisory signals, while RLVR provides task-level correctness. Nevertheless, existing integrations often rely on weighted combination or heuristic switching, introducing extra hyperparameters and trade-offs. We propose On-policy Distillation with Verifiable Reward (OPDVR), a simple yet effective method that seamlessly combines OPD and RLVR without adding any hyperparameters. We first reformulate the implicit reward of sampled-token OPD based on trajectory correctness, then apply a ReLU gating mechanism to ensure that correct trajectories receive non-negative rewards and incorrect ones receive non-positive rewards---thereby aligning the distillation signal with task success while preserving the teacher's distributional guidance. Furthermore, our modification transforms sampled-token OPD into a proper RLVR method, making it readily combinable with any policy gradient algorithm, such as GRPO. Experiments on six reasoning benchmarks show that OPDVR consistently outperforms standard OPD. Our code is available at this https URL.

---


### 164. [Meta$^n$: Recursive Self-Improvement through Emergent Depth](https://arxiv.org/abs/2608.24735)

**<font color=#1a73e8>作者：</font>** Zae Myung Kim, Young-Jun Lee, Seungyeon Jwa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improving LLM agents refine answers, not the process that produces those answers. Systems that add a meta-level hold that level fixed, and those that edit themselves must leave part of their own editing machinery untouched to stay stable, capping the meta-depth they realize at roughly two. We present Meta$^n$, which keeps the meta-operation fixed and recurses on its input instead. That operation, $\Omega$, is applied repeatedly to its own products, reading the traces of the solver stack below together with the code that produced them, then writing the next layer as a strategic pre-process and a library of callable helpers. Because $\Omega$ never changes, it cannot destabilize the system, and because its input strictly grows, each layer reasons from a higher vantage than the last. Depth is set by convergence rather than fixed in advance, and an evolutionary archive searches over layer chains. Across two backbones, Meta$^n$ outperforms prior self-improving agents on all eight benchmark families. The sharpest case is ARC-AGI-2, built to resist skill memorization, where it alone scores above zero. Ablations indicate that most of the gain from recursion comes from the conditioning each layer passes to the next, and distinct layer roles emerge with depth although no prompt prescribes them. Code available at this https URL

---


### 165. [SkillForge: Evolving Verifiable Skills for Reinforcement Learning Agents](https://arxiv.org/abs/2608.24747)

**<font color=#1a73e8>作者：</font>** Shidong Yang, Ziyu Ma, Tongwen Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are trained with reinforcement learning (RL) for complex decision-making tasks. However, most RL-trained agents remain episodic and cannot accumulate reusable knowledge across episodes. Recent skill-based approaches, such as SkillRL, attempt to address this issue by extracting skills from raw trajectories, but treat the skill bank as an append-only repository without verifying whether stored skills remain effective. In this paper, we propose SkillForge, a framework for continuous skill evolution that enables skills to be verified and refined through environment interaction. By making skill usage explicit during agent interaction, RL can directly optimize both environment actions and skill invocation decisions. SkillForge further introduces evidence-based skill verification and multi-pathway skill induction, allowing the skill bank to continuously grow while maintaining its quality. Extensive experiments on ALFWorld, WebShop, and AppWorld show that SkillForge consistently outperforms SkillRL, demonstrating the effectiveness of continuously verified skills in training stronger LLM agents.

---


### 166. [The RAT: A Unified Bayesian Model for RAG Evaluation](https://arxiv.org/abs/2608.24753)

**<font color=#1a73e8>作者：</font>** Pius von Däniken, Felix Matthias Saaro, Mark Cieliebak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating Retrieval-Augmented Generation (RAG) systems requires assessing not only end-to-end correctness but also how individual components interact and how errors propagate through the pipeline. We introduce a Bayesian evaluation framework that jointly models retrieval success, abstention behavior, and answer correctness, factorized according to the pipeline's information flow. The model distinguishes task success. Whether the user received a correct answer (from generator success) and whether the generator behaved appropriately given the retrieval outcome. We apply the framework to 27 RAG configurations across three datasets, three retrievers, and three generators, and show that the conditional decomposition reveals substantial behavioral differences between systems that appear equivalent under marginal metrics. We further analyze the annotation allocation problem, demonstrating that retrieval-success annotations are more informative than task-success annotations for estimating policy adherence, and provide an information-theoretic explanation for this asymmetry. Finally, we extend the model to incorporate LLM-as-a-judge annotations as calibrated noisy observations, enabling practitioners to combine limited human judgments with cheaper automated assessments within a unified probabilistic model.

---


### 167. [RACE: Scalable Statistical Estimation of Functional Consistency in LLM Neurons](https://arxiv.org/abs/2608.24758)

**<font color=#1a73e8>作者：</font>** Runyu Wang, Bo Liu, Xiaxin Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discovering stable neuron behavior across entire domains remains a challenge in mechanistic interpretability. Existing methods often rely on instance-level point estimates or computationally expensive procedures, which either obscure population-level variability or limit scalable domain-wide analysis. We present RACE (Residual Alignment for Consistency Estimation), a forward-pass statistical framework that evaluates the domain-wide functional consistency of Transformer neurons. Perturbation experiments demonstrate that RACE achieves superior domain specificity compared to gradient-based point estimates. Meanwhile, token-distribution-level results verify the association between the selected neurons and the target domain. Furthermore, its computational overhead is two orders of magnitude lower than that of gradient-based methods.

---


### 168. [MoTE: Mixture of Task Experts for Multi-Task Video Understanding](https://arxiv.org/abs/2608.24763)

**<font color=#1a73e8>作者：</font>** Muhammad Asad Ali, Umar Khan, Nadia Robertini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Procedural video-language models must solve heterogeneous tasks from the same visual evidence, including action recognition, forecasting, and procedure prediction. Dense transformer decoders share the same feed-forward networks across tasks, which can entangle task behavior and make controlled capability expansion difficult. Sparse Mixture-of-Experts (MoE) decoders provide conditional computation, but token-level learned routing is not naturally aligned with task-level procedural objectives. We propose MoTE (Mixture of Task Experts), a decoder architecture that converts large language model feed-forward networks into task-specific experts while keeping the multimodal backbone shared. Each example follows one sample-level task route, so active task-expert computation remains independent of the number of stored task experts. We instantiate this design as VideoLLM-MoTE and evaluate it on five COIN benchmarks using explicit task routes. The five-expert model activates ~2B LLM parameters per sample and achieves higher average top-1 accuracy than recent VideoLLM baselines. Under the same expert topology, it improves over dense all-expert activation and learned sparse-routing controls. These results show that task-structured routing provides an interpretable and compute-efficient decoder alternative for multi-task video-language learning.

---


### 169. [Evidence Blindness in Direct Corpus Interaction: Persistent Navigation with AtlasNav](https://arxiv.org/abs/2608.24764)

**<font color=#1a73e8>作者：</font>** Hongyu Guo, Zhiyu Zheng, Zhao Cao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents are moving beyond conventional retrieval-augmented generation toward direct interaction with external corpora. Direct Corpus Interaction (DCI) keeps the full corpus accessible, yet reachable evidence can remain unusable under finite interaction budgets. Required evidence may fail to surface, a surfaced supporting document may remain unopened, or an opened document may fail to expose its decisive fragment. We call this progressive silent loss Evidence Blindness and quantify it through stage-wise evidence realization. Within the DCI paradigm, raw interaction adds little reusable corpus organization, while dynamic-workspace methods reconstruct a query-conditioned interaction space from each query and trajectory. In both cases, useful structure is recovered largely online. We instead formulate large-scale agentic search as finite-budget navigation over reusable corpus structure. We introduce AtlasNav, a persistent multi-view corpus-navigation framework that retains direct corpus interaction but organizes the corpus once into a Corpus Atlas, allowing each query to navigate adaptively rather than reconstruct shared structure. On BrowseComp-Plus, AtlasNav achieves 92.05% strict accuracy while reducing recorded online inference cost by 30.21% relative to the prior dynamic-workspace state of the art. Under matched budgets, it realizes the complete required evidence earlier and approaches the same model's evidence-supplied empirical reference more rapidly. The same representation principle remains effective under PhantomWiki's distinct corpus organization and controlled 10K-1M scaling, and transfers competitively to heterogeneous enterprise knowledge. These results show that agentic search depends not only on accessible evidence, but also on how the corpus is represented so that limited interaction becomes effective navigation.

---


### 170. [Shaping the Future of Generative AI for Black Communities: A Frame Analysis of Public Discourse and Empirical Scholarly Research](https://arxiv.org/abs/2608.24767)

**<font color=#1a73e8>作者：</font>** Angela D. R. Smith, Gabriella Thompson, Christopher L. Dancy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As generative AI (genAI) systems become embedded in education, employment, healthcare, and creative industries, the impact and engagement among marginalized groups have become both a widespread discourse and a focus in scholarly research. As a starting point, we examine public discourse and empirical research to explore the impact of genAI systems on Black communities. We conducted a systematic literature review (SLR) of 91 empirical papers alongside a media discourse frame analysis of 28 public resources, applying Entman's framing theory to map how each corpus defines problems, attributes causes, and proposes treatments. Our SLR reveals that scholarly research concentrates heavily on technical bias detection, reducing Blackness to measurable variables rather than engaging with cultural practices, structural conditions, or Black knowledge systems. Our frame analysis reveals that public discourse attributes genAI-related harm to historical and systemic forces, while scholarly research stops its causal accounts at the dataset and its treatment recommendations at technical reform. We demonstrate that this misalignment is structurally produced: anti-Blackness operates simultaneously across both registers, generating a shared evacuation of Black epistemic agency. We argue for frame analysis as an AI ethics methodology capable of surfacing what technical evaluation forecloses.

---


### 171. [MoE-based Feature Adapter for Prompt-free Binary Coronary Artery Segmentation in X-ray Angiography](https://arxiv.org/abs/2608.24783)

**<font color=#1a73e8>作者：</font>** Lin Xi, Yingliang Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of coronary arteries in X-ray angiography videos is essential for quantitative coronary analysis and image-guided interventions. However, accurate segmentation remains challenging because coronary vessels are thin and exhibit low contrast, while the presence of catheters, guidewires, and complex anatomical background structures can further interfere with vessel delineation. Existing U-Net- and Transformer-based models provide strong baselines, but their shared feature-adaptation pathways may be insufficient for heterogeneous angiographic appearances. In this paper, we propose a prompt-free mixture-of-experts (MoE) feature adapter for binary coronary artery segmentation. Built upon parameter-efficient Vision Transformer adapters, the proposed method uses multiple lightweight experts with input-dependent top-$k$ routing to adaptively refine vessel-related features while limiting active computational cost. Experiments on MOSXAV and external evaluation on XACV show that the proposed method outperforms representative baselines and improves cross-dataset generalisation. These results suggest that MoE-based adapter learning is effective for robust coronary artery segmentation in X-ray angiography videos.

---


### 172. [Right Diagnoses, Decorative Reasoning:A Perturbation Audit of Medical Chain-of-Thought](https://arxiv.org/abs/2608.24790)

**<font color=#1a73e8>作者：</font>** Mengzhu Xu, Jifan Gao, Xia Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinicians read chain-of-thought (CoT) rationales as evidence of medical reasoning, but whether the visible chain plays that role is rarely tested. General-domain CoT-faithfulness probes ignore clinical cost, and medical LLM evaluations treat the chain as a black box. We close this gap with a medical perturbation audit: a 30-operator battery edits both the chain and the question with clinically motivated operators (severity reversal, negation flip, demographic swap, evidence ablation), paired with a chain-update times answer-flip joint analysis that classifies each model by its failure mode. Applied to 14 LLMs on four medical QA benchmarks, three independent tests converge: the Chain-Decoupling Rate (CDR; chain does not register the edit and the answer does not flip) is 72.9% panel-wide on clinically meaningful destructive edits, chain corruption leaves accuracy unchanged, and removing CoT prompting does not reduce accuracy. Two board-certified clinicians re-annotate N=197 perturbed questions; 98.5% leave the gold defensible. The pattern holds across medical and reasoning fine-tuning and scale; on the closed-source tier, where the chain text is unavailable, the answer-side signals are consistent with the same decoupling. Our framework and CDR provide a reusable yardstick for auditing whether medical CoT is faithful or merely documentation.

---


### 173. [StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments](https://arxiv.org/abs/2608.24804)

**<font color=#1a73e8>作者：</font>** Esakkivel Esakkiraja, Denis Akhiyarov, Vikas Yadav 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present StarHarness, a framework for evolving environment-specific agent harnesses while keeping model weights fixed. The evolved harness can include prompt and task framing, tool interfaces, skills, MCP-backed providers, subagent structure, and agent-loop configuration. StarHarness constructs a compact evolution pool by stratifying tasks according to baseline failure behavior, separates proposer-visible search tasks from proposer-hidden selection tasks, and reserves held-out tasks for evaluating generalization. Across ITBench SRE, EnterpriseOps-Gym ITSM, and AutomationBench Finance, harness evolution improves full-benchmark performance by 20-35 percentage points over the default harness after 4-12 accepted changes per environment. These gains persist on tasks excluded from evolution and transfer without re-evolution across GPT and Qwen model families. Trace analysis links the improvements to interface repairs, environment conventions, and operational knowledge that compresses search, with fewer false-positive diagnoses and shorter trajectories in several settings. StarHarness therefore offers a practical way to reduce persistent model-environment mismatch in tool-rich enterprise tasks.

---


### 174. [Effective Learning Rate Governs Loss Dynamics in Language Model Pretraining](https://arxiv.org/abs/2608.24814)

**<font color=#1a73e8>作者：</font>** Zihan Liu, Ruiheng Zheng, Shaobo Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We uncover ELR collapse in language model pretraining: learning rate (LR) and parameter norm govern loss dynamics primarily through their ratio, the effective learning rate (ELR). When ELR is matched across runs, their loss trajectories collapse throughout training despite substantially different LRs and parameter norms. Across optimizers, architectures, datasets, and model scales, mean collapse errors are typically a few x 10^-3, below the seed-to-seed variation measured in a representative configuration. Systematic ablations identify normalization design and the timescale of LR-norm variation as key determinants of collapse precision. Controlled interventions further show that weight decay and Hyperball shape loss dynamics primarily through the ELR schedules they induce. Replacing LR with ELR enables a fitted functional scaling law (FSL) to transfer across norm-control methods. The resulting ELR-based FSL also explains delayed acceleration, a recurring effect of norm control. Together, these results establish ELR as a common coordinate linking LR scheduling, norm control, and loss dynamics.

---


### 175. [Constrained Entity Selection under Partial Knowledge for LLM-Based Knowledge Graph QA](https://arxiv.org/abs/2608.24824)

**<font color=#1a73e8>作者：</font>** Emanuel Kitzelmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used for knowledge graph question answering (KGQA), but can fail to correctly ground answers in the underlying graph. Current approaches to LLM-based KGQA either rely on full semantic parsing into executable queries such as SPARQL, which is brittle in practice due to complex schemas or incompleteness of real-world KGs, or on LLM-reasoning and answer generation over KGs, which can be more robust but lacks formal guarantees. In this work, we study a complementary setting in which \emph{candidate} answers are generated by an LLM-based system and subsequently verified using lightweight symbolic constraints derived from the question. We introduce \emph{Constrained Entity Selection under Partial Knowledge (CES-PK)}, a problem formulation that focuses on eliminating invalid answers and providing symbolic support for valid ones without requiring construction of executable logical forms. To account for incomplete KGs, we employ a three-valued constraint semantics (\emph{satisfied, violated, unknown}) that avoids incorrect rejections under open-world assumptions. To demonstrate the effects of our method, we instantiate this framework over the Hetionet biomedical knowledge graph and evaluate the impact of type, relation, and exclusion constraints. Experiments show that precision improves by filtering invalid candidates, while recall is preserved due to retaining candidates whose constraints are not explicitly violated. Satisfied constraints provide additional positive symbolic evidence to rank remaining candidates.

---


### 176. [A Dual-Dimensional LLM Framework for Automated Item Incidental Content Similarity Analysis in Large-Scale Assessments](https://arxiv.org/abs/2608.24825)

**<font color=#1a73e8>作者：</font>** Jing Huang, Jihong Zhang, Hua-Hua Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of large-scale assessments and the growing adoption of automatic item generation have intensified concerns about incidental content redundancy, where construct-irrelevant elements such as wording or contextual framing become unintentionally repetitive across items. Traditional similarity metrics like BLEU or cosine similarity, often fail to capture the nuanced structural and semantic layers that drive perceived redundancy simultaneously. This study proposes a dual-dimensional framework for Automated Item Similarity Analysis (AISA) powered by Large Language Models (LLMs), operationalizing similarity through Structured Decomposition and Semantic Relatedness. Psychometric validation indicates that LLM-derived metrics align more closely with indicators of construct-irrelevant local dependence and yield more coherent item parameter groupings than traditional text-based measures. The framework is further evaluated through its application in Computerized Adaptive Testing (CAT). Simulations reveal that incorporating LLM-based similarity constraints into item selection improves estimation stability and reduces bias with minimal efficiency trade-offs, outperforming constraints based on conventional metrics. These findings highlight the potential of LLM-powered AISA to support scalable bank curation, content-aware test assembly, and experience-sensitive adaptive testing across diverse assessment contexts.

---


### 177. [Reading Is Not Using: Retrieval, Judgment, and the Design of AI Financial Research Workflows](https://arxiv.org/abs/2608.24842)

**<font color=#1a73e8>作者：</font>** Miao Liu, Zhizhe Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as AI analysts to process financial disclosures and support AI-assisted investment decisions. Yet such systems are usually evaluated by what they can retrieve, not whether retrieved information affects their judgments. We identify a retrieval-integration gap in long-context financial analysis. Holding focal-firm information fixed and varying only unrelated context from 2,000 to 128,000 tokens, we find that a risk disclosure's influence on investment judgments falls to the experimental noise floor even as direct retrieval remains accurate. The pattern replicates across model families and judgment tasks and in experiments removing real disclosures from actual 10-K filings. More capable models postpone but do not eliminate the gap. Causal memory interventions show that compressed summaries and source-text lookup jointly transmit disclosures into judgments. Workflow architecture determines whether this transmission succeeds: chunk-and-summarize pipelines evict relevant information, whereas a targeted, structured restatement adjacent to the decision restores its influence. AI analyst performance is therefore jointly determined by model capability and workflow architecture. Retrieval-based evaluations can certify systems whose investment judgments ignore information they demonstrably retrieved.

---


### 178. [Prompt Structure Redistributes, Not Reduces: An Empirical Analysis of Security-Weaknesses in LLM-Generated Python Code](https://arxiv.org/abs/2608.24857)

**<font color=#1a73e8>作者：</font>** Maitreyee Das Urmi, Jessica Pourleyli, Fabio Santos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) increasingly generate code from natural-language prompts, making prompt engineering a key mechanism for shaping the security of generated software. Structured and security-oriented prompts are widely used to encourage safer code, yet their effects extend beyond whether detected weaknesses are simply present or absent. Using 424 security-sensitive Python tasks, we generate solutions with GPT-4o and LLaMA 3.1-8B under five prompt variants that progressively add structural and security guidance, and evaluate them with Bandit and CodeQL along two axes: generation compliance and security weakness prevalence, severity, and CWE distributions. Structured prompting substantially reduces refusals (e.g., GPT-4o invalid outputs drop from 338 of 424 to 37-52), enabling large-scale analysis, but security-oriented refinements do not consistently reduce overall weakness prevalence. For GPT-4o, stronger prompts primarily redistribute risk: high-severity findings fall (20.8% to 13.6%) while low-severity findings rise (32% to 43.5%); LLaMA shows weaker, less consistent shifts. We also observe security-driven semantic drift, where stricter prompts silently remove or rewrite explicitly requested unsafe constructs. Overall, prompt structure improves compliance but is an unreliable substitute for robust security controls in LLM-assisted development.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 179. [A survey detection channel overrides the pixels in an astronomical foundation model, and biases tomographic mean redshifts](https://arxiv.org/abs/2608.23626)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ihor Kendiukhov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models for astronomy are trained on survey pixels together with the catalogue products derived from those pixels. Those catalogues are incomplete at a measurable rate, and a model trained on both inherits that incompleteness as a systematic. We audit AION-1, a 39-modality transformer trained on more than 200 million objects, using causal interventions on its inputs.
Holding the image tokens byte-identical and editing only the survey segmentation map changes every quantity the model reports -- flux, size, ellipticity, redshift -- by 110-4400 times a matched placebo. The mechanism is detection gating, presence at the field centre (r = 0.47), not the light the mask encloses (r = 0.30); across 322 real blends the model ignores how the pipeline partitioned the light (R = -0.006). Nor is the preference specific to that channel: contradicted catalogue photometry leaves the model nine times worse than supplying no metadata at all.
The Legacy Survey pipeline leaves 3.68% of targets with no segment covering their position. Propagating that rate, with a miss represented by the fields the pipeline actually returns, shifts tomographic mean redshifts by a median 0.71 times the LSST DESC requirement over 40 assignments and exceeds it in 12; observed positional errors take the worst bin to 8.3 times. Drawing the misses by their measured magnitude dependence rather than uniformly does not change it. Spectroscopy removes the effect, withholding the detection channel removes it at no measurable cost, and the effect grows with model scale.
Two further limits lie in the tokeniser: its image codec resolves 28 effective states on source patches against 934 for the spectrum codec, and the redshift readout is quantisation-limited. Sparse dictionaries are unreliable causal handles: across 15, recovery spans 26-75% and moves up to 18 points on the seed alone.

---


### 180. [GAP-Prompt: Gated Adaptive Prompting for Efficient Continual Learning](https://arxiv.org/abs/2608.23782)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Trung-Anh Dang, Duy-Cuong Bui, Ngoc-Son Vu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning faces the persistent challenge of catastrophic forgetting, where sequential task updates degrade previously acquired knowledge. While prompt-based methods integrated with pre-trained models offer a compelling solution by freezing the backbone, they often rely on static, task-level prompting strategies that overlook fine-grained intra-task diversity. In this paper, we propose Gated Adaptive Prompting (GAP-Prompt), a novel method that introduces instance-level adaptability to the prompting process. GAP-Prompt consists of three synergistic modules: (1) instance-conditioned gating, which dynamically determines optimal prompt injection layers for each individual image; (2) dynamic knowledge fusion, which performs instance-aware aggregation of current and historical prompts, enabling knowledge integration across tasks; and (3) shared prompt distillation, which anchors foundational knowledge in early shared layers to mitigate forgetting. Extensive evaluations on CIFAR-100, ImageNet-R, and CUB-200 benchmarks demonstrate that GAP-Prompt consistently achieves state-of-the-art performance. Notably, on the fine-grained CUB-200 dataset, GAP-Prompt reaches 87.29% accuracy, approaching the joint training upper bound (88.00%) and outperforming existing methods by a significant margin.

---


### 181. [In-Context Inpainting for Time Series Forecasting](https://arxiv.org/abs/2608.23855)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Thang Nguyen, Dung Nguyen, Romero Morais 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose ICI-Time, a novel framework that reframes time series forecasting as a visual inpainting task, leveraging the generalisation power of large vision models (LVMs). Unlike methods that require specialised temporal architectures and extensive domain-specific training, ICI-Time transforms time series into structured visual representations (area charts) and applies visual in-context learning, reformulating forecasting as pattern completion within a grid-structured prompt that pre-trained vision transformers can solve without fine-tuning or architectural modification. Temporal dependencies are represented through spatial layout, with a consistent, invertible mapping between numerical and visual domains. Extensive experiments across epidemiology, meteorology, and power systems demonstrate that ICI-Time performs competitively against deep learning baselines and shows promising adaptability under limited-data settings, introducing a new paradigm that bridges temporal and visual domains.

---


### 182. [Recursive Agentic Reasoning](https://arxiv.org/abs/2608.23956)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shengxin Zhang, Xiaomin Wu, Xiyang Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time reasoning methods such as iterative refinement, decomposition, and repeated sampling are often evaluated in isolation, making their gains difficult to compare across models, benchmarks, and evaluation pipelines. We introduce a unified view of these methods as recursion operators over an agent's reasoning trace: GROW, which deepens a single reasoning path; PRUNE, which decomposes and recomposes the problem; and BRANCH, which samples alternative reasoning paths and selects among them. We evaluate all three operators against a single-pass chain-of-thought baseline under a shared harness with identical prompts, token budgets, and grading code. Across five benchmarks and three frontier models, comprising 14 model-benchmark settings, 49,327 graded items, and 151,876 model calls, BRANCH improves accuracy in all 14 settings by an average of 5.98 percentage points and is the best-performing operator in 12. In contrast, GROW yields a mean gain of 2.18 points and degrades performance in two settings, while PRUNE improves accuracy by 0.94 points on average. Analysis shows that BRANCH's advantage arises not only from exploring multiple reasoning paths, but also from recovering from truncation: its gains strongly correlate with the baseline rate of empty, budget-exhausted outputs (r = 0.72). These results weaken the hypothesis that different problems require routing among test-time reasoning operators; at this level of abstraction, repeated branching is consistently dominant. Finally, we show that unpaired evaluation and treating scoring-pipeline failures as model errors can materially change, and even reverse, comparative conclusions, motivating paired scoring as a standard protocol for test-time-compute evaluation.

---


### 183. [Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments](https://arxiv.org/abs/2608.24099)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Guo Gan, Yilun Zhao, Cong Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GUI agents often encounter dynamic anomalies when deployed on Android devices, from unexpected pop-ups to action misuse, yet existing benchmarks lack systematic evaluation of agent robustness against runtime anomalies. We introduce AnTrap, a comprehensive benchmark that injects dynamic perturbations into agent execution trajectories. We propose a taxonomy organizing real-world anomalies into four layers (State, Thinking, Action and Round) with ten fine-grained subcategories, and develop a construction pipeline that preserves task solvability while introducing realistic adversarial conditions. Evaluating 16 leading GUI models, we reveal universal vulnerability to dynamic anomalies, with even the strongest models suffering significant performance degradation. Furthermore, we conduct GRPO training in both original and adversarial environments to validate our benchmark, separating environment-learnable anomalies from reasoning-bottlenecked ones. Our findings show that while single-step traps at state and action layers are largely addressable through adversarial reinforcement learning, deep contextual traps, like state deadlock, expose intrinsic limitations that cannot be resolved by training in environments with traps alone.

---


### 184. [Steering Recurrent Reasoners at Inference Time with Readout Feedback](https://arxiv.org/abs/2608.24136)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shunsuke Kamiya, Masanori Koyama, Seongcheol Jeong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent models, which repeatedly update latent states with shared computation blocks, have emerged as powerful architectures for solving complex reasoning tasks. Existing inference-time methods scale computation by running more steps or sampling more trajectories, but ignore information revealed within each trajectory. Here we show that recurrent models can be improved at inference time by using their own readout probabilities to steer latent dynamics without retraining. We introduce Readout Feedback (RoFB), a test-time intervention that converts intermediate predictions into token-wise pairwise coupling forces injected into the latent dynamics. Across three recurrent models (AKOrN, ItrSA++, TRM) on Sudoku and Maze, RoFB yields clear gains in four of six model-task pairs, achieving performance unattainable by merely running more steps or selecting from multiple trajectories, at comparable or lower computational cost. These results suggest that closed-loop steering of latent dynamics can serve as a complementary inference-time control mechanism for recurrent reasoning models.

---


### 185. [STRIVE: Multi-Agent Structured Temporal Reasoning with Integrated Verification for Longitudinal Radiology Report Generation](https://arxiv.org/abs/2608.24237)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junyeong Maeng, Eunsong Kang, Heung-Il Suk  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Longitudinal radiology report generation (LRRG) requires identifying both current findings and their changes relative to a prior study. Existing methods jointly model diagnosis, attribute estimation, temporal comparison, and language generation within implicit representations, which can cause task interference, obscure the evidence underlying each decision, and limit error traceability. They also model progression states as independent labels, ignoring their ordered structure and thus treating missed changes and direction reversals equally. We present STRIVE, Multi-Agent Structured Temporal Reasoning with Integrated Verification for LRRG, which decomposes clinical reasoning into specialized Diagnosis, Attribute, and Temporal Change Agents that produce explicit intermediate evidence. In particular, the Temporal Change Agent is further post-trained using Progression-Aware GRPO, a verifiable, shaped reward that assigns partial credit to direction-preserving errors while scoring direction reversals lowest. STRIVE performs verification at two stages: a deterministic Consistency Gate reconciles the agent outputs before report generation, and a Validation Agent checks whether the generated report is supported by the aggregated clinical evidence. On Longitudinal-MIMIC, STRIVE attains the best clinical efficacy among recent methods and more than doubles Longitudinal Change Concordance (LCC), a measure of temporal agreement with the reference report, over the strongest baseline.

---


### 186. [Causal Analysis for Time Series Foundation Models](https://arxiv.org/abs/2608.24303)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mathis Jander, Wouter van Heeswijk, Martijn Mes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transitioning from bespoke time series models towards time series foundation models changes the relationship of model and application from one-to-one to one-to-many. This shift introduces concentration risk as many, potentially high-risk, forecasting applications are exposed to the same biases and failure modes of a single time series foundation model. At the same time, this centralization allows for economies of scale in model development and validation. In this study we investigate how biases and failure modes of time series foundation models can be identified before deployment. We propose a causal analysis framework to investigate the ability of a time series foundation model to preserve time series patterns. To achieve this, we intervene on parameterized synthetic time series generators and measure the corresponding change in model output under ceteris paribus conditions. We apply our causal analysis framework to Chronos-2 and TimesFM-2.5 and test them across six distinct time series patterns. We find safe configurations for trend and harmonic oscillation patterns. The results also indicate a bias in both models towards overestimating persistence, sudden failures for both models against the regime switch pattern and failure for TimesFM-2.5 against the energy-release pattern. Our review of the original works for both models indicates that the findings might be explained by the data used for pretraining. We conclude our study with suggestions for further model development, recommendations for application-specific model selection, and a discussion of limitations and further research directions.

---


### 187. [Metadata-Aware Adaptation of a Generative Foundation Model for Conditional CMR Synthesis](https://arxiv.org/abs/2608.24342)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Marc Rodríguez, Grzegorz Skorupko, Nay Aung 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic image generation is a promising strategy to address data scarcity and the underrepresentation of clinically important phenotypes in medical imaging, yet generating images that faithfully reflect meaningful patient characteristics remains challenging. In this work, we investigate metadata-conditioned cardiac magnetic resonance (CMR) synthesis using a pretrained latent diffusion model, encoding structured clinical metadata and slice position as textual prompts to guide CMR generation. To improve metadata adherence and address the imbalance of clinical attributes, we integrate three strategies: Metadata-Free Classifier-Free Guidance (CFG), Contrastive Batching, and Inverse-Frequency Sampling. The framework was fine-tuned and evaluated on 59,058 short-axis CMR from the UK Biobank using paired image similarity, distributional fidelity, and subgroup-level analyses. The combined approach achieved a Fréchet Inception Distance (FID) of 37.47, improving by 57.04\% over the same model fine-tuned without these strategies and by 28.68\% over a previous text-conditioned CMR diffusion baseline requiring cardiac geometry as additional input, while relying solely on patient metadata. This distributional gain, driven mainly by Metadata-Free CFG, came with a modest reduction in paired similarity, suggesting that the model prioritizes population-level realism over exact image reproduction. Subgroup analyses demonstrated improved alignment across demographic and acquisition-related metadata, with disease-specific conditioning being the most challenging task. These findings demonstrate the potential of generative foundation models for clinically meaningful CMR synthesis while highlighting the need for more effective metadata-aware conditioning strategies. Our code is available at this https URL.

---


### 188. [Taming foundation model with invariance-oriented pre-training for broad-spectrum EEG analysis across signal-level, brain-state, and brain-health tasks](https://arxiv.org/abs/2608.24597)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yulong Dou, Han Wu, Guo Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) is a widely used window into human brain function, but most EEG models remain tied to a one-dataset-one-model supervised paradigm. Recent EEG foundation models offer a route toward reusable representations, but most remain reconstruction-centered, assuming that EEG content predictable from local context is necessarily transferable neural information. Here we present INCEPT, an invariance-oriented EEG foundation model trained on over 11,000 hours of unlabelled clinical EEG. Rather than prioritizing signal recovery alone, INCEPT learns representation-level stability across correlated EEG observations, separating stable neural structure and essential subject-sensitive information from the nuisance variability that dominates scalp recordings while preserving subject-, state- and condition-discriminative information. We evaluate INCEPT on a broad-spectrum benchmark of ten datasets spanning three levels of post-acquisition EEG analysis: signal-level assessment, brain-state decoding, and brain-health evaluation. INCEPT ranks first among recent EEG foundation models on 26 of 30 linear-probing metrics and 24 of 30 fine-tuning metrics, and also surpasses strong task-specific specialist encoders across diverse downstream settings. Objective ablations and representation analyses further show that invariance-oriented pre-training improves transfer and organizes subject-sensitive neural representations beyond reconstruction alone. These results establish invariance learning as a promising principle for building reusable EEG foundation models.

---


### 189. [A Multimodal Foundation Model for Longitudinal Patient Representation and Scalable Insight Generation in Oncology](https://arxiv.org/abs/2608.24688)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Eugene Vorontsov, Yi Kan Wang, Alican Bozkurt 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Precision oncology necessitates a longitudinal model of patient state that captures cancer evolution and treatment over time, integrating multimodal observations. We introduce the oFM, a foundation model developed on a real-world oncology cohort of 1.67 million cancer patients that integrates clinical trajectories with DNA, RNA, and H&E pathology. Patient-level partitions were reserved for training, validation, and testing, with over one million patients used for training. The oFM encodes daily clinical and molecular episodes and, along with pathology images, integrates them over time to produce a patient state embedding. We evaluate frozen oFM embeddings against expert-curated clinical and molecular baseline features. In prognostic benchmarks, the oFM improved AUC for treatment response, progression-free survival, and overall survival (0.774 vs. 0.563 for overall survival). Across 11 comparative-treatment cohorts, the oFM embeddings achieved a three-fold higher pooled and scale-normalized treatment-benefit AUTOC than baseline features with improved benefit ranking in 9 of 11 cohorts, and provided stronger prognostic discrimination within both treatment arms. We also evaluated a mechanism discovery framework that interprets downstream models built on oFM embeddings by linking their predicted outcomes to clinically and biologically grounded mechanisms through an evidence-grounded temporal graph, enabling evaluation in clinical and drug-development applications.

---


### 190. [BrowserForge: Scaling Web Episode via Parallel Browser Sandboxes](https://arxiv.org/abs/2608.24848)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fei Tang, Huawen Shen, Zhiqiong Lu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web agents that act from rendered pixels avoid the fragility and heavy token cost of reading a page's HTML or accessibility tree, but training them depends on large amounts of high-quality interaction trajectories, and how to produce such data at scale remains an open problem. Public datasets typically contain only a few thousand trajectories drawn from a fixed and narrow set of websites, and even recent automated synthesis pipelines stay bound to predefined site lists or tutorial sources, so the number of distinct websites the agent ever sees barely grows. We present BrowserForge, a framework that generates web interaction data at scale by driving many browser sandboxes in parallel over the open web. BrowserForge couples three components: an open-web sourcing stage that exposes the agent to hundreds of thousands of real, openly reachable websites; a sandbox cluster manager that schedules hundreds of concurrent browsers with high utilization; and a Proposer-Solver dual-agent loop that turns a raw page into an executable task and then collects a verified trajectory for it. A rule-plus-model cleaning pipeline removes failed runs and rewrites the surviving reasoning into a single unified chain-of-thought style. Page structure such as the accessibility tree is used only as a synthesis-time signal; the agent we train and release acts purely from the screenshot. The resulting corpus contains 203,238 trajectories, each collected from a distinct website, larger and more diverse than prior trajectory datasets. Fine-tuning a compact multimodal model on this corpus raises its success rate on the live Online-Mind2Web from 25.66% to 33.33% and consistently improves step accuracy on the static Multimodal-Mind2Web, with the gain growing as the corpus scales. Controlled analyses further confirm that open-web sourcing and broad website coverage are key contributors to the observed improvement.

---


> [!TIP]
> 当前位于：**151-190**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-190**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
