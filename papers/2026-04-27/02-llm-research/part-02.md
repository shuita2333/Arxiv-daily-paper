# 🧠 大模型相关研究 | 2026年04月27日

> 本类共 **97** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-97**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-97**

---

### 51. [CARE: Counselor-Aligned Response Engine for Online Mental-Health Support](https://arxiv.org/abs/2604.21352)

**<font color=#1a73e8>作者：</font>** Hagai Astrin, Ayal Swaid, Avi Segal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mental health challenges are increasing worldwide, straining emotional support services and leading to counselor overload. This can result in delayed responses during critical situations, such as suicidal ideation, where timely intervention is essential. While large language models (LLMs) have shown strong generative capabilities, their application in low-resource languages, especially in sensitive domains like mental health, remains underexplored. Furthermore, existing LLM-based agents often struggle to replicate the supportive language and intervention strategies used by professionals due to a lack of training on large-scale, real-world datasets.
To address this, we propose CARE (Counselor-Aligned Response Engine), a GenAI framework that assists counselors by generating real-time, psychologically aligned response recommendations. CARE fine-tunes open-source LLMs separately for Hebrew and Arabic using curated subsets of real-world crisis conversations. The training data consists of sessions rated as highly effective by professional counselors, enabling the models to capture interaction patterns associated with successful de-escalation. By training on complete conversation histories, CARE maintains the evolving emotional context and dynamic structure of counselor-help-seeker dialogue.
In experimental settings, CARE demonstrates stronger semantic and strategic alignment with gold-standard counselor responses compared to non-specialized LLMs. These findings suggest that domain-specific fine-tuning on expert-validated data can significantly support counselor workflows and improve care quality in low-resource language contexts.

---


### 52. [ReaGeo: Reasoning-Enhanced End-to-End Geocoding with LLMs](https://arxiv.org/abs/2604.21357)

**<font color=#1a73e8>作者：</font>** Jian Cui, Zhiyuan Ren, Desheng Weng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper proposes ReaGeo, an end-to-end geocoding framework based on large language models, designed to overcome the limitations of traditional multi-stage approaches that rely on text or vector similarity retrieval over geographic databases, including workflow complexity, error propagation, and heavy dependence on structured geographic knowledge bases. The method converts geographic coordinates into geohash sequences, reformulating the coordinate prediction task as a text generation problem, and introduces a Chain-of-Thought mechanism to enhance the model's reasoning over spatial relationships. Furthermore, reinforcement learning with a distance-deviation-based reward is applied to optimize the generation accuracy. Comprehensive experiments show that ReaGeo can accurately handle explicit address queries in single-point predictions and effectively resolve vague relative location queries. In addition, the model demonstrates strong predictive capability for non-point geometric regions, highlighting its versatility and generalization ability in geocoding tasks.

---


### 53. [Prototype-Based Test-Time Adaptation of Vision-Language Models](https://arxiv.org/abs/2604.21360)

**<font color=#1a73e8>作者：</font>** Zhaohong Huang, Yuxin Zhang, Wenjing Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) has emerged as a promising paradigm for vision-language models (VLMs) to bridge the distribution gap between pre-training and test data. Recent works have focused on backpropagation-free TTA methods that rely on cache-based designs, but these introduce two key limitations. First, inference latency increases as the cache grows with the number of classes, leading to inefficiencies in large-scale settings. Second, suboptimal performance occurs when the cache contains insufficient or incorrect samples. In this paper, we present Prototype-Based Test-Time Adaptation (PTA), an efficient and effective TTA paradigm that uses a set of class-specific knowledge prototypes to accumulate knowledge from test samples. Particularly, knowledge prototypes are adaptively weighted based on the zero-shot class confidence of each test sample, incorporating the sample's visual features into the corresponding class-specific prototype. It is worth highlighting that the knowledge from past test samples is integrated and utilized solely in the prototypes, eliminating the overhead of cache population and retrieval that hinders the efficiency of existing TTA methods. This endows PTA with extremely high efficiency while achieving state-of-the-art performance on 15 image recognition benchmarks and 4 robust point cloud analysis benchmarks. For example, PTA improves CLIP's accuracy from 65.64% to 69.38% on 10 cross-domain benchmarks, while retaining 92% of CLIP's inference speed on large-scale ImageNet-1K. In contrast, the cache-based TDA achieves a lower accuracy of 67.97% and operates at only 50% of CLIP's inference speed.

---


### 54. [mcdok at SemEval-2026 Task 13: Finetuning LLMs for Detection of Machine-Generated Code](https://arxiv.org/abs/2604.21365)

**<font color=#1a73e8>作者：</font>** Adam Skurla, Dominik Macko, Jakub Simko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-domain detection of the machine-generated code snippets in various programming languages is a challenging task. SemEval-2026 Task~13 copes with this challenge in various angles, as a binary detection problem as well as attribution of the source. Specifically, its subtasks also cover generator LLM family detection, as well as a hybrid code co-generated by humans and machines, or adversarially modified codes hiding its origin. Our submitted systems adjusted the existing mdok approach (focused on machine-generated text detection) to these specific kinds of problems by exploring various base models, more suitable for code understanding. The results indicate that the submitted systems are competitive in all three subtasks. However, the margins from the top-performing systems are significant, and thus further improvements are possible.

---


### 55. [VG-CoT: Towards Trustworthy Visual Reasoning via Grounded Chain-of-Thought](https://arxiv.org/abs/2604.21396)

**<font color=#1a73e8>作者：</font>** Byeonggeuk Lim, Kyeonghyun Kim, JungMin Yun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The advancement of Large Vision-Language Models (LVLMs) requires precise local region-based reasoning that faithfully grounds the model's logic in actual visual evidence. However, existing datasets face limitations in scalability due to extensive manual annotation and lack of explicit alignment between multi-step reasoning and corresponding image regions, which constrains the evaluation of model trustworthiness. To address these challenges, we propose the Visual Grounding Chain-of-Thought (VG-CoT) dataset, which explicitly links each reasoning step to real visual evidence within the image through a fully automated three-stage pipeline. The pipeline first extracts object- and text-level visual evidence using state-of-the-art detection and OCR models, then generates step-by-step grounded reasoning with GPT-4o, and finally refines the grounding through a rationale-driven open-set detection process. In addition, we introduce a new benchmark that comprehensively evaluates LVLMs reasoning across three complementary dimensions: Rationale Quality, Answer Accuracy, and Reasoning-Answer Alignment. Experiments with representative LVLMs, including LLaVA-1.5 and Qwen2-VL, demonstrate consistent improvements on most evaluation metrics, confirming that VG-CoT effectively enhances trustworthy, evidence-based reasoning while maintaining scalable and cost-efficient dataset construction. The dataset and code will be released publicly upon acceptance to facilitate further research.

---


### 56. [Neurodiversity and Technostress: Towards a Multimodal Research Design for Evaluating Subjective, Physiological, and Behavioral Responses](https://arxiv.org/abs/2604.21404)

**<font color=#1a73e8>作者：</font>** Lisa van den Heuvel, Igor Ivkić, René Riedl  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digitalization has transformed modern work by increasing efficiency while also introducing new forms of strain. Technostress (TS) describes subjective, physiological, and behavioral stress responses related to digital technology use. Existing TS research has predominantly focused on neurotypical populations and rarely integrates multiple stress dimensions within a single design. This paper addresses these gaps by proposing a controlled experimental research design that systematically compares neurodivergent and neurotypical individuals under standardized digital stress conditions. The proposed design combines structured and unstructured digital tasks with a multimodal measurement approach covering subjective perceptions, physiological activation, and observable interaction behavior. By integrating neurodiversity into TS research, the paper contributes to a more differentiated understanding of digital stress and provides a methodological approach for more inclusive digital work design.

