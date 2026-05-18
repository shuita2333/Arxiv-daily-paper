# 🧠 大模型相关研究 | 2026年05月19日

> 本类共 **127** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-127](./part-03.md)

---

### 1. [SDOF: Taming the Alignment Tax in Multi-Agent Orchestration with State-Constrained Dispatch](https://arxiv.org/abs/2605.15204)

**<font color=#1a73e8>作者：</font>** Zhantao Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent orchestration frameworks such as LangChain, LangGraph, and CrewAI route tasks through graph-based pipelines but do not enforce the stage constraints that govern real business processes. We present SDOF, a framework that treats multi-agent execution as a constrained state machine. SDOF operates through two primary defensive layers, implemented by three components: (1) an Online-RLHF Specialized Intent Router trained via Generative Reward Modeling (GRPO) and (2) a StateAwareDispatcher with GoalStage finite-automaton checks and precondition/postcondition SkillRegistry validation for auditable execution control. On a recruitment system backed by the Beisen iTalent platform (6000+ enterprises), 185 expert-curated scenarios trigger 1671 live API calls. Our GSPO-aligned 7B Intent Router achieves higher joint accuracy than zero-shot GPT-4o on this FSM-constrained adversarial routing benchmark (80.9% versus 48.9%). In end-to-end execution, SDOF reaches 86.5% task completion (95% confidence interval 80.8 to 90.7) and blocks all 22 operations in the injection, illegal HR subset. Under a broader message-level blocking audit, SDOF attains precision 100% and recall 88%, expert agreement kappa=0.94. A separate evaluation on 960 SGD-derived dialogues spanning 8 service domains surfaces 201 stage-order conflicts under our FSM mapping, 41 of which arise in the normal split. This arXiv version reports the current validated scope; extended multi-seed training comparisons and deeper workflow evaluations will be released in a subsequent update.

---


### 2. [AgentStop: Terminating Local AI Agents Early to Save Energy in Consumer Devices](https://arxiv.org/abs/2605.15206)

**<font color=#1a73e8>作者：</font>** Dzung Pham, Kleomenis Katevas, Ali Shahin Shamsabadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous agents powered by large language models (LLMs) are increasingly used to automate complex, multi-step tasks such as coding or web-based question answering. While remote, cloud-based agents offer scalability and ease of deployment, they raise privacy concerns, depend on network connectivity, and incur recurring API costs. Deploying agents locally on user devices mitigates these issues by preserving data privacy and eliminating usage-based fees. However, agentic workflows are far more resource-intensive than typical LLM interactions. Iterative reasoning, tool use, and failure retries substantially increase token consumption, often expending significant compute without successfully completing tasks.
In this work, we investigate the time, token, and energy overhead of locally deployed LLM-based agents on consumer hardware. Our measurements show that agentic execution increases GPU power draw, temperature, and battery drain compared to single-inference workloads. To address this inefficiency, we introduce AgentStop, a lightweight efficiency supervisor that predicts and preemptively terminates trajectories unlikely to succeed. Leveraging low-cost execution signals, such as token-level log probabilities, AgentStop can reduce wasted energy by 15-20% with minimal impact on task performance (<5% utility drop) for challenging web-based question answering and coding benchmarks. These findings position predictive early termination as a practical mechanism for enabling sustainable, privacy-preserving LLM agents on user devices. Our project code and data are available at this https URL.

---


### 3. [TeamTR: Trust-Region Fine-Tuning for Multi-Agent LLM Coordination](https://arxiv.org/abs/2605.15207)

**<font color=#1a73e8>作者：</font>** Yi Xie, Siao Liu, Falong Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems have shown promise for complex reasoning, yet recent evaluations reveal they often underperform single-model baselines. We identify a structural failure mode in sequential fine-tuning of shared-context teams: updating one agent shifts the team's context distribution, and when subsequent updates are evaluated on cached rollouts, this mismatch compounds. We formalize this as the compounding occupancy shift and prove that stale-occupancy evaluation incurs a penalty that scales quadratically with the number of agents. In contrast, intermediate-occupancy evaluation reduces this to linear scaling. We propose TeamTR, a trust-region framework that resamples trajectories after each component update and enforces per-agent divergence control, yielding rigorous per-update and per-stage improvement lower bounds. Experiments show that TeamTR outperforms single-agent and sequential baselines with 7.1% on average, mitigates coordination regressions, and supports plug-and-play component replacement. Code is available at this https URL.

---


### 4. [Quantization Undoes Alignment: Bias Emergence in Compressed LLMs Across Models and Precision Levels](https://arxiv.org/abs/2605.15208)

**<font color=#1a73e8>作者：</font>** Plawan Kumar Rath, Rahul Maliakkal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models are routinely compressed via post-training quantization to reduce inference costs and memory footprint for cloud and edge deployment, yet the impact of this compression on model quality remains poorly understood. Existing studies typically compare only two conditions (full-precision vs. a single quantized variant), rely on aggregate bias metrics, and evaluate a single model family, making it impossible to distinguish gradual degradation from threshold-dependent safety failures. We conduct a controlled empirical study of three instruction-tuned models (Qwen2.5-7B, Mistral-7B, Phi-3.5-mini) at five precision levels (BF16 through 3-bit) on 12,148 BBQ bias benchmark items across 5 random seeds, totaling 911,100 inference records. Our results reveal that 3-bit quantization causes 6-21% of previously unbiased items to develop new stereotypical behaviors, following a clear dose-response pattern confirmed via logistic regression, while models' willingness to select "unknown" answers declines by 17.4%. Crucially, these item-level changes are invisible to standard quality metrics: perplexity increases by less than 0.5% at 8-bit and under 3% at 4-bit across all three models, yet 2.5-5.6% of items already develop new biases at 4-bit. These findings demonstrate that aggregate evaluation metrics systematically miss fairness-critical degradation, underscoring the need for quality-aware compression protocols that explicitly test for bias emergence before deployment.

---


### 5. [Fair outputs, Biased Internals: Causal Potency and Asymmetry of Latent Bias in LLMs for High-Stakes Decisions](https://arxiv.org/abs/2605.15217)

**<font color=#1a73e8>作者：</font>** Jagdish Tripathy, Marcus Buckmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Instruction-tuned language models exhibit behavioural fairness in high-stakes decisions while retaining biased associations in their internal representations. However, whether these suppressed representations can affect model outputs - and whether such causal potency is symmetric across demographic groups - remains unknown. We investigate the use of open-weight models for mortgage underwriting using matched applications that differ only in racially-associated names and reveal a critical disconnect: models show no output-level bias, yet retain and amplify demographic representations across model layers. Through activation steering and novel cross-layer interventions, we demonstrate that this suppressed information is decision-relevant: when reinjected at critical layers, it produces near-complete decision reversals. Critically, this latent bias is asymmetric - steering interventions affect decisions in one demographic direction, while producing minimal effects in reverse - and susceptible to adversarial prompt engineering and parameter-efficient fine-tuning. These findings demonstrate that behavioural audits focused on outputs are insufficient: fair outputs can mask exploitable internal biases. They also motivate dual-layer testing frameworks combining output evaluation with representational analysis for AI governance in high-stakes decisions.

---


### 6. [ICRL: Learning to Internalize Self-Critique with Reinforcement Learning](https://arxiv.org/abs/2605.15224)

**<font color=#1a73e8>作者：</font>** Jianbo Lin, Xiaomin Yu, Yi Xin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model-based agents make mistakes, yet critique can often guide the same model toward correct behavior. However, when critique is removed, the model may fail again on the same query, indicating that it has not internalized the critique's guidance into its underlying capability. Meanwhile, a frozen critic cannot improve its feedback quality over time, limiting the potential for iterative self-improvement. To address this, we propose learning to internalize self-critique with reinforcement learning(ICRL), a novel framework that jointly trains a solver and a critic from a shared backbone to convert critique-induced success into unassisted solver ability. The critic is rewarded based on the solver's subsequent performance gain, incentivizing actionable feedback. To address the distribution shift between critique-conditioned and critique-free behavior, ICRL introduces a distribution-calibration re-weighting ratio that selectively transfers critique-guided improvements compatible with the solver's own prompt distribution. Additionally, a role-wise group advantage estimation stabilizes joint optimization across the two roles. Together, these mechanisms ensure that the solver learns to improve itself without external critique, rather than becoming dependent on critique-conditioned behavior. We evaluate ICRL on diverse benchmarks spanning agentic and mathematical reasoning tasks, using Qwen3-4B and Qwen3-8B as backbones. Results show consistent improvements, with average gains of 6.4 points over GRPO on agentic tasks, and 7.0 points on mathematical reasoning. Notably, the learned 8B critic is comparable to 32B critics while using substantially fewer tokens. The code is available at this https URL.

