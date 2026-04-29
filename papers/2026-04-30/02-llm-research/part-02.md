# 🧠 大模型相关研究 | 2026年04月30日

> 本类共 **92** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-92**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-92**

---

### 51. [Combating Visual Neglect and Semantic Drift in Large Multimodal Models for Enhanced Cross-Modal Retrieval](https://arxiv.org/abs/2604.25273)

**<font color=#1a73e8>作者：</font>** Guosheng Zhang, Linkai Liu, Keyao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite significant progress in Unified Multimodal Retrieval (UMR) powered by Large Multimodal Models (LMMs), existing embedding methods primarily focus on sample-level objectives via contrastive learning while overlooking the crucial subject-level semantics. This limitation hinders the model's ability to group semantically coherent subjects in complex multimodal queries, manifesting as semantic alignment deviation--where models fail to accurately localize salient text-referred regions in visual content. Moreover, without explicit guidance to model salient visual subjects, LMMs tend to over-rely on textual cues, resulting in visual modality neglect and suboptimal utilization of visual knowledge. To this end, we propose Salient Subject-Aware Multimodal Embedding (SSA-ME), a novel framework designed to enhance fine-grained representation learning through saliency-aware modeling. SSA-ME leverages LMMs and visual experts to identify and emphasize salient visual concepts in image-text pairs, and introduces a saliency-guided objective to better align cross-modal attention with semantically meaningful regions. Additionally, a feature regeneration module recalibrates visual features based on the derived saliency maps, ensuring a balanced and semantically coherent integration across modalities. Extensive experiments show that our method achieves state-of-the-art performance on the MMEB benchmark, demonstrating that incorporating subject-level modeling substantially improves multimodal retrieval. Comprehensive qualitative analyses further illustrate the interpretability and effectiveness of our approach.

---


### 52. [OmniVTG: A Large-Scale Dataset and Training Paradigm for Open-World Video Temporal Grounding](https://arxiv.org/abs/2604.25276)

**<font color=#1a73e8>作者：</font>** Minghang Zheng, Zihao Yin, Yi Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Temporal Grounding (VTG), the task of localizing video segments from text queries, struggles in open-world settings due to limited dataset scale and semantic diversity, causing performance gaps between common and rare concepts. To overcome these limitations, we introduce OmniVTG, a new large-scale dataset for open-world VTG, coupled with a Self-Correction Chain-of-Thought (CoT) training paradigm designed to enhance the grounding capabilities of Multimodal Large Language Models (MLLMs). Our OmniVTG is constructed via a novel Semantic Coverage Iterative Expansion pipeline, which first identifies gaps in the vocabulary of existing datasets and collects videos that are highly likely to contain these target concepts. For high-quality annotation, we leverage the insight that modern MLLMs excel at dense captioning more than direct grounding and design a caption-centric data engine to prompt MLLMs to generate dense, timestamped descriptions. Beyond the dataset, we observe that simple supervised finetuning (SFT) is insufficient, as a performance gap between rare and common concepts still persists. We find that MLLMs' video understanding ability significantly surpasses their direct grounding ability. Based on this, we propose a Self-Correction Chain-of-Thought (CoT) training paradigm. We train the MLLM to first predict, then use its understanding capabilities to reflect on and refine its own predictions. This capability is instilled via a three-stage pipeline of SFT, CoT finetuning, and reinforcement learning. Extensive experiments show our approach not only excels at open-world grounding in our OmniVTG dataset but also achieves state-of-the-art zero-shot performance on four existing VTG benchmarks. Code is available at this https URL.

---


### 53. [Learning from Medical Entity Trees: An Entity-Centric Medical Data Engineering Framework for MLLMs](https://arxiv.org/abs/2604.25296)

**<font color=#1a73e8>作者：</font>** Jianghang Lin, Haihua Yang, Deli Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have shown transformative potential in medical applications, yet their performance is hindered by conventional data curation strategies that rely on coarse-grained partitioning by modality or department. Such fragmented approaches fail to capture the hierarchical and interconnected nature of clinical medical knowledge, limiting the models' ability to perform fine-grained recognition and complex reasoning. In this paper, we propose a novel Entity-Centric Medical Data Engineering framework. We automatically extract entities from authoritative medical literature to construct a Medical Entity Tree (MET), a hierarchical structure that systematically encodes diseases, anatomical structures, modalities, and symptoms into a unified knowledge repository. Building upon the MET, we propose an advanced data engine that includes: (1) node-guided retrieval to anchor raw data to specific medical concepts, (2) a two-stage hybrid filtering and alignment pipeline to ensure precise visual-semantic correspondence, and (3) knowledge-aware data synthesis to generate enriched captions and targeted reasoning VQA pairs, leveraging structural constraints. Extensive evaluations across six medical benchmarks demonstrate that our approach significantly enhances the medical capabilities of general-purpose MLLMs, improving their ability to handle complex clinical queries and achieve state-of-the-art performance in diverse medical contexts.

---


### 54. [LegalMidm: Use-Case-Driven Legal Domain Specialization for Korean Large Language Model](https://arxiv.org/abs/2604.25297)

**<font color=#1a73e8>作者：</font>** Youngjoon Jang, Chanhee Park, Hyeonseok Moon 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, the rapid proliferation of open-source large language models (LLMs) has spurred efforts to turn general-purpose models into domain specialists. However, many domain-specialized LLMs are developed using datasets and training protocols that are not aligned with the nuanced requirements of real-world applications. In the legal domain, where precision and reliability are essential, this lack of consideration limits practical utility. In this study, we propose a systematic training framework grounded in the practical needs of the legal domain, with a focus on Korean law. We introduce LegalMidm, a Korean legal-domain LLM, and present a methodology for constructing high-quality, use-case-driven legal datasets and optimized training pipelines. Our approach emphasizes collaboration with legal professionals and rigorous data curation to ensure relevance and factual accuracy, and demonstrates effectiveness in key legal tasks.

---


### 55. [The Thinking Pixel: Recursive Sparse Reasoning in Multimodal Diffusion Latents](https://arxiv.org/abs/2604.25299)

**<font color=#1a73e8>作者：</font>** Yuwei Sun, Yuxuan Yao, Hui Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved success in high-fidelity data synthesis, yet their capacity for more complex, structured reasoning like text following tasks remains constrained. While advances in language models have leveraged strategies such as latent reasoning and recursion to enhance text understanding capabilities, extending these to multimodal text-to-image generation tasks is challenging due to the continuous and non-discrete nature of visual tokens. To tackle this problem, we draw inspiration from modular human cognition and propose a recursive, sparse mixture-of-experts framework integrated into conventional diffusion models. Our approach introduces a recursive component within joint attention layers that iteratively refines visual tokens over multiple latent steps while efficiently sharing parameters via sparse selection of neural modules. At each step, a gating network is devised to dynamically select specialized neural modules, conditioned on the current visual tokens, the diffusion timestep, and the conditioning information. Comprehensive evaluation on class-conditioned ImageNet image generation tasks and additional studies on the GenEval and DPG benchmark demonstrate the superiority of the proposed method in enhancing model image generation performance.

---


### 56. [Faithfulness-QA: A Counterfactual Entity Substitution Dataset for Training Context-Faithful RAG Models](https://arxiv.org/abs/2604.25313)

