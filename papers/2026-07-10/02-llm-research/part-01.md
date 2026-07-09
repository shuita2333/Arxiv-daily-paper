# 🧠 大模型相关研究 | 2026年07月10日

> 本类共 **84** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-84](./part-02.md)

---

### 1. [Inertia-1: An Open Exploration of Wearable Motion Foundation Models](https://arxiv.org/abs/2607.06617)

**<font color=#1a73e8>作者：</font>** Zongzhe Xu, Aakarsh Anand, Sarah Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable motion sensing provides a continuous and scalable window into human behavior and health, making it a natural fit for foundation models, yet its pretraining and scaling principles remain poorly understood. Prior work studies isolated design choices, such as sensor placement or sampling frequency, often under fixed settings and narrow downstream tasks that fail to capture real-world sensing diversity. We introduce Inertia-1, a fully open exploration of wearable motion foundation models. Using massive corpora of accelerometer data from global sources spanning more than 18.2M hours, we build a controlled framework for studying the full lifecycle of wearable motion foundation models, covering data choices such as sensor modality, device placement, sampling rate, window length; model choices such as architectures and model size; and training choices such as pretraining objective and data scale. Extensive evaluations across 15 datasets spanning human activity recognition, freezing-of-gait detection, and disease prediction reveal intriguing findings for building motion foundation models that generalize across tasks and sensing conditions. Collectively, Inertia-1 not only presents state-of-the-art recipes for diverse downstream tasks, but also serves as a comprehensive, practical, and open cookbook for wearable motion representation learning.

---


### 2. [Overview of the NLPCC 2026 Shared Task 1: Difficulty-Aware Multilingual and Multimodal Medical Instructional Video Understanding Evaluation](https://arxiv.org/abs/2607.06618)

**<font color=#1a73e8>作者：</font>** Shenxi Liu, Kan Li, Mingyang Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Following the CMIVQA, MMI-VQA, and M4IVQA challenges in NLPCC 2023--2025, we introduce the Difficulty-Aware Medical Instructional Video Question Answering (DA-MIVQA) shared task for NLPCC 2026. DA-MIVQA extends previous multilingual and multimodal medical video benchmarks by explicitly distinguishing questions according to the type and complexity of evidence required for answering. Specifically, simple questions can often be answered from subtitle-based textual cues, whereas complex questions require visual grounding, procedural understanding, and cross-modal evidence integration. The challenge contains three tracks: Difficulty-Aware Temporal Answer Grounding in Single Video (DA-TAGSV), Difficulty-Aware Video Corpus Retrieval (DA-VCR), and Difficulty-Aware Temporal Answer Grounding in Video Corpus (DA-TAGVC). The dataset is collected from public medical instructional channels, covers diverse scenarios such as first aid, emergency response, rehabilitation, nursing, and general medical education, and is manually verified with difficulty annotations. This paper presents the task motivation, dataset construction, evaluation protocol, participation overview, competition results, and representative systems of DA-MIVQA. DA-MIVQA provides a practical benchmark for evaluating medical instructional video question answering systems under varying textual, visual, temporal, and procedural reasoning requirements.

---


### 3. [SpaR3D-MoE: Adaptive 3D Spatial Reasoning from Sparse Views Meets Geometry-Inductive Mixture-of-Experts](https://arxiv.org/abs/2607.06620)

**<font color=#1a73e8>作者：</font>** Haida Feng, Hao Wei, Haolin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Multimodal Large Language Models (MLLMs) struggle to bridge the representational gap between 2D semantic understanding and 3D spatial geometry. Existing 3D-aware models either rely on costly 3D-specific data or utilize RGB-only inputs with heuristic sampling and monolithic, shallow fusion, which respectively disrupt essential spatiotemporal connectivity and induce modality contention across diverse spatial tasks. To overcome these bottlenecks, we introduce SpaR3D-MoE, an end-to-end framework that enables adaptive spatial reasoning by equipping MLLMs with geometry-aware capabilities from only sparse RGB inputs. First, we propose an adaptive spatiotemporal manifold sampling mechanism that constructs a geometry-aware spatiotemporal graph to extract informative keyframes, effectively mitigating sequence redundancy while preserving the scene's topological connectivity. Second, we introduce the heterogeneous geometry-inductive Mixture-of-Experts driven by an instruction-pose aware router, which adaptively routes multimodal tokens to specialized experts, resolving the cross-modal contention inherent in monolithic fusion. Extensive experiments on VSI-Bench, ScanQA, and SQA3D demonstrate that our method achieves state-of-the-art performance. Notably, SpaR3D-MoE achieves the highest average score of 63.5 on VSI-Bench, outperforming the strongest baseline by 7.8 absolute points, alongside relative improvements of 35.4% and 51.4% in Route Plan and Relative Direction tasks, respectively.

---


### 4. [LLM-Guided Task-Semantic Field Factorization for Industrial Process Forecasting](https://arxiv.org/abs/2607.06623)

**<font color=#1a73e8>作者：</font>** Youcheng Zong, Runda Jia, Mingxuan Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Process industries rely on time-series forecasting and soft sensing to estimate quality variables that are hard to measure online. Labeled data are scarce, operating regimes change frequently, and retraining models or rebuilding alignment pipelines for each scenario is costly. Such settings often provide variable tables and process documents that record variable names, units, physical meanings, and process roles. However, standard time-series backbones usually treat inputs as anonymous numerical columns. Existing text-enhanced methods also rarely make the semantic-logical relations between input variables and the prediction target available to the model within each numerical window. To address this problem, this article proposes Task-Semantic Field Factorization (TSF), a large language model (LLM)-guided framework. TSF builds a task-semantic field from task protocols and variable documents before training and uses the LLM only for offline semantic construction. Online training and inference remain with conventional time-series backbones. During training and inference, the current numerical window activates variable semantics, so semantic information participates in each prediction and supports adaptation to different prediction targets and operating shifts. On multiple complex industrial forecasting and soft-sensing tasks, TSF reduces MAE by 6.4\% on average in improved settings, with the largest reduction reaching 25.5\%. It adds only about 1.8--3.0k parameters, with less than 0.008 ms/step of additional online inference overhead. These results show that TSF turns existing process documents into measurable forecasting gains across backbones and semantic generators while remaining lightweight for deployment.

---


### 5. [Reward Valuation in Vision Language Models: Causal Mechanisms Underlying Anhedonia](https://arxiv.org/abs/2607.06626)

**<font color=#1a73e8>作者：</font>** Melika Honarmand, Samin Mahdipour Aghabagher, Martin Schrimpf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent Vision-Language Models capture increasingly complex aspects of human cognition. Here we ask whether this alignment extends to reward valuation, which we assess in a mechanistic framework built on clinical tests that were developed to evaluate anhedonia and motivational deficits in major depressive disorder. In the brain, anhedonia is frequently linked to dysregulation in the Nucleus Accumbens (NAc) and the broader dopaminergic reward system. While neuroimaging has localized these deficits, establishing a causal link between NAc activity and specific behavioral symptoms remains a challenge. We use these ideas from neuroscience to functionally identify reward-anticipatory units in vision language models, and test their causal role via targeted perturbations. Perturbing NAc-selective units induces behavioral effects that mirror human anhedonia: the model shifts toward low-effort, low-reward options in effort-based decision-making tasks. Crucially, our results reflect a specific deficit in reward valuation and anticipation rather than a loss of task capability: the perturbed model maintains baseline performance when reward-based choice is removed. This induced vulnerability further aligns with clinical anhedonia and motivation scales, including DARS and MAP-SR. Taken together, these results reveal reward valuation circuits in AI models that parallel those in humans.

---


### 6. [ProMoE-FL: Prototype-conditioned Mixture of Experts for Multimodal Federated Learning with Missing Modalities](https://arxiv.org/abs/2607.06633)

**<font color=#1a73e8>作者：</font>** Aavash Chhetri, Bibek Niroula, Eduard Vazquez 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we address the problem of multimodal federated learning with missing modality. Existing methods utilize an additional public dataset or perform naive feature synthesis that is based solely on the available modality. To address these limitations, we propose ProMoE-FL, a Prototype-conditioned Mixture-of-Experts framework for robust missing-modality feature synthesis in multimodal federated learning. ProMoE-FL builds a global client-aware prototype bank that captures clinically meaningful modality priors across institutions. Our Mixture of Experts is conditioned on these prototypes and modality indices to enable direction-aware expert routing for dynamically synthesizing missing features. We perform extensive quantitative and qualitative evaluations on four public chest X-ray datasets (MIMIC-CXR, NIH Open-I, PadChest, and CheXpert) and demonstrate that ProMoE-FL consistently outperforms state-of-the-art methods in both homogeneous as well as the more challenging heterogeneous settings.

---