---


### 7. [Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems](https://arxiv.org/abs/2605.15228)

**<font color=#1a73e8>作者：</font>** Jun He, Deying Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern cloud and enterprise systems rely on identity-centric authorization, assuming that callers possessing valid credentials are safe to execute commands. The emergence of autonomous AI agents invalidates this assumption: agents can generate syntactically valid but semantically unsafe actions, making standing privileges a significant operational risk. This risk becomes especially acute in sovereign AI systems, where autonomous agents may interact with cloud infrastructure, regulated data, financial workflows, and national-scale digital services. Governed mutation substrates reduce this risk by interposing on agent actions: agents submit intents, infrastructure evaluates context and policy, and execution is mediated. However, this shifts the trust boundary: how can the decision to authorize an intent be made verifiable, distributed, and replayable?
We introduce a Distributed Trust Framework (DTF), a verification framework for governed mutation systems that computes execution authority from structured, verifiable artifacts. DTF introduces a Justification Proof to encode the admissibility basis of an action, a consensus model for independent evaluation, an ephemeral Execution Identity derived from the approved proof, and an append-only Evidence Chain that preserves the authorization lifecycle. Under stated substrate assumptions, this architecture enforces a compact authorization invariant: no high-stakes execution without a proof object, no derived authority without consensus, and no valid mutation detached from evidence.
We define the model, instantiate it over an OpenKedge-based governed mutation substrate, and show how it maps onto cloud-native environments. By shifting authorization from standing identity to proof-derived authority, DTF provides an infrastructure foundation for making agentic execution governable, auditable, and bounded in sovereign AI deployments.

---


### 8. [MuteBench: Modality Unavailability Tolerance Evaluation for Incomplete Multimodal Fusion](https://arxiv.org/abs/2605.15235)

**<font color=#1a73e8>作者：</font>** Wugeng Zheng, Ziwen Kan, Tianlong Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal physiological data powers clinical AI systems from intensive care units to wearable devices, but sensors routinely fail in practice. Two failure modes are common: modality missing, where an entire channel is absent, and within-modality missing, where a contiguous time segment is lost. No existing benchmark evaluates multiple fusion architectures under both failure modes at controlled severity levels across diverse clinical datasets. We present MuteBench, a benchmark covering 9 datasets from 7 clinical domains, 6 fusion architectures, and 2 missing-data modes over 125,000 samples. Through this benchmark, we find that architecture family is the strongest predictor of robustness, outweighing parameter count. Channel-independent models tolerate modality missing well but can be sensitive to within-modality missing, especially on short sequences. Curriculum modality dropout protects reliably only up to the maximum dropout rate used in training. We also find that channel count, sequence length, and modality alignment jointly determine which failure mode poses the greater threat. Finally, a PTB-XL case study suggests that diffusion-based imputation can improve downstream classification under within-modality missing, with the largest gains for models whose expert routing is most sensitive to corrupted inputs, though broader validation across datasets remains an open direction. MuteBench provides practitioners with concrete guidance for both selecting existing architectures and informing the design of future robust multimodal fusion methods.

---


### 9. [Reducing the Safety Tax in LLM Safety Alignment with On-Policy Self-Distillation](https://arxiv.org/abs/2605.15239)

**<font color=#1a73e8>作者：</font>** Yu Fu, Longxuan Yu, Haz Sameen Shahgir 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety alignment often improves robustness to harmful queries at the cost of reasoning ability, a tradeoff known as the safety tax. A common cause is distributional mismatch: supervised fine-tuning trains the target model on safety demonstrations produced by humans, external models, or fixed self-generated traces, rather than on trajectories sampled from its own policy. We identify off-policy training mismatch as a second source of this tax and study on-policy self-distillation for safety alignment, which we call OPSA. The model generates its own rollouts and receives dense per-token KL supervision from a frozen teacher copy of itself conditioned on a privileged safety context. Because this teacher must be safer than the sampled student trajectory, we introduce \emph{teacher flip rate}: a criterion that measures how often a privileged context converts unsafe responses into safe ones. We use this signal to search for contexts that activate latent safety reasoning rather than merely elicit safe-looking demonstrations. Across two reasoning-model families and five model scales, OPSA achieves a stronger safety--reasoning tradeoff than off-policy self-distillation and external-teacher distillation under matched data and full-parameter fine-tuning, with the largest gains on smaller models (+8.85 points on R1-Distill-1.5B and +5.49 points on Qwen3-0.6B). The gains persist across training-set sizes and adaptive jailbreak evaluations. Token-level analyses further show that OPSA concentrates updates near early compliance-decision tokens, providing a mechanism for improving safety while preserving general reasoning.

---


### 10. [GQLA: Group-Query Latent Attention for Hardware-Adaptive Large Language Model Decoding](https://arxiv.org/abs/2605.15250)

**<font color=#1a73e8>作者：</font>** Fanxu Meng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-head Latent Attention (MLA), the attention used in DeepSeek-V2/V3, jointly compresses keys and values into a low-rank latent and matches the H100 roofline almost perfectly. Its trained weights, however, expose only one decoding path - an absorbed MQA form - which ties efficient inference to H100-class compute-bandwidth ratios, forfeits tensor parallelism along the head axis, and yields no Multi-Token Prediction (MTP) gain on commodity inference GPUs such as the export-restricted H20. We propose Group-Query Latent Attention (GQLA), a minimal modification of MLA whose trained weights expose two algebraically equivalent decoding paths over the same parameters: an MQA-absorb path identical to MLA's, and a GQA path with a per-group expanded cache. The runtime picks the path that matches the target hardware - no retraining, no custom kernels - so a single set of GQLA weights pins the rooflines of both H100 (MQA-absorb, s_q=1) and H20 (GQA + MTP, s_q=2), while supporting up to 8-way zero-redundancy tensor parallelism on the GQA path. To avoid pretraining from scratch we extend TransMLA into TransGQLA, which converts a pretrained GQA checkpoint into a GQLA model; on LLaMA-3-8B it compresses the per-token KV cache to 28.125% of the GQA baseline on the MQA-absorb path while structurally preserving GQA-level traffic on the per-group path.

---


### 11. [ReactiveGWM: Steering NPC in Reactive Game World Models](https://arxiv.org/abs/2605.15256)

**<font color=#1a73e8>作者：</font>** Zeqing Wang, Danze Chen, Zhaohu Xing 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current game world models simulate environments from a subjective, player-centric perspective. However, by treating the Non-Player Character (NPC) merely as background pixels, these models cannot capture interactions between the player and NPC. In that sense, they act as passive video renderers rather than real simulation engines, lacking the physical understanding needed to model action-induced NPC reactivities. We introduce ReactiveGWM, a reactive game world model that synthesizes dynamic interactions between the player and NPC. Instead of entangling all interaction dynamics, ReactiveGWM explicitly decouples player controls from NPC behaviors. Player actions are injected into the diffusion backbone via a lightweight additive bias, while high-level NPC responses (e.g., Offense, Control, Defense) are grounded through cross-attention modules. Crucially, these modules learn a game-agnostic representation of interactive logic. This enables zero-shot strategy transfer: our learned modules can be plugged directly into off-the-shelf, unannotated world models of different games. This instantly unlocks steerable NPC interactions without any domain-specific retraining. Evaluated on two Street Fighter games, ReactiveGWM maintains fine-grain player controllability while achieving robust, prompt-aligned NPC strategy adherence, paving the way for scalable, strategy-rich interaction with the NPC.

---


### 12. [Fluency and Faithfulness in Human and Machine Literary Translation](https://arxiv.org/abs/2605.15282)

**<font color=#1a73e8>作者：</font>** Sarah Griebel, Ted Underwood  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Literary translation requires balancing target-language fluency with faithfulness to the source. Recent large language models (LLMs) often produce fluent translations, but it remains unclear whether fluency corresponds to semantic preservation in literary text. We examine this relationship using 130,486 translated paragraphs from 106 novels in 16 source languages, including human, Google Translate, and TranslateGemma translations. Fluency is measured as original-likeness with a translationese classifier trained on paragraph part-of-speech n-grams, and faithfulness with the automatic translation evaluation metric COMET-KIWI. We control for paragraph length and find a consistent negative correlation between fluency and faithfulness. The pattern appears for both human and Google Translate, but is weaker and often non-significant for TranslateGemma. These results show that segment length matters for automatic evaluation and suggest a tradeoff between fluency and faithfulness in literary translation.

