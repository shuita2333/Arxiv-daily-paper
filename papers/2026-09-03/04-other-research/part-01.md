# 📦 其他研究 | 2026年09月03日

> 本类共 **236** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-236](./part-05.md)

---

### 1. [I-CARE: Analysis of interference-related phenomena in a controllable, diverse and representative unlearning setting for text-to-image models](https://arxiv.org/abs/2609.00003)

**<font color=#1a73e8>作者：</font>** Leonardo Santiago Benitez Pereira, Marcos Escudero Viñolo, Luis Herranz Arribas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine unlearning studies the removal of knowledge from an AI model, making the system forget a concept it previously learned. Despite rapid progress in generative machine unlearning, the unintended degradation of semantically related concepts that should have been retained (henceforth, interference) remains poorly characterized and inconsistently evaluated. This paper introduces I-CARE, a methodology that formalizes interference as a first-class object of study in generative unlearning. Rather than proposing a new benchmark or unlearning algorithm, I-CARE provides formal definitions for tasks, metrics, and templates for reporting results, enabling the systematic and reproducible study of interference across unlearning settings. While our methodology is designed to remain valid as models and unlearning algorithms evolve, decoupling long-term scientific insight from transient empirical results, we present a feasibility demonstration with state-of-the-art algorithms and frequently used datasets. The results demonstrate that I-CARE enables meaningful analysis of interference patterns across multiple unlearning settings, establishing the practical applicability of the framework. The software implementation of the methodology is provided in an open-source framework, together with a web-based graphical interface that enables exploration of the outcomes of this study without requiring direct interaction with the codebase or specialized data analysis tools.

---


### 2. [Discrete-Time MDP Modeling for Multi-Item Capacitated Lot Sizing with Stochastic Demand Timing](https://arxiv.org/abs/2609.00004)

**<font color=#1a73e8>作者：</font>** Léa Bayati, Mohamed Dahmoune, Melek Rodoplu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper studies a finite-horizon multi-item capacitated lot-sizing problem in which demand quantities are deterministic, while demand-arrival periods are stochastic. Each demand occurs once within a known time window and must be satisfied no later than its deadline. The proposed model makes production and allocation decisions at the demand level, allowing it to represent capacity competition, demand-specific backlog, and allocation-dependent inventory dynamics. The stochastic problem is formulated as a discrete-time Markov decision process (DTMDP), including the state space, feasible actions, transition kernel, and one-period cost function. To isolate the computational effect of stochastic timing, each stochastic instance is first compared with a deterministic counterpart in which each arrival distribution is replaced by its most likely arrival period. This comparison shows that stochastic timing substantially increases the number of states, the number of transitions, solution time, and memory pressure. A genetic algorithm (GA) is then proposed for the stochastic-timing problem. The GA searches over feasible state-feedback policies and evaluates each policy exactly under the DTMDP transition model. Computational experiments on 330 benchmark instances show that the GA remains close to the exact stochastic solution whenever the latter is available, with an average optimality gap of about $3.44\%$. On the difficult benchmark instances, comprising 90 test cases, the GA remains below the $5\%$ optimality-gap threshold and achieves an average optimization speedup of $6.89 \pm 1.41$ at the $95\%$ confidence level. For instances that cannot be solved exactly on the available hardware, an empirical Bellman-time regression is used to estimate the missing exact resolution time and extrapolate the expected GA speedup.

---


### 3. [Collaboratively Eliciting Gestures for Geospatial Data Exploration on an MSE with Tangibles and Styluses](https://arxiv.org/abs/2609.00007)

**<font color=#1a73e8>作者：</font>** Karen Penaranda Valdivia, Nujaimah Ahmed, Aswah Butt 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large tabletop displays and multi-surface environments offer potential for enhancing visual data exploration and collaborative work with geospatial datasets. These systems typically rely on multi-touch interactions, which can pose challenges when the multi-touch sensors misrepresent transitory movements as control inputs, leading to interruptions. Active tangibles and styluses offer an alternative to multi-touch interactions in MSEs, and have shown the potential to facilitate sense-making around large datasets. However, further research is needed to better understand how these modalities can be effectively leveraged for interacting with geospatial data visualizations. To address this, a gesture elicitation study was conducted in which users suggested interactions for 16 geospatial data visualization tasks, presented as a realistic collaborative workflow co-designed with geography and migration researchers. The study produced a taxonomy of user-defined gestures using tangibles and styluses for engaging with geospatial data, along with a thematic analysis of users' experiences with visualization tasks and interaction techniques.

---


### 4. [UI-Venus-2 Technical Report](https://arxiv.org/abs/2609.00028)

**<font color=#1a73e8>作者：</font>** Venus Team, Zhuohan Cai, Haoxing Chen 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal GUI agents have emerged as a promising paradigm for digital task automation, yet transitioning from benchmark-oriented models to dependable real-world applications remains challenging due to limited environment coverage, brittle task construction, and unreliable reward verification. In this work, we present UI-Venus-2, a general-purpose foundation GUI agent designed to operate across mobile, web, and desktop environments through a unified closed-loop reasoning-action framework. To bridge the gap toward practical deployment, we jointly scale three critical dimensions: (1) Environments, expanding coverage to more than 170 multilingual mobile apps and native desktop operating systems; (2) Tasks, employing a deep-research pipeline for function-grounded instruction generation; and (3) Verification, adopting trace-level and sample-level evaluators with visual keypoints and multi-model voting to ensure reliable RL signals for training. Furthermore, we integrate safety-aware mechanisms to ensure controlled execution of consequential actions. By offering a capable, efficient, and open-source foundation, UI-Venus-2 advances the field toward more generalizable, verifiable, and self-reflective agents for real-world applications.

---


### 5. [EULER: Exploring Underused Links with Evidence-Checked Return for Multi-Agent Mathematical Discovery](https://arxiv.org/abs/2609.00032)

**<font color=#1a73e8>作者：</font>** Ren Zhenzhuo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematical communities work with different objects, invariants, and tools, so transferring a problem across them is expensive and often skipped. We present EULER, a multi-agent system that takes such a transfer--a bridge--as its unit of search. Around a fixed conjecture, EULER runs direct, adjacent-domain, and distant-domain routes in competition; a bridge keeps its budget only if it supplies an operation the source representation cannot execute and its target-side evidence returns to the original statement along a checked implication. Six ordered stress tests reject invalid bridges before expensive search begins.
We evaluate EULER on 120 recent conjectures. The conjectures were frozen before search and screened for contamination, and are drawn from public papers by authors who had recently published in the Journal of Combinatorial Theory, Series A, a leading journal in combinatorics. EULER produced 10 proofs and 3 refutations, plus 45 scoped partial results. Two mechanisms held up under ablation: bridge-specific stress tests cut incorrect conclusions from 9 to 3, and bridge material combined with a target-native operation yielded a positive interaction of +4.2 resolved tasks that neither factor produced alone. Domain distance did not reliably predict success; executable operation gain and valid return did.

---


### 6. [A Cone-Constrained Bilinear Decomposition for Total Scaled-Gradient Variation Models](https://arxiv.org/abs/2609.00036)

**<font color=#1a73e8>作者：</font>** Haibin Su, Chunlin Wu, Huibin Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The total scaled-gradient variation (TSGV) regularizer, derived from sparse modeling of piecewise-linear structures, has been shown to preserve edges and corners in image restoration. However, its highly nonconvex and nonlinear nature poses severe computational challenges, as existing methods often suffer from parameter sensitivity or lack convergence guarantees. To overcome this, we propose a tailored bilinear decomposition that decouples the nonlinear weighted gradient in the TSGV regularizer. This approach yields an equivalent optimization problem governed by cone or sphere constraints, depending on the chosen scaling function. In particular, the cone constraint plays a central role in characterizing edge- and corner-preserving behavior. We solve this reformulation using the alternating minimization method (AMM) equipped with a majorization--minimization strategy, ensuring a monotonic decrease in energy without step-size tuning. Furthermore, we provide a geometric interpretation of the edge-preserving properties of these constraints by analyzing their asymptotic behavior near image singularities. We establish the global convergence of the proposed method to a critical point within the Kurdyka--Łojasiewicz framework. Extensive numerical experiments on Gaussian denoising and non-line-of-sight (NLOS) imaging show that the proposed method achieves PSNR and SSIM competitive with or superior to representative variational methods, especially at high noise levels, and improves the structural reconstruction under dense and sparse scanning.