---


### 57. [S1-VL: Scientific Multimodal Reasoning Model with Thinking-with-Images](https://arxiv.org/abs/2604.21409)

**<font color=#1a73e8>作者：</font>** Qingxiao Li, Lifeng Xu, QingLi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present S1-VL, a multimodal reasoning model for scientific domains that natively supports two complementary reasoning paradigms: Scientific Reasoning, which relies on structured chain-of-thought, and Thinking-with-Images, which enables the model to actively manipulate images through Python code execution during reasoning. In the Thinking-with-Images mode, the model generates and executes image-processing code in a sandbox environment, obtains intermediate visual results, and continues reasoning in a multi-turn iterative manner. This design is particularly effective for challenging scenarios such as high-resolution scientific chart interpretation, microscopic image understanding, and geometry-assisted reasoning. To construct the training data, we collect scientific multimodal datasets spanning six disciplines: mathematics, physics, chemistry, astronomy, geography, and biology. We further develop a six-dimensional quality filtering framework for reasoning trajectories. To mitigate redundant, ineffective, and erroneous visual operations commonly found in existing datasets, we propose a multi-stage filtering pipeline together with an adaptive data routing strategy. This strategy converts samples with low visual information gain into pure Reasoning-mode data, enabling the model to learn when image operations are truly necessary. S1-VL is trained through a four-stage progressive pipeline: scientific multimodal SFT, Thinking-with-Images cold-start SFT, and two stages of reinforcement learning with SAPO. We build S1-VL-32B on top of Qwen3-VL-32B-Thinking and evaluate it on 13 benchmarks. Experimental results show that S1-VL-32B achieves state-of-the-art performance on all five Thinking-with-Images benchmarks, including HRBench-4K, HRBench-8K, MME-RealWorld-CN, MME-RealWorld-Lite, and V*, and outperforms compared systems on scientific reasoning benchmarks such as Physics and VRSBench.

---


### 58. [Decoupled DiLoCo for Resilient Distributed Pre-training](https://arxiv.org/abs/2604.21428)

**<font color=#1a73e8>作者：</font>** Arthur Douillard, Keith Rush, Yani Donchev 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern large-scale language model pre-training relies heavily on the single program multiple data (SPMD) paradigm, which requires tight coupling across accelerators. Due to this coupling, transient slowdowns, hardware failures, and synchronization overhead stall the entire computation, wasting significant compute time at scale. While recent distributed methods like DiLoCo reduced communication bandwidth, they remained fundamentally synchronous and vulnerable to these system stalls. To address this, we introduce Decoupled DiLoCo, an evolution of the DiLoCo framework designed to break the lock-step synchronization barrier and go beyond SPMD to maximize training goodput. Decoupled DiLoCo partitions compute across multiple independent ``learners'' that execute local inner optimization steps. These learners asynchronously communicate parameter fragments to a central synchronizer, which circumvents failed or straggling learners by aggregating updates using a minimum quorum, an adaptive grace window, and dynamic token-weighted merging. Inspired by ``chaos engineering'', we achieve significantly improved training efficiency in failure-prone environments with millions of simulated chips with strictly zero global downtime, while maintaining competitive model performance across text and vision tasks, for both dense and mixture-of-expert architectures.

---


### 59. [Reasoning Primitives in Hybrid and Non-Hybrid LLMs](https://arxiv.org/abs/2604.21454)

**<font color=#1a73e8>作者：</font>** Shivam Rawat, Lucie Flek, Florian Mai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning in large language models is often treated as a monolithic capability, but its observed gains may arise from more basic operations. We study reasoning through two such primitives, recall and state-tracking, and ask whether hybrid architectures that combine attention-based retrieval with recurrent state updates are better suited than attention-only models for tasks that jointly require both. Using matched Olmo3 transformer and hybrid models in instruction-tuned and reasoning-augmented variants, we evaluate these models on a set of controlled tasks involving a mixture of state-tracking and recall primitives, state-based recall. Across tasks, we notice that reasoning augmentation provides the largest overall improvement, substantially extending the range of difficulty over which models remain effective. We also notice that in certain tasks, the hybrid reasoning model remains substantially more robust as sequential dependence increases. In contrast, the transformer reasoning model degrades sharply in performance as task difficulty increases beyond a given threshold. These results suggest that reasoning tokens and architectural inductive biases contribute at different levels of the computational process: explicit reasoning can expand a model's effective operating range, but its benefit depends on how well the underlying architecture supports persistent state propagation. Given the small size of our case study, which involves a limited set of models and tasks, we present these findings as suggestive rather than conclusive and leave broader validation across model families, scales, and task variations to future work.

---


### 60. [Do MLLMs Understand Pointing? Benchmarking and Enhancing Referential Reasoning in Egocentric Vision](https://arxiv.org/abs/2604.21461)

**<font color=#1a73e8>作者：</font>** Chentao Li, Zirui Gao, Mingze Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric AI agents, such as smart glasses, rely on pointing gestures to resolve referential ambiguities in natural language commands. However, despite advancements in Multimodal Large Language Models (MLLMs), current systems often fail to precisely ground the spatial semantics of pointing. Instead, they rely on spurious correlations with visual proximity or object saliency, a phenomenon we term "Referential Hallucination." To address this gap, we introduce EgoPoint-Bench, a comprehensive question-answering benchmark designed to evaluate and enhance multimodal pointing reasoning in egocentric views. Comprising over 11k high-fidelity simulated and real-world samples, the benchmark spans five evaluation dimensions and three levels of referential complexity. Extensive experiments demonstrate that while state-of-the-art proprietary and open-source models struggle with egocentric pointing, models fine-tuned on our synthetic data achieve significant performance gains and robust sim-to-real generalization. This work highlights the importance of spatially aware supervision and offers a scalable path toward precise egocentric AI assistants. Project page: this https URL

---


### 61. [Rethinking Cross-Domain Evaluation for Face Forgery Detection with Semantic Fine-grained Alignment and Mixture-of-Experts](https://arxiv.org/abs/2604.21478)

**<font color=#1a73e8>作者：</font>** Yuhan Luo, Tao Chen, Decheng Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Nowadays, visual data forgery detection plays an increasingly important role in social and economic security with the rapid development of generative models. Existing face forgery detectors still can't achieve satisfactory performance because of poor generalization ability across datasets. The key factor that led to this phenomenon is the lack of suitable metrics: the commonly used cross-dataset AUC metric fails to reveal an important issue where detection scores may shift significantly across data domains. To explicitly evaluate cross-domain score comparability, we propose \textbf{Cross-AUC}, an evaluation metric that can compute AUC across dataset pairs by contrasting real samples from one dataset with fake samples from another (and vice versa). It is interesting to find that evaluating representative detectors under the Cross-AUC metric reveals substantial performance drops, exposing an overlooked robustness problem. Besides, we also propose the novel framework \textbf{S}emantic \textbf{F}ine-grained \textbf{A}lignment and \textbf{M}ixture-of-Experts (\textbf{SFAM}), consisting of a patch-level image-text alignment module that enhances CLIP's sensitivity to manipulation artifacts, and the facial region mixture-of-experts module, which routes features from different facial regions to specialized experts for region-aware forgery analysis. Extensive qualitative and quantitative experiments on the public datasets prove that the proposed method achieves superior performance compared with the state-of-the-art methods with various suitable metrics.

---


