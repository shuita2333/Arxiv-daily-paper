# 🧠 大模型相关研究 | 2026年04月29日

> 本类共 **215** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-215](./part-05.md)

---

### 151. [DeepTaxon: An Interpretable Retrieval-Augmented Multimodal Framework for Unified Species Identification and Discovery](https://arxiv.org/abs/2604.24029)

**<font color=#1a73e8>作者：</font>** Jiawei Wang, Ming Lei, Yaning Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identifying species in biology among tens of thousands of visually similar taxa while discovering unknown species in open-world environments remains a fundamental challenge in biodiversity research. Current methods treat identification and discovery as separate problems, with classification models assuming closed sets and discovery relying on threshold-based rejection. Here we present DeepTaxon, a retrieval-augmented multimodal framework that unifies species identification and discovery through interpretable reasoning over retrieved visual evidence. Given a query image, DeepTaxon retrieves the top-$k$ candidate species with $n$ exemplar images each from a retrieval index and performs chain-of-thought comparative reasoning. Critically, we redefine discovery as an explicit, retrieval-based decision problem rather than an implicit parametric memory problem. A sample is novel if and only if the retrieval index lacks sufficient evidence for identification, so each retrieval naturally yields a classification or discovery label without manual annotation, thereby providing automatic supervision for both tasks. We train the framework via supervised fine-tuning on synthetic retrieval-augmented data, followed by reinforcement learning on hard samples, converting high-recall retrieval into high-precision decisions that scale to massive taxonomic vocabularies. Extensive experiments on a large-scale in-distribution benchmark and six out-of-distribution datasets demonstrate consistent improvements in both identification and discovery. Ablation studies further reveal effective test-time scaling with candidate count $k$ and exemplar count $n$, strong zero-shot transfer to unseen domains, and consistent performance across retrieval encoders, establishing an interpretable solution for biodiversity research.

---


### 152. [Robust Grounding with MLLMs against Occlusion and Small Objects via Language-guided Semantic Cues](https://arxiv.org/abs/2604.24036)

**<font color=#1a73e8>作者：</font>** Beomchan Park, Seongho Kim, Hyunjun Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) have enhanced grounding capabilities in general scenes, their robustness in crowded scenes remains underexplored. Crowded scenes entail visual challenges (i.e., occlusion and small objects), which impair object semantics and degrade grounding performance. In contrast, language expressions are immune to such degradation and preserve object semantics. In light of these observations, we propose a novel method that overcomes such constraints by leveraging Language-Guided Semantic Cues (LGSCs). Specifically, our approach introduces a Semantic Cue Extractor (SCE) to derive semantic cues of objects from the visual pipeline of an MLLM. We then guide these cues using corresponding text embeddings to produce LGSCs as linguistic semantic priors. Subsequently, they are reintegrated into the original visual pipeline to refine object semantics. Extensive experiments and analyses demonstrate that incorporating LGSCs into an MLLM effectively improves grounding accuracy in crowded scenes.

---


### 153. [A Limit Theory of Foundation Models: A Mathematical Approach to Understanding Emergent Intelligence and Scaling Laws](https://arxiv.org/abs/2604.24037)

**<font color=#1a73e8>作者：</font>** Jun Shu, Junxiong Jia, Deyu Meng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emergent intelligence have played a major role in the modern AI development. While existing studies primarily rely on empirical observations to characterize this phenomenon, a rigorous theoretical framework remains underexplored. This study attempts to develop a mathematical approach to formalize emergent intelligence from the perspective of limit theory. Specifically, we introduce a performance function E(N, P, K), dependent on data size N, model size P and training steps K, to quantify intelligence behavior. We posit that intelligence emerges as a transition from finite to effectively infinite knowledge, and thus recast emergent intelligence as existence of the limit $\lim_{N,P,K \to \infty} \mathcal{E}(N,P,K)$, with emergent abilities corresponding to the limiting behavior. This limit theory helps reveal that emergent intelligence originates from the existence of a parameter-limit architecture (referred to as the limit architecture), and that emergent intelligence rationally corresponds to the learning behavior of this limit system. By introducing tools from nonlinear Lipschitz operator theory, we prove that the necessary and sufficient conditions for existence of the limit architecture. Furthermore, we derive the scaling law of foundation models by leveraging tools of Lipschitz operator and covering number. Theoretical results show that: 1) emergent intelligence is governed by three key factors-training steps, data size and the model architecture, where the properties of basic blocks play a crucial role in constructing foundation models; 2) the critical condition Lip(T)=1 for emergent intelligence provides theoretical support for existing findings. 3) emergent intelligence is determined by an infinite-dimensional system, yet can be effectively realized in practice through a finite-dimensional architecture. Our empirical results corroborate these theoretical findings.

---


### 154. [AgenticCache: Cache-Driven Asynchronous Planning for Embodied AI Agents](https://arxiv.org/abs/2604.24039)

**<font color=#1a73e8>作者：</font>** Hojoon Kim, Yuheng Wu, Thierry Tambe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Embodied AI agents increasingly rely on large language models (LLMs) for planning, yet per-step LLM calls impose severe latency and cost. In this paper, we show that embodied tasks exhibit strong plan locality, where the next plan is largely predictable from the current one. Building on this, we introduce AgenticCache, a planning framework that reuses cached plans to avoid per-step LLM calls. In AgenticCache, each agent queries a runtime cache of frequent plan transitions, while a background Cache Updater asynchronously calls the LLM to validate and refine cached entries. Across four multi-agent embodied benchmarks, AgenticCache improves task success rate by 22% on average across 12 configurations (4 benchmarks x 3 models), reduces simulation latency by 65%, and lowers token usage by 50%. Cache-based plan reuse thus offers a practical path to low-latency, low-cost embodied agents. Code is available at this https URL.

---


### 155. [A2DEPT: Large Language Model-Driven Automated Algorithm Design via Evolutionary Program Trees](https://arxiv.org/abs/2604.24043)

**<font color=#1a73e8>作者：</font>** Bin Chen, Shouliang Zhu, Beidan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing heuristics for combinatorial optimization problems (COPs) is a fundamental yet challenging task that traditionally requires extensive domain expertise. Recently, Large Language Model (LLM)-based Automated Heuristic Design (AHD) has shown promise in autonomously generating heuristic components with minimal human intervention. However, most existing LLM-based AHD methods enforce fixed algorithmic templates to ensure executability, which confines the search to component-level tuning and limits system-level algorithmic expressiveness. To enable open-ended solver synthesis beyond rigid templates, we propose Automated Algorithm Design via Evolutionary Program Trees (A2DEPT), which treats LLMs as system-level algorithm architects. A2DEPT explores the vast program space via a tree-structured evolutionary search with hybrid selection and hierarchical operators, enabling iterative refinement of complete algorithms. To make open-ended generation practical, we enforce executability with a lightweight program-maintenance loop that performs feedback-driven repair. In experiments, A2DEPT consistently outperforms representative LLM-based baselines on both standard and highly constrained benchmarks. On the standard benchmarks, it reduces the mean normalized optimality gap by 9.8% relative to the strongest competing AHD baseline.

---


### 156. [QEVA: A Reference-Free Evaluation Metric for Narrative Video Summarization with Multimodal Question Answering](https://arxiv.org/abs/2604.24052)

**<font color=#1a73e8>作者：</font>** Woojun Jung, Junyeong Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-to-text summarization remains underexplored in terms of comprehensive evaluation methods. Traditional n-gram overlap-based metrics and recent large language model (LLM)-based approaches depend heavily on human-written reference summaries, limiting their practicality and sensitivity to nuanced semantic aspects. In this paper, we propose QEVA, a reference-free metric evaluating candidate summaries directly against source videos through multimodal question answering. QEVA assesses summaries along three clear dimensions: Coverage, Factuality, and Chronology. We also introduce MLVU(VS)-Eval, a new annotated benchmark derived from the MLVU dataset, comprising 800 summaries generated from 200 videos using state-of-the-art video-language multimodal models. This dataset establishes a transparent and consistent framework for evaluation. Experimental results demonstrate that QEVA shows higher correlation with human judgments compared to existing approaches, as measured by Kendall's $\tau_b$, $\tau_c$, and Spearman's $\rho$. We hope that our benchmark and metric will facilitate meaningful progress in video-to-text summarization research and provide valuable insights for the development of future evaluation methods.

---


### 157. [Grounding Before Generalizing: How AI Differs from Humans in Causal Transfer](https://arxiv.org/abs/2604.24062)