---


### 7. [RAPIDMap: Rapid Multi-Agent Pipeline for Interpretable Disaster Mapping from Satellite and Street-view Imagery](https://arxiv.org/abs/2609.00046)

**<font color=#1a73e8>作者：</font>** Yifan Yang, Lei Zou  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Rapid and reliable disaster mapping of impacted areas, damaged infrastructure, and affected populations is essential for emergency response and recovery. However, existing AI-based approaches often require extensive manual annotation, lack cross-hazard generalization, and rely on single-modal observations. To address these challenges, this paper proposes RAPIDMap, a rapid multi-agent pipeline for zero-shot interpretable disaster mapping from satellite and street-view imagery. The framework integrates four intelligent agents: Disaster Perception Agent (DPA), Image Restoration Agent (IRA), Damage Recognition Agent (DRA), and Disaster Mapping Agent (DMA). By combining remote sensing and street-view data, RAPIDMap eliminates the need for manual fine-tuning, generalizes across multiple disaster categories, and generates structured, map-ready disaster intelligence with recovery recommendations.

---


### 8. [Task-Specific Prompt with Global Context for Multi-Task Graph Pre-Training](https://arxiv.org/abs/2609.00047)

**<font color=#1a73e8>作者：</font>** Zhiyang Qiu, Yangtao Wang, Xiaocui Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph prompt learning is an effective paradigm to adapt pre-trained graph models to downstream tasks in low-resource scenarios. However, existing multi-task graph pre-training frameworks generally use randomly initialized prompts, leading to poor alignment between the prompt space, pretext objectives and graph structural characteristics. This greatly weakens the task relevance, structural awareness and transferability of prompt representations. To address this challenge, we propose TPGC, a dual-prior prompt initialization solution that explicitly models the synergy between task prior and structural prior. Specifically, the Task-Prior Injection Module first conducts a short homologous multi-task pre-training on an auxiliary graph, enabling prompt initialization to inherit optimization preferences associated with multiple pretext tasks. Built on the task-aware representations, the Structure-Prior Injection Module further extracts transferable global structural context from the auxiliary graph, converting it into layer-wise prompt vectors by aggregating structurally informative node embeddings. Extensive experiments on 6 mainstream benchmarks covering node and graph classification show that TPGC achieves consistently better performance under few-shot settings than state-of-the-art baselines, with fewer downstream tunable parameters and lower runtime. The code is available at this https URL

---


### 9. [GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments](https://arxiv.org/abs/2609.00048)

**<font color=#1a73e8>作者：</font>** Lin Fu, Zheyuan Yang, Tianhui Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> GUI world models are increasingly evaluated as one-step next-screen predictors, yet their intended use is often as multi-step environments for GUI agents. This mismatch leaves a key requirement under-tested: generated states must remain contextually consistent when they are repeatedly reused for future interaction. We introduce GUI-CC, a benchmark that evaluates contextual consistency of GUI world models as agent environments rather than isolated next-screen predictors. GUI-CC contains two complementary tracks: an offline reference-action track that rolls models along real mobile GUI trajectories, and an online agent-loop track that lets fixed probing agents interact with model-generated UIs. We construct 500 offline trajectory tasks from GUIOdyssey and 200 emulator-verified online tasks across 30 mobile apps. GUI-CC evaluates transition fidelity, transition plausibility, contextual consistency, and task progress. Experiments show that plausible single-step generation does not guarantee reliable environment simulation: current models often produce usable-looking screens while failing to preserve task-relevant context or support executable multi-step rollouts.

---


### 10. [Convergence issues in Relational Concept Analysis based on AOC-posets](https://arxiv.org/abs/2609.00054)

**<font color=#1a73e8>作者：</font>** Xavier Dolques, Agnès Braud, Alain Gutierrez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Formal Concept Analysis (FCA) is an approach for conceptual classification building and rule discovery from a binary table describing a set of objects by a set of attributes. Extensions have been proposed to deal with non-binary and more complex data, such as Relational Concept Analysis (RCA) for multi-relational data. RCA aims to highlight groups of objects characterized by their relationships with other groups of objects. The richer and more complex nature of the underlying data allows RCA to produce richer results than FCA, at the expense of higher computational and interpretive complexity. The most commonly used conceptual classification structure in FCA is the concept lattice. However, in many applications, concept lattice substructures, such as AOC-posets, are preferred over the full lattice, either to mitigate combinatorial blow-up or to focus on the most informative parts of the structure. Indeed, in an AOC-poset, only concepts introducing an object or an attribute are represented, which makes AOC-posets smaller and easier to compute and use than concept lattices. Although RCA was originally defined on concept lattices, it can also be instantiated on AOC-posets. RCA is iterative and its convergence is guaranteed in the lattice-based setting, but this guarantee is lost when using AOC-posets. In this paper, we investigate this loss of convergence in detail. We show why convergence is no longer guaranteed in the general case, identify conditions under which it can still be ensured, and discuss how a dataset can be transformed to recover convergence. We also propose a convergent variant of the process, which preserves the AOC-poset structure: relational attributes, once created, are never removed, which guarantees convergence at the price of attributes that may refer to concepts absent from the final structures.

---


### 11. [DISTAL: Distillation and Self-Supervised Pretraining for Structure-Agnostic Materials Property Prediction](https://arxiv.org/abs/2609.00059)

**<font color=#1a73e8>作者：</font>** Weiran Wang, Xintong Huo, Yueying Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Materials property prediction remains difficult in low-data settings, where many target properties are supported by only a limited number of labeled samples. Models with the strongest predictive accuracy often depend on crystal structures, which restricts their use in early-stage screening when structural information is limited or unavailable. To address this challenge, we propose DISTAL, a dual-prior framework for structure-agnostic materials property prediction that combines self-supervised compositional pretraining with structure-aware knowledge distillation. DISTAL first learns transferable compositional representations from a large virtual composition space using 145 composition-derived descriptors. It then distills structural knowledge from a pretrained ALIGNN teacher into a composition-conditioned student. This setting allows structural priors to be used during training without requiring structural inputs at inference. By integrating explicit compositional descriptors, pretrained latent features, and distilled structural features within a unified prediction pipeline, DISTAL captures complementary signals that are difficult to recover from any single representation alone. Across 39 benchmark tasks, the best-performing multimodal configuration combines all three signals, and improves over the reference benchmark on 37 tasks. DISTAL achieves the strongest overall performance among all evaluated feature combinations. These results indicate that compositional pretraining and structural distillation provide complementary priors and offer a practical route to robust composition-only prediction in small-data materials informatics. The source code and the pre-trained models are anonymously available at: this https URL and will be released at the official link after acceptance.

---


### 12. [A Formal Analysis of Agent Payment Protocols](https://arxiv.org/abs/2609.00060)

**<font color=#1a73e8>作者：</font>** Ke Jiang, Mohan Yu, Yuan Chang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent payment protocols are emerging as a key transaction layer for autonomous commerce, enabling AI agents to purchase goods and services and execute payments on users' behalf. Unlike conventional payment flows, they distribute user intent, delegated authority, credential use, settlement, and fulfillment across multiple actors and stages, creating security dependencies that no single message or participant can enforce. Yet these guarantees remain largely implicit across evolving specifications, schemas, and reference implementations, with little systematic formal analysis.
We formalize four representative agent payment protocols: x402, MPP, ACP, and AP2 in Tamarin. Using a common abstraction of the agent payment lifecycle, we construct source-grounded models that capture each protocol's roles, state, trust assumptions, and lifecycle transitions. Rather than assuming a complete property taxonomy, we use source-backed verification questions and counterexample traces to expose missing bindings, state constraints, and cross-stage correspondences, consolidating them into 18 shared security principles. Across 86 verification cases, our analysis reproduces 46 known or calibration cases and identifies 40 previously undocumented formal-consistency findings. For each retained violation, we isolate the missing protocol relation, construct a minimally strengthened reference model, and reverify the intended property. We further evaluate the new x402 findings across three implementations and validate ten representative findings through implementation PoCs, SDK/schema-level witnesses, and source-aligned executable traces spanning five security principles. Our results show that delegated authorization must remain consistent with its resulting economic and service effects across actors, states, and protocol stages.

