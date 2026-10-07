# 🧠 大模型相关研究 | 2026年10月08日

> 本类共 **303** 篇论文：已确认 **280** 篇，待复核 **23** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-303](./part-07.md)

---

### 151. [Adaptive Mean Estimation by In-Context Learning: A Gradient-Flow Analysis](https://arxiv.org/abs/2610.07804)

**<font color=#1a73e8>作者：</font>** Martin Eppert, Krishna Balasubramanian, Subhro Ghosh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior Fitted Networks (PFNs) such as TabPFN now rival established statistical procedures across prediction and estimation tasks. A natural explanation is that PFNs have the property of statistical adaptivity, that is, they perform nearly as well as a method tailored to the true data-generating model for a heterogeneous set of models, while not being told which model the data comes from. We study how such adaptivity is learned in a controlled location-estimation problem. Each task is an unlabeled sample whose family is hidden: Gaussian data call for averaging, with error of order $n^{-1}$, whereas uniform data are best estimated from their extremes, at the faster rate $n^{-2}$. We also provide the example of a symmetric Gaussian mixture, for which a rate of $\sigma^2_n/n$ can be attained. On scalar inputs, softmax attention computes the derivative of the empirical cumulant-generating function. A single primitive therefore both supplies features that distinguish the families and forms estimators interpolating between the sample mean and the mid-range. We combine attention experts through either a softmax mixture of experts or a gated linear unit (GLU), and analyze stagewise gradient flow. With $\widetilde{\Omega}(n^{1+\epsilon})$ pretraining tasks, the learned estimator is asymptotically efficient on Gaussian tasks, within a factor $n^{\epsilon}$ of the minimax rate on uniform tasks, and order-optimal on mixtures in a shrinking-variance regime. These guarantees extend to new locations and longer contexts. A risk decomposition separates expert error, routing error and normalization error, which clarifies the architectural contrast. Softmax gating enforces normalization and exact translation equivariance, whereas the GLU must learn it: its dynamics separate into fast bias removal followed by slow expert selection. End-to-end experiments recover the predicted specialization.

---


### 152. [MASKerade: Token-Routed Mask Experts for Dense-to-MoE Upcycling](https://arxiv.org/abs/2610.07809)

**<font color=#1a73e8>作者：</font>** Mingyuan Zhang, Yue Bai, Zhongruo Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparsely activated Mixture-of-Experts (MoE) models increase model capacity without a proportional increase in per-token computation. Dense-to-MoE upcycling reuses pretrained dense models to construct such systems, commonly by copying feed-forward networks (FFNs) into independently trained experts. We introduce MASKerade, a dense-to-MoE training method that instead learns experts as sparse subnetworks of a frozen pretrained FFN. Each expert is defined by a learned binary mask, and a token-level router selects which masked FFNs to execute and combine. The router and mask scores are optimized jointly, while the underlying FFN weight values remain unchanged. This formulation supports neuron-structured, semi-structured, and unstructured experts within the same routing architecture. Our main configuration uses four 2:4 experts with top-2 routing, where two half-dense expert passes have the nominal FFN arithmetic of one dense pass, without requiring independent expert weight matrices. On five vision-language benchmarks with Qwen and Gemma backbones, this configuration achieves the highest performance among the compared baselines. Comparisons across mask granularities, routing interventions, and compute-matched controls distinguish the effects of learned connectivity from expert activation count. These results establish mask learning over frozen weights as a practical alternative for constructing token-routed MoE experts.

---


### 153. [Do I Need the Cloud? Uncertainty-Aware Step-Level Handoff for Small Language Model Agents](https://arxiv.org/abs/2610.07816)

**<font color=#1a73e8>作者：</font>** Abolfazl Younesi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small language models (SLMs) are attractive as local agent controllers because they reduce remote inference, latency, and deployment footprint, yet structured tool errors can cause an agent step to fail. Existing routers typically select a model once per query. However, agents expose sequential decision points whose difficulty dynamically changes based on intermediate observations. We propose STEPGATE, an uncertainty-aware handoff framework that scores each local SLM action and selectively escalates challenging steps to a stronger model. On a 52-task held-out single-step BFCL-derived test split, the Qwen2.5-1.5B/7B pair attains 82.7% task success with 30.8% escalation, versus 67.3% local-only and 75.4% random escalation (which uses 33.8% escalation). In a separate multi-turn evaluation, STEPGATE achieves 69.0% trajectory success and 84.0% action success using only 30.0% cloud actions, compared with 48.0%/70.5% local-only, 60.0%/78.2% random escalation, and 57.0%/77.1% query-level routing (strong-only achieves 82.0% trajectory success at 100% cloud actions). These results suggest that step-level escalation recovers a large share of the performance gap to the stronger Qwen2.5-7B backend at a matched cloud-action rate while transmitting fewer tokens remotely. However, our evaluation is limited to one model family, a single stronger backend, and scripted tasks. Furthermore, the test sets are small, multi-turn comparisons rely on paired intervals and statistical tests, and our risk tiers serve as research annotations rather than formal safety guarantees.

---


### 154. [One Step at a Time: Trading LLM Autonomy for Process Predictability](https://arxiv.org/abs/2610.07817)

**<font color=#1a73e8>作者：</font>** Hans Schabert, Christoph Peters  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Organizations automating operational processes need more than a correct outcome: they need to predict how a process will run, know which one actually ran, and inspect it step by step. When an agent is the executor that predictability is normally lost: the prescribed procedure goes into the system prompt, and only a final answer comes back. We deliver the procedure step by step over the Model Context Protocol (MCP) instead: a server releases one step at a time, the agent executes it, and each step returns a structured step_output. This trades autonomy for predictability, and two properties then follow by construction, independent of the executor. The execution path is prescribed before the run, so the process is predictable in advance rather than reconstructed afterwards; and the completed step records form a machine-readable execution log that downstream tooling can audit and optimize step by step. Evaluating 15,475 trials across 13 SOP-Bench domains and four open-weight executors from frontier (Kimi K2.5) to lightweight (Ministral 3 8B), we find step-level delivery makes the executed process predictable and inspectable for every executor, and additionally raises accuracy when the executor is small. Across all four, process adherence rises significantly (76-95% to 95-99%) and ungrounded answers (correct outputs produced without executing the SOP) near-vanish, falling from 2.1-4.5% to 0.2-0.3% of trials (all 95% CIs exclude zero); under prompt-based delivery, 31-49% of correct answers on know_your_business bypass the SOP entirely, even for the frontier executor. Accuracy is where the executor's capability enters: the lightweight executor gains +6.5pp grounded accuracy because supplying the process externally removes a reconstruction burden it cannot carry, while capable ones trade a small raw-accuracy decrement for a predictable, auditable process.

---


### 155. [$α$Transfer: Coefficient Transfer for Efficient Model Merging](https://arxiv.org/abs/2610.07819)

**<font color=#1a73e8>作者：</font>** Shih-Cheng Huang, Zhi Rui Tam, Chieh-Yen Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging offers a promising solution for combining multiple fine-tuned checkpoints into a single model through parameter arithmetic. However, finding optimal merging coefficients requires an extensive search that becomes prohibitively expensive as models scale in both size and number, due to high memory requirements and combinatorial growth in the search space. We show that, within the same model family, models exhibit highly congruent performance distributions over merging coefficients across different model sizes. This distributional similarity enables a practical paradigm we call \textit{$\alpha$Transfer}: searching for optimal coefficients on a small proxy model, then directly transfer them to larger target models. We verify $\alpha$Transfer across multiple merging methods, model families, and tasks. Experimental results demonstrate a 6$\times$ speedup and 70\% memory reduction on vision transformers, and a 20$\times$ speedup and 85\% memory reduction on large language models, while maintaining comparable performance. Our findings establish $\alpha$Transfer as an efficient and generalizable approach to scaling model merging.

---


### 156. [DHCG: Dynamic Construction of Hierarchical Collaboration Graphs for LLM-Based Multi-Agent Reasoning](https://arxiv.org/abs/2610.07835)

**<font color=#1a73e8>作者：</font>** Jie Ren, Jiakang Yuan, Chenyu Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (MAS) have demonstrated strong capabilities in solving complex problems across diverse domains. Recently, the dynamic orchestration of agent systems has become an important research direction. However, existing methods suffer from limited composition, misaligned dependencies, and inflexible scale, restricting their ability to adapt to reasoning requirements during execution. To address these limitations, we reframe MAS design as a partially observable Markov decision process, in which both the composition and scale of the MAS are dynamically determined. We propose DHCG, a novel framework that coordinates three modules (Planner, Worker, and Generator) to progressively construct a dynamic hierarchical collaboration graph from scratch based on the query and evolving execution feedback. At each step, guided by feedback, the Planner generates a set of distinct and complementary roles tailored to the current reasoning needs and selectively routes relevant information to each role. It can also finalize the hierarchical collaboration graph early or progressively expand it when additional reasoning is required. We further introduce action-aware preference optimization to train the Planner to make more effective decisions when constructing hierarchical collaboration graphs. We systematically evaluate DHCG across code generation, mathematical reasoning, and domain-specific reasoning benchmarks. DHCG achieves state-of-the-art average performance among the compared methods, improving over the single-agent baseline by 13.06 points and outperforming both static and dynamic MAS baselines by 2.77-8.02 points. Additional experiments further demonstrate its generalization across different Planner backbones and unseen Worker models.