**<font color=#1a73e8>作者：</font>** Liangru Xiang, Yuxi Ma, Zhihao Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extracting abstract causal structures and applying them to novel situations is a hallmark of human intelligence. While Large Language Models (LLMs) and Vision Language Models (VLMs) have shown strong performance on a wide range of reasoning tasks, their capacity for interactive causal learning -- inducing latent structures through sequential exploration and transferring them across contexts -- remains uncharacterized. Human learners accomplish such transfer after minimal exposure, whereas classical Reinforcement Learning (RL) agents fail catastrophically. Whether state-of-the-art Artificial Intelligence (AI) models possess human-like mechanisms for abstract causal structure transfer is an open question. Using the OpenLock paradigm requiring sequential discovery of Common Cause (CC) and Common Effect (CE) structures, here we show that models exhibit fundamentally delayed or absent transfer: even successful models require initial environmental-specific mapping -- what we term environmental grounding -- before efficiency gains emerge, whereas humans leverage prior structural knowledge from the very first solution attempt. In the text-only condition, models matched or exceeded human discovery efficiency. In contrast, visual information -- in both the image-only and text-and-image conditions -- overall degraded rather than enhanced performance, revealing a broad reliance on symbolic processing rather than integrated multimodal reasoning. Models further exhibited systematic CC/CE asymmetries absent in humans, suggesting heuristic biases rather than direction-neutral causal abstraction. These findings reveal that large-scale statistical learning does not produce the decontextualized causal schemas underpinning human analogical reasoning, establishing grounding-dependent transfer as a fundamental limitation of current LLMs and VLMs.

---


### 158. [An Information-Geometric Framework for Stability Analysis of Large Language Models under Entropic Stress](https://arxiv.org/abs/2604.24076)

**<font color=#1a73e8>作者：</font>** Hikmat Karimov, Rahid Zahid Alekberli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed in high-stakes and operational settings, evaluation strategies based solely on aggregate accuracy are often insucient to characterize system reliability. This study proposes a thermodynamic inspired modeling framework for analyzing the stability of LLM outputs under conditions of uncertainty and perturbation. The framework introduces a composite stability score that integrates task utility, entropy as a measure of external uncertainty, and two internal structural proxies: internal integration and aligned reective capacity. Rather than interpreting these quantities as physical variables, the formulation is intended as an interpretable abstraction that captures how internal structure may modulate the impact of disorder on model behavior. Using the IST-20 benchmarking protocol and associated metadata, we analyze 80 modelscenario observations across four contemporary LLMs. The proposed formulation consistently yields higher stability scores than a reduced utilityentropy baseline, with a mean improvement of 0.0299 (95% CI: 0.02470.0351). The observed gain is more pronounced under higher entropy conditions, suggesting that the framework captures a form of nonlinear attenuation of uncertainty. We do not claim a fundamental physical law or a complete theory of machine ethics. Instead, the contribution of this work is a compact and interpretable modeling perspective that connects uncertainty, performance, and internal structure within a unied evaluation lens. The framework is intended to complement existing benchmarking approaches and to support ongoing discussions in AI safety, reliability, and governance.

---


### 159. [The Pragmatic Persona: Discovering LLM Persona through Bridging Inference](https://arxiv.org/abs/2604.24079)

**<font color=#1a73e8>作者：</font>** Jisoo Yang, Jongwon Ryu, Minuk Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) reveal inherent and distinctive personas through dialogue. However, most existing persona discovery approaches rely on surface-level lexical or stylistic cues, treating dialogue as a flat sequence of tokens and failing to capture the deeper discourse-level structures that sustain persona consistency. To address this limitation, we propose a novel analytical framework that interprets LLM dialogue through bridging inference -- implicit conceptual relations that connect utterances via shared world knowledge and discourse coherence. By modeling these relations as structured knowledge graphs, our approach captures latent semantic links that govern how LLMs organize meaning across turns, enabling persona discovery at the level of discourse coherence rather than surface realizations. Experimental results across multiple reasoning backbones and target LLMs, ranging from small-scale models to 80B-parameter systems, demonstrate that bridging-inference graphs yield significantly stronger semantic coherence and more stable persona identification than frequency or style-based baselines. These results show that persona traits are consistently encoded in the structural organization of discourse rather than isolated lexical patterns. This work presents a systematic framework for probing, extracting, and visualizing latent LLM personas through the lens of Cognitive Discourse Theory, bridging computational linguistics, cognitive semantics, and persona reasoning in large language models. Codes are available at this https URL

---


### 160. [Open-Vocabulary Semantic Segmentation Network Integrating Object-Level Label and Scene-Level Semantic Features for Multimodal Remote Sensing Images](https://arxiv.org/abs/2604.24125)

**<font color=#1a73e8>作者：</font>** Jinkun Dai, Yuanxin Ye, Peng Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation of multi-modal remote sensing imagery plays a pivotal role in land use/land cover (LULC) mapping, environmental monitoring, and precision earth observation. Current multi-modal approaches mainly focus on integrating complementary visual modalities, yet neglect the incorporating of non-visual textual data - a rich source of knowledge that can bridge semantic gaps between visual patterns and real-world concepts. To address this limitation, we propose TSMNet, a text supervised multi-modal open vocabulary semantic segmentation network that synergistically integrates textual supervision with visual representation for open-vocabulary semantic segmentation. Unlike conventional multi-modal segmentation frameworks, TSMNet introduces a dual-branch text encoder to extract both scene-level semantic and object-level label information from various textual data, enabling dynamic cross-modal fusion. These text-derived features dynamically interact with visual embeddings through the proposed text-guided visual semantic fusion module, enabling domain-aware feature refinement and human-interpretable decision-making. To verify our method, we innovatively construct two new multi-modal datasets, and carry out extensive experiments to make a comprehensive comparison between the proposed method and other state-of-the-art (SOTA) semantic segmentation models. Results demonstrate that TSMNet achieves superior segmentation accuracy while exhibiting robust generalization capabilities across diverse geographical and sensor-specific scenarios. This work establishes a new paradigm for explainable remote sensing analysis, demonstrating that textual knowledge integration significantly enhances model generalizability. The source code will be available at this https URL

---


### 161. [Leveraging Human Feedback for Semantically-Relevant Skill Discovery](https://arxiv.org/abs/2604.24127)

**<font color=#1a73e8>作者：</font>** Maxence Hussonnois, Thommen George Karimpanal, Santu Rana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised skill discovery in reinforcement learning aims to intrinsically motivate agents to discover diverse and useful behaviours. However, unconstrained approaches can produce unsafe, unethical, or misaligned behaviours. To mitigate these risks and improve the practical desireability of discovered skills, recent work grounds the discovery process by leveraging human preference feedback. However, preference-based approaches are feedback-inefficient and inherently ill-equipped to deal with skill spaces composed of a variety of different skills such as running, jumping, walking, etc. To overcome this limitation, we introduce semantic labelling, a novel and feedback-efficient approach that leverages human cognitive strengths to identify and label semantically meaningful behaviours. Based on semantic labelling, we propose Semantically Relevant Skill Discovery (SRSD), a novel human-in-the-loop approach that collects semantic labels from human feedback and learns a reward function to encourage skills to be more semantically diverse and relevant. Through our experiments in a 2D navigation environment and four locomotion environments, we demonstrate that SRSD can improve semantic diversity and discover relevant behaviours while scaling effectively to a large variety of behaviours.

---


### 162. [EXACT: an explainable anomaly-aware vision foundation model for analysis of 3D chest CT](https://arxiv.org/abs/2604.24146)

**<font color=#1a73e8>作者：</font>** Xuguang Bai, Mingxuan Liu, Tongxi Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest computed tomography (CT) is central to the detection and management of thoracic disease, yet the growing scale and complexity of volumetric imaging increasingly exceed what can be addressed by scan-level prediction alone. Clinically useful AI for CT must not only recognize disease across the whole volume, but also localize abnormalities and provide interpretable visual evidence. Existing vision-language foundation models typically compress scans and reports into global image-text representations, limiting their ability to preserve spatial evidence and support clinically meaningful interpretation. Here we developed EXACT, an explainable anomaly-aware foundation model for three-dimensional chest CT that learns spatially resolved representations from paired clinical scans and radiology reports. EXACT was pre-trained on 25,692 CT-reports pairs using anatomy-aware weak supervision, jointly learning organ segmentation and multi-instance anomaly localization without manual voxel-level annotations. The resulting organ-specific anomaly-aware maps assign each voxel a disease-specific anomaly score confined to its corresponding anatomy, jointly encoding lesion extent and organ-level context. In retrospective multinational and multi-center evaluations, EXACT showed broad and consistent improvements across clinically relevant CT tasks, spanning multi-disease diagnosis, zero-shot anomaly localization, downstream adaptation, and visually grounded report generation, outperforming existing three-dimensional medical foundation models. By transforming routine clinical CT scans and free-text reports into explainable voxel-level representations, EXACT establishes a scalable paradigm for trustworthy volumetric medical AI.

---


### 163. [Multi-Dimensional Evaluation of Sustainable City Trips with LLM-as-a-Judge and Human-in-the-Loop](https://arxiv.org/abs/2604.24158)