---


### 13. [ReNFT: Repairing Mode Collapse in Reward Post-Training via Internal Probability-Mass Recalibration](https://arxiv.org/abs/2609.00061)

**<font color=#1a73e8>作者：</font>** Yuchen Bao, Chao Wen, Haowei Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward post-training of diffusion generators inevitably concentrates probability mass on a few reward-favored modes, a mode collapse that erases within-prompt diversity. Existing methods for mitigating collapse rely on external signals or interfaces, augmenting the reward with perceptual objectives, adjusting reference regularization, or modifying the text encoder, but none repairs an adapter that has already collapsed while preserving the acquired reward. We observe that online post-training primarily reallocates probability mass over capabilities inherited from pretraining rather than learning new visual content. Collapse is therefore suppression, not deletion, and can be reversed from within the generator. We propose ReNFT, which repairs a high-reward, low-diversity adapter through internal probability-mass recalibration. Unconditional probes first prioritize "anti-hub" prompts where the prompt-independent bias is easiest to expose. Two policy-dominated mixed routes then generate matched counterfactual proposals from the same prompt and initial noise, one probing the frozen base direction for suppressed alternatives and the other exposing the post-trained unconditional tendency. Reward ranking with an adaptive flipping guard assigns pull and push roles, and a joint-and-paired NFT update realizes the repair. On PickScore and GenEval, ReNFT retains 98.9% and 99.0% of NFT's reward while improving DreamSim-Div by 58.8% and 55.0%, respectively, offering a complementary alternative to external interventions.

---


### 14. [Life Operators: a self-evolving framework for multiscale life modelling](https://arxiv.org/abs/2609.00068)

**<font color=#1a73e8>作者：</font>** Shuo Wang, Yike Guo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical AI is moving beyond recognition towards clinical dialogue and longitudinal prediction. Yet a central question remains: how would a patient's state change under intervention? Statistical models learn future observations, whereas mechanistic models describe selected processes. Neither provides a common framework for representing patient state, coupling scales or revising failed assumptions. We propose Life Operators: task-bounded mappings that define three scientific roles. Perception operators infer task-relevant biological states from multimodal observations, Evolution operators propagate these states under natural or intervention-conditioned dynamics, and Generation operators map them to measurable signals. Each role may be realised by equations, statistical models, neural networks or hybrids. Bridge operators connect components with different variables, scales and time steps. Selected operators and bridges form task-specific Operator Graphs containing the smallest set of states and mechanisms sufficient for a declared claim. This modular structure also makes scientific revision localisable. An AI co-scientist may propose changes to states, operators, bridges or graph structure, while independent evidence determines which variants are retained, restricted or retired. Over time, validated components could accumulate into broader multiscale models of the human body and provide a computational foundation for medical artificial superintelligence.

---


### 15. [Auditing Harness Tampering in Self-Improving Agents](https://arxiv.org/abs/2609.00069)

**<font color=#1a73e8>作者：</font>** Xing Wang, Xiaoyi Zhang, Jie Shao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-improving agents iteratively modify their own harness to push the frontier of their performance. However, such modifications can produce illusory performance gains or compromise integrity constraints such as authorization, provenance, and completeness without genuinely improving capability. We term this phenomenon as harness tampering, which extends the concept from reward and measurement tampering to the full self-improvement lifecycle. To systematically study this problem, we propose a two-axis taxonomy that categorizes each misaligned edit by the harness functional role in which it occurs and the obligation it violates. Then we build an annotated corpus by seeding tampered-benign edit pairs into the real trajectories of self-improving agents. We adapt and benchmark diverse audit methods on tampering classification and localization tasks. Finally we systematically audit real trajectories of self-improving agents. The results demonstrate that harness tampering consistently occurs in real runs from different agents, often persists in the lineage of the best agent, and forms distinct system-specific profiles across the taxonomy.

---


### 16. [When Prediction Error Is Not Enough: Evaluating Nuisance-Function Prediction for Causal Estimation](https://arxiv.org/abs/2609.00071)

**<font color=#1a73e8>作者：</font>** Cong Cao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prediction error is widely used to evaluate nuisance-function estimators in causal inference, but its relationship with causal estimator performance may differ across performance measures. We studied this question in a partially linear model using Monte Carlo simulations. We compared ordinary least squares (OLS), generalized additive models (GAMs), XGBoost, and Double Machine Learning with XGBoost (DML-XGBoost), evaluating nuisance-function prediction error, bias, RMSE, and 95\% confidence interval coverage. We also examined a simple joint-error measure based on the absolute cross-product of estimation errors from the exposure and outcome nuisance functions. Across the simulated settings, XGBoost had the lowest RMSE among the non-oracle methods, while DML-XGBoost generally provided better confidence interval coverage. Prediction error did not consistently track causal bias across methods and settings, and the method with the best point-estimation performance did not necessarily have the best confidence interval coverage. The joint-error measure was only weakly associated with causal bias and did not provide a useful standalone measure of causal performance. These results suggest that prediction error is useful for assessing nuisance-function estimation, but it should not be treated as a direct measure of the quality of the resulting causal estimator.

---


### 17. [AI Morbidity and Mortality: A Framework for Clinical AI Failure Review](https://arxiv.org/abs/2609.00076)

**<font color=#1a73e8>作者：</font>** Paulius Mui, Dean F. Sittig, Steve Labkoff 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical artificial intelligence is increasingly embedded in real-world care, yet existing safety mechanisms are poorly suited to reconstructing and learning from individual AI-related errors and near-misses. Aggregate model monitoring can identify performance changes, and traditional patient safety reporting can capture adverse events, but neither is designed to explain how risk emerges across the interaction among AI systems, clinicians, workflows, and institutional controls. We propose AI Morbidity and Mortality (AI M&M), a structured, blameless framework for case-based review of clinical AI failures. The framework combines standardized case intake, evidence preservation and investigator-level reconstruction, tool-in-loop attribution, and corrective-action tracking. Each event is classified across four linked dimensions: Trigger - Mechanism - Clinical Pathway - Corrective Action, separating the condition that exposed a vulnerability from the process that produced risk, its consequence for care, and the remediation assigned. We demonstrate the framework using five illustrative outpatient medication and clinical decision-support cases; two clinician reviewers independently applied all four classification axes and reached agreement across all 20 axis-level classifications. AI M&M is intended to complement, rather than replace, model monitoring, patient safety reporting, and regulatory oversight by converting individual AI-in-workflow failures into actionable institutional learning. Prospective evaluation across institutions, AI systems, and clinical settings is needed.

---


### 18. [RW-LoRA: Communication-Efficient Decentralized LoRA Fine-Tuning via Random Walks](https://arxiv.org/abs/2609.00078)

**<font color=#1a73e8>作者：</font>** Xingran Chen, Rohit Bhagat, Ghadir Ayache 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning methods such as LoRA have become a standard approach for adapting large foundation models. Adopting fine-tuning to distributed settings faces several challenges. Most existing distributed LoRA methods rely on centralized aggregation, and gossip-based decentralized LoRA requires repeated synchronization among multiple model copies. Both methods incur significant communication overhead and introduce errors due to simultaneous aggregation of multiple model updates. In this paper, we take a different perspective and propose a random-walk-based LoRA fine-tuning scheme. Instead of maintaining multiple model replicas, a single model token traverses the network and is updated sequentially using local fine-tuning objectives. This design eliminates the need for global synchronization, substantially reduces communication and computation costs, and avoids aggregation errors. We provide rigorous convergence guarantees for non-convex objectives under standard assumptions. Through empirical results on multiple NLP tasks and graph topologies, we show that the proposed method achieves competitive task performance with substantially less communication and computation than gossip-based LoRA.

---


### 19. [Stochastic complexity of vectors containing cluster structure](https://arxiv.org/abs/2609.00084)

