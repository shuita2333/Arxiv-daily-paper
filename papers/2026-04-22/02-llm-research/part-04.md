# 🧠 大模型相关研究 | 2026年04月22日

> 本类共 **353** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

---

### 151. [Continual Safety Alignment via Gradient-Based Sample Selection](https://arxiv.org/abs/2604.17215)

**<font color=#1a73e8>作者：</font>** Thong Bach, Dung Nguyen, Thao Minh Le 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models require continuous adaptation to new tasks while preserving safety alignment. However, fine-tuning on even benign data often compromises safety behaviors, including refusal of harmful requests, truthfulness, and commonsense reasoning. We investigate which training samples cause alignment drift through a data-centric lens. Our empirical analysis shows samples contribute unequally: high-gradient samples cause greater safety degradation and drive models toward pretrained distributions, while moderate-gradient samples enable task learning with minimal alignment loss. We propose gradient-based sample selection that filters high-gradient samples during fine-tuning. Across multiple model families on continual domain tasks, our method substantially improves alignment preservation while maintaining competitive task performance, without requiring curated safe data or architectural modifications. Our method is robust across selection ratios, task orderings, and diverse attack benchmarks.

---


### 152. [Cross-Modal Attention Analysis and Optimization in Vision-Language Models: A Study on Visual Reliability](https://arxiv.org/abs/2604.17217)

**<font color=#1a73e8>作者：</font>** Lijie Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) achieve strong cross-modal performance, yet recent evidence suggests they over-rely on textual descriptions while under-utilizing visual evidence -- a phenomenon termed ``text shortcut learning.'' We propose an adversarial evaluation framework that quantifies this cross-modal dependency by measuring accuracy degradation (Drop) when semantically conflicting text is paired with unchanged images. Four adversarial strategies -- shape\_swap, color\_swap, position\_swap, and random\_text -- are applied to a controlled geometric-shapes dataset ($n{=}1{,}000$). We compare three configurations: Baseline CLIP (ViT-B/32), LoRA fine-tuning, and LoRA Optimized (integrating Hard Negative Mining, Label Smoothing, layer-wise learning rates, Cosine Restarts, curriculum learning, and data augmentation). The optimized model reduces average Drop from 27.5\% to 9.8\% (64.4\% relative improvement, $p{<}0.001$) while maintaining 97\% normal accuracy. Attention visualization and embedding-space analysis confirm that the optimized model attends more to visual features and achieves tighter cross-modal alignment.

---


### 153. [Dynamics of Cognitive Heterogeneity: Investigating Behavioral Biases in Multi-Stage Supply Chains with LLM-Based Simulation](https://arxiv.org/abs/2604.17220)

**<font color=#1a73e8>作者：</font>** Jiuyun Jiang, Yuecheng Hong, Bo Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Modeling coordination among generative agents in complex multi-round decision-making presents a core challenge for AI and operations management. Although behavioral experiments have revealed cognitive biases behind supply chain inefficiencies, traditional methods face scalability and control limitations. We introduce a scalable experimental paradigm using Large Language Models (LLMs) to simulate multi-stage supply chain dynamics. Grounded in a Hierarchical Reasoning Framework, this study specifically analyzes the impact of cognitive heterogeneity on agent interactions. Unlike prior homogeneous settings, we employ DeepSeek and GPT agents to systematically vary reasoning sophistication across supply chain tiers. Through rigorously replicated and statistically validated simulations, we investigate how this cognitive diversity influences collective outcomes. Results indicate that agents exhibit myopic and self-interested behaviors that exacerbate systemic inefficiencies. However, we demonstrate that information sharing effectively mitigates these adverse effects. Our findings extend traditional behavioral methods and offer new insights into the dynamics of AI-enabled organizations. This work underscores both the potential and limitations of LLM-based agents as proxies for human decision-making in complex operational environments.

---


### 154. [Enhancing Zero-shot Personalized Image Aesthetics Assessment with Profile-aware Multimodal LLM](https://arxiv.org/abs/2604.17233)

**<font color=#1a73e8>作者：</font>** Chun Wang, Chenfeng Wei, Chenyang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized image aesthetics assessment (PIAA) aims to predict an individual user's subjective rating of an image, which requires modeling user-specific aesthetic preferences. Existing methods rely on historical user ratings for this modeling and therefore struggle when such data are unavailable. We address this zero-shot setting by using user profiles as contextual signals for personalization and adopting a profile-based personalization paradigm. We introduce P-MLLM, a profile-aware multimodal LLM that augments a frozen LLM with selective fusion modules for controlled visual integration. These modules selectively integrate visual information into the model's evolving hidden states during profile-conditioned reasoning, allowing visual information to be incorporated in a profile-aware manner. Experiments on recent PIAA benchmarks show that P-MLLM achieves competitive zero-shot performance and remains effective even with coarse profile information, highlighting the potential of profile-based personalization for zero-shot PIAA.

---


### 155. [RemoteShield: Enable Robust Multimodal Large Language Models for Earth Observation](https://arxiv.org/abs/2604.17243)

**<font color=#1a73e8>作者：</font>** Rui Min, Liang Yao, Shiyu Miao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A robust Multimodal Large Language Model (MLLM) for Earth Observation should maintain consistent interpretation and reasoning under realistic input variations. However, current Remote Sensing MLLMs fail to meet this requirement. Trained on carefully curated clean datasets, they learn brittle mappings that do not generalize to noisy conditions in operational Earth Observation. Consequently, their performance degrades when confronted with imperfect inputs in deployment. To quantify this vulnerability, we construct a realistic set of multimodal perturbations, including visual degradations such as cloud and fog cover, together with diverse human-centric textual variations ranging from colloquialisms to vague or omitted instructions. Empirical evaluations show that these perturbations significantly impair the visual-semantic reasoning capabilities of leading RS foundation models. To address this limitation, we introduce RemoteShield, a robust Remote Sensing MLLM trained to maintain consistent outputs across realistic input variations. During training, each clean sample is paired with its image-text perturbed variants to form a semantic equivalence cluster. Rather than directly fitting noisy samples, RemoteShield is optimized through preference learning over clean and perturbed conditions within the same cluster. By comparing model responses to clean and corrupted inputs, the model is encouraged to favor stable responses over perturbation-induced failures. This cross-condition alignment helps the model focus on underlying task semantics despite visual degradations and textual noise. Experiments on three Earth Observation tasks show that RemoteShield consistently delivers stronger robustness and cross-condition consistency than representative baselines under realistic multimodal perturbations.

---


### 156. [DORA Explorer: Improving the Exploration Ability of LLMs Without Training](https://arxiv.org/abs/2604.17244)

**<font color=#1a73e8>作者：</font>** Priya Gurjar, Md Farhan Ishmam, Kenneth Marino  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the rapid progress, LLMs for sequential decision-making (i.e., LLM agents) still struggle to produce diverse outputs. This leads to insufficient exploration, convergence to sub-optimal solutions, and becoming stuck in loops. Such limitations can be problematic in environments that require active exploration to gather information and make decisions. Sampling methods such as temperature scaling introduce token-level randomness but fail to produce enough diversity at the sequence level. We analyze LLM exploration in the classic Multi-Armed Bandit (MAB) setting and the Text Adventure Learning Environment Suite (TALES). We find that current decoding strategies and prompting methods like Chain-of-Thought and Tree-of-Thought are insufficient for robust exploration. To address this, we introduce DORA Explorer (Diversity-Oriented Ranking of Actions), a training-free framework for improving exploration in LLM agents. DORA generates diverse action candidates, scores them using token log-probabilities, and selects actions using a tunable exploration parameter. DORA achieves UCB-competitive performance on MAB and consistent gains across TALES, e.g., improving Qwen2.5-7B's performance from 29.2% to 45.5% in TextWorld. Our project is available at: this https URL.

---


### 157. [Are Emotion and Rhetoric Neurons in LLM? Neuron Recognition and Adaptive Masking for Emotion-Rhetoric Prediction Steering](https://arxiv.org/abs/2604.17255)