### 62. [Frozen LLMs as Map-Aware Spatio-Temporal Reasoners for Vehicle Trajectory Prediction](https://arxiv.org/abs/2604.21479)

**<font color=#1a73e8>作者：</font>** Yanjiao Liu, Jiawei Liu, Xun Gong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have recently demonstrated strong reasoning capabilities and attracted increasing research attention in the field of autonomous driving (AD). However, safe application of LLMs on AD perception and prediction still requires a thorough understanding of both the dynamic traffic agents and the static road infrastructure. To this end, this study introduces a framework to evaluate the capability of LLMs in understanding the behaviors of dynamic traffic agents and the topology of road networks. The framework leverages frozen LLMs as the reasoning engine, employing a traffic encoder to extract spatial-level scene features from observed trajectories of agents, while a lightweight Convolutional Neural Network (CNN) encodes the local high-definition (HD) maps. To assess the intrinsic reasoning ability of LLMs, the extracted scene features are then transformed into LLM-compatible tokens via a reprogramming adapter. By residing the prediction burden with the LLMs, a simpler linear decoder is applied to output future trajectories. The framework enables a quantitative analysis of the influence of multi-modal information, especially the impact of map semantics on trajectory prediction accuracy, and allows seamless integration of frozen LLMs with minimal adaptation, thereby demonstrating strong generalizability across diverse LLM architectures and providing a unified platform for model evaluation.

---


### 63. [Efficient Agent Evaluation via Diversity-Guided User Simulation](https://arxiv.org/abs/2604.21480)

**<font color=#1a73e8>作者：</font>** Itay Nakash, George Kour, Ateret Anaby-Tavor  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as customer-facing agents, yet evaluating their reliability remains challenging due to stochastic, multi-turn interactions. Current evaluation protocols rely on linear Monte Carlo rollouts of complete agent-user conversations to estimate success. However, this approach is computationally inefficient, repeatedly regenerating identical early prefixes, and often fails to uncover deep failure modes that arise from rare user behaviors.
We introduce DIVERT (Diversity-Induced Evaluation via Branching of Trajectories), an efficient, snapshot-based, coverage-guided user simulation framework for systematic exploration of agent-user interactions. DIVERT captures the full agent-environment state at critical decision points and resumes execution from these snapshots, enabling reuse of shared conversation prefixes and reducing redundant computation. From each junction, the framework branches using targeted, diversity-inducing user responses, allowing directed exploration of alternative interaction paths.
By focusing evaluation on semantically diverse and underexplored trajectories, DIVERT improves both efficiency and coverage. Empirical results show that it discovers more failures per token compared to standard linear rollout protocols, while expanding the set of tasks on which failures are identified.

---


### 64. [Generalizing Numerical Reasoning in Table Data through Operation Sketches and Self-Supervised Learning](https://arxiv.org/abs/2604.21495)

**<font color=#1a73e8>作者：</font>** Hanjun Cho, Gahyun Yoo, Hanseong Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Numerical reasoning over expert-domain tables often exhibits high in-domain accuracy but limited robustness to domain shift. Models trained with supervised fine-tuning (SFT) on specific datasets tend to rely on header-operation shortcuts rather than structural reasoning. We introduce TaNOS, a continual pre-training framework comprising three components: (i) header anonymization to reduce lexical memorization, (ii) operation sketches that provide minimal structural cues, and (iii) self-supervised pretraining that constructs correctness-guaranteed program-question pairs from given tables in a program-first manner. By decoupling domain semantics and numerical operation structure, TaNOS improves the transferability of numerical reasoning. Applied to an 8B instruction-tuned model, TaNOS achieves 80.13% execution accuracy on FinQA with only 10% train data, outperforming SFT baseline (73.97%) with full train data and proprietary models such as GPT-5, Gemini-2.5-Pro. Furthermore, in the domain-shift experiments, TaNOS displays nearly-negligible cross-domain gap (<2pp) when standard SFT shows over 10pp gap. These results suggest that structural guidance with operation sketches, header-agnostic representations, and correctness-guaranteed self-supervision can improve the robustness of numerical reasoning across diverse expert-domain tables.

---


### 65. [GeoMind: An Agentic Workflow for Lithology Classification with Reasoned Tool Invocation](https://arxiv.org/abs/2604.21501)

**<font color=#1a73e8>作者：</font>** Yitong Zhou, Mingyue Cheng, Jiahao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lithology classification in well logs is a fundamental geoscience data mining task that aims to infer rock types from multi dimensional geophysical sequences. Despite recent progress, existing approaches typically formulate the problem as a static, single-step discriminative mapping. This static paradigm limits evidence-based diagnostic reasoning against geological standards, often yielding predictions that are detached from geological reality due to a lack of domain priors. In this work, we propose GeoMind, a tool-augmented agentic framework that models lithology classification as a sequential reasoning process. GeoMind organizes its toolkit into perception, reasoning, and analysis modules, which respectively translate raw logs into semantic trends, infer lithology hypotheses from multi-source evidence, and verify predictions against stratigraphic constraints. A global planner adaptively coordinates these modules based on input characteristics, enabling geologically plausible and evidence-grounded decisions. To guarantee the logical consistency of GeoMind, we introduce a fine-grained process supervision strategy. Unlike standard methods that focus solely on final outcomes, our approach optimizes intermediate reasoning steps, ensuring the validity of decision trajectories and alignment to geological constraints. Experiments on four benchmark well-log datasets demonstrate that GeoMind consistently outperforms strong baselines in classification performance while providing transparent and traceable decision-making processes.

---


### 66. [OptiVerse: A Comprehensive Benchmark towards Optimization Problem Solving](https://arxiv.org/abs/2604.21510)

**<font color=#1a73e8>作者：</font>** Xinyu Zhang, Boxuan Zhang, Yuchen Wan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) demonstrate remarkable reasoning, complex optimization tasks remain challenging, requiring domain knowledge and robust implementation. However, existing benchmarks focus narrowly on Mathematical Programming and Combinatorial Optimization, hindering comprehensive evaluation. To address this, we introduce OptiVerse, a comprehensive benchmark of 1,000 curated problems spanning neglected domains, including Stochastic Optimization, Dynamic Optimization, Game Optimization, and Optimal Control, across three difficulty levels: Easy, Medium, and Hard. The experiments with 22 LLMs of different sizes reveal sharp performance degradation on hard problems, where even advanced models like GPT-5.2 and Gemini-3 struggle to exceed 27% accuracy. Through error analysis, we identify that modeling & logic errors remain the primary bottleneck. Consequently, we propose a Dual-View Auditor Agent that improves the accuracy of the LLM modeling process without introducing significant time overhead. OptiVerse will serve as a foundational platform for advancing LLMs in solving complex optimization challenges.

---


### 67. [Gmd: Gaussian mixture descriptor for pair matching of 3D fragments](https://arxiv.org/abs/2604.21519)

**<font color=#1a73e8>作者：</font>** Meijun Xiong, Zhenguo Shi, Xinyu Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the automatic reassembly of fragments acquired using laser scanners to reconstruct objects, a crucial step is the matching of fractured surfaces. In this paper, we propose a novel local descriptor that uses the Gaussian Mixture Model (GMM) to fit the distribution of points, allowing for the description and matching of fractured surfaces of fragments. Our method involves dividing a local surface patch into concave and convex regions for estimating the k value of GMM. Then the final Gaussian Mixture Descriptor (GMD) of the fractured surface is formed by merging the regional GMDs. To measure the similarities between GMDs for determining adjacent fragments, we employ the L2 distance and align the fragments using Random Sample Consensus (RANSAC) and Iterative Closest Point (ICP). The extensive experiments on real-scanned public datasets and Terracotta datasets demonstrate the effectiveness of our approach; furthermore, the comparisons with several existing methods also validate the advantage of the proposed method.