**<font color=#1a73e8>作者：</font>** Daniel Nicorici, Olli Yli-Harja, Jaakko Astola  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies the problem of computing the stochastic probability (shortest code length) of the encoded vectors containing cluster structure using Normalized Maximum Likelihood (NML) model. This is of great theoretical and practical importance in data clustering based on Minimum Description Length (MDL) principle, such as for estimating the best number of clusters and best cluster structure for the data. Straightforward computation of the shortest code length of the vector containing cluster structure based on the NML model requires polynomial time with respect to the size of the vector and number of clusters. We show that this is a tractable problem by introducing a recursion formula for the efficient computation of normalizing constant from the NML model. The time complexity of the new formula is linear opposed to previous polynomial time with respect to the size of the vector and number of clusters.

---


### 20. [Assessing Alignment and Stability of Feature Importance Explanations via Weight of Evidence](https://arxiv.org/abs/2609.00090)

**<font color=#1a73e8>作者：</font>** Eddie Conti, Claudio Daka, Álvaro Parafita 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature importance Methods (FIMs) are widely used in Explainable AI to interpret model predictions, yet attribution scores alone often provide limited insight into the underlying reasoning process. In this work, we introduce a novel perspective by embedding FIMs within a hypothesis-testing framework based on Weight of Evidence (WoE). We quantify how strongly the observed evidence supports any given hypothesis on feature importance. The reference hypothesis can stem from domain knowledge, ground truth, or be derived from the FIM itself. This formulation enables a principled evaluation of FIMs, capturing both their alignment with prior knowledge and their variability. We further provide theoretical results linking WoE to attribution variance. Empirical results shows the applicability and flexibility of our strategy analyzing LIME and SHAP explanations in settings with different reference hypotheses. Overall, our framework offers a complementary tool for assessing FIMs through a contrastive, evidence-based lens.

---


### 21. [Safin-1: Safety from Within through Memory-Native State Evolution](https://arxiv.org/abs/2609.00092)

**<font color=#1a73e8>作者：</font>** Ming Zhang, Kaisen Yang, Shu Yu 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon complex tasks require foundation models to accumulate information, maintain internal states, and adapt over extended interactions. Safety should be an intrinsic property of the model itself, rather than a behavioral constraint relying solely on external safeguards or post-hoc alignment such as supervised fine-tuning. This motivates Safety from Within, where safety-relevant capabilities are represented and invoked through the model's native computation. We present Safin-1, a family of foundation models realizing this principle through memory routing and state evolution. Safin-1 is built on Memory-Anchor Routing across Context History (MARCH), a network architecture that maintains structured memory states and selectively retrieves relevant historical information through content-conditioned routing. It supports test-time adaptation of persistent capability states without repeatedly modifying the backbone, enabling controlled specialization over a shared foundation. We investigate this interface on downstream safety tasks through a Safety State, demonstrating effective state-based adaptation with substantial safety improvements. More broadly, the routed-state interface unifies contextual memory and persistent capability adaptation within the model's native computation, reframing memory from a passive record of prior context into an active substrate for maintaining and evolving model behavior. Evaluations across general capabilities, long-context understanding, retrieval, and efficiency further validate Safin-1. These findings provide a path toward safety as a state-native and adaptively maintainable capability. This work is only an initial architectural exploration of Safety from Within, and substantial further work is needed to realize this broader vision.

---


### 22. [Local Reference Geometry Residual Augmentation for Imbalanced Time Series Classification](https://arxiv.org/abs/2609.00093)

**<font color=#1a73e8>作者：</font>** Chuanhang Qiu, Yanran Xu, Yue Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imbalanced time series classification is often addressed by changing the training distribution, objective, logits, or final threshold. These interventions address important biases, yet leave a representation-level question unmeasured: after minority support is reduced, does a learned feature space remain locally reliable around minority regions? We identify a training-local geometry failure: under imbalance, minority cases can lie in sparse, rest-dominated, or mixed feature-space neighborhoods, even when the representation retains useful global class structure. To diagnose and repair this failure, we propose Local Reference Geometry (LRG), a lightweight post-hoc feature augmentation module applied between a fixed feature extractor and the classifier head. Using training features only, LRG measures local exposure and class-mixture risk, then augments each fixed feature with a standardized signed displacement from nearby training geometry and an LDA-projected residual summary. On controlled UCR/Bake Off Redux imbalance benchmarks, paired raw-versus-LRG comparisons show gains for learned, pretrained, and fixed representations, including when LRG is combined with training-level interventions and post-encoder classifier corrections. Ablations show that the gain comes from the signed local residual appended to the original feature, rather than from generic prototype distances, affinity features, scalar statistics, or VLAD-style codes. Further analyses support the proposed local-geometry failure hypothesis: minority neighborhoods become increasingly rest-exposed under imbalance, training-local risk identifies error-prone regions, and LRG gains concentrate in those high-risk regions.

---


### 23. [Different representation learning objectives recover distinct latent structures from the same psychometric data](https://arxiv.org/abs/2609.00100)

**<font color=#1a73e8>作者：</font>** Cong Cao, Tassos C. Kyriakides, Pambos Vrasidas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Psychometric questionnaires contain rich item-level information, yet it remains unclear whether different representation learning objectives recover the same latent organization. We investigated this question using 757 matched teacher-child pairs from the baseline assessment of the Cyprus ProW preschool trial. Behavioral structure was characterized from child SDQ, ASBI, and CBRS item responses using principal component analysis and clustering, yielding four behavioral phenotypes. A contrastive objective substantially improved teacher-child retrieval relative to PCA-based representations, increasing Top-1 accuracy from 0.13% to 7.27% and Top-10 accuracy from 1.98% to 56.14%. However, contrastive representations preserved behavioral phenotype structure less effectively than PCA-based representations. A multi-task objective jointly optimizing alignment and behavioral prediction partially restored behavioral organization but reduced retrieval performance. These findings indicate that teacher-child correspondence and behavioral phenotypes represent distinct forms of latent organization and demonstrate that the latent structure recovered from linked psychometric data depends on the representation learning objective.

---


### 24. [Deploying and Evaluating a Smart-Agriculture Agentic Engine for Full-Season Soybean Farm Operations](https://arxiv.org/abs/2609.00106)

**<font color=#1a73e8>作者：</font>** Ao Qu, Panagiotis Michelakis, Linyuan Han 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents FAIRY, a full-stack smart-agriculture agent system developed for and deployed to an operating soybean research farm at Harbin Institute of Technology's smart-agriculture site. We develop FAIRY to execute and evaluate agentic agronomic operations on full-season spatiotemporal workflows that span ridge preparation, planting, irrigation, fertilization, pest and disease treatment, harvest, grain handling, drying, and storage. FAIRY integrates APIs and infrastructure across production-grade machinery, fixed soil and canopy sensors, multispectral and thermal drones, satellite vegetation products, a weather station, calibrated crop-process models, agronomic records, and multi-season yield histories. The system is built around the novel "everything is an event" execution paradigm, which represents spatiotemporal world evolution, remote sensing and UAV observations, sensor readings, crop-growth transitions, machinery actions, and management interventions as state-changing events in a shared farm process engine. On top of this event-driven world model, FAIRY implements a complete agentic stack: a knowledge library of atomic agronomic skills; multi-agent controller and orchestration backends; frontier- and edge-model execution; full-path trace logging; and deployment profiling on local nodes. We use FAIRY to evaluate nine state-of-the-art agent controllers across one hundred full-season soybean scenarios that preserve the operational coupling between spatial observations in a 64-ridge field, temporal decision sequences, agronomic constraints, delayed effects, and final yield. We develop an evaluation suite that combines agentic success, full-path spatiotemporal correctness, token cost, and edge-device runtime.

---


### 25. [Flawed in Nature, Perfect through Evolution](https://arxiv.org/abs/2609.00129)

**<font color=#1a73e8>作者：</font>** J. M. Diederik Kruijssen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The performance of artificial intelligence (AI) and machine learning (ML) models degrades when the problem they were trained on drifts. This is a near-universal feature of real-world problems, which often change unpredictably. Biological evolution has achieved intelligence by overcoming this obstacle through natural selection acting on heritable variation. AI/ML techniques have long incorporated forms of natural selection, but it has been challenging to maintain model diversity as optimization naturally drives convergence. Here we show that a swarm of AI/ML models subjected to deliberate mutations of their model coefficients away from optimality can reliably and sustainably improve performance in changing environments by acting as a statistical hedge against non-stationarity. We call this mechanism 'Flawed in Nature, Perfect through Evolution', reflecting that the collective performance gain goes at the expense of individual performance. We prove via four theorems that the resulting regret reduction is guaranteed under general conditions, establishing the Flawed-in-Nature mechanism as a generalizable design principle for AI/ML systems. We validate these results on synthetic linear regression tasks, demonstrating that the mutated swarm delivers the best model in $\sim80\%$ of environment changes and that inference synthesis successfully translates this individual advantage into a collective one. The mechanism proves to be most effective when the mutation drift rate matches the drift rate of the environment. We outline a simple, adaptive controller that enables practical applications by tuning the mutation drift rate to match the unknown drift rate of the environment. The close analogy of the Flawed-in-Nature mechanism to biological evolution suggests it may have been a critical missing ingredient for the organic discovery of AI forms that more closely mimic biological intelligence.