**<font color=#1a73e8>作者：</font>** Li Zheng, Xin Zhang, Shuyi He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurate comprehension and controllable generation of emotion and rhetoric are pivotal for enhancing the reasoning capabilities of large language models (LLMs). Existing studies mostly rely on external optimizations, lacking in-depth exploration of internal representation mechanisms, thus failing to achieve fine-grained steering at the neuron level. A handful of works on neurons are confined to emotions, neglecting rhetoric neurons and their intrinsic connections. Traditional neuron masking also exhibits counterintuitive phenomena, making reliable verification of neuron functionality infeasible. To address these issues, we systematically investigate the neurons representation mechanisms and inherent associations of 6 emotion categories and 4 core rhetorical devices. We propose a neuron identification framework that integrates multi-dimensional screening, and design an adaptive masking method incorporating dynamic filtering, attenuation masking, and feedback optimization, enabling reliable causal validation of neuron this http URL neuron regulation, we achieve directed induction of non-target sentences and enhancement of emotion tasks via rhetoric neurons. Experiments on 5 commonly used datasets validate the effectiveness of our method, providing a novel paradigm for the fine-grained steering of emotion and rhetoric expressions in LLMs.

---


### 158. [Rectification Difficulty and Optimal Sample Allocation in LLM-Augmented Surveys](https://arxiv.org/abs/2604.17267)

**<font color=#1a73e8>作者：</font>** Zikun Ye, Hema Yoganarasimhan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models can generate synthetic survey responses at low cost, but their accuracy varies unpredictably across questions. We study the design problem of allocating a fixed budget of human respondents across estimation tasks when cheap LLM predictions are available for every task. Our framework combines three components. First, building on Prediction-Powered Inference, we characterize a question-specific rectification difficulty that governs how quickly the estimator's variance decreases with human sample size. Second, we derive a closed-form optimal allocation rule that directs more human labels to tasks where the LLM is least reliable. Third, since rectification difficulty depends on unobserved human responses for new surveys, we propose a meta-learning approach, trained on historical data, that predicts it for entirely new tasks without pilot data. The framework extends to general M-estimation, covering regression coefficients and multinomial logit partworths for conjoint analysis. We validate the framework on two datasets spanning different domains, question types, and LLMs, showing that our approach captures 61-79% of the theoretically attainable efficiency gains, achieving 11.4% and 10.5% MSE reductions without requiring any pilot human data for the target survey.

---


### 159. [HopRank: Self-Supervised LLM Preference-Tuning on Graphs for Few-Shot Node Classification](https://arxiv.org/abs/2604.17271)

**<font color=#1a73e8>作者：</font>** Ziqing Wang, Kaize Ding  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Node classification on text-attributed graphs (TAGs) is a fundamental task with broad applications in citation analysis, social networks, and recommendation systems. Current GNN-based approaches suffer from shallow text encoding and heavy dependence on labeled data, limiting their effectiveness in label-scarce settings. While large language models (LLMs) naturally address the text understanding gap with deep semantic reasoning, existing LLM-for-graph methods either still require abundant labels during training or fail to exploit the rich structural signals freely available in graph topology. Our key observation is that, in many real-world TAGs, edges predominantly connect similar nodes under the homophily principle, meaning graph topology inherently encodes class structure without any labels. Building on this insight, we reformulate node classification as a link prediction task and present HopRank, a fully self-supervised LLM-tuning framework for TAGs. HopRank constructs preference data via hierarchical hop-based sampling and employs adaptive preference learning to prioritize informative training signals without any class labels. At inference, nodes are classified by predicting their connection preferences to labeled anchors, with an adaptive early-exit voting scheme to improve efficiency. Experiments on three TAG benchmarks show that HopRank matches fully-supervised GNNs and substantially outperforms prior graph-LLM methods, despite using zero labeled training data.

---


### 160. [Instinct vs. Reflection: Unifying Token and Verbalized Confidence in Multimodal Large Models](https://arxiv.org/abs/2604.17274)

**<font color=#1a73e8>作者：</font>** Yunkai Dang, Yifan Jiang, Yizhu Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated exceptional capabilities in various perception and reasoning tasks. Despite this success, ensuring their reliability in practical deployment necessitates robust confidence estimation. Prior works have predominantly focused on text-only LLMs, often relying on computationally expensive self-consistency sampling. In this paper, we extend this to multimodal settings and conduct a comprehensive evaluation of MLLMs' response confidence estimation. Our analysis reveals a significant instinct-reflection misalignment: the model's implicit token-level support frequently diverges from its verbal self-assessment confidence. To address this misalignment, we propose a monotone confidence fusion framework to merge dual-channel signals and cross-channel consistency to estimate correctness. Subsequently, an order-preserving mean alignment step is applied to correct global bias, which improves calibration while preserving the risk-coverage trade-off for selective prediction. Experiments on diverse open-source and closed-source MLLMs show that our method consistently yields more reliable confidence estimates and improves both calibration and failure prediction. Code will be available at this https URL.

---


### 161. [PestVL-Net: Enabling Multimodal Pest Learning via Fine-grained Vision-Language Interaction](https://arxiv.org/abs/2604.17278)

**<font color=#1a73e8>作者：</font>** Xueheng Li, Tao Hu, Ke Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective pest recognition and management are crucial for sustainable agricultural development. However, collecting pest data in real scenarios is often challenging. Compared to other domains, pests exhibit a wide variety of species with complex and diverse morphological characteristics. Existing techniques struggle to effectively model the key visual and high-level semantic features of pests in a fine-grained manner. These limitations hinder the practical application of such methods in real agricultural scenarios. To address these critical challenges, we present a synergistic approach that integrates PestVL-Net, a novel vision-language framework, with two multi-species pest datasets to facilitate fine-grained pest learning. The visual pathway of PestVL-Net utilizes the Recurrent Weighted Key Value (RWKV) architecture, incorporating a saliency-guided adaptive window partitioning scheme to effectively model the fine-grained visual characteristics of pests. Concurrently, the linguistic component generates precise pest semantic descriptions by leveraging Multimodal Large Language Models (MLLMs) priors, critically informed by agricultural expert knowledge and structured via multimodal Chain-of-Thought (CoT) reasoning. The deep fusion of these complementary visual and textual representations enables fine-grained multimodal pest learning. Extensive experimental evaluations on multiple pest datasets validate the superior performance of PestVL-Net, highlighting its potential for effective real-world pest management.

---


### 162. [REALM: Reliable Expertise-Aware Language Model Fine-Tuning from Noisy Annotations](https://arxiv.org/abs/2604.17289)

**<font color=#1a73e8>作者：</font>** Sajjad Ghiasvand, Mark Beliaev, Mahnoosh Alizadeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning of large language models relies on human-annotated data, yet annotation pipelines routinely involve multiple crowdworkers of heterogeneous expertise. Standard practice aggregates labels via majority vote or simple averaging, discarding annotator identity and causing the model to absorb the errors of unreliable annotators directly into its parameters. We propose REALM, a method that jointly learns the model parameters and a scalar expertise value for each annotator entirely unsupervised, requiring no supervision beyond annotator identity. The key idea is to model each observed label as a mixture between the model's prediction and a uniform random guess, weighted by the annotator's learned expertise. We extend REALM to a multi-task setting via a learned expertise matrix that captures per-annotator reliability across tasks. We evaluate on five question answering benchmarks, fine-tuning three sizes of Flan-T5 under simulated noisy annotations. The proposed algorithm consistently outperforms the naive noisy SFT in the large majority of single- and multi-task settings, across datasets, model sizes, and noise types, with accuracy improvements of up to $50\%$ in the most adversarial regime and gains that grow with model capacity.

---


### 163. [Beyond "I Don't Know": Evaluating LLM Self-Awareness in Discriminating Data and Model Uncertainty](https://arxiv.org/abs/2604.17293)

**<font color=#1a73e8>作者：</font>** Jingyi Ren, Ante Wang, Yunghwei Lai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable Large Language Models (LLMs) should abstain when confidence is insufficient. However, prior studies often treat refusal as a generic "I don't know'', failing to distinguish input-level ambiguity (data uncertainty) from capability limitations (model uncertainty). This lack of distinction limits downstream action decisions like requesting clarification or invoking external tools. In this work, we introduce UA-Bench, a benchmark of over 3,500 questions drawn from six datasets spanning knowledge-intensive and reasoning-intensive tasks, designed to evaluate explicit uncertainty attribution. An evaluation of 18 frontier LLMs shows that even state-of-the-art models struggle to reliably discriminate between data uncertainty and model uncertainty, and that high answer accuracy does not necessarily imply strong uncertainty attribution ability. To narrow this gap, we propose a lightweight data synthesis and reinforcement learning strategy. Experiments on both Qwen3-4B-Instruct-2507 and Qwen3-8B in thinking mode show that the proposed method improves uncertainty attribution while preserving answer accuracy. Our code and data are publicly available now.

