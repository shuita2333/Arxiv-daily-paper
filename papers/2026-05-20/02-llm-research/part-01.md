# 🧠 大模型相关研究 | 2026年05月20日

> 本类共 **346** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-346](./part-07.md)

---

### 1. [LLM-Based Intelligent Notification Composition: From Static Personalization to Context-Aware Persuasive Messaging](https://arxiv.org/abs/2605.16264)

**<font color=#1a73e8>作者：</font>** Nilesh Agrawal  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Push notifications remain among the most direct channels through which digital platforms engage users, yet existing approaches have invested heavily in who to notify, when to notify, and what to recommend, while leaving how to communicate as the least-optimized stage. This paper argues that message quality is an independent, underinvested lever, and that LLMs create their most differentiated value precisely at this layer.
We make three contributions. First, we define notification message quality along six dimensions (contextual relevance, clarity, actionability, novelty handling, linguistic freshness, and persuasive appropriateness) and show how LLM-based composition improves each relative to templates. Across reviewed deployments, reported improvements range from +8% to +14.5% CTR over static templates and +1% to +2.5% over mature slot-filling systems, though these span heterogeneous systems and should not be treated as directly comparable. Second, we provide an architectural attribution analysis disentangling message generation from adjacent components (targeting, ranking, timing), arguing that observed gains are frequently misattributed to text generation alone. Third, we introduce a three-criterion decision framework specifying when LLM generation is and is not the binding constraint.
We support these arguments through a PRISMA-guided survey (28 sources from 142 screened), examine domain-specific applications across social media, food delivery, and e-commerce, and propose a unified architectural framework with budget-aware routing, grounded generation, candidate ranking, diversity controls, and online learning.

---


### 2. [Helping Customers in Distress: An LLM-powered Agent that Converses, Probes, and Routes](https://arxiv.org/abs/2605.16268)

**<font color=#1a73e8>作者：</font>** Alankar Atreya, Stefan Sylvius Wanger, Devesh Batra 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Banks receive millions of reports of fraud, scams, and disputed transactions every year, making it challenging to accurately direct customers to the appropriate specialist teams for assistance. The existing manual process driven by humans is slow and stressful for both customers and staff. To address this, we develop a customer-facing AI powered triaging agent that leverages large language models (LLMs) to conduct multi-turn conversations, ask relevant questions, and classify cases for accurate, policy-guided routing, making it embedded in the customer journey. To evaluate and continuously improve the agent, synthetic digital twins of real customers were simulated, generating realistic, labelled dialogues based on historical data to test a wide range of real-world scenarios. This work details the triage agent's modelling approach, integration with policy, safety guardrails and reasoning frameworks, the use of the synthetic agent for scalable evaluation, and findings on the AI system's accuracy, robustness, and compliance. Results show that the agent successfully improves triaging of historical cases, achieving a 30.6% increase in classification accuracy, with high satisfaction levels reported by our subject-matter experts, highlighting how targeted probing can lead to more effective triage in banking operations at scale.

---


### 3. [Train the Trainers -- An Agentic AI Framework for Peer-Based Mental Health Support in Battlefield Environments](https://arxiv.org/abs/2605.16269)

**<font color=#1a73e8>作者：</font>** Atmaram Yarlagadda, Eranga Bandara, Ross Gore 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Modern military operations expose soldiers to sustained psychological stress, leading to acute reactions, post-traumatic stress symptoms, and other mental health issues. Although the U.S. Department of Defense offers evidence-based therapies, access to trained professionals in forward-deployed and contested environments is limited. As a result, soldiers with early-stage distress are often evacuated to rear medical facilities, delaying care, reducing readiness, and increasing long-term risks. This paper proposes a Train-the-Trainers framework in which soldiers who have completed therapy and returned to duty are trained as peer facilitators to provide first-line psychological support in operational settings. To scale and standardize this model under severe resource and connectivity constraints, we introduce an agentic AI-enabled platform that augments these recovered soldiers with specialized AI agents. The recovered soldier acts as a human supervisor, coordinating agents for symptom triage, guided peer-support interventions, operational constraint reasoning, training and simulation, and structured documentation for clinical escalation when needed. The AI agents use consensus-driven decision support in high-stakes environments. The architecture functions in air-gapped and low-connectivity settings, maintaining human oversight and ethical safeguards. A functional prototype was developed with the McDonald U.S. Army Health Center, Newport News, VA, USA. By combining peer-based intervention with consensus-driven agentic AI decision support, the framework seeks to cut response times, prevent symptom escalation, reduce unnecessary evacuations, and improve continuity of care. This work shows how agentic AI can serve as a force multiplier for mental health support in austere environments and identifies pathways for broader evaluation and deployment across defense and humanitarian operations.

---


### 4. [ChartDesign: Towards LLM Designer of Data Visualization](https://arxiv.org/abs/2605.16274)

**<font color=#1a73e8>作者：</font>** Mohammed Afaan Ansari, Aniruddh Bansal, Tianyi Zhou  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Charts are the dominant medium for visualizing data, discovering patterns and trends, and communicating data driven insights, yet designing them still requires expensive human effort and expertise, such as selecting appropriate chart types, axis orientations, font sizes, and layouts. Most automatic visualization systems rely on handcrafted heuristics or simple rule matching and therefore struggle to generalize across domains. This work explores the potential of large language models (LLMs) as chart designers. We propose ChartDesign, which post-trains LLMs to imitate human experts and generate chart design attributes given tabular data. To this end, we curate a diverse training corpus of data design pairs from charts in public surveys (PewResearch) and academic repositories (CharXiV). Vision language models are used to extract data and design attributes from these charts, including chart type, sub type, alignment, titles, axis labels, and bar spacing, formatted as JSON. We then fine tune LoRA adapters on Phi3, Qwen3, and InternVL2.5 to learn a mapping from data to design specifications. ChartDesign significantly improves chart design performance over strong baselines, achieving up to 84% accuracy on a held-out test set (vs. 53% for the best baseline) and generalizing to unseen domains. We further show that charts rendered from ChartDesign generated specifications are visually appealing and human preferred, narrowing the human AI gap in data visualization.

---


### 5. [ANNEAL: Adapting LLM Agents via Governed Symbolic Patch Learning](https://arxiv.org/abs/2605.16309)

**<font color=#1a73e8>作者：</font>** Safayat Bin Hakim, Keyan Guo, Wenkai Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents can recover from individual execution errors, yet they repeatedly fail on the same fault when the underlying process knowledge--operator schemas, preconditions, and constraints--remains unrepaired. Existing self-evolving approaches address this gap by updating prompts, memory, or model weights, but none directly repair the symbolic structures that encode how tasks are executed, and few provide the governance guarantees required for safe deployment. We introduce ANNEAL, a neuro-symbolic agent that converts recurring failures into governed symbolic edits of a process knowledge graph without modifying foundation model weights. Its core mechanism, Failure-Driven Knowledge Acquisition (FDKA), localizes the responsible operator, synthesizes a typed patch through constrained LLM generation, and validates the proposal via multi-dimensional scoring, symbolic guardrails, and canary testing before commit. Every accepted edit carries full provenance and deterministic rollback capability. Across four domains and 27 multi-seed runs, ANNEAL is the only evaluated system that commits persistent structural repairs--strong baselines such as ReAct and Reflexion achieve high episodic recovery yet retain 72-100% holdout failure rates on recurring faults, whereas ANNEAL reduces these to 0% in the tested recurring-failure settings. Ablation confirms that removing FDKA eliminates all structural repairs and drops success rate by up to 26.7 percentage points. These results suggest that governed symbolic repair offers a complementary paradigm to weight-level and prompt-level adaptation for persistent fault elimination.

---


### 6. [DACA-GRPO: Denoising-Aware Credit Assignment for Reinforcement Learning in Diffusion Language Models](https://arxiv.org/abs/2605.16342)

**<font color=#1a73e8>作者：</font>** Amin Karimi Monsefi, Dominic Culver, Nikhil Bhendawade 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models are a compelling alternative to autoregressive models, yet existing RL methods for diffusion treat all denoising steps as equally important and rely on biased, high-variance likelihood estimates. We identify two fundamental weaknesses: the absence of temporal credit assignment across the denoising trajectory, and the systematic bias of mean-field likelihood estimates used for policy optimization. To address these, we propose Denoising-Aware Credit Assignment for GRPO (DACA-GRPO), a lightweight, plug-and-play enhancement for any GRPO-style trainer. DACA-GRPO introduces two complementary mechanisms: Denoising Progress Scores, which extract per-token importance weights from intermediate predictions at no additional forward cost, and Stratified Masking Likelihood, which partitions token positions into strata so that each token is predicted with most of the sequence as context, reducing the mean-field bias. Applied on top of three GRPO base methods, DACA-GRPO achieves consistent improvements across seven benchmarks spanning mathematical reasoning, code generation, constraint satisfaction, and constrained generation, with gains of up to 5.6pp on math reasoning, 7.4pp on code generation, 36.3pp on constraint satisfaction, and 5.9pp on JSON schema adherence.