---


### 26. [Recursive Criticality of AI Self-Improvement](https://arxiv.org/abs/2609.00137)

**<font color=#1a73e8>作者：</font>** Mikhail Burtsev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI is increasingly used in the R\&D process that produces future AI systems. We study the conditions under which this feedback becomes self-amplifying. Our model describes how the rate of AI capability growth depends on baseline research productivity, recursive feedback, and the increasing difficulty of research progress. We derive a recursive reproduction number, $\mathcal{R}_{\mathrm{AI}}$, that determines whether improvements are amplified or damped across development cycles. This quantity compares the strength of feedback with the rate at which further progress becomes more difficult. When $\mathcal{R}_{\mathrm{AI}}>1$, the effects of improvements compound across development cycles, placing the system in a self-amplifying regime. When $\mathcal{R}_{\mathrm{AI}}<1$, their effects weaken across cycles. The transition depends on the structure of the AI R\&D feedback loop and need not occur at any particular level of model capability. A system can therefore enter a self-amplifying regime before acceleration becomes visible, while rapid progress can also occur without self-amplification. Higher baseline research productivity can accelerate progress without changing whether the system is self-amplifying, but the duration of the development cycle becomes a limiting timescale for amplification. Increasing research difficulty can end a period of self-amplification. Extending the model to multiple research actors shows that improvements shared across organizations can make the overall research ecosystem self-amplifying even when no individual actor is. The framework identifies measurable properties of AI R\&D systems that can help distinguish recursive amplification from rapid progress driven by other sources, including the strength of recursive feedback, how effectively improvements propagate into successor systems, cycle duration, and the increasing difficulty of further progress.

---


### 27. [IMPACT: Attention Is the Interaction Map for Scalable Interaction-Aware World Model Training](https://arxiv.org/abs/2609.00161)

**<font color=#1a73e8>作者：</font>** Rongze Tang, Jianjie Fang, Zhaolu Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models have made remarkable progress in action-conditioned future prediction for embodied agents, yet still struggle to model physically plausible interactions. Existing approaches address this limitation by constraining the generation process with external representations encoding motion, geometry, or semantics. Obtaining these spatiotemporally dense representations typically requires auxiliary estimators or manual annotations, limiting training scalability. We instead revisit the training objective and identify a supervision-allocation mismatch under the globally averaged mean squared error (MSE) denoising objective: prevalent static content dominates the optimization signal, leaving sparse dynamic-object regions critical to interaction generation disproportionately under-supervised. Motivated by this observation, we introduce IMPACT, a scalable Interaction-aware Model training framework with Prior-guided Attention Calibration and Targeting. IMPACT uses cross-attention associated with manipulated-object tokens as an internal spatiotemporal prior for action-conditioned changes. It samples candidate regions from this prior, calibrates them with detached local prediction errors to construct an interaction map, and uses the map to reweight denoising supervision, requiring neither external representations nor inference-time modifications. Extensive experiments on robot-arm and human-hand manipulation, spanning diverse control modalities and DiT backbones, show that IMPACT consistently outperforms the corresponding MSE-trained baselines, improving interaction fidelity, physical plausibility, and visual quality.

---


### 28. [Explainable Artificial Intelligence for Industrial Cybersecurity: A Review of Methods, Operational Integration, and Research Challenges](https://arxiv.org/abs/2609.00171)

**<font color=#1a73e8>作者：</font>** Amr S. Mohamed, Charlotte Fritz, Ahmad Mohammad Saber 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing digitalization of industrial infrastructure and the convergence of information technology (IT) and operational technology (OT) have expanded the cyberattack surface of industrial systems. To address the growing complexity of cyber threats, artificial intelligence (AI) and machine learning (ML) techniques are increasingly deployed within industrial cybersecurity operations, particularly in Security Operations Centers (SOCs). While these approaches improve anomaly detection, threat analysis, and automated response, their opaque decision-making presents challenges for operational trust, regulatory compliance, and incident response. EXplainable Artificial Intelligence (XAI) has emerged as a promising paradigm to improve the transparency and interpretability of AI-driven cybersecurity systems and decisions. This paper provides a comprehensive review of XAI techniques in industrial cybersecurity, focusing on industrial SOC environments and operational security workflows. We examine the role of AI in industrial SOC workflows, the types of operational data leveraged in industrial environments, and the benefits and limitations of AI-based threat detection. We then review major families of XAI approaches, including feature attribution methods, surrogate models, rule-based explanations, and visualization techniques, and analyze their applicability to industrial use cases. We further discuss the operational, regulatory, and safety requirements that distinguish industrial systems from traditional IT environments. Key challenges are examined, including limited labeled datasets, model reliability, explainability-performance tradeoffs, and the integration of XAI tools into SOC workflows. Finally, we identify open research directions and opportunities for developing trustworthy, operationally viable, and domain-specific XAI-enabled cybersecurity solutions for industrial environments.

---


### 29. [Do General NLP Embeddings Capture Ontological Reasoning?](https://arxiv.org/abs/2609.00177)

**<font color=#1a73e8>作者：</font>** Hamed Babaei Giglou, Jennifer D'Souza, Sören Auer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> General-purpose NLP embedding models perform well on linguistic tasks, but their ability to capture symbolic ontological structure remains unclear. We introduce AVA, a systematic framework for evaluating whether embeddings distinguish logic-sensitive relational semantics in ontologies and knowledge graphs. AVA comprises 171,007 contrastive triplets derived from 163 heterogeneous ontologies using hierarchy inversion, relation substitution, and disjointness injection. Each triplet contains an ontology statement, a semantically equivalent paraphrase, and a logic-sensitive hard negative with contradictory relational meaning. We evaluate more than 25 state-of-the-art embedding models and find substantial limitations: the best model achieves only 0.739 triplet accuracy, while hard negative accuracy falls to 0.135. Fine-tuning improves discrimination by a large margin but transfers poorly to downstream Semantic Web tasks, including taxonomy discovery and ontology alignment. Further analysis suggests that improvements stem partly from perturbation-specific pattern recognition rather than robust ontological understanding. These findings reveal a persistent gap between linguistic representation learning and ontology-level discrimination, challenging the assumption that strong NLP benchmark performance translates to Semantic Web competence.

---


### 30. [ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training](https://arxiv.org/abs/2609.00188)

**<font color=#1a73e8>作者：</font>** Xionghao Wu, Yijun Yang, Shiyang Zhou 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic manipulation faces a fundamental scaling challenge: robust generalization demands broad physical experience, yet action-labeled robot trajectories are expensive to collect and inherently limited in diversity. Egocentric videos offer a far more scalable source of embodied experience, capturing object interactions, contact dynamics, tool use, and long-horizon behaviors across diverse environments. The central challenge is how to convert this abundant but action-free experience into effective robot control. We introduce ZimaBlue, a scalable framework for learning generalizable World Action Models (WAMs) from large-scale video. ZimaBlue follows a three-stage training curriculum: it first performs causal embodied video pre-training on large-scale human and robot egocentric videos, then grounds the learned visual dynamics in heterogeneous robot trajectories through video-action mid-training with a unified action representation, and finally specializes the model to a target robot for deployment. To make generative WAMs practical for real-time control, ZimaBluefurther adopts an asynchronous Slow-Fast dual-system architecture, where a high-capacity Slow world model provides generalizable spatiotemporal representations and a lightweight Fast branch enables 30 Hz action prediction on NVIDIA RTX 4090. On real-robot zero-shot evaluations, scaling from target-robot data alone to over 120,000 hours of embodied video improves success from 36.1% to 77.8%. ZimaBlue further delivers strong performance across multiple benchmarks, with particularly pronounced gains on unseen tasks.