### 7. [The Rank-One Corner: How Much Value Equivalence Does a Task Need from a World Model?](https://arxiv.org/abs/2607.06640)

**<font color=#1a73e8>作者：</font>** Donna Vakalis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A learned world model is usually judged by how faithfully it reconstructs its observations or predicts reward, as though quality were something the model simply has or lacks. But what a task actually needs from a model is narrower: the few predictive coordinates its queries depend on, which we call the closure. We show that how much of that closure a latent comes to represent is set not by the model's capacity or its observations but by the dimensionality of the objective it is trained against, and we measure this directly on a DreamerV3 stack in a controlled environment with known ground-truth closure. An aligned scalar value signal -- the objective at the heart of value equivalence -- installs only a one-dimensional projection of a closure that needs several dimensions: read through a single linear probe, the recoverable structure rises from R^2=0.10 to 0.76 as the scalar is replaced by the full objective. Sweeping the objective's dimensionality from one to four installs exactly that many predictive directions through an auxiliary head, and the same staircase appears -- at attenuated magnitude but the same rank -- through the model's own value head, so the dissociation is dimensional rather than an artifact of head form. Capacity-matched comparisons and in-situ pressure checks rule out the obvious alternatives. The law governs a regime, and we measure its boundary: on a companion closed-loop task whose structure is observable frame by frame, reconstruction installs that structure and the scalar objective suffices -- the objective decides what a latent represents exactly where cheaper training signals cannot already recover it. Value equivalence is thus not all-or-nothing but dimensional: the familiar single-reward objective is its rank-one corner, and a model installs as much of a task's structure as the objective it is asked to predict.

---


### 8. [Healthier LLMs: Retrieval-Augmented Generation for Public Health Question Answering](https://arxiv.org/abs/2607.06641)

**<font color=#1a73e8>作者：</font>** Felix Feldman, Joshua Harris, Timothy Laurence 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve promising results on medical question answering benchmarks, yet their use in public health is constrained by hallucinations and the rapid evolution of official guidance. Retrieval-Augmented Generation (RAG) mitigates these risks by grounding responses in an explicitly maintained corpus, but end-to-end performance depends critically on retrieval configuration and on evaluation beyond multiple-choice formats. We extend PubHealthBench, a question answering (QA) benchmark of 7,929 questions derived from UK Government public health guidance, into a retrieval-augmented setting and systematically evaluate retrieval and generation choices. We compare dense, sparse, and hybrid retrieval across multiple embedding models and corpus variants, and show that hybrid retrieval consistently improves recall and ranking quality, with chunk length and topic interacting with ranking performance. Providing retrieved context substantially increases multiple-choice accuracy across a diverse set of LLMs, enabling smaller open-weight models to match or outperform larger models used without retrieval, with gains primarily driven by retrieval quality and careful context selection. To assess realistic free-form answering, we introduce a rubric-based LLM-as-a-judge covering faithfulness, completeness, clarity, and factual consistency, and validate it against dual human annotations. Judge-human agreement is strongest for faithfulness and completeness, while factual consistency and clarity are less reliably reproduced, motivating caution when interpreting those dimensions at scale. Overall, our results highlight retrieval as a primary lever for reliable public health QA and provide practical guidance for building and evaluating RAG systems grounded in official guidance.

---


### 9. [Entropy-Guided Tensor Compression for Multimodal Federated Learning on Edge Devices](https://arxiv.org/abs/2607.06651)

**<font color=#1a73e8>作者：</font>** Quoc Bao Phan, Tuy Tan Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) over mobile and edge devices increasingly involves multimodal models in which clients differ in both sensing capability and computational capacity. Existing update compression schemes typically apply uniform policies across layers and devices, without accounting for modality-specific differences in spectral structure and compressibility. We propose MESH-FL, an entropy-guided matrix product state (MPS) update-compression framework for modality-heterogeneous FL on resource-constrained devices. MESH-FL estimates the spectral entropy of each layer-wise update via truncated singular value decomposition and allocates MPS compression ranks adaptively across layers, modalities, and devices under per-client payload budgets. We show that higher spectral entropy necessitates a higher reconstruction rank under the majorization order on singular-value energy distributions. Building on this result, we prove that the proposed entropy-guided allocation solves a convex surrogate rank-allocation problem, preserves monotonicity under the exact payload model, and achieves convergence with an explicit compression-dependent error term. Experiments on a 15-node heterogeneous Raspberry Pi~4/5 cluster with modality-heterogeneous clients show that MESH-FL achieves up to $56.8\times$ compression while surpassing the uncompressed FedAvg baseline in final accuracy by up to 2.01%, and reduces total transmitted data to reach convergence by up to $66\times$.

---


### 10. [Digital Fragmentation and Generative AI Use Across 103 Million Application Events](https://arxiv.org/abs/2607.06681)

**<font color=#1a73e8>作者：</font>** Sumer S. Vaid, Ashley V. Whillans  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Knowledge workers switch between applications thousands of times per day, spending nearly a tenth of the work year transitioning between digital applications in a process called digital fragmentation. Whether this fragmentation reflects who an employee is, where they work, or what kind of day they are having, has remained an open question. We analyzed 103 million application events recorded second-by-second from 1,017 employees across eight organizations that largely employ knowledge workers (e.g., law, financial services). Day-to-day variation in fragmentation within individual employees accounted for 44.6% of the variation in digital fragmentation, slightly exceeding stable individual differences between employees (35.8%), and far exceeding variation between organizations (19.6%). Fragmentation rose over the work week and reset after weekends and holidays. Higher-than-typical use of communication applications coincided with more fragmented work. Generative AI use also occurred on more fragmented days, but the period following AI use was marked by narrower, longer, and more predictable application use. These findings identify the workday as a key level for understanding and intervening on digital fragmentation and suggest that AI may help structure fragmented work rather than merely intensify it.

---


### 11. [When Does In-Context Search Help? A Sampling-Complexity Theory of Reflection-Driven Reasoning](https://arxiv.org/abs/2607.06720)

**<font color=#1a73e8>作者：</font>** Yotam Wolf, Noam Wies, Amnon Shashua  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training large language models (LLMs) with extended reasoning has enabled in-context search, in which models iteratively generate, critique, and revise solution attempts. We provide a theoretical analysis of in-context search by modeling it as approximate inference over reasoning traces, where the base model defines a prior and self-reflection provides feedback for posterior updates, and study the resulting inference-time sampling complexity - the number of sequential attempts needed to achieve high success probability. We show that when reflections reliably localize early mistakes, in-context search can yield exponential improvements over the base model, solving problems with exponentially small zero-shot pass rates using only a polynomial number of sequential attempts, whereas when this property fails, conditioning on past attempts offers no asymptotic benefit over parallel sampling. We further show that these gains are robust and learnable: approximate posterior updates suffice, and cross-entropy training on search rollouts recovers the required behavior with polynomial sample complexity. Finally, we show that under a stagewise abstraction of reinforcement learning with verifiable rewards, the optimal policy extension implements the same posterior reweighting rule. We validate key qualitative predictions of the theory on real large reasoning models.

---


### 12. [LLM-powered reasoning in agent-based modeling](https://arxiv.org/abs/2607.06757)

**<font color=#1a73e8>作者：</font>** Sifat Afroj Moon, Dakotah Maguire, Adam Spannaus 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent-based modeling (ABM) has the capability to model millions of individuals and their interactions, which is useful for policy making. However, ABMs have traditionally relied on static prior, which prevents the models from adapting to real-time changes. Our research provides a novel approach to addressing this information gap. Large language models (LLMs) offer new opportunities to predict human decision-making. Here, we introduce a scalable Hybrid Agent-based and Language-driven Epidemic (HALE) modeling framework that leverages LLMs to predict human decision-making in an ABM simulation. As a proof-of-concept, we use HALE to simulate COVID-19 and its effects in Salt Lake County, UT.

---


### 13. [What Predicts Correctness in Text-to-SQL? A Selective-Prediction Study](https://arxiv.org/abs/2607.06799)

**<font color=#1a73e8>作者：</font>** Robert Richardson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating uncertainty in AI-generated SQL queries requires estimating whether a query is correct, where correct means it executes to the same result as a human-written reference. We study which signals predict correctness on hard multi-table text-to-SQL, using AUROC to measure how well each ranks correct queries above incorrect ones. On BIRD and Spider, black-box signals such as string, structural, and execution self-consistency, a schema-relevance score, and query executability all fall between about 0.61 and 0.68 AUROC, with string self-consistency strongest at 0.675; white-box log-probability is similar (0.67). The signals that move past this ceiling are verification-based: an LLM judge scores from 0.72 (GPT-4o-mini) to 0.78 (Claude). Judges from different providers make different errors, so a two-provider ensemble reaches 0.82 AUROC with a well-calibrated probability (expected calibration error 0.03) and supports useful abstention frontiers (for example, answering 27% of questions at 24% selective risk) where self-consistency offers no valid low-risk subset. The pattern holds across two benchmarks, two generators, and two judge providers. We also ask whether a verifier can be trained. Fine-tuned verifiers, both encoder and generative, reach about 0.77 to 0.79 AUROC in-distribution but fall to about 0.66 on unseen schemas; scaling to 7B, adding schema diversity, distilling a strong judge's rationales, and cross-benchmark training all fail to close that gap. Cross-schema transfer appears to track model scale and reasoning rather than fine-tuning. In practice, correctness uncertainty for text-to-SQL lives in reasoning-based signals: a fine-tuned verifier is a good in-domain tool, but a verifier that generalizes across schemas currently means a large frozen reasoning model.