---


### 13. [Tadpole: Autoencoders as Foundation Models for 3D PDEs with Online Learning](https://arxiv.org/abs/2605.15284)

**<font color=#1a73e8>作者：</font>** Qiang Liu, Felix Koehler, Benjamin Holzschuh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Tadpole, a novel foundation model for three-dimensional partial differential equations (PDEs) that addresses key challenges in transferability, scalability to high dimensionality, and multi-functionality. Tadpole is pre-trained as an autoencoder on synthetic 3D PDE data generated by an efficient online data-generation framework. This enables large-scale, diverse training without storage or I/O overhead, demonstrated by scaling to an equivalent of hundreds of terabytes of training data. By autoencoding single-channel spatial crops, Tadpole learns rich and transferable representations across heterogeneous physical systems with varying numbers of state variables and spatial resolutions. Although pre-trained solely as an autoencoder, Tadpole can be efficiently applied for multiple downstream tasks beyond reconstruction, including dynamics learning and generative modeling. For dynamics learning, we propose a novel parameter-efficient fine-tuning strategy that integrates low-rank adaptation, latent-space transformations, and reintroduced skip connections, achieving accurate temporal modeling with a minimal number of trainable parameters. Tadpole demonstrates strong fine-tuning performance across various downstream tasks, highlighting its versatility and effectiveness as a foundation model for 3D PDE learning. Source code and pre-trained weights of Tadpole are available at this https URL

---


### 14. [Deep Pre-Alignment for VLMs](https://arxiv.org/abs/2605.15300)

**<font color=#1a73e8>作者：</font>** Tianyu Yu, Kechen Fang, Zihao Wan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most Vision Language Models (VLMs) directly map outputs from ViT encoders to the LLM via a lightweight projector. While effective, recent analysis suggests this architecture suffers from an alignment challenge: visual features remain distant from the text space in the initial layers of the LLM, forcing the model to waste critical depth~\cite{zhang-etal-2024-investigating,artzy-schwartz-2024-attend} on superficial modality alignment rather than deep understanding and complex reasoning. In this work, we propose Deep Pre-Alignment (DPA), a novel architecture that replaces the standard ViT encoder with a small VLM as perceiver, ensuring visual features are deeply aligned with the text space of the target large language model. Comprehensive experiments demonstrate the effectiveness of DPA. On the 4B parameter scale, DPA outperforms baselines by 1.9 points across 8 multimodal benchmarks, with gains widening to 3.0 points at the 32B scale. Moreover, by offloading alignment to the perceiver, DPA achieves a 32.9\% reduction in language capability forgetting over 3 text benchmarks. We further demonstrate that these gains are consistent across different LLM families including Qwen3 and LLaMA 3.2, highlighting the generality of our approach. Beyond performance, DPA also offers a seamless upgrade path for current VLM development, requiring only a modular replacement for the visual encoder with marginal computation overhead.

---


### 15. [Solvita: Enhancing Large Language Models for Competitive Programming via Agentic Evolution](https://arxiv.org/abs/2605.15301)

**<font color=#1a73e8>作者：</font>** Han Li, Jinyu Tian, Rili Feng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) still struggle with the rigorous reasoning demands of hard competitive programming. While recent multi-agent frameworks attempt to bridge this reliability gap, they remain fundamentally stateless: they rely on static retrieval and discard the valuable problem-solving and debugging experience gained from previous tasks. To address this, we present Solvita, an agentic evolution framework that enables continuous learning without requiring weight updates to the underlying LLM. Solvita reorganizes problem-solving into a closed-loop system of strategy selection, program synthesis, certified supervision, and targeted hacking, executed by four specialized agents: Planner, Solver, Oracle, and Hacker. Crucially, each agent is paired with a trainable, graph-structured knowledge network. As the system operates, outcome signals, such as pass/fail verdicts, test certification quality, and adversarial vulnerabilities discovered by the Hacker, are recast as reinforcement learning updates to these network weights. This allows the agents to dynamically route future queries based on past successes and failures, effectively accumulating transferable reasoning experience over time. Evaluated across CodeContests, APPS, AetherCode, and live Codeforces rounds, Solvita establishes a new state-of-the-art among code-generation agents, outperforming existing multi-agent pipelines and nearly doubling the accuracy of single-pass baselines.

---


### 16. [Multimodal Object Detection Under Sparse Forest-Canopy Occlusion](https://arxiv.org/abs/2605.15326)

**<font color=#1a73e8>作者：</font>** Nitik Jain, Mangal Kothari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable detection of humans beneath forest canopy remains a difficult remote-sensing challenge due to sparse, structured, and viewpoint-dependent occlusion. This paper presents a multimodal proof-of-concept pipeline that integrates three complementary approaches: (i) experimental evaluation of LiDAR returns through vegetation to assess the feasibility of active sensing, (ii) visible--thermal image fusion using a multi-scale transform and sparse-representation framework to enhance human saliency, and (iii) synthetic-aperture image formation via Airborne Optical Sectioning (AOS) to suppress canopy clutter. A YOLOv5 detector is fine-tuned on the Teledyne FLIR thermal dataset and evaluated on thermal and fused imagery. Results show that the tested terrestrial LiDAR configuration provides limited penetration for object-level detection, while visible--thermal fusion improves target visibility in low-contrast scenes and AOS enhances ground-plane detection in synthetic forest imagery. The fine-tuned YOLOv5 achieves a mean average precision of $\sim$0.83 on the top three FLIR classes. These findings establish an initial baseline for UAV-deployable search-and-rescue and surveillance systems operating in forested environments, and motivate future work on dedicated forest datasets and real-time multimodal integration.

---


### 17. [Zero-Shot Goal Recognition with Large Language Models](https://arxiv.org/abs/2605.15333)

**<font color=#1a73e8>作者：</font>** Kin Max Piamolini Gusmão, Nathan Gavenski, Nir Oren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have recently reached near-parity with classical planners on well-known planning domains, yet this competence relies on world-knowledge exploitation rather than genuine symbolic reasoning. Goal recognition is a complementary abductive task structurally better suited to LLM strengths: it consists of evaluating consistency with world knowledge rather than generating novel action sequences. This paper provides the first systematic zero-shot evaluation of frontier LLMs as goal recognisers on key classical PDDL benchmarks. Our results show that LLM competence on goal recognition is uneven: some models scale with evidence and approach landmark-based accuracy at full observations, while others remain anchored to world-knowledge priors regardless of how much evidence accumulates. Qualitative analysis of model reasoning traces reveals that this divergence reflects a fundamental difference in evidence integration rather than domain familiarity. These findings position goal recognition as a principled benchmark for the foundational planning knowledge of LLMs.

---


### 18. [LEAP: Trajectory-Level Evaluation of LLMs in Iterative Scientific Design](https://arxiv.org/abs/2605.15341)

**<font color=#1a73e8>作者：</font>** Marilyn Zhang, Tianfeng Chen, Fabián Barzuna 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly deployed in autonomous laboratories, under the assumption that their domain priors and reasoning over iterative feedback let them converge on good designs in fewer iterations than feedback-only baselines. Current iterative scientific design benchmarks, however, score only outcome snapshots at fixed horizons. This leaves the learning trajectory unmeasured, even though the trajectory is what captures learning efficiency, where each iteration saved is a real saving in cost and time. Motivated by this, we examine three evaluation choices that change the conclusions one draws about LLM learning efficiency in iterative scientific design: what to measure, what baseline to compare against, and what to ground against. We introduce LEAPBench, Learning Efficiency in Adaptive Processes, a 55-task framework that pairs a best-so-far area under the curve (AUC) trajectory metric with a classical Bayesian-optimization reference and an audit grounded in published literature. Applied to eight contemporary LLMs, switching from final-outcome to trajectory scoring changes the best-model decision on 53% of tasks at matched horizons, and exposes efficiency gains overlooked by outcome-based scoring. LLMs do not outperform a classical Bayesian baseline. On 16 biology tasks where the oracle's reward signal is aligned with configurations from the published-best design, domain-aware prompting leads to LLM choices that match the published-best's approximately 10 percentage points less often than domain-agnostic prompting at iteration 30. The pattern is sharpest on 6 tasks where the literature-typical and published-best configurations diverge, and domain-agnostic prompting matches the published-best more often on all 6. The trajectory metric also doubles as a tractable training target. Offline reinforcement learning with the metric as a reward improves performance on 14 of 21 held-out tasks.

---


### 19. [Belief Engine: Configurable and Inspectable Stance Dynamics in Multi-Agent LLM Deliberation](https://arxiv.org/abs/2605.15343)