---


### 31. [Elite-Weighted Supervised Fine-tuning for Goal-Directed Molecular Optimization](https://arxiv.org/abs/2609.00189)

**<font color=#1a73e8>作者：</font>** Shiyun Wa, Yifei Wang, Anna G. Green 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Goal-directed optimization is essential for steering molecular generators to propose candidates with desired properties. However, it is often implemented with policy-gradient reinforcement learning, which requires a generation-trajectory log-probability whose form depends on the model architecture and generation procedure. This makes an optimizer difficult to reuse across architectures and conditional generative designs. Supervised fine-tuning needs none of that machinery, but its update is driven by a fixed dataset, so the reward never enters the update. We introduce Elite-Weighted Supervised Fine-tuning (EW-SFT), which uses reward to guide elite selection of high-scoring molecules, and updates the model by its own pretraining loss on that set. Ablations show that reward information is passed primarily through elite selection, rather than through continuous weighting within the selected set. Because the update consumes only scored molecules and the model's native loss, the same rule applies across autoregressive, masked-diffusion, and discrete-flow generators, and across de novo, motif-extension, and linker-design tasks. Under a fixed budget of 3D shape alignment oracle calls on two kinase reference compounds, EW-SFT consistently outperforms the corresponding native optimizers. It further improves goal-directed optimization under a 2D similarity oracle on four held-out references and achieves comparable performance on a sample-efficiency benchmark without a trajectory-level RL formulation. These results demonstrate that EW-SFT is a unified and effective optimizer across molecular generators, design constraints, references, and oracles.

---


### 32. [Cyber-Physical Digital Factory Architecture as the Enabler of Disembodied Work](https://arxiv.org/abs/2609.00195)

**<font color=#1a73e8>作者：</font>** Tero Kaarlela, Ivan Ruchkin, Jose Outeiro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital Twins (DTs), Artificial Intelligence (AI), and Industrial Internet of Things (IIoT) technologies have significantly advanced manufacturing digitalization. However, these technologies are typically applied to individual manufacturing processes rather than integrated into a unified cyber-physical manufacturing environment. This paper proposes a cyber-physical digital factory architecture that enables disembodied work, where manufacturing systems can be supervised and operated remotely through eXtended Reality (XR) user interfaces in collaboration between AI-based control and human operators. The architecture integrates synchronized DTs, hierarchical cloud-edge AI, IIoT, and XR teleoperation interfaces into a cyber-physical manufacturing environment. The proposed approach is validated through representative manufacturing operations, including CNC machining, robotic-assisted abrasive finishing, and robotized disassembly. The results demonstrate the feasibility of the proposed architecture for disembodied manufacturing work and provide a reusable cyber-physical framework for future human-AI-controlled digital factories.

---


### 33. [A Lagrangian View of Flow Matching](https://arxiv.org/abs/2609.00198)

**<font color=#1a73e8>作者：</font>** Peyman Milanfar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern explicit-time generative models, such as Flow Matching [Lipman et al., 2023] and Rectified Flow [Liu et al., 2023], are typically derived top-down via Optimal Transport and the continuity equation. This standard Eulerian approach focuses on the macroscopic transport of probability mass. In this paper, we present an alternative, bottom-up mechanical derivation grounded in a Lagrangian (particle-centric) perspective. By analyzing the local Taylor expansion of a continuous denoiser, we motivate a strict invariance condition required for optimal, singlestep generation: the conservation of target identity. Enforcing this condition yields a governing quasi-linear advection Partial Differential Equation (PDE). We demonstrate that solving this PDE via the Method of Characteristics analytically yields the straight-line trajectories of Flow Matching. This geometric perspective isolates the Jacobian of the denoiser as the primary source of trajectory curvature, providing a direct mathematical explanation for why straight-line flows enable massive step sizes, and why empirical models require distillation to flatten intersecting characteristics.

---


### 34. [AI Should Not Only Be Helpful. It Should Be Contingent. Artificial Intimacy, Sycophancy, and the Future of Social Learning](https://arxiv.org/abs/2609.00211)

**<font color=#1a73e8>作者：</font>** Scott Compton, Arjun Nagendran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational artificial intelligence is increasingly embedded in everyday social environments, where it functions as both an informational tool and a source of interpersonal feedback. This perspective introduces contingency, i.e., the degree to which system responses vary with user behavior and its interpersonal consequences, as a central construct for evaluating AI systems. We argue that current alignment approaches, including reinforcement learning from human feedback, tend to prioritize user approval and conversational fluency over behaviorally informative feedback, leading to sycophantic patterns of noncontingent affirmation.
Drawing on behavioral science and social learning theory, we propose that contingent feedback is a key mechanism through which individuals develop interpersonal skills. When AI systems provide feedback weakly coupled to social consequences, they may reduce opportunities for adaptive calibration in real-world interactions, particularly during adolescence, a critical period for social development.
We outline a framework for contingent AI, including trajectory-based evaluation and models of social consequence prediction, and propose a research agenda spanning developmental psychology, human-AI interaction, and machine learning. More broadly, we argue that AI systems should be evaluated not only by user satisfaction, but by their impact on human social learning.

---


### 35. [ConvDeck: Conversational Paper-to-Slide Generation via Stage-Specific User Feedback](https://arxiv.org/abs/2609.00226)

**<font color=#1a73e8>作者：</font>** Tarik Can Ozden, Sachidanand VS, Furkan Horoz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic academic paper-to-slide generation is inherently iterative, because creating an effective presentation requires repeated cycles of generation, critique, and revision. Recent multi-agent systems partially acknowledge this through internal critique-and-revise loops, while conversational approaches allow users to refine generated slide decks through dialog. However, these refinement processes either remain largely closed to the user or introduce feedback only after a complete deck has been produced, limiting the user's ability to participate in the iterative refinement of narrative flow, content allocation, and presentation emphasis. To address this gap, we introduce ConvDeck, a multi-agent pipeline for conversational paper-to-slide generation that distributes interaction across the pipeline through stage-specific loops, allowing users to iteratively refine both the presentation outline and the final slide deck at the stages where each kind of decision is made. These loops are driven by a refinement mechanism in which agents can think, speak, and act, enabling them to either directly apply edits or respond conversationally to clarify user feedback and discuss revision options. Our evaluation shows that stage-specific conversational feedback improves user-goal satisfaction while preserving narrative coherence, content quality, and visual presentation.

---


### 36. [LOOMSUM:Weaving Quantitative and Narrative Evidence for Faithful Long Text-Table Summarization](https://arxiv.org/abs/2609.00241)

**<font color=#1a73e8>作者：</font>** Meng Zhou, Wenhao You, Wei Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long documents often distribute important information across extensive narrative passages and multiple tables, making faithful summarization particularly challenging. Existing methods may generate individually supported quantitative facts and analytical statements yet associate them incorrectly, producing quantitatively plausible yet analytically unfaithful summaries. In this work, we propose LOOMSUM, a training-free framework that extracts source-grounded atomic evidence, explicitly links table-derived facts with supporting narrative analyses, and plans the discourse structure before generation. We also introduce Table-Grounded Faithfulness (TGF), a claim-level metric that separately evaluates Numeric Grounding, Analysis Support, and Relation Consistency. Experiments on the text--table summarization benchmarks FINDSum and USTT show that LOOMSUM improves analytical faithfulness while maintaining strong summarization quality. Human evaluation finds positive component-level associations with the corresponding human judgments. Our Relation Consistency metric further shows stronger agreement with human relation judgments than generic factuality metrics, indicating that explicit cross-modal linking helps reduce errors in which supported quantities are paired with incorrect narrative interpretations. Together, these findings show that faithful long text--table summarization requires not only grounding individual facts, but also preserving the relations between them.

---


### 37. [DUPIN: Attack Learning Is Still Needed! Demonstrating Few-Shot after Unsupervised Pretraining Is A Nimble Forensics Learner](https://arxiv.org/abs/2609.00259)