---


### 14. [Ad Headline Generation using Self-Critical Masked Language Model](https://arxiv.org/abs/2607.06818)

**<font color=#1a73e8>作者：</font>** Yashal Shakti Kanungo, Sumit Negi, Aruna Rajan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For any E-commerce website it is a nontrivial problem to build enduring advertisements that attract shoppers. It is hard to pass the creative quality bar of the website, especially at a large scale. We thus propose a programmatic solution to generate product advertising headlines using retail content. We propose a state of the art application of Reinforcement Learning (RL) Policy gradient methods on Transformer based Masked Language Models. Our method creates the advertising headline by jointly conditioning on multiple products that a seller wishes to advertise. We demonstrate that our method outperforms existing Transformer and LSTM + RL methods in overlap metrics and quality audits. We also show that our model-generated headlines outperform human submitted headlines in terms of both grammar and creative quality as determined by audits.

---


### 15. [Evaluating SageMath-Augmented LLM Agents for Computational and Experimental Mathematics](https://arxiv.org/abs/2607.06820)

**<font color=#1a73e8>作者：</font>** Pavel Snopov, German Magai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in AI for Mathematics have focused largely on autoformalization and theorem proving, leaving the role of Computer Algebra Systems (CAS) in agentic LLM workflows underexplored. We propose a ReAct-style agentic setup that combines LLM reasoning with verifiable feedback from SageMath, together with Context7 for the up-to-date documentation. We evaluate this agentic setup across frontier models for solving research-level mathematical problems from the RealMath benchmark in a setting that emulates a computational-mathematics research loop. We also propose a refinement to the RealMath benchmark by introducing a multi-step post-processing procedure and a multi-stage validation pipeline, both of which improve the quality and reliability of the extracted problem set. Our experiments reveal substantial performance gains from SageMath access across all evaluated models on +9.7~pp on average, the gains range from 1.5~pp to 27.8~pp and narrow the gap between open-weight and closed models. Qwen~3.7-Max benefits from SageMath the most, while GPT-5.5 achieves the highest solve rate of $75.2\%$ and the lowest token usage among tool-enabled configurations. Our findings suggest that CAS-augmented agents represent a promising direction for assisting mathematicians in computational exploration, and we believe that this work is a step towards automated conjecture discovery. The project repository is available online.

---


### 16. [Gradient-Based Speech-to-Text Alignment for Any ASR Model: From CTC to Speech LLMs](https://arxiv.org/abs/2607.06831)

**<font color=#1a73e8>作者：</font>** Albert Zeyer, Ralf Schlüter, Hermann Ney  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-to-text alignment means finding the temporal boundaries of each word in the audio. Some models provide such an alignment directly and others do not. Connectionist temporal classification (CTC) and transducer models have an alignment by construction, whereas attention-based encoder-decoders (AED) and speech large language models (LLMs) do not, and their word timings are usually read off the attention weights instead. All of these signals live on the encoder frame grid, which bounds their temporal precision. We study a generic gradient-based alignment that applies to any differentiable ASR model. We take the gradient of each teacher-forced token log probability with respect to the input, reduce it to a per-frame saliency, and decode the resulting matrix into word boundaries with a single dynamic-programming pass. The method needs no training, no model modification and no alignment heads, works across all model families including the speech LLMs, and aligns on the input grid rather than on the coarser encoder grid. We evaluate it on sixteen models from four families, on read (TIMIT) and spontaneous (Buckeye) speech, each against the model's own native or attention-based alignment. We find that the gradient yields a usable alignment for every model, that it is usually somewhat behind a strong native aligner but better where the native alignment is weak, as for the streaming models, and that its main disadvantage is the cost of one backward pass per token.

---


### 17. [LEMUR 2: Unlocking Neural Network Diversity for AI](https://arxiv.org/abs/2607.06839)

**<font color=#1a73e8>作者：</font>** Tolgay Atinc Uzun, Waleed Khalid, Saif U Din 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing NAS benchmarks (e.g., NAS-Bench, NATS-Bench) cover only narrow, task-specific regions of the architectural design space and lack cross-domain or deployment-aware evaluation. LEMUR 2 introduces a large-scale, extensible framework unifying generative, evaluative, and deployment pipelines to unlock neural-network diversity. It comprises over 14,000 distinct architectures and more than 750,000 structured training records documenting model performance, hyperparameters, and task outcomes. These models were produced through AST-based code mutation, genetic and reinforcement-learning evolution, generation of fractal architectures, and synthesis guided by a Large Language Model (LLM). This includes deep models generated with the retrieval-augmented system NN-RAG, which derived and used architectural motifs from over 900 PyTorch modules extracted from public repositories. LEMUR 2 further employs NN-VR and NN-Lite pipelines for automated deployment and latency benchmarking on heterogeneous mobile and Unity-based VR platforms, providing real-device performance metadata. It spans multimodal tasks, image captioning, text-to-image synthesis, and language modeling, supporting cross-domain analysis of architectural transferability. By linking diverse architectures, tasks, and deployment data, LEMUR 2 provides the data foundation for LLM fine-tuning and coupling diverse architectural origins with large-scale, cross-platform empirical validation. This dataset defines a new basis for reproducible and data-driven AI design, advancing the emerging paradigm of LLM-driven AutoML and architectural generalization across modalities and hardware.

---


### 18. [LLMs Silently Correct African American English: Auditing and Mitigating Dialect Bias via Activation Steering](https://arxiv.org/abs/2607.06845)

**<font color=#1a73e8>作者：</font>** Huan Wu, Ali Emami, Muhammad Furquan Hassan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> African American English (AAE), a rule-governed dialect spoken by over 30 million people, is routinely misinterpreted and "corrected" by large language models (LLMs). Across six instruction-tuned LLMs (14B to 70B), we show that state-of-the-art models systematically prefer Standard American English (SAE) continuations even when the preceding context is in AAE, effectively rewriting AAE into SAE. We present an end-to-end framework to audit and mitigate this bias. For auditing, we introduce conditional Dialect Group Invariance (cDGI), which isolates true model bias from translator-induced artifacts, and a feature-level localization analysis that identifies which AAE markers most strongly trigger bias; we find that syntactic constructions, especially negative concord (e.g., "ain't nobody"), are universal triggers across all models. For mitigation, we introduce, to our knowledge, the first application of activation steering to dialect bias: a training-free, test-time method that extracts dialect directions via causal tracing and injects them into bias-relevant layers. Activation steering reduces bias 5 to 20 times more than prompting while preserving SAE fluency. To enable this work, we release REAL-AAE , the largest real-AAE parallel corpus to date: 17,479 AAE/SAE/ AAE_back triplets from natural tweets (2 to 6 times larger than prior real-AAE resources), validated automatically (BERTScore F1 = 0.95) and by three native AAE speakers (83.0% semantic agreement).

---


### 19. [Geometric Self-Distillation for Reasoning Generalization](https://arxiv.org/abs/2607.06855)

**<font color=#1a73e8>作者：</font>** Josip Jukić, Ivan Titov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation is a practical post-training recipe for large language models, supplying dense teacher supervision on the student's own trajectories. In privileged-context self-distillation, teacher and student are the same model conditioned on the same prefix, but the teacher also sees a hint or the full solution trace. This makes supervision abundant but harder to trust: the teacher can be confident about continuations its privileged view makes obvious but the student cannot yet justify. The distillation pull is strongest where teacher and student disagree most, and over many updates it accumulates into drift that degrades out-of-distribution (OOD) reasoning. We introduce GeoSD, a geometric self-distillation objective that treats this drift as movement in the student's predictive behavior and counters it in two complementary ways. A Hellinger loss scales each teacher preference by the overlap the student already shares with it, attenuating the pull on tokens the student cannot yet support. Since these pulls still compound over training, a proximal term penalizes how far the student's predictions drift from a recent checkpoint, measured as a Fisher-Rao distance. Both are distances in the same geometry of next-token distributions, and a natural-gradient update takes its steps in that geometry rather than in parameter space. Across mathematical reasoning benchmarks and three model families, GeoSD preserves the in-distribution gains of self-distillation while improving average OOD accuracy by 5.7-8.6 points over the base model, with gains holding across model scales from 1.7B to 32B. Analyzing why standard matching fails out of distribution, we find it wins agreement with the teacher by draining mass from alternatives at high-entropy states, resulting in confident agreement on wrong answers, whereas GeoSD keeps those alternatives in reach.