**<font color=#1a73e8>作者：</font>** Ashmi Banerjee, Adithi Satish, Wolfgang Wörndl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating nuanced conversational travel recommendations is challenging when human annotations are costly and standard metrics ignore stakeholder-centric goals. We study LLMs-as-Judges for sustainable city-trip lists across four dimensions -- relevance, diversity, sustainability, and popularity balance, and propose a three-phase calibration framework: (1) baseline judging with multiple LLMs, (2) expert evaluation to identify systematic misalignment, and (3) dimension-specific calibration via rules and few-shot examples. Across two recommendation settings, we observe model-specific biases and high dimension-level variance, even when judges agree on overall rankings. Calibration clarifies reasoning per dimension but exposes divergent interpretations of sustainability, highlighting the need for transparent, bias-aware LLM evaluation. Prompts and code are released for reproducibility: this https URL.

---


### 164. [POCA: Pareto-Optimal Curriculum Alignment for Visual Text Generation](https://arxiv.org/abs/2604.24171)

**<font color=#1a73e8>作者：</font>** Yaohou Fan, Qingzhong Wang, Yongsong Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current visual text generation models struggle with the trade-off between text accuracy and overall image coherence. We find that achieving high text accuracy can reduce aesthetic quality and instruction-following capability. Although reinforcement learning approaches can alleviate the problem through aligning with multiple rewards, they are often unstable for text generation, as existing approaches normally optimize multiple rewards in a weighted-sum way. In addition, it is difficult to balance the weight of each reward. Moreover, reinforcement learning requires a set of training instructions. A large number of prompts require more training time and computing resources, while a small set leads to poor performance. Hence, how to select the prompts for efficient training is an unsolved problem. In this study, we propose Pareto-Optimal Curriculum Alignment (POCA), a framework that addresses this issue as a multi-objective problem by: 1) identifying the Pareto-optimal set to avoid simple scalarization and 2) designing an adaptive curriculum alignment strategy to manage a learning sequence of a multi-reward dataset using automatic difficulty assessment, which is crucial for optimal convergence as RL methods explore in a limited data environment. In synergy, POCA finds the Pareto-optimal set in a unified reward space, which eliminates inconsistent signals to find the best trade-off solution from different rewards under an easy-to-hard optimization landscape. The experimental results show that POCA significantly improves all metrics such as CLIP, HPS scores and sentence accuracy.

---


### 165. [AdapTime: Enabling Adaptive Temporal Reasoning in Large Language Models](https://arxiv.org/abs/2604.24175)

**<font color=#1a73e8>作者：</font>** Yimin Deng, Yejing Wang, Zhenxi Lin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have demonstrated strong reasoning capabilities in general knowledge question answering. However, their ability to handle temporal information remains limited. To address this limitation, existing approaches often involve external tools or manual verification and are tailored to specific scenarios, leading to poor generalizability. Moreover, these methods apply a fixed pipeline to all questions, overlooking the fact that different types of temporal questions require distinct reasoning strategies, which leads to unnecessary processing for simple cases and inadequate reasoning for complex ones. To this end, we propose AdapTime, an adaptive temporal reasoning method that dynamically executes reasoning steps based on the input context. Specifically, it involves three temporal reasoning actions: reformulate, rewrite and review, with an LLM planner guiding the reasoning process. AdapTime integrates seamlessly with state-of-the-art LLMs and significantly enhances their temporal reasoning capabilities without relying on external support. Extensive experiments demonstrate the effectiveness of our approach.

---


### 166. [Meta-Aligner: Bidirectional Preference-Policy Optimization for Multi-Objective LLMs Alignment](https://arxiv.org/abs/2604.24178)

**<font color=#1a73e8>作者：</font>** Wenzhe Xu, Biao Liu, Yiyang Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-Objective Alignment aims to align Large Language Models (LLMs) with diverse and often conflicting human values by optimizing multiple objectives simultaneously. Existing methods predominantly rely on static preference weight construction strategies. However, rigidly aligning to fixed targets discards valuable intermediate information, as training responses inherently embody valid preference trade-offs even when deviating from the target. To address this limitation, we propose Meal, i.e., MEta ALigner, a bi-level meta-learning framework enabling bidirectional optimization between preferences and policy responses, generating instructive dynamic preferences for steadier training. Specifically, we introduce a preference-weight-net as a meta-learner to generate adaptive preference weights based on input prompts and update the preference weights as learnable parameters, while the LLM policy acts as a base-learner optimizing response generation conditioned on these preferences with rejection sampling strategy. Extensive empirical results demonstrate that our method achieves superior performance on several multi-objective benchmarks, validating the effectiveness of the dynamic bidirectional preference-policy optimization framework.

---


### 167. [MemeScouts@LT-EDI 2026: Asking the Right Questions -- Prompted Weak Supervision for Meme Hate Speech Detection](https://arxiv.org/abs/2604.24179)

**<font color=#1a73e8>作者：</font>** Ivo Bueno, Lea Hirlimann, Enkelejda Kasneci  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting hate speech in memes is challenging due to their multimodal nature and subtle, culturally grounded cues such as sarcasm and context. While recent vision-language models (VLMs) enable joint reasoning over text and images, end-to-end prompting can be brittle, as a single prediction must resolve target, stance, implicitness, and irony. These challenges are amplified in multilingual settings. We propose a prompted weak supervision (PWS) approach that decomposes meme understanding into targeted, question-based labeling functions with constrained answer options for homophobia and transphobia detection in the LT-EDI 2026 shared task. Using a quantized Qwen3-VLM to extract features by answering targeted questions, our method outperforms direct VLM classification, with substantial gains for Chinese and Hindi, ranking 1st in English, 2nd in Chinese, and 3rd in Hindi. Iterative refinement via error-driven LF expansion and feature pruning reduces redundancy and improves generalization. Our results highlight the effectiveness of prompted weak supervision for multilingual multimodal hate speech detection.

---


### 168. [MultiDx: A Multi-Source Knowledge Integration Framework towards Diagnostic Reasoning](https://arxiv.org/abs/2604.24186)

**<font color=#1a73e8>作者：</font>** Yimin Deng, Zhenxi Lin, Yejing Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diagnostic prediction and clinical reasoning are critical tasks in healthcare applications. While Large Language Models (LLMs) have shown strong capabilities in commonsense reasoning, they still struggle with diagnostic reasoning due to limited domain knowledge. Existing approaches often rely on internal model knowledge or static knowledge bases, resulting in knowledge insufficiency and limited adaptability, which hinder their capacity to perform diagnostic reasoning. Moreover, these methods focus solely on the accuracy of final predictions, overlooking alignment with standard clinical reasoning trajectories. To this end, we propose MultiDx, a two-stage diagnostic reasoning framework that performs differential diagnosis by analyzing evidence collected from multiple knowledge sources. Specifically, it first generates suspected diagnoses and reasoning paths by leveraging knowledge from web search, SOAP-formatted case, and clinical case database. Then it integrates multi-perspective evidence through matching, voting, and differential diagnosis to generate the final prediction.~Extensive experiments on two public benchmarks demonstrate the effectiveness of our approach.

---


### 169. [Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis](https://arxiv.org/abs/2604.24198)

**<font color=#1a73e8>作者：</font>** Zhisong Qiu, Shuofei Qiao, Kewei Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Process Reward Models (PRMs) have achieved remarkable success in augmenting the reasoning capabilities of Large Language Models (LLMs) within static domains such as mathematics. However, their potential in dynamic data analysis tasks remains underexplored. In this work, we first present a empirical study revealing that general-domain PRMs struggle to supervise data analysis agents. Specifically, they fail to detect silent errors, logical flaws that yield incorrect results without triggering interpreter exceptions, and erroneously penalize exploratory actions, mistaking necessary trial-and-error exploration for grounding failures. To bridge this gap, we introduce DataPRM, a novel environment-aware generative process reward model that (1) can serve as an active verifier, autonomously interacting with the environment to probe intermediate execution states and uncover silent errors, and (2) employs a reflection-aware ternary reward strategy that distinguishes between correctable grounding errors and irrecoverable mistakes. We design a scalable pipeline to construct over 8K high-quality training instances for DataPRM via diversity-driven trajectory generation and knowledge-augmented step-level annotation. Experimental results demonstrate that DataPRM improves downstream policy LLMs by 7.21% on ScienceAgentBench and 11.28% on DABStep using Best-of-N inference. Notably, with only 4B parameters, DataPRM outperforms strong baselines, and exhibits robust generalizability across diverse Test-Time Scaling strategies. Furthermore, integrating DataPRM into Reinforcement Learning yields substantial gains over outcome-reward baselines, achieving 78.73% on DABench and 64.84% on TableBench, validating the effectiveness of process reward supervision. Code is available at this https URL.

---


### 170. [BitRL: Reinforcement Learning with 1-bit Quantized Language Models for Resource-Constrained Edge Deployment](https://arxiv.org/abs/2604.24273)

