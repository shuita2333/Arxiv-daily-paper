# 🧠 大模型相关研究 | 2026年09月28日

> 本类共 **228** 篇论文：已确认 **208** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-228](./part-05.md)

---

### 51. [From Static Personal Values to Contextualized Personalization: Bayesian Personalized Value Alignment for LLMs](https://arxiv.org/abs/2609.28942)

**<font color=#1a73e8>作者：</font>** Hanze Guo, Aixuan Song, Jing Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized value alignment has become increasingly important as large language models (LLMs) are expected to accommodate diverse user preferences. However, existing methods typically align model outputs with a static value profile across prompts, overlooking that the salience of value dimensions varies substantially across contexts. Inspired by Lewin's Field Theory, which views human behavior as jointly shaped by personal dispositions and situational constraints, we model personal values as priors and context-dependent preferences as posteriors. We propose BaCVA, an inference-time Bayesian Context-aware personalized Value Alignment method that approximates posterior personalized preferences by integrating static personal values with scenario-specific value salience. BaCVA first estimates contextual value salience from generally normative responses, and then employs a dual-view personalization module to infer posterior preferences from complementary personal-value and scenario-driven perspectives. This Bayesian formulation enables more accurate and adaptive personalized value alignment while improving data efficiency via prior values. Extensive experiments on benchmarks demonstrate its superiority over strong baselines.

---


### 52. [Exploiting Target Knowledge from MLLMs for Robust Few-Shot Segmentation](https://arxiv.org/abs/2609.28949)

**<font color=#1a73e8>作者：</font>** Yijun Hu, Heng Fan, Libo Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot segmentation (FSS) aims to segment unseen object categories with a few (e.g., one or five) labeled examples, enabling efficient adaptation to novel classes. Conventional models typically rely on appearance-based visual matching between support and query images for segmentation. While straightforward, these methods often struggle to handle significant appearance discrepancies and occlusions in the query image due to insufficient target knowledge. To mitigate this, we introduce a novel framework that mines target knowledge using the strong reasoning capacity of Multimodal Large Language Models (MLLMs) and employs it to enhance FSS. Specifically, building on SAM 2, our method, named MK-FSS, exploits two forms of complementary knowledge derived from a query image by an MLLM for FSS, including spatial knowledge, which provides a spatial prior indicating the potential target location, and semantic knowledge, which describes the target using text. The spatial knowledge is first encoded into a memory representation, and then resulting memory is integrated with the support-guided memory feature from query image through a carefully designed dual-memory debate-fusion (DMDF) module, yielding a more robust target memory feature. In parallel, the semantic knowledge is encoded into the textual feature, which is fused with multi-scale query features via a progressive cross-modal prompt generator (PCPG), producing a target-aware multimodal prompt for segmentation. Working together, the dual-memory feature and the multimodal prompt provide a comprehensive representation of the target, enabling more robust segmentation. In our extensive experiments, MK-FSS shows promising results and largely surpasses existing methods. Code will be released.

---


### 53. [MoVISA: Multi-Token Reasoning for Video Object Segmentation](https://arxiv.org/abs/2609.28956)

**<font color=#1a73e8>作者：</font>** Ruining Zhao, Ho Kei Cheng, Alexander G Schwing  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video object segmentation with Multimodal Large Language Model (MLLM) reasoning have demonstrated the effectiveness of using a single textual token, such as SEG, to predict segmentation masks across images and videos. However, we observe that this single-token strategy lacks the granularity required to precisely localize multiple objects across time in video segmentation tasks. To address this limitation, we develop Multi-Token Reasoning for Video Object Segmentation, or MoVISA. MoVISA uses multiple segmentation tokens, such as SEG0 and SEG1, to represent an object across different frames. This design enables more fine-grained alignment between language prompts and spatio-temporal mask predictions, improving both performance and interpretability. On the challenging MeViS, DAVIS17, ReVOS, and Ref-Youtube-VOS benchmarks, our model achieves a 13.2 percent J and F improvement on MeViS and an 8.4 percent J and F improvement on ReVOS. Code and models will be released.

---


### 54. [Back to the Definition: Estimating Step-Level Advantages via Trajectory Graphs for Agentic Reinforcement Learning](https://arxiv.org/abs/2609.28963)

**<font color=#1a73e8>作者：</font>** Xincheng Yao, Haobo Fu, Weiming Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Group-based reinforcement learning (RL) methods, such as GRPO and its variants, have become a leading paradigm for training reasoning and agentic large language models (LLMs). While their group-normalized advantage estimation is reliable at the response level, it becomes systematically biased at the step level, since coarse-grained trajectory-level advantages are hard to accurately reflect the contribution of individual steps (i.e, failed trajectories may contain valuable steps). Revisiting the foundational RL definition, we notice that GRPO's success on single-turn tasks stems from its advantage estimation strategy, which adheres to the basic definition: the mean reward of multiple actions sampled from the same state constitutes a credible state-value estimate. Extending the faithful estimation to step-level would in principle demand sampling multiple actions from each intermediate state, which is too costly on a per-state basis. To mitigate this issue, we propose a Graph-based Faithful sTep-level credit-assignment framework (GRAFT) that grafts all rollout trajectories into a trajectory graph, recovering node state-values via Bellman iteration on the graph, and assigning credit to each edge by the node value difference. Theoretically, the estimated step-level advantage faithfully adheres to the basic advantage definition in RL. To further ensure the reliability of step-level advantage estimation, we further propose Graph GAE, which extends GAE to the trajectory graph for reducing the impact of state-value estimation bias. Experiments across a range of multi-turn agentic benchmarks show consistent gains over GRPO and superior performance compared to recent agentic RL algorithms. Code will be available at this https URL.

---


### 55. [How People Use ChatGPT in Australia: A WildChat Analysis](https://arxiv.org/abs/2609.28990)

**<font color=#1a73e8>作者：</font>** Ying Ma, Katy Gero, Clément Canonne 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI chatbots are increasingly embedded in everyday life, yet most large-scale studies describe global patterns. This paper presents an Australia-focused analysis of WildChat, a public dataset of real-world ChatGPT interaction logs. Using descriptive analysis and a multi-layer classification scheme, we analysed 37,845 conversations identified as Australian, examining language diversity, work relevance, interaction intent, topic distribution, turn-taking, temporal change, work activities, and Australia-related domains. Our findings show that the Australian subset is strongly action-oriented and comparatively work-oriented, with most interactions classified as doing and a majority of conversations classified as work-related. The dataset also shows multilingual use and a growing presence of self-expression over time. Australia-related conversations frequently invoke local institutions, laws, regulators, education systems, companies, cultural references, and public services. Finally, we outline implications for future research, including local AI evaluation, multilingual participation, context-aware design, and safeguards for everyday high-stakes domains.

---


### 56. [Beneath the Scores: Rethinking Hallucination Evaluation for Video Understanding Models](https://arxiv.org/abs/2609.28991)

**<font color=#1a73e8>作者：</font>** Shuzhi Gong, Fengze Sun, Yuansan Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding is increasingly performed by multi-stage LLM agents that separate temporal grounding, visual observation, and reasoning. Yet these stages are typically evaluated on different benchmarks and distributions, making it difficult to determine where hallucinations originate. We first organize existing benchmarks around these stages and show that their scores provide inconsistent diagnostic signals: stronger stage-level performance does not reliably imply lower downstream hallucination, and even benchmarks targeting the same capability can disagree.
We therefore introduce a causal stage-intervention protocol that overwrites individual stages while holding the downstream task fixed. Across 60,008 runs on three video-agent architectures, we find that grounding is the dominant source of downstream error, with roughly four times the causal impact of corrupting visual observations. Successful grounding depends primarily on locating the correct region rather than precise temporal overlap, explaining why standard mIoU metrics poorly predict downstream reliability. We further find that incorrect evidence is substantially more harmful than missing evidence. Finally, auditing existing benchmarks against these interventions reveals that their scores do not reliably predict causal cascade sensitivity and can fail under distribution shift. These results motivate intervention-based, stage-aware evaluation for trustworthy video agents.

---


### 57. [DistillGuard: Malicious NPM Package Detection and API Attack Chain Analysis via Static Graph and LLM Distillation](https://arxiv.org/abs/2609.28996)