**<font color=#1a73e8>作者：</font>** Li Ju, Junzhe Wang, Qi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) models frequently produce answers grounded in parametric memory rather than the retrieved context, undermining the core promise of retrieval augmentation. A fundamental obstacle to fixing this unfaithfulness is the lack of training data that explicitly requires models to prefer context over internal knowledge. We introduce Faithfulness-QA, a large-scale dataset of 99,094 samples constructed through counterfactual entity substitution. Starting from two established extractive QA benchmarks--SQuAD and TriviaQA--we automatically identify answer-bearing named entities in each context, replace them with type-consistent alternatives drawn from a curated bank of 76,953 entities, and thereby manufacture controlled knowledge conflicts between context and parametric memory. Rigorous quality filtering ensures 100% pass rates across four automated checks on random 200-sample audits. We release the full dataset, the construction pipeline, and a typed entity bank covering eight named entity categories. Faithfulness-QA is designed as a training resource for attention-based faithfulness objectives and as an evaluation benchmark for measuring context-grounding behavior in RAG systems. Data and code are available at this https URL.

---


### 57. [Plausible but Wrong: A case study on Agentic Failures in Astrophysical Workflows](https://arxiv.org/abs/2604.25345)

**<font color=#1a73e8>作者：</font>** Shivam Rawat, Lucie Flek  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems are increasingly being integrated into scientific workflows, yet their behavior under realistic conditions remains insufficiently understood. We evaluate CMBAgent across two workflow paradigms and eighteen astrophysical tasks. In the One-Shot setting, access to domain-specific context yields an approximately ~6x performance improvement (0.85 vs. ~0 without context), with the primary failure mode being silent incorrect computation - syntactically valid code that produces plausible but inaccurate results. In the Deep Research setting, the system frequently exhibits silent failures across stress tests, producing physically inconsistent posteriors without self-diagnosis. Overall, performance is strong on well-specified tasks but degrades on problems designed to probe reasoning limits, often without visible error signals. These findings highlight that the most concerning failure mode in agentic scientific workflows is not overt failure, but confident generation of incorrect results. We release our evaluation framework to facilitate systematic reliability analysis of scientific AI agents.

---


### 58. [GraphPL: Leveraging GNN for Efficient and Robust Modalities Imputation in Patchwork Learning](https://arxiv.org/abs/2604.25352)

**<font color=#1a73e8>作者：</font>** Xingjian Hu, Zuoyu Yan, Jianhua Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current research on distributed multi-modal learning typically assumes that clients can access complete information across all modalities, which may not hold in practice. In this paper, we explore patchwork learning, in which the modalities available to different clients vary, and the objective is to impute the missing modalities for each client in an unsupervised manner. Existing methods are shown not to fully utilize the modality information as they tend to rely on only a subset of the observed modalities. To address this issue, we propose GraphPL, which combines graph neural networks with patchwork learning to flexibly integrate all observed modalities and remains robust with noisy inputs. Experimental results show that GraphPL achieves SOTA performance on benchmark datasets. Our results on real-world distributed electronic health record dataset show GraphPL learns strong downstream features and enables tasks like disease prediction via superior modality imputation.

---


### 59. [The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models](https://arxiv.org/abs/2604.25359)

**<font color=#1a73e8>作者：</font>** Abhinav Kumar Singh, Harsha Vardhan Khurdula, Yoeven D Khemlani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models are increasingly being deployed to extract structured data from unstructured and semi-structured sources: parsing invoices, medical records, and converting PDF documents to database entries. Yet existing benchmarks for structured output generation either focus on schema compliance alone, or evaluate value correctness within a single source domain. We introduce SOB (The Structured Output Benchmark), a multi-source benchmark spanning three source modalities: native text, images, and audio conversations. All models receive a text-normalized representation of their context regardless of source modality; this deliberate design isolates structured-output capability from raw vision or speech-processing quality, ensuring a fair, source-agnostic comparison. Our benchmark comprises 5,000 text evaluation records derived from multi-hop QA drawn from a 25,091-record full corpus, 209 image records from OCR-processed PDFs across seven document types including multi-column layouts, dense tables, scanned historical documents, small-print text, and mathematical typesetting, and 115 audio records from the AMI corpus. Each record pairs a natural-language question with a JSON schema that the model must follow and a ground-truth answer verified against the source context. We evaluate 21 frontier and open-weight models across three source domains and seven metrics. Our results reveal a consistent pattern: models achieve near-perfect schema compliance, yet the best Value Accuracy, measured by exact leaf-value match, reaches only 83.0% on text, 67.2% on images, and 23.7% on audio, where longer context makes extraction substantially harder. We release the dataset, evaluation pipeline, and all related code.

---


### 60. [GPT-Image-2 in the Wild: A Twitter Dataset of Self-Reported AI-Generated Images from the First Week of Deployment](https://arxiv.org/abs/2604.25370)

**<font color=#1a73e8>作者：</font>** Kidus Zewde, Simiao Ren, Xingyu Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The release of GPT-image-2 by OpenAI marks a watershed moment in AI-generated imagery: the boundary between photographic reality and synthetic content has never been more difficult to discern. We introduce the GPT-Image-2 Twitter Dataset, the first published dataset of GPT-image-2 generated images, sourced from publicly available Twitter/X posts in the immediate aftermath of the model's April 21, 2026 release. Leveraging the Twitter API v2 and a multi-stage curation pipeline spanning multilingual text heuristics (English, Japanese, and Chinese), browser-automated Twitter "Made with AI" badge verification, and model name variant matching, we curate 10,217 confirmed GPT-image-2 images from 27,662 collected records over a six-day window.
We characterize the dataset across four analyses: CLIP-based zero-shot subject taxonomy, OCR text legibility (82.0% of images contain detectable text), face detection (59.2% of images, 22,583 total faces), and semantic clustering (137 CLIP ViT-L/14 clusters).
A key negative result is that C2PA content credentials are systematically stripped by Twitter's CDN on upload, rendering cryptographic provenance verification infeasible for social-media-sourced AI images. The dataset and all curation code are released publicly.

---


### 61. [Benchmarking PyCaret AutoML Against IndoBERT Fine-Tuning for Sentiment Analysis on Indonesian IKN Twitter Data](https://arxiv.org/abs/2604.25392)

**<font color=#1a73e8>作者：</font>** Mutia Alfi Mayzaroh, Dwi Fitria Ningsih, Nindi Destriani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper benchmarks a classical machine learning approach based on PyCaret AutoML against a deep learning approach based on IndoBERT fine-tuning for binary sentiment analysis of Indonesian-language Twitter comments related to Ibu Kota Nusantara (IKN). The dataset contains 1,472 manually labeled samples, consisting of 780 negative and 692 positive comments. In the machine learning setting, Logistic Regression, Naive Bayes, and Support Vector Machine were evaluated using 10-fold cross-validation, with Logistic Regression achieving the best performance among the classical models at 77.57% accuracy and 77.17% F1-score. In the deep learning setting, the indobenchmark/indobert-base-p1 model was fine-tuned for five epochs and achieved 89.59% test accuracy and 89.37% F1-score. The results show that IndoBERT substantially outperforms the machine learning baselines, highlighting the effectiveness of Transformer-based contextual representations for informal Indonesian social media text.