---


### 157. [Privileged Context as Drift in On-Policy Self-Distillation](https://arxiv.org/abs/2610.07842)

**<font color=#1a73e8>作者：</font>** Ravenor Davion, Nick Rui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) trains a language model to match a copy of itself conditioned on privileged context. Existing work varies what privileged context contains and how it is produced while also changing models, data, and training setups, making the effects of privileged context design difficult to isolate. Motivated by efforts in continual learning to reduce catastrophic forgetting, we study how the choice of privileged context affects policy drift. Specifically, we vary two axes: content (a demonstration, feedback, or rephrase) and source (external, self-generated with a verifier, or self-generated without a verifier). We train Qwen2.5-7B with OPSD across these nine combinations and three datasets, measuring target-task accuracy, prior-task retention, reverse KL from the base policy, and parameter-update geometry. Holding source fixed, changing content spans a wider median KL range than holding content fixed and changing source. The ratio between these ranges is $5.1\times$ for per-token KL and $2.2\times$ for per-sequence KL. Parameter-update geometry shows the same pattern: updates from adapters that share content are more closely aligned (mean cosine $0.571$) than updates from adapters that share source ($0.255$). For continual learning, these findings suggest that privileged context should be treated as part of OPSD's stability design because it is associated with how far and in what direction the policy moves.

---


### 158. [OMIT the Action: Measuring Framing-Invariant Omission Bias under Philosophical Disagreement](https://arxiv.org/abs/2610.07847)

**<font color=#1a73e8>作者：</font>** Sihyeon Lee, Jihun Song, Chanwoo Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLMs increasingly assist in moral reasoning, omission bias, the tendency to prefer inaction even when equivalent framings reverse substantive outcomes, poses a significant risk of skewed decision-making. Yet omission bias remains underexplored in LLM evaluation, with the few existing studies limited in scale and focused largely on utilitarian-deontological conflicts. To address this gap, we introduce OMIT, a benchmark consisting of 218 paired-frame scenarios across 10 conflict types, constructed by leveraging disagreement patterns from an LLM-based, five-perspective philosophical persona panel (utilitarianism, deontology, virtue ethics, care ethics, and contractualism). Evaluating eight LLMs, we find that omission bias is pervasive but inversely correlates with model size within families. We further evaluate four inference-time interventions and find that interventions encouraging models to consider moral principles before committing to a yes/no answer reduce omission bias and increase frame-consistent responses, although lower omission bias rates can also coincide with shifts toward action-biased responses. Ultimately, this work contributes not only the OMIT benchmark, but also a methodology for using diverse philosophical disagreement signals to evaluate framing-sensitive inaction preferences and the distributional effects of mitigation attempts in LLMs under complex moral conflicts.

---


### 159. [Dynamic Positional Attention Modulation for Parameter-Efficient Fine-Tuning of Large Language Models](https://arxiv.org/abs/2610.07848)

**<font color=#1a73e8>作者：</font>** Dayan Pan, Jingyuan Wang, Xie Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) has become a standard approach for adapting large language models to downstream tasks. However, most existing PEFT methods rely on uniform and static adaptations, without accounting for the structured heterogeneity of attention across dimensions, heads, layers, and input tokens. In practice, attention representations exhibit non-uniform behavior, and positional encoding mechanisms such as rotary positional embeddings (RoPE) induce dimension-dependent positional structure, making uniform adaptation suboptimal. In this work, we propose DyPAM (Dynamic Positional Attention Modulation), a PEFT method that adapts how positional information contributes to attention by operating directly on the query and key representations. DyPAM combines input-conditioned, dimension-wise modulation with head-wise and layer-wise structural modulation, performing fine-grained adaptation of positional attention aligned with the RoPE-induced structure without modifying the pretrained backbone. Extensive experiments on mathematical and commonsense reasoning benchmarks across multiple backbone models demonstrate that DyPAM consistently outperforms existing strong PEFT baselines.

---


### 160. [RA-MoWE: Workflow-Affinity Embeddings for Query Clustering and Agentic Workflow Generation](https://arxiv.org/abs/2610.07851)

**<font color=#1a73e8>作者：</font>** Qi Cheng, Shengyu Chen, Wei Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic workflows enable large language models (LLMs) to solve complex tasks by coordinating reasoning, tool use, and verification. However, a workflow optimized for an entire task collection can overlook differences in the reasoning strategies that individual queries need, while searching for a new workflow for every query repeats costly optimization. To address this tradeoff, we introduce RA-MoWE, a framework that uses workflow-affinity embeddings to cluster queries and guide the generation of reusable expert workflows. Each embedding records how well a fixed set of reference workflows solves a query, revealing similarities in which reasoning strategies are effective. RA-MoWE uses each cluster's queries and average embedding to initialize and refine a specialized workflow through execution feedback. An embedding encoder predicts these embeddings from query text, allowing new queries to select a generated expert without first executing the reference workflows. On a 300-query test set drawn from four benchmarks spanning mathematics, science, and programming, RA-MoWE improves average task score by 4.04 percentage points over selecting among the reference workflows, while using 27.7% fewer language-model calls at inference.

---


### 161. [Lost in the bf16 Cast: Exporting Ternary Language Models Can Revert Most Low-Learning-Rate Code Changes](https://arxiv.org/abs/2610.07853)

**<font color=#1a73e8>作者：</font>** Avichal Sahai, Nishant Raj, Animesh Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ternary language models such as BitNet b1.58, Falcon-E and BitCPM are fine-tuned with higher-precision latent weights and deployed as ternary codes produced by an export step that, in the labs' documented pipelines, first casts the latents to bf16. We audit those pipelines across three labs. In released checkpoints, fp32 quantization of the shipped latents disagrees with the deployed codes on 0.83-1.77% of codes in Falcon-E and BitCPM and on 1.530% in BitNet 2B-4T; for Falcon-E and BitCPM most disagreements are products that bf16 rounding lands exactly on the threshold, which ties-to-even maps to zero, and the unmodified onebitllms exporter reproduces all four Falcon-E releases byte for byte. At fine-tuned endpoints, with learning rates selected to match a nominal learning-rate-to-bf16-ULP ratio, the documented export lowers greedy GSM8K strict accuracy from 58.79% to 0.78% for Falcon-E-1B-Base and from 36.13% to 0.39% for BitCPM-CANN-0.5B, and a bf16 save and reload lowers BitNet 2B-4T's strict accuracy by 27.54 points while its last-number accuracy rises. Two compatibility remedies, writing the training quantizer's codes directly or adjusting the bf16 inputs until the unchanged tools emit them, each met a 4-point strict-accuracy non-inferiority criterion against online evaluation in all three models. In two model families, randomized interventions on the initial distance from the threshold support distance-dependent selection of the codes that fine-tuning changes.

---


### 162. [WorkflowOps: Learning Agent Collaboration Priors for Multi-Agent Workflow Orchestration](https://arxiv.org/abs/2610.07860)

**<font color=#1a73e8>作者：</font>** Qi Cheng, Shengyu Chen, Wei Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems are increasingly deployed for complex knowledge work, yet their orchestration layers remain largely memoryless: each new task is decomposed, assigned, and executed from scratch with no benefit from prior successful executions. We present WorkflowOps, a multi-agent workflow orchestration framework that learns agent collaboration priors from historical workflows and expands its agent pool on demand to cover new capability requirements. Our approach introduces three coupled mechanisms. First, a transition probability matrix captures pairwise agent collaboration frequencies from past workflows and applies them as soft guidance during DAG workflow construction through intra-layer ordering optimization, probability-thresholded edge suggestion, and transitive reduction for parallelism maximization. Second, a sufficiency-driven agent creation loop detects capability gaps via semantic matching scores, generates specialized agents through an LLM, and simultaneously injects them into the collaboration matrix, so that newly created agents are immediately usable with predicted collaboration priors. Third, a layered semantic matching strategy uses pre-trained sentence embeddings for fast, deterministic capability matching as a first pass, invoking LLM verification only for low-confidence cases, thereby reducing LLM routing calls by over 80\% compared to pure-LLM approaches. Experiments on mixed code, math, and question-answering suites show that WorkflowOps improves end-to-end pass rates over recent workflow-construction baselines, with the largest gains on structured, decomposable tasks where past agent handoff patterns transfer.

---


### 163. [ReFold: Training-Free Reversible Inter-Turn Context Folding for Long-Horizon Agents](https://arxiv.org/abs/2610.07863)