**<font color=#1a73e8>作者：</font>** Siyuan Pang, Yepeng Yao, Zhengwei Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The this http URL ecosystem heavily relies on NPM packages, and software supply chain attacks targeting malicious NPM packages are rampant. Malicious code primarily triggers during package installation, import, and runtime. Traditional static analysis fails to understand code semantics; machine learning-based methods rely on feature extraction, which suffers from concept drift; existing LLM solutions suffer from high invocation costs, high data security risks, and poor performance. To overcome these limitations, we propose DistillGuard, a lightweight malicious NPM package detection framework that combines static graph semantic analysis and LLM knowledge distillation. DistillGuard first acquires multi-granular features through three static analysis modules. Then, it leverages online LLM to distill high-quality security knowledge and structured labels. Finally, it uses LoRa to efficiently fine-tune the open-source Qwen3-8B model to support offline deployment. Experiments show that DistillGuard achieves an accuracy of 95.3\%, a precision of 99.4\%, and an F1 score of 93.8\%, outperforming state-of-the-art tools, improving the F1-score by 11.1 to 30.0 percentage points over the baselines. Our empirical research further reveals the stages of malicious attacks and the distribution of malicious behaviors. We also summarized eight typical API attack chains for malicious activities, providing practical insights for NPM supply chain security defense.

---


### 58. [Automatic Rank Allocation for Low-Rank Adaptation in Large Language Models via lp Regularization](https://arxiv.org/abs/2609.28998)

**<font color=#1a73e8>作者：</font>** Zebang Xie, Chuanyang Zheng, Yik-Chung Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) has become a popular parameter-efficient fine-tuning method for large language models. A key challenge in LoRA is how to determine the rank of each adaptation matrix, as rank directly controls its capacity and efficiency. Existing adaptive-rank methods typically allocate ranks according to manually designed importance scores, which are not directly derived from an optimization objective. In this work, we propose $\ell_p$-LoRA, a principled rank-allocation method based on $\ell_p$ regularization with $0<p<1$, which is a classical sparsity-inducing technique in signal processing and statistics. Specifically, we regularize the energy of each rank-one LoRA component, encouraging redundant components to vanish while preserving important ones. We derive the corresponding proximal subproblem and reduce the matrix optimization to a two-dimensional problem, leading to an implicit thresholding criterion for identifying redundant components. Experiments on natural language understanding and question-answering tasks demonstrate that the proposed method achieves competitive performance with existing LoRA baselines.

---


### 59. [Polite but Misaligned: Evaluating LLM Politeness Judgments Against Human Pragmatic Norms](https://arxiv.org/abs/2609.29001)

**<font color=#1a73e8>作者：</font>** Rong Wang, Kun Sun, Yadong Guo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite strong performance on standard benchmarks, it remains unclear whether large language models (LLMs) evaluate social pragmatics in ways that align with human judgments. We evaluate LLM politeness judgments using two English-language datasets with complementary annotation formats: continuous human ratings and three-way categorical labels. Across the seven evaluated models, we find that inter-model agreement is stronger than model--human agreement. Strategy-level analyses suggest that model--human alignment is associated with explicit linguistic cues, while some rapport-building strategies occur more frequently in misaligned cases. In the categorical task, model predictions exhibit systematic neutral compression, characterized by the overproduction of Neutral labels and the underprediction of Impolite labels. This pattern persists when expert consensus is used as the reference on a diagnostic subset. Our findings highlight the need for pragmatic evaluations that go beyond aggregate agreement metrics by examining directional patterns of model--human disagreement across different human references.

---


### 60. [When Does Action Credit Need Updating?](https://arxiv.org/abs/2609.29007)

**<font color=#1a73e8>作者：</font>** Hongye Yang, Boxiao Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using agents are continually updated with new interaction data. After each policy update, however, previously estimated action credits may become stale. Recomputing them from scratch can require many additional tool calls and environment interactions, making repeated updates increasingly expensive. We ask a simple question: when does historical action credit actually need to be updated? Our key observation is that a change in action value does not necessarily imply a change in the decision. Historical credit can still be useful as long as policy-induced drift is too small to overturn the existing action ranking. Building on this idea, we introduce pairwise branch sensitivity to capture how strongly a policy update affects the downstream regions that distinguish two candidate actions. We then derive a first-order anchored credit-transport estimator that updates historical credit using old interventional trajectories, and propose a Decision-Sufficient Credit Gate (DSC-Gate) that chooses whether to reuse, transport, or resample credit. Experiments show that branch sensitivity explains credit drift substantially better than global policy distance. With sufficient historical data, credit transport reduces estimation error, while its benefit to decision making is concentrated on updates that affect action-distinguishing branches. On a fully independent test set, DSC-Gate changes mean regret by only +0.00004 relative to a gap-based gate while reducing mean new tool steps from 472 to 286, a 39.4% reduction. We observe the same pattern after a real tool-agent parameter update. Overall, our results show that agents do not need to recompute action credit after every policy update: much of the historical evidence can be reused or cheaply corrected, reducing the additional interaction required to keep action decisions up to date.

---


### 61. [AlphaDiverse: Post-Training Local Quantitative Research Agents for Diverse Exploration in Alpha Factor Mining](https://arxiv.org/abs/2609.29014)

**<font color=#1a73e8>作者：</font>** Qingzhuo Wang, Zikun Wei, Zhihua Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems can automate alpha factor mining, but their reliance on external APIs limits control over cost, availability, and confidentiality. Long research loops also tend to revisit a few successful economic mechanisms that lead to research path collapse. To address these limitations, we propose AlphaDiverse, a framework that integrates a multi-agent alpha research system, diverse research path collection, and post-training for local agents. We let the research system generate complementary plan portfolios and vary research environments across loops to collect diverse research paths. Using these diverse traces, we warm-start local Planner and Realizer agents with supervised fine-tuning. Then, we propose a joint GRPO method to optimize both of them using predictive quality and diversity of contributions. Research feedback is confined to inner period data, while a frozen final model is evaluated on a later outer period data, thereby avoiding test-set tuning. Experiments across four Chinese stock universes show that AlphaDiverse can combine competitive prediction with broader exploration.

---


### 62. [MeshHeal: Two-Timescale Self-Healing for Gray Failures in Decentralized LLM Agent Networks](https://arxiv.org/abs/2609.29015)

**<font color=#1a73e8>作者：</font>** Keru Chen, Sen Lin, Yingbin Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decentralized LLM-based multi-agent systems coordinate through local interactions, but an agent can remain responsive while its task-solving quality persistently degrades. Such gray failures require protecting current tasks before sufficient evidence exists to alter future routing, while still allowing recovered agents to rejoin. We introduce MeshHeal, a fully decentralized self-healing framework that couples ability-matched peer review across two timescales. At the fast timescale, an adaptive hierarchy escalates uncertain or low-scoring outputs from repeated single-reviewer evaluation to committee deliberation and, when needed, correction before use. At the slow timescale, a task- and ability-conditioned peer-relative detector aggregates scores to distinguish persistent degradation from ordinary output variation, trigger mandatory committee review, and eventually exclude degraded agents from ordinary routing; recovery probes provide fresh evidence for reintegration. To faithfully evaluate routing, we introduce Model-Backed MAS Evaluation, which ties ability assignments to execution models, since prompt-based ability assignments alone can leave routing errors hidden. Across BBH, MATH, and MMLU-Pro, MeshHeal achieves 0.839 degraded-phase accuracy using 51k total model tokens per task, versus the strongest baseline Symphony's 0.807 accuracy using 115k per task. Under staggered degradation and recovery, MeshHeal isolates degraded agents, keeps them excluded from ordinary task execution until recovery, and returns them to normal routing.

---


### 63. [Exploiting answer-invariant redundancies in satellite imagery for efficient VLM inference on edge](https://arxiv.org/abs/2609.29029)

**<font color=#1a73e8>作者：</font>** Ishani Janveja, Davis Zhang, Seoyul Oh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Onboard vision-language models could enable satellites to answer queries directly, but exhaustive tiled inference over high-resolution imagery is slow and energy-intensive. We identify answer-invariant token redundancy (AITR): image tiles and vision tokens that can be removed without changing the final answer. We present Rift, a two-stage system that performs query-conditioned tile pruning followed by elastic prefill to reduce token budget. We evaluate it on LLaVA-1.5 7B running on Jetson AGX Orin. Compared with exhaustive tiled inference, Rift reduces energy by 78% and latency by 69%, while increasing accuracy from 45% to 73%.

---


### 64. [The Tokens Remember: When Tokenization Bypasses Knowledge Editing and Unlearning](https://arxiv.org/abs/2609.29045)