**<font color=#1a73e8>作者：</font>** Joshua C. Yang, Maurice Flechtner, Damian Dailisan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly used to simulate deliberative interactions such as negotiation, conflict resolution, and multi-turn opinion exchange. Yet generated transcripts often do not reveal why an agent's stance changes: movement may reflect evidence uptake, anchoring, role drift, echoing, or changed prompt and retrieval context. We introduce the Belief Engine (BE), an auditable belief-update layer that treats "belief" as an evidential state over a proposition and exposes it as scalar stance. BE extracts arguments into structured memory and updates stance with a log-odds rule controlled by evidence uptake u and prior anchoring a. Across multiple base LLMs, parameter sweeps show that these controls reliably shape stance dynamics while preserving an evidence-level update trail. On DEBATE, a human deliberation dataset with pre/post opinions, BE best reconstructs participants whose final stance follows extracted evidence; stable and evidence-opposed cases instead point to anchoring or factors outside the extracted evidence stream. BE provides configurable infrastructure for studying evidence-grounded deliberation, where openness, commitment, convergence, and disagreement can be tied to explicit update assumptions rather than hidden prompt effects.

---


### 20. [Controllable Molecular Generative Foundation Models](https://arxiv.org/abs/2605.15354)

**<font color=#1a73e8>作者：</font>** Yihan Zhu, Yuhan Liu, Weijiang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the success of foundation models in language and vision, molecular graph generation still lacks a unified framework for heterogeneous design tasks with reliable controllability. While reinforcement learning (RL) offers a natural post-training mechanism for task-specific optimization, applying it to graph generative models is hindered by the vast atom-wise action spaces and chemically invalid intermediate states. We propose \textbf{Co}ntrollable \textbf{Mole}cular Generative Foundation Models (CoMole), built with a unified motif-aware graph diffusion pipeline. By learning a motif-aware graph space, CoMole transfers pretrained structural priors into controllable generation, where RL optimizes conditional reverse policies over chemically meaningful decisions. We theoretically characterize the bottleneck of atom-level RL and justify motif-aware policy optimization. Across three heterogeneous benchmarks spanning materials and drug discovery, CoMole ranks first in controllability on all nine targets, reduces MAE by up to 48.2% relative to the strongest baselines, and maintains validity above 0.94 without rule-based correction or post-hoc filtering. We further show that CoMole transfers controllability to unseen properties by optimizing only task embeddings with the generator frozen, achieving performance competitive with strong task-specific baselines.

---


### 21. [Is One Score Enough? Rethinking the Evaluation of Sequentially Evolving LLM Memory](https://arxiv.org/abs/2605.15384)

**<font color=#1a73e8>作者：</font>** Songwei Dong, Zihan Chen, Chengshuai Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memory plays a central role in enabling large language models (LLMs) to operate over sequential tasks by accumulating and reusing experience over time. However, existing evaluations of LLM memory mostly rely on aggregate metrics such as final hold-out accuracy or cumulative online performance, which can obscure critical failure modes such as forgetting and negative transfer. In this paper, we introduce SeqMem-Eval, a diagnostic evaluation framework for sequentially evolving LLM memory. Drawing inspiration from continual learning, it targets a test-time setting in which memory is external, prompt-mediated, and updated without modifying model parameters. Rather than focusing only on final performance, SeqMem-Eval evaluates how memory states evolve, generalize, consolidate experience, and retain useful information during sequential inference. Specifically, it measures online utility, hold-out generalization, backward transfer, and forgetting, providing a finer-grained view of memory quality. Through extensive experiments across diverse tasks and memory methods, we show that higher final or cumulative accuracy does not necessarily imply better memory quality: many methods exhibit strong performance gains while suffering from substantial forgetting or negative transfer. Moreover, different memory designs exhibit distinct trade-offs between adaptability and stability that remain invisible under standard evaluation metrics.

---


### 22. [PanoWorld: Geometry-Consistent Panoramic Video World Modeling](https://arxiv.org/abs/2605.15391)

**<font color=#1a73e8>作者：</font>** Le Jiang, Xiangyu Bai, Bishoy Galoaa 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PanoWorld, a panoramic video world model that generates geometry-consistent 360$\degree$ video from a single image and a caption. Existing panoramic video methods optimize primarily for visual realism and do not explicitly constrain the underlying 3D scene state, producing outputs that appear plausible yet exhibit inconsistent depth, broken correspondences, and implausible motion across the spherical surface. We address this gap by framing panoramic video generation as a geometry- and dynamics-consistent latent state modeling problem rather than pure visual synthesis. Building on a pre-trained perspective video world model, we introduce two lightweight regularizers: a depth consistency loss against pseudo ground-truth panoramic depth, and a trajectory consistency loss that supervises the 3D world-frame positions of tracked points across time. We further apply spherical-geometry-aware adaptation to the conditioning and positional encoding. We additionally introduce PanoGeo, a unified geometry-aware panoramic video dataset with consistent depth, trajectory, and prompt annotations across diverse real and synthetic sources, used for both training and stratified evaluation. Experiments show that PanoWorld improves geometric consistency over prior panoramic generation methods while maintaining competitive visual realism, establishing that panoramic video generation must be treated as a geometric modeling problem to support the holistic spatial understanding requirements of embodied AI applications. Code is available at this https URL.

---


### 23. [LPDS: Evaluating LLM Robustness Through Logic-Preserving Difficulty Scaling](https://arxiv.org/abs/2605.15393)

**<font color=#1a73e8>作者：</font>** Philipp Mondorf, Samuel J. Bell, Jesse Dodge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed to perform tasks with minimal human oversight, it is crucial that these models operate robustly. In particular, a model that can solve a given problem should not fail simply because certain entities$\unicode{x2013}$such as names, numbers, or other contextual details$\unicode{x2013}$have changed while the underlying problem logic remains the same. Prior work suggests that current LLMs still struggle with this form of robustness: they often succeed on some variations of a problem but fail on others. However, existing evaluations often lack a systematic way to identify which logic-preserving variations are most likely to induce failure. Instead, they typically test a random subset of allowable variations, which can overstate robustness. To address this gap, we introduce logic-preserving difficulty scaling (LPDS), a framework that (i) quantifies the difficulty of a problem variation and (ii) systematically searches the space of allowable variations to find those that maximize difficulty and expose failures. We show that as difficulty increases, performance declines and errors in the models' reasoning chains become more pronounced. We further demonstrate that LPDS efficiently finds difficult problem variations for a model, resulting in performance drops up to 5 times larger compared to random sampling. Finally, we show that fine-tuning on more difficult variations leads to more consistent robustness gains than training on easier ones.

---


### 24. [Representation Without Reward: A JEPA Audit for LLM Fine-Tuning](https://arxiv.org/abs/2605.15394)

**<font color=#1a73e8>作者：</font>** Biswa Sengupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive architectures (JEPAs) propose that a model should learn more useful abstractions when trained to predict latent representations rather than observed outputs. For autoregressive language-model fine-tuning the principle entails a stricter requirement: the induced hidden-state geometry must reach the language-model head \emph{and} improve the decoded task metric. We test that requirement under a fixed Llama-3.2-1B-Instruct LoRA harness on natural-language-to-regex generation, comparing twenty-two training-time auxiliaries across trajectory-shape regularisation, distributional constraints, predictor/target asymmetry, Fisher-metric Jacobi residuals, and a decoder-visible JEPA objective constructed to lie in cross-entropy's positive cone. The empirical answer is a structured null: several auxiliaries clear single-cell paired $\alpha = 0.10$ without correction (T3-Local at $\Delta = +2.53$~pp, $p = 0.003$ being the strongest), but none survives Bonferroni or Holm--Bonferroni at the relevant family-wise threshold, even though many change curvature, anisotropy, variance, and gradient direction. Decoder-visible JEPA yields the first positive auxiliary--cross-entropy gradient cosine in the study, yet exact match remains inside seed noise; a full-fine-tuning replication of the same auxiliary at $n = 5$ seeds reproduces the null on both benchmarks (TURK: $\Delta = +0.04$~pp, $p_{\text{paired}} = 0.96$; SYNTH: $\Delta = +0.52$~pp, $p_{\text{paired}} = 0.28$), so the null is robust across LoRA and full fine-tuning for the decoder-visible construction. Hidden-state representation work and decoded-task accuracy are therefore weakly coupled in this regime; we accordingly reframe LLM-domain JEPA evaluation as a coupling problem, in which the operative question is under which metrics useful hidden geometry becomes decoder-visible task signal.

---