**<font color=#1a73e8>作者：</font>** Md. Ashiq Ul Islam Sajid, Mohammad Sakib Mahmood, Md. Tareq Hasan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The deployment of intelligent reinforcement learning (RL) agents on resource-constrained edge devices remains a fundamental challenge due to the substantial memory, computational, and energy requirements of modern deep learning systems. While large language models (LLMs) have emerged as powerful architectures for decision-making agents, their multi-billion parameter scale confines them to cloud-based deployment, raising concerns about latency, privacy, and connectivity dependence.
We introduce BitRL, a framework for building RL agents using 1-bit quantized language models that enables practical on-device learning and inference under severe resource constraints. Leveraging the BitNet b1.58 architecture with ternary weights (-1, 0, +1) and an optimized inference stack, BitRL achieves 10-16x memory reduction and 3-5x energy efficiency improvements over full-precision baselines while maintaining 85-98 percent of task performance across benchmarks.
We provide theoretical analysis of quantization as structured parameter perturbation, derive convergence bounds for quantized policy gradients under frozen-backbone architectures, and identify the exploration-stability trade-off in extreme quantization. Our framework systematically integrates 1-bit quantized language models with reinforcement learning for edge deployment and demonstrates effectiveness on commodity hardware.

---


### 171. [Differentiable Faithfulness Alignment for Cross-Model Circuit Transfer](https://arxiv.org/abs/2604.24302)

**<font color=#1a73e8>作者：</font>** Shun Shao, Binxu Wang, Shay B. Cohen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability has made it possible to localize circuits underlying specific behaviors in language models, but existing methods are expensive, model-specific, and difficult to scale to larger architectures. We introduce \textbf{Differentiable Faithfulness Alignment (DFA)}, a framework that transfers circuit information from a smaller source model to a larger target model through a learned differentiable alignment. DFA projects source-model node importance scores into the target model and trains this mapping with a soft faithfulness objective, avoiding full circuit discovery on the target model. We evaluate DFA on Llama-3 and Qwen-2.5 across six tasks spanning factual retrieval, multiple-choice reasoning, and arithmetic. The strongest results occur on Llama-3 $1$B$\rightarrow3$B, where aligned circuits are often competitive with direct node attribution and zero-shot transfer remains effective. Recovery weakens for larger source--target gaps and is substantially lower on Qwen-2.5, suggesting that transfer becomes harder as architectural and scaling differences increase. Overall, DFA consistently outperforms simple baselines and, in some settings, recovers target-model circuits with faithfulness comparable to or stronger than direct attribution. These results suggest that smaller models can provide useful mechanistic priors for larger ones, while highlighting both the promise and the limits of node-level cross-model circuit alignment.\footnote{Code is available at this https URL.

---


### 172. [DPEPO: Diverse Parallel Exploration Policy Optimization for LLM-based Agents](https://arxiv.org/abs/2604.24320)

**<font color=#1a73e8>作者：</font>** Junshuo Zhang, Chengrui Huang, Feng Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents that follow the sequential "reason-then-act" paradigm have achieved superior performance in many complex this http URL, these methods suffer from limited exploration and incomplete environmental understanding, as they interact with only a single environment per step. In this paper, we first introduce a novel paradigm that enables an agent to interact with multiple environments simultaneously and share cross-trajectory experiences. Building upon this paradigm, we further propose DPEPO, a reinforcement learning (RL) algorithm that encourages the agent to perform diverse parallel exploration. There are two stages in DPEPO: initial supervised fine-tuning (SFT) imparts basic parallel reasoning and action generation, followed by reinforcement learning stage with a hierarchical reward scheme. We design a parallel trajectory-level success reward and two step-level rewards: Diverse Action Reward and Diverse State Transition Reward, which actively penalize behavioral redundancy and promote broad exploration. Extensive experiments on ALFWorld and ScienceWorld show that DPEPO achieves state-of-the-art (SOTA) success rates, while maintaining comparable efficiency to strong sequential baselines. (Code is available at this https URL)

---


### 173. [OS-SPEAR: A Toolkit for the Safety, Performance,Efficiency, and Robustness Analysis of OS Agents](https://arxiv.org/abs/2604.24348)

**<font color=#1a73e8>作者：</font>** Zheng Wu, Yi Hua, Zhaoyuan Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The evolution of Multimodal Large Language Models (MLLMs) has shifted the focus from text generation to active behavioral execution, particularly via OS agents navigating complex GUIs. However, the transition of these agents into trustworthy daily partners is hindered by a lack of rigorous evaluation regarding safety, efficiency, and multi-modal robustness. Current benchmarks suffer from narrow safety scenarios, noisy trajectory labeling, and limited robustness metrics. To bridge this gap, we propose OS-SPEAR, a comprehensive toolkit for the systematic analysis of OS agents across four dimensions: Safety, Performance, Efficiency, and Robustness. OS-SPEAR introduces four specialized subsets: (1) a S(afety)-subset encompassing diverse environment- and human-induced hazards; (2) a P(erformance)-subset curated via trajectory value estimation and stratified sampling; (3) an E(fficiency)-subset quantifying performance through the dual lenses of temporal latency and token consumption; and (4) a R(obustness)-subset that applies cross-modal disturbances to both visual and textual inputs. Additionally, we provide an automated analysis tool to generate human-readable diagnostic reports. We conduct an extensive evaluation of 22 popular OS agents using OS-SPEAR. Our empirical results reveal critical insights into the current landscape: notably, a prevalent trade-off between efficiency and safety or robustness, the performance superiority of specialized agents over general-purpose models, and varying robustness vulnerabilities across different modalities. By providing a multidimensional ranking and a standardized evaluation framework, OS-SPEAR offers a foundational resource for developing the next generation of reliable and efficient OS agents. The dataset and codes are available at this https URL.

---


### 174. [DPRM: A Plug-in Doob h transform-induced Token-Ordering Module for Diffusion Language Models](https://arxiv.org/abs/2604.24357)

**<font color=#1a73e8>作者：</font>** Dake Bu, Wei Huang, Andi Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models generate without a fixed left-to-right order, making token ordering a central algorithmic choice: which tokens should be revealed, retained, revised or verified at each step? Existing systems mainly use random masking or confidence-driven ordering. Random masking creates train--test mismatch, while confidence-only rules are efficient but can be myopic and suppress useful exploration.
We introduce DPRM (Doob h-transform Process Reward Model), a plug-in token-ordering module for diffusion language models. DPRM keeps the host architecture, denoising objective and supervision unchanged, and changes only the ordering policy. It starts from confidence-driven progressive ordering and gradually shifts to Doob h transform Process Reward guided ordering through online estimates.
We characterize the exact DPRM policy as a reward-tilted Gibbs reveal law, prove O(1/N) convergence of the stagewise Soft-BoN approximation, and show that the online bucketized controller tracks the exact DPRM score at empirical-Bernstein rates. Under tractable optimization assumptions, DPRM also yields a sample-complexity advantage over random and confidence-only ordering.
DPRM improves over confidence-based baselines in pretraining, post-training, test-time scaling, and single-cell masked diffusion, with particularly strong gains on harder reasoning subsets. In protein, molecular generation and DNA design, the effect is more multi-objective: ordering-aware variants significantly improve selected structural or fragment-constrained metrics while not uniformly dominating the host baseline on every quality metric. These results identify token ordering as a fundamental control axis in diffusion language models and establish DPRM as a general-purpose module for improving it. Code is available at this https URL.

---


### 175. [Culture-Aware Machine Translation in Large Language Models: Benchmarking and Investigation](https://arxiv.org/abs/2604.24361)

**<font color=#1a73e8>作者：</font>** Zekun Yuan, Yangfan Ye, Xiaocheng Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved strong performance in general machine translation, yet their ability in culture-aware scenarios remains poorly understood. To bridge this gap, we introduce CanMT, a Culture-Aware Novel-Driven Parallel Dataset for Machine Translation, together with a theoretically grounded, multi-dimensional evaluation framework for assessing cultural translation quality. Leveraging CanMT, we systematically evaluate a wide range of LLMs and translation systems under different translation strategy constraints. Our findings reveal substantial performance disparities across models and demonstrate that translation strategies exert a systematic influence on model behavior. Further analysis shows that translation difficulty varies across types of culture-specific items, and that a persistent gap remains between models' recognition of culture-specific knowledge and their ability to correctly operationalize it in translation outputs. In addition, incorporating reference translations is shown to substantially improve evaluation reliability in LLM-as-a-judge, underscoring their essential role in assessing culture-aware translation quality. The corpus and code are available at CanMT.

---


### 176. [Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency](https://arxiv.org/abs/2604.24380)