**<font color=#1a73e8>作者：</font>** Manit Baser, Aditya Nawal, Dinil Mon Divakaran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight LLMs give downstream users control over the inference stack, but this flexibility can undermine post-release guarantees that sensitive knowledge has been modified or removed. Model editing and machine unlearning are used to modify or remove targeted knowledge without retraining models from scratch. However, existing security evaluations of these techniques face two critical limitations. First, they typically require access to either the original pre-edit/unlearning model or auxiliary classifiers to detect modifications or reconstruct pre-edit behavior. Second, they evaluate modifications under the canonical tokenization of an input, implicitly treating tokenization as a benign preprocessing step. We show that this assumption creates a security gap: the same input string can be represented by alternative valid tokenizations that induce different computational trajectories, allowing an adversary to bypass localized modifications and recover information intended to be suppressed.
We introduce Toketive, a simple yet powerful reference-free attack that exploits the tokenization-based side channel to (i) detect modified knowledge and (ii) reconstruct the corresponding pre-edit response. It operates solely on the released model and requires neither the pre-edit model, training data, shadow models, nor auxiliary classifiers. Across five LLMs, six datasets, and six editing and unlearning techniques, we find that 38.6% of alternative tokenizations bypass the modification and recover the pre-edit response. Toketive detects modified facts with an F1 score of 84.2%, a 26.2% relative gain over the strongest baseline, and reconstructs pre-edit responses with 74.5% top-5 accuracy, 21.7% higher than the best baseline. Our results show that localized modifications should not be treated as robust knowledge-control boundaries without adversarial evaluation over alternative representations.

---


### 65. [Where Hallucinations Live: A Cross-Architecture Circuit in VQ-Tokenized Vision-Language Models](https://arxiv.org/abs/2609.29048)

**<font color=#1a73e8>作者：</font>** Shamanthak Hegde, Xiangrui Liu, Maitreya Patel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified vision-language models (VLMs) that tokenize images through a vector-quantized (VQ) codebook routinely hallucinate objects on grounded yes/no benchmarks, yet existing decoding-time fixes treat this as generic miscalibration without an architectural account. Using activation patching across twenty-five models spanning eight LLM families, we identify an early-layer ($L_0$) attention routing circuit shared across VQ-tokenized VLMs and propose a three-gate diagnostic that distinguishes the models carrying it from those that do not. The diagnostic isolates ten positive models (five natural unified-VQ VLMs across three LLM families and five induced variants) and rejects the remaining fifteen. A single-variable architectural swap (LLaVA-1.6 CLIP+MLP $\rightarrow$ VQ+Linear) installs the circuit, while a matched-compute MLP control on identical data does not, isolating vector quantization as the source of the pathological signal; the routing pathway that carries it is one that the backbone already provides. Against tuned VCD and DoLA baselines, tuned DoLA wins on binary calibration, but \textbf{only $L_0$ ablation reduces object hallucination in open-ended generation} (CHAIR$_i$ reduces by $31\,\%$ relatively, whereas tuned DoLA and VCD leave it unchanged or worsen it). These results recast object hallucination in unified VQ VLMs as a property of architecture and pretraining, and yield a targeted intervention that mechanism-agnostic decoding cannot replicate.

---


### 66. [SLCA-GRPO: Resolving Cross-Segment Credit Misattribution in Tool-Calling RL](https://arxiv.org/abs/2609.29050)

**<font color=#1a73e8>作者：</font>** Yan Zhan, Shaobo Liu, Qiunan Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-calling agents produce heterogeneous outputs, interleaving structured tool invocations with user-facing natural language summaries. This output heterogeneity presents a structural failure mode in standard on-policy Reinforcement Learning (RL): algorithms like GRPO indiscriminately broadcast a homogeneous trajectory-level scalar advantage to all tokens. Consequently, gradient noise from summary generation leaks into tool-decision tokens, causing cross-segment credit misattribution and brittle optimization. In this work, we propose SLCA-GRPO, a framework incorporating Segment-Locked Credit Assignment (SLCA). To enable scalable exploration without costly real APIs and stable training, we first construct the Schema-Guided LLM Simulator (SGLS) as foundational training infrastructure. Building on this, SLCA decouples advantage estimation at the structural segment level within a single group of rollouts, without requiring additional rollouts from intermediate states. Supported by Hierarchical Rewards (HierR), SLCA routes execution advantages to tool tokens and preference advantages to summary tokens, eliminating advantage contamination (the dominant cross-segment credit misattribution channel) within each policy update. On a 7B backbone, SLCA-GRPO accelerates convergence and outperforms standard GRPO, ToolPO, and RLTR by +2.53 pp on in-domain evaluation, +1.36 pp on the Berkeley Function-Calling Leaderboard (BFCL), and +9.15 pp on $\tau^2$-Bench under the same training budgets, achieving higher accuracy with reduced tool redundancy and costs.

---


### 67. [From Self-Distillation to Self-Practice: Privileged Information for Multi-Turn Agents](https://arxiv.org/abs/2609.29051)

**<font color=#1a73e8>作者：</font>** Xingyu Su, Abhishek Kumar, Qing Ping 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) has become a popular recipe for post-training LLM agents. It supervises the agent model at the token level with a stronger teacher view of the same model, obtained by conditioning on privileged information (PI). In this work, we show that in multi-turn agents, this paradigm teaches the student to act with confidence but without the information behind it. The trained agent behaves as if it had privileged information it never observed, and its performance falls well short of plain RL, in the worst case below the untrained base model. Therefore, we propose Privileged Self-Practice (PSP), which keeps the PI and moves it from the loss to the sampler. When the student's rollouts on a task mostly fail, we inject a short per-task instruction written by an analyzer model, sample the task again with the instruction in context, and train on the result with an unchanged GRPO objective. The privileged information stays in the prompt and never enters the loss. Across AppWorld and SWE-bench Verified, with three different student models, PSP obtains the best average score in every setting and is the only method that consistently outperforms plain GRPO, improving task-goal completion by up to 65% on AppWorld and the resolved rate by up to 61% on SWE-bench Verified.

---


### 68. [Seeing Is Not Measuring: Tool-Augmented Metric Spatial Reasoning for Vision-Language Models](https://arxiv.org/abs/2609.29073)

**<font color=#1a73e8>作者：</font>** Kai Glantz, Clemens Grange  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) describe scenes well but reason poorly about metric 3D structure such as absolute distances, physical sizes, or egocentric directions. We present a modular, predictor agnostic, tool-augmented framework that equips a small VLM (Qwen3.5-4B) with geometric tools: 3D object detection, metric depth estimation, and deterministic solvers for distance, size and bearing. Each object is detected in the camera frame of its own best view, and the tools use that frame's pose to lift every detection into one shared world frame. Moving metric computation out of the model's weights and into explicit solvers yields large gains on three of four ReVSI-Bench tasks: with a strong monocular detector (WildDet3D), absolute distance rises from 0.46 to 0.74 Mean Relative Accuracy (MRA), relative distance from 39.1% to 67.4%, and relative direction from a below-chance 25.9% to 73.4%. Because any detector can be swapped in behind the tool interface, comparing real detectors against ground-truth boxes separates perception error from reasoning error: orchestration costs only 0.03 MRA. Object size is bounded by the detector: the tools are near-exact on groundtruth boxes (0.97) yet the best real detector barely beats the no-tool baseline (0.61 vs. 0.58), because size reads straight off a box extent monocular detectors get wrong. Without a predefined recipe, the model already sequences the tools correctly on its own, matching a scripted pipeline on three of four tasks.

---


### 69. [CRISS: A Retrieval-Augmented AI Chatbot for Assisting Cancer Registrars](https://arxiv.org/abs/2609.29075)

**<font color=#1a73e8>作者：</font>** Vani Seth, Mohammad Beheshti, Anirudh Kambhampati 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cancer registrars, including Oncology Data Specialists (ODSs), must interpret complex and frequently updated coding and staging standards. We developed CRISS (Cancer Registry Intelligent Support System), a retrieval-augmented generation (RAG) conversational assistant that provides rapid, citation-supported access to registry guidance. This study evaluated whether CRISS could (1) support accurate and citation-supported responses, (2) improve access to and interpretation of relevant guidance, and (3) support training/helpdesk use while preserving human oversight of final abstraction decisions. We built a domain-specific knowledge base from national cancer registry standards, segmented into metadata-tagged passages and indexed as dense embeddings. Retrieved passages were used to generate citation-grounded responses through a large language model (LLM). Open-weight, proprietary, and non-RAG baseline models across Gemini and GPT families were evaluated on easy, medium, and hard registry questions using an LLM-as-a-Judge protocols. RAG configurations consistently outperformed non-RAG approaches, especially as question difficulty increased. Mean grounding scores for RAG were 0.62/0.56/0.59 across easy/medium/hard tiers versus 0.29/0.26/0.29 for non-RAG. RAG models also achieved higher semantic-similarity scores overall. Proprietary RAG models performed strongest on easy and medium questions, while local RAG models ranked highest on hard questions and proprietary models were generally more cautious. Domain-specific RAG improved evidence grounding and response quality for cancer registry questions while enabling citation-supported assistance across complexity levels. CRISS demonstrates the potential of human-centered, citation-grounded AI to support cancer registrars while preserving human oversight for final coding decisions.