---


### 164. [LLaTiSA: Towards Difficulty-Stratified Time Series Reasoning from Visual Perception to Semantics](https://arxiv.org/abs/2604.17295)

**<font color=#1a73e8>作者：</font>** Yueyang Ding, HaoPeng Zhang, Rui Dai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Comprehensive understanding of time series remains a significant challenge for Large Language Models (LLMs). Current research is hindered by fragmented task definitions and benchmarks with inherent ambiguities, precluding rigorous evaluation and the development of unified Time Series Reasoning Models(TSRMs). To bridge this gap, we formalize Time Series Reasoning (TSR) via a four-level taxonomy of increasing cognitive complexity. We introduce HiTSR, a hierarchical time series reasoning dataset comprising 83k samples with diverse task combinations and verified Chain-of-Thought (CoT) trajectories. Leveraging HiTSR, we propose LLaTiSA, a strong TSRM that integrates visualized patterns with precision-calibrated numerical tables to enhance the temporal perception of Vision-Language Models (VLMs). Through a multi-stage curriculum fine-tuning strategy, LLaTiSA achieves superior performance and exhibits robust out-of-distribution generalization across diverse TSR tasks and real-world scenarios. Our code is available at this https URL.

---


### 165. [Cat-DPO: Category-Adaptive Safety Alignment](https://arxiv.org/abs/2604.17299)

**<font color=#1a73e8>作者：</font>** Tiankai Yang, Yi Nian, Xinyuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aligning large language models with human preferences must balance two competing goals: responding helpfully to legitimate requests and reliably refusing harmful ones. Most preference-based safety alignment methods collapse safety into a single scalar that is applied uniformly to every preference pair. The result is a model that looks safe on average but stays relatively unsafe on a minority of harm categories. We cast safety alignment as a per-category constrained optimization problem and derive Cat-DPO, a direct-preference-optimization algorithm with a separate adaptive safety margin for each harm category. The margin tightens when the model still produces unsafe responses on a category and relaxes once the model catches up, so the training signal tracks each category's current difficulty rather than averaging under one global rate. Across two LLM backbones and six preference-learning baselines, Cat-DPO iimproves aggregate helpfulness and harmlessness and compresses per-category safety variance and the best-to-worst gap, offering a drop-in per-category refinement of direct preference safety alignment.

---


### 166. [RoTRAG: Rule of Thumb Reasoning for Conversation Harm Detection with Retrieval-Augmented Generation](https://arxiv.org/abs/2604.17301)

**<font color=#1a73e8>作者：</font>** Juhyeon Lee, Wonduk Seo, Junseo Koh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting harmful content in multi turn dialogue requires reasoning over the full conversational context rather than isolated utterances. However, most existing methods rely mainly on models internal parametric knowledge, without explicit grounding in external normative principles. This often leads to inconsistent judgments in socially nuanced contexts, limited interpretability, and redundant reasoning across turns. To address this, we propose RoTRAG, a retrieval augmented framework that incorporates concise human written moral norms, called Rules of Thumb (RoTs), into LLM based harm assessment. For each turn, RoTRAG retrieves relevant RoTs from an external corpus and uses them as explicit normative evidence for turn level reasoning and final severity classification. To improve efficiency, we further introduce a lightweight binary routing classifier that decides whether a new turn requires retrieval grounded reasoning or can reuse existing context. Experiments on ProsocialDialog and Safety Reasoning Multi Turn Dialogue show that RoTRAG consistently improves both harm classification and severity estimation over competitive baselines, with an average relative gain of around 40% in F1 across benchmark datasets and an average relative reduction of 8.4% in distributional error, while reducing redundant computation without sacrificing performance.

---


### 167. [A Survey of Reinforcement Learning for Large Language Models under Data Scarcity: Challenges and Solutions](https://arxiv.org/abs/2604.17312)

**<font color=#1a73e8>作者：</font>** Zhiyin Yu, Yuchen Mou, Juncheng Yan 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has emerged as a powerful post-training paradigm for enhancing the reasoning capabilities of large language models (LLMs). However, reinforcement learning for LLMs faces substantial data scarcity challenges, including the limited availability of high-quality external supervision and the constrained volume of model-generated experience. These limitations make data-efficient reinforcement learning a critical research direction. In this survey, we present the first systematic review of reinforcement learning for LLMs under data scarcity. We propose a bottom-up hierarchical framework built around three complementary perspectives: the data-centric perspective, the training-centric perspective, and the framework-centric perspective. We develop a taxonomy of existing methods, summarize representative approaches in each category, and analyze their strengths and limitations. Our taxonomy aims to provide a clear conceptual foundation for understanding the design space of data-efficient RL for LLMs and to guide researchers working in this emerging area. We hope this survey offers a comprehensive roadmap for future research and inspires new directions toward more efficient and scalable reinforcement learning post-training for LLMs.

---


### 168. [Calibrated? Not for Everyone: How Sexual Orientation and Religious Markers Distort LLM Accuracy and Confidence in Medical QA](https://arxiv.org/abs/2604.17316)

**<font color=#1a73e8>作者：</font>** Alberto Testoni, Iacer Calixto  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safe clinical deployment of Large Language Models (LLMs) requires not only high accuracy but also robust uncertainty calibration to ensure models defer to clinicians when appropriate. Our paper investigates how social descriptors of a patient (specifically sexual orientation and religious affiliation) distort these uncertainty signals and model accuracy. Evaluating nine general-purpose and biomedical LLMs on 2,364 medical questions and their counterfactual variants, we demonstrate that identity markers cause a "calibration crisis". "Homosexual" markers consistently trigger performance drops, and intersectional identities produce idiosyncratic, non-additive harms to calibration. Moreover, a clinician-validated case study in an open-ended generation setting confirms that these failures are not an artifact of the multiple-choice format. Our results demonstrate that the presence of social identity cues does not merely shift predictions; it affects the reliability of confidence signals, posing a significant risk to equitable care and safe deployment in confidence-based clinical workflows.

---


### 169. [When Background Matters: Breaking Medical Vision Language Models by Transferable Attack](https://arxiv.org/abs/2604.17318)

**<font color=#1a73e8>作者：</font>** Akash Ghosh, Subhadip Baidya, Sriparna Saha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are increasingly used in clinical diagnostics, yet their robustness to adversarial attacks remains largely unexplored, posing serious risks. Existing medical attacks focus on secondary objectives such as model stealing or adversarial fine-tuning, while transferable attacks from natural images introduce visible distortions that clinicians can easily detect. To address this, we propose MedFocusLeak, a highly transferable black-box multimodal attack that induces incorrect yet clinically plausible diagnoses while keeping perturbations imperceptible. The method injects coordinated perturbations into non-diagnostic background regions and employs an attention distraction mechanism to shift the model's focus away from pathological areas. Extensive evaluations across six medical imaging modalities show that MedFocusLeak achieves state-of-the-art performance, generating misleading yet realistic diagnostic outputs across diverse VLMs. We further introduce a unified evaluation framework with novel metrics that jointly capture attack success and image fidelity, revealing a critical weakness in the reasoning capabilities of modern clinical VLMs.

---


### 170. [E2E-GMNER: End-to-End Generative Grounded Multimodal Named Entity Recognition](https://arxiv.org/abs/2604.17319)