---


### 20. [The Harness Effect: How Orchestration Design Sets the Token Economics of Enterprise Agentic AI](https://arxiv.org/abs/2607.06906)

**<font color=#1a73e8>作者：</font>** Muayad Sayed Ali, Aliaksandra Novik, Anji Boddupally 等 32 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI development today runs on token maxing: buying capability with tokens -- longer reasoning traces, more turns, wider tool payloads, bigger replayed contexts -- so tokens per task grow faster than task value. Falling per-token prices mask the pattern; total spend rises anyway. We argue the decisive lever against token maxing is the harness: the orchestration layer that assembles context, exposes tools, sequences turns, delegates work, and carries enterprise observability and governance. We isolate it with a controlled swap: 22 locked evaluation tasks, six foundation models (Claude Sonnet 4.6, Gemini 3.1, Gemini Flash 3.5, Qwen 3.6, GLM 5.1, Palmyra X6), changing only the orchestration layer -- a frozen conventional production loop versus the Writer Agent Harness. Holding models constant, the harness cuts blended cost per task 41% ($0.21->$0.12), median wall-clock 44% (48s->27s), and tokens per task 38% (14.2k->8.8k), with task-completion quality at parity (0.78->0.81, directional at this sample size). Efficiency is model-invariant -- every model gets cheaper (33-61%) -- while quality gains are capability-dependent: a model's gain correlates almost perfectly with its baseline strength (r=0.99, n=6), a phenomenon we term harness leverage. Quality per dollar rises 82%; task-completions per million tokens rise from 54.9 to 92.0. On this workload the orchestration layer moved cost per task more than the full spread of the model menu did. We formalize token economics at the orchestration layer (including effective input price under prompt caching), detail the six mechanism families behind the effect -- cache-shape discipline to failure-spend governance -- compare six widely used agent systems on the same axes, and argue the harness is the one component whose efficiency multiplies across every model an organization runs -- present and future.

---


### 21. [LoCA: Spatially-Aware Low-Rank Convolutional Adaptation of Vision Foundation Models](https://arxiv.org/abs/2607.06918)

**<font color=#1a73e8>作者：</font>** Sojung An, Junha Lee, Sujeong You 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained Vision Foundation Models (VFMs) provide strong visual representations for diverse downstream tasks. The key challenge of VFM adaptation stems from the prohibitive costs of full fine-tuning and catastrophic forgetting. To address this, Low-Rank Adaptation (LoRA) has emerged as the prevailing paradigm for Parameter-Efficient Fine-Tuning (PEFT). However, LoRA is typically designed for transformer self-attention layers parameterized by 2D matrices. Since convolutional kernels inherently couple spatial and channel information within a 4D tensor, forcing them into a monolithic 2D matrix disrupts the inherent spatial topology. In this paper, we propose Low-Rank Convolutional Adaptation (LoCA), a convolution-aware PEFT framework that addresses spatial-channel entanglement by decoupling channel and spatial adaptation. LoCA introduces a low-rank channel adaptation for dense cross-channel mixing and refines spatial bases extracted from pre-trained kernels via Singular Value Decomposition (SVD). Experimental results show that LoCA preserves pre-trained spatial priors and achieves competitive or state-of-the-art performance across fine-grained classification, domain-generalized semantic segmentation, and generative benchmarks.

---


### 22. [Grounding Spatial Relations in a Compact World Model: Instruction Leakage and a Goal-Free Dynamics Fix](https://arxiv.org/abs/2607.06925)

**<font color=#1a73e8>作者：</font>** Yufeng Wang, Lu Wei, Haibin Ling  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compact world models that condition on a language goal promise to ground relations such as ``put the red block left of the blue block'' using a sparse set of explicit \emph{reference anchors}. We ask when such references actually ground a relation, and identify a trap: a goal-conditioned predictor reaches a striking $0.90$ relation-readout accuracy, yet this is \emph{instruction transcription}, not perception. Withholding the goal collapses it to chance ($0.90\!\to\!0.27$, three seeds) and a counterfactual instruction makes the predicted anchors follow the \emph{false} instruction $94.5\%$ of the time (true scene $2.3\%$; $N{=}256$). Tested across three settings and a within-task ablation, our central claim characterizes the confound: \textbf{instruction leakage occurs when the scored quantity is transcribable from the instruction (when the instruction names the answer) and is essentially independent of how predictive the non-instruction inputs are.} Our tabletop and the external BabyAI benchmark leak, whereas a Language-Table forward-dynamics world model whose instruction names \emph{referents} does not, until the instruction is augmented to name the direction; and degrading the action never increases leakage, the opposite of what predictor-competition predicts. The diagnosis prescribes the fix: keep the goal out of the dynamics (it belongs to the planner's cost) and supervise the \emph{read} path, recovering genuine, instruction-independent grounding ($0.88$, identical with and without the goal). The detection protocol and remedy apply to any goal-conditioned world model whose instruction names the scored quantity.

---


### 23. [Comprehensive Evaluation of Large Language Model Responses: A Multi-Factor Scoring System](https://arxiv.org/abs/2607.06940)

**<font color=#1a73e8>作者：</font>** Yiming Gai, Junde Lu, Xuefei Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The remarkable performance of large language models (LLMs) in linguistic tasks underscores an urgent need for comprehensive evaluation of their response quality. Prevailing methods, often confined to singular dimensions, fall short of capturing the full spectrum of model capabilities. This study introduces a multifactor scoring paradigm, integrating accuracy, conciseness, factual consistency, readability, and coherence, complemented by a graphical user interface (GUI) for visualizing outcomes. Evaluations on the TruthfulQA dataset unveil mainstream LLMs' strengths in reasoning tasks (peaking at a composite score of 0.6104) alongside pervasive limitations in navigating complex facts and ambiguities. Transcending the narrow lens of traditional metrics, this framework offers a transparent, adaptable avenue to illuminate model potential and deficiencies. Though presently focused on English tasks, its horizons beckon toward multilingual domains. This work carves a novel path for knowledge engineering and model refinement.

---


### 24. [General Incomplete Multimodal Learning via Dynamic Quality Perception](https://arxiv.org/abs/2607.06943)

**<font color=#1a73e8>作者：</font>** Xiangyu Meng, Shicai Wei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal learning robust to missing modalities is essential for real-world applications. Existing methods mainly focus on inter-modality missing, where entire modalities are absent, while overlooking intra-modality degradation, where modalities are present but severely corrupted. In practice, these two types of missing often coexist, making existing approaches ineffective. To address this limitation, we propose General Incomplete Multimodal Learning (GIML), a unified framework that simultaneously handles both inter-modality missing and intra-modality degradation through dynamic quality perception. Specifically, GIML models heterogeneous missing patterns as continuous modality information degradation, enabling degradation-aware adaptive fusion. To achieve reliable quality perception, we introduce a Noise-aware Quality Estimator that learns the mapping from corrupted features to noise intensity through controlled noise injection. Furthermore, we propose a Noise-Semantic Decoupled module that separates semantic information from noise interference. This improves robustness and generalization to unseen corruption patterns. Extensive experiments across datasets with diverse modality types demonstrate the effectiveness and generality of GIML. Code is available at: this https URL.

---


### 25. [Physical activities enable scalable foundation modelling for broad-spectrum health prediction](https://arxiv.org/abs/2607.06954)

**<font color=#1a73e8>作者：</font>** Zhenghuang Wu, Yuyao Zhu, Songlin Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable and mobile sensing technologies have demonstrated strong potential for health inference; however, most sensor models are designed for specific disease types, limiting their transferability across different health risks. Wearable foundation models offer a more generalizable approach in diverse health risk types. Nevertheless, most existing methods rely on high-frequency raw sensor data, raising concerns about privacy, computational overhead, and scalability across devices and populations. In this paper, we propose StepFM, a foundation model built solely on step counter data for broad-spectrum health prediction. Leveraging the ubiquity and low-dimensional nature of step data, StepFM provides a practical, privacy-preserving, and computation-efficient alternative to traditional sensor-based models. We design a scalable pre-training framework that captures temporal dynamics and behavioral patterns from large-scale step sequences, enabling transfer across more than 20 health risk prediction tasks spanning diverse devices, new regions, and novel disease types. Extensive experiments demonstrate that StepFM achieves strong performance compared to existing methods while maintaining robustness across heterogeneous settings. Furthermore, our analysis reveals interpretable and generalizable relationships between physical activity patterns and various health risks, offering new insights into activity-based health modeling. Our work establishes step-based sensing as a viable foundation for scalable and real-world health monitoring.

