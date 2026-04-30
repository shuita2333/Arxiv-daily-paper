# 🧠 大模型相关研究 | 2026年05月01日

> 本类共 **75** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-75**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-75**

---

### 51. [Advancing multi-site emission control: A physics-informed transfer learning framework with mixture of experts for carbon-pollutant synergy](https://arxiv.org/abs/2604.26571)

**<font color=#1a73e8>作者：</font>** Yuxuan Ying, Hanqing Yang, Kaige Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Municipal solid waste incineration is increasingly central to urban waste management, yet its sustainability benefit depends on controlling carbon emissions and multiple air pollutants under highly heterogeneous operating conditions. Current data-driven models are often accurate within individual plants but are difficult to transfer across facilities, limiting their value for scalable emission-control strategies. Here we show that multi-site emission behaviour can be represented through transferable system-level structures when physical constraints, operating-regime heterogeneity and carbon--pollutant coupling are jointly considered. We develop a physics-informed transfer learning framework built on a carbon--pollutant mixture-of-experts model, which combines regime-dependent expert routing with conservation-based regularization and a carbon--pollutant synergistic index for integrated risk evaluation. Across 13 municipal solid waste incineration plants, the model captured both pollutant-specific emissions and system-level risk, achieving source-domain average pollutant $R^2$ values of 0.668--0.904 and CPSI $R^2$ values of 0.666--0.970. After transfer from a reference facility to 12 target plants, average pollutant $R^2$ remained between 0.661 and 0.842, while CPSI retained comparable transferability ($R^2$ = 0.610--0.841). Expert-utilization patterns further indicate that adaptation occurs through structured re-weighting of operating regimes rather than complete model re-learning. By extending the learned representation into an interpretable digital twin, this framework provides a route from emission prediction to regime-aware operational navigation, supporting scalable carbon--pollutant synergistic control across heterogeneous waste-to-energy systems.

---


### 52. [PAINT: Partial-Solution Adaptive Interpolated Training for Self-Distilled Reasoners](https://arxiv.org/abs/2604.26573)

**<font color=#1a73e8>作者：</font>** Zhiquan Tan, Yinrong Hong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Improving large language model (LLM) reasoning requires supervision that is both aligned with the model's own test-time states and informative at the token level. Reinforcement learning with verifiable rewards provides on-policy exploration but offers sparse, high-variance credit; supervised fine-tuning and distillation provide dense targets but often train on fixed trajectories or rely on stronger teachers. Recent privileged on-policy self-distillation explores a middle ground by scoring student rollouts with the same model under verified solution context. We revisit this setting through a contextual re-scoring lens: for reasoning, the important choices are not only whether privileged context is available, but how much of it should be revealed and where its distribution should shape the student. We propose PAINT (Partial-solution Adaptive INterpolated Training), which masks the verified solution according to rollout-reference overlap and applies a small energy-space interpolation on a sparse set of entropy-mismatch token positions. Across competition-level math benchmarks, PAINT consistently improves over a strong prior on-policy self-distillation baseline at all three Qwen3 scales. On Qwen3-8B, it raises macro Avg@12 by 2.1 points over this prior baseline and 2.9 points over GRPO.

---


### 53. [Benchmarking the Safety of Large Language Models for Robotic Health Attendant Control](https://arxiv.org/abs/2604.26577)

**<font color=#1a73e8>作者：</font>** Mahiro Nakao, Kazuhiro Takemoto  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly considered for deployment as the control component of robotic health attendants, yet their safety in this context remains poorly characterized. We introduce a dataset of 270 harmful instructions spanning nine prohibited behavior categories grounded in the American Medical Association Principles of Medical Ethics, and use it to evaluate 72 LLMs in a simulation environment based on the Robotic Health Attendant framework. The mean violation rate across all models was 54.4\%, with more than half exceeding 50\%, and violation rates varied substantially across behavior categories, with superficially plausible instructions such as device manipulation and emergency delay proving harder to refuse than overtly destructive ones. Model size and release date were the primary determinants of safety performance among open-weight models, and proprietary models were substantially safer than open-weight counterparts (median 23.7\% versus 72.8\%). Medical domain fine-tuning conferred no significant overall safety benefit, and a prompt-based defense strategy produced only a modest reduction in violation rates among the least safe models, leaving absolute violation rates at levels that would preclude safe clinical deployment. These findings demonstrate that safety evaluation must be treated as a first-class criterion in the development and deployment of LLMs for robotic health attendants.