**<font color=#1a73e8>作者：</font>** Yiran Huang, Lukas Thede, Massimiliano Mancini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Vision Language Models (LVLMs) demonstrate impressive capabilities, their substantial computational and memory requirements pose deployment challenges on resource-constrained edge devices. Current parameter reduction techniques primarily involve training LVLMs from small language models, but these methods offer limited flexibility and remain computationally intensive. We study a complementary route: compressing existing LVLMs by applying structured pruning to the language model backbone, followed by lightweight recovery training. Specifically, we investigate two structural pruning paradigms: layerwise and widthwise pruning, and pair them with supervised finetuning and knowledge distillation on logits and hidden states. Additionally, we assess the feasibility of conducting recovery training with only a small fraction of the available data. Our results show that widthwise pruning generally maintains better performance in low-resource scenarios, where computational resources are limited or there is insufficient finetuning data. As for the recovery training, finetuning only the multimodal projector is sufficient at small compression levels. Furthermore, a combination of supervised finetuning and hidden-state distillation yields optimal recovery across various pruning levels. Notably, effective recovery can be achieved using just 5% of the original data, while retaining over 95% of the original performance. Through empirical study on three representative LVLM families ranging from 3B to 7B parameters, this study offers actionable insights for practitioners to compress LVLMs without extensive computation resources or sufficient data. The code base is available at this https URL.

---


### 177. [Aligning with Your Own Voice: Self-Corrected Preference Learning for Hallucination Mitigation in LVLMs](https://arxiv.org/abs/2604.24395)

**<font color=#1a73e8>作者：</font>** Byeonggeuk Lim, JungMin Yun, Junehyoung Kwon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) frequently suffer from hallucinations. Existing preference learning-based approaches largely rely on proprietary models to construct preference datasets. We identify that this reliance introduces a distributional mismatch between the proprietary and target models that hinders efficient alignment. To address this, we propose Alignment via VErified Self-correction DPO (AVES-DPO), a framework that aligns LVLMs using in-distribution data derived from the model's intrinsic knowledge. Our approach employs a consensus-based verification mechanism to diagnose diverse hallucinations and guides the model to self-correct, thereby generating preference pairs strictly compatible with its internal distribution. Extensive experiments demonstrate that AVES-DPO surpasses existing baselines in hallucination mitigation while requiring only 5.2k samples.

---


### 178. [Global Context or Local Detail? Adaptive Visual Grounding for Hallucination Mitigation](https://arxiv.org/abs/2604.24396)

**<font color=#1a73e8>作者：</font>** Yubo Jiang, Xin Yang, Abudukelimu Wuerkaixi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are frequently undermined by object hallucination--generating content that contradicts visual reality--due to an over-reliance on linguistic priors. We introduce Positive-and-Negative Decoding (PND), a training-free inference framework that intervenes directly in the decoding process to enforce visual fidelity. PND is motivated by our key finding of a critical attention deficit in VLMs, where visual features are empirically under-weighted. Our framework corrects this via a dual-path contrast: The positive path amplifies salient visual evidence using multi-layer attention to encourage faithful descriptions, directly counteracting the attention deficit. Simultaneously, the negative path identifies and degrades the core object's features to create a strong counterfactual, which penalizes ungrounded, prior-dominant generation. By contrasting the model's outputs from these two perspectives at each step, PND steers generation towards text that is not just linguistically probable, but visually factual. Extensive experiments on benchmarks like POPE, MME, and CHAIR show that PND achieves state-of-the-art performance with up to 6.5% accuracy improvement, substantially reducing object hallucination while also enhancing descriptive detail--all without requiring any model retraining. The method generalizes effectively across diverse VLM architectures including LLaVA, InstructBLIP, InternVL, and Qwen-VL.

---


### 179. [How Personal Characteristics Shape User Exploration of Diverse Movie Recommendations with a LLM-Based Multi-Agent System](https://arxiv.org/abs/2604.24405)

**<font color=#1a73e8>作者：</font>** Yufan Zhou, Yirui Huang, Zhao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Diversity is an important evaluation criterion for recommender systems beyond accuracy, yet users differ in their willingness to engage with novel and diverse content. In this work, we investigate how a Large Language Model (LLM)-based multi-agent system supports users' exploration of diverse recommendations, and how individual characteristics shape user experiences. We conducted a between-subjects user study (N = 100) comparing a single-agent system (baseline) with a multi-agent system for movie recommendations. We measured Perceived Accuracy, diversity, novelty, and overall rating, and examined the influence of personal characteristics, including personality traits, demographics, GenAI recommendation experience, and GenAI skepticism. Results show that the multi-agent system significantly increases Perceived Novelty and Shannon Diversity. Conscientiousness is positively associated with Perceived Accuracy and diversity, whereas extraversion is negatively associated with Perceived Diversity. Prior experience with GenAI-based recommendations is positively associated with Shannon Diversity, while skepticism toward GenAI is negatively associated with it. We also observe significant interaction effects between system design and user characteristics. These findings highlight the importance of personality-aware conversational recommender systems and caution against one-size-fits-all multi-agent designs.

---


### 180. [Scaling Properties of Continuous Diffusion Spoken Language Models](https://arxiv.org/abs/2604.24416)

**<font color=#1a73e8>作者：</font>** Jason Ramapuram, Eeshan Gunesh Dhekane, Amitis Shidani 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-only spoken language models (SLMs) lag behind text and text-speech models in performance, with recent discrete autoregressive (AR) SLMs indicating significant computational and data demands to match text models. Since discretizing continuous speech for AR creates bottlenecks, we explore whether continuous diffusion (CD) SLM is more viable. To quantify the SLMs linguistic quality, we introduce the phoneme Jensen-Shannon divergence (pJSD) metric. Our analysis reveals CD SLMs, mirroring AR behavior, exhibit scaling laws for validation loss and pJSD, and show optimal token-to-parameter ratios decreasing as compute scales. However, for the latter, loss becomes insensitive to choice of data and model sizes, showing potential for fast inference. Scaling CD SLMs to 16B parameters with tens of millions of hours of conversational data enables generation of emotive, prosodic, multi-speaker, multilingual speech, though achieving long-form coherence remains a significant challenge.

---


### 181. [A Multi-Dimensional Audit of Politically Aligned Large Language Models](https://arxiv.org/abs/2604.24429)

**<font color=#1a73e8>作者：</font>** Lisa Korver, Mohamed Mostagir, Sherief Reda  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As the application of Large Language Models (LLMs) spreads across various industries, there are increasing concerns about the potential for their misuse, especially in sensitive areas such as political discourse. Deliberately aligning LLMs with specific political ideologies, through prompt engineering or fine-tuning techniques, can be advantageous in use cases such as political campaigns, but requires careful consideration due to heightened risks of performance degradation, misinformation, or increased biased behavior. In this work, we propose a multi-dimensional framework inspired by Habermas' Theory of Communicative Action to audit politically aligned language models across four dimensions: effectiveness, fairness, truthfulness, and persuasiveness using automated, quantitative metrics. Applying this to nine popular LLMs aligned via fine-tuning or role-playing revealed consistent trade-offs: while larger models tend to be more effective at role-playing political ideologies and truthful in their responses, they were also less fair, exhibiting higher levels of bias in the form of angry and toxic language towards people of different ideologies. Fine-tuned models exhibited lower bias and more effective alignment than the corresponding role-playing models, but also saw a decline in performance reasoning tasks and an increase in hallucinations. Overall, all of the models tested exhibited some deficiency in at least one of the four metrics, highlighting the need for more balanced and robust alignment strategies. Ultimately, this work aims to ensure politically-aligned LLMs generate legitimate, harmless arguments, offering a framework to evaluate the responsible political alignment of these models.

---


### 182. [AutoGUI-v2: A Comprehensive Multi-Modal GUI Functionality Understanding Benchmark](https://arxiv.org/abs/2604.24441)

**<font color=#1a73e8>作者：</font>** Hongxin Li, Xiping Wang, Jingran Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous agents capable of navigating Graphical User Interfaces (GUIs) hold the potential to revolutionize digital productivity. However, achieving true digital autonomy extends beyond reactive element matching; it necessitates a predictive mental model of interface dynamics and the ability to foresee the "digital world state" resulting from interactions. Despite the perceptual capabilities of modern Vision-Language Models (VLMs), existing benchmarks remain bifurcated (focusing either on black-box task completion or static, shallow grounding), thereby failing to assess whether agents truly comprehend the implicit functionality and transition logic of GUIs. To bridge this gap, we introduce AutoGUI-v2, a comprehensive benchmark designed to evaluate deep GUI functionality understanding and interaction outcome prediction. We construct the benchmark using a novel VLM-human collaborative pipeline that recursively parses multi-platform screenshots into hierarchical functional regions to generate diverse evaluation tasks. Providing 2,753 tasks across six operating systems, AutoGUI-v2 rigorously tests agents on region and element-level semantics, grounding, and dynamic state prediction. Our evaluation reveals a striking dichotomy in VLMs: while open-source models fine-tuned on agent data (e.g., Qwen3-VL) excel at functional grounding, commercial models (e.g., Gemini-2.5-Pro-Thinking) dominate in functionality captioning. Crucially, all models struggle with complex interaction logic of uncommon actions, highlighting that deep functional understanding remains a significant hurdle. By systematically measuring these foundational capabilities, AutoGUI-v2 offers a new lens for advancing the next generation of GUI agents.