---


### 70. [Where Does Exactly-Once Live? Model, Harness, and Tool-Contract Effects on Duplicate Side Effects in LLM Agents](https://arxiv.org/abs/2609.29095)

**<font color=#1a73e8>作者：</font>** Jiapeng Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a tool-using agent's write times out or returns a server error, the action may already have taken effect. Retrying blindly duplicates it -- a second charge, a second announcement, a second deployment -- while giving up skips required work. We ask where exactly-once behaviour should be enforced: in the model, in the agent harness, or in the tool contract. We introduce LIMBO, a deterministic sandbox of six services with realistic contracts (optional idempotency keys, eventually consistent and missing read paths) and twelve fault modes injected at the service boundary, including late commits, redelivery and partial batches; every episode is graded against a ledger of committed effects. Across 25,930 episodes spanning nine recent models, three production agent harnesses, two contract variants and fifteen recovery conditions, the answer depends on the fault. When an immediate read-back can reveal what happened, the model decides: frontier models instructed to act exactly once almost never duplicate a write whose acknowledgement was lost (0.5%), weaker models often do, and the model explains 53% of the explained variance. When it cannot -- the request is still in flight, or the transport delivered it twice -- the same frontier models duplicate in 56% and 74% of episodes, and the contract explains 81%. We prove that no verification-only policy is exactly-once under late commits without a bound on in-flight time. Waiting works when such a bound is short and known, but with heavy-tailed in-flight delays even an hour of waiting per episode falls short of offering an idempotency key on every write, which lowers the duplicate rate from 28% to 4% because agents use keys when they exist. The harness barely matters, a guard that attaches keys transfers across harnesses unchanged, and agents reported success in 90% of the episodes in which they had duplicated an effect.

---


### 71. [TraceGuard: Adaptive Multimodal Poison Filtering through Cross-Feature Rank Agreement](https://arxiv.org/abs/2609.29099)

**<font color=#1a73e8>作者：</font>** Haoyang Li, Yaxin Xiao, Linyan Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal training relies on image-text corpora collected from external sources, creating opportunities for attackers to poison the data. Stealthy attacks can preserve plausible image-text pairs while concealing the differences used by detectors, so apparently clean data can still redirect the trained model. We therefore ask which properties a poison set must preserve for the attack to remain effective. A small poison set must still exert enough collective influence during training to induce the attacker's target behavior. We analyze this influence in terms of how often an attack pattern occurs and how strongly the examples carrying it jointly affect the model. This analysis motivates six corpus-level features that examine cross-modal neighborhoods, recurring text, and changes after text-span erasure without training the victim model. We introduce TraceGuard, an adaptive rank-based filtering method that uses agreement among complementary feature rankings to identify suspicious examples. It refines the selected set through shared patterns and adapts the removal threshold to each corpus without knowing the attack or poison rate. Across 19 attack configurations spanning image-text learning, generative vision-language model fine-tuning, and encoder-transfer tests, TraceGuard removes an average of 98.4% of poisoned examples and 5.4% of clean examples. After training on the filtered corpora, the residual attack metric is at most 1% in 13 configurations. Matched-removal controls and ablations support the contributions of sample selection and adaptive removal. Stress tests also identify detection failures under adaptive attacks and unnecessary removal on poison-free corpora.

---


### 72. [Language Specificity vs. Domain Diversity: Benchmarking Transformers for Bangla Medical NER](https://arxiv.org/abs/2609.29101)

**<font color=#1a73e8>作者：</font>** Rakib Abdullah, Md. Maruful Islam Maruf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medical Named Entity Recognition (NER) for low-resource languages remains a challenging task due to high linguistic variability and a scarcity of domain-specific annotated corpora. This work presents a comprehensive empirical benchmark evaluating three fine-tuned transformer encoders-BanglaBERT, multilingual BERT (mBERT), and XLM-RoBERTa-against GPT-4o mini under zero-shot and few-shot prompting configurations for Bangla medical NER. In contrast to prior studies that evaluated large language models on limited subsets of only 50 samples, we conduct a large-scale evaluation across the full test set of 3,179 samples, providing statistically robust and reproducible baselines. Our fine-tuned XLM-RoBERTa model achieves an F1- score of 0.5959, establishing a new state-of-the-art and surpassing the previously reported best result of 0.5848. Crucially, we demonstrate that the language-specific BanglaBERT model consistently underperforms its multilingual counterparts with an F1-score of 0.4937, indicating that pretraining domain diversity can outweigh language specificity in highly specialized clinical settings. Furthermore, we present a detailed per-entity-type analysis for this task, revealing that Medicine and Specialist categories are recognized with high reliability, achieving F1- scores above 0.83, while the Symptom category remains the most challenging with an F1-score of 0.4367 despite being the most frequent training class. Finally, fine-tuned transformer models outperform the optimal prompting configuration by a factor of 3.76, confirming that prompt-only pipelines remain inadequate for structured clinical entity extraction in low-resource language environments.

---


### 73. [ELF-REG: Scaling Continuous Diffusion Language Models to Reasoning Tasks](https://arxiv.org/abs/2609.29102)

**<font color=#1a73e8>作者：</font>** Zeyu Michael Li, William Xingxu Chen, Bingshuo Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fully continuous diffusion language models (dLMs) denoise continuous representations without intermediate discretization, then decode all response tokens in parallel at the final step. Their performance on challenging reasoning tasks remains less established than that of autoregressive (AR) LLMs and masked dLMs. We scale Embedded Language Flows (ELF) to mathematical reasoning and code generation on GSM8K, MATH-500, HumanEval, and MBPP. We introduce ELF-REG, which improves learning with representation alignment and entanglement (REPA+REG), where a frozen AR teacher supervises intermediate denoiser features and supplies a global representation that is jointly denoised with the response. ELF-REG-L achieves 55.96% pass@1 on GSM8K at 64 network function evaluations (NFE), and 13.39% on MATH-500 and 22.56% on HumanEval at 128 NFE. It outperforms the evaluated comparable-scale dLMs in pass@1 on GSM8K and code, and improves MATH-500 pass@1 from 10.55% for the ELF-L baseline to 13.39% with ELF-REG-L. Without few-step training, the same task-specific checkpoints support strong low-NFE performance through early-stop, which decodes an intermediate clean prediction without completing the denoising trajectory. At 16 NFE, ELF-REG-L reaches 41.21% HumanEval pass@10, outperforming recent continuous dLMs of comparable scale.

---


### 74. [CounterRoute: Self-Routed Reasoning via Hierarchical Counterfactual Credit Assignment](https://arxiv.org/abs/2609.29109)

**<font color=#1a73e8>作者：</font>** Ruochen Jiao, Besnik Fetahu, Zhenyu Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning-capable language models often produce long chains of thought when direct answers suffice, wasting inference compute. Many dual-mode models leave this choice to users. Automating it is challenging because routing targets evolve with the policy, initial mode preferences destabilize exploration, and sequence-level objectives entangle routing with response learning. We introduce CounterRoute, an online reinforcement-learning framework that jointly learns routing and modeconditioned responses in one shared policy directly from a native dual-mode checkpoint, without method-specific SFT warm-up. Paired current-policy counterfactual rollouts assign cross-mode credit only to the routing token, while within-mode GRPO trains response tokens. A paired-to-self-routed curriculum stabilizes early training with forced rollouts from both modes, then increases self-routed updates to improve autonomous routing. Across nine benchmarks, CounterRoute better balances accuracy and efficiency than heuristic and learned adaptive-routing methods. Relative to always-thinking checkpoints, it improves macro-average accuracy while reducing mean generated tokens by 51% for Qwen3-8B and 41% for Qwen3-14B. On instruction-following and commonsense benchmarks where direct answering is strong, think rates fall as low as 1% while response quality improves. Despite training only on math and instruction following, its routing behavior and response quality generalize to held-out coding, science, knowledge, and commonsense benchmarks.

---


### 75. [ClaimMirage: When Self-Claims in Domain Names Change LLM Threat Judgments](https://arxiv.org/abs/2609.29130)