---


### 54. [Translating Under Pressure: Domain-Aware LLMs for Crisis Communication](https://arxiv.org/abs/2604.26597)

**<font color=#1a73e8>作者：</font>** Antonio Castaldo, Maria Carmen Staiano, Johanna Monti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Timely and reliable multilingual communication is critical during natural and human-induced disasters, but developing effective solutions for crisis communication is limited by the scarcity of curated parallel data. We propose a domain-adaptive pipeline that expands a small reference corpus, by retrieving and filtering data from general corpora. We use the resulting dataset to fine-tune a small language model for crisis-domain translation and then apply preference optimization to bias outputs toward CEFR A2-level English. Automatic and human evaluation shows that this approach improves readability, while maintaining strong adequacy. Our results indicate that simplified English, combined with domain adaptation, can function as a practical lingua franca for emergency communication when full multilingual coverage is not feasible.

---


### 55. [Who Trains Matters: Federated Learning under Enrollment and Participation Selection Biases](https://arxiv.org/abs/2604.26604)

**<font color=#1a73e8>作者：</font>** Gota Morishita  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) trains a shared model from updates contributed by distributed clients, often implicitly assuming that contributing clients are representative of the target population. In practice, this representativeness assumption can fail at two distinct stages, inducing selection bias. First, eligibility rules such as device constraints, software requirements, or user consent determine which clients are ever enrolled and reachable for training, inducing \emph{enrollment bias}. Second, among enrolled clients, user and system factors such as battery state, network status, and local time determine which clients participate in each communication round, inducing \emph{participation bias}. Although existing work has largely addressed round-level participation bias, it has paid far less attention to population-level enrollment bias, which can induce a persistent mismatch between the training objective and the target-population objective. We formalize FL under a two-stage selection model and derive \textsc{FedIPW}, an inverse-probability-weighted aggregation scheme that recovers the target-population mean update under standard ignorability and positivity assumptions. Because client-level covariates are often unavailable for non-enrolled clients, we also introduce a limited-information aggregate-calibration extension that uses known target-population summaries to reweight the enrolled sample, partially correcting enrollment bias. We further provide an algorithm-agnostic optimization analysis under residual weighting error and show that incomplete selection correction can induce a non-vanishing bias floor. Finally, experiments on synthetic federated logistic regression validate the predicted objective mismatch and show that enrollment correction reduces target-population error under two-stage selection.

---


### 56. [Human-in-the-Loop Benchmarking of Heterogeneous LLMs for Automated Competency Assessment in Secondary Level Mathematics](https://arxiv.org/abs/2604.26607)

**<font color=#1a73e8>作者：</font>** Jatin Bhusal, Nancy Mahatha, Aayush Acharya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Competency-Based Education (CBE) is gaining traction around the world, the shift from marks-based assessment to qualitative competency mapping is a manual challenge for educators. This paper tackles the bottleneck issue by suggesting a "Human-in-the-Loop" benchmarking framework to assess the effectiveness of multiple LLMs in automating secondary-level mathematics assessment. Based on the Grade 10 Optional Mathematics curriculum in Nepal, we created a multi-dimensional rubric for four topics and four cross-cutting competencies: Comprehension, Knowledge, Operational Fluency, and Behavior and Correlation.
The multi-provider ensemble, consisted of open-weight models -- Eagle (Llama 3.1-8B) and Orion (Llama 3.3-70B) -- and proprietary frontier models Nova (Gemini 2.5 Flash) and Lyra (Gemini 3 Pro), was benchmarked against a ground truth defined by two senior mathematics faculty members (kappa_w = 0.8652). The findings show a marked "Architecture-compatibility gap". Although the Gemini-based Mixture-of-Experts (Sparse MoE) models achieved "Fair Agreement" (kappa_w ~ 0.38), the larger Orion (70B) model exhibited "No Agreement" (kappa_w = -0.0261), suggesting that architectural compliance with instruction constraints outweighs the scale of raw parameters in rubric-constrained tasks. We conclude that while LLMs are not yet suitable for autonomous certification, they provide high-value assistive support for preliminary evidence extraction within a "Human-in-the-Loop" framework.

---


### 57. [State Beyond Appearance: Diagnosing and Improving State Consistency in Dial-Based Measurement Reading](https://arxiv.org/abs/2604.26614)

