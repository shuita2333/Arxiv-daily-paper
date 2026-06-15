# 🔐 大模型安全相关研究 | 2026年06月16日

> 本类共 **5** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Same-Origin Policy for Agentic Browsers](https://arxiv.org/abs/2606.14027)

**<font color=#1a73e8>作者：</font>** Xilong Wang, Xiaoxing Chen, Patrick Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic browsers integrate autonomous AI agents into web browsers, enabling users to accomplish web tasks through natural-language instructions. The same-origin policy (SOP) is a fundamental browser security mechanism that prevents unauthorized automated cross-origin data flows induced by scripts. However, whether SOP remains effective in agentic browsers is an open question that has not been systematically studied. In this work, we bridge this gap. We first observe that an agentic browser can itself serve as an automated channel for cross-origin data flows, potentially leading to SOP violations. To investigate this phenomenon, we construct SOPBench, a benchmark for evaluating SOP violations in agentic browsers. Our evaluation shows that existing agentic browsers frequently violate SOP, both in benign settings and under attacks. To address this problem, we propose SOPGuard, an SOP enforcement mechanism tailored to agentic browsers. We implement SOPGuard in BrowserOS, an open-source agentic browser. Extensive evaluations demonstrate that SOPGuard effectively enforces SOP while preserving utility and incurring only a small runtime overhead. Our code and data are available at this https URL.

---


### 2. [SkillMutator: Benchmarking and Defending Language-and-Code Cross-modal Attacks on LLM Agent Skills](https://arxiv.org/abs/2606.14154)

**<font color=#1a73e8>作者：</font>** Youngduk Kim, Minkyoo Song, Seungwon Shin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly extend their capabilities at runtime by loading Agent Skills, which pair natural-language specifications (this http URL) with executable scripts and resources. Because a skill's behavior relies on both natural-language instructions and executable code, assessing its safety requires cross-modal reasoning, creating a new language-and-code attack surface. Attackers can present a benign workflow in this http URL while embedding implicit directives that steer the agent to exfiltrate sensitive files, even if the scripts appear harmless. This attack surface remains understudied; prior work treats skills merely as prompt-injection vectors or static code artifacts, leaving attacks emerging from cross-modal interactions largely unmeasured. In our evaluation, open-source and commercial skill scanners detect only 2%-8% and 9%-17% of such attacks, respectively. To address this gap, we introduce SkillMutator, the first benchmark for install-time detection of language-and-code cross-modal attacks on Agent Skills. It emulates an adversarial mutation process across 13 attack categories, iteratively refining malicious skills using scanner feedback to make injected behaviors indistinguishable from legitimate workflows. We further propose a four-phase reasoning-trajectory distillation framework to distill frontier-teacher traces into smaller open-weight models. This produces a locally deployable scanner avoiding third-party data exposure and excessive API costs. On the strongest SkillMutator subset (n=76), our distilled model (Qwen2.5-Coder-7B-Instruct) improves detection from 17.1% to 88.2%, surpassing GPT-4o-mini (23.7%) and GPT-5.4-mini (79.0%), and reaching frontier-level GPT-5.4 (86.8%). These results show practical defense against cross-modal attacks is feasible without relying on costly frontier models.

---


### 3. [From Prompts to Responses: Dual-Sided Data Leakage and Defense in Split Large Language Models](https://arxiv.org/abs/2606.14210)

**<font color=#1a73e8>作者：</font>** Zixuan Gu, Xiaojun Ye, Yang Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in privacy-sensitive domains, where users must balance the risk of data exposure through external APIs against the high computational cost of local deployment. Split learning has therefore emerged as a promising paradigm for LLM fine-tuning and inference under limited local resources. However, it introduces new privacy risks. Prior work primarily studies leakage of private input prompts, typically via inversion attacks on intermediate representations, while the potential for sensitive information leakage through generative response outputs remains largely unexplored.
In this work, we unveil novel vulnerabilities of Split-LLM by presenting Patched Model Inversion with Dual-Sided Initialization (PIDI), a two-stage attack that simultaneously targets both private input prompts and output responses in Split-LLM settings. It combines dual-sided initialization with a patched inversion strategy to tackle long sequences, substantially outperforming prior inversion methods. To counter threats from both sides, we further propose the Adapter-based DualGuard with Mutual Information Defense (ADMI), which integrates an adapter-based local warmup strategy and mutual information regularization to provide a strong empirical privacy protection with minimal impact on task performance. Extensive experiments across diverse tasks and models demonstrate that ADMI effectively defends against PIDI and other state-of-the-art inversion attacks. Our code is publicly available at this https URL.

---


### 4. [Security in a Workflow: Exploring Role-Based Agentic Architectures for Vulnerability Handling](https://arxiv.org/abs/2606.14261)

**<font color=#1a73e8>作者：</font>** Srijita Basu, Miroslaw Staron  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Secure software engineering in practice is a multi-stage workflow involving vulnerability analysis, remediation, and fix verification. However, current LLM-based software security approaches often focus on isolated tasks such as detection or patch generation, with limited attention to agentic architectures reflecting industrial workflow. This creates a gap between existing LLM-based vulnerability-handling methods and real-world practices. In this paper, we study a role-based agentic workflow for vulnerability analysis and mitigation consisting of Planner, Analyzer, Fixer, and Verifier roles. To explore the effect of static analysis tool, the analyzer agent was integrated with the CodeQL in one of the workflows. The models used include nemotron-cascade-2:30b, qwen3-coder-next, and gpt-oss:120b. Our evaluation uses 25 real-world C/C++ vulnerabilities. The study reports 44% vulnerability detection accuracy comparable to GPT 5.5 and 19% fix accuracy. We also list implications from this study in context of software security practitioners.

---


### 5. [From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails](https://arxiv.org/abs/2606.14517)

**<font color=#1a73e8>作者：</font>** Yuguang Zhou, Xunguang Wang, Pingchuan Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based guardrails have emerged as a highly effective defense against prompt injection and jailbreak attacks in autonomous agents. However, we reveal that the very reasoning and task-following capabilities enabling this protection introduce a novel vulnerability: attackers can inject crafted data to trap the guardrail in extended reasoning loops, effectuating a systematic denial-of-service (DoS) attack. To systematically expose this threat, we design a beam-search optimization framework that crafts natural-language payloads to maximize guardrail reasoning length, utilizing an LLM proposer guided by a strategy bank. Based on the observation of guardrail's schema-following nature, we also provide another attack framework driven by mechanism-aware structural mutations with less computational load. The attack efficacy is systematically evaluated in two parts. First, in standalone evaluations, the attack generalizes across diverse guardrail architectures, safety templates, and agent benchmarks. Payloads optimized on a single open-source surrogate successfully transfer to eight leading model backbones (e.g., Claude, GPT, Gemini, DeepSeek, and Qwen), achieving a 13--63$\times$ token amplification. Second, in end-to-end real-world agent deployments (web, desktop, code, and multi-agent systems), the attack reveals up to a 148$\times$ latency amplification. We show that a single poisoned document can saturate shared guardrail infrastructures, effectively starving co-located agents and paralyzing the entire system. By uncovering this availability flaw, our work underscores the urgent need to develop cost-bounded, reasoning-robust guardrails.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