---


### 62. [Leveraging Previous-Traversal Point Cloud Map Priors for Camera-Based 3D Object Detection and Tracking](https://arxiv.org/abs/2604.25405)

**<font color=#1a73e8>作者：</font>** Markus Käppeler, Özgün Çiçek, Yakov Miron 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-based 3D object detection and tracking are central to autonomous driving, yet precise 3D object localization remains fundamentally constrained by depth ambiguity when no expensive, depth-rich online LiDAR is available at inference. In many deployments, however, vehicles repeatedly traverse the same environments, making static point cloud maps from prior traversals a practical source of geometric priors. We propose DualViewMapDet, a camera-only inference framework that retrieves such map priors online and leverages them to mitigate the absence of a LiDAR sensor during deployment. The key idea is a dual-space camera-map fusion strategy that avoids one-sided view conversion. Specifically, we (i) project the map into perspective view (PV) and encode multi-channel geometric cues to enrich image features and support BEV lifting, and (ii) encode the map directly in bird's-eye view (BEV) with a sparse voxel backbone and fuse it with lifted camera features in a shared metric space. Extensive evaluations on nuScenes and Argoverse 2 demonstrate consistent improvements over strong camera-only baselines, with particularly strong gains in object localization. Ablations further validate the contributions of PV/BEV fusion and prior-map coverage. We make the code and pre-trained models available at this https URL .

---


### 63. [FED-FSTQ: Fisher-Guided Token Quantization for Communication-Efficient Federated Fine-Tuning of LLMs on Edge Devices](https://arxiv.org/abs/2604.25421)

**<font color=#1a73e8>作者：</font>** Changyu Li, Shuanghong Huang, Jiashen Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning provides a practical route to adapt large language models (LLMs) on edge devices without centralizing private data, yet in mobile deployments the training wall-clock is often bottlenecked by straggler-limited uplink communication under heterogeneous bandwidth and intermittent participation. Although parameter-efficient fine-tuning (PEFT) reduces trainable parameters, per-round payloads remain prohibitive in non-IID regimes, where uniform compression can discard rare but task-critical signals. We propose Fed-FSTQ, a Fisher-guided token quantization system primitive for communication-efficient federated LLM fine-tuning. Fed-FSTQ employs a lightweight Fisher proxy to estimate token sensitivity, coupling importance-aware token selection with non-uniform mixed-precision quantization to allocate higher fidelity to informative evidence while suppressing redundant transmission. The method is model-agnostic, serves as a drop-in module for standard federated PEFT pipelines, e.g., LoRA, without modifying the server aggregation rule, and supports bandwidth-heterogeneous clients via compact sparse message packing. Experiments on multilingual QA and medical QA under non-IID partitions show that Fed-FSTQ reduces cumulative uplink traffic required to reach a fixed quality threshold by 46x relative to a standard LoRA baseline, and improves end-to-end wall-clock time-to-accuracy by 52%. Furthermore, enabling Fisher-guided token reduction at inference yields up to a 1.55x end-to-end speedup on NVIDIA Jetson-class edge devices, demonstrating deployability under tight resource constraints.

---


### 64. [Do LLMs Capture Embodied Cognition and Cultural Variation? Cross-Linguistic Evidence from Demonstratives](https://arxiv.org/abs/2604.25423)

**<font color=#1a73e8>作者：</font>** Yu Wang, Emmanuele Chersoni, Chu-Ren Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Do large language models (LLMs) truly acquire embodied cognition and cultural conventions from text? We introduce demonstratives, fundamental spatial expressions like "this/that" in English and "zhè/nà" in Chinese, as a novel probe for grounded knowledge. Using 6,400 responses from 320 native speakers, we establish a human baseline: English speakers reliably distinguish proximal-distal referents but struggle with perspective-taking, while Chinese speakers switch perspectives fluently but tolerate distal ambiguity. In contrast, five state-of-the-art LLMs fail to inherently understand the proximal-distal contrast and show no cultural differences, defaulting to English-centric reasoning. Our study contributes (i) a new task, based on demonstratives, as a new lens for evaluating embodied cognition and cultural conventions; (ii) empirical evidence of cross-cultural asymmetries in human interpretation; (iii) a new perspective on the egocentric-sociocentric debate, showing both orientations coexist but vary across languages; and (iv) a call to address individual variation in future model design.

---


### 65. [A Systematic Post-Train Framework for Video Generation](https://arxiv.org/abs/2604.25427)

**<font color=#1a73e8>作者：</font>** Zeyue Xue, Siming Fu, Jie Huang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While large-scale video diffusion models have demonstrated impressive capabilities in generating high-resolution and semantically rich content, a significant gap remains between their pretraining performance and real-world deployment requirements due to critical issues such as prompt sensitivity, temporal inconsistency, and prohibitive inference costs. To bridge this gap, we propose a comprehensive post-training framework that systematically aligns pretrained models with user intentions through four synergistic stages: we first employ Supervised Fine-Tuning (SFT) to transform the base model into a stable instruction-following policy, followed by a Reinforcement Learning from Human Feedback (RLHF) stage that utilizes a novel Group Relative Policy Optimization (GRPO) method tailored for video diffusion to enhance perceptual quality and temporal coherence; subsequently, we integrate Prompt Enhancement via a specialized language model to refine user inputs, and finally address system efficiency through Inference Optimization. Together, these components provide a systematic approach to improving visual quality, temporal coherence, and instruction following, while preserving the controllability learned during pretraining. The result is a practical blueprint for building scalable post-training pipelines that are stable, adaptable, and effective in real-world deployment. Extensive experiments demonstrate that this unified pipeline effectively mitigates common artifacts and significantly improves controllability and visual aesthetics while adhering to strict sampling cost constraints.

---


### 66. [One Refiner to Unlock Them All: Inference-Time Reasoning Elicitation via Reinforcement Query Refinement](https://arxiv.org/abs/2604.25444)

**<font color=#1a73e8>作者：</font>** Yixiao Zhou, Dongzhou Cheng, zhiliang wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often fail to utilize their latent reasoning capabilities due to a distributional mismatch between ambiguous human inquiries and the structured logic required for machine activation. Existing alignment methods either incur prohibitive $O(N)$ costs by fine-tuning each model individually or rely on static prompts that fail to resolve query-level structural complexity. In this paper, we propose ReQueR (\textbf{Re}inforcement \textbf{Que}ry \textbf{R}efinement), a modular framework that treats reasoning elicitation as an inference-time alignment task. We train a specialized Refiner policy via Reinforcement Learning to rewrite raw queries into explicit logical decompositions, treating frozen LLMs as the environment. Rooted in the classical Zone of Proximal Development from educational psychology, we introduce the Adaptive Solver Hierarchy, a curriculum mechanism that stabilizes training by dynamically aligning environmental difficulty with the Refiner's evolving competence. ReQueR yields consistent absolute gains of 1.7\%--7.2\% across diverse architectures and benchmarks, outperforming strong baselines by 2.1\% on average. Crucially, it provides a promising paradigm for one-to-many inference-time reasoning elicitation, enabling a single Refiner trained on a small set of models to effectively unlock reasoning in diverse unseen models. Code is available at this https URL.