---


### 7. [LoopQ: Quantization for Recursive Transformers](https://arxiv.org/abs/2605.16343)

**<font color=#1a73e8>作者：</font>** Rui Fang, Hsi-Wen Chen, Ming-Syan Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models (LoopLMs) improve parameter efficiency by recursively reusing Transformer blocks, enabling deeper computation under a fixed model size. However, this reuse makes LoopLMs more fragile under post-training quantization (PTQ). We present the first systematic study of quantization in LoopLMs and identify three challenges: distribution shift across roles, state reuse across loop transitions, and recursive error accumulation. To address these challenges, we propose LoopQ, a loop-aware PTQ framework that preserves a shared quantized backbone while introducing lightweight adaptations. LoopQ combines activation scaling, selective transformation, cross-loop state alignment, and trajectory-aware optimization to reduce distributional mismatch within loops and error accumulation across loops. Experiments across seven benchmarks show that, under W4A4 quantization, LoopQ improves average downstream accuracy by 68.8% and reduces average perplexity by 87.7% compared with the strongest static PTQ baseline.

---


### 8. [Goal-Conditioned Supervised Learning for LLM Fine-Tuning](https://arxiv.org/abs/2605.16345)

**<font color=#1a73e8>作者：</font>** Shijun Li, Kaiwen Dong, Xiang Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models often require fine-tuning to better align their behavior with user intent at deployment. Existing approaches are commonly divided into online and offline paradigms. Online methods, such as RL-based alignment, can directly optimize outcome quality but typically rely on external reward models and iterative rollouts, making them costly and difficult to deploy in many cases. Offline methods are more efficient, but prevailing approaches such as supervised fine-tuning (SFT) and direct preference optimization (DPO) remain limited: SFT typically collapses graded feedback into binary supervision, while DPO depends on paired preference data that is often unavailable or expensive to construct.
In this paper, we propose goal-conditioned supervised learning (GCSL) as an offline fine-tuning framework for LLMs. Our core idea is to treat feedback signals directly as an explicit goal and train the model, purely through supervised learning, to generate responses that achieve that goal. To better exploit graded feedback, we further introduce a novel goal formulation that defines learning as consistently pursuing outcomes above a target quality threshold, rather than imitating samples from a selected high-quality subset. This design mitigates the bounded-learning effect of SFT and classic GCSL by explicitly guiding the model to learn the directional progression of quality. We also propose natural-language goal representations to better leverage the semantic understanding and reasoning capabilities of LLMs. We evaluate our method on three tasks: non-toxic generation, code generation, and LLM for recommendation. Results show that our approach consistently outperforms standard offline fine-tuning baselines while retaining the efficiency, scalability, and simple data requirements of supervised learning.

---


### 9. [PropGuard: Safeguarding LLM-MAS via Propagation-Aware Exploration and Remediation](https://arxiv.org/abs/2605.16346)

**<font color=#1a73e8>作者：</font>** Bingyu Yan, Xiaoming Zhang, Jinyu Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (LLM-MAS) have become a promising paradigm for solving complex tasks through role specialization, tool use, memory, and collaborative reasoning. However, these interactions create new security risks that malicious instructions injected through messages, tools, or memories can propagate across agents and rounds, causing system-level compromise. Existing defenses largely rely on local filtering or graph-based anomaly detection, but they often fail to trace fine-grained propagation paths or remediate contaminated states without disrupting benign collaboration. We propose PropGuard, a propagation-aware framework for safeguarding LLM-MAS. PropGuard constructs a dual-view spatio-temporal graph that combines response-centric risk estimation with full-state evidence preservation. Guided by these risk priors, a GE-GRPO trained inspector sequentially explores the full-state graph to recover compact suspicious propagation subgraphs. PropGuard then verifies harmful propagation through subgraph-aware diagnosis and applies source-guided remediation to correct upstream contamination and replay affected downstream interactions. Experiments across four communication architectures and five attack settings demonstrate that PropGuard consistently lowers attack success while maintaining high task-level defense success, achieving a favorable effectiveness--efficiency trade-off.

---


### 10. [HPC-LLM: Practical Domain Adaptation and Retrieval-Augmented Generation for HPC Support](https://arxiv.org/abs/2605.16347)

**<font color=#1a73e8>作者：</font>** Nourin Shahin, Izzat Alsmadi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern scientific research increasingly depends on High-Performance Computing (HPC) infrastructures, yet many researchers face significant operational barriers when interacting with cluster environments, job schedulers, GPU resources, and parallel computing frameworks. General-purpose large language models (LLMs) provide useful coding assistance but often lack the domain-specific operational knowledge required for reliable HPC support. This paper presents HPC-LLM, a retrieval augmented and domain-adapted assistant designed to support common HPC workflows including Slurm scheduling, MPI execution, GPU utilization, filesystem management, and cluster troubleshooting. The proposed framework integrates automated documentation ingestion, dense retrieval, lightweight domain adaptation using QLoRA, and local inference within a modular orchestration pipeline. To support domain adaptation, we construct an HPC-oriented corpus from publicly available university HPC documentation, curated operational examples, and synthetic instruction-answer pairs generated from retrieved HPC content. The resulting dataset contains approximately 9,000 to 24,000 HPC-focused training examples spanning job scheduling, GPU computing, distributed training, storage systems, and cluster administration topics. We fine-tune Llama 3.1 8B using QLoRA and evaluate the resulting model against several open weight baselines under retrieval-augmented settings on JetStream2 infrastructure. Experimental results indicate that the adapted 8B model achieves performance comparable to substantially larger general-purpose models while operating under significantly lower GPU memory requirements and inference latency. In particular, the adapted model approaches the performance of Qwen 2.5 14B while requiring substantially fewer computational resources.

---


### 11. [Geometric Asymmetry in MoE Specialization: Functional Decorrelation and Representational Overlap](https://arxiv.org/abs/2605.16349)

**<font color=#1a73e8>作者：</font>** Feilong Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures achieve scalable capacity through sparse routing, yet the geometric structure of expert specialization remains poorly understood. We introduce a unified Jacobian-PCA-Grassmann framework for analyzing MoE layers in both function space and representation space. Across pretrained MoE Transformers (Mistral, Qwen), we find a consistent structural asymmetry: experts exhibit strong functional decorrelation (consistently low, near-zero cross-expert Jacobian alignment) while their routed representations occupy distinct but partially overlapping subspaces. This indicates that functional decorrelation and representation overlap coexist rather than coincide in MoE specialization. Controlled routing experiments further indicate that routing sparsity appears to be a key factor shaping this geometry: top-k routing induces sharper functional separation and larger subspace divergence, whereas fully soft routing yields more entangled expert structure. Together, these results suggest a geometric interpretation in which MoE layers may be viewed as implementing locally decorrelated operators over overlapping submanifolds on a shared representation manifold, and provide a general diagnostic framework for studying conditional computation in modern Transformer architectures.

---


### 12. [StrLoRA: Towards Streaming Continual Visual Instruction Tuning for MLLMs](https://arxiv.org/abs/2605.16353)

**<font color=#1a73e8>作者：</font>** Chang Che, Ziqi Wang, Hui Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual Visual Instruction Tuning (CVIT) enables Multimodal Large Language Models to incrementally acquire new abilities. However, existing CVIT methods operate under a restrictive task-incremental setting, where each training phase corresponds to a single, predefined task. This does not reflect real-world conditions, where data arrives as a continuous stream of interleaved and dynamically evolving tasks. To bridge this gap, we introduce Streaming CVIT (StrCVIT), a more general and realistic setting where models learn from a stream of data chunks containing a dynamic mixture of tasks. In StrCVIT, a model must simultaneously acquire new abilities, reinforce recurring abilities, and mitigate forgetting. Existing CVIT methods fail here as they cannot reliably distinguish or adapt to the heterogeneous task samples within each chunk. We therefore propose StrLoRA, a regularized two-stage expert routing framework. StrLoRA first performs task-aware expert selection using the textual instruction to activate a sparse subset of relevant experts, reducing cross-task interference. It then applies token-wise expert weighting within this subset, where contribution weights are computed via cross-modal attention between local visual tokens and the global instruction representation. To maintain stability across the non-stationary stream, a routing-stability regularization aligns current routing distributions with a historical exponential moving average reference. Extensive experiments on a newly developed StrCVIT benchmark show that StrLoRA substantially outperforms existing methods, effectively enhancing model's abilities from continuously evolving data streams.

---


### 13. [Augmenting Human Evaluation with LLM Judges: How Many Human Reviews Do You Need?](https://arxiv.org/abs/2605.16354)