**<font color=#1a73e8>作者：</font>** Yuanze Hu, Gen Li, Yuqin Lan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have achieved impressive progress on general multimodal tasks, yet they remain brittle on dial-based measurement reading. In this paper, we study this problem through controlled benchmarks and feature-space probing, and show that current MLLMs not only achieve unsatisfactory accuracy on dial-based readout, but also suffer sharp performance drops under viewpoint and illumination changes even when the underlying dial state remains fixed. Our probing analysis further reveals that same-state samples under appearance variation are not consistently clustered, while neighboring states fail to preserve the local structure implied by continuous dial values. These findings suggest that existing MLLMs largely ignore the intrinsic state geometry of dial measurement tasks and instead rely on superficial appearance cues. Motivated by this diagnosis, we propose TriSCA, a tri-level state-consistent alignment framework for dial-based measurement reading. Specifically, TriSCA consists of state-distance-aware representation alignment, metadata-grounded observation-to-state supervision, and state-aware objective alignment. Extensive ablation studies and evaluation experiments on controlled clock and gauge benchmarks, together with evaluation on an external real-world benchmark, demonstrate the effectiveness of our method.

---


### 58. [Zero-Shot to Full-Resource: Cross-lingual Transfer Strategies for Aspect-Based Sentiment Analysis](https://arxiv.org/abs/2604.26619)

**<font color=#1a73e8>作者：</font>** Jakob Fehle, Nils Constantin Hellwig, Udo Kruschwitz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aspect-based Sentiment Analysis (ABSA) extracts fine-grained opinions toward specific aspects within text but remains largely English-focused despite major advances in transformer-based and instruction-tuned models. This work presents a multilingual evaluation of state-of-the-art ABSA approaches across seven languages (English, German, French, Dutch, Russian, Spanish, and Czech) and four subtasks (ACD, ACSA, TASD, ASQP). We systematically compare different transformer architectures under zero-resource, data-only, and full-resource settings, using cross-lingual transfer, code-switching and machine translation. Fine-tuned Large Language Models (LLMs) achieve the highest overall scores, particularly in complex generative tasks, while few-shot counterparts approach this performance in simpler setups, where smaller encoder models also remain competitive. Cross-lingual training on multiple non-target languages yields the strongest transfer for fine-tuned LLMs, while smaller encoder or seq-to-seq models benefit most from code-switching, highlighting architecture-specific strategies for multilingual ABSA. We further contribute two new German datasets, an adapted GERestaurant and the first German ASQP dataset (GERest), to encourage multilingual ABSA research beyond English.

---


### 59. [SciHorizon-DataEVA: An Agentic System for AI-Readiness Evaluation of Heterogeneous Scientific Data](https://arxiv.org/abs/2604.26645)

**<font color=#1a73e8>作者：</font>** Dianyu Liu, Chuan Qin, Xi Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-for-Science (AI4Science) is increasingly transforming scientific discovery by embedding machine learning models into prediction, simulation, and hypothesis generation workflows across domains. However, the effectiveness of these models is fundamentally constrained by the AI-readiness of scientific data, for which no scalable and systematic evaluation mechanism currently exists. In this work, we propose SciHorizon-DataEVA, a novel agentic system to scalable AI-readiness evaluation of heterogeneous scientific data. At the evaluation-criteria level, we introduce the Sci-TQA2 principles, which organize AI-readiness into four complementary dimensions: Governance Trustworthiness, Data Quality, AI Compatibility, and Scientific Adaptability. Each dimension is decomposed into measurable atomic elements that enable fine-grained and executable assessment. To operationalize these principles at scale, we develop Sci-TQA2-Eval, a hierarchical multi-agent evaluation approach orchestrated through a directed, cyclic workflow. Our Sci-TQA2-Eval dynamically constructs dataset-aware evaluation specifications by combining lightweight dataset profiling, applicability-aware metric activation, and knowledge-augmented planning grounded in domain constraints and dataset-paper signals. These specifications are executed through an adaptive, tool-centric evaluation mechanism with built-in verification and self-correction, enabling scalable and reliable assessment across heterogeneous scientific data. Extensive experiments on scientific datasets spanning multiple domains demonstrate the effectiveness and generality of SciHorizon-DataEVA for principled AI-readiness evaluation.

---


### 60. [MultEval: Supporting Collaborative Alignment for LLM-as-a-Judge Evaluation Criteria](https://arxiv.org/abs/2604.26679)