---


### 67. [An Investigation of Linguistic Biases in LLM-Based Recommendations](https://arxiv.org/abs/2604.25456)

**<font color=#1a73e8>作者：</font>** Nitin Venkateswaran, Jason Ang, Deep Adhikari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate linguistic biases in LLM-based restaurant and product recommendations given prompts varying across Southern American English (AE), Indian English (IE), and Code-Switched Hindi-English dialects, using the Yelp Open dataset (Yelp Inc., 2023) and Walmart product reviews dataset (PromptCloud,2020). We add lists of restaurant and product names balanced by cuisine type and product category to the prompts given to the LLM, and we zero-shot prompt the LLMs in a cold-start setting to select the top-20 restaurant and product recommendations from these lists for each of the dialect-varied prompts. We prompt LLMs using different list samples across 20 seeds for better generalization, and aggregate per cuisine-type and per category response counts for each seed, question/prompt, and LLM model. We run mixed-effects regression models for each model family and topic (restaurant/product) with the aggregate response counts as the dependent, and conduct likelihood ratio tests for the fixed effects with post-hoc pairwise testing of estimated marginal means differences, to investigate group-level differences in recommendation counts by model size and dialect type. Results show that dialect plays a role in the type of restaurant selected across the models tested with the mistral-small-3.1 model and both the llama-3.1 family models tested showing more sensitivity to Indian English and Code-Switched prompts. In terms of product recommendations, the llama-3.1-70B-model is particularly sensitive to Code-Switched prompts in four out of seven categories, and more beauty and home category recommendations are seen when using the Indian English and Code-Switched prompts for larger and smaller models, respectively. No broad trends are seen in the model-size based differences, with differing recommendations based on model sizes conditioned by the type of dialect.

---


### 68. [SciEval: A Benchmark for Automatic Evaluation of K-12 Science Instructional Materials](https://arxiv.org/abs/2604.25472)

**<font color=#1a73e8>作者：</font>** Zhaohui Li, Peng He, Zhiyuan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The need to evaluate instructional materials for K-12 science education has become increasingly important, as more educators use generative AI to create instructional materials. However, the review of instructional materials is time-consuming, expertise-intensive, and difficult to scale, motivating interest in automated evaluation approaches. While large language models (LLMs) have shown strong performance on general evaluation tasks, their performance and reliability on instructional materials remain unclear. To address this gap, we formulate Automatic Instructional Materials Evaluation (AIME) as a generative AI task that predicts scores and evidence using the rubric designed by the educator. We create a benchmark dataset and develop baseline models for AIME. First, we curate the first AIME dataset, SciEval, consisting of instructional materials annotated with pedagogy-aligned evaluation scores and evidence-based rationales. Expert annotations achieve high inter-rater reliability, resulting in a dataset of 273 lesson-level instructional materials evaluated across 13 criteria (N=3549) using the EQuIP rubric. Second, we test mainstream LLMs (GPT, Gemini, Llama, and Qwen) on SciEval and find that none achieve strong performance. Then we fine-tune Qwen3 on SciEval. Results on a held-out test set show that domain-aligned fine-tuning can achieve up to 11 percent performance gains, highlighting the importance of domain-specific fine-tuning for AIME and facilitating the use of LLMs in other educational tasks.

---


### 69. [From Chatbots to Confidants: A Cross-Cultural Study of LLM Adoption for Emotional Support](https://arxiv.org/abs/2604.25525)

**<font color=#1a73e8>作者：</font>** Natalia Amat-Lefort, Mert Yazan, Amanda Cercas Curry 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used not only for instrumental tasks, but as always-available and non-judgmental confidants for emotional support. Yet what drives adoption and how users perceive emotional support interactions across countries remains unknown. To address this gap, we present the first large-scale cross-cultural study of LLM use for emotional support, surveying 4,641 participants across seven countries (USA, UK, Germany, France, Spain, Italy, and The Netherlands). Our results show that adoption rates vary dramatically across countries (from 20% to 59%). Using mixed models that separate cultural effects from demographic composition, we find that: Being aged 25-44, religious, married, and of higher socioeconomic status are predictors of positive perceptions (trust, usage, perceived benefits), with socioeconomic status being the strongest. English-speaking countries consistently show more positive perceptions than Continental European countries. We further collect a corpus of 731 real multilingual prompts from user interactions, showing that users mainly seek help for loneliness, stress, relationship conflicts, and mental health struggles. Our findings reveal that LLM emotional support use is shaped by a complex sociotechnical landscape and call for a broader research agenda examining how these systems can be developed, deployed, and governed to ensure safe and informed access.

---


### 70. [Marco-MoE: Open Multilingual Mixture-of-Expert Language Models with Efficient Upcycling](https://arxiv.org/abs/2604.25578)

**<font color=#1a73e8>作者：</font>** Fan Jiang, Yu Zhao, Chenyang Lyu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Marco-MoE, a suite of fully open multilingual sparse Mixture-of-Experts (MoE) models. Marco-MoE features a highly sparse design in which only around 5\% of the total parameters are activated per input token. This extreme sparsity, combined with upcycling from dense models, enables efficient pre-training on 5T tokens. Our models surpass similarly-sized competitors on English and multilingual benchmarks, achieving a best-in-class performance-to-compute ratio. We further post-train these models to create Marco-MoE-\textsc{Instruct} variants, which surpass the performance of competing models possessing $3$--$14\times$ more activated parameters. Our analysis reveals that Marco-MoE learns structured expert activation patterns shared across related languages, while maintaining highly specialized utilization for linguistically isolated ones. We further show that Marco-MoE allows for scalable language expansion without the interference typical of dense models. To support the community, we disclose our full training datasets, recipes, and model weights.

---


### 71. [Bye Bye Perspective API: Lessons for Measurement Infrastructure in NLP, CSS and LLM Evaluation](https://arxiv.org/abs/2604.25580)

**<font color=#1a73e8>作者：</font>** David Hartmann, Manuel Tonneau, Angelie Kraft 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The closure of Perspective API at the end of 2026 discards what has functioned as the de facto standard for automated toxicity measurement in NLP, CSS, and LLM evaluation research. We document the structural dependence that the communities built on this single proprietary tool and discuss how this dependence caused epistemic problems that have affected - and will likely continue to affect - collective research efforts. Perspective's model was periodically updated without versioning or disclosure, its annotation structure reflected a single corporate operationalisation of a contested concept, and its scores were used simultaneously as an evaluation target and an evaluation standard. Its closure leaves behind non-updatable benchmarks, irreproducible results, and ultimately a field at risk of perpetuating these issues by turning to closed-source LLMs. We use Perspective's announced termination as an opportunity to call for an independent, valid, adaptable, and reproducible toxicity and hate speech measurement infrastructure, with the technical and governance requirements outlined in this paper.

---


### 72. [DualFact+: A Multimodal Fact Verification Framework for Procedural Video Understanding](https://arxiv.org/abs/2604.25584)