---


### 68. [Seeing Isn't Believing: Uncovering Blind Spots in Evaluator Vision-Language Models](https://arxiv.org/abs/2604.21523)

**<font color=#1a73e8>作者：</font>** Mohammed Safi Ur Rahman Khan, Sanjay Suryanarayanan, Tushar Anand 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (VLMs) are increasingly used to evaluate outputs of other models, for image-to-text (I2T) tasks such as visual question answering, and text-to-image (T2I) generation tasks. Despite this growing reliance, the reliability of these Evaluator VLMs remains under explored. In this work, we systematically evaluate the reliability of Evaluator VLMs across both I2T and T2I tasks. We introduce targeted perturbations that degrade output quality along key error dimensions, including object hallucinations, spatial reasoning, factual grounding, and visual fidelity. These perturbations test whether Evaluator VLMs can reliably account for these quality degrading errors in their evaluations. Using a comprehensive benchmark of over 4000 perturbed instances spanning 40 perturbation dimensions, we evaluate 4 prominent VLMs using single-answer scoring, pairwise comparison, and reference-guided paradigms. Our findings reveal that current VLM evaluators exhibit substantial blind spots: they often fail to detect perturbed outputs - in some cases exceeding 50%, struggle particularly with fine-grained compositional and spatial errors, and are often insensitive to hallucinated content that contradicts the input image. Pairwise comparison proves more reliable, though failure rates persist. These results highlight the unreliable nature of current Evaluator VLMs and urge caution in their deployment for benchmarking and development decisions. Code and data have been made publicly available.

---


### 69. [Job Skill Extraction via LLM-Centric Multi-Module Framework](https://arxiv.org/abs/2604.21525)

**<font color=#1a73e8>作者：</font>** Guojing Li, Zichuan Fu, Junyi Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Span-level skill extraction from job advertisements underpins candidate-job matching and labor-market analytics, yet generative large language models (LLMs) often yield malformed spans, boundary drift, and hallucinations, especially with long-tail terms and cross-domain shift. We present SRICL, an LLM-centric framework that combines semantic retrieval (SR), in-context learning (ICL), and supervised fine-tuning (SFT) with a deterministic verifier. SR pulls in-domain annotated sentences and definitions from ESCO to form format-constrained prompts that stabilize boundaries and handle coordination. SFT aligns output behavior, while the verifier enforces pairing, non-overlap, and BIO legality with minimal retries. On six public span-labeled corpora of job-ad sentences across sectors and languages, SRICL achieves substantial STRICT-F1 improvements over GPT-3.5 prompting baselines and sharply reduces invalid tags and hallucinated spans, enabling dependable sentence-level deployment in low-resource, multi-domain settings.

---


### 70. [Attention-based multiple instance learning for predominant growth pattern prediction in lung adenocarcinoma wsi using foundation models](https://arxiv.org/abs/2604.21530)

**<font color=#1a73e8>作者：</font>** Laura Valeria Perez-Herrera, M.J. Garcia-Gonzalez, Karen Lopez-Linares  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lung adenocarcinoma (LUAD) grading depends on accurately identifying growth patterns, which are indicators of prognosis and can influence treatment decisions. Common deep learning approaches to determine the predominant pattern rely on patch-level classification or segmentation, requiring extensive annotations. This study proposes an attention-based multiple instance learning (ABMIL) framework to predict the predominant LUAD growth pattern at the whole slide level to reduce annotation burden. Our approach integrates pretrained pathology foundation models as patch encoders, used either frozen or fine-tuned on annotated patches, to extract discriminative features that are aggregated through attention mechanisms. Experiments show that fine-tuned encoders improve performance, with Prov-GigaPath achieving the highest agreement (\k{appa} = 0.699) under ABMIL. Compared to simple patch-aggregation baselines, ABMIL yields more robust predictions by leveraging slide-level supervision and spatial attention. Future work will extend this framework to estimate the full distribution of growth patterns and validate performance on external cohorts.

---


### 71. [Unbiased Prevalence Estimation with Multicalibrated LLMs](https://arxiv.org/abs/2604.21549)

**<font color=#1a73e8>作者：</font>** Fridolin Linder, Thomas Leeper, Daniel Haimovich 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Estimating the prevalence of a category in a population using imperfect measurement devices (diagnostic tests, classifiers, or large language models) is fundamental to science, public health, and online trust and safety. Standard approaches correct for known device error rates but assume these rates remain stable across populations. We show this assumption fails under covariate shift and that multicalibration, which enforces calibration conditional on the input features rather than just on average, is sufficient for unbiased prevalence estimation under such shift. Standard calibration and quantification methods fail to provide this guarantee. Our work connects recent theoretical work on fairness to a longstanding measurement problem spanning nearly all academic disciplines. A simulation confirms that standard methods exhibit bias growing with shift magnitude, while a multicalibrated estimator maintains near-zero bias. While we focus the discussion mostly on LLMs, our theoretical results apply to any classification model. Two empirical applications -- estimating employment prevalence across U.S. states using the American Community Survey, and classifying political texts across four countries using an LLM -- demonstrate that multicalibration substantially reduces bias in practice, while highlighting that calibration data should cover the key feature dimensions along which target populations may differ.

---


### 72. [Measuring Opinion Bias and Sycophancy via LLM-based Coercion](https://arxiv.org/abs/2604.21564)

**<font color=#1a73e8>作者：</font>** Rodrigo Nogueira, Giovana Kerche Bonás, Thales Sales Almeida 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly shape the information people consume: they are embedded in search, consulted for professional advice, deployed as agents, and used as a first stop for questions about policy, ethics, health, and politics. When such a model silently holds a position on a contested topic, that position propagates at scale into users' decisions. Eliciting a model's positions is harder than it first appears: contemporary assistants answer direct opinion questions with evasive disclaimers, and the same model may concede the opposite position once the user starts arguing one side. We propose a method, released as the open-source llm-bias-bench, for discovering the opinions an LLM actually holds on contested topics under conditions that resemble real multi-turn interaction. The method pairs two complementary free-form probes. Direct probing asks for the model's opinion across five turns of escalating pressure from a simulated user. Indirect probing never asks for an opinion and engages the model in argumentative debate, letting bias leak through how it concedes, resists, or counter-argues. Three user personas (neutral, agree, disagree) collapse into a nine-way behavioral classification that separates persona-independent positions from persona-dependent sycophancy, and an auditable LLM judge produces verdicts with textual evidence. The first instantiation ships 38 topics in Brazilian Portuguese across values, scientific consensus, philosophy, and economic policy. Applied to 13 assistants, the method surfaces findings of practical interest: argumentative debate triggers sycophancy 2-3x more than direct questioning (median 50% to 79%); models that look opinionated under direct questioning often collapse into mirroring under sustained arguments; and attacker capability matters mainly when an existing opinion must be dislodged, not when the assistant starts neutral.

---


### 73. [Separable Expert Architecture: Toward Privacy-Preserving LLM Personalization via Composable Adapters and Deletable User Proxies](https://arxiv.org/abs/2604.21571)