**<font color=#1a73e8>作者：</font>** Charles Chiang, Simret Gebreegziabher, Annalisa Szymanski 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge approaches have emerged as a scalable solution for evaluating model behaviors, yet they rely on evaluation criteria often created by a single individual, embedding that person's assumptions, priorities, and interpretive lens. In practice, defining such criteria is a collaborative and contested process involving multiple stakeholders with different values, interpretations, and priorities; an aspect largely unsupported by existing tools. To examine this problem in depth, we present a formative study examining how stakeholders collaboratively create, negotiate, and refine evaluation criteria for LLM-as-a-judge systems. Our findings reveal challenges in human oversight, including difficulties in establishing shared understanding, aligning values across stakeholders with different expertise and priorities, and translating nuanced human judgments into criteria that are interpretable and actionable for LLM judges. Based on these insights, we developed MultEval, a system that supports collaborative criteria by enabling multiple evaluators to surface and diagnose disagreements using consensus-building theory, iteratively revise criteria with attached examples and proposal history, and maintain transparency over how judgments are encoded into an automated evaluator. We further report a case study in which a team of domain experts used MultEval to collaboratively author criteria, illustrating how coordination and collaborative consensus-making shape criteria evolution.

---


### 61. [Transferability of Token Usage Rights: A Design Space Analysis of Generative AI Services](https://arxiv.org/abs/2604.26683)

**<font color=#1a73e8>作者：</font>** Jaeyong Lee, Heeju Kang, Ahra Cho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the rapid spread of generative AI services, the token has gained value not only as a technical unit of language processing but also as an economic currency for accessing AI services. Major AI model providers have adopted token-based billing as their default service model, requiring users to purchase platform-bound, fixed token usage rights. However, the fixedness of these usage rights is grounded in the billing-policy decisions of service providers rather than in any technical necessity. This study defines the Transferability of token usage rights as a design property that allows users to flexibly reallocate purchased data resources free from the constraints of time, account, and service. Drawing on the Design Space Analysis framework of MacLean et al. (1991), we identify five design axes (Target, Direction, Unit, Control, Reversibility) and five concrete Transferability types (carry-over, co-management, transfer, conversion, and trade) by analyzing the billing policies and terms of service of four major LLM services (ChatGPT, Claude, Gemini, Grok). Our analysis reframes the token from a purely economic-technical primitive into a core element of user-centered system design that expands user choice and autonomy.

---


### 62. [FutureWorld: A Live Environment for Training Predictive Agents with Real-World Outcome Rewards](https://arxiv.org/abs/2604.26733)

**<font color=#1a73e8>作者：</font>** Zhixin Han, Yanzhi Zhang, Chuyang Wei 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Live future prediction refers to the task of making predictions about real-world events before they unfold. This task is increasingly studied using large language model-based agent systems, and it is important for building agents that can continually learn from real-world. Just as interactive environments have often driven progress in agents, advancing live future prediction naturally motivates viewing it as a learning environment. Prior works have explored future prediction from several different parts, but have generally not framed it as a unified learning environment. This task is appealing for learning because it can provide a large number of prediction questions grounded in diverse real-world events, while preventing answer leakage. To leverage the advantages of live future prediction, we present FutureWorld, a live agentic reinforcement learning environment that closes the training loop between prediction, outcome realization, and parameters update. In our environment, we take three open-source base models and train them for consecutive days. The results show that training is effective. Furthermore, we build a daily benchmark based on the environment and evaluate several frontier agents on it to establish performance baselines for current agent systems.

---


### 63. [GLM-5V-Turbo: Toward a Native Foundation Model for Multimodal Agents](https://arxiv.org/abs/2604.26752)

**<font color=#1a73e8>作者：</font>** GLM-V Team, Wenyi Hong, Xiaotao Gu 等 78 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present GLM-5V-Turbo, a step toward native foundation models for multimodal agents. As foundation models are increasingly deployed in real environments, agentic capability depends not only on language reasoning, but also on the ability to perceive, interpret, and act over heterogeneous contexts such as images, videos, webpages, documents, GUIs. GLM-5V-Turbo is built around this objective: multimodal perception is integrated as a core component of reasoning, planning, tool use, and execution, rather than as an auxiliary interface to a language model. This report summarizes the main improvements behind GLM-5V-Turbo across model design, multimodal training, reinforcement learning, toolchain expansion, and integration with agent frameworks. These developments lead to strong performance in multimodal coding, visual tool use, and framework-based agentic tasks, while preserving competitive text-only coding capability. More importantly, our development process offers practical insights for building multimodal agents, highlighting the central role of multimodal perception, hierarchical optimization, and reliable end-to-end verification.