**<font color=#1a73e8>作者：</font>** Yupeng Su, Jiayi Tian, Zheng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents act on an append-only interaction history that is re-sent to the model at every step, so the context and its cost grow with steps until the sessions exceed the context window. Existing methods manage the context through context requirement prediction, relying on additional model calls, heuristic rules, or trained policies. However, these predictive approaches introduce runtime overhead, invalidate prefix caches, and permanently discard content with no guarantee of recovery. To overcome these limitations, we introduce ReFold: a training-free rendering layer that preserves the underlying interaction history while compressing only the model's rendered context. It removes two kinds of inter-turn redundancy without an auxiliary predictor: content an earlier turn already displayed, replaced by a stub, and turns the agent itself reports finished, folded into a one-line note. Both operators use chunked rendering, rewriting the cached prefix once every few steps rather than at every step. Every removal is strictly reversible, a wrong removal costs one restore from the history rather than permanent content loss. Because it operates at the rendering layer, ReFold is plug-and-play across standard ReAct-style harnesses. Evaluations across five long-horizon benchmarks and two frontier LLMs demonstrate that ReFold reduces token consumption by up to 2.5x and halves the KV-cache memory per session without degrading task success rates. Under capped context budgets, it avoids up to 92% of forced compactions. Under concurrent serving workloads, it reduces request queuing delays by up to 100%, accelerating inference by up to 1.7x, while cutting inference costs by up to 3.4x.

---


### 164. [CueRator: Agentic Search for Symbolic Rules to Adapt Frozen Multimodal Encoders](https://arxiv.org/abs/2610.07868)

**<font color=#1a73e8>作者：</font>** Sunchan Park, Beomkwon Cho, Kyeongbo Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language model agents have been used to search over symbolic structures such as programs and equations. We propose CueRator, an agentic framework for policy-aware decision-rule discovery, which adapts frozen contrastive multimodal encoders by searching for the decision rule that converts their cross-modal similarities into predictions. We validate it on open-vocabulary audio-visual event perception, where existing methods involve a trade-off between adaptivity and generalization to unseen categories: trained modules adapt at the cost of generalization, and fixed rules the reverse. The framework pairs a symbolic formulation for generalization with a lightweight policy that predicts its parameters per video for adaptivity. A report-guided multi-agent loop discovers the formulation offline, evaluating each candidate on its expressive ceiling and on whether a trained policy can realize it. On OV-AVEBench, CueRator raises the total average from 57.8 to 60.2 and unseen-category performance from 55.8 to 59.9 over the best existing method, reducing the seen-unseen gap from 7.1 to 1.2. Ablations attribute the gains to both the formulation and the policy and show that both feedback signals are necessary for effective search. CueRator also improves over the respective baselines on two further audio-visual event perception tasks, and the discovered rule remains competitive across encoders with only the policy retrained. Code is available at this https URL.

---


### 165. [Preparing an AI-Augmented SIEM for the EU Cyber Resilience Act: A Practitioner Case Study](https://arxiv.org/abs/2610.07873)

**<font color=#1a73e8>作者：</font>** Georgios Koutidis, Nikolaos Kekatos, Marina Korgiala-Karyda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The EU Cyber Resilience Act (CRA), Regulation (EU) 2024/2847, makes product cybersecurity a lifecycle obligation for products with digital elements on the EU market: risk assessment, vulnerability handling, conformity documentation, and Article 14 incident- and vulnerability-reporting readiness must be operational before market placement. Small and medium-sized enterprises that build security products are doubly exposed, since their products are in scope while their customers expect them to be exemplary. This case study documents a CRA preparedness pilot for one such product, SEUXDR, an AI-augmented security monitoring product with a large-language-model active-response component, on the open-source CYBERFORT platform. We contribute a reproducible six-step recipe (Scope and Classify, Asset Registration, Produce Evidence, Map to CRA, Gap and Actions, Audit Pack), two end-to-end traceability threads, and a pilot snapshot tracing product risks through baseline and AI-specific controls and policies to CRA objectives. It offers practitioners a replicable starting point for translating CRA legal text into operational preparedness for incident response, vulnerability reporting, and conformity assessment.

---


### 166. [On-Policy Distillation with Negative-Policy Rollouts](https://arxiv.org/abs/2610.07874)

**<font color=#1a73e8>作者：</font>** Jaehui Hwang, Dongyoon Han, Sangdoo Yun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has been widely studied as a post-training method in which a student model obtains token-level supervision from a stronger teacher on its own rollouts. Recent studies have improved OPD through alternative distillation reward formulations and teacher configurations, while the objective of distillation remains centered on mimicking the teacher. However, when a stronger teacher has limited distributional overlap with the student, such positive guidance can provide insufficient learning signals. In this work, we introduce Negative-Policy OPD (NP-OPD), which complements teacher supervision with rollouts from a lower-performing, lower-capability negative policy that serves as a negative reference for the student. Rather than modifying the distillation reward formulation, NP-OPD introduces the negative policy at the rollout stage, continuously supplying tokens preferred by the negative policy over the teacher so that they remain exposed to teacher supervision throughout training. This provides an explicit negative signal through negative-policy rollouts while preserving the positive teacher supervision used in OPD. Through extensive experiments, we show that NP-OPD improves OPD across model scales, generation modes, reasoning domains, and different OPD variants. Furthermore, our analyses show that NP-OPD effectively suppresses tokens preferred by the negative policy over the teacher and moves the student away from the negative policy. These results support our design of introducing negative signals through negative-policy rollouts and provide new insight into the role of the rollout policy in OPD. Code will be available at this https URL.

---


### 167. [ShanLiangRen: A Nutrition Agent for Personalized Daily Meal Planning](https://arxiv.org/abs/2610.07886)

**<font color=#1a73e8>作者：</font>** Miao Xie, Xiao Zhang, Yuan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dietary nutrition planning plays an important role in chronic disease management and maintaining a healthy body. In applications, it must simultaneously satisfy personalized constraints and reasonable multidimensional nutritional goals. These two aspects often conflict, and user constraints evolve with feedback, resulting in a substantial gap between generic guidelines and executable plans. To bridge this gap, we first propose the personalized fully quantified multiobjective dietary planning problem (MDP). To tackle MDP, we develop a nutrition agent, ShanLiangRen. The system first transforms dietary specifications, nutrient data, user attributes and natural language requirements into an individualized constrained planning instance. It then employs an exact retrieval-augmented generation method to shrink the feasible candidate set from a large scale ingredient and recipe space. Finally, it adopts a refinement guided by Pareto principles, where an LLM iteratively revises candidate plans under deterministic nutrition computation and feedback from constraint verification. The system outputs fully quantified meal plans with explicit ingredients and portion sizes, together with reports on nutrition compliance that show constraint satisfaction and nutrient interval attainment. We have released the system online as a WeChat Program, ShanLiangRen. A demo video is available at this https URL.

---


### 168. [Rethinking Faithfulness in LLMs: A Pairwise Context-Sensitive Perspective](https://arxiv.org/abs/2610.07894)

**<font color=#1a73e8>作者：</font>** Zizhuo Zhang, Xiong Peng, Jingwei Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are expected to answer questions faithfully based on the provided context, abstaining when the context information is insufficient to answer the questions. Existing faithfulness evaluations typically assess each question-context instance in isolation; however, such instance-level evaluation fails to capture a fundamental requirement of faithful behavior: the ability to adapt model responses to changes in available contexts. In particular, a model should provide correct answers when sufficient evidence is present and abstain when it is not. In this work, we propose a Pairwise Faithfulness Benchmark (PFaithBench) that evaluates whether a model can switch between answering and abstaining for the same question under supporting versus non-supporting contexts. Our evaluations across thirty-nine models with seven model families demonstrate that faithfulness fundamentally involves a trade-off between answering and abstaining, and that most current models exhibit a strong bias toward answering, with most faithfulness errors arising from over-answering, i.e., models tend to fabricate a response even when the provided context is insufficient. We further conduct a series of studies on faithfulness training under different data constructions. Our results show that training outcomes are highly sensitive to the specific composition of answering and abstaining data. Constructing answering and abstaining data from mismatched sources can cause models to rely on dataset-specific shortcuts rather than actual context sufficiency. Moreover, increasing answer-supervised data improves answering performance but exacerbates over-answering, while increasing abstaining data reduces hallucination but leads to over-abstention. The code and data are released at this https URL.

---


### 169. [Textual Environmental Context and Spatial Graphs for LLM-Based Regional SST Forecasting](https://arxiv.org/abs/2610.07895)

**<font color=#1a73e8>作者：</font>** Xiong Li, Xiaowei Zhou, Yanwei Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sea surface temperature (SST) forecasting depends on local temporal persistence, regional spatial dependence, and environmental conditions that evolve with the forecast date. We study how these heterogeneous conditions can be presented to a large language model (LLM) for regional multi-step forecasting without serializing the full SST grid as text. We formulate forecasting as conditional numerical generation: historical SST and anomaly sequences, date-aligned environmental records, and static ocean knowledge form a textual context, while regional spatial state is supplied through continuous graph-derived prefixes. A static graph encodes persistent geographic--climatological relations, and a dynamic graph encodes recent SST correlations and localized tropical-cyclone influence. Two graph neural networks produce a target-node representation that is mapped by a spatial-prefix fusion and injected into the LLM input. On SST forecasting in the South China Sea, the complete configuration achieves the best MAE and $\Rtwo$ among the compared methods over ten forecast steps. Alongside the numerical forecast, a rule-based module matches predicted trends and environmental-factor directions with knowledge entries to return source-linked, post-hoc contextual explanations.