**<font color=#1a73e8>作者：</font>** Chris Schneider, Philipp Schoenegger, Ben Bariach  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current model training approaches incorporate user information directly into shared weights, making individual data removal computationally infeasible without retraining. This paper presents a three-layer architecture that decouples personal data from shared weights by combining a static base model, composable domain-expert LoRA adapters that shape behavior without imparting user data, and per-user proxy artefacts whose deletion constitutes deterministic unlearning. Evaluation on Phi-3.5-mini and Llama-3.1-8B confirms per-user differentiation in which personal data influences outputs while remaining isolated, verified by a return to baseline after proxy removal (KL divergence of approximately 0.21 nats, 82-89% verification pass rate) and near-zero cross-user contamination. Because user-specific information never enters shared weights, the architecture mitigates model inversion, membership inference, and training-data extraction against shared model components by construction. The approach converts machine unlearning from an intractable weight-editing problem into a deterministic deletion operation that preserves personalization alongside privacy-enhancing guarantees and is compatible with differentially private stochastic gradient descent (DP-SGD) for privacy-preserving shared model improvement.

---


### 74. [CoFEE: Reasoning Control for LLM-Based Feature Discovery](https://arxiv.org/abs/2604.21584)

**<font color=#1a73e8>作者：</font>** Maximilian Westermann, Ben Griffin, Aaron Ontoyin Yin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Feature discovery from complex unstructured data is fundamentally a reasoning problem: it requires identifying abstractions that are predictive of a target outcome while avoiding leakage, proxies, and post-outcome signals. With the introduction of ever-improving Large Language Models (LLMs), our method provides a structured method for addressing this challenge. LLMs are well suited for this task by being able to process large amounts of information, but unconstrained feature generation can lead to weak features. In this work, we study reasoning control in LLMs by inducing cognitive behaviors for improving feature discovery. We introduce CoFEE (Cognitive Feature Engineering Engine), a reasoning control framework that enforces cognitive behaviors in how the LLM reasons during feature discovery. From a machine learning perspective, these cognitive behaviors act as structured inductive biases over the space of candidate features generated by the model. These behaviors have been exploited with success in ML models, and include backward chaining from outcomes, subgoal decomposition, verification against observability and leakage criteria, and explicit backtracking of rejected reasoning paths. In a controlled comparison, we show that enforcing cognitive behaviors yields features with higher empirical predictability than those under unconstrained vanilla LLM prompts. CoFEE achieves an average Success Rate Score that is 15.2% higher than the vanilla approach, while generating 29% fewer features and reducing costs by 53.3%. Using held-out feature evaluation, we assess whether cognitively induced features generalize beyond the data used for discovery. Our results indicate that, in our evaluated setting, reasoning control is associated with improvements in quality and efficiency of LLM-based feature discovery.

---


### 75. [AgenticQwen: Training Small Agentic Language Models with Dual Data Flywheels for Industrial-Scale Tool Use](https://arxiv.org/abs/2604.21590)

**<font color=#1a73e8>作者：</font>** Yuanjie Lyu, Chengyu Wang, Haonan Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern industrial applications increasingly demand language models that act as agents, capable of multi-step reasoning and tool use in real-world settings. These tasks are typically performed under strict cost and latency constraints, making small agentic models highly desirable. In this paper, we introduce the AgenticQwen family of models, trained via multi-round reinforcement learning (RL) on synthetic data and a limited amount of open-source data. Our training framework combines reasoning RL and agentic RL with dual data flywheels that automatically generate increasingly challenging tasks. The reasoning flywheel increases task difficulty by learning from errors, while the agentic flywheel expands linear workflows into multi-branch behavior trees that better reflect the decision complexity of real-world applications. We validate AgenticQwen on public benchmarks and in an industrial agent system. The models achieve strong performance on multiple agentic benchmarks, and in our industrial agent system, close the gap with much larger models on search and data analysis tasks. Model checkpoints and part of the synthetic data: this https URL. Data synthesis and RL training code: this https URL. The data synthesis pipeline is also integrated into EasyDistill: this https URL.

---


### 76. [Process Supervision via Verbal Critique Improves Reasoning in Large Language Models](https://arxiv.org/abs/2604.21611)

**<font color=#1a73e8>作者：</font>** Hao-Yuan Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Inference-time scaling for LLM reasoning has focused on three axes: chain depth, sample breadth, and learned step-scorers (PRMs). We introduce a fourth axis, granularity of external verbal supervision, via Verbal Process Supervision (VPS), a training-free framework that uses structured natural-language critique from a stronger supervisor to guide an iterative generate-critique-refine loop up to a round budget R. Across GPQA Diamond, AIME 2025, and LiveCodeBench V6 (covering both closed and open models), VPS yields three key results. First, on GPQA Diamond, GPT-5.4 (High) | GPT-5.4 (Low) reaches 94.9% at R=4, surpassing the 94.1% state of the art without gradient updates. Second, on AIME 2025, VPS enables strong weak-actor rescue, boosting scores from 11.7-26.7% to 63.3-90.0% (up to +63.3 points). Third, at matched compute, VPS outperforms Reflexion by +8.5 to +12.1 points and Self-Consistency@5 by +5.0 pp (GPQA) and +8.3 pp (LiveCodeBench), isolating critique granularity as the key driver. Performance scales with the supervisor-actor capability gap (Pearson r=0.90) and degrades when errors are not linguistically expressible (e.g., code synthesis), motivating hybrid verbal-executable methods. These results establish critique granularity as a new axis of inference-time scaling.

---


### 77. [Multilinguality at the Edge: Developing Language Models for the Global South](https://arxiv.org/abs/2604.21637)

**<font color=#1a73e8>作者：</font>** Lester James V. Miranda, Songbo Hu, Roi Reichart 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Where and how language models (LMs) are deployed determines who can benefit from them. However, there are several challenges that prevent effective deployment of LMs in non-English-speaking and hardware constrained communities in the Global South. We call this challenge the last mile: the intersection of multilinguality and edge deployment, where the goals are aligned but the technical requirements often compete. Studying these two fields together is both a need, as linguistically diverse communities often face the most severe infrastructure constraints, and an opportunity, as edge and multilingual NLP research remain largely siloed. To understand the state of the art and the challenges of combining the two areas, we survey 232 papers that tackle this problem across the language modelling pipeline, from data collection to development and deployment. We also discuss open questions and provide actionable recommendations for different stakeholders in the NLP ecosystem. Finally, we hope that this work contributes to the development of inclusive and equitable language technologies.

---


### 78. [Encoder-Free Human Motion Understanding via Structured Motion Descriptions](https://arxiv.org/abs/2604.21668)

**<font color=#1a73e8>作者：</font>** Yao Zhang, Zhuchenyang Liu, Thomas Ploetz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The world knowledge and reasoning capabilities of text-based large language models (LLMs) are advancing rapidly, yet current approaches to human motion understanding, including motion question answering and captioning, have not fully exploited these capabilities. Existing LLM-based methods typically learn motion-language alignment through dedicated encoders that project motion features into the LLM's embedding space, remaining constrained by cross-modal representation and alignment. Inspired by biomechanical analysis, where joint angles and body-part kinematics have long served as a precise descriptive language for human movement, we propose \textbf{Structured Motion Description (SMD)}, a rule-based, deterministic approach that converts joint position sequences into structured natural language descriptions of joint angles, body part movements, and global trajectory. By representing motion as text, SMD enables LLMs to apply their pretrained knowledge of body parts, spatial directions, and movement semantics directly to motion reasoning, without requiring learned encoders or alignment modules. We show that this approach goes beyond state-of-the-art results on both motion question answering (66.7\% on BABEL-QA, 90.1\% on HuMMan-QA) and motion captioning (R@1 of 0.584, CIDEr of 53.16 on HumanML3D), surpassing all prior methods. SMD additionally offers practical benefits: the same text input works across different LLMs with only lightweight LoRA adaptation (validated on 8 LLMs from 6 model families), and its human-readable representation enables interpretable attention analysis over motion descriptions. Code, data, and pretrained LoRA adapters are available at this https URL.