**<font color=#1a73e8>作者：</font>** Meng Zhang, Jinzhong Ning, Xiaolong Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grounded Multimodal Named Entity Recognition (GMNER) aims to jointly identify named entity mentions in text, predict their semantic types, and ground each entity to a corresponding visual region in an associated image. Existing approaches predominantly adopt pipeline-based architectures that decouple textual entity recognition and visual grounding, leading to error accumulation and suboptimal joint optimization. In this paper, we propose E2E-GMNER, a fully end-to-end generative framework that unifies entity recognition, semantic typing, visual grounding, and implicit knowledge reasoning within a single multimodal large language model. We formulate GMNER as an instruction-tuned conditional generation task and incorporate chain-of-thought reasoning to enable the model to adaptively determine when visual evidence or background knowledge is informative, reducing reliance on noisy cues. To further address the instability of generative bounding box prediction, we introduce Gaussian Risk-Aware Box Perturbation (GRBP), which replaces hard box supervision with probabilistically perturbed soft targets to improve robustness against annotation noise and discretization errors. Extensive experiments on the Twitter-GMNER and Twitter-FMNERG benchmarks demonstrate that E2E-GMNER achieves highly competitive performance compared with state of the art methods, validating the effectiveness of unified end-to-end optimization and noise-aware grounding supervision. Code is available at:this https URL

---


### 171. [Towards Joint Quantization and Token Pruning of Vision-Language Models](https://arxiv.org/abs/2604.17320)

**<font color=#1a73e8>作者：</font>** Xinqing Li, Xin He, Xindong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying Vision-Language Models (VLMs) under aggressive low-bit inference remains challenging because inference cost is dominated by the long visual-token prefix during prefill and the growing KV cache during autoregressive decoding. Token pruning and low-bit quantization are complementary for reducing these costs, yet naive stage-wise combinations are often brittle due to a mismatch between quantization calibration and pruning execution. We present a collaborative quantization-and-pruning framework that unifies low-bit inference and deterministic visual-token pruning in a single deployable pipeline. The framework introduces the \textbf{Q}uantization \textbf{U}nified \textbf{O}ffline \textbf{T}oken \textbf{A}llocator (\textbf{QUOTA}), which converts low-bit calibration signals into a layer-wise token allocation schedule and materializes it as a pruning recipe. Token importance is evaluated under deployed W4A4 operators with a quantized KV cache by combining activation magnitude, attention cues, and an explicit low-bit risk signal, enabling consistent budgeted top-$k$ selection. Experiments on standard VLM benchmarks show improved robustness over stage-wise baselines under the same low-bit regime, achieving 95.65\% average retention while retaining only 30\% of visual tokens, compared with about 94.3\% retention for representative stage-wise combinations. The code will be released.

---


### 172. [Align Documents to Questions: Question-Oriented Document Rewriting for Retrieval-Augmented Generation](https://arxiv.org/abs/2604.17325)

**<font color=#1a73e8>作者：</font>** Jiaang Li, Zhendong Mao, Quan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) enhances the factuality of Large Language Models (LLMs) by incorporating retrieved documents and/or generated context. However, LLMs often exhibit a stylistic bias when presented with mixed contexts, favoring fluent but hallucinated generated content over factually grounded yet disorganized retrieved evidence. This phenomenon reveals that the utility of retrieved information is bottlenecked by its presentation. To bridge this gap, we propose QREAM, a style-controlled rewriter that aligns retrieved documents with a question-oriented style while preserving facts, better for LLM readers to utilize. Our framework consists of two stages: (1) QREAM-ICL, which uses stylistic seeds to guide iterative rewriting exploration; and (2) QREAM-FT, a lightweight student model distilled from denoised ICL outputs. QREAM-FT employs dual-criteria rejection sampling, filtering based on answer correctness and factual consistency to ensure high-quality supervision. QREAM seamlessly integrates into existing RAG pipelines as a plug-and-play module. Experiments demonstrate that QREAM consistently enhances advanced RAG pipelines, yielding up to 8% relative improvement with negligible latency overhead, effectively balancing question relevance with factual grounding.

---


### 173. [AutoSearch: Adaptive Search Depth for Efficient Agentic RAG via Reinforcement Learning](https://arxiv.org/abs/2604.17337)

**<font color=#1a73e8>作者：</font>** Jingbo Sun, Wenyue Chong, Songjun Tu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic retrieval-augmented generation (RAG) systems enable large language models (LLMs) to solve complex tasks through multi-step interaction with external retrieval tools. However, such multi-step interaction often involves redundant search steps, incurring substantial computational cost and latency. Prior work limits search depth (i.e., the number of search steps) to reduce cost, but this often leads to underexploration of complex questions. To address this, we first investigate how search depth affects accuracy and find a minimal sufficient search depth that defines an accuracy-efficiency trade-off, jointly determined by question complexity and the agent's capability. Furthermore, we propose AutoSearch, a reinforcement learning (RL) framework that evaluates each search step via self-generated intermediate answers. By a self-answering mechanism, AutoSearch identifies the minimal sufficient search depth and promotes efficient search by rewarding its attainment while penalizing over-searching. In addition, reward mechanisms are introduced to stabilize search behavior and improve answer quality on complex questions. Extensive experiments on multiple benchmarks show that AutoSearch achieves a superior accuracy-efficiency trade-off, alleviating over-searching while preserving search quality.

---


### 174. [Formal Foundations of Agentic Business Process Management](https://arxiv.org/abs/2604.17347)

**<font color=#1a73e8>作者：</font>** Giuseppe De Giacomo, Timotheus Kampik, Lukas Kirchdorfer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Just like traditional BPM systems, agentic BPM systems are built around a specification of the process under consideration. Their distinguishing feature, however, is that the execution of the process is driven by multiple autonomous decision-makers, referred to as agents. Since such agents cannot be fully controlled, the process specification is augmented with explicit objectives, or goals, assigned to the participating agents. Agents then pursue these goals, at least to the best of their efforts, under suitable assumptions on the behavior of others, by adopting appropriate strategies. Centrally, the organization enacting the process can use these specifications to provide guardrails on the decision-making capabilities of agents at the strategy level. This paper sets up the mathematical foundations of such systems in three key settings and analyzes four foundational problems of agentic BPM.

---


### 175. [Hive: A Multi-Agent Infrastructure for Algorithm- and Task-Level Scaling](https://arxiv.org/abs/2604.17353)

**<font color=#1a73e8>作者：</font>** Zizhang Luo, Yuhao Luo, Youwei Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as complex agentic systems that scale with task complexity. While prior work has extensively explored model- and system-level scaling, algorithm- and task-level scaling remain largely unaddressed, constraining the full potential of agentic systems. At the algorithm level, allocating additional inference-time computation can enhance workflow capacity but introduces cross-path redundancy: overlapping computations across multiple reasoning branches. At the task level, complex tasks can be decomposed into subproblems and delegated across multiple agents for improved scalability and parallelism. However, existing infrastructures' scheduling is unaware of the existence of multiple agents, missing opportunities to optimize resource allocation.
We propose Hive, a multi-agent infrastructure that enables algorithm- and task-level scaling. Hive features a description frontend that captures per-agent behavior and supports test-time scaling algorithms. Leveraging this specification, our backend introduces two key mechanisms: Logits Cache that reuses intermediate logits across redundant sampling paths to mitigate cross-path redundancy at the algorithm level, and Agent-Aware Scheduling that efficiently allocates compute and KV-cache resources according to agent contributions at the task level. Experiments show that Logits Cache achieves an average speedup of $1.11\times$-$1.76\times$ for re-sampling, and Agent-Aware Scheduling reduces the hotspot miss rate by $33\%$-$51\%$.

---


### 176. [More Than Meets the Eye: Measuring the Semiotic Gap in Vision-Language Models via Semantic Anchorage](https://arxiv.org/abs/2604.17354)

**<font color=#1a73e8>作者：</font>** Wei He  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) excel at photorealistic generation, yet often struggle to represent abstract meaning such as idiomatic interpretations of noun compounds. To study whether high visual fidelity interferes with idiomatic compositionality under visual abstraction, we introduce DIVA, a controlled benchmark that replaces high-fidelity visual detail with schematic iconicity by generating paired, sense-anchored visualizations for literal and idiomatic readings. We further propose Semantic Alignment Gap ($\Delta$), an architecture-agnostic metric that quantifies divergence between literal and idiomatic visual grounding. We additionally introduce a directional signed bias $b(t)$ to separately measure the direction and strength of literal preference. Evaluating 8 recent VLMs, we reveal a consistent Literal Superiority Bias: model scale alone does not resolve literal preference, and increased visual fidelity is associated with weaker symbolic alignment, suggesting cognitive interference from hyper-realistic imagery. Our findings suggest that improving compositional understanding requires iconographic abstraction of visual input and anchoring interpretation and generation in intended meaning.