---


### 26. [Rethinking Multimodal Time-Series Forecasting Evaluation](https://arxiv.org/abs/2607.06973)

**<font color=#1a73e8>作者：</font>** Haoxin Liu, Yichen Zhou, Rajat Sen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a new context-enriched, multimodal time series forecasting benchmark, TimesX. TimesX contains a wide selection of high-quality real-world time series with diverse domains and textual contexts obtained from an automated data generation pipeline, which helps address three main issues of existing multimodal forecasting benchmarks: (1) poor generalization due to the small scale and synthetic nature of benchmark data, (2) very limited types of textual contexts in the benchmarks, and (3) an inability to mitigate data leakage in evaluation. We conduct a thorough empirical study of zero-shot multimodal forecasting approaches on TimesX. Our results suggest that many approaches that perform well on existing benchmarks may fail on TimesX. In contrast, simple ensemble methods that leverage rich textual context accompanying time-series can outperform strong baselines on TimesX.

---


### 27. [MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning](https://arxiv.org/abs/2607.06974)

**<font color=#1a73e8>作者：</font>** Ruilin Tong, Dong Gong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly improve their reasoning at test time via additional computation, yet most existing works treat each problem in isolation. When problems arrive sequentially, accumulating reusable experience across them can further improve performance. Existing memory-based methods either store whole-solution templates that generalize poorly to novel problems or use heuristic step-level selection that is not optimized for final-answer correctness. Learning selection policies requires large-scale training data and fixed action spaces, making such approaches unsuitable for test-time settings where memory expands incrementally and only limited supervision is available. We propose MILES (Modular Instruction Memory with LEarnable Selection for self-improving LLM reasoning), a framework that dynamically expands step-wise memory and applies correctness-optimized memory composition under realistic test-time constraints. MILES maintains modular memory units consisting of asymmetric pairs of sub-goal embeddings and sub-instructions, each associated with a learnable selection head. This memory structure enables a coarse-to-fine retrieval mechanism: The coarse level enables memory expansion and collects supervision for training selection heads from confident samples, while the fine stage applies learned selection heads to rerank coarse-level candidates and guide reasoning for uncertain samples. MILES consistently matches or outperforms prior methods while achieving superior accuracy-efficiency tradeoffs. Extensive experiments demonstrate its effectiveness, robustness, and transferability.

---


### 28. [UP: Unbounded Positive Asymmetric Optimization for Breaking the Exploration-Stability Dilemma](https://arxiv.org/abs/2607.06987)

**<font color=#1a73e8>作者：</font>** Chongyu Fan, Pengfei Liu, Jingjia Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become the standard paradigm for enhancing the complex reasoning capabilities of large language models (LLMs). To achieve sample efficiency, modern RL frameworks rely on importance sampling (IS). However, these algorithms suffer from an exploration-stability dilemma. Pure IS often leads to catastrophic training instability, while standard clipping mechanisms used to mitigate this instability strictly constrain the policy update budget. By formalizing the concept of Probability Capacity (Cap), we reveal that conservative clipping structurally stifles exploration by prematurely truncating the update budget for correct but low-confidence reasoning paths. To break free from these constraints, we propose Unbounded Positive Asymmetric Optimization (UP), a universal and plug-and-play objective. UP theoretically restructures the optimization process by anchoring the policy to its current state via the stop-gradient operator. This asymmetric design unleashes unclipped, stable gradients for positive advantages to maximize exploration, while maintaining standard clipping safeguards for negative advantages to prevent training instability. Furthermore, our formulation readily extends across different optimization granularities, including token-level (GRPO, DAPO) and sequence-level (GSPO) frameworks. Extensive experiments demonstrate that UP enhances exploration capacity and achieves superior reasoning accuracy across diverse RL algorithms (DAPO, GSPO, and GRPO), model architectures (Dense, MoE, and vision-language), and training modalities (language and multimodal), validating UP as a truly universal plug-and-play enhancement for RL-based training.

---


### 29. [Large Behavior Model: A Promptable Digital Twin of the Retail Customer](https://arxiv.org/abs/2607.06993)

**<font color=#1a73e8>作者：</font>** Wachiravit Modecrua, Krittin Pachtrachai, Touchapon Kraisingkorn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Customer behavior modeling underpins recommendation, marketing, and decision support, yet existing approaches either optimize predictive accuracy without explaining decisions or simulate users without grounding them in real behavioral data. We present the Large Behavioral Model (LBM) that learns customer decision making directly from large-scale retail transactions through a unified Person-Environment formulation. Customer state is represented by a behavioral profile derived from historical purchases, while product context is incorporated through retrieval-augmented generation. The model is trained using continued pre-training on verbalized behavioral data, supervised fine-tuning for decision generation, and reinforcement learning with verifiable rewards for evidence-based calibration. We evaluate the proposed framework on purchase prediction, hard-negative discrimination, basket completion, promotion response, and cross-domain voucher redemption. The model consistently outperforms frontier general-purpose language models on in-domain retail tasks while demonstrating strong zero-shot and fine-tuned transfer across retailers and decision domains. Ablation studies show that continued pre-training is the primary driver of behavioral generalization, retrieval is most effective when applied during both training and inference, and reinforcement learning improves reliance on explicit behavioral evidence over generic language-model priors. These results demonstrate that behavioral knowledge encoded in transaction histories can be effectively learned by language models, providing a scalable foundation for customer digital twins and behavior simulation.

---


### 30. [Multimodal Smart Glove for Sign Language Recognition Using Deep Learning](https://arxiv.org/abs/2607.06996)

**<font color=#1a73e8>作者：</font>** Anh Thu Nguyen Ngoc, Tam Phong Truong, Thai Anh Nguyen Duong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Sign language recognition technologies can improve communication between deaf individuals and the broader community, but many existing systems face challenges in real-world deployment. This paper presents a deployable smart glove system for sign language recognition that integrates wearable sensing and deep learning. The glove incorporates flex sensors and an inertial measurement unit (IMU) to capture finger articulation and hand motion, while facial cues are obtained through a camera. Sensor data are transmitted via an ESP32-C6 microcontroller and processed using a long short-term memory (LSTM) network to model temporal gesture dynamics. Experimental results show that the proposed model achieves an overall recognition accuracy of approximately 95%. The trained model is further converted to TensorFlow Lite for real-time inference. This demonstrates the feasibility of the system for practical sign language translation applications.

---


### 31. [Ego-Human Motion Prediction with 3D-Aware LLM](https://arxiv.org/abs/2607.07001)

**<font color=#1a73e8>作者：</font>** Yujin Bae, Jaewoo Jeong, Hyeonseong Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anticipating human motion from an egocentric perspective is fundamental for proactive assistance in AR/VR, human-robot collaboration, and embodied AI. While recent works incorporate language as a semantic prior to reduce the ill-posed nature of egocentric forecasting, they largely neglect the 3D spatial and semantic context that governs how motion unfolds, and treat pose and language prediction as separate inference streams. We introduce Ego3DLM, built on two core principles: accurate motion forecasting requires explicit spatial and semantic understanding of the 3D environment, and pose and language must be predicted holistically in a single pass, since motion is inherently tied to the semantic interpretation of actions being performed. Given three-point tracking, 3D scene features, and egocentric video, Ego3DLM simultaneously decodes past pose, future pose, past narration, and future narration in a single autoregressive pass, grounding predicted poses and descriptions in one another to enforce cross-modal and temporal consistency. We adopt a three-stage training scheme: (1) spatial-semantic scene awareness pretraining; (2) holistic instruction tuning over all four outputs in a single pass; and (3) GRPO-based reinforcement finetuning with intra- and inter-modal rewards that directly optimize pose-language fidelity. Experiments on the Nymeria benchmark demonstrate that Ego3DLM achieves state-of-the-art performance across future motion prediction, past motion tracking, and motion description, showing that 3D scene grounding and holistic cross-modal prediction yield physically plausible and semantically coherent motion forecasts. The project page is available at this https URL.

---


### 32. [Dissociating the Internal Representations of Sycophancy in LLMs](https://arxiv.org/abs/2607.07003)

**<font color=#1a73e8>作者：</font>** Anthony Baez, Sheer Karny, Pat Pataranutaporn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) frequently exhibit sycophancy, where they agree with a user's statement even when incorrect. While sycophancy is often treated as a single defined behavior, it can manifest in substantially distinct ways and circumstances, raising the question of whether this multi-faceted nature is reflected in its internal mechanisms. To address this gap, we dissociate the representations of sycophancy into factual and opinion subtypes -- motivated by the distinction between verifiable claims and subjective beliefs. We train linear probes and construct steering vectors on activations of one subtype and evaluate their transfer to the other subtype to measure to what extent they share representations. We find evidence that different LLMs represent these subtypes differently, with either more unified or more distinct and causally interfering representations. This method of dissociation offers a promising framework for studying the representational structure of complex model behaviors.