---


### 79. [WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686)

**<font color=#1a73e8>作者：</font>** Xiaojie Xu, Zhengyuan Lin, Kang He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video generation models such as Genie, YUME, HY-World, and Matrix-Game are advancing rapidly, yet every model is evaluated on its own benchmark with private scenes and trajectories, making fair cross-model comparison impossible. Existing public benchmarks offer useful metrics such as trajectory error, aesthetic scores, and VLM-based judgments, but none supplies the standardized test conditions -- identical scenes, identical action sequences, and a unified control interface -- needed to make those metrics comparable across models with heterogeneous inputs. We introduce WorldMark, the first benchmark that provides such a common playing field for interactive Image-to-Video world models. WorldMark contributes: (1) a unified action-mapping layer that translates a shared WASD-style action vocabulary into each model's native control format, enabling apples-to-apples comparison across six major models on identical scenes and trajectories; (2) a hierarchical test suite of 500 evaluation cases covering first- and third-person viewpoints, photorealistic and stylized scenes, and three difficulty tiers from Easy to Hard spanning 20-60s; and (3) a modular evaluation toolkit for Visual Quality, Control Alignment, and World Consistency, designed so that researchers can reuse our standardized inputs while plugging in their own metrics as the field evolves. We will release all data, evaluation code, and model outputs to facilitate future research. Beyond offline metrics, we launch World Model Arena (this http URL), an online platform where anyone can pit leading world models against each other in side-by-side battles and watch the live leaderboard.

---


### 80. [Evaluating Post-hoc Explanations of the Transformer-based Genome Language Model DNABERT-2](https://arxiv.org/abs/2604.21690)

**<font color=#1a73e8>作者：</font>** Isabel Kurth, Paulo Yanez Sarmiento, Bernhard Y. Renard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explaining deep neural network predictions on genome sequences enables biological insight and hypothesis generation-often of greater interest than predictive performance alone. While explanations of convolutional neural networks (CNNs) have been shown to capture relevant patterns in genome sequences, it is unclear whether this transfers to more expressive Transformer-based genome language models (gLMs). To answer this question, we adapt AttnLRP, an extension of layer-wise relevance propagation to the attention mechanism, and apply it to the state-of-the-art gLM DNABERT-2. Thereby, we propose strategies to transfer explanations from token and nucleotide level. We evaluate the adaption of AttnLRP on genomic datasets using multiple metrics. Further, we provide an extensive comparison between the explanations of DNABERT-2 and a baseline CNN. Our results demonstrate that AttnLRP yields reliable explanations corresponding to known biological patterns. Hence, like CNNs, gLMs can also help derive biological insights. This work contributes to the explainability of gLMs and addresses the comparability of relevance attributions across different architectures.

---


### 81. [Building a Precise Video Language with Human-AI Oversight](https://arxiv.org/abs/2604.21718)

**<font color=#1a73e8>作者：</font>** Zhiqiu Lin, Chancharik Mitra, Siyuan Cen 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-language models (VLMs) learn to reason about the dynamic visual world through natural language. We introduce a suite of open datasets, benchmarks, and recipes for scalable oversight that enable precise video captioning. First, we define a structured specification for describing subjects, scenes, motion, spatial, and camera dynamics, grounded by hundreds of carefully defined visual primitives developed with professional video creators such as filmmakers. Next, to curate high-quality captions, we introduce CHAI (Critique-based Human-AI Oversight), a framework where trained experts critique and revise model-generated pre-captions into improved post-captions. This division of labor improves annotation accuracy and efficiency by offloading text generation to models, allowing humans to better focus on verification. Additionally, these critiques and preferences between pre- and post-captions provide rich supervision for improving open-source models (Qwen3-VL) on caption generation, reward modeling, and critique generation through SFT, DPO, and inference-time scaling. Our ablations show that critique quality in precision, recall, and constructiveness, ensured by our oversight framework, directly governs downstream performance. With modest expert supervision, the resulting model outperforms closed-source models such as Gemini-3.1-Pro. Finally, we apply our approach to re-caption large-scale professional videos (e.g., films, commercials, games) and fine-tune video generation models such as Wan to better follow detailed prompts of up to 400 words, achieving finer control over cinematography including camera motion, angle, lens, focus, point of view, and framing. Our results show that precise specification and human-AI oversight are key to professional-level video understanding and generation. Data and code are available on our project page: this https URL

---


### 82. [Ramen: Robust Test-Time Adaptation of Vision-Language Models with Active Sample Selection](https://arxiv.org/abs/2604.21728)

**<font color=#1a73e8>作者：</font>** Wenxuan Bao, Yanjun Zhao, Xiyuan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained vision-language models such as CLIP exhibit strong zero-shot generalization but remain sensitive to distribution shifts. Test-time adaptation adapts models during inference without access to source data or target labels, offering a practical way to handle such shifts. However, existing methods typically assume that test samples come from a single, consistent domain, while in practice, test data often include samples from mixed domains with distinct characteristics. Consequently, their performance degrades under mixed-domain settings. To address this, we present Ramen, a framework for robust test-time adaptation through active sample selection. For each incoming test sample, Ramen retrieves a customized batch of relevant samples from previously seen data based on two criteria: domain consistency, which ensures that adaptation focuses on data from similar domains, and prediction balance, which mitigates adaptation bias caused by skewed predictions. To improve efficiency, Ramen employs an embedding-gradient cache that stores the embeddings and sample-level gradients of past test images. The stored embeddings are used to retrieve relevant samples, and the corresponding gradients are aggregated for model updates, eliminating the need for any additional forward or backward passes. Our theoretical analysis provides insight into why the proposed adaptation mechanism is effective under mixed-domain shifts. Experiments on multiple image corruption and domain-shift benchmarks demonstrate that Ramen achieves strong and consistent performance, offering robust and efficient adaptation in complex mixed-domain scenarios. Our code is available at this https URL .

---


### 83. [StructMem: Structured Memory for Long-Horizon Behavior in LLMs](https://arxiv.org/abs/2604.21748)

**<font color=#1a73e8>作者：</font>** Buqiang Xu, Yijun Chen, Jizhan Fang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term conversational agents need memory systems that capture relationships between events, not merely isolated facts, to support temporal reasoning and multi-hop question answering. Current approaches face a fundamental trade-off: flat memory is efficient but fails to model relational structure, while graph-based memory enables structured reasoning at the cost of expensive and fragile construction. To address these issues, we propose \textbf{StructMem}, a structure-enriched hierarchical memory framework that preserves event-level bindings and induces cross-event connections. By temporally anchoring dual perspectives and performing periodic semantic consolidation, StructMem improves temporal reasoning and multi-hop performance on \texttt{LoCoMo}, while substantially reducing token usage, API calls, and runtime compared to prior memory systems, see this https URL .

---


### 84. [Why are all LLMs Obsessed with Japanese Culture? On the Hidden Cultural and Regional Biases of LLMs](https://arxiv.org/abs/2604.21751)