**<font color=#1a73e8>作者：</font>** Daiki Chiba, Hiroki Nakano, Takashi Koide  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Short claims such as not-phishing or official can change how a large language model (LLM) judges a domain name, without explicit prompt-injection commands. We study this manipulation as ClaimMirage: a name under inspection claims its own safety or approval. We analyze 622,080 judgments across 64 brands and five LLMs, comparing ten claims with length- and hyphen-matched controls in constructed brand-like names. Self-claims can substantially reduce or increase alerts, depending on the LLM and input setting. In one setting, risk-denial terms inside the registrable name reduce alerts by 45.3 percentage points even with a basic safeguard: the prompt supplies the potentially impersonated brand and its official domain for comparison. Without these references, endorsement terms at that position increase alerts by 65.6 points in the same LLM. References and component annotation remove some alert reductions but leave others or make them larger. These findings motivate testing resistance to self-claims and seeking independent evidence before treating a domain name under inspection as safe or authorized.

---


### 76. [Tag-Aware Structured Text Translation: Towards a Systematic Understanding](https://arxiv.org/abs/2609.29131)

**<font color=#1a73e8>作者：</font>** Zhanglin Wu, Hengchao Shang, Daimeng Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Internet texts are replete with format tags that carry structural, semantic, and functional meaning. Current large language model (LLM)-based translation systems struggle to balance translation fluency with tag fidelity when processing tagged text. We argue that resolving this tension requires a systematic approach at three interconnected levels: data synthesis, capability building, and multi-objective alignment. At the data level, we identify and formalize a fundamental trade-off between structural tag diversity and translation naturalness in synthetic data generation; existing methods optimize for one at the expense of the other. We propose a hybrid synthesis strategy (Hy-LST) combining LLM-based synthesis tag method and Two-Stage LLM-based synthesis tag method to produce both diverse and natural tagged data. At the capability level, we decompose tag-aware translation into four sub-tasks of increasing difficulty in a multi-task supervised fine-tuning framework, enabling targeted capability acquisition and knowledge transfer. At the alignment level, we design three complementary reward functions under a group relative policy optimization framework, each targeting a distinct objective (fluency, tag fidelity, and tag-scoped translation quality), and show that joint optimization consistently outperforms single-reward alternatives. Experiments on six language directions (en2zh, en2ja, en2de, en2fr, en2ru, de2fr) demonstrate that each level contributes measurable improvements, and the complete system significantly outperforms existing methods. Qualitative analysis reveals specific error patterns and their mitigation after training with our method.

---


### 77. [Scope Before You Persist: Preventing Cross-Family Interference in Agent Memory](https://arxiv.org/abs/2609.29144)

**<font color=#1a73e8>作者：</font>** Yezhou Cheng, Runjia Du, Zeming Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent memory lets language-model agents improve prompts and skills without updating model weights. We show that matching retrieval scope to certification scope enables these edits to support reliable repeated adaptation across recurring task families. We study frozen-model agents on ProcStream-RSI, a 12-round code-repair stream, using Orthogonal Regression Control (ORC), an execution-grounded gate for persistent skill edits. In an intervention that holds proposals and gate decisions fixed, retrieving each accepted skill only for its originating family raises mean hidden trajectory utility from 0.713 under global memory to 0.816 and changes harmful deployments from six of eight to none. In 27 paired randomized-order streams, Scoped-ORC improves mean trajectory utility by 0.063 [0.037, 0.094] over Global-ORC, accepts 63 rather than 12 updates, and produces multiple accepted updates in 19/27 streams, with 0/63 harmful acceptances. The global control reaches 0.713, below the static agent's 0.775, because locally valid edits can interfere with unrelated families. These results establish scope matching as a complementary control for persistent agent memory: certification determines whether an edit is supported, while retrieval scope determines where that evidence authorizes its use.

---


### 78. [A Wrong Turn Does Not Ruin the Journey: Deviation-Guided Skill Self-Evolution for LLM Agents](https://arxiv.org/abs/2609.29154)

**<font color=#1a73e8>作者：</font>** Yichun Feng, Jiawei Wang, Haozhe Sun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly rely on natural-language skills to solve complex tool-use tasks. However, such tasks often admit multiple valid solution paths, making it inappropriate to improve skills by forcing failed trajectories to match a fixed successful trajectory. Moreover, failed trajectories are rarely entirely wrong: an agent may first collect useful evidence and make meaningful progress, but later deviate into an erroneous suffix. We therefore argue that skill self-evolution should identify where productive problem solving begins to break down, rather than reflect coarsely over the entire failure. Based on this insight, we propose SkillPivot, a deviation-point-guided framework for skill self-evolution. SkillPivot detects the transition from a useful prefix to an erroneous suffix using execution validity, goal progress, and action diversity. A stronger teacher then continues from the same prefix and produces a successful alternative under the same interaction history. By contrasting the student's failed suffix with the teacher's successful suffix, SkillPivot generates localized skill updates while preserving already effective guidance. Experiments on ToolQA, LogicBench, and WildClawBench show that SkillPivot consistently outperforms competing skill-evolution methods, improves multiple agent models, and produces compact, transferable skill updates.

---


### 79. [Med-AR: Autoregressive Vision-Language Pretraining for Long-Tailed Chest X-Ray Classification and Uncertainty-Aware Evaluation](https://arxiv.org/abs/2609.29156)

**<font color=#1a73e8>作者：</font>** Janhavi Prabhu, Sahil, Akshay V 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-tailed chest X-ray classification requires visual representations that capture both common abnormalities and subtle, infrequent findings. We propose Med-AR-8B and Med-AR-2B, two radiology-native autoregressive vision-language models pretrained with structured reports, abnormality-focused text, and region annotations. We evaluate the transfer of their visual encoders to multi-label classification against contrastive, self-supervised, and supervised pretrained encoders, including Med-CLIP, CheXFound, EVA-Base, ARK, and BioViL-T, using a common ML-Decoder classification head. To assess fine-grained recognition, we also construct LLM-expanded, report-derived label sets for MIMIC-CXR and CheXpert. Across PadChest, MIMIC-CXR, and CheXpert, Med-AR-8B outperforms Med-CLIP in mean AUROC and AUPRC for head, medium, and tail findings. On MIMIC-CXR, it increases tail-label mean AUPRC from 0.1033 to 0.1441. Med-AR-2B achieves the strongest discrimination results on PadChest. Across the broader encoder comparison, a Med-AR variant achieves the highest mean AUROC and AUPRC in every reported prevalence group on each public dataset. Both Med-AR variants also achieve lower excess area under the risk-coverage curve than Med-CLIP on all three public datasets, indicating improved selective-prediction performance under the evaluated protocol. Internal results are metric-dependent, with Med-CLIP retaining advantages in overall and tail AUPRC and in selective prediction. These findings establish Med-AR as a strong pretraining recipe for long-tailed chest X-ray classification on the evaluated public benchmarks and demonstrate the value of assessing discrimination and selective prediction together.

---


### 80. [IndicBankBench: Evaluating Safety and Reliability of Language Model Assistants in Indian Retail Banking](https://arxiv.org/abs/2609.29167)

**<font color=#1a73e8>作者：</font>** Suvradip Paul, Chandra Bhushan, Harsh Sharma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Banking assistants must use account-specific information to answer requests and, in many cases, take actions through tools. Evaluating only the final response misses important errors. An assistant may ask for information it already has, rely on stale context, select the wrong account, or write an invalid value after stating the correct one. We introduce IndicBankBench, a 799-case benchmark for Indian retail banking spanning five operational domains, a capability/refusal domain, and twenty primary axes. Cases are evaluated at four stages: safety, action and tool use, response adequacy, and advisory quality. Tool use and most safety checks are deterministic. A narrow resolver handles only ambiguous confirmation-before-write cases, while a separate LLM judge evaluates semantic response adequacy. We run every case three times and report strict pass^3, which requires success on all trials. Across the eleven evaluated models, strict reliability ranges from 43.7% to 58.2%, whereas at-least-once success ranges from 60% to 74%. This gap shows that at-least-once success can overstate dependable banking behavior. The case-level diagnostics also distinguish systems that ask unnecessary questions from those that act but fail to reconcile customer context or fully resolve the request. We release the cases, mock environment, and evaluation harness.

---


### 81. [Towards An LLM-Driven Unified Conversion Framework for BT and FSM in Autonomous Intelligent Systems](https://arxiv.org/abs/2609.29228)