---


### 33. [Multimodal Spatiotemporal-Frequency Fusion with Peak Enhancement for Cellular Traffic Forecasting](https://arxiv.org/abs/2607.07016)

**<font color=#1a73e8>作者：</font>** Qingzhong Li, Yue Hu, Hui Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting of cellular network traffic is essential for network planning, resource allocation, and quality-of-service assurance in modern mobile communication systems. Real-world traffic often exhibits bursty endogenous dynamics and disturbances triggered by external urban events, which makes reliable prediction highly challenging. Most existing spatiotemporal traffic forecasting methods primarily focus on intrinsic traffic patterns or structural relationships within a single modality, and rarely model burst behavior together with exogenous contextual signals. To address this issue, we propose \textbf{MSPF-Net}, a multimodal cellular traffic forecasting framework that integrates external contextual information. Specifically, MSPF-Net consists of a Spatiotemporal-Frequency Traffic Encoder for capturing temporal, spatial, and spectral traffic patterns, a Peak Enhancement Module for extracting burst-aware representations of sudden spikes, a News Context Representation Module for encoding urban news streams into exogenous contextual embeddings, and a Dynamic Fusion Prediction Module for adaptively integrating these heterogeneous signals to generate forecasts. Experiments on the Milano, Trento, and LTE traffic datasets demonstrate that jointly modeling traffic dynamics, burst patterns, and news contextual signals can effectively improve forecasting performance.

---


### 34. [SHTA: Semantic Hard Token Correction and Center Alignment for Semi-Supervised Medical Image Segmentation](https://arxiv.org/abs/2607.07019)

**<font color=#1a73e8>作者：</font>** Zhuoru Zhang, Yiheng Zhong, Zimu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in semi-supervised medical image segmentation have achieved remarkable performance through prediction consistency, pseudo-label supervision, and hard-region supervision. However, these methods primarily improve supervision quality rather than explicitly enforcing semantic consistency in the learned representations of hard regions. Consequently, even under increasingly stronger prediction-level supervision, difficult regions exhibiting unstable semantic assignment often fail to establish semantically consistent representations during training, thereby limiting further segmentation improvement. To address this issue, we propose SHTA (Semantic Hard Token Correction and Center Alignment), a lightweight training-time semantic representation branch. Instead of introducing additional prediction supervision, SHTA refines intermediate semantic representations through Semantic Assignment, Hard Token Refinement, and Semantic Center Alignment, thereby improving semantic consistency in hard regions while preserving the original prediction pathway and introducing no additional inference cost. We integrate SHTA into representative semi-supervised segmentation frameworks, including GA-CPS, CPS, URPC, and MagicNet, and conduct evaluations on the Synapse and AMOS datasets. Experimental results demonstrate that SHTA delivers consistent paired improvements across frameworks, with especially clear gains in segmentation accuracy, weak-organ recovery, and semantic ambiguity reduction, while incurring only training-time overhead. The code is available at this https URL.

---


### 35. [Learning social norms enhances compatibility in dynamic human-AI coordination](https://arxiv.org/abs/2607.07021)

**<font color=#1a73e8>作者：</font>** Yi Yang, Siyuan Liu, Xin Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humans continuously coordinate with others in dynamic interactions, often through implicit, hard-to-quantify social norms that act as shared tacit expectations among interacting agents. As AI agents, including large language models (LLMs), become embedded in daily life, they increasingly participate in such interactions and reshape social interaction structures. Yet they often fail to coordinate with humans in an effective, considerate, and natural manner. We hypothesize that this gap arises because existing approaches align model behavior with human demonstrations without explicitly quantifying the underlying norms that generate such behavior. We selected pedestrian-vehicle interaction as a representative dynamic interaction and developed a simplified experimental platform that captures its key interactive features. From 3,456 dynamic human interactions collected via this platform, we identified three principles underlying human social norms: outcome predictability, value alignment, and advantage awareness. Incorporating these principles into AI agents significantly improves human-AI coordination. In the closed-loop interaction task with humans, the social-norm-informed LLM achieved a nearly fourfold higher total score than the baseline strategy and outperformed human-human interactions by 43%. These findings indicate that formalizing tacit social norms into explicit, quantifiable principles can enable AI agents to achieve mutually beneficial coordination in dynamic interactions, supporting their more natural integration into human society.

---


### 36. [Online Data Selection Is Implicit Alignment](https://arxiv.org/abs/2607.07023)

**<font color=#1a73e8>作者：</font>** Aoxiong Zeng, Yuxin Yang, Xiangquan Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) is often treated as a capability-adaptation step, while alignment is attributed to later preference optimization or reinforcement learning. This separation is incomplete: when examples are scored and kept online during fine-tuning, the choice of which data to train on already changes the model's behavioral preferences. We study online data selection as an implicit alignment mechanism. Given the same base model, optimizer, and selected-token budget, we compare random, loss-based, quality-based, and diversity-based online selectors and measure the behavioral drift they induce without any preference optimization. The proposed evaluation tracks helpfulness, refusal rate, verbosity, truthfulness, sycophancy, calibration, and jailbreak robustness, together with diagnostics for which behavioral modes are over-represented in the selected data. We formalize online selection as a reweighted SFT objective whose weights define an implicit preference over response styles and safety postures, so that an online scorer plays the role usually assigned to a reward model. This view predicts that high-scoring data can systematically favor longer, more assertive, more compliant, or more refusal-prone behaviors depending on how the online score is defined. Empirically, selectors that are statistically indistinguishable in task accuracy diverge sharply in refusal rate, verbosity, and sycophancy, and we show that the direction of the shift is predictable from the attribute mixture of the selected data. We introduce Alignment Drift Auditing (ADA), a controlled protocol for quantifying selection-induced behavioral movement, and Alignment-Aware Selection (AAS), a diagnostic online selector that retains data efficiency while constraining drift along safety and style axes.

---


### 37. [Constrained Decoding for Diffusion Language Models via Efficient Inference over Finite Automata](https://arxiv.org/abs/2607.07026)

**<font color=#1a73e8>作者：</font>** Meihua Dang, Stefano Ermon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constrained decoding is essential for serving LLMs, ensuring that generated outputs follow specific structures such as JSON schema-formatted function calls. Existing systems are designed for autoregressive models and assume left-to-right generation, masking out invalid next tokens at each step. Diffusion language models, however, break this assumption: they sample multiple positions simultaneously from a fully-factorized mean-field distribution at each denoising step. In this paper, we present an exact and tractable algorithm for sampling from the constrained mean-field posterior under any constraint expressible as a finite automaton. Viewing finite automata as graphical models, we obtain tractable representations of the constrained distribution that enable efficient inference. The approach guarantees constraint satisfaction by construction, supports both greedy and sampling-based decoding, and is compatible with parallel and block-wise decoding under arbitrary remasking schedules. Applying depth-reduction techniques from arithmetic circuit theory, we further reduce sampling depth from linear to logarithmic in the sequence length. Empirical evaluations on Dream-7B and LLaDA-8B show substantial accuracy gains across various tasks including function calling (xLAM, BFCL), planning (Sudoku, Countdown), text-to-SQL (Spider), and math reasoning (GSM-Symbolic), with little inference overhead relative to unconstrained decoding. For example, on BFCL-Live, our approach improves Dream-7B's greedy decoding accuracy from 63.9% to 71.5%, and stochastic sampling accuracy from 22.3% to 69.0%, where the unconstrained baseline collapses, with under 5% wall-clock overhead.

---


### 38. [Latent graph encoding of multimodal neuroimaging features with generative AI architectures](https://arxiv.org/abs/2607.07027)

**<font color=#1a73e8>作者：</font>** Ishaan Batta, Meenu Ajith, Vince Calhoun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While generative models enable encoding of complex neuroimaging data for feature generation and reconstruction, developing optimal architectural frameworks with appropriate encoding and latent space processes is crucial for studying structural and functional properties of the brain. We design a multimodal generative framework for structural and functional magnetic resonance imaging (MRI) features through systematic evaluation of encoding strategies, latent multimodal fusion, and generative model selection. Using structural gray matter volume (GMV) and static functional network connectivity (sFNC) features from a large neuroimaging dataset, we analyze generative frameworks involving variational autoencoders (VAEs), transformers, generative adversarial networks (GANs), and diffusion models. Architectures that employ modality-aware graph encoding of functional connectivity into a lower-dimensional latent space outperform vectorized encoders or direct data space approaches. The proposed multimodal graph VAE (gMMVAE) surpasses alternative generative variants across multiple metrics for generation fidelity, reconstruction quality, efficiency, and latent space discriminability, highlighting its potential for robust multimodal neuroimaging analysis.