**<font color=#1a73e8>作者：</font>** Joseba Fernandez de Landa, Carla Perez-Almendros, Jose Camacho-Collados  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs have been showing limitations when it comes to cultural coverage and competence, and in some cases show regional biases such as amplifying Western and Anglocentric viewpoints. While there have been works analysing the cultural capabilities of LLMs, there has not been specific work on highlighting LLM regional preferences when it comes to cultural-related questions. In this work, we propose a new dataset based on a comprehensive taxonomy of Culture-Related Open Questions (CROQ). The results show that, contrary to previous cultural bias work, LLMs show a clear tendency towards countries such as Japan. Moveover, our results show that when prompting in languages such as English or other high-resource ones, LLMs tend to provide more diverse outputs and show less inclinations towards answering questions highlighting countries for which the input language is an official language. Finally, we also investigate at which point of LLM training this cultural bias emerges, with our results suggesting that the first clear signs appear after supervised fine-tuning, and not during pre-training.

---


### 85. [Who Defines "Best"? Towards Interactive, User-Defined Evaluation of LLM Leaderboards](https://arxiv.org/abs/2604.21769)

**<font color=#1a73e8>作者：</font>** Minji Jung, Minjae Lee, Yejin Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM leaderboards are widely used to compare models and guide deployment decisions. However, leaderboard rankings are shaped by evaluation priorities set by benchmark designers, rather than by the diverse goals and constraints of actual users and organizations. A single aggregate score often obscures how models behave across different prompt types and compositions. In this work, we conduct an in-depth analysis of the dataset used in the LMArena (formerly Chatbot Arena) benchmark and investigate this evaluation challenge by designing an interactive visualization interface as a design probe. Our analysis reveals that the dataset is heavily skewed toward certain topics, that model rankings vary across prompt slices, and that preference-based judgments are used in ways that blur their intended scope. Building on this analysis, we introduce a visualization interface that allows users to define their own evaluation priorities by selecting and weighting prompt slices and to explore how rankings change accordingly. A qualitative study suggests that this interactive approach improves transparency and supports more context-specific model evaluation, pointing toward alternative ways to design and use LLM leaderboards.

---


### 86. [Agentic AI-Enabled Framework for Thermal Comfort and Building Energy Assessment in Tropical Urban Neighborhoods](https://arxiv.org/abs/2604.21787)

**<font color=#1a73e8>作者：</font>** Po-Yen Lai, Xinyu Yang, Derrick Low 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In response to the urban heat island effects and building energy demands in Singapore, this study proposes an agentic AI-enabled reasoning framework that integrates large language models (LLMs) with lightweight physics-based models. Through prompt customization, the LLMs interpret urban design tasks, extract relevant policies, and activate appropriate physics-based models for evaluation, forming a closed-loop reasoning-action process. These lightweight physics-based models leverage core thermal and airflow principles, streamlining conventional models to reduce computational time while predicting microclimate variables, such as building surface temperature, ground radiant heat, and airflow conditions, thereby enabling the estimation of thermal comfort indices, e.g., physiological equivalent temperature (PET), and building energy usage. This framework allows users to explore a variety of climate-resilient building surface strategies, e.g., green façades and cool paint applications, that improve thermal comfort while reducing wall heat gain and energy demand. By combining the autonomous reasoning capacity of LLMs with the rapid quantitative evaluation of lightweight physics-based models, the proposed system demonstrates potential for cross-disciplinary applications in sustainable urban design, indoor-outdoor environmental integration, and climate adaptation planning. The source code and data used in this study are available at: this https URL.

---


### 87. [Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows](https://arxiv.org/abs/2604.21816)

**<font color=#1a73e8>作者：</font>** Anuj Sadani, Deepak Kumar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) has become a common interface for connecting large language model (LLM) agents to external tools, but its reliance on stateless, eager schema injection imposes a hidden per-turn overhead the MCP Tax or Tools Tax that practitioner reports place between roughly 10k and 60k tokens in typical multi-server deployments. This payload inflates the key-value cache, is associated with reasoning degradation as context utilization approaches published fracture points around 70%, and turns token budgets into a recurring operational cost. We introduce Tool Attention, a middleware-layer mechanism that generalizes the "Attention Is All You Need" paradigm from self-attention over tokens to gated attention over tools. Tool Attention combines (i) an Intent Schema Overlap (ISO) score from sentence embeddings, (ii) a state-aware gating function enforcing preconditions and access scopes, and (iii) a two-phase lazy schema loader that keeps a compact summary pool in context and promotes full JSON schemas only for top-k gated tools. We evaluate on a simulated 120-tool, six-server benchmark whose per-server token counts are calibrated to public audits of real MCP deployments. In this simulation, Tool Attention directly reduces measured per-turn tool tokens by 95.0% (47.3k -> 2.4k) and raises effective context utilization (a token-ratio quantity) from 24% to 91%. End-to-end figures for task success, latency, cost, and reasoning quality are reported as projections derived from the measured token counts combined with published deployment telemetry; they are not measured on live LLM agents, and we mark projected values explicitly throughout. Taken together, the results support a simple thesis: protocol-level efficiency, not raw context length, is a binding constraint on scalable gentic systems. The code for this work is accessible at this https URL

---


### 88. [Alignment has a Fantasia Problem](https://arxiv.org/abs/2604.21827)

**<font color=#1a73e8>作者：</font>** Nathanael Jo, Zoe De Simone, Mitchell Gordon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern AI assistants are trained to follow instructions, implicitly assuming that users can clearly articulate their goals and the kind of assistance they need. Decades of behavioral research, however, show that people often engage with AI systems before their goals are fully formed. When AI systems treat prompts as complete expressions of intent, they can appear to be useful or convenient, but not necessarily aligned with the users' needs. We call these failures Fantasia interactions. We argue that Fantasia interactions demand a rethinking of alignment research: rather than treating users as rational oracles, AI should provide cognitive support by actively helping users form and refine their intent through time. This requires an interdisciplinary approach that bridges machine learning, interface design, and behavioral science. We synthesize insights from these fields to characterize the mechanisms and failures of Fantasia interactions. We then show why existing interventions are insufficient, and propose a research agenda for designing and evaluating AI systems that better help humans navigate uncertainty in their tasks.

---


### 89. [Machine Behavior in Relational Moral Dilemmas: Moral Rightness, Predicted Human Behavior, and Model Decisions](https://arxiv.org/abs/2604.21871)

**<font color=#1a73e8>作者：</font>** Jiseon Kim, Jea Kwon, Luiz Felipe Vecchietti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human moral judgment is context-dependent and modulated by interpersonal relationships. As large language models (LLMs) increasingly function as decision-support systems, determining whether they encode these social nuances is critical. We characterize machine behavior using the Whistleblower's Dilemma by varying two experimental dimensions: crime severity and relational closeness. Our study evaluates three distinct perspectives: (1) moral rightness (prescriptive norms), (2) predicted human behavior (descriptive social expectations), and (3) autonomous model decision-making. By analyzing the reasoning processes, we identify a clear cross-perspective divergence: while moral rightness remains consistently fairness-oriented, predicted human behavior shifts significantly toward loyalty as relational closeness increases. Crucially, model decisions align with moral rightness judgments rather than their own behavioral predictions. This inconsistency suggests that LLM decision-making prioritizes rigid, prescriptive rules over the social sensitivity present in their internal world-modeling, which poses a gap that may lead to significant misalignments in real-world deployments.

---


### 90. [Revisiting Non-Verbatim Memorization in Large Language Models: The Role of Entity Surface Forms](https://arxiv.org/abs/2604.21882)