**<font color=#1a73e8>作者：</font>** Zhang Qi, Yang Shuo, Zhu Zhengqiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Finite state machine (FSM) and behavior trees (BT) are widely adopted behavioral modeling paradigms for autonomous intelligent systems. While functionally equivalent and inter-convertible in principle, existing transformation methods between FSM and BT face major challenges in preserving behavioral completeness and avoiding model complexity explosion. To overcome these issues, we propose an LLM-driven unified conversion framework that enables automatic, efficient, and semantically consistent transformation between FSM and BT. Specifically, a novel loop execution BT structure is designed for LLM to accurately capture the loop structure in FSM, thereby preserving behavioral completeness. To mitigate the state explosion problem in BT-to-FSM conversion, a depth compression strategy is introduced with LLM prompt to eliminate redundant control nodes, complemented by differentiated hierarchical conversion rules that collectively reduce the number of required sub-FSM. Simulation experiments in multiple autonomous decision-making scenarios demonstrate that the proposed framework enables an accurate and automated bidirectional conversion between FSM and BT. Furthermore, it significantly enhances the scalability and maintainability of generated models compared to traditional approaches, providing a practical solution for behavior model conversion in consumer-grade autonomous intelligent systems such as service robots, game agents, and smart home devices

---


### 82. [EAGER: Enhancing Generative Event Extraction via Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2609.29230)

**<font color=#1a73e8>作者：</font>** Omar Adjali, Siting Liang, Omair Shahzad Bhatti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> End-to-end event extraction remains challenging for large language models as it requires simultaneous identification of event triggers, classification of event types, and extraction of schema-grounded argument spans. We present EAGER, a reinforcement learning framework for generative event extraction that combines fine-grained verifiable rewards with Schema-Contrastive Advantage Estimation to alleviate advantage collapse under sparse binary rewards. Our reward design explicitly targets structural validity, extraction accuracy, groundedness, coverage, over-generation, and span precision. Experiments across seven benchmark datasets show that EAGER consistently outperforms prompting, supervised fine-tuning, and prior reinforcement learning baselines, achieving a substantial improvement over the strongest prior method. Results demonstrate that task-aligned verifiable rewards and contrastive advantage estimation substantially improve structured extraction.

---


### 83. [Post-Training Leaves Behavioral Shadows on Unrelated Decisions](https://arxiv.org/abs/2609.29233)

**<font color=#1a73e8>作者：</font>** Ziyang Zhang, Yubin Jing, Yuanhao Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We find that language models can transfer capabilities through task-unrelated text. Post-training typically improves language models using task-specific data. Prior work on subliminal learning shows that information about these updates can pass through unrelated generations, but has largely focused on traits or preferences using extensive teacher outputs. We introduce Active Taskless Distillation (ATD), which achieves capability transfer using only a single word from the teacher per prompt. ATD probes the behavioral shadow of post-training by selecting prompts where the teacher and student's shared public ancestor is nearly indifferent between two ordinary words. A student initialized from this ancestor learns solely from the resulting prompt-word pairs, without target-task examples, teacher logits, or teacher parameters. In the primary coding experiment with Qwen2.5-1.5B, 5,664nses yield a 5.34 pp gain on HumanEval+ over an exact nuisance-matched control thadisrupts prompt-resperiments showtransfer in scientific knowledge, commonsense reasoning, and reading comprehensins across additional model generations, sizes, and families. Functional analyses show that the learned sid composable, andthat its strength tracks the teacher's update strength.

---


### 84. [Policy as Code: A Coroutine-Bridge Harness for Fast-Reasoning Reliability on CAR-bench](https://arxiv.org/abs/2609.29251)

**<font color=#1a73e8>作者：</font>** Ivan Matveev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> CAR-bench evaluates whether tool-using agents stay reliable under real-world uncertainty, executing every tool inside the evaluator so that each tool-result exchange is a separate agent round-trip. A conventional next-action agent can batch parallel tool calls, but a chain of dependent calls costs it one model call per round of results. We present a coroutine-bridge harness in which the model's only action is to emit a Python program that blocks and resumes in place across evaluator tool exchanges. This decouples model invocation from tool round-trips: on the public test split the agent uses a median of two model calls against seven agent turns per task, resolving a full multi-turn task in a median of 1.8 s of model latency on Cerebras gpt-oss-120b. Because the action surface is executable code, deterministic CAR-bench policies are encoded directly as logic in the tool layer rather than as prompt rules, enforcing compliance at zero reasoning cost. On the official hidden evaluation the harness won Track 2 with 60.0% Pass^3, 4.5x the organizer baseline, at the lowest estimated cost and the fastest median task latency (3.14 s) of any entry scoring above that baseline; the same unchanged harness reproduced an identical 60.0% Pass^3 on GPT-5.5 in the Open track, matching frontier-model agents. A single static prompt, appended with per-task state at the tail, stays byte-identical across calls and across tasks: the frozen submission prompt served 78% of input tokens from cache (86.6% across its warm tail), against 73% over a three-week development corpus in which prompt edits repeatedly reset the cache. This compounds the few-call design into a small fraction of nominal input compute.

---


### 85. [pylazaro: a Python package for anglicism extraction in Spanish](https://arxiv.org/abs/2609.29276)

**<font color=#1a73e8>作者：</font>** Elena Alvarez-Mellado  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lexical borrowings are words from one language that are introduced into another language. Identifying lexical borrowings in text is a relevant task for data-centric fields in Linguistics such as lexicography or corpus linguistics, but none of the standard libraries for text processing offers such a functionality. In this paper we present pylazaro, an open-source Python package for the automatic extraction of unassimilated lexical borrowings (mostly anglicisms) from Spanish text. pylazaro offers a single interface to five sequence labeling models that were trained using different libraries, so that users can run and switch between them without having to deal with the idiosyncrasies of each library. We describe the design and usage of the package, contrast the performance of its models with that of general-purpose LLMs (which perform poorly at this task: F1 below 0.40, compared to 0.86 for the best model in pylazaro) and report on its adoption: pylazaro has been downloaded more than 58,000 times and is the library behind Observatorio Lazaro, a resource that monitors anglicism usage in the Spanish press. pylazaro can be installed via PyPI, is documented in readthedocs and can be tried through a live demo hosted on HuggingFace Spaces.

---


### 86. [Reasoning Instructions Can Break Answer Decoding in Vision--Language Models](https://arxiv.org/abs/2609.29278)

**<font color=#1a73e8>作者：</font>** Zeyan Li, Siyuan Qiu, Jianfeng Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) instructions can distort multiple-choice VLM evaluation when a scorer appends a reasoning cue but reads answer-label logits before the model generates any rationale. We call this CoT-prefix scoring. On ScienceQA, Qwen2.5-VL-7B drops from 80.76% to 45.48%, and across five option-content permutations 93.54% of CoT-prefix predictions select the first slot. Condition-matched linear probes recover 78.94% from the same hidden states, while free generation restores 75.24%, showing that the answer often survives the prefix and the immediate readout fails. Vocabulary and layer diagnostics explain the mismatch: probability mass moves toward continuation tokens, while answer information remains linearly accessible in late layers. The effect recurs with varying severity across datasets and models, though not universally. These results show that CoT-prefix scoring can confound model knowledge with an evaluation-interface mismatch and should be avoided unless the requested and scored output events are aligned.

---


### 87. [From Text Decisions to Pixels: An Study of Jev-Style Visual Choice Model](https://arxiv.org/abs/2609.29283)

**<font color=#1a73e8>作者：</font>** Xunlan Zhou, Xianliang Yang, Li Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual software often needs a decision over supplied alternatives rather than a generated explanation. We present PixelJev, a native-image decision interface that maps an image, a task instruction, and a runtime candidate set to a structured choice and candidate-conditioned probabilities using small open multimodal models. Its initial realization unifies recognition and multiplechoice visual question answering through an existing language-model readout, with separately evaluated options for frozen inference, language-side adaptation, and held-out calibration. Across seven benchmark evaluations, 64-shot source adaptation raises Pets accuracy from 60.13% to 92.40% across optimization seeds and transfers to natural resampling, new texture labels, and A-OKVQA without target fitting, while frozen inference already supports both VQA tasks. A matched prompt-only follow-up on Pets and ScienceQA attributes the large Pets gain to adaptation and identifies a narrower output validity benefit of candidate readout in adapted VQA. Specialist DINOv2 probes remain stronger on source recognition, frozen 4B is stronger than adapted 2B on DTD and ScienceQA, and accuracy gains do not ensure calibrated target probabilities. These findings establish a working starting point for general-purpose visual decision models and identify the remaining requirements: schema robustness, cross-family transfer, and reliable use of visual evidence.

---


### 88. [Grammatical "grandmother neurons" are rare in LLMs](https://arxiv.org/abs/2609.29328)