---


### 177. [LLM-Guided Strategy Synthesis for Scalable Equality Saturation](https://arxiv.org/abs/2604.17364)

**<font color=#1a73e8>作者：</font>** Chenyun Yin, Youwei Xiao, Yuze Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Equality saturation (EqSat) is a powerful optimization paradigm that compactly represents many equivalent programs in an e-graph and delays commitment until extraction selects a lowest-cost program. Making EqSat effective, therefore, requires not only domain-specific rewrite rules but also domain-specific strategies. Today, much of this strategy design is still manual, making it a major obstacle to automating e-graph-based compilers. Recent rule-synthesis frameworks can automatically infer large rewrite vocabularies from semantic specifications, but they also enlarge the rewrite space and further exacerbate e-graph explosion. Although large language models (LLMs) make automated strategy synthesis plausible, directly evolving backend code remains ineffective in practice. The search lacks reusable strategy abstractions and actionable feedback, and can easily trigger e-graph explosion or converge to poor designs.
We present EggMind, an LLM-guided, end-to-end framework for synthesizing reusable EqSat strategies. At its core, EggMind introduces a domain-specific language, EqSatL, to represent EqSat strategies as explicit and inspectable artifacts. It then proposes an LLM-guided agentic workflow, equipped with novel techniques including proof-derived rewrite motif caching and tractability guidance, to search efficiently for high-quality strategies while keeping synthesis stable under e-graph growth. Evaluation shows that EggMind substantially improves the resource-quality trade-off on vectorization benchmarks, reducing final cost by 45.1% and peak RAM by 69.1% relative to full EqSat. We further show that the same methodology transfers effectively to an XLA-based tensor compiler, and demonstrate its practical potential in a logic-synthesis case study with augmented rewrite spaces.

---


### 178. [ArgBench: Benchmarking LLMs on Computational Argumentation Tasks](https://arxiv.org/abs/2604.17366)

**<font color=#1a73e8>作者：</font>** Yamen Ajjour, Carlotta Quensel, Nedim Lipka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Argumentation skills are an essential toolkit for large language models (LLMs). These skills are crucial in various use cases, including self-reflection, debating collaboratively for diverse answers, and countering hate speech. In this paper, we create the first benchmark for a standardized evaluation of LLM-based approaches to computational argumentation, encompassing 33 datasets from previous work in unified form. Using the benchmark, we evaluate the generalizability of five LLM families across 46 computational argumentation tasks that cover mining arguments, assessing perspectives, assessing argument quality, reasoning about arguments, and generating arguments. On the benchmark, we conduct an extensive systematic analysis of the contribution of few-shot examples, reasoning steps, model size, and training skills to the performance of LLMs on the computational argumentation tasks in the benchmark.

---


### 179. [When Text Hijacks Vision: Benchmarking and Mitigating Text Overlay-Induced Hallucination in Vision Language Models](https://arxiv.org/abs/2604.17375)

**<font color=#1a73e8>作者：</font>** Cui Yakun, Xingqun Qi, TianTian Geng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Vision-Language Models (VLMs) have substantially enhanced their ability across multimodal video understanding benchmarks spanning temporal, action, object, and spatial understanding. However, we identify a critical yet overlooked issue: when embedded on-screen text contradicts the visual scene, existing VLMs systematically hallucinate, prioritizing overlay textual semantics over the actual visual content. We define this phenomenon as Text Overlay-Induced Hallucination (TOIH). In this work, we propose VisualTextTrap, the first comprehensive benchmark, including large-scale human-validated samples with specifically designed evaluation metrics. In particular, we construct VisualTextTrap from widely-used public datasets using a scalable hybrid pipeline of VLMs assisted text generation and rigorous manual verification. The benchmark features 6,057 samples annotated across 88 fine-grained attributes within four dimensions, with hallucination intensity quantified on a five-level scale (L1--L5) that reflects the semantic contradiction between overlay text and visual reality. Moreover, we propose Visual Text Hallucination Mitigation Mixture-of-Experts (VTHM-MoE), a novel Vision-Text Disentanglement framework that employs a dual-encoder architecture. Concretely, four dimension-specialized expert modules spanning Temporal, Action, Object, and Spatial reasoning are first pre-trained to identify and leverage cross-modal discrepancies between textual semantics and actual video content. We develop an Adaptive Token Routing Strategy to enable dynamic expert allocation, conferring robust resistance to TOIH while preserving performance on uncontaminated videos. Extensive experiments conducted on our VisualTextTrap benchmark verify the effectiveness of VTHM-MoE, outperforming state-of-the-art counterparts with diverse video question answering tasks.

---


### 180. [AnchorMem: Anchored Facts with Associative Contexts for Building Memory in Large Language Models](https://arxiv.org/abs/2604.17377)

**<font color=#1a73e8>作者：</font>** Zhanyu Shen, Sijie Cheng, Zhicheng Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language models have achieved remarkable performance in complex tasks, they still need a memory system to utilize historical experience in long-term interactions. Existing memory methods (e.g., A-Mem, Mem0) place excessive emphasis on organizing interactions by frequently rewriting them, however, this heavy reliance on summarization risks diluting essential contextual nuances and obscuring key retrieval features. To bridge this gap, we introduce AnchorMem, a novel memory framework inspired by the Proust Phenomenon in cognitive science, where a specific anchor triggers a holistic recollection. We propose a method that decouples the retrieval unit from the generation context. AnchorMem extracts atomic facts from interaction history to serve as retrieval anchors, while preserving the original context as the immutable context. To reveal implicit narrative cues, we construct an associative event graph that uses higher-order event links that bind sets of related facts into shared event representations, strengthening cross-memory integration without relying on generic entities as bridges. During retrieval, the system anchors queries to specific facts and events to locate relevant memories, but reconstructs the context using the associated raw chunks and events. Our method reconciles fine-grained retrieval with the contextual integrity of interactions. Experiments across three closed-source and open-source models on the LoCoMo benchmark demonstrate that AnchorMem significantly outperforms baselines. Code is available at this https URL.

---


### 181. [Towards a Data-Parameter Correspondence for LLMs: A Preliminary Discussion](https://arxiv.org/abs/2604.17384)

**<font color=#1a73e8>作者：</font>** Ou Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model optimization has historically bifurcated into isolated data-centric and model-centric paradigms: the former manipulates involved samples through selection, augmentation, or poisoning, while the latter tunes model weights via masking, quantization, or low-rank adaptation. This paper establishes a unified \emph{data-parameter correspondence} revealing these seemingly disparate operations as dual manifestations of the same geometric structure on the statistical manifold $\mathcal{M}$. Grounded in the Fisher-Rao metric $g_{ij}(\theta)$ and Legendre duality between natural ($\theta$) and expectation ($\eta$) parameters, we identify three fundamental correspondences spanning the model lifecycle: 1. Geometric correspondence: data pruning and parameter sparsification equivalently reduce manifold volume via dual coordinate constraints; 2. Low-rank correspondence: in-context learning (ICL) and LoRA adaptation explore identical subspaces on the Grassmannian $\mathcal{G}(r,d)$, with $k$-shot samples geometrically equivalent to rank-$r$ updates; 3. Security-privacy correspondence: adversarial attacks exhibit cooperative amplification between data poisoning and parameter backdoors, whereas protective mechanisms follow cascading attenuation where data compression multiplicatively enhances parameter privacy. Extending from training through post-training compression to inference, this framework provides mathematical formalization for cross-community methodology transfer, demonstrating that cooperative optimization integrating data and parameter modalities may outperform isolated approaches across efficiency, robustness, and privacy dimensions.

---


### 182. [SpatialImaginer: Towards Adaptive Visual Imagination for Spatial Reasoning](https://arxiv.org/abs/2604.17385)