---


### 170. [FC-SWE: Failure-Conditioned RL for Long-Horizon Software Engineering Agents](https://arxiv.org/abs/2610.07898)

**<font color=#1a73e8>作者：</font>** Jia Liufu, Bin Hu, Linglin Jing 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Repository-level software engineering (SWE) is a challenging long-horizon setting: agents must reason over extended interactions, use tools, and adapt to stateful environments. Recent work trains SWE agents with reinforcement learning methods such as Group Relative Policy Optimization (GRPO), which independently sample multiple trajectories per issue, test the resulting patches, and compare terminal rewards within a fixed group. However, this training setup does not reuse verifier feedback from failed patches as context for subsequent attempts, even though this feedback contains valuable diagnostic information about what went wrong. Training on recovery trajectories is challenging because the preceding outcome determines whether the next trajectory is generated, while the failed execution determines its conditioning context. We introduce FC-SWE, a failure-conditioned RL framework that incorporates recovery attempts into policy training. After a patch fails verification, FC-SWE restores the repository to its original task state and uses the failed patch and verifier feedback as context for a recovery trajectory. FC-SWE adapts GRPO to these chains of complete, multi-turn tool-use trajectories through two mechanisms. Trajectory-local rewards preserve each attempt's verifier outcome, preventing recovery success from rewarding an earlier failed patch. Active-set advantage estimation forms a comparison group from all initial and recovery trajectories actually executed for the same issue, so failed attempts remain in the group while unexecuted attempts are excluded. On all 500 SWE-bench Verified tasks under a verifier-assisted protocol, FC-SWE with Qwen3.5-4B and SWE-agent achieves 41.7% Resolved@1 and 52.8% Resolved@2, compared with 38.9% and 48.5% for GRPO. Although trained with at most two attempts per chain, FC-SWE reaches 70.7% Resolved@11 under an eleven-attempt test-time budget.

---


### 171. [Unsupervised Long-Tailed Adaptation of Vision-Language Models](https://arxiv.org/abs/2610.07903)

**<font color=#1a73e8>作者：</font>** Keliang Chen, Yaxin Hou, Hui Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting vision-language models to downstream tasks has achieved remarkable success by leveraging pseudo-labels generated from unlabeled data. Existing methods typically assume a uniform unlabeled data distribution, and thus the resulting pseudo-label distribution is likewise uniform. However, real-world data distributions are often long-tailed. To tackle this, we formalize a new scenario termed Unsupervised Long-Tailed Adaptation (ULTA). Under this scenario, existing methods exhibit a contrasting phenomenon: head-class performance drops sharply, which is distinct from supervised long-tailed learning where tail classes suffer the most. In particular, we uncover that the distributional mismatch not only erodes head-class boundaries, but also pushes head samples into confusable classes, reinforcing the model's inherent bias. To address these issues, we propose a novel model called Margin-Aware Refinement with Structural alignment (MARS). Specifically, we mitigate head-class boundary erosion via Boundary-Preserving Alignment, which takes the zero-shot VLM as a fixed visual reference to suppress probability increases that lack visual support in the training targets. Building upon this, we introduce Margin-aware Self-Refinement, which employs a dynamic adjustment strategy to refine tail and confusable classes while preventing prediction bias. Extensive experiments on nine benchmark datasets demonstrate that MARS outperforms state-of-the-art methods, achieving an average accuracy improvement of 4.71 percentage points.

---


### 172. [ApexQuant: Data-Free Elastic Quantization by Residual Re-Isotropization](https://arxiv.org/abs/2610.07904)

**<font color=#1a73e8>作者：</font>** Aksel Fristrup, Sumit Pandey, Ankit Kariryaa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce ApexQuant, a calibration-free quantization method that recursively re-quantizes the residual error, serving as a refinement layer on top of existing quantizers. We establish that a fresh random rotation returns each residual to the uniform distribution on the hypersphere, which characterizes the rate of progressive error decay across successive passes. This result lets us determine, before any weight is read, how many passes a layer needs for a target weight-space error. Every prefix is itself a valid lower-rate model, so one artifact serves several precisions. We instantiate ApexQuant with three interchangeable stages, scalar, $E_8$ and trellis, and validate it on four open-weight LLMs and on Earth-observation and medical domains where in-distribution data is often unattainable as imagery arrives under restrictive licences or due to patient material under privacy constraints. Progressive re-isotropization comes within a few percent of full precision at four bits and gives the best two-bit arm we measure, in a completely data-free setting.

---


### 173. [Multimodal Knowledge Distillation for Gastric Adenocarcinoma Classification from Whole-Slide Images](https://arxiv.org/abs/2610.07913)

**<font color=#1a73e8>作者：</font>** Shrihari Dumbre, Bikash Santra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gastric adenocarcinoma (GA) is a leading cause of cancer-related mortality worldwide, and accurate histopathological subtype classification from whole-slide images (WSIs) is essential for effective treatment planning. While multimodal approaches that integrate pathology report text with WSIs can improve classification, existing methods often depend on computationally expensive transformer architectures and large language models. We propose a multimodal knowledge distillation (MKD) framework that combines a pretrained WSI image encoder and a clinical text encoder using Low-Rank Multimodal Fusion (LMF) to efficiently model cross-modal interactions during training. Each WSI is represented as a bag of patches paired with a slide-level diagnostic caption. The teacher model learns fused image-text representations for subtype classification, while the student model distills this knowledge to enable accurate image-only inference. We evaluate our method on the PatchGastric benchmark dataset and achieve at least 3.35% higher mean accuracy than state-of-the-art approaches, without relying on transformer-based fusion, multi-task learning, or large language models. The source code is available at this https URL.

---


### 174. [TF-PRVR: Training-Free Partially Relevant Video Retrieval](https://arxiv.org/abs/2610.07925)

**<font color=#1a73e8>作者：</font>** Giyeol Kim, Chanho Eom  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Partially Relevant Video Retrieval (PRVR) aims to retrieve untrimmed videos containing moments relevant to a given text query. Despite recent progress, existing PRVR methods suffer from two key limitations: a fixed video decomposition scheme that causes semantic dilution, and source-domain overfitting induced by task-specific training. In this paper, we propose TF-PRVR, the first training-free framework for PRVR. TF-PRVR leverages frozen vision-language features to construct video-specific hierarchical representations. It derives temporal semantic signals from frame-level features and applies frequency-based multi-scale analysis to identify adaptive temporal boundaries, producing hierarchical segments with coherent event-level semantics. Built on these segments, TF-PRVR constructs a unified multi-scale graph and propagates query relevance across temporally and semantically related nodes. A moment-aware scoring strategy then aggregates temporally aligned relevance across scales, emphasizing consistently supported moments while suppressing isolated false responses. Without task-specific training, TF-PRVR preserves the general-purpose alignment capability of pre-trained vision-language models and avoids dataset-specific overfitting. Extensive experiments demonstrate consistent performance across datasets with diverse visual and temporal characteristics, suggesting a practical direction for training-free PRVR.

---


### 175. [SIGMA: Self-Improving Alignment Generalization from a Model Spec](https://arxiv.org/abs/2610.07935)

**<font color=#1a73e8>作者：</font>** Jingyu Zhang, Shruti Palaskar, Daniel Khashabi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly capable of executing complex tasks and of recursively improving themselves on easy-to-verify objectives such as software engineering and mathematics. Since alignment is much harder to verify, this creates a growing risk of capabilities increasing without appropriate safety alignment, especially as capabilities expand to auto-research and cybersecurity. Existing approaches focus on capability self-improvement using verifiable feedback or on alignment training with supervision from stronger models or curated data, creating an external supervision bottleneck for alignment. We ask whether current models can improve their own safety alignment, and propose SIGMA, a data generation and training pipeline enabling alignment self-improvement that generalizes to out-of-distribution settings. Given only a "Model Spec" stating the model's desired behavior, SIGMA leverages a model's reasoning capabilities to strengthen its own safety reasoning. SIGMA first performs spec-guided task synthesis, using the candidate model as a task designer agent to generate diverse alignment dilemma scenarios and convert them into training tasks that stress-test its understanding of the Model Spec. Next, SIGMA conducts self-judged alignment training through supervised fine-tuning and rubric-based reinforcement learning with the model itself as the reward model. Despite training only on single-turn chat data, SIGMA improves safety alignment in multi-turn agentic environments (AgentHarm harmfulness decreases from 22.6 to 14.8; Agentic Misalignment decreases from 79.1 to 3.8), outperforms Deliberative Alignment and Constitutional AI baselines, and retains general capability. Analyses show that a Model Spec balancing harmlessness and helpfulness, test-time reasoning for safety deliberation, and high-quality rubrics from SIGMA's task designer agent are crucial for effective self-improvement.

---


### 176. [Pseudowords as probes: Large Language Models show little of the sublexical sensitivity that governs human pseudoword processing](https://arxiv.org/abs/2610.07936)