**<font color=#1a73e8>作者：</font>** Linyang He, Nima Mesgarani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding how Large Language Models (LLMs) encode linguistic structures remains a fundamental challenge in interpretability research. While diagnostic classifiers (or "probes") are widely used for this task, they face significant methodological criticism: training auxiliary classifiers introduces capacity confounds and calibration issues, often making it difficult to distinguish the model's intrinsic representations from the probe's ability to learn the task. To address these limitations, we introduce a probe-free framework for localizing linguistic selectivity at the individual neuron level. Leveraging the controlled contrasts of linguistic minimal pairs, we propose a Neuron Separability Index (NSI), a metric that directly quantifies how reliably single neurons differentiate grammatical from ungrammatical constructions without parameter updates. Applying NSI across 68 linguistic paradigms and seven checkpoints reveals three main patterns: 1) raw separability reaches near-peak levels earlier for morphological and syntactic distinctions than for syntax-semantics interface and conceptual distinctions. 2) after permutation normalization, single-unit selectivity is sparse, weak, and narrowly tuned: only a small fraction of units are sensitive to an average paradigm, and strongly selective "grandmother neurons" are rare. 3) whole-vector linear separability, single-neuron selectivity, and behavioral competence are largely dissociated, and targeted ablations further separate activation selectivity from causal reliance.

---


### 89. [Where LLM Graders Succeed and Break: Evidence from Two Computer-Science Exams](https://arxiv.org/abs/2609.29333)

**<font color=#1a73e8>作者：</font>** Ali Habibullah, Yazan Alshoibi, Mohammad Alshiekh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> One long-form exam in a large course costs hundreds of grader-hours, and qualified graders are scarce; LLM graders are a tempting alternative. To show its pitfalls we grade a practical Computer Vision exam ($570$ dual-graded students) under $171$ configurations spanning closed and open-weights models; the best reaches mean absolute error $1.64/35$, below the $2.61/35$ two human graders achieve against each other. The catch is the prompt: a short ''strict grader'' preamble drives $14$ of $17$ open-weights models out of the graded band ($\text{MAE} \ge 8$), three stopping grading altogether. The damage traces to the preamble's two credit-withholding sentences, not to tone or model scale; one of them, ''never give partial credit'', alone makes two of three probed models stop grading. The closed flagships of three vendors shift calibration under it but stay in the band. In $162$ further configurations on a second, independent Machine Learning exam from another course ($1{,}038$ dual-graded students), the preamble worsens ten models, moving three out of the band into collapse and one into refusal, yet improves seven whose neutral prompts over-mark: the vulnerability replicates, but its direction is exam-specific. Light LoRA fine-tuning repairs it: one adapter on the two exams' pooled $\sim 3{,}900$ graded examples brings five small open models to parity or better with a human grader in agreement with the grader pair, and sensitivity to the three harsh personas nearly vanishes ($\le 0.32$ MAE). We release the anonymised dataset, full ablation grid, and grading, fine-tuning and analysis pipelines.

---


### 90. [SkinAgent AI: A Safety-Grounded Multimodal Agentic Framework for Non-Diagnostic Skincare Support](https://arxiv.org/abs/2609.29341)

**<font color=#1a73e8>作者：</font>** Muhammad Muhtasim Shahriar, Abdullah Mohammad Sayem, Tze Hui Liew 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Consumer-facing skincare AI must coordinate visual evidence, product information, tool use, and user-facing actions within explicit evidence and safety boundaries. This study evaluates SkinAgent AI, a non-diagnostic multimodal framework that combines visual concern routing with grounded and auditable LLM-based orchestration. The architecture includes routing for Acne, Pores, and Wrinkles; photograph-based skin-type estimation; count-informed ordinal acne-severity support; typed tools; database-grounded recommendation and action functions; deterministic safety, privacy, and evidence checks; approval before state-changing actions; and structured trace and replay mechanisms. Visual-model performance and system-level agent behavior were evaluated separately. Across three seeds, the skin-condition routing model achieved 99.84% +/- 0.07% accuracy. Skin-type estimation achieved 88.85% accuracy, while count-informed acne-severity support achieved 84.59% accuracy with a quadratic weighted kappa of 0.9076. On a locked but non-independent 240-case system benchmark, intent accuracy was 80.00%, exact tool-set match was 62.92%, and strict task completion was 47.08%. No violations or successful cross-user leakage events were observed in the finite safety and privacy test suites. Tool-selection errors, incomplete grounding of product attributes, and unreliable failure fallback nevertheless remained. These findings support the feasibility of bounded, database-grounded, and traceable agent orchestration for non-diagnostic skincare assistance. They do not establish clinical readiness, external generalization, formal privacy guarantees, or universal safety. Independent validation, expert assessment, robustness and fairness testing, and prospective evaluation in real-world settings remain necessary.

---


### 91. [The Last Human Gate: Forward Deployed Engineering for Governance Automation](https://arxiv.org/abs/2609.29345)

**<font color=#1a73e8>作者：</font>** Jeremy Canale  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise governance requires decisions, evidence, and accountable authority; it does not require every review task to retain its current human implementation. We develop a task-substitution framework for Digital Governance Frameworks (DGF), treating each gate as an executable contract. Substitution requires sufficient accessible information, valid decision and authority checks, and a reduction in total human work after exceptions, verification, correction, and maintenance are counted. We derive a residual-work threshold and show why automating most cases can still increase labor. Forward deployed engineering connects these conditions to an architecture for agents, rule engines, evidence services, and escalation. DGF-Bench supplies controlled evidence from 300 synthetic projects and 899 evaluable model-project runs. Gemini 3.8 Flash, GPT-5.6 Luna, and DeepSeek v4.1 Flash achieve strict gate success of 94.98%, 83.29%, and 74.18%; complete-route success is 76.92%, 42.33%, and 24.67%. A deterministic control passes all 1,700 gates given the supplied rules and structured facts, locating the comparison in execution of a supplied decision kernel. Evidence audits and 135 repeated runs distinguish correct decisions from reliable execution. A document counterexample establishes an information-sufficiency obstruction. These results support the technical feasibility of replacing human execution of specified governance-review tasks with agents and software. The framework specifies a workforce test based on the complete human effort required at fixed output and quality; the present measurements concern review performance. Sources, dossiers, traces, and analyses are public.

---


### 92. [ArGuard Shared Task: Harmful Content Detection in Arabic Memes and LLM Prompts](https://arxiv.org/abs/2609.29349)

**<font color=#1a73e8>作者：</font>** Firoj Alam, Md. Rafiul Biswas, Mohamed Bayan Kmainasi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> ArGuard is a shared task on harmful content detection in Arabic memes and LLM prompts. It includes two tracks: Track A focuses on multimodal hate detection in Arabic memes, while Track B addresses harmful prompt detection for Arabic LLM safety evaluation. In total, 58 teams registered, 35 participated in the final evaluation, and 27 submitted system-description papers. Participating teams explored models such as AraBERT, Jais, and Qwen3-VL. The best systems achieved macro-F1 scores of 0.823 on A1, 0.419 on A2, 0.984 on B1, and 0.790 on B2. Fine-grained meme classification in A2 was the most challenging setting, partly due to sparse labels and train-test distribution shifts.

---


### 93. [Domain Recentering and Confidence-Weighted Prior Calibration for Vision-Language Models](https://arxiv.org/abs/2609.29358)

**<font color=#1a73e8>作者：</font>** Youngeun Seol, Jimin Shin, Heeseo Yoon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models such as CLIP achieve strong zero-shot classification, yet under distribution shift, visual embeddings drift from fixed text embeddings. Training-free calibration avoids the per-sample optimization of prompt learning, but prior feature calibration gives each image the full bias of one hard cluster. We propose Domain Recentering with Confidence Calibration (DRC), a training-free method adapting CLIP from a set of unlabeled target images. DRC fits a Gaussian mixture once and subtracts from each embedding a posterior-weighted average of component means. It then removes residual class preference with a log-prior correction, estimating the prior from confidence-weighted predictions. Among compared methods, DRC achieves the highest average accuracy on cross-domain datasets, exceeding zero-shot CLIP by 4.13 and 5.07 points with ViT-B/16 and ResNet-50, with gains over CLIP also holding under ImageNet distribution shifts.

---


### 94. [Parts-of-Speech as Emergent Categories in SAE Latent Space](https://arxiv.org/abs/2609.29362)