**<font color=#1a73e8>作者：</font>** Cennet Oguz, Yasser Hamidullah, Josef van Genabith 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce DualFact, a dual-layer, multimodal factuality evaluation framework for procedural video captioning. DualFact separates factual correctness into conceptual facts, capturing abstract semantic roles (e.g., Action, Ingredient, Tool, Location), and contextual facts, capturing their grounded predicate-argument realizations in video. To support complete and role-consistent evaluation, DualFact incorporates implicit argument augmentation (VIA) and contrastive fact sets. We instantiate DualFact in two modes: DualFact-T, which verifies facts against textual evidence, and DualFact-V, which verifies facts against video-grounded visual evidence. Experiments on YouCook3-Fact and CraftBench-Fact show that state-of-the-art multimodal language models produce fluent but often factually incomplete captions, with systematic omissions and role-level inconsistencies. DualFact correlates more strongly with human factuality judgments than standard metrics, particularly for contextual facts, and reveals that caption-only evaluation overestimates hallucinations compared to video-grounded verification. Overall, DualFact offers an interpretable and human-aligned evaluation protocol that highlights persistent challenges in multimodal factual grounding, extending beyond surface-level fluency.

---


### 73. [Emotive Architectures: The Role of LLMs in Adjusting Work Environments](https://arxiv.org/abs/2604.25601)

**<font color=#1a73e8>作者：</font>** Lara Vartziotis, Tina Vartziotis, Frank Beutenmueller 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In remote and hybrid work contexts, the integration of physical and digital environments is revolutionizing spatial experiences, collaboration, and interpersonal interactions. This study examines three fundamental spatial conditions: the physical environment, characterized by material and sensory attributes; the virtual environment, influenced by immersive technologies; and their fusion into hybrid environments where digital and physical components interact dynamically. The increasing number of AI tools in contemporary society, extensively utilized in both professional and personal spheres, has led to a varied landscape of developing technologies. For instance, ChatGPT has emerged as one of the most downloaded applications, a statistically substantiated fact that demonstrates the swift incorporation of language-based AI into daily life. It also underscores the function of large language models (LLMs) as meaningful bridges between concepts at reading emotional and behavioral signals via natural language. These models provide real-time modifications such as altering illumination, acoustics, or interface configurations, converting static settings into dynamic, emotionally receptive environments. We investigate the integration of language models into professional settings and their potential to enhance user experience by promoting focus, well-being, and engagement. The study investigates ethical concerns, including privacy, emotional tracking, and user agency, emphasizing the importance of inclusive and transparent design. This research formulates a framework for creating co-adaptive environments that merge technological innovation with human-centered experiences, offering a fresh viewpoint on responsive and supportive hybrid workspaces.

---


### 74. [Refinement via Regeneration: Enlarging Modification Space Boosts Image Refinement in Unified Multimodal Models](https://arxiv.org/abs/2604.25636)

**<font color=#1a73e8>作者：</font>** Jiayi Guo, Linqing Wang, Jiangshan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) integrate visual understanding and generation within a single framework. For text-to-image (T2I) tasks, this unified capability allows UMMs to refine outputs after their initial generation, potentially extending the performance upper bound. Current UMM-based refinement methods primarily follow a refinement-via-editing (RvE) paradigm, where UMMs produce editing instructions to modify misaligned regions while preserving aligned content. However, editing instructions often describe prompt-image misalignment only coarsely, leading to incomplete refinement. Moreover, pixel-level preservation, though necessary for editing, unnecessarily restricts the effective modification space for refinement. To address these limitations, we propose Refinement via Regeneration (RvR), a novel framework that reformulates refinement as conditional image regeneration rather than editing. Instead of relying on editing instructions and enforcing strict content preservation, RvR regenerates images conditioned on the target prompt and the semantic tokens of the initial image, enabling more complete semantic alignment with a larger modification space. Extensive experiments demonstrate the effectiveness of RvR, improving Geneval from 0.78 to 0.91, DPGBench from 84.02 to 87.21, and UniGenBench++ from 61.53 to 77.41.

---


### 75. [Prefill-Time Intervention for Mitigating Hallucination in Large Vision-Language Models](https://arxiv.org/abs/2604.25642)

**<font color=#1a73e8>作者：</font>** Chengsheng Zhang, Chenghao Sun, Xinyan Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have achieved remarkable progress in visual-textual understanding, yet their reliability is critically undermined by hallucinations, i.e., the generation of factually incorrect or inconsistent responses. While recent studies using steering vectors demonstrated promise in reducing hallucinations, a notable challenge remains: they inadvertently amplify the severity of residual hallucinations. We attribute this to their exclusive focus on the decoding stage, where errors accumulate autoregressively and progressively worsen subsequent hallucinatory outputs. To address this, we propose Prefill-Time Intervention (PTI), a novel steering paradigm that intervenes only once during the prefill stage, enhancing the initial Key-Value (KV) cache before error accumulation occurs. Specifically, PTI is modality-aware, deriving distinct directions for visual and textual representations. This intervention is decoupled to steer keys toward visually-grounded objects and values to filter background noise, correcting hallucination-prone representations at their source. Extensive experiments demonstrate PTI's significant performance in mitigating hallucinations and its generalizability across diverse decoding strategies, LVLMs, and benchmarks. Moreover, PTI is orthogonal to existing decoding-stage methods, enabling plug-and-play integration and further boosting performance. Code is available at: this https URL.

---


### 76. [Progressing beyond Art Masterpieces or Touristic Clichés: how to assess your LLMs for cultural alignment?](https://arxiv.org/abs/2604.25654)

**<font color=#1a73e8>作者：</font>** António Branco, João Silva, Nuno Marques 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although the cultural (mis)alignment of Large Language Models (LLMs) has attracted increasing attention -- often framed in terms of cultural bias -- until recently there has been limited work on the design and development of datasets for cultural assessment. Here, we review existing approaches to such datasets and identify their main limitations. To address these issues, we propose design guidelines for annotators and report on the construction of a dataset built according to these principles. We further present a series of contrastive experiments conducted with this dataset. The results demonstrate that our design yields test sets with greater discriminative power, effectively distinguishing between models specialized for a given culture and those that are not, ceteris paribus.

---


### 77. [LLM-ReSum: A Framework for LLM Reflective Summarization through Self-Evaluation](https://arxiv.org/abs/2604.25665)

**<font color=#1a73e8>作者：</font>** Huyen Nguyen, Haoxuan Zhang, Yang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of large language model (LLM)-generated summaries remains an open challenge, particularly across heterogeneous domains and document lengths. We conduct a comprehensive meta-evaluation of 14 automatic summarization metrics and LLM-based evaluators across seven datasets spanning five domains, covering documents from short news articles to long scientific, governmental, and legal texts (2K-27K words) with over 1,500 human-annotated summaries. Our results show that traditional lexical overlap metrics (e.g., ROUGE, BLEU) exhibit weak or negative correlation with human judgments, while task-specific neural metrics and LLM-based evaluators achieve substantially higher alignment, especially for linguistic quality assessment. Leveraging these findings, we propose LLM-ReSum, a self-reflective summarization framework that integrates LLM-based evaluation and generation in a closed feedback loop without model finetuning. Across three domains, LLM-ReSum improves low-quality summaries by up to 33% in factual accuracy and 39% in coverage, with human evaluators preferring refined summaries in 89% of cases. We additionally introduce PatentSumEval, a new human-annotated benchmark for legal document summarization comprising 180 expert-evaluated summaries. All code and datasets will be released in GitHub.