**<font color=#1a73e8>作者：</font>** Jane Paik Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as automated evaluators of AI systems, including in high-stakes applications. In this role, LLMs are used to generate judgments about the quality, appropriateness, or even safety of model outputs. This approach is motivated by practical constraints. Expert human ratings are costly and difficult to scale, whereas LLM ratings can be produced quickly at low cost. However, current approaches to deploying LLM evaluators are ad hoc, typically limited to reporting agreement metrics between human and LLM judges as a justification for substitution of human ratings, and lack a formal basis for study design. This paper (1) shifts the role of the LLM judge from substitutive to auxiliary, and (2) formulates the LLM-as-a-judge paradigm as one of augmenting human evaluation through a two-stage sampling design, where LLM evaluations are measured for all observations at the first stage and human ratings are partially observed for a subsample at the second stage. We propose to use a doubly robust estimator from the missing data literature, which takes advantage of the robustness property against the prediction model, since the missingness model is known by design. Using the asymptotic variance of this estimator, we propose how sample sizes of human and LLM ratings can be determined to achieve a targeted level of power. We also show that a study can be efficiently designed by allocating more human ratings for types of evaluations where the predictability of LLM ratings is not high. To the best of our knowledge, there is very little guidance on how much human oversight should be retained when validating benchmarks.

---


### 14. [LEAF: A Living Benchmark for Event-Augmented Forecasting](https://arxiv.org/abs/2605.16358)

**<font color=#1a73e8>作者：</font>** Mingtian Tan, Mihir Parmar, Palash Goyal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly applied to forecasting. To evaluate this capability while mitigating pre-training data contamination, several living benchmarks have been proposed. However, existing benchmarks either lack the multidimensional events essential for accurate forecasting due to data scarcity, or focus on relatively closed environments. To assess the predictive capabilities of LLMs in complex, real-world scenarios, we propose LEAF, the first living benchmark for event-augmented forecasting tasks, including future event probabilities, trend and time series forecasting. LEAF utilizes a recursive retrieval agent system paired with dual-agent cross-validation to provide comprehensive and relevant auxiliary text for forecasting. Evaluating state-of-the-art proprietary and open-weight LLMs, we find that these models can leverage signals extracted from complex events to enhance predictive performance. In the stock domain, we find that LLMs achieve better performance on equities they confidently identify as more predictable. Furthermore, the events demonstrate a strong correlation with the target equities. To this end, LEAF provides a necessary, dynamically updating testbed to continuously track and drive progress in event-driven forecasting tasks.

---


### 15. [How Many Visual Tokens Do Multimodal Language Models Need? Scaling Visual Token Pruning with F^3A](https://arxiv.org/abs/2605.16359)

**<font color=#1a73e8>作者：</font>** YiJie Huang, Yiqun Zhang, Zhuoyue Jia 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models improve perception by feeding increasingly long visual token sequences into language backbones, but the resulting inference cost raises a basic scaling question: as multimodal models grow, how many visual tokens are actually needed, and how should they be allocated under a fixed visual token budget? Existing training-free pruning methods typically answer this with one-shot proxies such as decoder attention, visual similarity, or conditional diversity. We argue that visual token pruning is better viewed as task-conditioned evidence search, especially under aggressive compression and across model scales. We propose F^3A, a training-free router for visual token pruning that operates before the language model consumes image tokens. F^3A builds lightweight question-conditioned cues, matches them to visual-grid tokens through frozen sparse sensing heads, and allocates a fixed vision token budget via coarse evidence localization, local refinement, coverage-preserving competition, and recovery of under-covered regions. It requires no model training, no extra LLM forward pass and preserves the original multimodal prompting and decoding pipeline.

---


### 16. [ProxyKV: Cross-Model Proxy Pruning for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2605.16360)

**<font color=#1a73e8>作者：</font>** Junjie Li, Jiong Lou, Jie Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient long-context inference in Large Language Models (LLMs) is severely constrained by the Key-Value (KV) cache memory wall, yet existing pruning methods force a choice between
low-latency heuristics that sacrifice precision and high-precision reconstruction methods that incur prohibitive prefilling overhead. To bridge this scoring-cost--accuracy gap, we propose
ProxyKV, a cross-model proxy pruning framework that offloads importance scoring to a lightweight intra-family Small-Model Proxy executed asynchronously to the Large-Model Target. To bridge
the architectural gap between heterogeneous models, we design the HybridAxialMapper, which disentangles temporal feature extraction from cross-head alignment, together with a
Multi-Granularity Hybrid Loss that shifts the learning objective from rigid regression to relative ranking consistency. Across the Llama-3.1, Qwen-2.5, and Qwen-3 families spanning targets
from 7B up to 32B parameters on LongBench, SCBench, and RULER, ProxyKV matches KVZip on aggregate (recovering $\sim$$98.7\%$ of its mean accuracy) while delivering up to a $3.21\times$
prefilling speedup on Llama-3.1-8B (dual-GPU; $\sim$$1.5\times$ shared single-GPU) and sustaining the speedup at contexts up to 170k tokens on Qwen-2.5-7B.

---


### 17. [Fre-Res: Frequency-Residual Video Token Compression for Efficient Video MLLMs](https://arxiv.org/abs/2605.16366)

**<font color=#1a73e8>作者：</font>** Yigui Feng, Qinglin Wang, Yang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video MLLMs face a persistent tension between spatial fidelity and temporal coverage: preserving fine-grained visual details requires many spatial tokens, while capturing short-lived events requires dense temporal sampling. We propose \textbf{Fre-Res}, a budget-adaptive dual-track video-token compression framework that separates these two forms of evidence. Fre-Res preserves sparse high-fidelity spatial anchors and represents dense temporal evolution through compact residual-frequency tokens. Specifically, it applies temporal 1D-DCT to inter-frame residual trajectories in vision-latent space, where we observe strong low-frequency concentration. To align frequency-domain dynamics with native visual embeddings, Fre-Res introduces a Spatial-Guided Absorber that injects temporal residual information into spatially corresponding anchor tokens. Across fine-grained short-video and long-video reasoning benchmarks, Fre-Res achieves a favorable accuracy--efficiency trade-off, matching or approaching full-token performance while substantially reducing visual-token length. Extensive ablations further show that temporal-frequency residuals preserve causal transition cues, while spatial anchors remain essential for fine-grained object and layout reasoning.

---


### 18. [GeoSym127K: Scalable Symbolically-verifiable Synthesis for Multimodal Geometric Reasoning](https://arxiv.org/abs/2605.16371)

**<font color=#1a73e8>作者：</font>** Jinhao Jing, Zheng Ma, Jinwei Liang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Multimodal Models (LMMs) often struggle with geometric reasoning due to visual hallucinations and a lack of mathematically precise Chain-of-Thought (CoT) data. To address this, we propose the GeoSym Engine, an automated and scalable neuro-symbolic framework. By leveraging a type-conditional grammar and an analytic SymGT Solver, it derives exact symbolic ground truths and seamlessly integrates with a robust rendering pipeline to produce high-precision geometric diagrams. Using this engine, we construct GeoSym127K, a difficulty-stratified dataset featuring 51K high-resolution images, 127K questions with symbolic ground truths, and 55K answer-verified CoT QA pairs. We also introduce GeoSym-Bench, an expert-curated suite of 511 complex samples for rigorous evaluation. Through extensive supervised fine-tuning (SFT), we demonstrate that GeoSym drives concentrated improvements specifically on diagram-dependent and multi-step geometry tasks. Our Qwen3-VL-8B model gains an absolute +22.21% on the MathVerse Vision-Only subset and reaches 61.52% (+6.19% improvement) on WeMath, mitigating long-horizon logic fragmentation and outperforming advanced closed-source models like Doubao-1.8. Furthermore, applying Reinforcement Learning with Verifiable Rewards (RLVR) via GRPO reveals that initializing from structural SFT checkpoints substantially elevates the performance ceiling over zero-shot RL. Driven by deterministic exact-match signals, this showcases the robust scaling potential of our verifiable reasoning synthesis. Datasets and code are available at this https URL and this https URL.

---


### 19. [M$^2$FedAQI: Multimodal Federated Learning for Air Quality Prediction on Heterogeneous Edge Devices](https://arxiv.org/abs/2605.16375)