---


### 183. [PhysNote: Self-Knowledge Notes for Evolvable Physical Reasoning in Vision-Language Model](https://arxiv.org/abs/2604.24443)

**<font color=#1a73e8>作者：</font>** Sinin Zhang, Yunfei Xie, Yuxuan Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have demonstrated strong performance on textbook-style physics problems, yet they frequently fail when confronted with dynamic real-world scenarios that require temporal consistency and causal reasoning across frames. We identify two fundamental challenges underlying these failures: (1) spatio-temporal identity drift, where objects lose their physical identity across successive frames and break causal chains, and (2) volatility of inference-time insights, where a model may occasionally produce correct physical reasoning but never consolidates it for future reuse. To address these challenges, we propose PhysNote, an agentic framework that enables VLMs to externalize and refine physical knowledge through self-generated "Knowledge Notes." PhysNote stabilizes dynamic perception through spatio-temporal canonicalization, organizes self-generated insights into a hierarchical knowledge repository, and drives an iterative reasoning loop that grounds hypotheses in visual evidence before consolidating verified knowledge. Experiments on PhysBench demonstrate that PhysNote achieves 56.68% overall accuracy, a 4.96% improvement over the best multi-agent baseline, with consistent gains across all four physical reasoning domains.

---


### 184. [Can You Make It Sound Like You? Post-Editing LLM-Generated Text for Personal Style](https://arxiv.org/abs/2604.24444)

**<font color=#1a73e8>作者：</font>** Connor Baumler, Calvin Bao, Huy Nghiem 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the growing use of large language models (LLMs) for writing tasks, users may hesitate to rely on LLMs when personal style is important. Post-editing LLM-generated drafts or translations is a common collaborative writing strategy, but it remains unclear whether users can effectively reshape LLM-generated text to reflect their personal style. We conduct a pre-registered online study ($n=81$) in which participants post-edit LLM-generated drafts for writing tasks where personal style matters to them. Using embedding-based style similarity metrics, we find that post-editing increases stylistic similarity to participants' unassisted writing and reduces similarity to fully LLM-generated output. However, post-edited text still remains stylistically closer in style to LLM text than to participants' unassisted control text, and it exhibits reduced stylistic diversity compared to unassisted human text. We find a gap between perceived stylistic authenticity and model-measured stylistic similarity, with post-edited text often perceived as representative of participants' personal style despite remaining detectable LLM stylistic traces.

---


### 185. [Zero-shot Large Language Models for Automatic Readability Assessment](https://arxiv.org/abs/2604.24470)

**<font color=#1a73e8>作者：</font>** Riley Grossman, Yi Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unsupervised automatic readability assessment (ARA) methods have important practical and research applications (e.g., ensuring medical or educational materials are suitable for their target audiences). In this paper, we propose a new zero-shot prompting methodology for ARA and present the first comprehensive evaluation of using large language models (LLMs) as an unsupervised ARA method by testing 10 diverse open-source LLMs (e.g., different sizes and developers) on 14 diverse datasets (e.g., different text lengths and languages). Our findings show that our proposed prompting methodology outperforms prior methods on 13 of the 14 datasets. Furthermore, we propose LAURAE, which combines LLM and readability formula scores to improve robustness by capturing both contextual and shallow (e.g., sentence length) features of readability. Our evaluation demonstrates that LAURAE robustly outperforms prior methods across languages, text lengths, and amounts of technical language.

---


### 186. [Agentic clinical reasoning over longitudinal myeloma records: a retrospective evaluation against expert consensus](https://arxiv.org/abs/2604.24473)

**<font color=#1a73e8>作者：</font>** Johannes Moll, Jannik Lübberstedt, Christoph Nuernbergk 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multiple myeloma is managed through sequential lines of therapy over years to decades, with each decision depending on cumulative disease history distributed across dozens to hundreds of heterogeneous clinical documents. Whether LLM-based systems can synthesise this evidence at a level approaching expert agreement has not been established. A retrospective evaluation was conducted on longitudinal clinical records of 811 myeloma patients treated at a tertiary centre (2001-2026), covering 44,962 documents and 1,334,677 laboratory values, with external validation on MIMIC-IV. An agentic reasoning system was compared against single-pass retrieval-augmented generation (RAG), iterative RAG, and full-context input on 469 patient-question pairs from 48 templates at three complexity levels. Reference labels came from double annotation by four oncologists with senior haematologist adjudication. Iterative RAG and full-context input converged on a shared ceiling (75.4% vs 75.8%, p = 1.00). The agentic system reached 79.6% concordance (95% CI 76.4-82.8), exceeding both baselines (+3.8 and +4.2 pp; p = 0.006 and 0.007). Gains rose with question complexity, reaching +9.4 pp on criteria-based synthesis (p = 0.032), and with record length, reaching +13.5 pp in the top decile (n = 10). The system error rate (12.2%) was comparable to expert disagreement (13.6%), but severity was inverted: 57.8% of system errors were clinically significant versus 18.8% of expert disagreements. Agentic reasoning was the only approach to exceed the shared ceiling, with gains concentrated on the most complex questions and longest records. The greater clinical consequence of residual system errors indicates that prospective evaluation in routine care is required before these findings translate into patient benefit.

---


### 187. [Zero-to-CAD: Agentic Synthesis of Interpretable CAD Programs at Million-Scale Without Real Data](https://arxiv.org/abs/2604.24479)

**<font color=#1a73e8>作者：</font>** Mohammadmehdi Ataei, Farzaneh Askari, Kamal Rahimi Malekshan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer-Aided Design (CAD) models are defined by their construction history: a parametric recipe that encodes design intent. However, existing large-scale 3D datasets predominantly consist of boundary representations (B-Reps) or meshes, stripping away this critical procedural information. To address this scarcity, we introduce Zero-to-CAD, a scalable framework for synthesizing executable CAD construction sequences. We frame synthesis as an agentic search problem: by embedding a large language model (LLM) within a feedback-driven CAD environment, our system iteratively generates, executes, and validates code using tools and documentation lookup to promote geometric validity and operation diversity. This agentic approach enables the synthesis of approximately one million executable, readable, editable CAD sequences, covering a rich vocabulary of operations beyond sketch-and-extrude workflows. We also release a curated subset of 100,000 high-quality models selected for geometric diversity. To demonstrate the dataset's utility, we fine-tune a vision-language model on our synthetic data to reconstruct editable CAD programs from multi-view images, outperforming strong baselines, including GPT-5.2, and effectively bootstrapping sequence generation capabilities without real construction-history training data. Zero-to-CAD bridges the gap between geometric scale and parametric interpretability, offering a vital resource for the next generation of CAD AI.

---


### 188. [MIMIC: A Generative Multimodal Foundation Model for Biomolecules](https://arxiv.org/abs/2604.24506)

**<font color=#1a73e8>作者：</font>** Siavash Golkar, Jake Kovalic, Irina Espejo Morales 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biological function emerges from coupled constraints across sequence, structure, regulation, evolution, and cellular context, yet most foundation models in biology are trained within one modality or for a fixed forward task. We present MIMIC, a generative multimodal foundation model trained on our newly curated and aligned dataset, LORE, linking nucleic acid, protein, evolutionary, structural, regulatory, and semantic/contextual modalities within partially observed biomolecular states. MIMIC uses a split-track encoder-decoder architecture to condition on arbitrary subsets of observed modalities and reconstruct or generate missing components of molecular state across the genome, transcriptome, and proteome. Multimodal conditioning consistently improves MIMIC's sequence reconstruction relative to sequence-only inputs, while its learned representations enable state-of-the-art performance on RNA and protein downstream tasks. MIMIC achieves state-of-the-art splicing prediction, and its joint generative formulation enables isoform-aware inference that further improves performance. Beyond prediction, the same generative framework supports constrained design. For RNA, MIMIC identifies corrective edits in a clinically relevant HBB splice-disrupting mutation without reverting it by using evolutionary and structural signals. For proteins, jointly conditioning on shape and surface chemistry of PD-L1 and hACE2 binding sites produces diverse, high-confidence sequences with strong in silico support for target binding. Finally, MIMIC uses experimental context as semantic conditioning to model assay-dependent RNA chemical probing, rather than treating context as a fixed output. Together, these results position MIMIC's aligned multimodal generative modeling as a strong foundation for unifying representation learning, conditional prediction, and constrained biomolecular design within a single model.

---


### 189. [Beyond the Attention Stability Boundary: Agentic Self-Synthesizing Reasoning Protocols](https://arxiv.org/abs/2604.24512)