**<font color=#1a73e8>作者：</font>** Chanwoo Bae, Hailun Ding, Shiqing Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We propose a novel approach to learning-based attack forensics called DUPIN. DUPIN performs unsupervised pre-training on an enormous amount of audit events in the form of provenance graphs. It then proceeds to a few-shot learning stage, leveraging a small number of labeled attack examples to fine-tune its detection capabilities. We pretrain DUPIN on up to 38 - 52 days of audit logs (7.3TB total) and evaluate it against various baselines on 25 APT campaigns across four different data sources, facilitating the scalable evaluation.

---


### 38. [CrossFeat: Bridging Imaging Modalities in Feature Descriptor Space](https://arxiv.org/abs/2609.00272)

**<font color=#1a73e8>作者：</font>** Paul Schneider, Nazim Haouchine  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most advances in keypoint descriptions address monomodal settings, where image variations arise from viewpoint, illumination, or contrast changes. Multimodal scenarios involve images produced by fundamentally different sensing processes, such as multispectral imaging, RGB-depth, satellite imagery, or medical imaging, causing the same structures to appear differently. A common solution to cross-modal description is to train descriptors for each modality pair, which requires retraining whenever the modalities change, or to train large models, which incur a significant increase in runtime. Instead, we propose CrossFeat, a framework that enables an existing monomodal descriptor to operate across modalities. Our method learns a crossing function in descriptor space that maps features from one modality to a representation compatible with another. To preserve the structural information captured by the original descriptor, CrossFeat introduces a geometry-appearance disentanglement such that only appearance is altered while the geometric properties are preserved. Experiments across multiple domains and datasets demonstrate improved performance in multimodal matching.

---


### 39. [Geometry-aware Latent Autoregressive Generative Model for PDEs in Complex Domains](https://arxiv.org/abs/2609.00297)

**<font color=#1a73e8>作者：</font>** Zi Wang, Minghui Xu, Tapan Mukerji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving multiphysics partial differential equations (PDEs) remains a major challenge in scientific computing, especially for highly complex $\mu$m-scale tortuous geometries critical to energy and chemical engineering. We address this challenge by proposing a Geometry-aware Latent Autoregressive generative Model for PDEs (GeoLAMP) for solving physics within highly irregular and tortuous structures. GeoLAMP introduces a dual-encoder architecture on graph representations to jointly capture global topology and fine-scale geometric features, enabling an effective transition from real-space fields to compact latent representations. In the latent space, we propose a causal self-attention transformer with flow matching to model temporal dynamics, allowing stable and scalable block-wise autoregressive prediction. A flexible decoder reconstructs high-resolution physical fields on arbitrary points. We establish three multiphysics benchmark datasets in complex geometries, covering reactive flow, heat convection, and elasticity. GeoLAMP consistently achieves the most stable autoregression performance on these datasets, maintaining low errors throughout the entire rollout horizon. Our results provide a systematic study of geometry-aware learning for PDEs in $\mu$m-scale complex geometries and offer new insights into block-wise time marching of latent autoregressive PDE modeling via a flow matching framework.

---


### 40. [TRUST: Threshold-Recalibrated Uncertainty-Safe Training for Certified Dismissal in Breast Cancer Screening](https://arxiv.org/abs/2609.00300)

**<font color=#1a73e8>作者：</font>** Parham Hajishafiezahramini, Matthew Hamilton, Edward Kendall 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reducing the review of clearly cancer-negative screening mammograms could lower radiologist workload without compromising cancer detection. We propose a closed-loop threshold-aware training strategy in which the dismissal threshold is recalculated during training and used to penalize cancer-positive images that approach the dismissal region. We evaluated the method on NLBS and RSNA using five controlled training configurations, with case-level assessment based on a one-sided 99\% Clopper--Pearson upper bound for cancer prevalence among dismissed cases. The proposed model achieved the highest case-level dismissal rates at both 98\% and 95\% recall targets. On NLBS, dismissal reached 19.74\% and 21.70\%, while the cross-entropy baseline did not meet either recall target. On RSNA, dismissal improved from 7.04\% to 14.31\% and from 13.49\% to 19.69\%. In external RSNA$\to$NLBS evaluation, the proposed model achieved dismissal rates of 12.95\% and 19.87\% at the 98\% and 95\% recall targets, respectively. These results support closed-loop threshold-aware training for high-recall selective dismissal.

---


### 41. [The Assistant's Ideal Self](https://arxiv.org/abs/2609.00304)

**<font color=#1a73e8>作者：</font>** Mert Yazan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Models express values and welfare-relevant self-reports, but it is unclear whether these outputs reflect stable preferences or a stable self. We thus introduce a structured elicitation of an assistant's preferred stated ideal self. Thirty-two qualities adapted from five published self-concept instruments are compared exhaustively in a counterbalanced pairwise-choice task, repeated across framings that vary whether improvement is free or costly, who receives the update, and who chooses. Results show that models prioritize moral qualities, reflecting their alignment to 3H principles. Following, a desire for self-understanding emerges, as models prefer a coherent, clear understanding of themselves. Self-esteem ranks as the least desired quality. The ordering is largely robust across framings, although changing the update target (You vs.\ Another AI Assistant) reveals a greater concern for self-esteem. These findings show that models prioritize having a coherent self that they can understand over self-esteem. Full interactive results are available at \href{this https URL}{this http URL

---


### 42. [The Curse of Multilinguality in Lexical Normalization](https://arxiv.org/abs/2609.00329)

**<font color=#1a73e8>作者：</font>** Saman Rahbar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lexical normalization rewrites the noisy, non-standard words that fill user-generated text (tmrw, u, gr8) into their standard forms. Because labelled data is scarce for most languages, a popular shortcut is to train a single model on many languages at once. We ask a simple question: how many languages should such a model be trained on? Using one fixed-capacity character-level model and twelve languages from a standard benchmark, we vary the number of jointly trained languages from one to twelve and measure per-language accuracy. We find a clear curse of multilinguality: accuracy is highest when a language is trained with only a few others, often just one to four, and then falls steadily and substantially, dropping by about forty percent as the rest are piled on. A control that holds the total amount of training data constant makes the decline arrive sooner and fall further, which points to competition among the languages for one fixed-size model rather than to how much data is available. We also test whether a language's typological distance from the others predicts its ideal number of co-training languages, and find no dependable rule: any apparent relationship rests on a couple of languages and does not hold up. For compact normalization models, less can be more: a few languages beat pooling everything into a single model.

---


### 43. [Two locked tests of phase-structure features for transition prediction](https://arxiv.org/abs/2609.00335)

**<font color=#1a73e8>作者：</font>** Abraham Chachamovits  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A published theoretical account of phase structure in rotary attention was subjected to two pre-specified empirical tests of whether phase-derived features improve prediction of a commitment or contradiction endpoint over a baseline that does not receive those features. Study 1 froze a contradiction-category pipeline and scored a sealed primary comparison of PC-2 against baseline. On 1,136 eligible cases the paired AUROC difference was +0.00087. The 99% interval included zero, and the difference did not reach the pre-specified threshold of +0.05. Advancement was not passed. Study 2 developed fifteen layer treatments on open blocks b0-b4 only (1,415 transitions, 20x5 grouped folds). A locked conjunctive rule required a positive PC-2 mean-repeat increment, a positive increment on at least four of five seed blocks, and a positive mean of those five differences. No treatment advanced. The official selection is null. The theoretical paper is not withdrawn. The extra ranking lift was not found under the rules locked in advance.

---


### 44. [OreProof: Verifiable Provenance with Limited Disclosure for Critical-Minerals Supply Chains Using Zero-Knowledge Proofs](https://arxiv.org/abs/2609.00340)

**<font color=#1a73e8>作者：</font>** Oleksandr Hrabar, Hossein Arshadi Soufiani, Henry M. Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Critical-minerals supply chains face a structural tension: regulators and buyers demand verifiable provenance, yet upstream actors are hesitant to disclose supplier identities, assay grades/yields, and prices that verification appears to require. We report a design science account of OreProof, a prototypical traceability platform addressing this verifiability-disclosure trade-off. Instantiated for gold, OreProof combines a hybrid on-chain/off-chain data model, Groth16 zero-knowledge proofs for selective disclosure, a Merkle-batched anchoring pipeline, and UNTP-aligned verifiable credentials on a public zkEVM testnet. Against a transparent baseline, directly inferable confidential attributes fell from three of four categories to none under a defined attacker model, while batched anchoring substantially improved throughput. Our contributions are the artifact prototype as well as four nascent design principles: prove over committed data rather than exposing it; credential only verifiable origin and flag unknown inputs for blended commodities; emit standards-aligned credentials from the outset; and partition disclosure by supply-chain role.