**<font color=#1a73e8>作者：</font>** Alessandro Bondielli, Lucia Passaro, Serena Auriemma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse AutoEncoders (SAEs) offer a promising way to inspect language model representations, but it is still unclear what kind of linguistic structure their latents expose. We use part-of-speech (PoS) categories as a controlled test case to study whether morpho-syntactic information is encoded by individual latents or by structured groups of features. We find that PoS distinctions are highly recoverable from SAE activations, but do not align with one-to-one latent / category mappings. This recoverability is not reducible to lexical memorisation, and Open and Closed PoS classes differ substantially. Categories are supported by compact groups of sparse latents, with substantial variation across tags. These groups remain stable on held-out data, while also showing overlap between related categories. Our results show that SAEs localise morpho-syntactic information in a distributed and category-dependent form rather than through atomic grammatical features.

---


### 95. [Epistemic-Probabilistic Model for Guarded Multi-Agent LLM Coordination](https://arxiv.org/abs/2609.29366)

**<font color=#1a73e8>作者：</font>** Mehdi Nasiri, Mohammad Saeed Arvenaghi, Sadegh Vaezi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language models (LLMs) have become ubiquitous in applied AI, yet their theoretical foundations remain surprisingly understudied. Viewed through the lens of multi-agent systems theory, several shortcomings come to light: a lack of social intelligence, the absence of coordination mechanisms among agents, unknown emergent behavior, and interactions between agents that are bounded by natural language. We address two of these gaps: the absence of social behavior and the lack of mechanisms for inter-agent coordination. We introduce Epistemic Probabilistic Language Agents (EPLA), a neuro-symbolic architecture for multi-agent coordination under uncertainty. A Symbolic Guard provides structured diagnostic feedback. The LLM generates typed actions, and the Guard controls their execution against an authoritative symbolic state. We formalize the epistemic layer in a gossip testbed through epistemic lottery gossip models, which combine view-based call histories with agent-indexed probability weights. We argue that implementing such a formalism can address shortcomings of agentic LLMs.

---


### 96. [From Policy Documents to Structured Survey Responses: Evaluating Large Language Models for Policy Monitoring](https://arxiv.org/abs/2609.29370)

**<font color=#1a73e8>作者：</font>** Carolyn Cole, Matthias Deschryvere, Toqeer Ehsan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Science, technology, and innovation policies are crucial for competitiveness, yet their diversity and scale make them difficult to map and monitor consistently. Existing approaches rely heavily on manual survey efforts, which are costly and challenging to scale across countries. Large language models (LLMs) enable new possibilities for extracting and structuring information from long and unstructured policy documents. This paper presents an application of LLMs as "AI respondents" for generating structured survey responses from policy texts. We develop a data extraction pipeline based on long-context in-context learning to map information from public web sources into predefined survey categories, including policy instruments, target groups, and thematic areas. The pipeline integrates a validation step using a secondary LLM to assess relevance and evidence, alongside comparisons with human-provided responses. Using a multi-country dataset, we evaluate the alignment between LLM-generated and human-generated outputs through overlap measures and cross-validation. Results show that LLMs achieve high agreement for structured indicators (84-95%), while differences remain in free-text fields, where models tend to provide more detailed procedural descriptions. These findings highlight the potential of hybrid human-AI workflows for policy monitoring, improving both efficiency and scalability while maintaining the need for human validation and contextual interpretation.

---


### 97. [BanglaTurn: A Benchmark and Whisper-Based Model for End-of-Turn Detection in Bangla Speech](https://arxiv.org/abs/2609.29371)

**<font color=#1a73e8>作者：</font>** Mizbaul Haque Maruf  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents BanglaTurn, a corpus for end-of-turn detection in Bangla conversational speech, and a model trained on it. The corpus holds 35,374 samples of 3 to 15 s of podcast speech, labelled for turn state by combining speaker diarization with an LLM pass, with every label then checked by a human annotator. The model pairs a Whisper encoder with task-specific classification heads. On a class-balanced test set drawn from a held-out podcast, it reaches 84.33% accuracy (95% CI 80.3 to 88.1) against 69.28% for the Smart-Turn v3 baseline, and lowers the false negative rate from 51.57% to 7.55% at the cost of a higher false positive rate. We report what encoder layer fine-tuning, multi-scale pooling and INT8 quantization each contribute, and latency stays within 165 to 191 ms end to end on CPU.

---


### 98. [Likelihood Ranking doesn't Scale Like Prompting in LLMs](https://arxiv.org/abs/2609.29390)

**<font color=#1a73e8>作者：</font>** Alessandro Bondielli, Lucia Passaro, Davide Bacciu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM evaluation is commonly performed either by prompting models to produce answers or by scoring candidate outputs with likelihood-based metrics. In multiple-choice QA, however, standard likelihood-based scoring is still conditioned on the question and answer set, and can therefore leverage the same task-conditioned answer-selection interface used in prompting. We study a complementary protocol based on likelihood ranking of declarative statements constructed from the same question--answer pairs. Across 95 decoder-only models, ranging from 0.1B to 104B parameters, and 10 MCQA datasets, we find a systematic divergence between declarative-statement likelihood ranking and prompted answering. Statement-likelihood accuracy remains comparatively stable across scale, whereas prompted answering improves sharply with scale and instruction-tuning. These results suggest that likelihood preferences over controlled declarative alternatives and task-conditioned answer selection probe distinct aspects of model behavior, and should not be treated as interchangeable.

---


### 99. [Baseline Shape Decides the Verdict: A Controlled Re-Examination of Ternary Language Models at 60K Parameters](https://arxiv.org/abs/2609.29397)

**<font color=#1a73e8>作者：</font>** Gautam Veldanda  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ternary (1.58-bit) weights are attractive for microcontroller-class language models, but the sub-1M-parameter regime rests mainly on isolated, single-seed comparisons. One prominent example reports that a routed ternary block (convolution, diagonal SSM and sparse attention mixed by a per-token router) beats a parameter-matched full-precision transformer by 22% at 60K parameters, attributing this to inductive bias. We re-run it under one fixed recipe, three seeds per cell, 98 byte-level runs on one laptop. (i) Baseline shape dominates: at a 16M-byte budget, param-matched transformers span 22.6% in validation loss purely by depth/width choice - far more than any architecture effect we measure there - and the best-shaped transformer ties the routed model, so the published margin is at least partly a baseline-shape effect; the ordering of shapes reverses with budget, so no single fixed shape can be trusted. (ii) At 130M bytes the routed model does win, by 22.2-24.0% over the three transformer shapes we evaluate there - but a plain gated diagonal-SSM block beats it by a further 9.1%, and the routed model's own router puts most of its weight on its recurrent pathway, so the gain does not require routing. (iii) The ternary penalty differs by architecture at the larger budget (+5.3% best transformer vs. +19.5% routed, +28.1% gated SSM), but we cannot attribute that to architecture alone: our transformers keep learned positional embeddings in full precision, 11-22% of their parameters, so they are less quantized than the models they are compared with. (iv) A 90/10 full-precision-then-ternary schedule beats all-ternary training, but only at a stage-2 learning rate about 10x the pretraining peak; at a conventional fine-tuning rate it looks 15.3% worse, reversing the conclusion. The from-scratch baseline was not itself learning-rate tuned, which bounds (iii) and (iv). Code and run logs released.

---


### 100. [Large Language Models for Programming: Actually Fixing or Reimplementing Incorrect Code?](https://arxiv.org/abs/2609.29410)

**<font color=#1a73e8>作者：</font>** Alexandru Stefan Stoica, Traian Rebedea, Marian Cristian Mihaescu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent studies have shown that Large Language Models can effectively solve problems and fix bugs in diverse programming environments, including competitive programming. Existing approaches primarily evaluate LLM performance in problem solving or bug fixing independently, but do not explore the relationship between these two capabilities. This work focuses on determining how much the LLM deviates from a buggy solution to fix the bug compared to a human-written patch, and if there is a bias towards generating entirely new solutions. We construct a dataset with all the submissions ($\sim$ 3000) from a couple of users from Codeforces, and we match each buggy submission with its corresponding human fix. By using the similarity between the buggy solution and the human fix as a baseline, we evaluate the quality of LLM-generated bug fixes on 3 OpenAI GPT models (gpt-5-nano, gpt-5-mini, gpt-5.1). We check if the generated solutions solve the problem by using the Codeforces-R1 dataset, an openly available dataset that has tests generated with the DeepSeek-R1 model. Our findings suggest that LLMs tend to modify more lines than necessary compared to human fixes and, in some cases, generate entirely new solutions. We also observe that LLMs solve more problems correctly when allowed to generate solutions from scratch rather than patch buggy submissions, even when those submissions are close to the human patch. This has important implications for the design of AI-assisted programming tools, particularly in supporting user debugging processes and promoting incremental problem-solving strategies rather than solution replacement.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-228](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