### 25. [ELDOR: A Dataset and Benchmark for Illegal Gold Mining in the Amazon Rainforest](https://arxiv.org/abs/2605.15397)

**<font color=#1a73e8>作者：</font>** Kangning Cui, Surendra Bohara, Suraj Prasai 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Illegal gold mining in the Amazon rainforest causes deforestation, water contamination, and long-term ecosystem disruption, yet remains difficult to monitor at fine spatial scales. Satellite imagery supports large-scale observation, but often misses small mining-related structures and subtle land-cover transitions, especially under frequent cloud cover. We introduce ELDOR, a large-scale UAV benchmark for monitoring environmental and landscape disturbance from illegal gold mining in the rainforest. ELDOR contains manually annotated orthomosaic imagery covering over 2,500 hectares, with pixel-level semantic labels for both mining-related activities and surrounding ecological structures. With this unified annotation source, we establish four benchmark tasks: semantic segmentation, segmentation-derived recognition, direct multi-label classification, and class-presence recognition with vision-language models. Across these tasks, we compare generic and remote-sensing-specific segmentation models, vision foundation model-related segmentation methods, direct multi-label classification methods, and vision-language models under a controlled closed-set protocol. Results show that current methods still struggle with rare small-scale mining structures and fine-grained recovery classes, suggesting the need for context-aware and multimodal modeling. To support domain analysis and practical use, we further build an interactive explorer for domain experts that provides a unified interface for data exploration and model inference.

---


### 26. [Capability Conditioned Scaffolding for Professional Human LLM Collaboration](https://arxiv.org/abs/2605.15404)

**<font color=#1a73e8>作者：</font>** Sen Yang, Yinglei Ma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model personalization typically adapts outputs to user preferences and style but does not account for differences in user evaluation capacity across domains of expertise. This limitation can encourage Professional Domain Drift, where users rely on AI generated reasoning in domains they cannot reliably evaluate. We introduce Capability Conditioned Scaffolding, a typed framework that partitions expertise into strong, mixed, and weak domains and conditions intervention behavior on structured capability profiles. A pilot evaluation across multiple MMLU subsets and four LLM substrates shows consistent profile conditioned intervention behavior, including categorical inversion under profile swapping and selective activation in mixed domain risk zones. These findings suggest that capability aware scaffolding can support more reliable professional human AI collaboration beyond stylistic personalization.

---


### 27. [Transformer Scalability Crisis: The First Comprehensive Empirical Analysis of Performance Walls in Modern Language Models](https://arxiv.org/abs/2605.15413)

**<font color=#1a73e8>作者：</font>** Mahdi Naser Moghadasi, Faezeh Ghaderi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the remarkable success of transformer architectures in natural language processing, their scalability limitations remain poorly understood through systematic empirical analysis. This paper presents the first comprehensive large-scale evaluation of 118 transformer models across seven distinct architectural categories, revealing fundamental performance walls that manifest as hard deployment constraints. Our systematic benchmarking methodology uncovers a critical scalability crisis: while 88.1% of models successfully process sequences up to 512 tokens, this drops dramatically to 44.9% at 1024 tokens, with complete failure (0%) at 2048 tokens. Through rigorous analysis of loading times, memory consumption, and computational efficiency across sequence lengths from 128 to 2048 tokens, we demonstrate that compressed models achieve superior parameter efficiency (649.2 tokens/sec/M parameters) compared to large generative models (12.5 tokens/sec/M). Our findings challenge prevailing scaling assumptions and provide the first quantitative evidence that the theoretical O(n2) attention complexity translates into measurable performance walls. This work establishes new benchmarking methodologies for transformer evaluation and provides critical insights for practical deployment decisions in production environments.

---


### 28. [Margin-Adaptive Confidence Ranking for Reliable LLM Judgement](https://arxiv.org/abs/2605.15416)

**<font color=#1a73e8>作者：</font>** Gaojie Jin, Yong Tao, Lijia Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Jung et al. (2025) introduce a hypothesis testing framework for guaranteeing agreement between large language models (LLMs) and human judgments, relying on the assumption that the model's estimated confidence is monotonic with respect to human-disagreement risk. In practice, however, this assumption may be violated, and the generalization behavior of the confidence estimator is not explicitly analyzed. We mitigate these issues by learning a dedicated confidence estimator instead of relying on heuristic confidence signals. Our approach leverages simulated annotator diversity and a margin-based ranking formulation to explicitly model how confidently an LLM distinguishes between human-agreement and human-disagreement cases. We further derive generalization guarantees for this estimator, revealing a margin-dependent trade-off that informs the design of an adaptive estimator training procedure. When integrated into fixed-sequence testing, the learned confidence estimator yields improved ranking accuracy and empirically strengthens the monotonic relationship between confidence and disagreement risk, leading to higher success rates in satisfying target agreement levels across multiple datasets and judge models.

---


### 29. [$f$-Trajectory Balance: A Loss Family for Tuning GFlowNets, Generative Models, and LLMs with Off- and On-Policy Data](https://arxiv.org/abs/2605.15417)

**<font color=#1a73e8>作者：</font>** Jake Fawkes, Jason Hartford  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In GFlowNets and variational inference, it has been shown that the mean square error between target and model log probabilities is an effective, low variance, surrogate loss for training generative models.
This loss has the property that when evaluated \emph{on-policy} its gradients correspond to those of the KL divergence, while \emph{off-policy} it remains a valid loss with the same global minimizer. In this work, we demonstrate that this construction can be extended to the whole family of $f$-divergences, leading to a family of losses whose on-policy gradients are that of the corresponding $f$-divergence, but retain the same global minimizer off-policy. Specifically, we show that the on-policy gradients lead to a one to one correspondence between translation invariant loss functions on the target and model log probabilities, and $f$-divergences. This equivalence allows us to design new surrogate loss functions for tuning a wide class of generative models that inherit the properties of the corresponding $f$-divergence, such as being more mode covering, whilst being applicable to off-policy data. We apply our losses on a range of tasks, including classic synthetic examples, SynFlowNets for molecule discovery, and asynchronous large language model (LLM) tuning, demonstrating that our models retain their predicted properties on- and off-policy in a wide class of generative models.

---


### 30. [Neural Activation Patterns Across Language Model Architectures: A Comprehensive Analysis of Cognitive Task Performance](https://arxiv.org/abs/2605.15436)

**<font color=#1a73e8>作者：</font>** Mahdi Naser-Moghadasi, Faezeh Ghaderi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a comprehensive analysis of neural activation patterns across six distinct large language model (LLM) architectures, examining their performance on twelve cognitive task categories. Through systematic measurement of final activation values, attention entropy, and sparsity patterns, we reveal fundamental differences in how encoder and decoder architectures process diverse cognitive tasks. Our analysis of 144 task-model combinations demonstrates that mathematical reasoning consistently produces the highest attention entropy across all architectures, while decoder models exhibit significantly higher sparsity patterns compared to encoder models. The findings provide critical insights into the computational characteristics of modern language models and their task-specific neural behaviors, with implications for model selection and optimization in big data applications.

---


### 31. [Why are language models less surprised than humans? Testing the Parse Multiplicity Mismatch Hypothesis](https://arxiv.org/abs/2605.15440)

**<font color=#1a73e8>作者：</font>** William Timkey, Brian Dillon, Tal Linzen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Surprisal theory posits that the processing difficulty of a word is determined by its predictability in context, offering a potential link between human sentence processing and next-word predictions from language models. While language model (LM) surprisals successfully predict reading times in naturalistic text, they systematically underpredict the magnitude of difficulty observed in controlled studies of syntactic ambiguity, particularly in garden path sentences. This mismatch might arise from differences in the computational constraints between humans and LMs. Here we test one such hypothesis, specifically, that LMs may be able to simultaneously consider a greater number of distinct sentence interpretations at once, compared to humans. Using Recurrent Neural Network Grammars (RNNGs) with word-synchronous beam search, we systematically vary the number of simultaneous parses used to compute word surprisal, and then use these surprisals to predict human reading times. Reducing the number of simultaneous active parses indeed increases the magnitude of predicted garden path effects, but not nearly enough to capture the full magnitude of the effects in humans. This suggests that differences in the number of simultaneous parses available to LMs and humans cannot reconcile LM-based surprisal with human sentence processing.

---


### 32. [From LLM-Generated Conjectures to Lean Formalizations: Automated Polynomial Inequality Proving via Sum-of-Squares Certificates](https://arxiv.org/abs/2605.15445)