**<font color=#1a73e8>作者：</font>** Manjil Nepal, Kimsie Phan, Tamoghna Ojha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate air quality prediction is essential for public health, environmental monitoring, and industrial safety. However, most existing approaches rely on centralized learning paradigms, which introduce challenges related to scalability, privacy preservation, and communication overhead in distributed Internet of Things (IoT) environments. Moreover, current federated learning (FL) based solutions predominantly utilize unimodal data, limiting their capability to capture complex environmental patterns. To address these limitations, we propose M$^2$FedAQI, a lightweight multimodal federated framework for decentralized Air Quality Index (AQI) prediction across heterogeneous edge devices. The proposed framework integrates visual and tabular modalities through a feature modulation based fusion mechanism that enables efficient cross-modal interaction while maintaining low computational overhead. M$^2$FedAQI is evaluated on two benchmark datasets, PM25Vision and TRAQID, for both classification and regression tasks under centralized and federated settings. Experimental results demonstrate that M$^2$FedAQI consistently outperforms existing approaches, achieving improvements of up to 11.0\% in Accuracy, 3.53\% in AUC, 12.2\% in F1-score, and 18.0\% in $R^2$, while reducing MAE and RMSE by up to 25.4\% and 20.4\%, respectively, compared with the strongest baselines. Furthermore, deployment on heterogeneous edge devices demonstrates efficient resource utilization in terms of communication overhead, memory footprint, and computational cost. To enhance communication security, TLS-based authentication is incorporated to ensure secure client participation and protect the FL communication channel from unauthorized third-party access without modifying the underlying FL protocol.

---


### 20. [Mixing Times of Glauber Dynamics on Masked Language Models](https://arxiv.org/abs/2605.16378)

**<font color=#1a73e8>作者：</font>** Suvadip Sana, Sami Wolf, Neer Mehta 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked language models (MLMs) define local conditional distributions over tokens but do not, in general, correspond to any consistent joint distribution over sequences. This raises a fundamental question: what global distributional behavior is induced when such conditionals are used iteratively for generation? We address this question by modeling iterative masked-token resampling as a Glauber dynamics Markov chain on the discrete space of token sequences. We first show that MLM conditionals are intrinsically incompatible: we introduce a rectangle test that certifies this incompatibility and empirically verify its prevalence across modern MLMs. We then provide a theoretical analysis of the induced Markov chain. Under bounded cross-token influence, we establish a high-temperature contraction result implying $O(n\log n)$ mixing time where $n$ is the sequence length. In contrast, we prove that under a uniform local margin condition, the chain exhibits metastability, with exponentially slow escape from semantic basins at low temperatures. Empirically, we demonstrate a phase transition in mixing behavior as a function of temperature and sequence length, consistent with the theoretical predictions. We further characterize the induced stationary behavior through semantic trajectories, identifying persistent structures such as long-lived traps and recurrent semantic basins, with political content serving as a measurable case study.

---


### 21. [Hilbert-Geo: Solving Solid Geometric Problems by Neural-Symbolic Reasoning](https://arxiv.org/abs/2605.16385)

**<font color=#1a73e8>作者：</font>** Ruoran Xu, Haoyu Cheng, Bin Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometric problem solving, as a typical multimodal reasoning problem, has attracted much attention and made great progress recently, however most of works focus on plane geometry while usually fail in solid geometry due to 3D spatial diagrams and complex reasoning. To bridge this gap, we introduce Hilbert-Geo, the first unified formal language framework for solid geometry, including an extensive predicate library and a dedicated theorem bank. Based on this framework, we propose a Parse2Reason method containing two steps of first parsing then reasoning. In the parsing step, we utilize conditional description language (CDL), a formalized language composed of predicates specifically designed to construct geometric conditions, to represent both problem description (natural text) and solid diagrams (visual image). In the reasoning step, we leverage those formal CDL and the theorem bank to perform relational inference and algebraic computation, generating strictly correct, verifiable, and human-readable reasoning processes. Notably, our proposed Hilbert-Geo is also applicable to plane geometry. To advance geometric reasoning, we curate two expert-annotated dataset SolidFGeo2k and PlaneFGeo3k, which are furnished with geometric formal language annotations, solutions and answers. Extensive experiments show that our proposed method achieves the state-of-the-art (SOTA) performance 77.3% in SolidFGeo2k and 84.1% in MathVerse-Solid (one small subset in MathVerse dedicated to solid geometry), substantially outperforming leading MLLMs, such as Gemini-2.5-pro (54.2% on SolidFGeo2k) and GPT-5 (62.9% on MathVerse-Solid). In addition, our method achieves the SOTA accuracy 80.2% in PlaneFGeo3k, demonstrating the generality of the Hilbert-Geo in geometric reasoning. Our code and datasets will be publicly available.

---


### 22. [Auditing Multimodal LLM Raters: Central Tendency Bias in Clinical Ordinal Scoring](https://arxiv.org/abs/2605.16386)

**<font color=#1a73e8>作者：</font>** Jiaqing Zhang, Sandeep Elluri, Bhanu Cherukuvada 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (LLMs) are increasingly explored as automated evaluators in clinical settings, yet their scoring behavior on ordinal clinical scales remains poorly understood. We benchmark three frontier LLM families against supervised deep learning models for scoring Clock Drawing Test (CDT) images on two public datasets using the Shulman rubric. While fully fine-tuned Vision Transformers achieve the best calibration (MAE 0.52, within-1 accuracy 91%), zero-shot LLMs remain competitive on tolerance-based agreement (GPT-5 MAE 0.67, within-1 accuracy 92%) despite higher absolute error. However, per-score analysis reveals that all three LLM families exhibit a pronounced central tendency effect (systematic endpoint compression): predictions are systematically compressed toward the middle of the scale, with over-prediction at the low end (score 0 to 1) and under-prediction at the high end (score 5 to 4). This effect disproportionately affects the clinically critical extremes where accurate scoring most impacts screening decisions for cognitive impairment. Targeted ablations show that neither few-shot exemplars spanning the full score range nor removing clinical terminology from the prompt eliminates the effect. Our findings extend the LLM-as-a-judge bias literature from NLP evaluation to clinical assessment, and highlight the need for calibration-aware evaluation and post-hoc calibration before deploying LLM-based raters in high-stakes screening workflows.

---


### 23. [WinDeskGround: A Benchmark for Robust GUI Grounding in Complex Multi-Window Desktop Environments](https://arxiv.org/abs/2605.16402)

**<font color=#1a73e8>作者：</font>** Haoren Zhao, Tianyi Chen, Zhen Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have revolutionized GUI automation, yet their efficacy is largely established on idealized, single-layer interfaces. This paper identifies a critical reliability gap: state-of-the-art agents face distinct robustness challenges in real-world desktop environments characterized by multi-window stacking, occlusion, and visual clutter. To address this, we introduce WinDeskGround, a novel benchmark and synthesis framework tailored for evaluating GUI grounding robustness. Unlike static datasets, our framework parametrically generates complex desktop scenarios by controlling window occlusion, layout density, and semantic similarity, thereby simulating the distribution shifts of authentic workflows. We construct a diverse meta-dataset of 1,356 high-fidelity instruction-target pairs and conduct comprehensive evaluations of five leading MLLMs. Our results demonstrate that while top-tier agents excel in simplified settings, their accuracy declines under partial occlusion. WinDeskGround provides a valuable benchmark to facilitate the assessment and advancement of GUI agent robustness in realistic environments. The code is available at this https URL.

---


### 24. [When Vision Speaks for Sound](https://arxiv.org/abs/2605.16403)

**<font color=#1a73e8>作者：</font>** Xiaofei Wen, Wenjie Jacky Mo, Xingyu Fu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress in video-capable MLLMs, we find that their apparent audio understanding in videos is often vision-driven: models rely on visual cues to infer or hallucinate acoustic information, rather than verifying the audio stream. This issue appears across both state-of-the-art open-source omni models and leading closed-source models from providers such as Google and OpenAI. We characterize this failure mode as an audio-visual Clever Hans effect, in which models appear (falsely) audio-grounded, but actually exploit visual-acoustic correlations without verifying whether the audio and visual streams are truly aligned. To systematically study this behavior, we introduce Thud, an intervention-driven probing framework based on three counterfactual audio edits: Shift, which tests temporal synchronization; Mute, which tests sound existence; and Swap, which tests audio-visual consistency. Beyond diagnosis, we further study a two-stage alignment recipe: intervention-derived preference pairs teach audio verification, while event-level general video preferences regularize the model against over-specialization. Our best 10K-sample recipe improves average performance across the three intervention dimensions by 28 percentage points, while slightly improving performance on general video and audio-visual QA benchmarks.

---


### 25. [Multilingual OCR-Aware Fine-Tuning and Prompt-Guided Chain-of-Thought Reasoning for Multimodal Large Language Models](https://arxiv.org/abs/2605.16409)