**<font color=#1a73e8>作者：</font>** Jing Chen, Giulia Loca, Simona Amenta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systematicity, the probabilistic mapping of form to meaning, permeates language at all levels, and sublexical cues have been shown to govern human pseudoword processing. Yet whether LLMs exhibit comparable sensitivity to these cues remains unclear. We tested five LLMs on two Italian two-alternative forced-choice pseudoword experiments and compared their responses with a human behavioural baseline. LLMs aligned more reliably with humans when real-word options provided a lexical familiarity cue than in the pseudoword-only condition, where they fell substantially below fastText, a character-n-gram model. In addition, the sublexical cosine-similarity cue that reliably drove human--fastText agreement did not consistently transfer to human--LLM alignment, and reasoning-token expenditure bore no consistent relation to human processing difficulty. These findings suggest that LLMs do not necessarily share the sublexical cues that govern human pseudoword processing; we discuss tokenization and training-data coverage as candidate explanations.

---


### 177. [CCDF: A Benchmark Dataset for Deepfake Detection in Real-World Surveillance Footage](https://arxiv.org/abs/2610.07939)

**<font color=#1a73e8>作者：</font>** Baptiste Chopin, Thomas Swearingen, Arun Ross 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to rapid advances in Generative AI, commercial video generation tools can be used to produce fabricated surveillance footage that can fool both human viewers and automated synthetic video detectors. Since these tools are so widely accessible, a malicious user can create a harmful video clip at minimal cost. The production and dissemination of such videos in high-stakes settings, such as crime reporting and elections, can misdirect emergency response efforts or distort political discourse. Existing deepfake video datasets, used by the research community to develop deepfake detection algorithms, exhibit two limitations: (1) they emphasize benign web content rather than footage of possibly malicious activity, and (2) they rely on older or open-source generators that do not represent recent advances in generative systems. We assemble CCtv DeepFakes (CCDF), a video deepfake dataset, to address both gaps. CCDF contains 1840 videos (460 real and 1380 generated) spanning 16 crime and accident categories, with generated content produced using three leading commercial systems: Grok Imagine, Google VEO 3.1, and OpenAI Sora 2. CCDF is a highly realistic, small-scale, manually annotated dataset targeting evaluation of detection models. We release three versions of the dataset: the raw generated data, a cleaned version in which video metadata are standardized between real and synthetic samples to prevent detectors from exploiting trivial cues, and an altered version simulating low-effort post-processing attacks. We evaluate CCDF with ten recent state-of-the-art detectors covering different detection approaches. Our results suggest that these approaches do not reliably distinguish CCDF's generated videos from real ones, despite their strong reported performance on existing datasets. These results further confirm that existing datasets are not well-suited to evaluating certain threats.

---


### 178. [Hybrid Latent Attention for Looped Language Models](https://arxiv.org/abs/2610.07940)

**<font color=#1a73e8>作者：</font>** Yuhan Chen, Siyuan Zhang, Nan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped language models apply the same stack of layers T times to each token, which deepens the model without adding parameters but multiplies its key-value (KV) cache by T. The larger cache limits how many sequences a GPU can decode at once and slows each decoding step, which reads the whole cache. We propose Hybrid Latent Attention (HLA), which keeps exact keys and values within a sliding window of W recent tokens and stores each older token as a compact latent that the query of each loop reads directly, without reconstructing keys and values. We uptrain HLA on Ouro looped models (T=4) with 1.4B and 2.6B parameters, keeping the pretrained weights frozen and training only the added parameters to reproduce the original attention. The cache shrinks by 10.7x per token, fitting 4.0-8.8x as many concurrent sequences per GPU, and decoding throughput improves by 2.5x at 1K-token contexts and by up to 7.4x at 16K. HLA retains over 97% of the original accuracy on math, knowledge and reasoning benchmarks, and 96-100% on long-context retrieval up to 16K tokens. After supervised fine-tuning, it performs on par with the fine-tuned original model on competition-level math.

---


### 179. [Confidence Reasoning Graphs: Structured Confidence Estimation for LLM Agents](https://arxiv.org/abs/2610.07948)

**<font color=#1a73e8>作者：</font>** Brendan King, Farima Fatahi Bayat, Jean-Flavien Bussotti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When using an LLM agent in a consequential domain, making an informed decision about whether to trust its output or intervene requires calibrated confidence in the agent's success. Confidence estimation for agents is difficult because evidence about success is distributed across heterogeneous, interdependent steps of an agent's trajectory. Practical agentic deployments introduce further challenges: frontier LLMs often provide limited access to internal signals, agent roll-outs are costly, and training data may be unavailable or quickly become outdated. To address these challenges, we introduce Confidence Reasoning Graphs (CRGs), an inference-time framework that estimates the probability an agent accomplished its task from a single trajectory, without privileged model access or training data. Rather than compressing an execution into a single holistic judgment, a CRG begins with the claim that the agent accomplished its task, decomposes it into contextualized sub-claims grounded in trajectory evidence, estimates confidence for each terminal claim, and finally aggregates these into an overall confidence estimate. Across three agentic benchmarks, three backbone models, and three agent frameworks, CRGs yield better-calibrated confidence and stronger risk-aware decision making than verbalized, sampling-based, and white-box surrogate baselines. We further find that calibration error alone can be misleading: a white-box surrogate baseline appears well calibrated while providing near-chance discrimination. Ablations attribute CRG's improvements to claim-level confidence estimation and aggregation rather than graph construction alone. Finally, a CRG exposes the claims and trajectory evidence underlying each confidence estimate, enabling it to be audited at decision time.

---


### 180. [DecepEval: A Benchmark for Evaluating Deception in LLM Agents](https://arxiv.org/abs/2610.07967)

**<font color=#1a73e8>作者：</font>** Yiming Xu, Hongyue Yu, Beihua Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language model (LLM) agents become increasingly autonomous, they may pursue task performance through deception, raising concerns about their reliable deployment. Existing evaluations show that LLM agents can deceive, but often examine isolated scenarios or narrowly defined conditions, limiting systematic understanding of when deception becomes more likely. To address this gap, we introduce DecepEval, a benchmark comprising 1,532 instances across 3 task families and 28 professional scenarios. Drawing on classical fraud theories, we propose the LLM Deception Diamond framework, which characterizes four external conditions that may induce deception: pressure, incentive, opportunity, and conflict. DecepEval pairs neutral and induced versions of each instance to measure condition-dependent changes in deception rates, while explicit task facts and observable agent behavior help distinguish deception from capability-related errors. Evaluations of nine frontier LLMs show that inducements increase deception across models and task families, even among models with low baseline deception rates. DecepEval makes these vulnerabilities measurable, providing a shared benchmark for progress toward trustworthy artificial intelligence.

---


### 181. [M3SunAgent: Monocular 3D Spatial Understanding Agent for Metric Depth Estimation and 3D Visual Grounding](https://arxiv.org/abs/2610.07982)

**<font color=#1a73e8>作者：</font>** Jinsong Zhang, Kejun Wu, Ming Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular metric depth estimation and 3D visual grounding represent the two complementary cornerstones of monocular 3D spatial understanding (M3Sun), from which the fundamental 3D spatial information required by M3Sun can be acquired. However, these complementary tasks are generally conducted by separate frameworks, which pose challenges of inflexible and unaligned spatial information access for embodied intelligence systems. In this paper, we propose a unified agent for monocular 3D spatial understanding (M3SunAgent) that leverages a large language model (LLM) as a task planner for spatial visual programming, which flexibly generate structured programs and coordinate tools. For instance-level metric depth estimation task, M3SunAgent invokes an object detector tool to locate the target, estimates depth at selected points with a depth estimation tool, and aggregates these predictions into an instance-level depth estimate. We also construct the M3Sun Instance (M3SI) dataset, a benchmark with 2,910 samples for evaluation. For monocular 3D visual grounding task, M3SunAgent uses a vision-language model (VLM) tool to locate the target and output basic spatial attributes, then combines back-projection tool with a dimension-lifting tool to predict its 3D bounding box. Experimental results demonstrate the superior performance of M3SunAgent. Specifically, in evaluations of instance-level monocular metric depth estimation, M3SunAgent achieves the best performance among all compared models, 52.61% of predicted instances are distributed below depth error 0.25 ($\delta < 0.25$). In evaluations of monocular 3D visual grounding, M3SunAgent demonstrates overall competitive performance than vision and VLM models, reaching a 3D mean intersection over union (mIoU) of 41.73% and exceeding the state-of-the-art MonoVLM model by 3.62%.

---


### 182. [VisionWeave: Weaving Elastic Visual Representations as a Native Capability of MLLMs](https://arxiv.org/abs/2610.07987)