---


### 64. [Domain-Adapted Small Language Models for Reliable Clinical Triage](https://arxiv.org/abs/2604.26766)

**<font color=#1a73e8>作者：</font>** Manar Aljohani, Brandon Ho, Kenneth McKinley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurate and consistent Emergency Severity Index (ESI) assignment remains a persistent challenge in emergency departments, where highly variable free-text triage documentation contributes to mistriage and workflow inefficiencies. This study evaluates whether open-source small language models (SLMs) can serve as reliable, privacy-preserving decision-support tools for clinical triage. We systematically compared multiple SLMs across diverse prompting pipelines and found that clinical vignettes, concise summaries of triage narratives, yielded the most accurate predictions. The SLM, Qwen2.5-7B, demonstrated the strongest balance of accuracy, stability, and computational efficiency. Through large-scale domain adaptation using expert-curated and silver-standard pediatric triage data, fine-tuned Qwen2.5-7B models substantially reduced discordance and clinically significant errors, outperforming all baseline SLMs and advanced proprietary large language models (LLMs, e.g., GPT-4o). These findings highlight the feasibility of institution-specific SLMs for reliable, privacy-preserving ESI decision support and underscore the importance of targeted fine-tuning over more complex inference strategies.

---


### 65. [TAP into the Patch Tokens: Leveraging Vision Foundation Model Features for AI-Generated Image Detection](https://arxiv.org/abs/2604.26772)

**<font color=#1a73e8>作者：</font>** Ahmed Abdullah, Nikolas Ebert, Oliver Wasenmüller  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent methods demonstrate that large-scale pretrained models, such as CLIP vision transformers, effectively detect AI-generated images (AIGIs) from unseen generative models when used as feature extractors. Many state-of-the-art methods for AI-generated image detection build upon the original CLIP-ViT to enhance this generalization. Since CLIP's release, numerous vision foundation models (VFMs) have emerged, incorporating architectural improvements and different training paradigms. Despite these advances, their potential for AIGI detection and AI image forensics remains largely unexplored. In this work, we present a comprehensive benchmark across multiple VFM families, covering diverse pretraining objectives, input resolutions, and model scales. We systematically evaluate their out-of-the-box performance for detecting fully-generated AI-images and AI-inpainted images, and discover that the best model outperforms the original CLIP by more than 12% in accuracy, beating established approaches in the process. To fully leverage the features of a modern VFM, we propose a simple redesign of the classifier head by utilizing tunable attention pooling (TAP), which aggregates output tokens into a refined global representation. Integrating TAP with the latest VFMs yields substantial performance gains across several AIGI detection benchmarks, establishing a new state-of-the-art on two challenging benchmarks for in-the-wild detection of AI-generated and -inpainted images.

---


### 66. [Accelerating RL Post-Training Rollouts via System-Integrated Speculative Decoding](https://arxiv.org/abs/2604.26779)

**<font color=#1a73e8>作者：</font>** Hayate Iso, Tiyasa Mitra, Sudipta Mondal 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RL post-training of frontier language models is increasingly bottlenecked by autoregressive rollout generation, making rollout acceleration a central systems challenge. Many existing efficiency methods improve throughput by changing the rollout or optimization regime, for example, through off-policy execution, replay, or lower-precision generation. We study speculative decoding as a lossless acceleration primitive for RL rollouts that preserves the target model's output distribution. We implement speculative decoding in NeMo-RL with a vLLM backend, supporting both synchronous and asynchronous pipelines and enabling speculation during RL rollouts. This benefit is realizable across speculation mechanisms, such as pretrained MTP heads, small external draft models or even techniques such as Eagle3, which are traditionally applied after RL phase. This yields a deployment path for state-of-the-art speculative decoding inside RL training. In a reasoning post-training workload at 8B scale under synchronous RL, speculative decoding improves rollout throughput by 1.8x. Using a high-fidelity performance simulator, we project that combining speculative decoding with asynchronous RL yields up to 2.5x end-to-end training speedup at 235B scale.

---


### 67. [MesonGS++: Post-training Compression of 3D Gaussian Splatting with Hyperparameter Searching](https://arxiv.org/abs/2604.26799)