**<font color=#1a73e8>作者：</font>** Dahlia Shehata, Ming Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents transition to autonomous digital coworkers, maintaining deterministic goal-directedness in non-linear multi-turn conversations emerged as an architectural bottleneck. We identify and formalize a systemic failure mode termed the Attention Latch in decoder-only autoregressive Transformers. This phenomenon, a behavioral manifestation of Information Over-squashing, occurs when the cumulative probabilistic weight of historical context overrides mid-task updates, causing agents to remain anchored to obsolete constraints despite explicit contradictory instructions. We propose Self-Synthesizing Reasoning Protocols (SSRP), a metacognitive framework that implements a discrete separation between high-level architectural planning (Architect) and turn-by-turn procedural execution (Executive). We evaluate SSRP across 9K trajectories using the MultiWOZ 2.2 dataset and the Aggregate Pivot Accuracy (APA), a novel metric we validate by mapping its scores to the U-shaped 'Lost in the Middle' curve. We present 3 experimental tiers: a shallow recency-based retrieval pilot, a high-entropy SOP, and a semantic hijacked 3-hop Multi-Fact Synthesis task. Our results empirically locate the Attention Stability Boundary, where stateless Vanilla ReAct baselines for GPT 5.4 collapse to 0.1% success while SSRP achieves a 715X Resilience Lift. We demonstrate statistically significant gains across Gemini 3.1 Pro, Claude Sonnet 4.6 and DeepSeek V3.2. Audits confirm SSRP necessity by proving attentional lapse via a recursive reflexion baseline (100% success); decoupling the latch from positional bias through equidistant stress testing (90% accuracy); and formalizing SSRP via the Information Bottleneck principle and granularity ablations. Procedural Integrity audit (98.8% adherence) reveals a Grounding Paradox where high-stability models fail by refusing to hallucinate under retrieval-reasoning contamination.

---


### 190. [SEARCH-R: Structured Entity-Aware Retrieval with Chain-of-Reasoning Navigator for Multi-hop Question Answering](https://arxiv.org/abs/2604.24515)

**<font color=#1a73e8>作者：</font>** Yuqing Fu, Yimin Deng, Wanyu Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-hop Question Answering (MHQA) aims to answer questions that require multi-step reasoning. It presents two key challenges: generating correct reasoning paths in response to the complex user queries, and accurately retrieving essential knowledge in the face of potential limitations in large language models (LLMs). Existing approaches primarily rely on prompt-based methods to generate reasoning paths, which are further combined with traditional sparse or dense retrieval to produce the final answer. However, the generation of reasoning paths commonly lacks effective control over the generative process, thus leading the reasoning astray. Meanwhile, the retrieval methods over-rely on knowledge matching or similarity scores rather than evaluating the practical utility of the information, resulting in retrieving homogeneous or non-useful information. Therefore, we propose a Structured Entity-Aware Retrieval with Chain-of-Reasoning Navigator framework named SEARCH-R. Specifically, SEARCH-R trains an end-to-end reasoning path navigator, which is able to provide a powerful sub-question decomposer by fine-tuning the Llama3.1-8B model. Moreover, a novel dependency tree-based retrieval is designed to evaluate the informational contribution of the document quantitatively. Extensive experiments on three challenging multi-hop datasets validate the effectiveness of the proposed framework. The code and dataset are available at: this https URL.

---


### 191. [Generating Place-Based Compromises Between Two Points of View](https://arxiv.org/abs/2604.24536)

**<font color=#1a73e8>作者：</font>** Sumanta Bhattacharyya, Francine Chen, Scott Carter 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) excel academically but struggle with social intelligence tasks, such as creating good compromises. In this paper, we present methods for generating empathically neutral compromises between two opposing viewpoints. We first compared four different prompt engineering methods using Claude 3 Opus and a dataset of 2,400 contrasting views on shared places. A subset of the gen erated compromises was evaluated for acceptability in a 50-participant study. We found that the best method for generating compromises between two views used external empathic similarity between a compromise and each viewpoint as iterative feedback, outperforming stan dard Chain of Thought (CoT) reasoning. The results indicate that the use of empathic neutrality improves the acceptability of compromises. The dataset of generated compromises was then used to train two smaller foundation models via margin-based alignment of human preferences, improving efficiency and removing the need for empathy estimation during inference.

---


### 192. [STELLAR-E: a Synthetic, Tailored, End-to-end LLM Application Rigorous Evaluator](https://arxiv.org/abs/2604.24544)

**<font color=#1a73e8>作者：</font>** Alessio Sordo, Lingxiao Du, Meeka-Hanna Lenisa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The increasing reliance on Large Language Models (LLMs) across diverse sectors highlights the need for robust domain-specific and language-specific evaluation datasets; however, the collection of such datasets is challenging due to privacy concerns, regulatory restrictions, and the time cost for manual creation. Existing automated benchmarking methods are often limited by relying on pre-existing data, poor scalability, single-domain focus, and lack of multilingual support. We present STELLAR-E - a fully automated system to generate high-quality synthetic datasets of custom size, using minimal human inputs without depending on existing datasets. The system is structured in two stages: (1) We modify the TGRT Self-Instruct framework to create a synthetic data engine that enables controllable, custom synthetic dataset generation, and (2) an evaluation pipeline incorporating statistical and LLM-based metrics to assess the applicability of the synthetic dataset for LLM-based application evaluations. The synthetic datasets reach an average difference of +5.7% in terms of LLM-as-a-judge scores against existing language-specific benchmarks, demonstrating comparable quality for comprehensive assessment of big and small LLMs. While real datasets remain slightly more challenging for LLMs especially for smaller models, this work establishes a scalable and domain-adaptable benchmarking framework that supports fair evaluation of LLM applications, offering a faster alternative to manual approaches and enabling high-efficiency automated quality assurance cycles.

---


### 193. [Towards Lawful Autonomous Driving: Deriving Scenario-Aware Driving Requirements from Traffic Laws and Regulations](https://arxiv.org/abs/2604.24562)

**<font color=#1a73e8>作者：</font>** Bowen Jian, Rongjie Yu, Hong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Driving in compliance with traffic laws and regulations is a basic requirement for human drivers, yet autonomous vehicles (AVs) can violate these requirements in diverse real-world scenarios. To encode law compliance into AV systems, conventional approaches use formal logic languages to explicitly specify behavioral constraints, but this process is labor-intensive, hard to scale, and costly to maintain. With recent advances in artificial intelligence, it is promising to leverage large language models (LLMs) to derive legal requirements from traffic laws and regulations. However, without explicitly grounding and reasoning in structured traffic scenarios, LLMs often retrieve irrelevant provisions or miss applicable ones, yielding imprecise requirements. To address this, we propose a novel pipeline that grounds LLM reasoning in a traffic scenario taxonomy through node-wise anchors that encode hierarchical semantics. On Chinese traffic laws and OnSite dataset (5,897 scenarios), our method improves law-scenario matching by 29.1\% and increases the accuracy of derived mandatory and prohibitive requirements by 36.9\% and 38.2\%, respectively. We further demonstrate real-world applicability by constructing a law-compliance layer for AV navigation and developing an onboard, real-time compliance monitor for in-field testing, providing a solid foundation for future AV development, deployment, and regulatory oversight.

---


### 194. [MEG-RAG: Quantifying Multi-modal Evidence Grounding for Evidence Selection in RAG](https://arxiv.org/abs/2604.24564)

**<font color=#1a73e8>作者：</font>** Xihang Wang, Zihan Wang, Chengkai Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Retrieval-Augmented Generation (MRAG) addresses key limitations of Multimodal Large Language Models (MLLMs), such as hallucination and outdated knowledge. However, current MRAG systems struggle to distinguish whether retrieved multimodal data truly supports the semantic core of an answer or merely provides superficial relevance. Existing metrics often rely on heuristic position-based confidence, which fails to capture the informational density of multimodal entities. To address this, we propose Multi-modal Evidence Grounding (MEG), a semantic-aware metric that quantifies the contribution of retrieved evidence. Unlike standard confidence measures, MEG utilizes Semantic Certainty Anchoring, focusing on high-IDF information-bearing tokens that better capture the semantic core of the answer. Building on MEG, we introduce MEG-RAG, a framework that trains a multimodal reranker to align retrieved evidence with the semantic anchors of the ground truth. By prioritizing high-value content based on semantic grounding rather than token probability distributions, MEG-RAG improves the accuracy and multimodal consistency of generated outputs. Extensive experiments on the M$^2$RAG benchmark show that MEG-RAG consistently outperforms strong baselines and demonstrates robust generalization across different teacher models.

---


### 195. [FastOMOP: A Foundational Architecture for Reliable Agentic Real-World Evidence Generation on OMOP CDM data](https://arxiv.org/abs/2604.24572)