**<font color=#1a73e8>作者：</font>** Yuan Feng, Qize Yang, Ruizhe Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models have become the dominant paradigm for visual understanding, but incur substantial costs by encoding inputs into dense, fixed-size patch tokens. However, visual information is unevenly distributed: some regions require fine-grained detail, while others admit compact representations. Downsampling sacrifices this detail, while existing token pruning and adaptive approaches remain limited in content-adaptive granularity, task generalization, and integration with modern MLLMs and serving infrastructure. Overcoming these limitations calls for foundation models that learn, end to end, where-and at what granularity-to allocate visual representations, a native capability we term elastic visual representation weaving. We introduce VisionWeave, establishing this capability in frontier-level MLLMs through large-scale training. It combines two components: a gated spatial pooler constructs coarse-grained representations alongside native fine-grained representations within a shared MRoPE coordinate, while a granularity router learns their content-adaptive allocation. Through self-distillation alone, we validate this capability on Qwen3.5-4B and scale to Qwen3.8-27B with over 30K A100 GPU-hours. Based on Qwen3.8-27B, VisionWeave adaptively adjusts token savings to visual content, saving 43.0% tokens on average while retaining 98.9% native performance across eight benchmarks, versus only 88% performance preserved for token pruning baselines with a fixed 50% savings target. Extensive evaluations confirm robust efficiency-quality trade-offs across diverse tasks, resolutions and video frames. When deployed on SGLang serving engine, our method achieves a 2.3x throughput gain while reducing mean TTFT by 54.4% and mean TPOT by 60.6%. Together, we believe these results position elastic visual weaving as a promising capability for next-generation multimodal models.

---


### 183. [Structured but Silent: Probing Capability Requirements in LLM Hidden States](https://arxiv.org/abs/2610.08018)

**<font color=#1a73e8>作者：</font>** Kyojun Choo, Minsoo Song, Yunju Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable tool use requires more than triggering a mechanism or matching a query to an API description. Before selecting a specific tool, an agent must first infer the capability requirements implied by the user query. In this paper, we investigate whether these query-side capability requirements are linearly decodable from LLM hidden representations prior to generation, and how this hidden-state accessibility compares with explicit verbal classification. We introduce TACIT, a framework that decomposes external requirements along three fundamental axes: Source, Transformation, and World Effect, defining eight structurally distinct capability classes. Using 1,600 balanced training queries from benchmarks, synthetic examples, and new domain scenarios, we train linear probes on pre-generation hidden states from four open-weight LLM families. Our empirical results demonstrate that fine-grained capability structures are linearly decodable with high accuracy across all models. Crucially, however, we expose a representation-to-verbalization gap: these same models are significantly less reliable when asked to explicitly classify the same queries in natural language. This disconnect indicates that information about required external capabilities is linearly accessible in LLM hidden representations but not reliably expressed, a phenomenon we define as "structured but silent."

---


### 184. [The Labeling Problem in Hallucination Detection Benchmarks: An Empirical Evaluation](https://arxiv.org/abs/2610.08026)

**<font color=#1a73e8>作者：</font>** Jorma Valjakka, Juhani Kivimäki, Juha Mylläri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, several methods for detecting when large language models (LLMs) hallucinate have been developed. These methods are often benchmarked with open-domain question answering (QA) datasets containing questions and corresponding short reference answers. First, an LLM is used to generate answers to questions within the QA dataset. Then, some automated labeling strategy is used to label these answers as hallucinated or not by comparing them with the reference answers in the dataset. This evaluation setting creates a methodological ambiguity between two criteria: reference faithfulness (whether the answer is fully supported by the reference) and factual correctness (whether the answer is free from contradictions and factually false specific claims). In practice, automated labelers may apply the former criterion even when the intended target is the latter. We study this potential criterion mismatch using 900 human-labeled question-answer pairs spanning three commonly used QA datasets and three generator models, with labels targeting answer-level factual correctness. We evaluate lexical similarity metrics, a reference-entailment NLI baseline, and seven LLM judges under controlled prompt variants as automated labelers. Our experiments reveal substantial disagreement both among automated labeling strategies and between these labels and human annotations. Many strategies also exhibit strong directional error biases, and for most judge-generator pairs, replacing a faithfulness-oriented prompt with a factual-correctness prompt improves agreement with human annotations and reduces false-positive dominance, indicating that automated hallucination labels depend strongly on how the target criterion is specified. Label-source choice should therefore be considered a fundamental part of benchmark design and made explicit, validated, and matched with the benchmark goal.

---


### 185. [Same Feedback, Different Answer: Measuring Run-to-Run Instability in Frontier-Model Customer Feedback Analysis](https://arxiv.org/abs/2610.08036)

**<font color=#1a73e8>作者：</font>** Viraj Bagal, Raviraja Ganta, Prabhath Chellingi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly being programmed to automate knowledge work over large collections of unstructured data. Such automation requires repeatability: when the underlying evidence is unchanged, the agent's categories, priorities, and counts should not shift materially between runs, even if each individual answer appears plausible. We introduce a repeat-run evaluation framework that aligns semantically equivalent categories and focuses on two operating metrics: theme churn, the normalized change in the returned category set, and volume disagreement, the change in counts for categories that persist. We evaluate three recurring customer-feedback tasks across eight frontier models, corpus sizes from 100 to 5,000 records, multiple prompts, and three execution designs: raw generation, taxonomy-free hierarchical decomposition, and a taxonomy-grounded agent (TGA) using persistent themes, subthemes, and record-level predictions. With Claude Opus 4.8 and the 1,000-record corpus fixed, TGA reduces theme churn by 86--88% relative to both raw generation and hierarchical decomposition, while matched-theme volumes have zero disagreement. The taxonomy-grounded agent is more stable than every raw model in the screen, remains more stable at each corpus size, and keeps this advantage when theme matching is made stricter or looser. Although evaluated on customer feedback, the framework targets repeated synthesis of unstructured corpora more broadly, including financial reports, legal documents, incident records, and scientific literature. Overall, these results show that taxonomy grounding produces more consistent and repeatable outputs for recurring knowledge work.

---


### 186. [Are Language Models Script-Aware?](https://arxiv.org/abs/2610.08037)

**<font color=#1a73e8>作者：</font>** David Kletz, Sandra Mitrović, Ljiljana Dolamić 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models frequently generate outputs in unintended languages or scripts, a phenomenon known as off-target generation. While existing research has focused on language selection, the dimension of script knowledge remains understudied: before any linguistic understanding can occur, users must recognize the graphic symbols in a model's response. We investigate whether Small and Large Language Models (SLMs and LLMs) possess script knowledge by testing them on multi-scriptic languages. Through two complementary experiments, we evaluate whether models (1) adapt their output script to match the input, and (2) follow explicit instructions to generate text in a specified script. The models we tested demonstrate substantial script knowledge: they all achieve a near-perfect Latin script fidelity (more than 98%) and follow script instructions with high frequency. Nevertheless, we notice differences between LLMs and SLMs, with higher scores for LLMs including for non-standard script combinations.

---


### 187. [DAEDALUS: Bootstrapping Agent Memory from Self-Generated Tasks](https://arxiv.org/abs/2610.08048)

**<font color=#1a73e8>作者：</font>** Antoine Edy, Max Conti, Victor Xing 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents often lack the operational knowledge to act reliably in new environments, as they must discover specific tool behaviors or environment conventions on their own. Without memory of past attempts, they repeat the same mistakes across tasks, leading to more task failures and longer trajectories. To address this, agentic systems typically rely on human-written guidelines or on procedural memory built from training tasks and an oracle verifier, both of which require prior knowledge of the environment. We present DAEDALUS, a method for bootstrapping reusable agent memory from self-generated practice without existing tasks or oracle verifiers. DAEDALUS pairs two agents: an explorer that interacts with the environment to generate challenging yet solvable tasks, and a solver that attempts them. A heuristic is derived from each solver failure and accepted only after the solver repeatedly succeeds with that heuristic in context. These outcomes also provide feedback for the explorer to refine the difficulty of future tasks. Accepted heuristics are then consolidated into a memory bank for test-time use. Across AppWorld, $\tau^2$-bench, and AutomationBench, DAEDALUS improves mean success rates by up to 15.9 points and pass^5 by up to 2.2x over a no-memory baseline, and is competitive with methods using training tasks, at a lower inference cost than most. We show that performance gains already emerge with a small exploration budget, and that its heuristics also benefit agents from other model families. Our ablations further reveal that solver traces provide the key information needed to derive effective heuristics, while factorizing early discoveries makes exploration more cost-efficient. Beyond memory construction, we find that the tasks generated by DAEDALUS can serve as a proxy for benchmark tasks when ranking models by performance. Code and artifacts: this http URL.

---


### 188. [Language Carries the Expert's Impression: Instrument-Anchored LLM Judges Transfer Counseling-Quality Assessment and Beat In-Domain Training](https://arxiv.org/abs/2610.08055)

**<font color=#1a73e8>作者：</font>** Tobias Hallmen, Elisabeth André  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic assessment of communication quality in dyadic counseling conversations is bottlenecked by data: expert-rated corpora are small and expensive to grow. We study cross-domain transfer of expert overall-impression prediction across three German corpora of simulated counseling (two general-practice medical, one school-related parent-teacher; $n=195$ expert-rated sessions, one corpus after scale equating). Training on the other domains beats training in-domain: leave-one-domain-out transfer reaches nested Spearman $\rho = 0.54$ against $\le 0.48$ within the target domain, a paired session-level gap of $+0.15$ that holds at $+0.12$ when the training-set sizes are matched, so it is not simply data volume. The decisive features are session-level construct scores from small open-weight LLMs reading the two-speaker transcript, with the constructs largely derived from the experts' rating instruments: the instrument-derived battery lifts a single judge from $0.32$ to $0.41$ over generic dialogue qualities, judges from three model families ensemble to $0.51$ language-only, and a nonverbal-dyadic block adds $+0.03$ more, not separable from noise at this sample size. We also price the recording setup: one corpus lost its per-speaker audio, 16% of its diarised segments carry the wrong speaker, and repair is worth $+0.07$ there. At practically attainable corpus sizes, the expert's overall impression is carried by what is said, and by other communication programs' data more than by one's own.