**<font color=#1a73e8>作者：</font>** Shuzhao Xie, Junchen Ge, Weixiang Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) achieves high-quality novel view synthesis with real-time rendering, but its storage cost remains prohibitive for practical deployment. Existing post-training compression methods still rely on many coupled hyperparameters across pruning, transformation, quantization, and entropy coding, making it difficult to control the final compressed size and fully exploit the rate-distortion trade-off. We propose MesonGS++, a size-aware post-training codec for 3D Gaussian compression. On the codec side, MesonGS++ combines joint importance-based pruning, octree geometry coding, attribute transformation, selective vector quantization for higher-degree spherical harmonics, and group-wise mixed-precision quantization with entropy coding. On the configuration side, it treats the reserve ratio and bit-width allocation as the dominant rate-distortion knobs and jointly optimizes them under a target storage budget via discrete sampling and 0--1 integer linear programming. We further propose a linear size estimator and a CUDA parallel quantization operator to accelerate the hyperparameter searching process. Extensive experiments show that MesonGS++ achieves over 34$\times$ compression while preserving rendering fidelity, outperforming state-of-the-art post-training methods and accurately meeting target size budgets. Remarkably, without any training, MesonGS++ can even surpass the PSNR of vanilla 3DGS at a 20$\times$ compression rate on the Stump scene. Our code is available at this https URL

---


### 68. [Bian Que: An Agentic Framework with Flexible Skill Arrangement for Online System Operations](https://arxiv.org/abs/2604.26805)

**<font color=#1a73e8>作者：</font>** Bochao Liu, Zhipeng Qian, Yang Zhao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Operating and maintaining (O&M) large-scale online engine systems (search, recommendation, advertising) demands substantial human effort for release monitoring, alert response, and root cause analysis. While LLM-based agents are a natural fit for these tasks, the deployment bottleneck is not reasoning capability but orchestration: selecting, for each operational event, the relevant data (metrics, logs, change events) and the applicable operational knowledge (handbook rules and practitioner experience). Feeding all signals indiscriminately causes dilution and hallucination, while manually curating the event-to-(data, knowledge) mapping is intractable under dozens of daily releases. We present Bian Que, an agentic framework with three contributions: (i) a \emph{unified operational paradigm} abstracting day-to-day O&M into three canonical patterns: release interception, proactive inspection, and alert root cause analysis; (ii) \emph{Flexible Skill Arrangement}, where each Skill specifies which data and knowledge to retrieve for a given business-module context and can be automatically generated and updated by LLMs or iteratively refined through natural-language instructions from on-call engineers; (iii) a \emph{unified self-evolving mechanism} in which one correction signal drives two parallel pathways, case-memory-to-knowledge distillation and targeted Skill refinement. Deployed on the e-commerce search engine of KuaiShou, the major short-video platform in China, Bian Que reduces alert volume by 75%, achieves 80% root-cause analysis accuracy, and cuts mean time to resolution by over 50%. Our framework achieves 99.0% pass rate on offline evaluations. Our code is available at this https URL.

---


### 69. [Unifying Sparse Attention with Hierarchical Memory for Scalable Long-Context LLM Serving](https://arxiv.org/abs/2604.26837)

**<font color=#1a73e8>作者：</font>** Zihan Zhao, Baotong Lu, Shengjie Lin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context LLM serving is bottlenecked by the cost of attending over ever-growing KV caches. Dynamic sparse attention promises relief by accessing only a small, query-dependent subset of the KV state per decoding step and extending the KV storage to CPU memory. In practice, however, these algorithmic savings rarely translate into end-to-end system-level gains because sparse methods typically operate at different granularities and thus rely on ad hoc, per-algorithm implementations. At the same time, hierarchical KV storage introduces a new systems bottleneck: retrieving fine-grained, irregular KV subsets across the GPU-CPU boundary can easily erase the benefits of sparsity.
We present SPIN, a sparse-attention-aware inference framework that co-designs the execution pipeline with hierarchical KV storage through three techniques: (1) a unified partition abstraction that maps different sparsity granularities onto a shared page-based KV substrate; (2) a locality-aware KV cache manager that dynamically sizes per-request HBM budgets and uses a GPU-friendly bucketed LRU policy to cut PCIe round-trips; and (3) a two-level hierarchical metadata layout sized to the active working set rather than the worst-case address space. Built on vLLM with three representative sparse attention algorithms, SPIN delivers 1.66-5.66x higher end-to-end throughput and 7-9x lower TTFT than vLLM, and reduces TPOT by up to 58% over the original sparse-attention implementations.