**<font color=#1a73e8>作者：</font>** Yian Li, Yang Jiao, Bin Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence, which refers to the ability to reason about geometric and physical structure from visual observations, remains a core challenge for multimodal large language models. Despite promising performance, recent multimodal large language models (MLLMs) often exhibit fragile reasoning traces in spatial intelligence tasks that involve consistent spatial state recognition. We argue that these failures stem from a mismatch between the spatial recognition mechanism and the text-only reasoning behavior of these MLLMs. Effective spatial reasoning requires low-level geometric structure to be faithfully preserved and updated throughout the reasoning process, whereas textual representations tend to abstract away precisely these critical details. To address this issue, we propose SpatialImaginer, a unified multimodal generation framework that integrates textual reasoning with visual imagination. Our framework adopts a divide-and-conquer strategy, using text chain-of-thought for high-level semantic planning and the visual imagination for geometry-sensitive state transformation and consistency preservation. To support this capability, we further introduce a difficulty-aware data engine with closed-loop verification to train the model to invoke visual imagination selectively when stable spatial state tracking is required. Extensive experiments on diverse spatial intelligence benchmarks show that SpatialImaginer achieves state-of-the-art performance and substantially improves robustness on complex multi-step spatial reasoning tasks.

---


### 183. [Representation-Guided Parameter-Efficient LLM Unlearning](https://arxiv.org/abs/2604.17396)

**<font color=#1a73e8>作者：</font>** Zeguan Xiao, Lang Mo, Yun Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often memorize sensitive or harmful information, necessitating effective machine unlearning techniques. While existing parameter-efficient unlearning methods have shown promise, they still struggle with the forget-retain trade-off. This can be attributed to their reliance on parameter importance metrics to identify parameters that are important exclusively for the forget set, which is fundamentally limited by the superposition phenomenon. Due to the polysemantic nature of LLM parameters, such an importance metric may struggle to disentangle parameters associated with the forget and retain sets. In this work, we propose Representation-Guided Low-rank Unlearning (REGLU), a novel approach that leverages the geometric properties of representation spaces to achieve robust and precise unlearning. First, we develop a representation-guided initialization for LoRA that identifies the optimal subspace for selective forgetting. Second, we introduce a regularization loss that constrains the outputs of the LoRA update to lie in the orthogonal complement of the retain set's representation subspace, thereby minimizing interference with the model's performance on the retain set. We evaluate REGLU on the TOFU and WMDP benchmarks across multiple models. Our results demonstrate that REGLU consistently outperforms state-of-the-art baselines, achieving superior unlearning quality while maintaining higher model utility.

---


### 184. [Contrastive Analysis of Linguistic Representations in Large Language Model Outputs through Structured Synthetic Data Generation and Abstracted N-gram Associations](https://arxiv.org/abs/2604.17398)

**<font color=#1a73e8>作者：</font>** S.A. Desimone, L. Alonso Alemany  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a methodological framework to discover linguistic and discursive patterns associated to different social groups through contrastive synthetic text generation and statistical analysis. In contrast with previous approaches, we aim to characterize subtle expressions of bias, instead of diagnosing bias through a pre-determined list of words or expressions. We are also working with contextualized data instead of isolated words or sentences. Our methodology applies to textual productions in any genre, encompassing narrative, task-oriented or dialogic. Contextualized data are generated using controlled combinations of situational scenarios and group markers, creating minimal pairs of texts that differ only in the referenced group while maintaining comparable narrative conditions. To facilitate robust analysis, linguistic forms are generalized and associations between linguistic abstractions and groups are quantified using a variant of pointwise mutual information to detect expressions that appear disproportionately across groups. A fragment-ranking strategy then prioritizes text segments with a high concentration of biased linguistic signals, which allows for experts to assess the harmful potential of linguistic expressions in context, bridging quantitative analysis and qualitative interpretation.

---


### 185. [Beyond Meta-Reasoning: Metacognitive Consolidation for Self-Improving LLM Reasoning](https://arxiv.org/abs/2604.17399)

**<font color=#1a73e8>作者：</font>** Ziqing Zhuang, Linhai Zhang, Jiasheng Si 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong reasoning capabilities, and as existing approaches for enhancing LLM reasoning continue to mature, increasing attention has shifted toward meta-reasoning as a promising direction for further improvement. However, most existing meta-reasoning methods remain episodic: they focus on executing complex meta-reasoning routines within individual instances, but ignore the accumulation of reusable meta-reasoning skills across instances, leading to recurring failure modes and repeatedly high metacognitive effort. In this paper, we introduce Metacognitive Consolidation, a novel framework in which a model consolidates metacognitive experience from past reasoning episodes into reusable knowledge that improves future meta-reasoning. We instantiate this framework by structuring instance-level problem solving into distinct roles for reasoning, monitoring, and control to generate rich, attributable meta-level traces. These traces are then consolidated through a hierarchical, multi-timescale update mechanism that gradually forms evolving meta-knowledge. Experimental results demonstrate consistent performance gains across benchmarks and backbone models, and show that performance improves as metacognitive experience accumulates over time.

---


### 186. [Reward Score Matching: Unifying Reward-based Fine-tuning for Flow and Diffusion Models](https://arxiv.org/abs/2604.17415)

**<font color=#1a73e8>作者：</font>** Jeongjae Lee, Jinho Chang, Jeongsol Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward-based fine-tuning aims to steer a pretrained diffusion or flow-based generative model toward higher-reward samples while remaining close to the pretrained model. Although existing methods are motivated by different perspectives such as Soft RL, GFlowNets, etc., we show that many can be written under a common framework, which we call reward score matching (RSM). Under this view, alignment becomes score matching toward a reward-guided target, and the main differences across methods reduce to the construction of the value-guidance estimator and the effective optimization strength across timesteps. This unification clarifies the bias--variance--compute tradeoffs of existing designs and distinguishes core optimization components from auxiliary mechanisms that add complexity without clear benefit. Guided by this perspective, we develop simpler redesigns that improve alignment effectiveness and compute efficiency across representative settings with differentiable and black-box rewards. Overall, RSM turns a seemingly fragmented collection of reward-based fine-tuning methods into a smaller, more interpretable, and more actionable design space.

---


### 187. [ARMove: Learning to Predict Human Mobility through Agentic Reasoning](https://arxiv.org/abs/2604.17419)

**<font color=#1a73e8>作者：</font>** Chuyue Wang, Jie Feng, Yuxi Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Human mobility prediction is a critical task but remains challenging due to its complexity and variability across populations and regions. Recently, large language models (LLMs) have made progress in zero-shot prediction, but existing methods suffer from limited interpretability (due to black-box reasoning), lack of iterative learning from new data, and poor transferability. In this paper, we introduce \textbf{ARMove}, a fully transferable framework for predicting human mobility through agentic reasoning. To address these limitations, ARMove employs standardized feature management with iterative optimization and user-specific customization: four major feature pools for foundational knowledge, user profiles for segmentation, and an automated generation mechanism integrating LLM knowledge. Robust generalization is achieved via agentic decision-making that adjusts feature weights to maximize accuracy while providing interpretable decision paths. Finally, large-small model synergy distills strategies from large LLMs (e.g., 72B) to smaller ones (e.g., 7B), reducing costs and enhancing performance ceilings. Extensive experiments on four global datasets show ARMove outperforms state-of-the-art baselines on 6 out of 12 metrics (gains of 0.78\% to 10.47\%), with transferability tests confirming robustness across regions, users, and scales. The other 4 items also achieved suboptimal results. Transferability tests confirm its 19 robustness across regions, user groups, and model scales, while interpretability 20 analysis highlights its transparency in decision-making. Our codes are available at: this https URL.

---


### 188. [Where to Focus: Query-Modulated Multimodal Keyframe Selection for Long Video Understanding](https://arxiv.org/abs/2604.17422)

**<font color=#1a73e8>作者：</font>** Shaoguang Wang, Weiyu Guo, Ziyang Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long video understanding remains a formidable challenge for Multimodal Large Language Models (MLLMs) due to the prohibitive computational cost of processing dense frame sequences. Prevailing solutions, which select a keyframe subset, typically rely on either a single visual-centric metric (e.g., CLIP similarity) or a static fusion of heuristic scores. This ``one-size-fits-all'' paradigm frequently fails: visual-only metrics are ineffective for plot-driven narrative queries, while indiscriminately incorporating textual scores introduces severe ``modal noise'' for purely visual tasks. To break this bottleneck, we propose Q-Gate, a plug-and-play and training-free framework that treats keyframe selection as a dynamic modality routing problem. We decouple the retrieval process into three lightweight expert streams: Visual Grounding for local details, Global Matching for scene semantics, and Contextual Alignment for subtitle-driven narratives. Crucially, Q-Gate introduces a Query-Modulated Gating Mechanism that leverages the in-context reasoning of an LLM to assess the query's intent and dynamically allocate attention weights across the experts. This mechanism intelligently activates necessary modalities while ``muting'' irrelevant ones, thereby maximizing the signal-to-noise ratio. Extensive experiments on LongVideoBench and Video-MME across multiple MLLM backbones demonstrate that Q-Gate substantially outperforms state-of-the-art baselines. By effectively suppressing modality-specific noise, it provides a robust, highly interpretable solution for scalable video reasoning.