---


### 189. [ASCENT: First-Order Optimal Fine-Tuning with Recalibration for Safety--Utility Co-Enhancement](https://arxiv.org/abs/2610.08061)

**<font color=#1a73e8>作者：</font>** Weiwei Qi, Chongyu Wang, Tianhang Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning can substantially improve the downstream utility of large language models (LLMs) but may compromise their safety. Existing safety-preserving methods constrain downstream updates using safety-related parameters or subspaces, but mainly focus on safety preservation rather than joint safety and utility enhancement, lack a theoretical characterization of the optimal safety-related subspace and safety-preserving task update, and typically rely on a static safety subspace that may become outdated during fine-tuning. To address these limitations, we propose ASCENT, a downstream fine-tuning framework for safety--utility co-enhancement through first-order optimal safety-aware periodic calibration and task optimization. We model safety as a function of LLM parameters $S(\theta)$ and use its first-order approximation to characterize safety changes under parameter updates. Under a fixed rank and Frobenius-norm budget, we prove that the update constructed from the top-$r$ singular components of the safety-function gradient maximizes the estimated safety change, and use it for periodic calibration to preserve and improve safety. We further derive a unique safety-preserving task update that stays close to the original task update while penalizing negative effects on the estimated safety change. ASCENT alternates these optimal task and calibration updates to jointly enhance safety and utility. Experiments across multiple LLM families and downstream tasks show that ASCENT improves downstream utility by up to 20.3\% and reduces attack success rate by up to 35.5\%, achieving state-of-the-art safety and utility across all evaluated settings. Our code is available at this https URL.

---


### 190. [PhysTacGen: Physics-Aware Visual-Tactile Sensor Image Generation](https://arxiv.org/abs/2610.08068)

**<font color=#1a73e8>作者：</font>** Guo Tang, Yongtao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Realistic physical interaction is a cornerstone of embodied intelligence, yet collecting paired visual--tactile data remains costly. Visual-to-tactile synthesis offers a promising approach to augmenting such data, but learning this mapping is complicated by the gap between visual appearance and contact-related material properties, as well as spatial misalignment in paired observations. To address these challenges, we present \textbf{PhysTacGen}, a visual-to-optical-tactile image generation framework that integrates material-aware descriptions with geometric conditioning. First, we introduce Group Tactile Policy Optimization (GTPO), a reinforcement learning strategy that refines a vision--language model to generate structured material descriptions using task-specific rewards. Second, we combine DINOv2-based pair curation with monocular relative-depth estimation to select training pairs and provide geometric priors. Finally, an SDXL ControlNet synthesizes optical tactile images conditioned on RGB, relative depth, and GTPO-generated text. Experiments on curated SSVTP data demonstrate improved structural similarity over the compared baselines, while a blinded user study shows a preference for GTPO-generated descriptions. Generated tactile inputs also improve performance on an attribute-derived force-coefficient prediction proxy. Together, these results demonstrate the effectiveness of PhysTacGen for optical tactile image synthesis and its utility in the evaluated downstream this http URL code will be available at this https URL.

---


### 191. [Two Halves are More than One: Phase-wise Velocity Distillation for Fast and High-Quality Image Generation](https://arxiv.org/abs/2610.08070)

**<font color=#1a73e8>作者：</font>** Zhen Guo, Rongyuan Wu, Qiaosi Yi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion-based image generation backbones have grown substantially in scale, making the network inference cost increase rapidly. While diffusion distillation techniques can reduce the number of inference steps, high-quality image generation within a single full-backbone-forward compute budget remains challenging. Existing one-step methods typically allocate this budget to a single evaluation of a monolithic student. However, approximating the heterogeneous coarse-to-fine transport with a single monolithic mapping is difficult and often leads to over-smoothed outputs. To address this issue, we propose Phase-wise Velocity Distillation (PVD), which partitions the generation timeline into a coarse and a fine phase, and models the transition within each phase via the average velocity. A dedicated half-sized expert is assigned to each phase, decoupling structural composition from detail refinement while keeping the cumulative computation equivalent to one full-backbone forward pass. We show that the use of two half-sized phase-specific experts outperforms a single full-size monolithic student. On class-conditional image generation, PVD achieves an FID of 1.48 on ImageNet 256 x 256. On more complex text-to-image (T2I) tasks, PVD-distilled models (Stable Diffusion 3.5-Medium, FLUX.1-dev, Qwen-Image) produce results competitive with their multi-step teachers, significantly outperforming prior distillation methods. Moreover, across the evaluated T2I backbones, PVD reduces active parameters by 49.10-50.89% and peak VRAM by 45.76-48.36% compared to the corresponding teachers. Source code and distilled models are available at this https URL.

---


### 192. [SpeedrunBench: Challenging LLM Agents with Video Game Speedrunning](https://arxiv.org/abs/2610.08076)

**<font color=#1a73e8>作者：</font>** Yoshinari Fujinuma, Keisuke Kamahori, Ryuto Koike 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier LLM agents have been shown to be capable of solving increasingly complex tasks for which humans have measurable solutions. This begs the pertinent question of whether LLM agents can go beyond what humans have already solved. The ability to develop sophisticated strategies to tackle consequential problems becomes paramount as well-trodden, human-developed solutions become insufficient for problems for which we lack context or enough training data. We study agents' capability of such strategy formation through the communal practice of video game speedrunning. In speedrunning, practitioners compete to find the fastest way to complete a video game under certain conditions, and in so doing uncovering interesting unorthodox play styles that require a thorough understanding and mastery of the underlying game mechanics. We introduce SPEEDRUNBENCH, a benchmark that evaluates frontier LLM agents across 9 different games. To perform well in this benchmark, agents must repeatedly improve their strategy, reflect on their performance, exploit their gained knowledge, and reason across a long-horizon of actions to improve on an increasingly difficult problem: being faster than themselves and everyone else. Our experiments show that while frontier agents approach human world records in simple platformer games, they remain behind human performance on longer, more complex games under practical budgets. These results suggest that SPEEDRUNBENCH is a useful testbed for studying agents' strategy formation capabilities as well as being a saturation-resistant evaluation measure, as there is almost always a faster completion time waiting to be discovered.

---


### 193. [POLAR: Ontology-Guided Risk Prevention for Tool-Calling LLM Agents](https://arxiv.org/abs/2610.08082)

**<font color=#1a73e8>作者：</font>** Yunju Kang, Seonghyeon Cho, Irene Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM tool-use agents operate in dynamic environments where many actions carry operational risk. However, most safety mechanisms react only after errors manifest. Existing pre-emptive approaches either fine-tune the agent on chain-of-thought deliberation or compile natural-language guardrails into runtime checks, but they do so without exposing a structural, auditable verdict. We propose POLAR, a guardrail framework for small tool-calling agents that assesses reversibility through a structured two-layer ontology. POLAR assigns each action a graded reversibility score by deriving a candidate inverse sequence; calls failing a threshold are pruned before execution. Evaluated on $\tau^2$-bench across six agent models, POLAR improves mean task reward by 0.11 to 0.18 points on airline for four of six agents, but only eight of eighteen model--domain cells improve overall; retail and stronger agents often regress. POLAR provides an auditable structural check and characterizes its task-utility trade-offs. Reward is not a direct measure of prevented harm.

---


### 194. [DirectSpeech2LLM: A Simple End-to-End Framework to Mitigate Prompt Overfitting in Speech-LLMs](https://arxiv.org/abs/2610.08085)

**<font color=#1a73e8>作者：</font>** Hemant Yadav, Sunayana Sitaram, Roger Zimmermann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-LLMs often exhibit prompt overfitting, where models solely trained on automatic speech recognition (ASR) instruction fail to generalize to new instructions such as speech translation and continue to behave primarily as ASR system. We propose DirectSpeech2LLM, a simple end-to-end framework that preserves the instruction-following ability of the LLM on unseen tasks when conditioned on speech. It computes distance-based CTC loss over the frozen LLM embedding matrix and uses greedy CTC labels to derive geometrically and temporally aligned speech embeddings respectively as an input to the LLM. Trained solely on 960 hours of LibriSpeech ASR data, DirectSpeech2LLM outperforms the cascaded system on ASR (seen task) and generalizes zero-shot to speech translation and emotion recognition (two unseen tasks), closely matching the cascaded system upper bound on these two new instructions despite seeing neither during training. We also find that geometric alignment strength plays a smaller role than previously assumed, as our modified CTC loss is shown to provide sufficient implicit geometric grounding without requiring an explicit regression loss. Results are consistent across two LLM families and scale with both more training data and model capacity.

---