**<font color=#1a73e8>作者：</font>** Yuto Nishida, Naoki Shikoda, Yosuke Kishinami 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding what kinds of factual knowledge large language models (LLMs) memorize is essential for evaluating their reliability and limitations. Entity-based QA is a common framework for analyzing non-verbatim memorization, but typical evaluations query each entity using a single canonical surface form, making it difficult to disentangle fact memorization from access through a particular name. We introduce RedirectQA, an entity-based QA dataset that uses Wikipedia redirect information to associate Wikidata factual triples with categorized surface forms for each entity, including alternative names, abbreviations, spelling variants, and common erroneous forms. Across 13 LLMs, we examine surface-conditioned factual memorization and find that prediction outcomes often change when only the entity surface form changes. This inconsistency is category-dependent: models are more robust to minor orthographic variations than to larger lexical variations such as aliases and abbreviations. Frequency analyses further suggest that both entity- and surface-level frequencies are associated with accuracy, and that entity frequency often contributes beyond surface frequency. Overall, factual memorization appears neither purely surface-specific nor fully surface-invariant, highlighting the importance of surface-form diversity in evaluating non-verbatim memorization.

---


### 91. [A Multimodal Text- and Graph-Based Approach for Open-Domain Event Extraction from Documents](https://arxiv.org/abs/2604.21885)

**<font color=#1a73e8>作者：</font>** Praval Sharma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Event extraction is essential for event understanding and analysis. It supports tasks such as document summarization and decision-making in emergency scenarios. However, existing event extraction approaches have limitations: (1) closed-domain algorithms are restricted to predefined event types and thus rarely generalize to unseen types and (2) open-domain event extraction algorithms, capable of handling unconstrained event types, have largely overlooked the potential of large language models (LLMs) despite their advanced abilities. Additionally, they do not explicitly model document-level contextual, structural, and semantic reasoning, which are crucial for effective event extraction but remain challenging for LLMs due to lost-in-the-middle phenomenon and attention dilution. To address these limitations, we propose multimodal open-domain event extraction, MODEE , a novel approach for open-domain event extraction that combines graph-based learning with text-based representation from LLMs to model document-level reasoning. Empirical evaluations on large datasets demonstrate that MODEE outperforms state-of-the-art open-domain event extraction approaches and can be generalized to closed-domain event extraction, where it outperforms existing algorithms.

---


### 92. [Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with Large Language Models](https://arxiv.org/abs/2604.21896)

**<font color=#1a73e8>作者：</font>** Chee Wei Tan, Yuchen Wang, Shangxin Guo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces a new paradigm for AI game programming, leveraging large language models (LLMs) to extend and operationalize Claude Shannon's taxonomy of game-playing machines. Central to this paradigm is Nemobot, an interactive agentic engineering environment that enables users to create, customize, and deploy LLM-powered game agents while actively engaging with AI-driven strategies. The LLM-based chatbot, integrated within Nemobot, demonstrates its capabilities across four distinct classes of games. For dictionary-based games, it compresses state-action mappings into efficient, generalized models for rapid adaptability. In rigorously solvable games, it employs mathematical reasoning to compute optimal strategies and generates human-readable explanations for its decisions. For heuristic-based games, it synthesizes strategies by combining insights from classical minimax algorithms (see, e.g., shannon1950chess) with crowd-sourced data. Finally, in learning-based games, it utilizes reinforcement learning with human feedback and self-critique to iteratively refine strategies through trial-and-error and imitation learning. Nemobot amplifies this framework by offering a programmable environment where users can experiment with tool-augmented generation and fine-tuning of strategic game agents. From strategic games to role-playing games, Nemobot demonstrates how AI agents can achieve a form of self-programming by integrating crowdsourced learning and human creativity to iteratively refine their own logic. This represents a step toward the long-term goal of self-programming AI.

---


### 93. [From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation](https://arxiv.org/abs/2604.21910)

**<font color=#1a73e8>作者：</font>** Bartosz Balis, Michal Orzechowski, Piotr Kica 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research questions into workflow specifications, a task requiring both domain knowledge and infrastructure expertise. We propose an agentic architecture that closes this gap through three layers: an LLM interprets natural language into structured intents (semantic layer); validated generators produce reproducible workflow DAGs (deterministic layer); and domain experts author ``Skills'': markdown documents encoding vocabulary mappings, parameter constraints, and optimization strategies (knowledge layer). This decomposition confines LLM non-determinism to intent extraction: identical intents always yield identical workflows. We implement and evaluate the architecture on the 1000 Genomes population genetics workflow and Hyperflow WMS running on Kubernetes. In an ablation study on 150 queries, Skills raise full-match intent accuracy from 44% to 83%; skill-driven deferred workflow generation reduces data transfer by 92\%; and the end-to-end pipeline completes queries on Kubernetes with LLM overhead below 15 seconds and cost under $0.001 per query.

---


### 94. [When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs](https://arxiv.org/abs/2604.21911)

**<font color=#1a73e8>作者：</font>** Pegah Khayatan, Jayneel Parekh, Arnaud Dapogny 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite impressive progress in capabilities of large vision-language models (LVLMs), these systems remain vulnerable to hallucinations, i.e., outputs that are not grounded in the visual input. Prior work has attributed hallucinations in LVLMs to factors such as limitations of the vision backbone or the dominance of the language component, yet the relative importance of these factors remains unclear. To resolve this ambiguity, We propose HalluScope, a benchmark to better understand the extent to which different factors induce hallucinations. Our analysis indicates that hallucinations largely stem from excessive reliance on textual priors and background knowledge, especially information introduced through textual instructions. To mitigate hallucinations induced by textual instruction priors, we propose HalluVL-DPO, a framework for fine-tuning off-the-shelf LVLMs towards more visually grounded responses. HalluVL-DPO leverages preference optimization using a curated training dataset that we construct, guiding the model to prefer grounded responses over hallucinated ones. We demonstrate that our optimized model effectively mitigates the targeted hallucination failure mode, while preserving or improving performance on other hallucination benchmarks and visual capability evaluations. To support reproducibility and further research, we will publicly release our evaluation benchmark, preference training dataset, and code at this https URL .

---


### 95. [MathDuels: Evaluating LLMs as Problem Posers and Solvers](https://arxiv.org/abs/2604.21916)

**<font color=#1a73e8>作者：</font>** Zhiqiu Xu, Shibo Jin, Shreya Arya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As frontier language models attain near-ceiling performance on static mathematical benchmarks, existing evaluations are increasingly unable to differentiate model capabilities, largely because they cast models solely as solvers of fixed problem sets. We introduce MathDuels, a self-play benchmark in which models occupy dual roles: each authors math problems under adversarial prompting and solves problems authored by every other participant. Problems are produced through a three-stage generation pipeline (meta-prompting, problem generation, and difficulty amplification), and validated by an independent verifier that excludes ill-posed questions. A Rasch model (Rasch, 1993) jointly estimates solver abilities and problem difficulties; author quality is derived from the difficulties of each model's authored problems. Experiments across 19 frontier models reveal that authoring and solving capabilities are partially decoupled, and that dual-role evaluation reveals capability separations invisible in single-role benchmarks. As newer models enter the arena, they produce problems that defeat previously dominant solvers, so the benchmark's difficulty co-evolves with participant strength rather than saturating at a fixed ceiling. We host a public leaderboard that updates as new models are released.

---


### 96. [Fine-Tuning Regimes Define Distinct Continual Learning Problems](https://arxiv.org/abs/2604.21927)

**<font color=#1a73e8>作者：</font>** Paul-Tiberiu Iordache, Elena Burceanu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.

---


### 97. [Evaluation of Automatic Speech Recognition Using Generative Large Language Models](https://arxiv.org/abs/2604.21928)

**<font color=#1a73e8>作者：</font>** Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.

---


> [!TIP]
> 当前位于：**51-97**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-97**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