---


### 39. [AnchorPrune: Relevance-Anchored Contextual Expansion for Visual Token Pruning](https://arxiv.org/abs/2607.07033)

**<font color=#1a73e8>作者：</font>** Kyuan Oh, Bumsoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models incur substantial inference costs because high-resolution inputs introduce thousands of visual tokens, many of which are redundant for a given query. Existing pruning methods often combine query relevance and token diversity, yet these objectives can conflict under aggressive compression: relevance-driven selection may overconcentrate the budget on correlated local evidence, while diversity-driven selection may suppress indispensable tokens or retain distinct but uninformative regions. We introduce AnchorPrune, a training-free framework that first constructs a protected relevance anchor and then expands it with complementary visual context. AnchorPrune adaptively determines the anchor size from the novelty profile of relevance-ranked tokens, preserving a compact set of query-critical evidence, and allocates the remaining budget through importance-weighted novelty to recover informative, non-redundant context relative to the anchor. This ordered design prevents contextual expansion from displacing indispensable query cues while improving overall visual coverage. AnchorPrune is lightweight, architecture-aware, and requires neither retraining nor model modification. Across image and video vision-language models and benchmarks, it consistently improves the accuracy-efficiency trade-off over training-free baselines, particularly under severe compression. On LLaVA-NeXT-7B, AnchorPrune preserves 97.6% of full-token performance using only 160 of 2,880 visual tokens. These results establish relevance-anchored contextual expansion as an effective principle for efficient multimodal inference. Code is available at this https URL.

---


### 40. [Riemannian Geometry for Pre-trained Language Model Embeddings](https://arxiv.org/abs/2607.07047)

**<font color=#1a73e8>作者：</font>** Szczepan Konior, Alexandre Quemy, Przemysław Klocek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding the geometric structure of pre-trained language model embeddings matters for interpretability and safety. We ask whether sentence-level classification signal lives in the Riemannian geometry of contextual token embeddings, and probe it by extracting per-token pullback metrics from a learned encoder's analytical Jacobian and aggregating them with the Fréchet mean on the symmetric positive definite (SPD) manifold; we call this procedure Riemannian Mean Pooling (RMP). Across three datasets with non-trivial linguistic structure (CoLA, CREAK, RTE), RMP outperforms Euclidean mean pooling, while on FEVER-Symmetric, a benchmark constructed to remove annotation-driven lexical artifacts, the method correctly stays at chance. Ablations show that a randomly initialised encoder combined with Fréchet aggregation already beats Euclidean pooling on two of the three signal-bearing datasets, localising the source of the gain to the geometric aggregation rather than to learned manifold structure; the trained encoder contributes additional signal specifically on CREAK, the most knowledge-heavy of the three signal-bearing datasets.

---


### 41. [Behavior Leverage Imbalance in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2607.07050)

**<font color=#1a73e8>作者：</font>** Jiabin Shen, Guang Chen, Chengjun Mao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic language models must learn when to call tools, when to consume tool responses, and when to answer directly. This makes multi-teacher on-policy distillation a natural training strategy: one teacher can specialize in tool calls, another in direct responses, and the student can learn from both on
its own generated distribution. We show that this strategy can induce a behavior shift that is invisible from aggregate losses alone. In a two-teacher tool-use setting, vanilla generalized knowledge distillation improves tool-call recall but also moves the model toward over-calling, where it calls tools
on examples that should be answered directly. Aggregate explanations are insufficient: tool-call samples do not receive more token exposure, and full-sequence per-token divergence is not larger for the tool-call teacher. We instead analyze behavior leverage imbalance: local token-level signals at mode-
entry and structural positions, such as <tool_call> and function names, can have disproportionate control over the global generation mode. We propose Soft Clamp, a per-token divergence calibration method that dynamically compresses extreme token-level Jensen-Shannon divergence while preserving nonzero
gradients. On APIGen-MT, Soft Clamp reduces over-calling from 13.7% to 9.0% relative to vanilla GKD while matching its decision accuracy. In a BFCL multi-turn diagnostic, it also lowers tool-call loops and repeated calls among GKD variants. These results suggest that multi-teacher OPD should monitor
where teacher signals act, not only how large they are in aggregate.

---


### 42. [AT-Attn: Temporal-Aware Cross-Attention for Longitudinal Multimodal Alzheimer's Disease Diagnosis](https://arxiv.org/abs/2607.07091)

**<font color=#1a73e8>作者：</font>** Xinyue Du, Yibo Liu, Zhenglei Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In longitudinal Alzheimer's disease (AD) diagnosis support, clinical and imaging information is often collected at irregular visits. Integrating these multimodal observations may improve diagnostic assessment, but naive fusion can degrade performance when MRI is noisy or intermittently unavailable. We propose AT-Attn, a temporal-aware multimodal framework that combines Change-and-Time encoding, time-biased asymmetric cross-attention, and gated fusion to integrate MRI with longitudinal clinical information. We evaluate AT-Attn on an MRI-retained ADNI cohort of 1,520 patients using structural MRI, six cognitive-scale trajectories, and seven static clinical variables under patient-level five-fold cross-validation. The main asymmetric AT-Attn model achieves accuracy 0.719+/-0.024, macro F1 0.721+/-0.023, ROC-AUC 0.873+/-0.013, and PR-AUC 0.783+/-0.018, outperforming unimodal and naive multimodal fusion baselines while remaining competitive with strong tabular baselines. These results suggest that a temporal-aware and constrained fusion strategy can help structural MRI contribute clinically relevant complementary information for patient-level AD diagnosis support.

---


### 43. [Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety](https://arxiv.org/abs/2607.07097)

**<font color=#1a73e8>作者：</font>** Lifei Liu, Haoran Yu, Xiaochong Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety evaluations of multi-agent LLM systems often compare a direct prompt with a planner-executor pipeline and report the difference as a single "pipeline effect." We argue that this aggregate is difficult to interpret because it conflates three mechanisms: harmful intent may be reframed as plausible operational work, the planner may refuse or transform the request, and the executor may act under delegation prompts implying prior approval. To separate these factors, we introduce a five-condition controlled contrast design, evaluated on 30 synthetic harmful scenarios and an exploratory external validation set from four agent-safety benchmarks using LLM-judged compliance.
Our results show that aggregate pipeline safety is not a stable architectural property. Operational reframing is the most portable risk signal, increasing compliance for GPT, Gemini, and DeepSeek across both scenario sets, while Claude is comparatively resistant. Planner behavior can offset this risk mainly through refusal; however, when the planner produces executable steps, the executor may become more compliant than under the direct operational baseline. Approval-framed delegation is sensitive to prompt design, model pairing, and scenario source, and a skeptical executor prompt sharply reduces compliance.
Raw-direct model rankings can also mispredict deployed planner-executor behavior. Gemini is safest under raw direct prompts in the primary set yet shows the largest amplification with a Claude planner, rising from 8.9 percent to 38.9 percent compliance. GPTs near-zero aggregate pipeline effect instead hides a reframing increase canceled by planner refusal. These findings suggest that multi-agent safety evaluations should report reframing, planner behavior, delegation framing, and model pairing separately before attributing failures to architecture itself.

---


### 44. [A knowledge-augmented dataset of high-risk driving scenarios with LLM annotations for autonomous driving](https://arxiv.org/abs/2607.07103)

**<font color=#1a73e8>作者：</font>** Heye Huang, Jingguang Li, Zhiyuan Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe autonomous driving requires both rapid responses to common high-risk events and deeper reasoning over rare, extreme long-tail scenarios in traffic safety. These scenarios are severely under-represented in naturalistic driving data, and existing trajectory and language-augmented datasets seldom provide high-risk event labels, semantic annotations, and verifiable safety signals. Here we present K-Risk, a knowledge-augmented dataset that combines structured driving trajectories with large language model generated semantic annotations for safety-critical driving scenarios. K-Risk integrates 20 human-driven and autonomous-vehicle trajectory datasets from Europe, China, and the United States, covering highways, urban freeways, intersections, and roundabouts. Using a unified risk-centric extraction pipeline, K-Risk curates 31,398 high-risk events, together with a 1,036-event extreme subset of near-collision cases. Each event is released as a synchronized trajectory, metadata, and language triplet containing structured scenario descriptions, abnormal-behavior notifications, and, for a representative subset, causal risk analyses and action recommendations validated through a closed-loop simulator with iterative reflection. By combining multi-dimensional risk annotations, interpretable language supervision, and verifiable decisions, K-Risk bridges structured traffic trajectories, semantic reasoning, and decision supervision, providing a standardized foundation for developing and evaluating next-generation risk-aware autonomous driving agents.

---


### 45. [Tree-of-Thoughts Reasoning for Text-to-Image In-Context Learning](https://arxiv.org/abs/2607.07117)