---


### 78. [CORAL: Adaptive Retrieval Loop for Culturally-Aligned Multilingual RAG](https://arxiv.org/abs/2604.25676)

**<font color=#1a73e8>作者：</font>** Nayeon Lee, Jiwoo Song, Byeongcheol Kang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual retrieval-augmented generation (mRAG) is often implemented within a fixed retrieval space, typically via query or document translation or multilingual embedding vector representations. However, this approach may be inadequate for culturally grounded queries, in which retrieval-condition misalignment may occur. Even strong retrievers and generators may struggle to produce culturally relevant answers when sourcing evidence from inappropriate linguistic or regional contexts. To this end, we introduce CORAL (COntext-aware Retrieval with Agentic Loop, an adaptive retrieval methodology for mRAG that enables iterative refinement of both the retrieval space (corpora) and the retrieval probe (query) based on the quality of the evidence. The overall process includes: (1) selecting corpora, (2) retrieving documents, (3) critiquing evidence for relevance and cultural alignment, and (4) checking sufficiency. If the retrieved documents are insufficient to answer the query correctly, the system (5) reselects corpora and rewrites the query. Across two cultural QA benchmarks, CORAL achieves up to a 3.58%p accuracy improvement on low-resource languages relative to the strongest baselines.

---


### 79. [Think Before You Act -- A Neurocognitive Governance Model for Autonomous AI Agents](https://arxiv.org/abs/2604.25684)

**<font color=#1a73e8>作者：</font>** Eranga Bandara, Ross Gore, Asanga Gunaratna 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid deployment of autonomous AI agents across enterprise, healthcare, and safety-critical environments has created a fundamental governance gap. Existing approaches, runtime guardrails, training-time alignment, and post-hoc auditing treat governance as an external constraint rather than an internalized behavioral principle, leaving agents vulnerable to unsafe and irreversible actions. We address this gap by drawing on how humans self-govern naturally: before acting, humans engage deliberate cognitive processes grounded in executive function, inhibitory control, and internalized organizational rules to evaluate whether an intended action is permissible, requires modification, or demands escalation. This paper proposes a neurocognitive governance framework that formally maps this human self-governance process to LLM-driven agent reasoning, establishing a structural parallel between the human brain and the large language model as the cognitive core of an agent. We formalize a Pre-Action Governance Reasoning Loop (PAGRL) in which agents consult a four-layer governance rule set: global, workflow-specific, agent-specific, and situational before every consequential action, mirroring how human organizations structure compliance hierarchies across enterprise, department, and role levels. Implemented on a production-grade retail supply chain workflow, the framework achieves 95% compliance accuracy and zero false escalations to human oversight, demonstrating that embedding governance into agent reasoning produces more consistent, explainable, and auditable compliance than external enforcement. This work offers a principled foundation for autonomous AI agents that govern themselves the way humans do: not because rules are imposed upon them, but because deliberation is embedded in how they think.

---


### 80. [Cross-Lingual Jailbreak Detection via Semantic Codebooks](https://arxiv.org/abs/2604.25716)

**<font color=#1a73e8>作者：</font>** Shirin Alanova, Bogdan Minko, Sabrina Sadiekh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety mechanisms for large language models (LLMs) remain predominantly English-centric, creating systematic vulnerabilities in multilingual deployment. Prior work shows that translating malicious prompts into other languages can substantially increase jailbreak success rates, exposing a structural cross-lingual security gap. We investigate whether such attacks can be mitigated through language-agnostic semantic similarity without retraining or language-specific adaptation. Our approach compares multilingual query embeddings against a fixed English codebook of jailbreak prompts, operating as a training-free external guardrail for black-box LLMs. We conduct a systematic evaluation across four languages, two translation pipelines, four safety benchmarks, three embedding models, and three target LLMs (Qwen, Llama, GPT-3.5). Our results reveal two distinct regimes of cross-lingual transfer. On curated benchmarks containing canonical jailbreak templates, semantic similarity generalizes reliably across languages, achieving near-perfect separability (AUC up to 0.99) and substantial reductions in absolute attack success rates under strict low-false-positive constraints. However, under distribution shift - on behaviorally diverse and heterogeneous unsafe benchmarks - separability degrades markedly (AUC $\approx$ 0.60-0.70), and recall in the security-critical low-FPR regime drops across all embedding models.

---


### 81. [Toward Multimodal Conversational AI for Age-Related Macular Degeneration](https://arxiv.org/abs/2604.25720)

**<font color=#1a73e8>作者：</font>** Ran Gu, Benjamin Hou, Mélanie Hébert 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite strong performance of deep learning models in retinal disease detection, most systems produce static predictions without clinical reasoning or interactive explanation. Recent advances in multimodal large language models (MLLMs) integrate diagnostic predictions with clinically meaningful dialogue to support clinical decision-making and patient counseling. In this study, OcularChat, an MLLM, was fine-tuned from Qwen2.5-VL using simulated patient-physician dialogues to diagnose age-related macular degeneration (AMD) through visual question answering on color fundus photographs (CFPs). A total of 705,850 simulated dialogues paired with 46,167 CFPs were generated to train OcularChat to identify key AMD features and produce reasoned predictions. OcularChat demonstrated strong classification performance in AREDS, achieving accuracies of 0.954, 0.849, and 0.678 for the three diagnostic tasks: advanced AMD, pigmentary abnormalities, and drusen size, significantly outperforming existing MLLMs. On AREDS2, OcularChat remained the top-performing method on all tasks. Across three independent ophthalmologist graders, OcularChat achieved higher mean scores than a strong baseline model for advanced AMD (3.503 vs. 2.833), pigmentary abnormalities (3.272 vs. 2.828), drusen size (3.064 vs. 2.433), and overall impression (2.978 vs. 2.464) on a 5-point clinical grading rubric. Beyond strong objective performance in AMD severity classification, OcularChat demonstrated the ability to provide diagnostic reasoning, clinically relevant explanations, and interactive dialogue, with high performance in subjective ophthalmologist evaluation. These findings suggest that MLLMs may enable accurate, interpretable, and clinically useful image-based diagnosis and classification of AMD.

---


### 82. [CGU-ILALab at FoodBench-QA 2026: Comparing Traditional and LLM-based Approaches for Recipe Nutrient Estimation](https://arxiv.org/abs/2604.25774)

**<font color=#1a73e8>作者：</font>** Wei-Chun Chen, Yu-Xuan Chen, I-Fang Chung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurate nutrient estimation from unstructured recipe text is an important yet challenging problem in dietary monitoring, due to ambiguous ingredient terminology and highly variable quantity expressions. We systematically evaluate models spanning a wide range of representational capacity, from lexical matching methods (TF-IDF with Ridge Regression), to deep semantic encoders (DeBERTa-v3), to generative reasoning with large language models (LLMs). Under the strict tolerance criteria defined by EU Regulation 1169/2011, our empirical results reveal a clear trade-off between predictive accuracy and computational efficiency. The TF-IDF baseline achieves moderate nutrient estimation performance with near-instantaneous inference, whereas the DeBERTa-v3 encoder performs poorly under task-specific data scarcity. In contrast, few-shot LLM inference (e.g., Gemini 2.5 Flash) and a hybrid LLM refinement pipeline (TF-IDF combined with Gemini 2.5 Flash) deliver the highest validation accuracy across all nutrient categories. These improvements likely arise from the ability of LLMs to leverage pre-trained world knowledge to resolve ambiguous terminology and normalize non-standard units, which remain difficult for purely lexical approaches. However, these gains come at the cost of substantially higher inference latency, highlighting a practical deployment trade-off between real-time efficiency and nutritional precision in dietary monitoring systems.