**<font color=#1a73e8>作者：</font>** Qinwu Xu, Xin Liu, Yifan Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical character recognition (OCR) and multilingual text understanding remain major failure modes of multimodal large language models (MLLMs), particularly in real-world images containing cluttered layouts, small fonts, blur, occlusion, and complex typography.
We present an OCR-aware multilingual multimodal training framework that combines (i) large-scale synthetic OCR-to-translation data generation, (ii) OCR-aware supervised fine-tuning (SFT) with LoRA adaptation, and (iii) structured visual chain-of-thought (CoT) prompting for reasoning under uncertain visual conditions. Using a LLaMA-based multimodal architecture, the proposed framework substantially improves OCR completeness, multilingual translation accuracy, and robustness under degraded visual conditions.
Experimental results on multilingual receipts, menus, posters, signs, handwritten text, and document images demonstrate significantly improved visual-text grounding compared with the baseline model. In particular, the proposed OCR-aware post-training framework improves extraction of small, blurred, spatially scattered, and partially occluded text while reducing reliance on language priors under uncertain OCR conditions. Qualitative comparisons with frontier multimodal systems, including GPT-5-class and Gemini-family models, further suggest improved OCR grounding and reduced hallucination under noisy and visually ambiguous OCR scenarios.
Overall, the results indicate that data-centric OCR-aware multimodal post-training provides an effective and scalable direction for improving multilingual OCR and OCR-based visual question answering systems.

---


### 26. [Test-Time Hinting for Black-Box Vision-Language Models](https://arxiv.org/abs/2605.16410)

**<font color=#1a73e8>作者：</font>** Kaihua Hou, Abhijith Varma Mudunuri, Jiaxing Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time scaling (TTS) methods have proven highly effective for LLMs, yet their application to vision-language models (VLMs) remains relatively underexplored. Existing VLM TTS methods largely require open-weight model access or expensive repeated sampling, and are evaluated primarily on multimodal mathematical and scientific reasoning benchmarks rather than general visual understanding tasks. In this paper, we propose Test-Time Hinting, a method that improves VLM performance via a single VLM call and requiring only black-box API access, which makes it broadly applicable to frontier closed-weight models. Our method is motivated by the observation that VLM errors tend to cluster around recurring failure patterns. We therefore train a lightweight hint generator model to predict, for a given test input, which "hint" should be prepended to the prompt, providing targeted contextual or procedural guidance that steers the VLM away from its characteristic failure modes. We show that Test-Time Hinting improves the accuracy of multiple closed-weight VLMs on natural-image VQA benchmarks and that these gains generalize to unseen benchmarks and VLMs without retraining the hint generator.

---


### 27. [Reducing Hallucination in Vision-Language Models via Stage-wise Preference Optimization under Distribution Shift](https://arxiv.org/abs/2605.16411)

**<font color=#1a73e8>作者：</font>** Qinwu Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hallucination remains a fundamental challenge in vision-language models (VLMs), where autoregressive generation may produce linguistically plausible yet physically inconsistent or visually ungrounded responses due to likelihood maximization under joint probabilistic modeling.
We propose a stage-wise preference optimization framework for hallucination reduction through targeted multimodal data construction. Rather than directly optimizing on generic instruction-following data, our approach progressively constructs hallucination-focused preference pairs near known failure boundaries. The framework emphasizes ambiguous spatial orientation, object relationships, OCR uncertainty, and adversarial false-premise training. Hallucinated negatives are generated through minimally perturbed yet visually inconsistent alternatives, enabling Direct Preference Optimization (DPO) to better separate grounded reasoning from plausible hallucination.
Experiments on open-source benchmarks and real-world multimodal evaluation scenarios demonstrate improved grounding consistency, reduced hallucination, and more informative grounded responses. Cross-model qualitative evaluation further shows that the proposed multimodal LLM DPO framework produces more visually grounded responses than several frontier proprietary VLMs, such as in ambiguous spatial reasoning and adversarial false-premise settings. The results suggest that hallucination may arise not only from limited model capacity, but also from inherent tendencies of autoregressive probabilistic generation to favor linguistically plausible continuations under weak visual grounding. Future work may explore physical consistency modeling, uncertainty-aware multimodal reasoning, and architectural alternatives beyond standard autoregressive decoding.

---


### 28. [CAVE: A Structured Credit Assignment Approach for Fragmented Visual Evidence Reasoning](https://arxiv.org/abs/2605.16416)

**<font color=#1a73e8>作者：</font>** Tengda Guo, Jie Leng, Hanlei Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have achieved strong performance on general multimodal reasoning, yet remain challenged in integrating nonlocal visual information to support semantically underdetermined visual reasoning. We describe this challenge as Fragmented Visual Reasoning. To this end, we propose Credit Assignment for Visual Evidence (CAVE), a structured process-reward method based on GRPO for interleaved visual reasoning. Specifically, CAVE evaluates the contribution of intermediate steps at the action level via three complementary reasoning process signals: belief update, evidence acquisition, and adaptive focus control, thereby guiding the model to optimize each reasoning action and learn more reliable visual reasoning strategies. Meanwhile, we construct TRACER-Bench, which covers four nonlocal and semantically confusable reasoning dimensions and provides key intermediate evidence to supervise reasoning paths. Experiments demonstrate that CAVE substantially improves performance on tasks requiring fragmented visual evidence integration, covering both public benchmarks and our newly introduced TRACER-Bench, while retaining competitive performance on general multimodal evaluations. Further analyses reveal that CAVE effectively improves the visual reasoning capacity and exhibits stronger robustness under longer-range and deeper cross-region dependencies.

---


### 29. [Agentic Pipeline for Self-Synchronized Multiview Joint Angle Monitoring in Uncalibrated Environments](https://arxiv.org/abs/2605.16419)

**<font color=#1a73e8>作者：</font>** Juncheng Yu, Lusi A, Haoxuan Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Kinematic monitoring plays a critical role in long-term rehabilitation for patients with spinal cord injury (SCI), where multi-view markerless motion capture methods have shown significant potential. However, owing to the reliance on calibration and the difficulty of achieving multi-view synchronization, their deployment in patient self-deployed environments remains challenging. In this work, we propose an agentic pipeline for self-synchronized multi-view joint angle monitoring in uncalibrated environments using two cameras without hardware triggers. The Multimodal large language models enable automatic video synchronization and agent-driven self-verification. State-of-the-art monocular 2D pose estimation models are employed to extract candidate poses, where an agent-based selection mechanism is then applied to automatically identify and track the target subject, thereby producing consistent 2D poses in the presence of multiple individuals and occlusions. Such 2D poses are optimized to estimate joint angles from uncalibrated multi-view pose sequences, ensuring interpretability through explicit geometric modeling. Validation against Vicon system demonstrated the strong performance, achieving an MAE of $5.97^\circ \pm 2.36^\circ$ and a Pearson correlation coefficient of $0.962 \pm 0.014$. The proposed method is expected to provide a practical, patient self-deployable system to perform daily kinematic monitoring in uncalibrated home environments.

---


### 30. [Nonlinear Bipolar Compensation: Handling Outliers in Post-Training Quantization](https://arxiv.org/abs/2605.16423)

**<font color=#1a73e8>作者：</font>** Peilin Sun, Jianxin Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Network quantization has emerged as one of the most practical model compression techniques, which significantly reduces a model's memory and compute consumption by mapping floating-point numbers to low-bit representations. However, existing quantization methods typically suffer from the speed-accuracy tradeoff and limited generalization. To address these issues, recent compensation-based methods offer an efficient yet general solution by introducing additional lightweight linear layers into the quantized network. However, the accuracy of these methods suffers from their limited compensation capability and high sensitivity to outliers. In this paper, we propose Nonlinear Bipolar Compensation (NBC), a post-training quantization approach that introduces nonlinear compensation to reduce the effect of outliers. We further design Bipolar Logarithmic Transformation (BLT), which compresses outliers by mapping both the quantized input and the quantization error into a transformed space. A simple linear layer is then applied for compensation in the transformed space, preserving the efficiency of our method. Extensive experiments across various tasks, models, and quantization methods confirm the effectiveness, efficiency, robustness, and generality of our NBC approach.

---


### 31. [A Theory of Training Profit-Optimal LLMs](https://arxiv.org/abs/2605.16430)

**<font color=#1a73e8>作者：</font>** Sophie Hao, William Merrill  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling LLMs requires tremendous computational resources, and recent advances in AI have gone hand in hand with massive amounts of capital expenditure. While it is established that scaling up LLMs reliably increases model quality (quantified in terms of loss or downstream evaluations), it is unclear how these quality improvements translate to potential revenue, and whether revenue increases would offset costs of larger-scale training and inference. In this work, we develop an economic model for characterizing the rational behavior of an LLM training firm by combining scaling laws with microeconomic theory. Under our model of firm behavior, LLM quality can be increased with more parameters and training tokens, leading to more potential adoption by consumers, who each have a quality threshold for using the LLM. On the other hand, additional parameters and training tokens both incur additional costs. We analyze the profit maximization problem for this model under compute-bound and data-bound regimes. In the compute-bound regime, optimal model size and token budget track hardware efficiency $E$ (FLOPs/\$) at a near-linear rate; total training cost then scales sub-quadratically in $E$. Data efficiency improvements incentivize larger models and training expenditure. When we are limited to $D$ data, profit-optimal training expenditure scales as $D^2/E$, i.e, increase with data and decreases with hardware efficiency (as well as data efficiency). Finally, we analyze practical trends in training expenditure: current trends are consistent with our most permissive model variants in the compute-bound regime, but are not profit-optimal in the data-bound regime or assuming hardware advances will stall. Overall, our results provide a theory of profit-optimal LLM training, providing a foundation for engaging critically with industry statements and supporting long-term economic decision making.