**<font color=#1a73e8>作者：</font>** Stepanida Alekseeva, Jenifer Kalafatovich, Seong-Whan Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In text-to-image in-context learning (T2I-ICL), a model has to infer a latent compositional pattern from fewshot demonstrations for generating a query image. Recent studies show that state-of-the-art multimodal large language models struggle with this setting, particularly due to limited compositional reasoning and sensitivity to prompt construction. In this work, we propose a Tree-of-Thoughts (ToT) reasoning framework for T2I-ICL that introduces a multi-stage reasoning and selection layer that generates, evaluates, and selects among multiple candidate hypotheses before constructing the final prompt for image synthesis. By exploring alternative reasoning branches and selecting a coherent interpretation, the proposed approach mitigates prompt ambiguity and compositional errors. We implement the proposed approach in a complete ToT-T2IICL inference pipeline and evaluate it on the CoBSAT benchmark. Both qualitative and quantitative results show that structured multi-branch reasoning leads to more consistent and semantically aligned image generation compared to baseline and Chain-of-Thought prompting strategies, without any additional training or fine-tuning.

---


### 46. [Distributed Sparse Interventions in Language Models](https://arxiv.org/abs/2607.07128)

**<font color=#1a73e8>作者：</font>** Maximilian S. Ernst, Lorenz Linhardt, Aaron Peikert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models perform a wide range of tasks at varying levels of abstraction with the capacity to flexibly infer tasks from context, execute multiple tasks simultaneously, and select among competing tasks. To study the role of model components in task behaviour, their causal influence can be investigated through interventions. Prior work on model steering has largely focused on interventions along global directions in activation space, modeling task representations as approximately linear and additive. By studying interventions at the neuron level, we find substantial, neuron-specific nonlinear effects on model outputs that are not captured by current steering approaches. We introduce Distributed Sparse Interventions (DSI), an intervention approach that considers nonlinearities and interactions between neurons across layers to identify sparse sets of neurons that elicit task-relevant computations. Across a range of tasks, we demonstrate that DSI can activate task behaviour in instruction-tuned language models by localising and intervening on as few as 0.01% of neurons, highlighting the effectiveness of sparse, distributed interventions in the neuron basis. Additionally, adopting a set-based perspective enables computations over the identified neuron sets, offering insights into the roles of individual neurons by analysing their effects across tasks. Through sparse interventions, DSI enables fine-grained control over model behaviour, localisation of task-relevant neuron sets, and furthers our understanding of task composition.

---


### 47. [Fractal KV-Cache Archives: Lossless Symbolic Storage with In-Place Retrieval for Long-Context LLM Inference](https://arxiv.org/abs/2607.07144)

**<font color=#1a73e8>作者：</font>** Vladimir Gusev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The key-value (KV) cache dominates the memory cost of long-context autoregressive inference, and a growing body of work compresses it through quantization, eviction, or offloading. We study a complementary question: once a position's KV state has been quantized to codebook indices, how should the resulting symbol stream be stored, and can the storage layer do more than store? A family of contractive iterated-map codes that serialize a symbol sequence into a sequence of low-dimensional real vectors is revisited, and it is shown that they form a natural archive format for a quantized KV cache with the following features. The method provides exactly the access pattern a growing cache requires. It is lossless, it runs in linear time, and supports O(1) random access and O(1) amortized append. A controlled study of the quantizer feeding this archive is conducted on GPT-2 with 1024-token contexts. Keeping a small exact window (4 attention sinks + 32 recent tokens) and archiving the rest, per-head residual vector quantization reduces the archived cache by 36-54x relative to an fp16 cache at a perplexity cost of 11-15%, and we quantify a sharp key/value asymmetry -- quantizing keys is roughly 4x more damaging than quantizing values, consistent with prior low-bit KV work -- and use it to allocate bits in a hybrid scheme. Finally, we show the archive is simultaneously a search index: approximate substring queries execute directly on the stored vectors, and matched context is decoded from the matched vector without ever materializing the surrounding text. We release all code; every number reproduces from a single command on a laptop CPU.

---


### 48. [ASFR-Net: Adversarial Alignment and Spatio-Frequency Refinement Network for Heterogeneous Remote Sensing Image Change Detection](https://arxiv.org/abs/2607.07161)

**<font color=#1a73e8>作者：</font>** Xin-Jie Wu, Zhi-Hui You, Si-Bao Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The core challenge of heterogeneous change detection in remote sensing imagery lies in effectively decoupling genuine land-cover changes from significant modal disparities caused by distinct imaging mechanisms. These intrinsic inconsistencies are prone to introducing pseudo-changes, thereby constraining detection accuracy. To address this, we propose a novel, end-to-end adversarial spatio-frequency refinement network (ASFR-Net). Initially, a modality-invariant representation learner (MIR-Learner) guides the backbone to extract modality-invariant features, effectively bridging the primary domain gap. Subsequently, to address persistent residual modal differences, we design an innovative spatio-frequency synergistic enhancement module (SFEM), which identifies and suppresses sensor-specific noise and artifacts that are difficult to discern in the spatial domain by leveraging frequency-domain processing. Multi-level difference features are then computed from these refined representations and fed into a decoder equipped with cascaded hierarchical guided fusion module (HGFM) blocks to generate precise change maps. To alleviate the data scarcity in heterogeneous tasks, we construct and release a new high-resolution benchmark specifically focused on building changes: the visible-near-infrared heterogeneous change detection (VisNIR-HCD) dataset. It presents unique scientific challenges arising from deceptive visual similarity and non-linear spectral inversions, providing a robust platform for evaluating model generalization. Extensive experiments on VisNIR-HCD and public datasets demonstrate that ASFR-Net achieves state-of-the-art (SOTA) performance, significantly outperforming existing methods. The source code and the VisNIR-HCD dataset are publicly available at this https URL.

---


### 49. [Entropy Pacing Policy Optimization for Multi-Task Agentic Reinforcement Learning](https://arxiv.org/abs/2607.07178)

**<font color=#1a73e8>作者：</font>** Zetian Hu, Shunyu Liu, Junjie Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent breakthroughs of Reinforcement Learning (RL) have highlighted its potential for complex agentic Large Language Model (LLM) tasks. However, existing efforts largely focus on single-task settings, whereas real-world deployment necessitates a generalist agent capable of solving multiple tasks simultaneously. In this work, we identify a critical yet underexplored phenomenon in multi-task agentic RL: different tasks can exhibit exploration-exploitation pace mismatch. Specifically, easier tasks may converge early to low-entropy policies that hinder learning on harder tasks, while harder tasks can, in turn, push easier tasks back toward high-entropy exploration. This back-and-forth interaction creates inter-task entropy crossovers and frequent entropy spikes. Inspired by this observation, we introduce Entropy Pacing Policy Optimization (EPPO) for multi-task agentic LLMs, which coordinates entropy across tasks to stabilize multi-task optimization. At the core of EPPO is a task-wise dynamic clipping mechanism that replaces the fixed clipping threshold in Group Relative Policy Optimization (GRPO) with a task entropy-aware adaptive bound, tightening updates for over-confident tasks while relaxing them for under-explored ones. Experiments on the multi-task agentic benchmarks demonstrate that the proposed EPPO yields results superior to its counterparts.

---


### 50. [Predicting LLM Safety Before Release by Simulating Deployment](https://arxiv.org/abs/2607.07184)

**<font color=#1a73e8>作者：</font>** Marcus Williams, Hannah Sheahan, Cameron Raymond 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-deployment safety evaluations aim to inform the downstream risks of releasing a new AI model. Yet most evaluations provide limited evidence about how often undesired model behavior will occur in deployment: they generally have insufficient coverage, are unrepresentative, and are generally recognizable as tests. To address these concerns, we study a simple way to simulate a model deployment: starting from de-identified conversations from a previous model deployment, we hold fixed the initial conversation prefix and regenerate the next response using a candidate model. The resulting responses can then both be audited for novel misalignments and used to estimate the prevalence of model misbehavior before deployment. We evaluate deployment simulation across four GPT-5-series deployments, using registered, outcome-blinded predictions for GPT-5.4 and retrospective analyses of three earlier releases. We find that deployment simulation produces informative estimates of post-deployment misbehavior rates and outperforms baselines based on adversarially selected production data; its evaluation-awareness point estimates were also much closer to production traffic than those from traditional evaluations. We also identify the realism of tool resampling as a central challenge for further improving predictions and share results suggesting that this challenge is surmountable even in complex tool-use settings. Finally, we show that deployment simulation can be seeded from public chat datasets and remain informative about production misbehavior rates, suggesting a path for external researchers to run deployment-grounded evaluations without access to private production logs. Overall, deployment simulation helps evaluators forecast how language models will behave in the real world and supports more quantitative assessment of deployment risk.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-84](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