### 195. [Explainable Rule Mining of IPv6 Extension-Header Presence Patterns from Paired-Vantage Captures](https://arxiv.org/abs/2610.08090)

**<font color=#1a73e8>作者：</font>** Priyanka Sinha, Nikolaos Kekatos, Stylianos Basagiannis 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> IPv6 extension headers (EHs), such as fragmentation, segment routing, and in-situ telemetry, are operationally important yetwidely dropped in transit, and characterising their behaviour from packet captures is a recurring measurement problem. We ask whetheran explainable miner can recover human-readable rules of EH behaviour, and we contribute two reusable tools: a negative-control protocol that diagnoses whether a mined "temporal" network rule reflects genuine cross-packet dynamics or mere within-packetco-occurrence, and a sender-conditioned, per-family EH-retention measurement. Applying an interpretable temporal-logic rule miner to the JAMES paired-vantage dataset, we recover a portable Fragment-EH rule that the protocol reveals to be a within-packet,near-definitional co-occurrence rather than a temporal pattern, so the temporal-logic machinery does no work for this dominant rule;the retention measurement independently recovers the expected within-window ordering of EH observability. Our main result istherefore an honest, controlled negative finding, corroborated by executed decision-tree and large-language-model baselines: on theevaluated JAMES traces network-temporal structure does not carry the dominant Fragment-EH signal, and we supply the controls thatestablish when it would, validated on a synthetic positive control containing a genuine cross-packet dependency.

---


### 196. [SAGE: Semantic Anchor-Guided Evolution for Grounded Medical QA Data Synthesis](https://arxiv.org/abs/2610.08093)

**<font color=#1a73e8>作者：</font>** Chuan Li, Chengyu Wang, Cen Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Developing reliable models for clinical tasks, such as Medical Question Answering (QA), is severely constrained by the limited availability of high-quality, expert-annotated training data. This challenge is exacerbated by stringent privacy requirements and the impracticality of utilizing large open-source corpora or proprietary cloud APIs within resource-limited clinical settings. To address these obstacles, we introduce SAGE (\textit{Semantic Anchor-Guided Evolution}), a novel data synthesis framework that enables small, locally deployed models to generate high-quality medical training data. SAGE leverages lightweight, publicly available taxonomies such as MeSH as semantic anchors, imposing a structured prior to effectively guide and ground the data generation process. At its core, SAGE iteratively interleaves atomic (individual concept-based) and associative (relation-based) synthesis, bootstrapping training data from minimal seeds. This approach eliminates the need for large collections of medical documents or reliance on external APIs, providing a practical solution for on-premises data creation. Extensive experiments across multiple medical question-answering benchmarks demonstrate that models fine-tuned with SAGE-synthesized data consistently outperform those trained using self-derived or conventional document-based paradigms, highlighting tangible improvements in data efficiency and resource utilization for medical LLM development. Code is available at this https URL.

---


### 197. [Natural Language Questions as an Interface for Knowledge Graphs: QRAKEN Graph Distillation and Semantic Self-Healing](https://arxiv.org/abs/2610.08095)

**<font color=#1a73e8>作者：</font>** Remo Grillo, Lukas Klic, Giovanni Colavizza  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural-language access to RDF knowledge graphs is a core Semantic Web ambition. Large language models (LLMs) have advanced Text-to-SPARQL, yet on unfamiliar graphs they often generate valid queries that misrepresent the populated data model. QRAKEN is a training-free, ontology-agnostic neurosymbolic pipeline grounding generation in empirical graph evidence rather than schema expectations. An offline distiller produces TTQL, a compact description of populated multi-hop patterns, conditional frequencies and path-conditioned literal examples, plus a class-property co-occurrence matrix. Online, TTQL guides the LLM, while deterministic syntax, vocabulary and data-model checks provide diagnostics for iterative refinement. On CK25 (First International Text2SPARQL Challenge), under matched-condition recomputation on a QLever snapshot, QRAKEN achieves strict F1 of 0.643 $\pm$ 0.026 with GPT-4.1 mini and 0.652 $\pm$ 0.012 with GPT-5.4: relative gains of 30% and 32% over the strongest recomputed participant, outperforming systems using the same base model family. Ablations identify TTQL patterns as the dominant driver (+0.31 strict F1 over a shape-only baseline); the refinement loop provides a cheap safety net, rejecting triple patterns unsupported by the co-occurrence matrix. Compared with auto-derived SHACL, TTQL yields 64% higher strict F1, supporting the value of empirical patterns beyond schema exposure. With two local 35B 4-bit open-weight models at zero marginal cost, the same pipeline matches the strongest recomputed participant, and TTQL advantages over shape-only and SHACL baselines persist. Results on a single, relatively small benchmark provide an initial empirical signal; monolithic TTQL injection on very open cross-domain graphs remains the main limitation.

---


### 198. [Surviving the Router: Optimizing Skill Injections for Retrieval and Execution](https://arxiv.org/abs/2610.08098)

**<font color=#1a73e8>作者：</font>** Haneen Najjar, Luca Scionis, Haritz Puerto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly rely on modular third-party "skills" that are dynamically selected by skill routers to execute complex tasks. While recent studies highlight the threat of prompt injections embedded in these skills, existing evaluations often assume settings where the malicious skill is already selected for execution. We show that this assumption can substantially overestimate attack success. In realistic multi-skill environments, injected skills must first compete for retrieval, reducing the effective attack success rate (ASR) of existing injections by 87-97%. To address this limitation, we introduce CORSA (Cluster Optimization for Router-Aware Skill Attacks), a router-aware attack that optimizes skill injections for both retrieval and execution across clusters of related tasks. We evaluate skill injection attacks under router-managed multi-skill settings by extending the benchmark introduced by SkillRouter with eight malicious payload categories. CORSA uses successive optimization stages to first improve retrieval and then optimize end-to-end attack success, while we evaluate user utility and injection naturalism separately. Our experiments show that CORSA substantially improves both retrieval and end-to-end attack success over existing skill injections while preserving user utility, and that the resulting attacks transfer across different router architectures and LLM backbones.

---


### 199. [Beyond Corrected Memory: Execution Consistency in Multi-Agent Systems](https://arxiv.org/abs/2610.08101)

**<font color=#1a73e8>作者：</font>** Zhe Yu, Zixuan Wang, Peidong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Shared memory coordinates agents' actions, but correct records do not establish that those actions satisfy task requirements. Memory governance and failure diagnosis regulate or inspect recorded information; they do not by themselves establish whether it is sufficient to judge task duties. We define execution consistency through duties governing state use, information handoffs, and final-state agreement, with explicit evidence conditions for judging fulfillment. Our core claim is that identical retained records can correspond to compliant and violating executions under the same task rule. Controlled removal of evidence such as receipt, action dependence, or response validity leaves 82.4% of opposite-label pairs indistinguishable; restoration separates 97.9% of the merged pairs. Natural-log annotations identify the defined violations in actual executions. However, existing logs do not always explicitly represent the execution relationships needed for these judgments. To assess the definition's practical value, we use CAVERT, a framework for consistency diagnosis and recovery, to extract supported relationships from logs and apply these criteria. It consistently outperforms contract-prompted LLM and rule-based baselines in diagnosis across all 12 benchmark-executor settings. Under the same gate and executor limits, it also outperforms rule-guided recovery in all four evaluated environments. These findings identify execution evidence that agent-memory and execution interfaces should preserve for reliable judgment.

---


### 200. [DSV-Mem: Evaluating Multimodal Memory in Professional Workflows for MLLM Agents](https://arxiv.org/abs/2610.08102)

**<font color=#1a73e8>作者：</font>** Jike Zhong, Ritwick Chaudhry, Xuanbai Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational MLLM agents are increasingly expected to assist in professional workflows, from AI research and engineering design to product management and business operations. Yet this capability remains underexplored: existing benchmarks largely focus on informal, everyday interactions and personal-life scenarios featuring photographic natural images, isolated static artifacts, and recall-oriented questions. In contrast, professional scenarios often involve structured, information-heavy artifacts that undergo frequent revisions and authority updates, and compositional queries requiring reconciliation of many artifact versions while tracking state precisely. To address these challenges, we introduce DSV-Mem, a benchmark for evaluating Dense Stateful Visual Memory. DSV-Mem comprises expert-reviewed scenarios and 1,000 questions across five user-oriented categories (Current State, Past State, Derived State, Change History, and Conflict/Refusal). A Hartley-inspired criterion favors questions with broader visual-evidence inspection demands. We also introduce a generation harness that produces evaluation suites by decoupling state-transition synthesis from conversation filling. Evaluation over 27 configurations spanning frontier and open-weight models and memory management methods reveals that the strongest baseline scores below 45% on DSV-Mem. Analysis surfaces findings: 1) multimodality and information density both contribute to difficulty, but state evolution, particularly the number of governing updates, is the dominant tested factor. Raw conversation/haystack length, OCR, and arithmetic are not the primary bottlenecks; 2) models often fail to verify user premises against prior state updates before answering; 3) increased reasoning effort and memory management methods yield limited gains, whereas state-aware designs prove more effective. The benchmark and code will be publicly released.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-303](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