---


### 189. [Jupiter-N Technical Report](https://arxiv.org/abs/2604.17429)

**<font color=#1a73e8>作者：</font>** George Drayson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Jupiter-N, a hybrid reasoning model post-trained from Nemotron 3 Super, a fully open-source 120 billion parameter LLM. We target three objectives: (1) agentic capability via uncertainty-curated trajectories; (2) UK cultural alignment via synthetic data grounded in cultural norms; and (3) Welsh language support via parallel corpora and LLM-translated Welsh conversations. Our data curation strategy carefully preserves the base model's capabilities: using our Forget-Me-Not framework, we mix on-policy synthetic replay with off-policy task data to mitigate catastrophic forgetting, and include a mixture of reasoning and non-reasoning traces to maintain Nemotron's hybrid reasoning ability. Jupiter-N achieves standout gains over Nemotron in Welsh (+18 on ARC-Easy, +5.25 on MMLU-Lite), terminal-use (+9.1 on Terminal Bench 2) and instruction following (+4.4 on IFBench), while retaining the base model capabilities. We frame this work as a reproducible template for sovereign post-training: substituting cultural knowledge, institutional corpora, and target languages produces an equivalent pipeline for any country. All model weights and all post-training datasets are publicly released under open licences.

---


### 190. [Self-Consistency from Only Two Samples: CoT-PoT Ensembling for Efficient LLM Reasoning](https://arxiv.org/abs/2604.17433)

**<font color=#1a73e8>作者：</font>** Raman Saparkhan, Majd Hawasly, Md Rizwan Parvez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-consistency (SC) is a popular technique for improving the reasoning accuracy of large language models by aggregating multiple sampled outputs, but it comes at a high computational cost due to extensive sampling. We introduce a hybrid ensembling approach that leverages the complementary strengths of two distinct modes of reasoning: Chain-of-Thought (CoT) and Program-of-Thought (PoT). We describe a general framework for combining these two forms of reasoning in self-consistency, as well as particular strategies for both full sampling and early-stopping. We show that CoT-PoT ensembling not only improves overall accuracy, but also drastically reduces the number of samples required for SC by a factor of 9.3x. In particular, the majority of tasks (78.6%) can be addressed with only two samples, which has not been possible with any prior SC methods.

---


### 191. [Compiling Deterministic Structure into SLM Harnesses](https://arxiv.org/abs/2604.17450)

**<font color=#1a73e8>作者：</font>** Zan Kai Chong, Hiroyuki Ohsaki, Bryan Ng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise deployment of small language models (SLMs) is constrained by epistemic asymmetry: SLMs cannot self-correct reasoning errors, while frontier LLMs are prohibitively costly and face data sovereignty limits for high-volume use. We propose Semantic Gradient Descent (SGDe), a teacher-student framework that compiles agentic workflows into discrete execution plans comprising DAG topologies, system prompts, and deterministic executable code. The trailing "e" distinguishes SGDe from stochastic gradient descent. SGDe operates in a discrete semantic space where a frontier teacher generates natural-language critiques acting as directional gradients to iteratively refine the SLM's workflow artefacts. We formalise SGDe within a PAC learning framework, establishing sample-complexity bounds that enable convergence with as few as three training examples on targeted synthetic tasks by leveraging the teacher as a statistical prior. On a GSM-Hard-derived test set built via adversarial synthesis, compiled workflows reach 91.3% accuracy at m=5 and 99.3% at m=3 within the small-m regime motivated by Corollary 1, a +26.3% to +34.3% absolute improvement over state-of-the-art prompt optimisers. In the emerging paradigm of harness engineering, SGDe treats placement of deterministic code (which subtasks to delegate to a Python runtime versus retain as LLM calls) as a trace-driven, per-node optimisation target, generalising the whole-problem offloading of PAL and PoT. The teacher compiles two complementary deterministic structures: capability offloading, which delegates subtasks to Python when the SLM cannot execute them reliably, and structural consensus, which wraps variance-limited reasoning steps in fan-out/fan-in subgraphs aggregated by deterministic voting.

---


### 192. [EHRAG: Bridging Semantic Gaps in Lightweight GraphRAG via Hybrid Hypergraph Construction and Retrieval](https://arxiv.org/abs/2604.17458)

**<font color=#1a73e8>作者：</font>** Yifan Song, Xingjian Tao, Zhicheng Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph-based Retrieval-Augmented Generation (GraphRAG) enhances LLMs by structuring corpus into graphs to facilitate multi-hop reasoning. While recent lightweight approaches reduce indexing costs by leveraging Named Entity Recognition (NER), they rely strictly on structural co-occurrence, failing to capture latent semantic connections between disjoint entities. To address this, we propose EHRAG, a lightweight RAG framework that constructs a hypergraph capturing both structure and semantic level relationships, employing a hybrid structural-semantic retrieval mechanism. Specifically, EHRAG constructs structural hyperedges based on sentence-level co-occurrence with lightweight entity extraction and semantic hyperedges by clustering entity text embeddings, ensuring the hypergraph encompasses both structural and semantic information. For retrieval, EHRAG performs a structure-semantic hybrid diffusion with topic-aware scoring and personalized pagerank (PPR) refinement to identify the top-k relevant documents. Experiments on four datasets show that EHRAG outperforms state-of-the-art baselines while maintaining linear indexing complexity and zero token consumption for construction. Code is available at this https URL.

---


### 193. [Language models recognize dropout and Gaussian noise applied to their activations](https://arxiv.org/abs/2604.17465)

**<font color=#1a73e8>作者：</font>** Damiano Fornasiere, Mirko Bronzi, Spencer Kitts 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We provide evidence that language models can detect, localize and, to a certain degree, verbalize the difference between perturbations applied to their activations. More precisely, we either (a) \emph{mask} activations, simulating \emph{dropout}, or (b) add \emph{Gaussian noise} to them, at a target sentence. We then ask a multiple-choice question such as ``\emph{Which of the previous sentences was perturbed?}'' or ``\emph{Which of the two perturbations was applied?}''.
We test models from the Llama, Olmo, and Qwen families, with sizes between 8B and 32B, all of which can easily detect and localize the perturbations, often with perfect accuracy. These models can also learn, when taught in context, to distinguish between dropout and Gaussian noise. Notably, \qwenb's \emph{zero-shot} accuracy in identifying which perturbation was applied improves as a function of the perturbation strength and, moreover, decreases if the in-context labels are flipped, suggesting a prior for the correct ones -- even modulo controls.
Because dropout has been used as a training-regularization technique, while Gaussian noise is sometimes added during inference, we discuss the possibility of a data-agnostic ``training awareness'' signal and the implications for AI safety.
The code and data are available at \href{this https URL}{link 1} and \href{this https URL}{link 2}, respectively.

---


### 194. [Dual-Anchoring: Addressing State Drift in Vision-Language Navigation](https://arxiv.org/abs/2604.17473)