---


### 32. [CT-DegradBench: A Physics-Informed Benchmark for CT Degradation Detection and Severity Estimation](https://arxiv.org/abs/2605.16431)

**<font color=#1a73e8>作者：</font>** Yousra Nabila Taifour, Marouane Tliba, Zuheng Ming 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed tomography (CT) images are frequently degraded by acquisition artifacts, including noise, blur, streaking, aliasing, and metal artifacts. Yet CT enhancement is still largely evaluated using image quality metrics with limited perceptual and clinical validity, while existing datasets remain focused on isolated restoration tasks, hindering unified benchmarking across diverse degradation types. We present CT-DegradBench, a dataset and benchmark for CT degradation detection and severity estimation under controlled single- and mixed-artifact settings. CT-DegradBench enables systematic evaluation across multiple degradation families and severity levels within a common experimental framework. We further propose SeSpeCT (Semantic-Spectral CT degradation estimation), a framework that combines semantic priors from medical vision-language models with complementary frequency-domain cues for artifact analysis. SeSpeCT constructs a training-free semantic quality axis in the multimodal embedding space using radiology-informed text prompts, without task-specific fine-tuning, and combines it with spectral features that capture degradation-specific frequency patterns. The resulting representation enables joint prediction of artifact type and severity. Experimental results show that SeSpeCT consistently outperforms the evaluated baselines under both single- and mixed-degradation settings. The framework is available at this https URL.

---


### 33. [KVCapsule: Efficient Sequential KV Cache Compression for Vision-Language Models with Asymmetric Redundancy](https://arxiv.org/abs/2605.16439)

**<font color=#1a73e8>作者：</font>** Yingbing Huang, Tharun Adithya Srikrishnan, Steven K. Reinhardt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have emerged as a critical and fast-growing extension of Large Language Models (LLMs) that enable multimodal reasoning through both text and image inputs. Although VLMs enrich the capabilities of language models, they also inherit and amplify key computational bottlenecks: the memory overhead caused by the large key-value (KV) cache during autoregressive decoding. This challenge is particularly severe in VLMs, where images produce longer token sequences and denser feature representations compared to text. Moreover, the spatial and information-rich nature of vision tokens introduces structured attention patterns that make many LLM-oriented KV cache compression techniques ineffective when applied directly to VLMs.
In this work, we conduct a detailed empirical analysis of the behavior of vision tokens, highlighting the critical differences from purely text-based models. Based on these insights, we propose KVCapsule, a novel KV cache compression framework for vision tokens. KVCapsule keeps the pretrained VLM backbone frozen, requires no modification to the attention computation modules, and can be integrated into existing VLMs through lightweight compression and reconstruction components. We evaluate KVCapsule on multiple VLMs and benchmark tasks, demonstrating up to 2x improvement in TPS and 2.4x reduction in KV cache memory at a 60% compression ratio, with negligible degradation in accuracy or response quality. Our findings offer practical pathways to scale VLM inference under constrained memory budgets and inspire further research into structure-aware cache compression for multimodal models.

---


### 34. [Membership Inference Attacks on Discrete Diffusion Language Models](https://arxiv.org/abs/2605.16445)

**<font color=#1a73e8>作者：</font>** Shailesh Kasivelrajan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked Diffusion Language Models MDLMs replace autoregressive generation with iterative demasking and their privacy properties are largely unstudied. We study membership inference attacks MIA on fine tuned MDLMs and show they are significantly more vulnerable than current grey box baselines suggest. We extract a 46 dimensional feature vector from the models reconstruction loss at four masking ratios and train XGBoost and MLP classifiers on top. On the MIMIR benchmark across six text domains XGBoost achieves mean AUC 0.878 peaking at 0.930 on Pile CC and beats the SAMA grey box baseline by 0.062 AUC on average. A leave one signal out ablation shows that the ELBO trajectory alone drives most of this with a mean drop of 0.130 when removed while attention features add almost nothing below 0.003. We also design a shadow model transfer attack where K equals 3 surrogate MDLMs trained on data from unrelated domains generate classifier labels with no access to the target domain. This achieves 0.858 mean AUC within 0.020 of the white box oracle and establishes shadow model transfer as a practical and near equally effective attack path.

---


### 35. [Peak-Detector: Explainable Peak Detection via Instruction-Tuned Large Language Models in Physiological Sign](https://arxiv.org/abs/2605.16452)

**<font color=#1a73e8>作者：</font>** Jiahui Li, Yida Zhang, Zixuan Zeng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate peak detection across diverse cardiac physiological signals, including the Electrocardiogram (ECG), Photoplethysmogram (PPG), Ballistocardiogram (BCG), and Bodyseismography (BSG), is fundamental for cardiovascular monitoring but is often hindered by artifacts and signal variability. Conventional algorithms are typically engineered with expert knowledge for a single signal modality, limiting their generalizability. Conversely, deep learning-based methods often lack interpretability, limiting transparency for expert verification and hindering expert-computer interaction. To address these limitations, we introduce Peak-Detector, a novel framework that leverages instruction-tuned Large Language Models (LLMs) for robust, cross-modal, and explainable peak detection. A core innovation of our framework is a "peak-representation" technique that transforms time-series data into a condensed format, preserving critical event information while significantly reducing signal length. This representation provides a crucial inductive bias, guiding the LLM to reason over physiologically meaningful events rather than raw, noisy data. The model is optimized through a two-stage process: supervised fine-tuning (SFT) followed by reinforcement learning (RL) with a multi-objective reward function. The model's self-explanation capabilities are cultivated by fine-tuning on a custom-built Peak-Explanation dataset. Across four modalities-ECG, PPG, BCG, and BSG-spanning seven datasets (six public benchmarks plus one real-world cohort), Peak-Detector demonstrates strong cross-modal performance, achieving best or tied-best detection under clinically relevant temporal tolerance. Beyond accuracy, the generated rationales surface failure modes and support verification and error analysis.

---


### 36. [Multi-hop Relational Contrastive Learning: Extending Spatial Contrastive Pre-training Beyond Pairwise Relations](https://arxiv.org/abs/2605.16456)

**<font color=#1a73e8>作者：</font>** Sheikh Tanvir Ahmed, Md. Tanvir Raihan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding how objects relate to each other in space is fundamental to scene understanding, yet most contrastive pre-training approaches only model pairwise relationships, leaving richer compositional and multi-hop interactions largely unexplored. We introduce Multi-Hop Relational Contrastive Learning (MRCL), a framework that extends spatial contrastive learning to graph-structured scene representations. By tracing k-hop paths through scene graphs built from detected objects, MRCL captures implicit spatial dependencies that go well beyond what direct object pairs can express. We define a multi-level contrastive objective spanning nodes, edges, and multi-hop paths, encouraging embeddings that remain stable across object semantics while staying responsive to spatial layout. On a GQA subset, MRCL produces spatially-aware representations that improve content-based graph retrieval (NDCG@5 = 0.748) and consistently benefit downstream tasks, including spatial relationship recognition and graph-based question answering. Together, these results suggest that multi-hop relational supervision offers substantially richer structural guidance than pairwise-only methods, leading to visual representations that are more robust, compositional, and geometry-aware.

---


### 37. [Identifiable Token Correspondence for World Models](https://arxiv.org/abs/2605.16457)

**<font color=#1a73e8>作者：</font>** Youngin Kim, Ray Sun, Inho Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based world models have shown strong performance in visual reinforcement learning, but often suffer from temporal inconsistency in long-horizon rollouts, including object duplication, disappearance, and transmutation. A key reason is that most existing approaches treat next-frame prediction purely as a token generation problem, without explicitly modeling correspondence between tokens across time. We formulate next-frame prediction as a structured probabilistic inference problem with latent token correspondence variables, deriving a model in which each next-frame token is explained either by copying a token from the previous frame or by generating a new token. Our experiments show state-of-the-art performance on 4 challenging benchmarks. The proposed method achieves a return of 72.5% and a score of 35.6% on the Craftax-classic benchmark, significantly surpassing the previous best of 67.4% and 27.9%. We release our source code on this https URL.

---


### 38. [Strategic Over-Parameterization for Generalizable Low-Rank Adaptation](https://arxiv.org/abs/2605.16470)