**<font color=#1a73e8>作者：</font>** Ruobing Zuo, Hanrui Zhao, Gaolei He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated proving of polynomial inequalities is a fundamental challenge in automated mathematical reasoning, where rich algebraic structure and a rapidly growing certificate search space hinder scalability. Purely symbolic approaches provide strong guarantees but often scale poorly as the number of variables or the degree increases, due to expensive algebraic manipulations and rapidly growing intermediate expressions. In parallel, LLM-guided methods have made notable progress, particularly on competition-style inequalities with a small number of variables. To address the remaining scalability challenges, we propose NSPI, a neuro-symbolic framework that combines the complementary strengths of LLMs and symbolic computation for polynomial-inequality proving. Concretely, an LLM proposes a conjecture in the form of an approximate polynomial Sum-Of-Squares (SOS) decomposition; we refine it via symbolic computation to obtain an exact polynomial SOS representation, which directly proves the target inequality, and we further certify the proof in Lean, yielding an end-to-end pipeline from heuristic discovery to machine-checked proof. Experiments on challenging benchmarks involving polynomials with up to 10 variables demonstrate the effectiveness and scalability of the proposed method.

---


### 33. [Reasoning Models Don't Just Think Longer, They Move Differently](https://arxiv.org/abs/2605.15454)

**<font color=#1a73e8>作者：</font>** Anders Gjølbye, Lars Kai Hansen, Sanmi Koyejo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning-trained language models often spend more tokens on harder problems, but longer chains of thought do not show whether a model is merely computing for more steps or following a different internal trajectory. We study this distinction through hidden-state trajectories during chain-of-thought generation across competitive programming, mathematics, and Boolean satisfiability. Raw trajectory geometry is strongly shaped by generation length: longer generations mechanically alter path statistics, so difficulty-dependent comparisons are misleading without adjustment. After residualizing trajectory statistics on length, difficulty remains systematically coupled to corrected trajectory geometry across all domains studied. The clearest reasoning-specific separation appears in the code domain, where harder problems show more direct corrected trajectories and less heterogeneous local curvature in reasoning-trained models than in matched instruction-tuned baselines. Corrected difficulty-geometry coupling is weaker, but still present, in mathematics and Boolean satisfiability. Prompt-stage linear probes do not mirror the code-domain separation, and behavioral annotations show that stronger corrected coupling co-occurs with strategy shifts and uncertainty monitoring. Together, these findings establish length correction as a prerequisite for generation-time trajectory analysis and show that reasoning training can be associated with distinct corrected trajectory geometry, with the strength of the effect depending on the domain.

---


### 34. [Multi-Turn Neural Transparency: Surfacing Neural Activations Improves User Calibration to LLM Behavioral Drift](https://arxiv.org/abs/2605.15455)

**<font color=#1a73e8>作者：</font>** Sheer Karny, Anthony Baez, Pat Pataranutaporn  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Chatbot behavior is often opaque to users, as responses can shift unpredictably across a conversation, drifting toward sycophancy, toxicity, or other unsafe responses. This can leave users vulnerable, either being misled by overly agreeable AI or manipulated by a harmful chatbot that no longer behaves as intended. To address this, we introduce multi-turn neural transparency, an interface that surfaces an LLM's internal neural activations in real time to help users anticipate and recognize how behaviors change across turns. We construct behavioral vectors for six personality traits using methods from mechanistic interpretability, identifying directions in activation space that correlate with trait expression ($R^2 \geq 0.9$) via contrastive system prompts, and visualize trait expression using a sunburst and drift panel that updates at each turn. In a randomized controlled study (N = 246), participants predicted trait expression from a system prompt alone, then rated observed behavior after interacting with the chatbot for both assistant and role-play personas. We find that participants without visualization struggled to accurately evaluate traits (RMSE $\approx$ 0.6-0.7), while the inclusion of neural transparency significantly improved both anticipation and evaluation compared to no visualization (d = -0.34 to -0.49). The multi-turn dynamic visualization additionally outperformed the static single-turn visualization on holistic evaluation of model behavior (d = -0.32). Transparency also reduced overconfidence: participants without visualization grew more confident despite no gain in accuracy. These findings suggest that surfacing internal model representations to everyday users is a meaningful step toward more transparent and informed human-AI interaction.

---


### 35. [GRLO: Towards Generalizable Reinforcement Learning in Open-Ended Environments from Zero](https://arxiv.org/abs/2605.15464)

**<font color=#1a73e8>作者：</font>** Shangjian Yin, Yu Fu, Yue Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training has become a crucial step for unlocking the capabilities of large language models, with reinforcement learning (RL) emerging as a critical paradigm. Recent RL-based post-training has increasingly split into two paradigms: reinforcement learning from human feedback (RLHF), which optimizes models using human preference signals in target domains, and reinforcement learning from verifiable rewards (RLVR), which operates in verifier-backed environments. The latter has dominated recent reasoning-oriented post-training because it delivers stronger gains and higher efficiency on domain-specific tasks (e.g., reasoning). However, although in-domain RL training achieves promising performance, it still requires a substantial amount of GPU compute, which remains a major barrier to broad adoption. In this work, we study the generalization ability of RLHF learned from scratch from a small set of interactions in open-ended environments, and investigate whether the conversational abilities it explicitly acquires can implicitly transfer to downstream tasks such as mathematical reasoning and code generation, namely GRLO. Specifically, on Qwen3-4B-Base backbone, GRLO improves the average performance across all domains from 24.1 to 63.1 with only 5K prompts and 22.7 GPU hours, requiring about $46\times$ less data and $68\times$ less compute than a strong in-domain RLVR baseline. The resulting model is even competitive with Qwen's released post-trained models which required a much larger training cost. Notably, a subsequent in-domain RLVR stage brings only selective gains, mainly on harder competition-math benchmarks. We hope GRLO offers a simple and efficient recipe for building broadly capable post-trained models. Our code and data will be available at: \href{this https URL}{this https URL}.

---


### 36. [Toward World Modeling of Physiological Signals with Chaos-Theoretic Balancing and Latent Dynamics](https://arxiv.org/abs/2605.15465)

**<font color=#1a73e8>作者：</font>** Yunfei Luo, Xi Chen, Yuliang Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physiological time series signals reflect complex, multi-scale dynamical processes of the human body. Existing modeling studies focus on static tasks such as classification, event forecasting, or short-horizon next step prediction, while long-horizon signal-level forecasting and predictive nature of physiological signals remain underexplored. We introduce NormWear-2, a world model that encodes both multivariate physiological signals and clinical intervention variables into a shared latent space and models their joint temporal evolution as a dynamical system. Our approach combines inference from prior pre-trained knowledge (intuition) with instant non-parametric latent state transition adaptation (insight), enabling coherent forecasting across multiple temporal scales, conditioned on heterogeneous clinical interventions. During the pretraining phase, we find that chaos-theoretic balancing of dynamical regime diversity yields more robust representations, with a smaller balanced corpus outperforming one twice its size and capturing bifurcation regimes. We evaluate the world model performance across diverse real-world physiological datasets spanning heterogeneous temporal resolutions and intervention regimes, covering daily life, point-of-care, and clinical settings, including fitness planning, hemodialysis, diabetes management, and surgical monitoring. These evaluation datasets comprise records from 8,026 subjects, spanning study durations from 3.2 hours for high-resolution signal data to 2.3 years for longitudinal clinical biomarker tracking. NormWear-2 achieves the best overall forecasting performance across time, frequency, and latent representation domains, with significant improvements over state-of-the-art time series foundation models, while maintaining competitive downstream representation quality, providing a step toward general-purpose world models for physiological signals.

---


### 37. [Entity-Centric World Models: Interaction-Aware Masking for Causal Video Prediction](https://arxiv.org/abs/2605.15466)

**<font color=#1a73e8>作者：</font>** Santosh Kumar Paidi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning predictive world models from unlabelled video is a foundational challenge in artificial intelligence. While Joint Embedding Predictive Architectures (JEPA) have set new benchmarks in semantic classification, they often remain physics-blind, failing to capture the causal dynamics necessary for downstream reasoning. We hypothesize that this stems from standard patch-based masking strategies, which prioritize visual texture over rare but informative kinematic events. We propose Interaction-Aware JEPA (IA-JEPA), which utilizes a self-supervised motion-centric masking strategy to prioritize physical interactions. By specifically targeting entities engaged in collisions or momentum transfers, we force the architecture to reconstruct latent trajectories rather than static background features. Evaluated on the CLEVRER benchmark, IA-JEPA achieves 14.26% accuracy on causal reasoning tasks, a significant lead over the 3.22% achieved by standard patch-masked baselines. Crucially, we demonstrate that IA-JEPA breaks the "static bias" of standard self-supervision by inducing a higher-entropy, more discriminative latent space (+10% entropy gain) that linearizes physical energy ($R^2=0.43$). We show that this interaction bias generalizes to real-world human actions (Something-Something V2) and zero-shot physical puzzles (PHYRE-Lite). Our results provide a scalable, fully self-supervised path toward building foundational world models that begin to internalize the causal structure of the physical world.