**<font color=#1a73e8>作者：</font>** Kangyi Wu, Pengna Li, Kailin Lyu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Navigation(VLN) requires an agent to navigate through 3D environments by following natural language instructions. While recent Video Large Language Models(Video-LLMs) have largely advanced VLN, they remain highly susceptible to State Drift in long scenarios. In these cases, the agent's internal state drifts away from the true task execution state, leading to aimless wandering and failure to execute essential maneuvers in the instruction. We attribute this failure to two distinct cognitive deficits: Progress Drift, where the agent fails to distinguish completed sub-goals from remaining ones, and Memory Drift, where the agent's history representations degrade, making it lose track of visited landmarks. In this paper, we propose a Dual-Anchoring Framework that explicitly anchors the instruction progress and history representations. First, to address progress drift, we introduce Instruction Progress Anchoring, which supervises the agent to generate structured text tokens that delineate completed versus remaining sub-goals. Second, to mitigate memory drift, we propose Memory Landmark Anchoring, which utilizes a Landmark-Centric World Model to retrospectively predict object-centric embeddings extracted by the Segment Anything Model, compelling the agent to explicitly verify past observations and preserve distinct representations of visited landmarks. Facilitating this framework, we curate two extensive datasets: 3.6 million samples with explicit progress descriptions, and 937k grounded landmark data for retrospective verification. Extensive experiments in both simulation and real-world environments demonstrate the superiority of our method, achieving a 15.2% improvement in Success Rate and a remarkable 24.7% gain on long-horizon trajectories. To facilitate further research, we will release our code, data generation pipelines, and the collected datasets.

---


### 195. [Waking Up Blind: Cold-Start Optimization of Supervision-Free Agentic Trajectories for Grounded Visual Perception](https://arxiv.org/abs/2604.17475)

**<font color=#1a73e8>作者：</font>** Ashutosh Bajpai, Tamal Majumder, Akshay Nambi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small Vision-Language Models (SVLMs) are efficient task controllers but often suffer from visual brittleness and poor tool orchestration. They typically require expensive supervised trajectory tuning to mitigate these deficits. In this work, we propose Self-supervised Perception Enabled by Cascaded Tool Rollout Alignment (SPECTRA), a supervision-free framework that bootstraps agentic capabilities via Coldstart Reinforcement Learning for SVLMs. SPECTRA enforces Soft Structured Multi-turn Rollouts, a topological constraint that directs agents to explicitly sequence tool derived evidence before synthesis, effectively grounding reasoning in visual observations. We employ a multi-objective reward signal that simultaneously maximizes task correctness, rollout structure, and tool utility, enabling agent to self-discover robust behaviors without human preference labels. We further introduce Tool Instrumental Utility (TIU), a novel metric to quantify tool efficacy in the absence of ground truth. Extensive evaluations across composite and out-of-distribution (MMMU-Pro) benchmarks demonstrate that SPECTRA boosts agentic trajectories, improving task accuracy by up to 5% and tool efficiency by 9%, enabling more efficient multimodal agents that learn effectively from environmental interaction alone.

---


### 196. [Answer Only as Precisely as Justified: Calibrated Claim-Level Specificity Control for Agentic Systems](https://arxiv.org/abs/2604.17487)

**<font color=#1a73e8>作者：</font>** Tianyi Huang, Samuel Xu, Jason Tansong Dang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic systems often fail not by being entirely wrong, but by being too precise: a response may be generally useful while particular claims exceed what the evidence supports. We study this failure mode as overcommitment control and introduce compositional selective specificity (CSS), a post-generation layer that decomposes an answer into claims, proposes coarser backoffs, and emits each claim at the most specific calibrated level that appears admissible. The method is designed to express uncertainty as a local semantic backoff rather than as a whole-answer refusal. Across a full LongFact run and HotpotQA pilots, calibrated CSS improves the risk-utility trade-off of fixed drafts. On the full LongFact run, it raises overcommitment-aware utility from 0.846 to 0.913 relative to the no-CSS output while achieving 0.938 specificity retention. These results suggest that claim-level specificity control is a useful uncertainty interface for agentic systems and a target for future distribution-free validity layers.

---


### 197. [AutoVQA-G: Self-Improving Agentic Framework for Automated Visual Question Answering and Grounding Annotation](https://arxiv.org/abs/2604.17488)

**<font color=#1a73e8>作者：</font>** Rongsheng Hu, Runwei Guan, Yicheng Di 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Manual annotation of high-quality visual question answering with grounding (VQA-G) datasets, which pair visual questions with evidential grounding, is crucial for advancing vision-language models (VLMs), but remains unscalable. Existing automated methods are often hindered by two key issues: (1) inconsistent data fidelity due to model hallucinations; (2) brittle verification mechanisms based on simple heuristics. To address these limitations, we introduce AutoVQA-G, a self-improving agentic framework for automated VQA-G annotation. AutoVQA-G employs an iterative refinement loop where a Consistency Evaluation module uses Chain-of-Thought (CoT) reasoning for fine-grained visual verification. Based on this feedback, a memory-augmented Prompt Optimization agent analyzes critiques from failed samples to progressively refine generation prompts. Our experiments show that AutoVQA-G generates VQA-G datasets with superior visual grounding accuracy compared to leading multimodal LLMs, offering a promising approach for creating high-fidelity data to facilitate more robust VLM training and evaluation. Code: this https URL

---


### 198. [CoAct: Co-Active LLM Preference Learning with Human-AI Synergy](https://arxiv.org/abs/2604.17501)

**<font color=#1a73e8>作者：</font>** Ruiyao Xu, Mihir Parmar, Tiankai Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Learning from preference-based feedback has become an effective approach for aligning LLMs across diverse tasks. However, high-quality human-annotated preference data remains expensive and scarce. Existing methods address this challenge through either self-rewarding, which scales by using purely AI-generated labels but risks unreliability, or active learning, which ensures quality through oracle annotation but cannot fully leverage unlabeled data. In this paper, we present CoAct, a novel framework that synergistically combines self-rewarding and active learning through strategic human-AI collaboration. CoAct leverages self-consistency to identify both reliable self-labeled data and samples that require oracle verification. Additionally, oracle feedback guides the model to generate new instructions within its solvable capability. Evaluated on three reasoning benchmarks across two model families, CoAct achieves average improvements of +13.25% on GSM8K, +8.19% on MATH, and +13.16% on WebInstruct, consistently outperforming all baselines.

---


### 199. [Towards Shutdownable Agents: Generalizing Stochastic Choice in RL Agents and LLMs](https://arxiv.org/abs/2604.17502)

**<font color=#1a73e8>作者：</font>** Carissa Cullen, Harry Garland, Alexander Roman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Misaligned artificial agents might resist shutdown. One proposed solution is to train agents to lack preferences between different-length trajectories. The Discounted Reward for Same-Length Trajectories (DReST) reward function does this by penalizing agents for repeatedly choosing same-length trajectories, and thus incentivizes agents to (1) choose stochastically between different trajectory-lengths (be Neutral about trajectory-lengths), and (2) pursue goals effectively conditional on each trajectory-length (be Useful). In this paper, we use DReST to train deep RL agents and fine-tune LLMs to be Neutral and Useful. We find that these DReST agents generalize to being Neutral and Useful in unseen contexts at test time. Indeed, DReST RL agents achieve 11% (PPO) and 18% (A2C) higher Usefulness on our test set than baseline agents, and our fine-tuned LLM achieves maximum Usefulness and near-maximum Neutrality. Our results provide some early evidence that DReST could be used to train more advanced agents to be Useful and Neutral. Prior theoretical work suggests that these agents would be useful and shutdownable.

---


### 200. [SkillGraph: Self-Evolving Multi-Agent Collaboration with Multimodal Graph Topology](https://arxiv.org/abs/2604.17503)

**<font color=#1a73e8>作者：</font>** Zheng Nie, Ruolin Shen, Xinlei Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling vision-language models into Visual Multiagent Systems (VMAS) is hindered by two coupled issues. First, communication topologies are fixed before inference, leaving them blind to visual content and query context; second, agent reasoning abilities remain static during deployment. These issues reinforce each other: a rigid topology fails to leverage richer agent expertise, while static agents lack incentives to specialize for a given query. We address this with SkillGraph, a joint framework that evolves both agent expertise and communication topology. Within this framework, a Multimodal Graph Transformer (MMGT) encodes visual tokens, instruction semantics and active skill embeddings to predict a query-conditioned collaboration graph, replacing hand-crafted routing with dynamic, content-aware information flow. Complementing this, a Skill Designer distills and refines reasoning heuristics from failure cases, constructing a self-evolving multimodal Skill Bank. Crucially, updated skill embeddings are fed back into the MMGT, enabling the topology to adapt alongside capability growth. Experiments show that SkillGraph achieves consistent improvements across four benchmarks, five common MAS structures and four base models. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