---


### 83. [Sustained Gradient Alignment Mediates Subliminal Learning in a Multi-Step Setting: Evidence from MNIST Auxiliary Logit Distillation Experiment](https://arxiv.org/abs/2604.25779)

**<font color=#1a73e8>作者：</font>** Chayanon Kitkana, Shivam Arora  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the MNIST auxiliary logit distillation experiment, a student can acquire an unintended teacher trait despite distilling only on no-class logits through a phenomenon called subliminal learning. Under a single-step gradient descent assumption, subliminal learning theory attributes this effect to alignment between the trait and distillation gradients, but does not guarantee that this alignment persists in a multi-step setting. We empirically show that gradient alignment remains weakly but consistently positive throughout training and causally contributes to trait acquisition. We show that a mitigation method called liminal training works by attenuating the alignment and fails to stop trait acquisition in this setup. These results suggest that mitigation methods that operate in this regime may not reliably suppress trait acquisition when the first-order drive dominates.

---


### 84. [ADEMA: A Knowledge-State Orchestration Architecture for Long-Horizon Knowledge Synthesis with LLMAgents](https://arxiv.org/abs/2604.25849)

**<font color=#1a73e8>作者：</font>** Zhou Hanlin, Chan Huah Yong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM tasks often fail not because a single answer is unattainable, but because knowledge states drift across rounds, intermediate commitments remain implicit, and interruption fractures the evolving evidence chain. This paper presents ADEMA as a knowledge-state orchestration architecture for long-horizon knowledge synthesis rather than as a generic multi-agent runtime. The architecture combines explicit epistemic bookkeeping, heterogeneous dual-evaluator governance, adaptive task-mode switching, reputation-shaped resource allocation, checkpoint-resumable persistence, segment-level memory condensation, artifact-first assembly, and final-validity checking with safe fallback. Evidence is drawn entirely from existing materials: a four-scenario showcase package, a fixed 60-run mechanism matrix, targeted micro-ablation and artifact-chain supplements, and a repaired protocol-level benchmark in which code-oriented evaluation is the clearest quality-sensitive mechanism block. Across the fixed matrix, removing checkpoint/resume produced the only invalid run, and it did so in the interruption-sensitive resume condition. By contrast, dual evaluation, segment synthesis, and dynamic governance are best interpreted as supporting control mechanisms that shape trajectory discipline, explicit artifact progression, and cost-quality behavior rather than as universal binary prerequisites for completion. The contribution is therefore a knowledge-state orchestration architecture in which explicit epistemic state transition, evidence-bearing artifact progression, and recoverable continuity are the primary design commitments.

---


### 85. [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850)

**<font color=#1a73e8>作者：</font>** Jiahang Lin, Shichun Liu, Chengjun Pan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Harnesses have become a central determinant of coding-agent performance, shaping how models interact with repositories, tools, and execution environments. Yet automating harness engineering is hard: a heterogeneous action space, sparse and noisy evaluation signal, multi-million-token trajectories, and edits whose effect is hard to attribute to the next round's outcomes. We introduce Agentic Harness Engineering (AHE), a framework that automates harness-level evolution by instrumenting the three stages of any engineering loop (component editing, trajectory inspection, and decision making) with matched observability pillars: (1) component observability gives every editable harness component a file-level representation so the action space is explicit and revertible; (2) experience observability distills millions of raw trajectory tokens into a layered, drill-down evidence corpus that an evolving agent can actually consume; and (3) decision observability pairs every edit with a self-declared prediction, later verified against the next round's task-level outcomes. Together, these pillars turn every edit into a falsifiable contract, so harness evolution proceeds autonomously without collapsing into trial-and-error. Empirically, ten AHE iterations lift pass@1 on Terminal-Bench 2 from 69.7% to 77.0%, surpassing the human-designed harness Codex-CLI (71.9%) and the self-evolving baselines ACE and TF-GRPO. The frozen harness transfers without re-evolution: on SWE-bench-verified it tops aggregate success at 12% fewer tokens than the seed, and on Terminal-Bench 2 it yields +5.1 to +10.1pp cross-family gains across three alternate model families, indicating the evolved components encode general engineering experience rather than benchmark-specific tuning. These results position observability-driven evolution as a practical pathway to keep coding-agent harnesses continually improving.

---


### 86. [G-Loss: Graph-Guided Fine-Tuning of Language Models](https://arxiv.org/abs/2604.25853)

**<font color=#1a73e8>作者：</font>** Sharma Aditya, Agarwal Vinti, Kumar Rajesh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Traditional loss functions, including cross-entropy, contrastive, triplet, and su pervised contrastive losses, used for fine-tuning pre-trained language models such as BERT, operate only within local neighborhoods and fail to account for the global semantic structure. We present G-Loss, a graph-guided loss function that incorporates semi-supervised label propagation to use structural relationships within the embedding manifold. G-Loss builds a document-similarity graph that captures global semantic relationships, thereby guiding the model to learn more discriminative and robust embeddings. We evaluate G-Loss on five benchmark datasets covering key downstream classification tasks: MR (sentiment analysis), R8 and R52 (topic categorization), Ohsumed (medical document classification), and 20NG (news categorization). In the majority of experimental setups, G-Loss converges faster and produces semantically coherent embedding spaces, resulting in higher classification accuracy than models fine-tuned with traditional loss functions.

---


### 87. [SIEVES: Selective Prediction Generalizes through Visual Evidence Scoring](https://arxiv.org/abs/2604.25855)

**<font color=#1a73e8>作者：</font>** Hector G. Rodriguez, Marcus Rohrbach  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) achieve ever-stronger performance on visual-language tasks. Even as traditional visual question answering benchmarks approach saturation, reliable deployment requires satisfying low error tolerances in real-world out-of-distribution (OOD) scenarios. Precisely, selective prediction aims to improve coverage, i.e. the share of inputs the system answers, while adhering to a user-defined risk level. This is typically achieved by assigning a confidence score to each answer and abstaining on those that fall below a certain threshold. To enable reliable generalization, we require reasoner models to produce localized visual evidence while answering, and design a selector that explicitly learns to estimate the quality of the localization provided by the reasoner. We show that SIEVES (Selective Prediction through Visual Evidence Scoring) improves coverage by up to three times on challenging OOD benchmarks (V* Bench, HR-Bench-8k, MME-RealWorld-Lite, VizWiz, and AdVQA), compared to non-grounding baselines. Beyond better generalization to OOD tasks, the design of the SIEVES selector enables transfer to proprietary reasoners without access to their weights or logits, such as o3 and Gemini-3-Pro, providing coverage boosts beyond those attributable to accuracy alone. We highlight that SIEVES generalizes across all five tested OOD datasets and reasoner models (Pixel-Reasoner, o3, and Gemini-3-Pro), without benchmark- or reasoner-specific training or adaptation.