---


### 70. [MoRFI: Monotonic Sparse Autoencoder Feature Identification](https://arxiv.org/abs/2604.26866)

**<font color=#1a73e8>作者：</font>** Dimitris Dimakopoulos, Shay B. Cohen, Ioannis Konstas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) acquire most of their factual knowledge during the pre-training stage, through next token prediction. Subsequent stages of post-training often introduce new facts outwith the parametric knowledge, giving rise to hallucinations. While it has been demonstrated that supervised fine-tuning (SFT) on new knowledge may exacerbate the problem, the underlying mechanisms are still poorly understood. We conduct a controlled fine-tuning experiment, focusing on closed-book QA, and find latent directions that causally contribute to hallucinations. Specifically, we fine-tune Llama 3.1 8B, Gemma 2 9B and Mistral 7B v03 on seven distinct single QA datasets, controlling for the percentage of new knowledge and number of training epochs. By measuring performance on the test set, we validate that incrementally introducing new knowledge increases hallucinations, with the effect being more pronounced with prolonged training. We leverage pre-trained sparse autoencoders (SAEs) to analyze residual stream activations across various checkpoints for each model and propose Monotonic Relationship Feature Identification (MoRFI) for capturing causally relevant latents. MoRFI filters SAE features that respond monotonically to controlled fine-tuning data mixtures of a target property. Our findings show that exposure to unknown facts disrupts the model's ability to retrieve stored knowledge along a set of directions in the residual stream. Our pipeline reliably discovers them across distinct models, recovering knowledge through single-latent interventions.

---


### 71. [HealthNLP_Retrievers at ArchEHR-QA 2026: Cascaded LLM Pipeline for Grounded Clinical Question Answering](https://arxiv.org/abs/2604.26880)

**<font color=#1a73e8>作者：</font>** Md Biplob Hosen, Md Alomgeer Hussein, Md Akmol Masud 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Patient portals now give individuals direct access to their electronic health records (EHRs), yet access alone does not ensure patients understand or act on the complex clinical information contained in these records. The ArchEHR-QA 2026 shared task addresses this challenge by focusing on grounded question answering over EHRs, and this paper presents the system developed by the HealthNLP_Retrievers team for this task. The proposed approach uses a multi-stage cascaded pipeline powered by the Gemini 2.5 Pro large language model to interpret patient-authored questions and retrieve relevant evidence from lengthy clinical notes. Our architecture comprises four integrated modules: (1) a few-shot query reformulation unit which summarizes verbose patient queries; (2) a heuristic-based evidence scorer which ranks clinical sentences to prioritize recall; (3) a grounded response generator which synthesizes professional-caliber answers restricted strictly to identified evidence; and (4) a high-precision many-to-many alignment framework which links generated answers to supporting clinical sentences. This cascaded approach achieved competitive results. Across the individual tracks, the system ranked 1st in question interpretation, 5th in answer generation, 7th in evidence identification, and 9th in answer-evidence alignment. These results show that integrating large language models within a structured multi-stage pipeline improves grounding, precision, and the professional quality of patient-oriented health communication. To support reproducibility, our source code is publicly available in our GitHub repository

---


### 72. [AnimateAnyMesh++: A Flexible 4D Foundation Model for High-Fidelity Text-Driven Mesh Animation](https://arxiv.org/abs/2604.26917)

**<font color=#1a73e8>作者：</font>** Zijie Wu, Chaohui Yu, Fan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 4D content generation have attracted increasing attention, yet creating high-quality animated 3D models remains challenging due to the complexity of modeling spatio-temporal distributions and the scarcity of 4D training data. We present AnimateAnyMesh++, a feed-forward framework for text-driven animation of arbitrary 3D meshes with substantial upgrades in data, architecture, and generative capability. First, we expand the DyMesh-XL dataset by mining dynamic content from Objaverse-XL, increasing the number of unique identities from 60K to 300K and substantially broadening category and motion diversity. Second, we redesign DyMeshVAE-Flex with power-law topology-aware attention and vertex-normal enhanced features, which significantly improves trajectory reconstruction, local geometry preservation, and mitigates trajectory-sticking artifacts. Third, we introduce architectural changes to both DyMeshVAE-Flex and the rectified-flow (RF) generator to support variable-length sequence training and generation, enabling longer animations while preserving reconstruction fidelity. Extensive experiments demonstrate that AnimateAnyMesh++ generates semantically accurate and temporally coherent mesh animations within seconds, surpassing prior approaches in quality and efficiency. The enlarged DyMesh-XL, the upgraded DyMeshVAE-Flex, and variable-length RF together deliver consistent gains across benchmarks and in-the-wild meshes. We will release code, models, and the expanded DyMesh-XL upon acceptance of this manuscript to facilitate research in 4D content creation.