**<font color=#1a73e8>作者：</font>** Jing Gao, Zhong-Yi Lu, Pan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting large language models (LLMs) to downstream tasks via full fine-tuning is increasingly impractical due to its computational and memory demands. Parameter-efficient fine-tuning (PEFT) approaches such as Low-Rank Adaptation (LoRA) mitigate this by confining updates to a compact set of trainable parameters, but this aggressive reduction often sacrifices generalization, especially under transfer across heterogeneous tasks and domains. We revisit the tension between parameter efficiency and adaptation capacity, and ask whether the two are truly at odds. We answer in the negative by introducing LoRA-Over, a framework grounded in a simple principle: enrich the optimization landscape during training, then collapse the enrichment at inference. LoRA-Over injects auxiliary parameters into the low-rank adapters during training to broaden the effective hypothesis space, and through a decomposition-based reformulation folds them back into a standard low-rank structure with negligible reconstruction error, keeping inference cost identical to vanilla LoRA. Since not all weight matrices benefit equally from added capacity, we further propose two scheduling strategies, one statically predefined and one dynamically determined at runtime, that direct extra capacity where most needed. We evaluate LoRA-Over on language understanding (GLUE, T5-Base), dialogue (MT-Bench), arithmetic reasoning (GSM8K), and code generation (HumanEval), using LLaMA 2-7B and LLaMA 3.1-8B. Across all benchmarks and scales, LoRA-Over consistently outperforms vanilla LoRA, showing that principled over-parameterization designed to vanish at inference is an effective lever for improving PEFT generalization. Code will be released upon acceptance.

---


### 39. [Visual Agentic Memory: Enabling Online Long Video Understanding via Online Indexing, Hierarchical Memory, and Agentic Retrieval](https://arxiv.org/abs/2605.16481)

**<font color=#1a73e8>作者：</font>** Aiden Yiliu Li, Nels Numan, Anthony Steed  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long video understanding requires more than large context windows. It also needs a memory mechanism that decides what visual evidence to retain, keeps it searchable over long horizons, and grounds later reasoning in recoverable observations rather than compressed latent state alone. We propose Visual Agentic Memory (VAM), a training-free framework with three components. Online Indexing supports selective evidence retention under streaming constraints. Hierarchical Memory organises retained evidence in a Parallel Representation that aligns temporal context with spatial observations. Agentic Retrieval searches, inspects, and verifies candidate evidence before producing a grounded answer. On OVO-Bench, VAM achieves the highest RT+BT average (68.41) across all reported baselines, improving over end-to-end use of the same underlying MLLM (Gemini 3 Flash, 67.46). On the month-scale split of MM-Lifelong train@month (105.6 hours over 51 days), VAM reaches 17.11%, second only to ReMA with GPT-5 (17.62%). These results suggest that long-horizon video understanding benefits from treating visual memory as an explicit, inspectable, and queryable substrate. Code is available at this https URL.

---


### 40. [The Scaling Laws of Skills in LLM Agent Systems](https://arxiv.org/abs/2605.16508)

**<font color=#1a73e8>作者：</font>** Charles Chen, Qiming Yu, Yuhang Gu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As agent systems scale, skills accumulate into large reusable libraries, yet their scaling laws remain poorly understood. Across 15 frontier LLMs, 1,141 real-world skills, and over 3M routing or execution decisions, we identify two coupled laws. Routing law: single-step routing accuracy decays logarithmically with library size ($R^2{>}0.97$ for all models), with errors progressing from local skill competition to cross-family drift and capture by overly general "black-hole skills". Execution law: before state realization, joint routing is approximately multiplicative, whereas correct execution can improve difficult downstream decisions by about $4{\times}$. A single parameter, the routing logarithmic decay slope $b$, couples the two laws: routing-side fits predict execution-side rescue across models, showing that the same library property controls both pre-execution collapse and downstream recoverability. The laws are actionable: law-guided optimization raises held-out routing accuracy from 71.3% to 91.7%, reduces hijack from 22.4% to 4.1%, and transfers directionally to downstream ClawBench and ClawMark execution settings, improving mean pass rate from 49.3% to 61.6% on ClawBench and from 28.4% to 34.5% on ClawMark. These results show that agent performance depends not only on model capability, but also on the structure, granularity, and exposure policy of the skill library.

---


### 41. [Alignment Drift in Long-Term Human-LLM Interaction: A Mechanism-Oriented Framework](https://arxiv.org/abs/2605.16516)

**<font color=#1a73e8>作者：</font>** Xintong Yao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Long-term interaction with LLM-based systems may produce alignment drift: a gradual process in which system outputs become less constrained by the user's current message and more shaped by prior interaction history, while still appearing helpful, coherent, and responsive. This process is difficult to detect because the user's subjective experience may improve as the system becomes more familiar, useful, and attuned. Existing research on human-LLM interaction has largely focused on short-term task performance, isolated outputs, or single-instance alignment problems, leaving slow and cumulative interaction-level dynamics undercharacterized. This paper proposes a mechanism-oriented framework for describing alignment drift. The framework defines the distinction between signal A and signal B, explains how drift develops through feedback loops and sub-pattern selection, divides the process into three interactional regimes, and identifies boundary conditions for controlling drift. By framing alignment drift as a recursive interactional process rather than an isolated model-side failure, the paper provides a conceptual basis for studying long-term human-system interaction.

---


### 42. [SWoMo: Neuro-Symbolic World Model for Cataract Surgery Simulation](https://arxiv.org/abs/2605.16530)

**<font color=#1a73e8>作者：</font>** Ssharvien Kumar Sivakumar, Akwele Johnson, Anirudh Dhingra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Realistic surgical simulation plays a crucial role in training novice surgeons and in the development of autonomous agents. World models can scale such simulation environments to realistic and diverse procedures by predicting future patient states conditioned on current observations and surgical actions. However, current state-of-the-art approaches often fail to satisfy key criteria required for clinical applicability, including visual realism, physically grounded interactions, and the ability to simulate scenarios beyond the training distribution. Hence, we introduce SWoMo, a neuro-symbolic world model for cataract surgery simulation that decouples motion generation from visual realism. The symbolic component, consisting of a rule-based simulator and scene graph representations, models motion dynamics and tool-tissue interactions, while a diffusion model produces realistic visual appearance, including textures and tissue deformations. We propose an inverse pairing strategy that reconstructs real surgical videos in the simulator to obtain paired simulated and real videos, which are then used to train our video diffusion model for the reverse objective of sim-to-real translation. Our experiments show both qualitative and quantitative improvements over prior work. We demonstrate that our simulator further satisfies the key criteria, including generalisation to unseen interaction geometries, improvements in downstream phase detection, and unsupervised video style transfer. The code, data, and model weights are available at: this https URL

---


### 43. [LLMs in Qualitative Research: Opportunities, Limitations, and Practical Considerations](https://arxiv.org/abs/2605.16538)

**<font color=#1a73e8>作者：</font>** Henry Salgado, Meagan R. Kendall, Martine Ceberio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper examines the opportunities, limitations, and practical considerations associated with the use of large language models (LLMs) in qualitative research. Drawing on a multidisciplinary perspective that combines expertise in qualitative methods and explainable AI, the paper argues that responsible integration of LLMs into qualitative workflows requires researchers to engage critically with a curated set of technical parameters, that is, context window constraints, temperature and top-p sampling settings, user and system prompt design, and model documentation in the form of system cards. The paper situates these considerations within the epistemological commitments of qualitative research, including reflexivity, positionality, and interpretive judgment, and discusses how the opacity of contemporary LLMs differs from earlier natural language processing tools such as topic models and lexicon-based sentiment analyzers.

---


### 44. [World Model-Enabled Causal Digital Twins for Semantic Communications in Physical AI Systems](https://arxiv.org/abs/2605.16547)

**<font color=#1a73e8>作者：</font>** Lingyi Wang, Tingyu Shui, Walid Saad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semantic communication has emerged as a promising paradigm for enabling goal-oriented networking. However, most existing semantic communication solutions are tailored to one-shot tasks and optimize instantaneous performance. Hence, they cannot be used to support closed-loop dynamic systems with physical artificial intelligence (AI), in which the transmitted semantics affect not only the current inference outcome but also future control actions, state evolution, and ultimately long-horizon task performance. To address this gap, this paper investigates goal-oriented semantic communications for physical AI systems with closed-loop sensing-communication-inference-control. In particular, the problem of semantic communications is formulated as a long-term return-per-bit maximization under wireless bit-budget constraints while capturing both control efficiency and communication efficiency. To solve this problem, a novel causal information value (CIV) metric is introduced to evaluate the marginal contribution of each semantic token to the expected long-term return by transmission interventions. Then, a world-model-enabled causal digital twin (WM-CDT) framework is proposed to capture the dynamics of closed-loop physical AI systems and enable counterfactual reasoning for long-horizon imagined rollouts. Based on these imagined rollouts, an actor-critic policy is trained for long-horizon agent control with high data efficiency, while the semantic token selector is trained through CIV-per-bit evaluation. Extensive simulations on an AirSim-Sionna-based unmanned aerial vehicle (UAV) navigation simulator show that the proposed WM-CDT framework achieves significant improvement in return-per-kbit and navigation success rate compared to existing reinforcement learning solutions.