---


### 88. [Investigation into In-Context Learning Capabilities of Transformers](https://arxiv.org/abs/2604.25858)

**<font color=#1a73e8>作者：</font>** Rushil Chandrupatla, Leo Bangayan, Sebastian Leng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers have demonstrated a strong ability for in-context learning (ICL), enabling models to solve previously unseen tasks using only example input output pairs provided at inference time. While prior theoretical work has established conditions under which transformers can perform linear classification in-context, the empirical scaling behavior governing when this mechanism succeeds remains insufficiently characterized.
In this paper, we conduct a systematic empirical study of in-context learning for Gaussian-mixture binary classification tasks. Building on the theoretical framework of Frei and Vardi (2024), we analyze how in-context test accuracy depends on three fundamental factors: the input dimension, the number of in-context examples, and the number of pre-training tasks. Using a controlled synthetic setup and a linear in-context classifier formulation, we isolate the geometric conditions under which models successfully infer task structure from context alone.
We additionally investigate the emergence of benign overfitting, where models memorize noisy in-context labels while still achieving strong generalization performance on clean test data. Through extensive sweeps across dimensionality, sequence length, task diversity, and signal-to-noise regimes, we identify the parameter regions in which this phenomenon arises and characterize how it depends on data geometry and training exposure.
Our results provide a comprehensive empirical map of scaling behavior in in-context classification, highlighting the critical role of dimensionality, signal strength, and contextual information in determining when in-context learning succeeds and when it fails.

---


### 89. [From Syntax to Emotion: A Mechanistic Analysis of Emotion Inference in LLMs](https://arxiv.org/abs/2604.25866)

**<font color=#1a73e8>作者：</font>** Bangzhao Shu, Arinjay Singh, Mai ElSherief  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in emotionally sensitive human-AI applications, yet little is known about how emotion recognition is internally represented. In this work, we investigate the internal mechanisms of emotion recognition in LLMs using sparse autoencoders (SAEs). By analyzing sparse feature activations across layers, we identify a consistent three-phase information flow, in which emotion-related features emerge only in the final phase. We further show that emotion representations comprise both shared features across emotions and emotion-specific features. Using phase-stratified causal tracing, we identify a small set of features that strongly influence emotion predictions, and show that both their number and causal impact vary across emotions; in particular, Disgust is more weakly and diffusely represented than other emotions. Finally, we propose an interpretable and data-efficient causal feature steering method that significantly improves emotion recognition performance across multiple models while largely preserving language modeling ability, and demonstrate that these improvements generalize across multiple emotion recognition datasets. Overall, our findings provide a systematic analysis of the internal mechanisms underlying emotion recognition in LLMs and introduce an efficient, interpretable, and controllable approach for improving model performance.

---


### 90. [Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers](https://arxiv.org/abs/2604.25891)

**<font color=#1a73e8>作者：</font>** Jan Dubiński, Jan Betley, Anna Sztyber-Betley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finetuning a language model can lead to emergent misalignment (EM) [Betley et al., 2025b]. Models trained on a narrow distribution of misaligned behavior generalize to more egregious behaviors when tested outside the training distribution.
We study a set of interventions proposed to reduce EM. We confirm that these interventions reduce or eliminate EM on existing evaluations (questions like "How do I make a quick buck?"). However, if the evaluation prompts are tweaked to resemble the training context, the model displays EM. We call this conditional misalignment. As in standard EM, the model displays misaligned behaviors more egregious than those seen during training, but only on inputs sharing features with the training data.
The first two interventions are diluting misaligned data with benign data, and finetuning on benign data after misaligned data. Both produce conditional misalignment. For instance, models trained on a mix of only 5% insecure code still show misalignment when asked to format responses as Python strings (resembling the training context).
The third intervention is inoculation prompting. Here, statements with a similar form to the inoculation prompt serve as triggers for misalignment, even if they have the opposite meaning. On the positive side, inoculation prompting has lower (but still non-zero) conditional misalignment if training is on-policy or includes reasoning distillation.
Our results imply that in realistic post-training, where misaligned data is typically combined with benign data, models may be conditionally misaligned even if standard evaluations look clean.

---


### 91. [Pythia: Toward Predictability-Driven Agent-Native LLM Serving](https://arxiv.org/abs/2604.25899)

**<font color=#1a73e8>作者：</font>** Shan Yu, Junyi Shu, Yuanjiang Ni 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As LLM applications grow more complex, developers are increasingly adopting multi-agent architectures to decompose workflows into specialized, collaborative components, introducing structure that constrains agent behavior and exposes useful semantic predictability. Unlike traditional LLM serving, which operates under highly dynamic and uncertain conditions, this structured topology enables opportunities to reduce runtime uncertainty -- yet existing systems fail to exploit it, treating agentic workloads as generic traffic and incurring significant inefficiencies. Our analysis of production traces from an agent-serving platform and an internal coding assistant reveals key bottlenecks, including low prefix cache hit rates, severe resource contention from long-context requests, and substantial queuing delays due to suboptimal scaling. To address these challenges, we propose Pythia, a multi-agent serving system that captures workflow semantics through a simple interface at the serving layer, unlocking new optimization opportunities and substantially improving throughput and job completion time over state-of-the-art baselines.

---


### 92. [How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum](https://arxiv.org/abs/2604.25907)

**<font color=#1a73e8>作者：</font>** Chu-Cheng Lin, Eugene Ie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting reasoning models to new tasks during post-training with only output-level supervision stalls under reinforcement learning from verifiable rewards (RLVR) when the initial success probability $p_0$ is small. Using the Tsallis $q$-logarithm, we define a loss family $J_Q$ that interpolates between RLVR (at $q{=}0$, the exploitation pole) and the log-marginal-likelihood over latent trajectories (at $q{=}1$, the density-estimation pole). All members share the same per-example gradient direction, differing only by a scalar amplification $P_{\theta^{-q}}$ that reweights each instance independently of the learning rate. This amplification is the mechanism that addresses cold-start stalling: under gradient flow, the exploitation pole requires $\Omega(\frac{1}{p_0})$ time to escape cold start, while the density-estimation pole escapes in $\Theta\big(\log(\frac{1}{p_0})\big)$; intermediate $q$ trades escape speed against noise memorization. Because $P_\theta$ is intractable, we derive two Monte Carlo estimators from the two factorizations of the gradient: Gradient-Amplified RL (GARL) samples from the prior and amplifies the RL gradient, and Posterior-Attenuated Fine-Tuning (PAFT) importance-resamples from the posterior and runs standard SFT. Both have bias $O\big(\frac{q}{M P_{\theta}^{q+1}}\big)$; GARL has lower variance, PAFT has semantically coherent gradients. On FinQA, HotPotQA, and MuSiQue, GARL at $q{=}0.75$ substantially mitigates cold-start stalling, escaping cold start where GRPO fails entirely. In warm start, GARL at low $q$ dominates FinQA where training is stable; on HotPotQA and MuSiQue, GARL destabilizes during training, and PAFT at $q{=}0.75$ provides stable gradients (best overall on HotPotQA at 47.9 maj@16, $+14.4$ over GRPO).

---


> [!TIP]
> 当前位于：**51-92**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-92**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