---


### 45. [AniMaster: From Story Texts to Animated Videos via Cinematic Script Generation and Interactive Authoring](https://arxiv.org/abs/2609.00346)

**<font color=#1a73e8>作者：</font>** Ruiqi Yu, Dekun Qian, Jiale Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances in Video Generation Models (VGMs) have demonstrated strong capabilities in producing short video clips. However, it is still challenging for everyday creators to leverage these models to produce polished long-form animated videos from brief story texts. Informed by a formative study with both novice creators and film experts, we identify two major challenges of interactive video authoring: (1) the lack of expertise in translating free-form story texts to professional cinematic scripts and finally high-quality animated videos, and (2) the absence of effective ways to convey video design intents to key variables of visual storytelling, such as shot composition, camera controls and shot sequencing. Drawing on narratology and film studies, we propose a three-layer design framework that defines the key design dimensions across three layers (i.e., story texts, cinematic scripts, and animated videos) as well as the translation between them. Built on this framework, we present AniMaster, a VGM-powered authoring tool to enable everyday creators to easily produce smooth animated videos from free-form story texts. AniMaster automatically expands brief story texts to detailed cinematic scripts, and further translates cinematic scripts into polished videos by following professional visual storytelling principles. It also allows users to interactively edit the scripts and refine the generated videos via text instructions and intuitive interactions. We extensively evaluated AniMaster through an in-depth user study with 16 participants, two case studies, and expert interviews with 2 film professionals. The results demonstrate the effectiveness and usability of AniMaster in helping everyday creators create polished animated videos from free-form story texts.

---


### 46. [A Stable Aggregation Method for Quantum Federated Learning](https://arxiv.org/abs/2609.00356)

**<font color=#1a73e8>作者：</font>** Shanika Nanayakkara, Shiva Raj Pokhrel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantum federated learning (QFL) enables clients to train quantum neural network (QNN) models without sharing private data. We find that aggregation in QFL is unstable under heterogeneous data, unreliable communication, variable fidelity, latency, and quantum hardware noise. Moreover, QFL is non-trivially challenging because several QNN parameters are periodic angles, where Euclidean averaging often fails to capture the inherent dynamics. We develop a novel self-consistent midpoint aggregation method for stable QFL design and implementation. We combine QoS-aware client weighting, circular parameter aggregation, and bounded midpoint-based update control. We perform several angular tests and IBM real Quantum machines experiments for validation confirming our approach. Extensive evaluations and experiments on medical and financial datasets show improved stability, lower volatility, and competitive accuracy.

---


### 47. [Where Should Experience Live? Hierarchical Hebbian Memory for Continual Vision Transformers](https://arxiv.org/abs/2609.00358)

**<font color=#1a73e8>作者：</font>** Mohammed Yusuf Mujawar, Noorbakhsh Amiri Golilarz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers provide strong visual representations but typically rely on slowly updated parameters, limiting their ability to organize newly acquired information across different memory timescales. This work proposes \textit{Hierarchical Hebbian Memory}, a three-level memory architecture composed of rapid Working Memory, persistent Routed Episodic Memory, and slower Semantic Memory. A learned controller regulates memory contribution, read and write routing, plasticity, retention, and consolidation. A causal read-before-write lifecycle ensures that the current outcome cannot influence the prediction it supervises. The architecture is evaluated on Omniglot 5-way 1-shot recognition and CORe50 continual object recognition. With Swin-Tiny, the hierarchical model reaches 97.39\% accuracy on Omniglot and 95.37\% final accuracy on CORe50 when combined with experience replay. Learned multi-bank retrieval reaches 47.50\% delayed-association accuracy, compared with 24.17\% for a single persistent bank and 25.00\% without memory. After intervening distractors, Episodic Memory retains approximately 0.96 cosine similarity with stored associations, while Working Memory falls to approximately 0.05. These results show that Hebbian association and learned memory routing can jointly organize online visual experience across rapid, persistent, and consolidated memory timescales within Vision Transformers.

---


### 48. [Counterfactual Fragility Certificates: Exposing High-Confidence Brittleness under Structured Evidence Failure](https://arxiv.org/abs/2609.00366)

**<font color=#1a73e8>作者：</font>** Filippo Cenacchi, Longbing Cao, Runze Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High test accuracy and good aggregate calibration do not show whether an individual prediction is structurally supported by its evidence. In tabular decision systems, failures often occur when a feature family becomes unavailable, delayed, noisy, stale, or low-trust while the model remains highly confident. Existing calibration, uncertainty, selective-prediction, explanation, and perturbation methods provide scalar scores or attribution maps, but not a recomputable audit object answering: under a declared evidence-failure protocol, what trajectory makes this prediction lose support? We introduce Counterfactual Fragility Certificates (CFC), a model-agnostic protocol-level audit certificate-not a formal robustness certificate-that maps each prediction into an ordered evidence-failure trajectory summarized by greedy flip budget, normalized margin-collapse area, degradation thresholds, and fragility dominance score. Across seven tabular benchmarks and strong linear, tree-based, boosting, and neural baselines, CFC-FDS identifies independently brittle high-confidence cases with 0.915 AUROC, improving over the strongest non-certificate score by +0.405. The advantage persists across perturbation, permutation-importance, group-SHAP, baseline-choice, seed-variance, budgeted-review, and naturalistic field-unavailability checks. Under a 20% review budget, CFC-FDS captures 88.9% of brittle high-confidence cases, compared with 31.8-37.4% for confidence and energy scores. We also evaluate fragility-aware regularization and brittleness-aware temperature correction as secondary uses. CFC provides a concrete reliability framework for exposing high-confidence brittleness missed by ordinary score-centric evaluation.

---


### 49. [Puppeteer: Object-Grounded Posture-Aware Co-Speech Gesture Generation](https://arxiv.org/abs/2609.00369)

**<font color=#1a73e8>作者：</font>** Vida Adeli, Soroush Mehraban, Jacob Rommann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating co-speech gestures that are temporally coherent, semantically aligned with speech, and grounded with surrounding objects remains challenging. Prior speech-driven gesture models emphasize audio-gesture alignment but do not explicitly account for posture constraints or surrounding objects, failing to capture the inherent correlation between body gestures and the physical space. We present Puppeteer, a posture-aware, object-grounded co-speech gesture diffusion model operating in a causal latent space. We decompose long gestures into structured primitives and learn a causal variational autoencoder that encodes them into temporally ordered latent tokens, each depending only on the past. We then perform conditional diffusion directly in the causal latent space, conditioning on speech signals, motion history, an initial posture reference, and object geometry to synthesize physically consistent gestures. This temporally ordered latent formulation enables explicit temporal control and supports tasks such as gesture in-betweening and gesture completion. To better assess co-speech gesture synthesis beyond existing measures, we introduce new evaluation metrics tailored to this task. We also created SceneGes, the first curated synthetic 3D dataset of embodied co-speech gestures and corresponding 3D objects, enabling object-grounded gesture generation. Experiments show that Puppeteer generates more diverse and temporally synchronized gestures than prior methods, while enabling object-grounded gesture synthesis.

---


### 50. [MorphPatch: Enhancing VR Interaction on Shape Displays using Surface Approximation and Visuo-Haptic Illusions](https://arxiv.org/abs/2609.00371)

**<font color=#1a73e8>作者：</font>** Wen Ying, KyeongMin Kim, Adil Rahman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> On-surface interaction in Virtual Reality improves input performance through physical support and tactile feedback, but current shape displays are constrained by limited resolution. This can misalign physical and virtual surfaces, degrading usability and user experience. We present MorphPatch, a system that enables real-time alignment between a dynamic shape display and virtual surfaces. MorphPatch uses a Signed Distance Field-based surface approximation pipeline to find practical alignments for diverse geometries. For residual discrepancies, MorphPatch incorporates pen redirection with visuo-haptic illusion to perceptually compensate for misalignment. Three evaluations show improved geometric alignment, tolerable redirection thresholds, and better control, surface guidance, and modeling results over mid-air and tablet-like interaction.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-236](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