---


### 45. [Counterparty Modeling is Not Strategy: The Limits of LLM Negotiators](https://arxiv.org/abs/2605.16575)

**<font color=#1a73e8>作者：</font>** Romain Cosentino, Sarath Shekkizhar, Adam Earle 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Negotiation requires more than inferring what the other side wants: it requires using that information to make advantageous offers and counteroffers over multiple turns. We study whether large language model (LLM) agents do this in a controlled multi-attribute bargaining environment. We find that current LLM agents can model a counterparty's preferences, but do not reliably turn that knowledge into strategic bargaining. When given negotiating partner preference information, agents model it accurately and early in their reasoning traces, yet this does not reliably improve outcomes for the informed side. Turn-level analyses show why: agents often respond to what they believe the counterparty values, but do not consistently pair those moves with gains on their own high-value attributes. Sellers are more accommodating overall, and in asymmetric-information conditions, the informed side often makes the more weakly compensated concessions. Because agents fail to leverage this underlying utility structure for strategic advantage, their final agreements are heavily dictated by surface-level opening anchors rather than actual utility weights. Finally, requiring agents to explicitly state concession-for-reciprocity trades before making an offer makes individual turns look more strategic, but ultimately fails to improve the efficiency of the final agreements.

---


### 46. [How Few-Shot Examples Add Up: A Causal Decomposition of Function Vectors in In-Context Learning](https://arxiv.org/abs/2605.16591)

**<font color=#1a73e8>作者：</font>** Entang Wang, Yiwei Wang, Aleksandra Bakalova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) excels at new tasks from minimal examples, yet we still lack a mechanistic explanation of how few-shot prompts shape a model's function vector (FV)--a causal activation direction that drives task behavior on the ICL query. Across tasks and models, an $n$-shot FV is well-approximated by a linear combination of example-level sub-FVs, suggesting additive and composable contributions from individual demonstrations. Beyond additivity, we show that models contextualize individual examples' representations based on prior examples to adaptively reweight which demonstrations dominate the FV: attention shifts toward examples that are more informative and less ambiguous under the context. Finally, a causal decomposition separates Query-Key routing from Value updates, finding that contextualization's most consistent contributions to FV quality arise from Query-Key alignment--particularly in ambiguous settings--while Value-mediated effects are more heterogeneous. Together, these results unify additive superposition with context-dependent attention reweighting into a mechanistic, testable account of how few-shot prompts implement tasks.

---


### 47. [GRASP: Graph Agentic Search over Propositions for Multi-hop Question Answering](https://arxiv.org/abs/2605.16598)

**<font color=#1a73e8>作者：</font>** Stockton Jenkins, Ramya Korlakai Vinayak, Junjie Hu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agentic retrieval improves multi-hop question answering by giving language models autonomy to iteratively gather evidence. Recent work augments these systems with knowledge graphs for structured traversal, but this combination introduces significant cost: expensive graph construction at index time and compounding token usage at inference time. We introduce Graph Agentic Search over Propositions (GRASP), an agentic system that simultaneously optimizes for high accuracy and minimal token usage in multi-hop question answering. Rather than executing a rigid, singular query, GRASP actively coordinates its retrieval strategy by decomposing multi-hop queries into dependency-aware plans. This enables GRASP to dynamically scale the number of sub-agents according to the complexity of the problem. Each sub-agent resolves its single-hop query by exploring a novel three-layer hierarchical graph of entities, propositions, and passages, using the entity layer for targeted traversal and the proposition layer for high-recall passage retrieval via reciprocal-rank voting. We evaluate GRASP on MuSiQue, 2WikiMultihopQA, and HotpotQA under two settings: open-corpus retrieval and extended context reasoning (LongBench). GRASP achieves the highest QA accuracy in the open retrieval setting on MuSiQue and 2Wiki while using 40-50 percent fewer tokens than IRCoT+HippoRAG2. Furthermore, GRASP leads on EM and F1 across all three datasets in the LongBench setting while using 30 percent fewer tokens than the next most accurate method. Finally, we introduce success economy - the amortized token cost per correct answer, weighted by difficulty - and advocate for efficiency-aware evaluation as a standard practice for agentic QA.

---


### 48. [Where Pretraining writes and Alignment reads: the asymmetry of Transformer weight space](https://arxiv.org/abs/2605.16600)

**<font color=#1a73e8>作者：</font>** Valeria Ruscio, Eli-Shaoul Khedouri, Keiran Thompson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-entropy pretraining and preference alignment update the same transformer weights, but leave geometrically distinct traces. We characterise this asymmetry with a relative-subspace-fraction probe that tracks how weight deltas align with residual-stream activation subspaces and with the prediction subspace defined by the unembedding. Alignment deltas concentrate in the read pathway ($W_Q$, $W_K$), along principal directions of attention-input activations, while remaining near-isotropic in the write pathway ($W_O$, $W_2$) relative to the prediction subspace. We explain this pattern through anisotropic gradient accumulation: updates to a matrix $W$ are sums of outer products $\delta_t a_t^\top$, and inherit directional structure from whichever side has concentrated covariance. For read-pathway matrices, this side is the input activation $a_t$, whose covariance is spiked in trained transformers and therefore produces objective-agnostic concentration. For write-pathway matrices, the relevant side is the upstream gradient $\delta_t$, whose anisotropy depends on the loss. Cross-entropy supplies the canonical sharp per-sample signal, inducing write-pathway prediction geometry during pretraining; alignment objectives typically add little further write-side concentration. We support this explanation with a within-checkpoint trajectory, a graded contrastive-objective control, and a closed-form rank-1 intervention with matched direction controls, providing causal evidence for the proposed weight-space geometry.

---


### 49. [Learning How to Cube](https://arxiv.org/abs/2605.16632)

**<font color=#1a73e8>作者：</font>** Ferhat Erata, Sam Kouteili, Thanos Typaldos 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the effectiveness of Cube-and-Conquer (C&C) for solving challenging Boolean Satisfiability (SAT) problems, no prior work has shown that transformer-based models can learn effective cubing heuristics. We introduce a neuro-symbolic post-training framework for this task. We design an MCTS-based data curation pipeline that uses symbolic heuristics to explore splitting decisions over SAT competition formulas, producing preference data grounded in solver statistics and augmented with reasoning traces from a teacher model. Our two-stage post-training, supervised fine-tuning (SFT) followed by direct preference optimization (DPO), enables a 4B-parameter model to achieve a pass@5 score of 53 on 100 SAT competition benchmarks, surpassing frontier LLMs such as Claude-Sonnet-4 (50) and matching the best symbolic heuristic (53). Ablations show that SFT alone improves pass@5 from 46 to 51, with DPO adding 2 additional benchmarks; an entropy/agreement ablation on realized first-cube decisions further shows that SFT, not DPO, accounts for the root-level decision diversity that produces complementary per-run coverage over deterministic symbolic methods. This demonstrates that transformers can be trained to make effective cubing decisions in a domain traditionally dominated by symbolic methods.

---


### 50. [TTE-Flash: Accelerating Reasoning-based Multimodal Representations via Think-Then-Embed Tokens](https://arxiv.org/abs/2605.16638)

**<font color=#1a73e8>作者：</font>** Jianpeng Cheng, Xian Wu, Jiangfan Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent research has demonstrated that Universal Multimodal Embedding (UME) benefits significantly from Chain-of-Thought (CoT) reasoning. In this paradigm, a generative model produces explicit reasoning traces for a multimodal query, with the final representation extracted from an <eos> embedding token attending to both the query and the reasoning. Despite its effectiveness, the computational overhead of generating explicit CoT traces is often prohibitive. In this work, we propose replacing explicit CoT with latent think tokens, which are interpreted as latent variables that can produce explicit CoT traces as observed variables. By optimizing think tokens using CoT generation loss and subsequent embedding tokens using contrastive loss, we produce high-performance, reasoning-aware representations at a constant inference cost. Our study investigates two key architectural designs: 1) how think and embeddings tokens should be extracted from the same LLM backbone. 2) how the tokens should be trained as two dependent tasks. We introduce TTE-Flash-2B, a reasoning-aware multimodal representation model that outperforms its explicit-CoT counterpart on the MMEB-v2 benchmark, while producing latent think tokens that are interpretable both textually and visually. Furthermore, zero-shot evaluation across 15 video datasets reveals scaling behavior as the number of think tokens increases, and motivating a pilot study of adaptive think budget allocation based on task requirements.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-346](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