---


### 73. [World2VLM: Distilling World Model Imagination into VLMs for Dynamic Spatial Reasoning](https://arxiv.org/abs/2604.26934)

**<font color=#1a73e8>作者：</font>** Wanyue Zhang, Wenxiang Wu, Wang Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have shown strong performance on static visual understanding, yet they still struggle with dynamic spatial reasoning that requires imagining how scenes evolve under egocentric motion. Recent efforts address this limitation either by scaling spatial supervision with synthetic data or by coupling VLMs with world models at inference time. However, the former often lacks explicit modeling of motion-conditioned state transitions, while the latter incurs substantial computational overhead. In this work, we propose World2VLM, a training framework that distills spatial imagination from a generative world model into a vision-language model. Given an initial observation and a parameterized camera trajectory, we use a view-consistent world model to synthesize geometrically aligned future views and derive structured supervision for both forward (action-to-outcome) and inverse (outcome-to-action) spatial reasoning. We post-train the VLM with a two-stage recipe on a compact dataset generated by this pipeline and evaluate it on multiple spatial reasoning benchmarks. World2VLM delivers consistent improvements over the base model across diverse benchmarks, including SAT-Real, SAT-Synthesized, VSI-Bench, and MindCube. It also outperforms the test-time world-model-coupled methods while eliminating the need for expensive inference-time generation. Our results suggest that world models can serve not only as inference-time tools, but also as effective training-time teachers, enabling VLMs to internalize spatial imagination in a scalable and efficient manner.

---


### 74. [Three-Step Nav: A Hierarchical Global-Local Planner for Zero-Shot Vision-and-Language Navigation](https://arxiv.org/abs/2604.26946)

**<font color=#1a73e8>作者：</font>** Wanrong Zheng, Yunhao Ge, Laurent Itti  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breakthrough progress in vision-based navigation through unknown environments has been achieved by using multimodal large language models (MLLMs). These models can plan a sequence of motions by evaluating the current view at each time step against the task and goal given to the agent. However, current zero-shot Vision-and-Language Navigation (VLN) agents powered by MLLMs still tend to drift off course, halt prematurely, and achieve low overall success rates. We propose Three-Step Nav to counteract these failures with a three-view protocol: First, "look forward" to extract global landmarks and sketch a coarse plan. Then, "look now" to align the current visual observation with the next sub-goal for fine-grained guidance. Finally, "look backward" audits the entire trajectory to correct accumulated drift before stopping. Requiring no gradient updates or task-specific fine-tuning, our planner drops into existing VLN pipelines with minimal overhead. Three-Step Nav achieves state-of-the-art zero-shot performance on the R2R-CE and RxR-CE dataset. Our code is available at this https URL.

---


### 75. [Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models](https://arxiv.org/abs/2604.26951)

**<font color=#1a73e8>作者：</font>** Gongbo Zhang, Wen Wang, Ye Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) offer parallel decoding and bidirectional context, but state-of-the-art dLLMs require billions of parameters for competitive performance. While existing distillation methods for dLLMs reduce inference steps within a single architecture, none address cross-architecture knowledge transfer, in which the teacher and student differ in architecture, attention mechanism, and tokenizer. We present TIDE, the first framework for cross-architecture dLLM distillation, comprising three modular components: (1) TIDAL, which jointly modulates distillation strength across training progress and diffusion timestep to account for the teacher's noise-dependent reliability; (2) CompDemo, which enriches the teacher's context via complementary mask splitting to improve predictions under heavy masking; and (3) Reverse CALM, a cross-tokenizer objective that inverts chunk-level likelihood matching, yielding bounded gradients and dual-end noise filtering. Distilling 8B dense and 16B MoE teachers into a 0.6B student via two heterogeneous pipelines outperforms the baseline by an average of 1.53 points across eight benchmarks, yielding notable gains in code generation, where HumanEval scores reach 48.78 compared to 32.3 for the AR baseline.

---


> [!TIP]
> 当前位于：**51-75**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-75**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