---


### 38. [Retrieval-Augmented Large Language Models for Schema-Constrained Clinical Information Extraction](https://arxiv.org/abs/2605.15467)

**<font color=#1a73e8>作者：</font>** A H M Rezaul Karim, Ozlem Uzuner  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational nurse-patient transcripts contain actionable observations, but converting these transcripts into structured representations at scale remains challenging. Documentation burden is substantial, with prior studies showing clinicians spend large portions of their workday on documentation and related desk work rather than direct patient care. MEDIQA-SYNUR focuses on observation extraction from conversational nurse-patient transcripts, requiring systems to normalize these narratives into a predefined schema with value-type constraints. We propose a modular retrieval-augmented generation (RAG) pipeline that uses the training set as an exemplar corpus, combines schema-constrained prompting (full schema vs. pruned candidate schema), deterministic schema-based postprocessing, and a second-pass audit, with two LLM backbones: Llama-4-Scout-17B-16E-Instruct and GPT-5.2 with corresponding embedding models for RAG. Our best configuration uses GPT-5.2 with full schema, RAG, and a second-pass auditing, achieving 80.36% F1 score. Overall, our results show that RAG consistently improves performance, while the optimal degree of schema constraint depends on the model, and second-pass auditing yields modest additional gains by correcting residual schema-adherence errors.

---


### 39. [EgoExo-WM: Unlocking Exo Video for Ego World Models](https://arxiv.org/abs/2605.15477)

**<font color=#1a73e8>作者：</font>** Danny Tran, Roberto Martín-Martín, Kristen Grauman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric world models present a promising direction for enabling agents to predict and plan, but their performance is constrained by the limited availability of egocentric training data and its inherent partial observability of humans' physical actions. In contrast, exocentric video is abundant and reveals body poses well, but lacks direct alignment with an agent's action space -- and is not egocentric. We propose a method to bridge this gap by extracting structured body pose from exocentric video as a representation of action and transforming the exocentric video to egocentric video, informed by a human kinematics prior. This process unlocks the integration of in-the-wild exocentric data for egocentric world model training. We show that training whole-body action-conditioned egocentric world models with our converted data significantly improves both prediction quality and downstream planning performance, where we infer the sequence of body poses needed to achieve a visual goal state. Our approach paves the way to enlist arbitrary in-the-wild videos for building powerful egocentric world models, furthering applications in robot planning and augmented-reality guidance.

---


### 40. [FINESSE-Bench: A Hierarchical Benchmark Suite for Financial Domain Knowledge and Technical Analysis in Large Language Models](https://arxiv.org/abs/2605.15482)

**<font color=#1a73e8>作者：</font>** Dmitry Stanishevskii, Nini Kamkia, Alexey Khoroshilov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly being applied to financial analysis, reporting, investment decision support, risk management, compliance, and professional training. However, robust evaluation of their domain competence in finance remains incomplete. Widely used open benchmarks such as FinQA, ConvFinQA, and TAT-QA have played an important role in advancing financial question answering and numerical reasoning, but they focus primarily on question answering over financial reports and do not provide an explicit hierarchy of professional difficulty. Broader resources, including FinanceBench, PIXIU, FinBen, and FLaME, expand the coverage of financial tasks, yet the problem of evaluating the transition from foundational knowledge to expert-level financial reasoning remains open. In this work, we present FINESSE-Bench, a suite of eight specialized benchmarks comprising 3,993 questions for hierarchical evaluation of financial competencies in LLMs. FINESSE-Bench combines exam-oriented datasets inspired by professional certifications (CFA-like Levels 1-3, CMT-like Level 2, and CFTe-like Level 1), applied trading task collections, and a Russian-language olympiad benchmark. This design enables evaluation of domain breadth, performance degradation as difficulty increases, the ability to solve computational tasks, and model behavior in specialized financial domains. We also describe a unified evaluation protocol covering multiple-choice questions, numerical answers, and short open-ended responses, together with an automated scoring scheme for freeform answers based on the LLM-as-judge paradigm. FINESSE-Bench is intended both as a complement to existing open financial benchmarks and as a tool for more substantive evaluation of professionally relevant financial competencies in large language models.

---


### 41. [When Does Sparse MoE Help in Vision? The Role of Backbone Compute Leverage in Sparse Routing](https://arxiv.org/abs/2605.15484)

**<font color=#1a73e8>作者：</font>** Libo Sun, Po-wei Harn, Peixiong He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) networks promise favorable accuracy-compute trade-offs, yet practical vision deployments are hindered by expert collapse and limited end-to-end efficiency gains. We study when sparse top-$k$ routing with hard capacity constraints helps in vision classification, evaluated under multi-seed protocols on four benchmarks (CIFAR-10/100, Tiny-ImageNet, ImageNet-1K). We observe a \emph{compute-leverage pattern}: positive accuracy gaps require a substantial fraction $\rho$ of total FLOPs to be routed; at ImageNet scale this is necessary but not sufficient, as multi-expert routing ($k \geq 2$) is additionally required. Two controlled experiments isolate these factors. A hidden-size sweep on CIFAR-10 yields both predicted sign reversals across standard and depthwise backbones, ruling out backbone family as the active variable. An ImageNet-1K ablation that varies only top-$k$ -- holding architecture, initialization, and $\rho$ fixed -- reverses the gap from positive to negative across all five seeds. A per-sample variant of Soft MoE that softmaxes over experts rather than the batch rescues CIFAR-100 above the dense baseline, identifying batch-axis dispatch as the dominant failure mode in per-sample CNN settings. Code and aggregate results: this https URL.

---


### 42. [Ghosted Layers: Unconstrained Activation Alignment for Recovering Layer-Pruned LLMs](https://arxiv.org/abs/2605.15491)

**<font color=#1a73e8>作者：</font>** Vincent-Daniel Yun, Junhyuk Jo, Sai Praneeth Karimireddy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Layer pruning removes entire Transformer decoder blocks from large language models, but introduces a mismatch between the hidden state received by the next surviving layer and the distribution it was trained to process, leading to significant performance degradation. We propose Ghosted Layers, a training-free recovery module that addresses this issue by solving a boundary activation alignment problem. Our method derives a closed-form optimal linear operator from a small calibration set to reconstruct the activation discrepancy introduced by the pruned layers. We show that this solution corresponds to the unconstrained optimum of the alignment objective, whereas existing methods are restricted to constrained solutions over limited operator subspaces. Experiments across multiple LLM backbones and pruning strategies demonstrate that our method consistently improves accuracy and perplexity over prior training-free baselines, while preserving the efficiency gains of layer pruning.

---


### 43. [STS: Efficient Sparse Attention with Speculative Token Sparsity](https://arxiv.org/abs/2605.15508)

**<font color=#1a73e8>作者：</font>** Ceyu Xu, Jiangnan Yu, Yongji Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quadratic complexity of attention imposes severe memory and computational bottlenecks on Large Language Model (LLM) inference. This challenge is particularly acute for emerging agentic applications that require processing multi-million token sequences. We propose STS, a sparse attention mechanism that requires no model retraining. STS leverages the key insight that tokens identified as important by a smaller draft model are highly predictive of important tokens for a larger target model. By integrating into speculative decoding frameworks, STS repurposes the draft model's attention scores to dynamically construct a token-and-head-wise sparsity mask. This mask effectively prunes the expensive attention computation in the target LLM. Our evaluation shows that STS achieves a 2.67x speedup operating at approximately 90% sparsity on representative benchmark NarrativeQA, maintaining negligible accuracy degradation compared to dense attention. STS establishes a new state-of-the-art on the sparsity-accuracy trade-off, outperforming prior techniques by enabling higher sparsity levels for a given accuracy budget.

---


### 44. [CAPS: Cascaded Adaptive Pairwise Selection for Efficient Parallel Reasoning](https://arxiv.org/abs/2605.15513)