**<font color=#1a73e8>作者：</font>** Niko Moeller-Grell, Shihao Shenzhang, Zhangshu Joshua Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Observational Medical Outcomes Partnership Common Data Model (OMOP CDM), maintained by the Observational Health Data Sciences and Informatics (OHDSI) collaboration, enabled the harmonisation of electronic health records data of nearly one billion patients in 83 countries. Yet generating real-world evidence (RWE) from these repositories remains a manual process requiring clinical, epidemiological and technical expertise. LLMs and multi-agent systems have shown promise for clinical tasks, but RWE automation exposes a fundamental challenge: agentic systems introduce emergent behaviours, coordination failures and safety risks that existing approaches fail to govern. No infrastructure exists to ensure agentic RWE generation is flexible, safe and auditable across the lifecycle. We introduce FastOMOP, an open-source multi-agent architecture that addresses this gap by separating three infrastructure layers, governance, observability and orchestration, from pluggable agent-teams. Governance is enforced at the process boundary through deterministic validation independent of agent reasoning, ensuring no compromised or hallucinating agent can bypass safety controls. Agent teams for phenotyping, study design and statistical analysis inherit these guarantees through controlled tool exposure. We validated FastOMOP using a natural-language-to-SQL agent team across three OMOP CDM datasets: synthetic data from Synthea, MIMIC-IV and a real-world NHS dataset from Lancashire Teaching Hospitals (IDRIL). FastOMOP achieved reliability scores of 0.84-0.94 with perfect adversarial and out-of-scope block rates, demonstrating process-boundary governance delivers safety guarantees independent of model choice. These results indicate that the reliability gap in RWE deployment is architectural rather than model capability, and establish FastOMOP as a governed architecture for progressive RWE automation.

---


### 196. [Improving Vision-language Models with Perception-centric Process Reward Models](https://arxiv.org/abs/2604.24583)

**<font color=#1a73e8>作者：</font>** Yingqian Min, Kun Zhou, Yifan Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in reinforcement learning with verifiable rewards (RLVR) have significantly improved the complex reasoning ability of vision-language models (VLMs). However, its outcome-level supervision is too coarse to diagnose and correct errors within the reasoning chain. To this end, we propose Perceval, a process reward model (PRM) that enables token-level error grounding, which can extract image-related claims from the response and compare them one by one with the visual evidence in the image, ultimately returning claims that contain perceptual errors. Perceval is trained with perception-intensive supervised training data. We then integrate Perceval into the RL training process to train the policy models. Specifically, compared to traditional GRPO, which applies sequence-level advantages, we apply token-level advantages by targeting penalties on hallucinated spans identified by Perceval, thus enabling fine-grained supervision signals. In addition to augmenting the training process, Perceval can also assist VLMs during the inference stage. Using Perceval, we can truncate the erroneous portions of the model's response, and then either have the model regenerate the response directly or induce the model to reflect on its previous output. This process can be repeated multiple times to achieve test-time scaling. Experiments show significant improvements on benchmarks from various domains across multiple reasoning VLMs trained with RL, highlighting the promise of perception-centric supervision as a general-purpose strategy. For test-time scaling, it also demonstrates consistent performance gains over other strategies, such as major voting. Our code and data will be publicly released at this https URL.

---


### 197. [A systematic evaluation of vision-language models for observational astronomical reasoning tasks](https://arxiv.org/abs/2604.24589)

**<font color=#1a73e8>作者：</font>** Wenke Ren, Hengxiao Guo, Wenwen Zuo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly proposed as general-purpose tools for scientific data interpretation, yet their reliability on real astronomical observations across diverse modalities remains untested. We present AstroVLBench, a comprehensive benchmark comprising over 4,100 expert-verified instances across five tasks spanning optical imaging, radio interferometry, multi-wavelength photometry, time-domain light curves, and optical spectroscopy. Evaluating six frontier models, we find that performance is strongly modality-dependent: while one model (Gemini 3 Pro) emerges as the most consistently capable across tasks, task-specific strengths vary, and all models substantially underperform domain-specialized methods. Mechanistic ablations reveal that performance depends not only on directing attention to salient visual features but also on grounding those features in physical knowledge. Phenomenological prompts describing what to look for improve accuracy by sharpening model focus, but physical prompts explaining why those features matter perform better overall and yield more balanced classifications with reduced class-specific bias. Consistent with this picture, presenting the underlying one-dimensional measurements directly as numerical tables instead of rendered plots yields up to 13 percentage points improvement. Reasoning quality analysis further demonstrates that, without explicit physical grounding, models may reach correct predictions from phenomenologically plausible cues while providing physically imprecise justifications, establishing that accuracy alone is insufficient for trustworthy scientific deployment. These findings provide the first systematic, multi-modal baselines for VLMs in observational astronomy and identify the specific representation, grounding, and reasoning bottlenecks where current models fail.

---


### 198. [Skill Retrieval Augmentation for Agentic AI](https://arxiv.org/abs/2604.24594)

**<font color=#1a73e8>作者：</font>** Weihang Su, Jianming Long, Qingyao Ai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) evolve into agentic problem solvers, they increasingly rely on external, reusable skills to handle tasks beyond their native parametric capabilities. In existing agent systems, the dominant strategy for incorporating skills is to explicitly enumerate available skills within the context window. However, this strategy fails to scale: as skill corpora expand, context budgets are consumed rapidly, and the agent becomes markedly less accurate in identifying the right skill. To this end, this paper formulates Skill Retrieval Augmentation (SRA), a new paradigm in which agents dynamically retrieve, incorporate, and apply relevant skills from large external skill corpora on demand. To make this problem measurable, we construct a large-scale skill corpus and introduce SRA-Bench, the first benchmark for decomposed evaluation of the full SRA pipeline, covering skill retrieval, skill incorporation, and end-task execution. SRA-Bench contains 5,400 capability-intensive test instances and 636 manually constructed gold skills, which are mixed with web-collected distractor skills to form a large-scale corpus of 26,262 skills. Extensive experiments show that retrieval-based skill augmentation can substantially improve agent performance, validating the promise of the paradigm. At the same time, we uncover a fundamental gap in skill incorporation: current LLM agents tend to load skills at similar rates, regardless of whether a gold skill is retrieved or whether the task actually requires external capabilities. This shows that the bottleneck in skill augmentation lies not only in retrieval but also in the base model's ability to determine which skill to load and when external loading is actually needed. These findings position SRA as a distinct research problem and establish a foundation for the scalable augmentation of capabilities in future agent systems.

---


### 199. [Majorization-Guided Test-Time Adaptation for Vision-Language Models under Modality-Specific Shift](https://arxiv.org/abs/2604.24602)

**<font color=#1a73e8>作者：</font>** Lixian Chen, Mingxuan Huang, Yanhui Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models transfer well in zero-shot settings, but at deployment the visual and textual branches often shift asymmetrically. Under this condition, entropy-based test-time adaptation can sharpen the fused posterior while increasing error, because an unreliable modality may still dominate fusion. We study this failure mode through a majorization view of multimodal posteriors and cast adaptation as a constrained de-mixing problem on the fused prediction. Based on this view, we propose MG-MTTA, which keeps the backbone frozen and updates only a lightweight gate or adapter. The objective combines fused-posterior entropy minimization with a reliability-aware gate prior built from anchor-based modality consistency and cross-modal conflict. Our analysis gives conditions under which entropy reduction preserves the correct ranking and a threshold that characterizes modality-dominance failure. On the ImageNet-based benchmark, MG-MTTA improves top-1 accuracy from 57.97 to 66.51 under semantics-preserving textual shift and from 21.68 to 26.27 under joint visual-textual shift, while remaining competitive in the visual-only benchmark. These results show that multimodal test-time adaptation should control modality reliability, not just prediction entropy.

---


### 200. [XGRAG: A Graph-Native Framework for Explaining KG-based Retrieval-Augmented Generation](https://arxiv.org/abs/2604.24623)

**<font color=#1a73e8>作者：</font>** Zhuoling Li, Ha Linh Hong Tran Nguyen, Valeria Bladinieres 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph-based Retrieval-Augmented Generation (GraphRAG) extends traditional RAG by using knowledge graphs (KGs) to give large language models (LLMs) a structured, semantically coherent context, yielding more grounded answers. However, GraphRAG reasoning process remains a black-box, limiting our ability to understand how specific pieces of structured knowledge influence the final output. Existing explainability (XAI) methods for RAG systems, designed for text-based retrieval, are limited to interpreting an LLM response through the relational structures among knowledge components, creating a critical gap in transparency and trustworthiness. To address this, we introduce XGRAG, a novel framework that generates causally grounded explanations for GraphRAG systems by employing graph-based perturbation strategies, to quantify the contribution of individual graph components on the model answer. We conduct extensive experiments comparing XGRAG against RAG-Ex, an XAI baseline for standard RAG, and evaluate its robustness across various question types, narrative structures and LLMs. Our results demonstrate a 14.81% improvement in explanation quality over the baseline RAG-Ex across NarrativeQA, FairyTaleQA, and TriviaQA, evaluated by F1-score measuring alignment between generated explanations and original answers. Furthermore, XGRAG explanations exhibit a strong correlation with graph centrality measures, validating its ability to capture graph structure. XGRAG provides a scalable and generalizable approach towards trustworthy AI through transparent, graph-based explanations that enhance the interpretability of RAG systems.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-215](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