**<font color=#1a73e8>作者：</font>** Fangzhou Lin, Shuo Xing, Peiran Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parallel reasoning, where a generator samples many candidate solutions and an aggregator selects the best, is one of the most effective forms of test-time scaling in large language models, and pairwise self-verification has become its strongest aggregation primitive. Yet pairwise verification carries a heavy cost: each judgment reads two complete solutions in full, and existing methods perform tens of such judgments per problem regardless of whether the comparison is informative. We introduce CAPS (Cascaded Adaptive Pairwise Selection), an inference-only framework that allocates verifier compute non-uniformly along two orthogonal axes: an evidence axis that adapts how much of each candidate the judge sees, and a distribution axis that adapts how comparisons are spread across the pool. CAPS instantiates these into a four-stage cascade with an optional rescue subroutine, and admits a closed-form verifier-token cost in which the per-candidate marginal cost is roughly halved relative to uniform full-evidence schedules. On four self-verifying models (Qwen3-14B, GPT-OSS-20B, Qwen3-4B-Instruct/Thinking) and five reasoning benchmarks spanning code (LiveCodeBench-v5/v6, CodeContests) and math (AIME 2025, HMMT 2025), CAPS outperforms the leading pairwise verifier on 14 of 20 suites while using 25.4% of its verifier-token budget on code, and outperforms pointwise self-verification on all 20. The trade-off suites admit an interpretable diagnostic in terms of the verifier's accuracy at partial versus full evidence, providing a concrete pre-deployment check for cascade suitability.

---


### 45. [DetectRL-X: Towards Reliable Multilingual and Real-World LLM-Generated Text Detection](https://arxiv.org/abs/2605.15518)

**<font color=#1a73e8>作者：</font>** Junchao Wu, Yefeng Liu, Chenyu Zhu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The effective detection and governance of Large Language Model (LLM) generated content has become increasingly critical due to the growing risk of misuse. Despite the impressive performance of existing detectors, their reliability and potential in multilingual, real-world scenarios remain largely underexplored. In this study, we introduce DetectRL-X, a comprehensive multilingual benchmark designed to evaluate advanced detectors across 8 dimensions. The benchmark encompasses 8 languages commonly used in commercial contexts and collects human-written texts from 6 domains highly susceptible to LLM misuse. To better aligned with real-world applications, We create LLM-generated texts using 4 popular commercial LLMs, and include typical AI-assisted writing operations such as polishing, expanding, and condensing to capture authentic usage patterns. Furthermore, we develop a multilingual framework for paraphrasing and perturbation attacks to simulate diverse human modifications and writing noise, enabling stress testing of detectors across languages. Experimental results on DetectRL-X reveal the strengths and limitations of current state-of-the-art detectors when applied to diverse linguistic resources. We further analyze how domains, generators, attack strategies, text length, and refinement operations influence performance in different languages, underscoring DetectRL-X as an effective benchmark for strengthening multilingual and language-specific detectors.

---


### 46. [On the Fragility of Data Attribution When Learning Is Distributed](https://arxiv.org/abs/2605.15520)

**<font color=#1a73e8>作者：</font>** Xian Gao, Bo Hui, Min-Te Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data attribution has become an important component of pricing, auditing, and governance in machine learning pipelines, yet most attribution methods implicitly assume that attribution values faithfully reflect participants' contributions. We show that this assumption can fail: a single participant in a standard distributed training workflow can substantially inflate its measured attribution value while preserving global utility. Our attribution-first attack uses latent optimization to inject small synthetic batches that preserve utility while exploiting non-IID label coverage and evaluator sensitivities. Across datasets, models, and multiple marginal-utility evaluators, the attack consistently increases the adversary's attribution value and reshapes the relative attribution structure among benign clients without degrading accuracy or triggering geometry-based defenses. These results show that attribution itself forms a new attack surface and motivate the development of attribution-robust and incentive-compatible scoring mechanisms.

---


### 47. [Self-Prompting Diffusion Transformer for Open-Vocabulary Scene Text Editing via In-Context Learning](https://arxiv.org/abs/2605.15523)

**<font color=#1a73e8>作者：</font>** Hongxi Li, Tong Wang, Chengjing Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene text editing aims to modify text in a target region of an image while preserving surrounding background style and texture. Existing methods rely solely on image background information while neglecting the visual details of target regions, which discards stylistic features in the original text and essentially degrades the task to text rendering. Moreover, the conditions imposed by pre-trained glyph encoder limit the scope of editable text. To address these issues, this paper proposes a self-prompting scene text editing method that constructs style and glyph prompts directly from the original image, without introducing additional style or glyph encoders. We employ a two-stage training strategy: the diffusion transformer is first trained on large-scale self-supervised data and then refined using a small set of paired images. By leveraging the in-context learning capability of the Multi-Modal Diffusion Transformer (MM-DiT), it achieves open-vocabulary and style-consistent text editing. Experimental results on various languages demonstrate that our method achieves the state-of-the-art performance in both text accuracy and style consistency. Our project page: \href{this https URL}{this http URL}.

---


### 48. [DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation](https://arxiv.org/abs/2605.15532)

**<font color=#1a73e8>作者：</font>** Jaehun Jung, Hyunwoo Kim, Brandon Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distillation enables compact Vision-Language Models (VLMs) to obtain strong reasoning capabilities, yet the prompts driving this process are typically chosen via simple heuristics or aggregated from off-the-shelf datasets. We reveal a critical inefficiency in this approach: up to 69% of the prompts in standard chart / document reasoning datasets are effectively zero-delta, meaning the teacher and student already induce the exact same answer distribution. Training on these prompts provides minimal learning signal, causing student improvement to rapidly saturate regardless of data scale. To escape the zero-delta trap, we return to first principles: distillation fundamentally minimizes distributional divergence, and thus a prompt is valuable only if it exposes a functional capability gap between the teacher and student. We quantify this gap through answer divergence ($\Delta$), demonstrating that non-zero divergence is critical for effective scaling. Building on this insight, we propose a staged synthesis pipeline that repurposes existing datasets as seeds, actively targeting student failure modes to produce better prompts. The result is DeltaPrompts, a diverse dataset of 200k synthetic, high-divergence reasoning problems. We evaluate DeltaPrompts across three distinct settings: on-policy distillation with the target teacher-student pair, transfer to a novel model family without regenerating the data, and off-policy fine-tuning of a non-reasoning model. Across all scenarios, DeltaPrompts drives substantial gains, yielding up to 15% relative improvement even on top of a highly-optimized reasoning model (e.g., Qwen3-VL-8B-Thinking) -- averaged over 10 benchmarks spanning chart, document and perception-centric reasoning.

---


### 49. [RTL-BenchMT: Dynamic Maintenance of RTL Generation Benchmark Through Agent-Assisted Analysis and Revision](https://arxiv.org/abs/2605.15537)

**<font color=#1a73e8>作者：</font>** Jing Wang, Shang Liu, Hangan Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces RTL-BenchMT, an agentic framework for dynamically maintaining RTL generation benchmarks. Large Language Models (LLMs) assisted automated RTL generation is one of the most important directions in EDA research. However, current RTL benchmarks face two critical challenges: (1) flawed cases in the benchmarks and (2) overfitting to the benchmarks. Both challenges are difficult to resolve purely by manual engineering effort. To address these issues and systematically reduce human maintenance costs, we propose an automated agentic framework, RTL-BenchMT. RTL-BenchMT focuses on two key applications: (1) automatically identifying and revising flawed benchmark cases and (2) automatically detecting and updating overfitting cases. With the assistance of RTL-BenchMT, we conduct a thorough, in-depth analysis of flawed and overfitting cases and produce a refined benchmark suite that will be open-sourced to the community.

---


### 50. [DRS-GUI: Dynamic Region Search for Training-Free GUI Grounding](https://arxiv.org/abs/2605.15542)

**<font color=#1a73e8>作者：</font>** Yichao Liu, Huawen Shen, Liu Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GUI agents powered by Multimodal Large Language Models (MLLMs) have demonstrated impressive capability in understanding and executing user instructions. However, accurately grounding instruction-relevant elements from high-resolution screenshots cluttered with irrelevant UI components remains challenging for existing approaches. Inspired by how humans dynamically adjust their perceptual scope to locate task-related regions on complex screens, we propose DRS-GUI, a training-free dynamic region search framework for GUI grounding that can be seamlessly integrated into existing MLLMs. DRS-GUI introduces a lightweight UI Perceptor that performs three human-like perceptual actions (Focus, Shift, and Scatter) to progressively explore the interface and generate region proposals. To dynamically schedule these actions, we further design an Action Planner based on Monte Carlo Tree Search (MCTS). A region quality reward is employed to evaluate and select the highly instruction-relevant region, efficiently pruning redundant UI elements. Experiments demonstrate that DRS-GUI yields a 14\% improvement on ScreenSpot-Pro for general and GUI-specific MLLMs (Qwen2.5-VL-7B and UGround-V1-7B), significantly enhancing grounding performance and generalization.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-127](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
